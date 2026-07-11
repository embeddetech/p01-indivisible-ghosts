"""
Multidimensional deficiency analysis for the malicious ghost
(rigorous layer for the explosion dictionary; see notes.md for the
theorems and full proofs).

WHY 1D IS NOT ENOUGH. In n >= 2 the naive dictionary "classical
incompleteness <=> quantum non-self-adjointness" FAILS in general
(Rauch & Reed, Commun. Math. Phys. 29, 105 (1973)). The correct
multidimensional structure is CHANNEL-WISE:

THEOREM A (channel additivity of deficiency). H = h1 (x) 1 + 1 (x) h_perp
on L^2(R x R^m), with h1 = p^2/2 + V1, V1 super-quadratically falling
(finite classical time of flight), and h_perp self-adjoint with
eigenbasis {phi_n, E_n}. Weyl's limit-circle property is independent of
the spectral parameter z, so for EVERY channel n, every solution u of
(h1 - (+-i - E_n))u = 0 is L^2, and u (x) phi_n lies in ker(H* -+ i).
Orthogonality across n gives deficiency indices (inf, inf): the
conservative completions carry an S-MATRIX AT INFINITY -- an
infinite-dimensional, channel-mixing reflection law.

THEOREM D (non-separable, rigorous). Adding a BOUNDED channel-mixing
coupling mu f(x1) g(x2) preserves the deficiency indices exactly (Kato
stability under bounded symmetric perturbations), so infinite deficiency
survives genuine non-separability. (The physical unbounded couplings,
e.g. lambda x1^2 x2^2, remain open.)

THEOREM C (quadratic ghosts rigorously safe). Any at-most-quadratic
Hamiltonian -- the indefinite cascade at ANY coupling, the free PU
Ostrogradski operator -- is essentially self-adjoint (Nelson's
analytic-vector theorem on the Hermite span): instability never breaks
uniqueness or conservativity. Transient /= explosive, now rigorous.

THIS SCRIPT verifies the quantitative fingerprints of Theorems A and D
on the M-channel model (M = 4 transverse oscillator channels, escape
potential V1 = -|x|^{5/2}, bounded coupling mu tanh(x1) x2^2/(1+x2^2/10)),
whose deficiency indices are (2M, 2M) by the theorems:

 N1  Channel additivity of the spectrum: with the wall regulator at L,
     the number of levels in an energy window equals the CHANNEL SUM of
     the 1D semiclassical counts  sum_n Int T_cross(E - E_n, L)/pi dE
     (the multichannel version of the V2 spacing law), and at mu = 0 the
     spectrum is exactly the union of shifted 1D ladders.
 N2  Kato stability made visible: switching on the bounded coupling
     (mu = 0 -> 0.2) shifts individual levels but leaves the window
     count / level density unchanged.
 N3  The S-matrix at infinity: a channel-0 packet slides out, reflects
     off the regulator ("infinity"), and RETURNS IN A MIXTURE OF
     CHANNELS; the returned channel content depends on the regulator
     position (L = 6 vs 9) -- the completion carries channel data that
     is not in H. The only completion-independent object remains the
     minimal explosive process.

Run:  python -u deficiency_multiD.py    (~2-3 minutes)
"""

import functools
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
from scipy.integrate import quad
import scipy.fft as sfft

print = functools.partial(print, flush=True)

M = 4                       # transverse channels kept
ALPHA = 2.5                 # escape potential -|x|^alpha, alpha > 2
MU = 0.2                    # bounded channel-mixing strength


def V1(x):
    return -np.abs(x) ** ALPHA


def g(x):
    return x ** 2 / (1 + 0.1 * x ** 2)      # bounded: sup = 10


# ----------------------------------------------------------------------
# 0. transverse oscillator basis and the bounded mixing matrix
# ----------------------------------------------------------------------
def transverse():
    n1, l1 = 1600, 9.0
    dx1 = 2 * l1 / (n1 + 1)
    x1 = -l1 + dx1 * np.arange(1, n1 + 1)
    A = (np.diag(1.0 / dx1 ** 2 + 0.5 * x1 ** 2)
         + np.diag(np.full(n1 - 1, -0.5 / dx1 ** 2), 1)
         + np.diag(np.full(n1 - 1, -0.5 / dx1 ** 2), -1))
    w, v = np.linalg.eigh(A)
    B = v[:, :M].T @ (np.tanh(x1)[:, None] * v[:, :M])
    return w[:M], 0.5 * (B + B.T)


EN, B0 = transverse()
print("transverse channel energies:", np.round(EN, 4),
      "(harmonic ladder n + 1/2)")
print("mixing matrix <n|tanh x1|m> (odd: couples n <-> n+-1):\n",
      np.round(B0, 4))

# ----------------------------------------------------------------------
# N1 + N2. Channel additivity of the wall-regularized spectrum
# ----------------------------------------------------------------------
DX = 8e-3


def multichannel_spectrum(L, mu, k=260, sigma=11.0):
    N = int(round(2 * L / DX)) - 1
    x = -L + DX * np.arange(1, N + 1)
    T1 = sparse.diags([np.full(N - 1, -0.5 / DX ** 2),
                       np.full(N, 1.0 / DX ** 2),
                       np.full(N - 1, -0.5 / DX ** 2)], [-1, 0, 1])
    H = (sparse.kron(T1 + sparse.diags(V1(x)), sparse.identity(M))
         + sparse.kron(sparse.identity(N), sparse.diags(EN))
         + sparse.kron(sparse.diags(mu * g(x)), sparse.csr_matrix(B0)))
    vals = eigsh(H.tocsc(), k=k, sigma=sigma, which="LM",
                 return_eigenvectors=False)
    return np.sort(vals)


def channel_sum_count(L, Elo, Ehi):
    total = 0.0
    for En in EN:
        dens = lambda E: 2 * quad(
            lambda x: 1 / np.sqrt(2 * (E - En - V1(x))), 0, L,
            limit=400)[0] / np.pi
        total += quad(dens, Elo, Ehi, limit=200)[0]
    return total


print()
print("=" * 72)
print("N1/N2. Levels in [5, 17] vs channel-sum prediction "
      "sum_n Int T/pi dE")
print("=" * 72)
print(f"{'L':>5} {'mu':>5} {'measured count':>15} {'channel-sum':>12}")
for L in (8.0, 12.0):
    pred = channel_sum_count(L, 5.0, 17.0)
    for mu in (0.0, MU):
        ev = multichannel_spectrum(L, mu)
        assert ev.min() < 5.0 and ev.max() > 17.0, "window not covered"
        cnt = int(np.sum((ev > 5.0) & (ev < 17.0)))
        print(f"{L:>5.1f} {mu:>5.2f} {cnt:>15d} {pred:>12.2f}")
# exact ladder-union check at mu = 0
L = 8.0
N = int(round(2 * L / DX)) - 1
x = -L + DX * np.arange(1, N + 1)
T1 = sparse.diags([np.full(N - 1, -0.5 / DX ** 2),
                   np.full(N, 1.0 / DX ** 2),
                   np.full(N - 1, -0.5 / DX ** 2)], [-1, 0, 1])
ev1 = np.sort(eigsh((T1 + sparse.diags(V1(x))).tocsc(), k=90, sigma=9.0,
                    which="LM", return_eigenvectors=False))
union = np.sort(np.concatenate([ev1 + En for En in EN]))
evm = multichannel_spectrum(L, 0.0, k=200, sigma=11.0)
mid = evm[(evm > 7) & (evm < 15)]
dev = max(np.min(np.abs(union - e)) for e in mid)
print(f"mu=0 exact ladder-union check (L=8, window [7,15]): "
      f"max deviation {dev:.2e}")
print("=> deficiency is CHANNEL-ADDITIVE (Theorem A): each transverse")
print("   channel contributes its own 1D limit-circle ladder; the bounded")
print("   coupling shifts levels but not the count (Theorem D / Kato).")

# ----------------------------------------------------------------------
# N3. The S-matrix at infinity: channel-mixing reflection
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("N3. Reflection from 'infinity' returns a channel MIXTURE whose")
print("    content depends on the regulator (wall) position")
print("=" * 72)


def channel_run(L, dx=8e-3, dt=1e-4, tmax=4.0, x0=2.0, sig=0.5, mu=MU):
    N = int(round(2 * L / dx)) - 1
    x = -L + dx * np.arange(1, N + 1)
    kn = np.pi * np.arange(1, N + 1) / (2 * L)
    kin = np.exp(-1j * kn ** 2 * dt / 2)[:, None]
    Vm = (V1(x)[:, None, None] * np.eye(M)
          + np.eye(M) * EN
          + (mu * g(x))[:, None, None] * B0)
    w, v = np.linalg.eigh(Vm)
    ph = np.exp(-1j * w * dt / 2)

    def apply_V(psi):
        c = np.einsum("inm,in->im", np.conj(v), psi)
        return np.einsum("inm,im->in", v, ph * c)

    psi = np.zeros((N, M), dtype=complex)
    psi[:, 0] = np.exp(-(x - x0) ** 2 / (2 * sig ** 2))
    psi /= np.linalg.norm(psi)
    mask = np.abs(x) < 4.0
    nst = int(round(tmax / dt))
    rec = max(1, nst // 200)
    ts, Pc, Pn = [0.0], [1.0], [np.array([1.0, 0, 0, 0])]
    for s in range(1, nst + 1):
        psi = apply_V(psi)
        psi = sfft.idst(kin * sfft.dst(psi, type=1, axis=0),
                        type=1, axis=0)
        psi = apply_V(psi)
        if s % rec == 0:
            w2 = np.abs(psi) ** 2
            ts.append(s * dt)
            Pc.append(float(w2[mask].sum()))
            Pn.append(w2[mask].sum(axis=0))
    return np.array(ts), np.array(Pc), np.array(Pn)


def t_out(L):
    E = V1(2.0)
    f = lambda u: 2 * u / np.sqrt(2 * (E - V1(2.0 + u * u)))
    return quad(f, 1e-9, np.sqrt(L - 2.0), limit=400)[0]


for L in (6.0, 9.0):
    ts, Pc, Pn = channel_run(L)
    third = len(Pc) // 3
    imin = np.argmin(Pc[:third * 2])
    irev = imin + np.argmax(Pc[imin:])
    frac = Pn[irev] / Pn[irev].sum()
    print(f"L = {L:4.1f}: classical wall arrival t = {t_out(L):.3f} | "
          f"P_center min {Pc[imin]:.3f} at t={ts[imin]:.2f}, revival "
          f"{Pc[irev]:.3f} at t={ts[irev]:.2f}")
    print(f"          returned channel fractions (n=0..3): "
          f"{np.round(frac, 4)}")
print("=> the packet leaves in channel 0 and returns as a MIXTURE; the")
print("   mixture depends on where 'infinity' was regularized. In the")
print("   L -> infinity limit the reflection law is a genuine unitary")
print("   S-matrix at infinity -- extension data, not physics contained")
print("   in H. Completions can scramble the transverse state; only the")
print("   minimal (explosive, sub-stochastic) process is canonical.")
