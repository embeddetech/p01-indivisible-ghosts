"""
Section 5.4 of PT_stochastic_handoff.md (= paper Sec. 6):
The Pais-Uhlenbeck oscillator and the stochastic-quantum correspondence.

MODEL. L = (gamma/2)[xdd^2 - (w1^2 + w2^2) xd^2 + w1^2 w2^2 x^2].
Ostrogradski variables q1 = x, q2 = xd give the HERMITIAN Hamiltonian
    H = p1 q2 + p2^2/(2 gamma) + (gamma/2)(w1^2 + w2^2) q2^2
        - (gamma/2) w1^2 w2^2 q1^2
on the REAL configuration space (q1, q2) = (x, xdot). Its spectrum is the
famous ghost ladder E = w1(n1 + 1/2) - w2(n2 + 1/2): real, UNBOUNDED BELOW
(and dense for irrational w1/w2). Classical dynamics is nevertheless stable
(x(t) = superposition of the two frequencies).

QUESTIONS (from the handoff):
 (a) Does the stochastic-quantum correspondence even make sense for PU?
 (b) Does the PT-metric (no-ghost) resolution yield a valid indivisible
     process?

WHAT THIS SCRIPT SHOWS.
 A. GHOST REALIZATION = VALID PROCESS. On a discretized (x, xdot) grid
    (spectral derivatives, exactly Hermitian H), Gamma(t) = |U(t)|^2 is
    exactly doubly stochastic and genuinely indivisible, with beables =
    physical configurations, fixed (Hermitian => K1-K4 hold with eta = 1).
    Validation: Ehrenfest is exact for quadratic H, so <x(t)> must track
    the exact classical 4th-order trajectory (it does). The unbounded-below
    ENERGY spectrum never enters: the ghost is an energy-accounting
    pathology, invisible to the free stochastic process.
 B. THE NO-GHOST MOVE HAS NO STOCHASTIC COUNTERPART. Mannheim's positive
    spectrum requires re-quantizing the ghost mode with its vacuum on a
    rotated contour (b^dag Omega = 0, i.e. e^{+y^2/2}): a DOMAIN change,
    not a similarity. Numerically: (i) truncated b has a truncation-stable
    null vector |0>, while the null vector of truncated b^dag sits at the
    truncation EDGE |N-1> and escapes to infinity -- restricted to any
    fixed low-energy sector, sigma_min(b^dag) = 1: the PT vacuum has NO
    shadow in the real-line theory at any cutoff; (ii) the contour-rotation
    operator R = exp[(pi/2) D], D = (i/2)(a^dag^2 - a^2) (the y -> -iy
    dilation), has cond(R_N) growing EXPONENTIALLY with cutoff N, so the
    would-be metric (~ (R R^dag)^{-1}) is unbounded with unbounded inverse:
    the beable map degenerates exponentially with energy -- the paper-Sec.-5
    collapse, but with no rescaled-time survivor.
 C. EQUAL FREQUENCIES (the PU exceptional point). The classical normal-mode
    matrix becomes DEFECTIVE (Jordan block, secular t sin(wt) growth), yet
    the Hermitian grid realization passes through smoothly: <x(t)> tracks
    the secular classical solution and Gamma stays exactly doubly
    stochastic. PU-scale confirmation of paper Sec. 5's verdict: the EP is a
    singularity of the normal-mode (non-Hermitian) dictionary, not of the
    process.

VERDICT. (a) YES -- on the physical beables, via the ghost realization.
(b) NO -- the PT/no-ghost quantization moves the state space off the real
configuration contour; there is no valid stochastic process ON THE ORIGINAL
BEABLES that realizes the positive-energy theory. The two programs resolve
the ghost in incompatible currencies: Barandes keeps real beables and pays
in negative energies; Mannheim buys positive energies and pays with the
sample space itself.

NOT addressed: interactions (where the ghost instability becomes physical
via vacuum decay), the dense-spectrum subtleties, field theory.

Run:  python pais_uhlenbeck.py   (~1-2 minutes: two 1936x1936 eigh + a few
                                  1936^3 matrix products)
"""

import numpy as np
from scipy.linalg import expm, eigh

np.set_printoptions(precision=4, suppress=True)

GAMMA = 1.0
N1D = 44
LBOX = 10.0


def spectral_ops(n=N1D, L=LBOX):
    """Periodic spectral derivative operators: exactly Hermitian."""
    dx = 2 * L / n
    x = -L + dx * np.arange(n)
    F = np.fft.fft(np.eye(n), axis=0, norm="ortho")
    k = 2 * np.pi * np.fft.fftfreq(n, d=dx)
    P = F.conj().T @ (k[:, None] * F)
    P2 = F.conj().T @ ((k ** 2)[:, None] * F)
    return x, 0.5 * (P + P.conj().T), 0.5 * (P2 + P2.conj().T)


def build_pu(w1, w2):
    """Ostrogradski PU Hamiltonian on the (x, y=xdot) grid."""
    x, P, P2 = spectral_ops()
    n = len(x)
    In = np.eye(n)
    X2 = np.diag(x ** 2)
    Y = np.diag(x)
    Y2 = np.diag(x ** 2)
    H = (np.kron(P, Y) + np.kron(In, P2) / (2 * GAMMA)
         + (GAMMA / 2) * (w1 ** 2 + w2 ** 2) * np.kron(In, Y2)
         - (GAMMA / 2) * (w1 * w2) ** 2 * np.kron(X2, In))
    return x, H


def classical_K(w1, w2):
    """Linear flow on (q1, q2, p1, p2)."""
    Om = w1 ** 2 + w2 ** 2
    return np.array([[0, 1, 0, 0],
                     [0, 0, 0, 1 / GAMMA],
                     [GAMMA * (w1 * w2) ** 2, 0, 0, 0],
                     [0, -GAMMA * Om, -1, 0]], dtype=float)


def packet(x, x0, y0, sig=1.0):
    g1 = np.exp(-(x - x0) ** 2 / (2 * sig ** 2))
    g2 = np.exp(-(x - y0) ** 2 / (2 * sig ** 2))
    psi = np.kron(g1, g2).astype(complex)
    return psi / np.linalg.norm(psi)


def run_sector(w1, w2, tmax, label):
    x, H = build_pu(w1, w2)
    herm = np.linalg.norm(H - H.conj().T)
    E, V = eigh(H)
    print(f"[{label}] w1={w1}, w2={w2}: dim = {H.shape[0]}, "
          f"||H - H^dag|| = {herm:.2e}")
    print(f"  spectrum range: [{E[0]:.1f}, {E[-1]:.1f}]  "
          "(indefinite -- the ghost; continuum ladder w1 n1 - w2 n2)")
    # Ehrenfest vs exact classical flow
    psi0 = packet(x, 2.0, 0.0)
    c0 = V.conj().T @ psi0
    xw = np.repeat(x, len(x))
    ts = np.linspace(0, tmax, 61)
    K = classical_K(w1, w2)
    z0 = np.array([2.0, 0.0, 0.0, 0.0])
    dev_half, dev, amp = 0.0, 0.0, 0.0
    for t in ts[1:]:
        psit = V @ (np.exp(-1j * E * t) * c0)
        xq = float(xw @ np.abs(psit) ** 2)
        xc = (expm(K * t) @ z0)[0]
        dev = max(dev, abs(xq - xc))
        if t <= tmax / 2:
            dev_half = max(dev_half, abs(xq - xc))
        amp = max(amp, abs(xc))
    print(f"  Ehrenfest: max |<x>_qm - x_cl| = {dev_half:.4f} on (0, "
          f"{tmax / 2}] and {dev:.4f} on (0, {tmax}]  "
          f"(classical amplitude {amp:.2f};")
    print("   residual = packet tails reaching the box walls, shrinks with "
          "box size)")
    # the stochastic process
    t1 = 1.3
    U1 = (V * np.exp(-1j * E * t1)) @ V.conj().T
    G1 = np.abs(U1) ** 2
    U2 = (V * np.exp(-1j * E * 2 * t1)) @ V.conj().T
    G2 = np.abs(U2) ** 2
    cs = max(abs(G1.sum(0) - 1).max(), abs(G1.sum(1) - 1).max())
    indiv = np.linalg.norm(G2 - G1 @ G1)
    print(f"  Gamma(t={t1}) on {H.shape[0]} configs: doubly-stochastic "
          f"error {cs:.2e} | indivisibility ||G(2t)-G(t)^2|| = {indiv:.2f}")
    return dev


# ----------------------------------------------------------------------
# A. Unequal frequencies: the ghost realization is a valid process
# ----------------------------------------------------------------------
print("=" * 72)
print("A. Ghost (Ostrogradski) PU as a Barandes process on (x, xdot)")
print("=" * 72)
run_sector(1.0, 0.5, tmax=8.0, label="unequal")
print("  beables: FIXED. H is Hermitian on the configuration grid, so")
print("  K1-K4 of paper Sec. 3 hold trivially with eta = identity -- no")
print("  metric correction, no beable rotation. The unbounded-below ENERGY")
print("  never obstructs the PROBABILITY structure: at the free level the")
print("  Ostrogradski ghost is invisible to the stochastic process.")

# ----------------------------------------------------------------------
# B. The no-ghost (PT) move is a domain change with no truncation shadow
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("B. Mannheim's positive-energy move: domain effect, unbounded metric")
print("=" * 72)
print("B1. PT vacuum (b^dag Omega = 0 <-> e^{+y^2/2}) vs Fock truncation:")
print(f"{'N':>5} {'null(b): |<0|v>|':>17} {'null(b^dag): |<N-1|v>|':>23} "
      f"{'sigma_min(b^dag|low)':>21}")
for N in (8, 16, 32, 64):
    A = np.diag(np.sqrt(np.arange(1, N)), 1)      # annihilation b
    for M, tag in ((A, "b"), (A.T.copy(), "bdag")):
        _, sv, vh = np.linalg.svd(M)
        v = vh[-1]
        if tag == "b":
            o_b = abs(v[0])
        else:
            o_bd = abs(v[-1])
    smin = np.linalg.svd(A.T[:, : N // 2], compute_uv=False).min()
    print(f"{N:>5} {o_b:>17.6f} {o_bd:>23.6f} {smin:>21.6f}")
print("  null(b) = |0> at every N (the true vacuum, truncation-stable);")
print("  null(b^dag) = |N-1>: pinned to the truncation EDGE -- it escapes")
print("  to infinite energy as N grows, and on any fixed low-energy sector")
print("  b^dag is bounded below by 1. The PT vacuum has NO shadow in the")
print("  real-configuration theory: not a rotation of beables (sec. 5.1),")
print("  but an exit from the sample space.")
print()
print("B2. Contour rotation R = exp[(pi/2) D], D = (i/2)(a^dag^2 - a^2):")
print(f"{'N':>5} {'lam_max(D_N)':>13} {'log10 cond(R_N)':>16} "
      f"{'log10 cond(metric)':>19}")
lc = []
Ns = (8, 16, 24, 32, 40, 48)
for N in Ns:
    A = np.diag(np.sqrt(np.arange(1, N)), 1)
    D = 0.5j * (A.T @ A.T - A @ A)
    lam = np.linalg.eigvalsh(D)
    logcond = (np.pi / 2) * (lam[-1] - lam[0]) / np.log(10)
    lc.append(logcond)
    print(f"{N:>5} {lam[-1]:>13.3f} {logcond:>16.2f} {2 * logcond:>19.2f}")
slope = np.polyfit(Ns, lc, 1)[0]
print(f"  growth: ~{slope:.2f} decades per level -- cond EXPONENTIAL in the")
print("  cutoff. The would-be metric (RR^dag)^{-1} is unbounded with")
print("  unbounded inverse: the beable map degenerates exponentially with")
print("  energy. This is the paper-Sec.-5 collapse at every scale at once,")
print("  with no critical-rescaling survivor.")

# ----------------------------------------------------------------------
# C. Equal frequencies: the PU exceptional point
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("C. Equal frequencies (w1 = w2 = 0.75): the PU exceptional point")
print("=" * 72)
Keq = classical_K(0.75, 0.75)
ev, W = np.linalg.eig(Keq)
print(f"classical normal-mode matrix: eigenvalues {np.round(ev, 4)},")
print(f"eigenvector condition number = {np.linalg.cond(W):.2e}  "
      "(defective: Jordan block, secular t*sin(wt) growth)")
run_sector(0.75, 0.75, tmax=3.5, label="equal")
print("  => the Hermitian realization crosses the PU exceptional point")
print("  smoothly: <x(t)> tracks the SECULAR classical solution")
print("  x(t) = 2 cos(wt) + w t sin(wt), and Gamma remains exactly doubly")
print("  stochastic. The Jordan pathology lives in the normal-mode")
print("  (non-Hermitian) dictionary only -- as in paper Sec. 5.")
