"""
Exact channelization of the quartic Pais-Uhlenbeck operator, and the
falsifiable prediction it makes (continuation of
pu_deficiency_evidence.py; Open Problem 9.6).

PROPOSITION (exact displaced-oscillator channelization). In the
Fourier-rotated representation (p1 -> y, q1 -> -p_y), where
    H = y q2 + p2^2/(2g) + (g O/2) q2^2 + T(p_y),
    T(p) = lam p^4 - (g wb/2) p^2,
the unitary U = exp(-i y p2 / (g O)) gives EXACTLY
    U H U^dag = T(p_y + p2/(g O)) + [p2^2/(2g) + (g O/2) q2^2]
                - y^2/(2 g O).
Expanding T about p_y: the mode-2-diagonal (channel) part is, in the
k = p_y representation and up to k^2- and constant corrections,
    H_n = -[ p_hat^2/(2 g O) - lam k^4 + (g wb/2) k^2 - sqrt(O)(n+1/2) ],
i.e. MINUS a 1D Schroedinger operator whose potential falls like
-lam k^4. Interchannel couplings are polynomial of degree <= 3 in k
(T', T'', T''' terms), subordinate to the quartic diagonal.

CONSEQUENCES.
 - lam > 0: every channel is LIMIT CIRCLE (the -x^4 class, with the
   time-of-flight dictionary); channel additivity then argues for
   deficiency indices (inf, inf) -- independent structural support for
   the drift verdict of pu_deficiency_evidence.py. (Gap to full rigor:
   stability under the degree-3 subordinate couplings.)
 - lam < 0: every channel is (minus) a CONFINING operator: prediction =
   quantum complete, even though the classical lam < 0 quartic PU also
   blows up in finite time. A second Rauch-Reed-type quantum-completion
   candidate, and a falsifiable prediction for the drift diagnostic.

THIS SCRIPT:
 P1  verifies the displaced-oscillator identity numerically in a padded
     Fock representation (operator algebra check);
 P2  computes the channel time-of-flight (finite for lam > 0) and the
     channel confinement (lam < 0);
 P3  TESTS THE PREDICTION: drift diagnostic for the lam = -0.05 quartic
     PU (expect e.s.a. baseline, in sharp contrast to lam = +0.05);
 P4  extends the truncation range (N up to 64) for the two headline
     verdicts: quartic PU lam = +0.05 (expect O(1) drift persists) and
     ghost pair lam = -0.05 (does the baseline hold?).

Run:  python -u pu_bo_channels.py     (~10-15 minutes)
"""

import functools
import numpy as np
from scipy.linalg import eigvalsh, expm
from scipy.integrate import quad

print = functools.partial(print, flush=True)

PAD = 12
GAM, W1, W2, LAM = 1.0, 1.0, 0.5, 0.05
OMEGA, WBAR = W1 ** 2 + W2 ** 2, (W1 * W2) ** 2


def ops(N, nu):
    Nb = N + PAD
    a = np.diag(np.sqrt(np.arange(1, Nb)), 1)
    X = (a + a.T) / np.sqrt(2 * nu)
    M = a.T - a
    return X, M


def compress(op, N):
    return op[:N, :N]


def quartic_pu(N, lam, nu1=1.0, nu2=1.0):
    Y, M1 = ops(N, nu1)
    X2, M2 = ops(N, nu2)
    Py2 = -(nu1 / 2) * (M1 @ M1)
    Py4 = (nu1 / 2) ** 2 * np.linalg.matrix_power(M1, 4)
    P22 = -(nu2 / 2) * (M2 @ M2)
    I = np.eye(N)
    H = (np.kron(compress(Y, N), compress(X2, N))
         + np.kron(I, compress(P22, N)) / (2 * GAM)
         + (GAM * OMEGA / 2) * np.kron(I, compress(X2 @ X2, N))
         - (GAM * WBAR / 2) * np.kron(compress(Py2, N), I)
         + lam * np.kron(compress(Py4, N), I))
    return 0.5 * (H + H.T)


def ghost_pair(N, lam):
    X1, M1 = ops(N, 1.0)
    X2, M2 = ops(N, 0.5)
    P12 = -(1.0 / 2) * (M1 @ M1)
    P22 = -(0.5 / 2) * (M2 @ M2)
    I = np.eye(N)
    H = (0.5 * np.kron(compress(P12 + W1 ** 2 * X1 @ X1, N), I)
         - 0.5 * np.kron(I, compress(P22 + W2 ** 2 * X2 @ X2, N))
         + lam * np.kron(compress(X1 @ X1, N), compress(X2 @ X2, N)))
    return 0.5 * (H + H.T)


def window(evals, lo=-0.75, hi=0.75):
    return evals[(evals > lo) & (evals < hi)]


def drift_report(label, pairs, lo=-0.75, hi=0.75):
    print(f"  {label}:")
    print(f"    {'N':>5} {'#win':>5} {'spacing':>10} {'med drift':>10} "
          f"{'ratio':>7}")
    for (N1, e1), (N2, e2) in zip(pairs[:-1], pairs[1:]):
        w1, w2 = window(e1, lo, hi), window(e2, lo, hi)
        if len(w1) < 2 or len(w2) < 1:
            print(f"    {N1:>5}  (too few levels)")
            continue
        sp = np.median(np.diff(w1))
        dr = np.median([np.min(np.abs(w2 - x)) for x in w1])
        print(f"    {N1:>5} {len(w1):>5} {sp:>10.4f} {dr:>10.4f} "
              f"{dr / sp:>7.3f}")


# ----------------------------------------------------------------------
# P1. The exact identity, checked as operator algebra in Fock space
# ----------------------------------------------------------------------
print("=" * 72)
print("P1. Displaced-oscillator identity U H U^dag = T(p_y + p2/(gO))")
print("    + oscillator - y^2/(2gO): finite-BCH Fock-space check")
print("=" * 72)
# The adjoint action of the quadratic A = -i y p2/(gO) preserves the
# polynomial algebra (it shifts p_y and q2), so exp-conjugation equals a
# FINITE Baker-Campbell-Hausdorff sum; this avoids expm of a non-banded
# displacement operator, whose truncation error would swamp the check.
Nc, Np = 14, 30          # compare on inner Nc block, build at Np
nu = 1.0
a = np.diag(np.sqrt(np.arange(1, Np)), 1)
X = (a + a.T) / np.sqrt(2 * nu)          # position (either mode)
P = 1j * np.sqrt(nu / 2) * (a.T - a)     # momentum
I = np.eye(Np)
Y, P2m = np.kron(X, I), np.kron(I, P)
Q2, PY = np.kron(I, X), np.kron(P, I)
T = lambda A: LAM * np.linalg.matrix_power(A, 4) - (GAM * WBAR / 2) * A @ A
Hfull = (Y @ Q2 + np.kron(I, (P @ P).real) / (2 * GAM)
         + (GAM * OMEGA / 2) * np.kron(I, X @ X) + T(PY))
A = -1j * Y @ P2m / (GAM * OMEGA)
acc = Hfull.copy()
term = Hfull.copy()
fact = 1.0
for k in range(1, 7):
    term = A @ term - term @ A
    fact *= k
    acc = acc + term / fact
rhs = (T(PY + P2m / (GAM * OMEGA))
       + np.kron(I, (P @ P).real) / (2 * GAM)
       + (GAM * OMEGA / 2) * np.kron(I, X @ X)
       - Y @ Y / (2 * GAM * OMEGA))
inner = np.array([i * Np + j for i in range(Nc) for j in range(Nc)])
diff = np.abs(acc[np.ix_(inner, inner)] - rhs[np.ix_(inner, inner)]).max()
print(f"max |BCH(LHS) - RHS| on the inner {Nc}x{Nc}-per-mode block: "
      f"{diff:.2e}")
print("(series terminates: ad_A^5 H = 0 identically)")

# ----------------------------------------------------------------------
# P2. Channel structure: time of flight (lam>0) vs confinement (lam<0)
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("P2. Channel operators S_n = p^2/(2 g O) - lam k^4 + (g wb/2) k^2"
      " - sqrt(O)(n+1/2)")
print("=" * 72)
Msl = GAM * OMEGA
Vch = lambda k, lam: -lam * k ** 4 + (GAM * WBAR / 2) * k ** 2
for lam, tag in ((LAM, "lam = +0.05"), (-LAM, "lam = -0.05")):
    if lam > 0:
        E0 = 1.0
        # time of flight with mass Msl: dk / sqrt(2 (E - V)/Msl)
        tof = quad(lambda k: 1 / np.sqrt(2 * (E0 - Vch(k, lam)) / Msl),
                   2.0, 400.0, limit=400)[0]
        tail = quad(lambda k: 1 / np.sqrt(2 * (E0 - Vch(k, lam)) / Msl),
                    400.0, 4000.0, limit=400)[0]
        print(f"  {tag}: V(k) -> -{lam}k^4: LIMIT CIRCLE; channel time of")
        print(f"    flight T(k=2 -> 400) = {tof:.4f}, tail(400->4000) = "
              f"{tail:.6f}  (convergent)")
    else:
        kk = np.array([2.0, 5.0, 10.0])
        print(f"  {tag}: V(k) = +{-lam}k^4 + {GAM*WBAR/2}k^2 = "
              f"{np.round(Vch(kk, lam), 1)} at k = {kk}: CONFINING")
print("=> lam > 0: LC channels (deficiency, channel-additive).")
print("   lam < 0: confining channels: PREDICT quantum complete despite")
print("   classical finite-time blowup (t* = 4.4-6.9 observed earlier).")

# ----------------------------------------------------------------------
# P3. The prediction tested: drift for lam = -0.05
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("P3. Drift diagnostic, quartic PU lam = -0.05 "
      "(prediction: e.s.a. baseline ~0.2)")
print("=" * 72)
NS = (24, 30, 36, 42, 48)
for nu1 in (1.0, 0.7):
    pairs = [(N, np.sort(eigvalsh(quartic_pu(N, -LAM, nu1=nu1))))
             for N in NS]
    drift_report(f"quartic PU lam = -0.05, basis scale nu1 = {nu1}", pairs)

# ----------------------------------------------------------------------
# P4. Extended truncations for the headline verdicts
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("P4. Extended truncations N = 48, 56, 64")
print("=" * 72)
NS_BIG = (48, 56, 64)
pairs = [(N, np.sort(eigvalsh(quartic_pu(N, LAM)))) for N in NS_BIG]
drift_report("quartic PU lam = +0.05 (expect O(1) drift persists)", pairs)
pairs = [(N, np.sort(eigvalsh(ghost_pair(N, -LAM)))) for N in NS_BIG]
drift_report("ghost pair lam = -0.05 (does the baseline hold?)", pairs)
print()
print("Read-out: P3 at baseline validates the BO channel picture on both")
print("signs; P4 checks persistence of the lam = +0.05 LC signal and")
print("stresses the ghost-pair completion hypothesis at larger N.")
