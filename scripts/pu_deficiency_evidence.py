"""
Numerical-evidence campaign for Open Problem 9.6:
essential self-adjointness of the exact quartic Pais-Uhlenbeck operator
and of the lambda x1^2 x2^2 ghost pair.

No finite computation can prove essential self-adjointness (a statement
about behavior at infinity), so the campaign measures REGULATOR
DEPENDENCE with a diagnostic validated on known cases.

REGULATOR. Fock-space (Hermite-basis) compression at N states per mode:
regulates position and momentum symmetrically (the PU escape accelerates
without bound, so momentum infinity matters as much as position
infinity), and has no lattice doubler artifacts from the p1 q2 term.
Operators are built at size N+12 and compressed to N (so products are
exact). A mode-1 Fourier rotation (p1 -> y, q1 -> -p_y) makes the
quartic PU real symmetric:
    H_PU -> y q2 + p2^2/(2g) + (g O/2) q2^2 - (g wb/2) p_y^2 + l p_y^4.

DIAGNOSTIC (matched-eigenvalue drift). For successive truncations
N < N', take the window spectrum near E = 0; for each eigenvalue at N,
find the distance to the nearest eigenvalue at N'; report the median
drift, the median local spacing, and their ratio. Calibrated regimes:
  - discrete e.s.a.  (control: p^2/2 + x^4):        ratio -> 0 fast;
  - continuous e.s.a. (control: p^2/2 - x^2):       spacing -> 0;
  - limit circle      (control: p^2/2 - x^4, (2,2)): spacing saturates
    AND ratio stays O(1) forever (the eigenvalues never stop moving --
    the compression plays the role of the sweeping wall of the
    explosion-dictionary verification V3).
  - dense-point e.s.a. (control: free PU, e.s.a. by the quadratic
    theorem): previously-converged eigenvalues persist (small ratio),
    newcomers merely join.

STRUCTURAL PREDICTION (tested). Born-Oppenheimer channels of the ghost
pair: transverse frequency Omega1(x2) = sqrt(w1^2 + 2 l x2^2). For
l > 0 it GROWS along the escape direction, so every channel potential
    W_n(x2) = (w2^2/2) x2^2 - (n+1/2) Omega1(x2)
is quadratically confining: prediction = quantum complete (e.s.a.),
matching the observed classical benignity of l > 0. For l < 0 the
transverse channel collapses at x2 = sqrt(w1^2/(2|l|)): malicious.

Run:  python -u pu_deficiency_evidence.py     (~6-10 minutes)
"""

import functools
import numpy as np
from scipy.linalg import eigvalsh

print = functools.partial(print, flush=True)

PAD = 12


def ops(N, nu):
    """Single-mode X, P^2, and antisymmetric M = a^T - a at size N
    (built padded, compressed after products by the caller)."""
    Nb = N + PAD
    a = np.diag(np.sqrt(np.arange(1, Nb)), 1)
    X = (a + a.T) / np.sqrt(2 * nu)
    M = a.T - a                       # P = i sqrt(nu/2) M
    return X, M


def compress(op, N):
    return op[:N, :N]


def window(evals, lo=-0.75, hi=0.75):
    return evals[(evals > lo) & (evals < hi)]


def drift_report(label, pairs, lo=-0.75, hi=0.75):
    """pairs = list of (N, sorted eigenvalues). Print drift table."""
    print(f"  {label}:")
    print(f"    {'N':>5} {'#win':>5} {'spacing':>10} {'med drift':>10} "
          f"{'ratio':>7}")
    for (N1, e1), (N2, e2) in zip(pairs[:-1], pairs[1:]):
        w1, w2 = window(e1, lo, hi), window(e2, lo, hi)
        if len(w1) < 2 or len(w2) < 1:
            print(f"    {N1:>5}  (too few levels in window)")
            continue
        sp = np.median(np.diff(w1))
        dr = np.median([np.min(np.abs(w2 - x)) for x in w1])
        print(f"    {N1:>5} {len(w1):>5} {sp:>10.4f} {dr:>10.4f} "
              f"{dr / sp:>7.3f}")


# ----------------------------------------------------------------------
# Part 0: calibration on known 1D cases (window near E = 10)
# ----------------------------------------------------------------------
print("=" * 72)
print("0. Calibration of the drift diagnostic on known 1D operators")
print("   (window E in [5, 15]; h = p^2/2 + V)")
print("=" * 72)
NS1 = (80, 120, 160, 200, 240)


def h1d(N, vsign, quartic, nu=2.0):
    X, M = ops(N, nu)
    P2 = -(nu / 2) * (M @ M)
    V = vsign * (np.linalg.matrix_power(X, 4) if quartic else X @ X)
    return compress(0.5 * P2 + V, N)


for label, vsign, quartic, expect in (
        ("p^2/2 + x^4  (discrete e.s.a.)", +1, True, "ratio -> 0"),
        ("p^2/2 - x^2  (continuous e.s.a.)", -1, False, "spacing -> 0"),
        ("p^2/2 - x^4  (LIMIT CIRCLE, n=(2,2))", -1, True,
         "spacing saturates, ratio O(1)")):
    pairs = [(N, np.sort(eigvalsh(h1d(N, vsign, quartic)))) for N in NS1]
    drift_report(label + f"   [expect: {expect}]", pairs, 5.0, 15.0)

# ----------------------------------------------------------------------
# 2D builders
# ----------------------------------------------------------------------
GAM, W1, W2, LAM = 1.0, 1.0, 0.5, 0.05
OMEGA, WBAR = W1 ** 2 + W2 ** 2, (W1 * W2) ** 2


def quartic_pu(N, lam, nu1=1.0, nu2=1.0):
    """Fourier-rotated rep: y q2 + p2^2/2g + gO/2 q2^2 - g wb/2 p_y^2
    + lam p_y^4; real symmetric."""
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


NS2 = (24, 30, 36, 42, 48)

# ----------------------------------------------------------------------
# Part 1: free PU (e.s.a. by the quadratic theorem) -- 2D methodology check
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("1. Free PU (lambda = 0): e.s.a. by Nelson's theorem -- the 2D")
print("   control. Old window eigenvalues must persist.")
print("=" * 72)
pairs = [(N, np.sort(eigvalsh(quartic_pu(N, 0.0)))) for N in NS2]
drift_report("free PU, window E in [-0.75, 0.75]", pairs)

# ----------------------------------------------------------------------
# Part 2: the quartic PU, two basis scales
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("2. Quartic PU (lambda = 0.05): the open problem")
print("=" * 72)
for nu1 in (1.0, 0.7):
    pairs = [(N, np.sort(eigvalsh(quartic_pu(N, LAM, nu1=nu1))))
             for N in NS2]
    drift_report(f"quartic PU, basis scale nu1 = {nu1}", pairs)

# ----------------------------------------------------------------------
# Part 3: ghost pair, both signs, with the BO prediction
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("3. Ghost pair (lambda = +-0.05): Born-Oppenheimer prediction first")
print("=" * 72)
print("channel potentials W_n(x2) = w2^2 x2^2/2 - (n+1/2) "
      "sqrt(w1^2 + 2 lam x2^2):")
print(f"{'x2':>5}", " ".join(f"W_{n}(+)" .rjust(9) for n in range(4)),
      "  | lam<0 transverse freq^2")
for x2 in (2.0, 4.0, 6.0, 8.0):
    wp = [0.5 * W2 ** 2 * x2 ** 2
          - (n + 0.5) * np.sqrt(W1 ** 2 + 2 * LAM * x2 ** 2)
          for n in range(4)]
    f2m = W1 ** 2 - 2 * LAM * x2 ** 2
    print(f"{x2:>5.1f}", " ".join(f"{w:>9.3f}" for w in wp),
          f"  | {f2m:>+8.3f}" + ("  (collapsed)" if f2m < 0 else ""))
print(f"=> lam > 0: every channel confining (quadratic dominates):")
print("   PREDICT quantum complete (e.s.a.).  lam < 0: transverse")
print(f"   collapse beyond x2 = {np.sqrt(W1**2/(2*LAM)):.2f}: malicious.")
print()
for lam, tag in ((+LAM, "lam = +0.05 (predicted complete)"),
                 (-LAM, "lam = -0.05 (classically malicious)")):
    pairs = [(N, np.sort(eigvalsh(ghost_pair(N, lam)))) for N in NS2]
    drift_report(f"ghost pair, {tag}", pairs)

print()
print("=" * 72)
print("Read-out: compare each system's drift ratio and spacing trend with")
print("the calibrated regimes of Part 0. Persistent O(1) ratio with")
print("saturating spacing = limit-circle-like (deficiency evidence);")
print("shrinking ratio = convergence (essential-self-adjointness")
print("evidence); shrinking spacing = continuous-spectrum-like. Evidence,")
print("not proof: the verdicts should be robust under the basis-scale")
print("change (Part 2) to count.")
