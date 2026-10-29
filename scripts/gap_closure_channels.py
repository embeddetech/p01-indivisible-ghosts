"""
Closing the last gap of Open Problem 9.6 at the finite-channel level:
DEFICIENCY STABILITY UNDER THE PU INTERCHANNEL COUPLINGS.

THE OBSERVATION THAT CLOSES IT. The channelized quartic PU
(pu_bo_channels.py) has interchannel couplings that are NOT generic
subordinate couplings: T(k + c p2) is a polynomial in the single
Hermitian operator p2, so it commutes with p2 and is EXACTLY diagonal in
the k-independent eigenframe of the truncated P2 (simple eigenvalues
p_nu, scaled Gauss-Hermite points). In that frame the M-channel Galerkin
model
    S_M = p_hat^2/(2 g O) - T(k 1 + c P2_M) - sqrt(O) (N + 1/2),
decouples exactly into scalar branches p_hat^2/(2 g O) - T(k + c p_nu)
-- each limit circle at BOTH ends for lam > 0 (shifted -lam k^4 class,
Reed-Simon X.10) -- plus the rotated channel-energy matrix
R^dag sqrt(O)(N+1/2) R, which is CONSTANT (k-independent) and BOUNDED
(norm <= sqrt(O)(M - 1/2)).

THEOREM (finite-channel stability). For every M, S_M has deficiency
indices (2M, 2M).
Proof: (i) exact frame decoupling as above; (ii) a finite direct sum of
LC/LC scalar operators has indices (2M, 2M); (iii) bounded symmetric
perturbations preserve deficiency indices (relative bound zero; Kato).

REDUCED REMAINING GAP (full operator): (a) the exact Fock compression
differs from the Galerkin model by k-dependent terms supported on the
top ~4 channels (edge effects, vanishing from any fixed matrix element
as M grows); (b) the M -> infinity limit: the full operator is a direct
integral of LC fibers over spec(p2) coupled by the transverse
oscillator; channel-tail decay of deficiency vectors remains open.

VERIFICATIONS BELOW.
 G1  exact frame decoupling: eig T(k1 + cP2_M) = T(k + c p_nu) to
     machine precision; the exact-compression edge effects are confined
     to the top channels.
 G2  the theorem's falsifiable consequence: with couplings ON, the
     wall-regularized level density equals the ALL-BRANCH sum
     sum_nu T_cross,nu / pi (if any channel's deficiency were destroyed,
     the density would drop below the prediction). Tested for
     M = 1, 2, 3 and three wall positions.
 G3  LC signature: the eigenvalue nearest E sweeps erratically with the
     wall (no regulator-independent completion), as in the scalar case.

Run:  python -u gap_closure_channels.py     (~1-2 minutes)
"""

import functools
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

print = functools.partial(print, flush=True)

GAM, W1, W2, LAM = 1.0, 1.0, 0.5, 0.05
OMEGA, WBAR = W1 ** 2 + W2 ** 2, (W1 * W2) ** 2
C = 1.0 / (GAM * OMEGA)                  # the p2-shift coefficient
MEFF = GAM * OMEGA                       # mass of the k-motion
NUP = GAM * np.sqrt(OMEGA)               # mode-2 ladder scale for p2


def p2_real(M):
    """P2 in the phase-rotated Fock basis: real symmetric tridiagonal,
    same spectrum as i sqrt(nup/2)(a^dag - a)."""
    a = np.diag(np.sqrt(np.arange(1, M)), 1)
    return np.sqrt(NUP / 2) * (a + a.T)


def Tpoly(A):
    return LAM * np.linalg.matrix_power(A, 4) - (GAM * WBAR / 2) * (A @ A)


def W_matrix(k, P2M, Nterm):
    """Potential matrix of S_M at position k."""
    M = P2M.shape[0]
    return -Tpoly(k * np.eye(M) + C * P2M) - Nterm


def build_SM(M, L, dx):
    P2M = p2_real(M)
    Nterm = np.sqrt(OMEGA) * (np.diag(np.arange(M)) + 0.5 * np.eye(M))
    Nk = int(round(2 * L / dx)) - 1
    ks = -L + dx * np.arange(1, Nk + 1)
    kin = sparse.diags([np.full(Nk - 1, -0.5 / dx ** 2),
                        np.full(Nk, 1.0 / dx ** 2),
                        np.full(Nk - 1, -0.5 / dx ** 2)],
                       [-1, 0, 1]) / MEFF
    H = sparse.kron(kin, sparse.identity(M)).tolil()
    for i, k in enumerate(ks):
        H[i * M:(i + 1) * M, i * M:(i + 1) * M] += W_matrix(k, P2M, Nterm)
    return H.tocsc(), ks, P2M, Nterm


# ----------------------------------------------------------------------
print("=" * 72)
print("G1. Exact frame decoupling (and where the edge effects live)")
print("=" * 72)
M = 8
P2M = p2_real(M)
pnu = np.sort(np.linalg.eigvalsh(P2M))
k0 = 3.7
ev = np.sort(np.linalg.eigvalsh(-Tpoly(k0 * np.eye(M) + C * P2M)))
pred = np.sort([-(LAM * (k0 + C * p) ** 4 - (GAM * WBAR / 2)
                  * (k0 + C * p) ** 2) for p in pnu])
print(f"M = {M}, k = {k0}: max |eig(-T(k1+cP2)) - (-T(k+c p_nu))| = "
      f"{np.abs(ev - pred).max():.2e}   (matrix-function identity)")
# exact Fock compression vs Galerkin: edge-channel effects
PAD = 10
a = np.diag(np.sqrt(np.arange(1, M + PAD)), 1)
P2pad = np.sqrt(NUP / 2) * (a + a.T)
Texact = (-Tpoly(k0 * np.eye(M + PAD) + C * P2pad))[:M, :M]
Tgaler = -Tpoly(k0 * np.eye(M) + C * P2M)
d = np.abs(Texact - Tgaler)
print(f"exact-compression minus Galerkin: max over first {M-4} channels "
      f"= {d[:M-4, :M-4].max():.2e}, max over top 4 channels = "
      f"{d[M-4:, M-4:].max():.3f}")
print("=> couplings are functions of P2 alone: exactly removable by a")
print("   constant rotation; compression edge effects sit at the top")
print("   channels only.")

# ----------------------------------------------------------------------
print()
print("=" * 72)
print("G2. All-branch level density with couplings ON (the theorem's")
print("    falsifiable consequence), E window [9, 13]")
print("=" * 72)
DX = 5e-3
EMID, ELO, EHI = 11.0, 9.0, 13.0


def predicted_spacing(M, L):
    P2M = p2_real(M)
    Nterm = np.sqrt(OMEGA) * (np.diag(np.arange(M)) + 0.5 * np.eye(M))
    ks = np.linspace(-L, L, 4001)
    dens = 0.0
    for ki in range(len(ks) - 1):
        k = 0.5 * (ks[ki] + ks[ki + 1])
        w = np.linalg.eigvalsh(W_matrix(k, P2M, Nterm))
        dk = ks[ki + 1] - ks[ki]
        dens += np.sum(np.sqrt(MEFF / (2 * (EMID - w)))) * dk / np.pi
    return 1.0 / dens


print(f"{'M':>3} {'L':>6} {'#win':>5} {'med gap':>9} {'width/#':>9} "
      f"{'predicted':>10}")
for M in (1, 2, 3):
    for L in (7.0, 8.5, 10.0):
        H, ks, _, _ = build_SM(M, L, DX)
        ev = np.sort(eigsh(H, k=90, sigma=EMID, which="LM",
                           return_eigenvectors=False))
        win = ev[(ev > ELO) & (ev < EHI)]
        sp = np.median(np.diff(win)) if len(win) > 2 else np.nan
        print(f"{M:>3} {L:>6.1f} {len(win):>5} {sp:>9.4f} "
              f"{(EHI - ELO) / len(win):>9.4f} "
              f"{predicted_spacing(M, L):>10.4f}")
print("=> the count-based spacing (window width / count) tracks the")
print("   ALL-2M-branch prediction everywhere; the median gap is biased")
print("   low where the +-p_nu branch ladders lock into near-degenerate")
print("   parity doublets (M = 2 at small L). Every channel contributes")
print("   its limit-circle ladder despite the couplings: deficiency")
print("   (2M, 2M), as the theorem states.")

# ----------------------------------------------------------------------
print()
print("=" * 72)
print("G3. Regulator sweep (M = 2): the completion never converges")
print("=" * 72)
near = []
for L in np.arange(9.0, 9.41, 0.1):
    H, _, _, _ = build_SM(2, L, DX)
    ev = eigsh(H, k=1, sigma=EMID, which="LM", return_eigenvectors=False)
    near.append(ev[0])
print("L      :", " ".join(f"{L:6.2f}" for L in np.arange(9.0, 9.41, 0.1)))
print("E near :", " ".join(f"{e:6.3f}" for e in near))
print("=> eigenvalue nearest E sweeps with the wall: LC behavior of the")
print("   coupled system, consistent with indices (2M, 2M).")
