"""
Section 5.1 of PT_stochastic_handoff.md (= paper Sec. 3):
Fixed-beable / Kolmogorov-cycle characterization.

QUESTION: which non-Hermitian H admit a metric eta that is DIAGONAL in the
configuration basis (so the Barandes beables are preserved, not rotated)?

THEOREM (derived analytically, verified numerically below).
H admits a positive diagonal metric eta = diag(d), d_i > 0, with
H^dag eta = eta H, iff all of:

  (K1)  H_ii real for every i                      [from the i=j component]
  (K2)  H_ij = 0  <=>  H_ji = 0                    [symmetric coupling support]
  (K3)  H_ij H_ji > 0 for every coupled pair       [arg H_ij + arg H_ji = 0]
  (K4)  KOLMOGOROV CYCLE CONDITION: around every cycle of the coupling graph,
        prod of |H| one way  =  prod of |H| the other way.

Proof sketch: the component form of H^dag eta = eta H with eta = diag(d) is
      d_i H_ij = d_j H_ji^*                                   (*)
i=j gives K1. i!=j: existence of d_i>0 forces K2; the phase of (*) forces K3;
the modulus of (*) gives d_i/d_j = |H_ji|/|H_ij|, and consistency of these
ratios around closed loops is exactly K4 (Kolmogorov's criterion for detailed
balance). Conversely, if K1-K4 hold, build d along a spanning forest; K4 makes
it well-defined; positivity is automatic. d is unique up to one overall scale
per connected component of the coupling graph, and the fixed-beable process
      Gamma_ij(t) = (d_i/d_j) |U_ij(t)|^2 ,   U = exp(-iHt)
is scale-invariant, hence UNIQUE.

COROLLARIES.
  1. K1-K4 imply the spectrum of H is real (h = eta^{1/2} H eta^{-1/2} is
     Hermitian) -- unbroken antilinearity is *derived*, not assumed.
  2. Fixed-beable H = (positive diagonal) similarity orbit of Hermitian
     matrices: exactly "detailed-balanced gain/loss", no new physics beyond a
     reweighting Gamma_ij = (d_i/d_j)|U_ij|^2 of the naive Barandes process.
  3. Classical dictionary: with hopping rates q(i->j) := |H_ji|, the
     distribution pi_i ∝ 1/d_i satisfies detailed balance
     pi_i q(i->j) = pi_j q(j->i). The metric weights are the INVERSE of the
     Kolmogorov equilibrium distribution of the modulus rate graph.
  4. For n=2 there are no cycles beyond pairs, so K4 is vacuous: fixed-beable
     <=> H_11, H_22 real and H_12 H_21 > 0. The canonical PT 2x2 model
     (diagonal e^{+-i theta}) fails K1 for every theta != 0, pi -- within that
     family, fixed beables <=> Hermitian. Genuinely non-Hermitian fixed-beable
     examples need magnitude-asymmetric couplings (see Section B).

Run:  python fixed_beable_kolmogorov.py
"""

import numpy as np
from scipy.linalg import expm, eig, sqrtm

np.set_printoptions(precision=4, suppress=True)
TOL = 1e-9


# ----------------------------------------------------------------------
# Core machinery
# ----------------------------------------------------------------------

def diagonal_metric(H, tol=TOL):
    """Construct a positive diagonal metric eta = diag(d) with
    H^dag eta = eta H, or explain why none exists.
    Returns (d, []) on success, (None, [failed conditions]) otherwise."""
    n = H.shape[0]
    fails = []
    if not np.allclose(H.diagonal().imag, 0, atol=1e-8):
        fails.append("K1: diagonal entries not all real")
    sup = (np.abs(H) > tol) & ~np.eye(n, dtype=bool)
    if not np.array_equal(sup, sup.T):
        fails.append("K2: coupling support not symmetric")
        return None, fails
    for i in range(n):
        for j in range(i + 1, n):
            if sup[i, j]:
                p = H[i, j] * H[j, i]
                if abs(p.imag) > 1e-8 * max(abs(p), 1) or p.real <= 0:
                    fails.append(f"K3: H[{i},{j}]*H[{j},{i}] = {p:.4f} "
                                 "not real positive")
    if fails:
        return None, fails
    # spanning forest: d_root = 1; edge j -> i fixes d_i = d_j |H_ji|/|H_ij|
    d = np.zeros(n)
    for root in range(n):
        if d[root] > 0:
            continue
        d[root] = 1.0
        stack = [root]
        while stack:
            j = stack.pop()
            for i in range(n):
                if sup[i, j] and d[i] == 0:
                    d[i] = d[j] * abs(H[j, i]) / abs(H[i, j])
                    stack.append(i)
    # full verification of (*): catches K4 (cycle) violations
    resid = np.linalg.norm(np.diag(d) @ H - H.conj().T @ np.diag(d))
    if resid > 1e-7 * max(np.linalg.norm(H), 1):
        return None, [f"K4: Kolmogorov cycle condition violated "
                      f"(intertwining residual {resid:.3g})"]
    return d, []


def diagonal_metric_nullspace_dim(H, tol=1e-8):
    """Independent numeric check: dimension of the real solution space
    { d in R^n : d_i H_ij - d_j H_ji^* = 0 for all i,j }."""
    n = H.shape[0]
    rows = []
    for i in range(n):
        for j in range(n):
            re, im = np.zeros(n), np.zeros(n)
            re[i] += H[i, j].real
            im[i] += H[i, j].imag
            re[j] -= H[j, i].real
            im[j] += H[j, i].imag
            rows += [re, im]
    A = np.array(rows)
    sv = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(sv < tol * max(sv[0], 1)))


def biorthogonal_metric(H):
    """Canonical (generally NON-diagonal) metric eta = (V V^dag)^{-1}."""
    E, V = eig(H)
    Vinv = np.linalg.inv(V)
    eta = Vinv.conj().T @ Vinv
    return E, 0.5 * (eta + eta.conj().T)


def gamma_of(H, rho, t):
    """Metric-corrected Barandes process Gamma(t) = |rho U rho^{-1}|^2."""
    Th = rho @ expm(-1j * H * t) @ np.linalg.inv(rho)
    return np.abs(Th) ** 2


def stochastic_report(H, rho, t=1.3, label=""):
    G, G2 = gamma_of(H, rho, t), gamma_of(H, rho, 2 * t)
    ds = (np.allclose(G.sum(0), 1) and np.allclose(G.sum(1), 1)
          and np.all(G >= -1e-12))
    indiv = np.linalg.norm(G2 - G @ G)
    print(f"  Gamma({t}) {label}=\n" + str(np.round(G, 4)))
    print(f"  doubly stochastic: {ds} | col sums {np.round(G.sum(0), 4)}")
    print(f"  indivisible? ||Gamma(2t) - Gamma(t)^2|| = {indiv:.4f} "
          "(>0 => non-Markovian)")
    return ds, indiv


def real_spectrum(H):
    E = eig(H, right=False)
    return np.allclose(E.imag, 0, atol=1e-8), np.sort_complex(E)


# ----------------------------------------------------------------------
# A. Task (b): the canonical 2x2 PT model FAILS the fixed-beable test
# ----------------------------------------------------------------------
print("=" * 72)
print("A. 2x2 canonical PT model (unbroken phase: r=1, theta=pi/4, s=1)")
print("=" * 72)
th = np.pi / 4
H2 = np.array([[np.exp(1j * th), 1.0], [1.0, np.exp(-1j * th)]], dtype=complex)
d, fails = diagonal_metric(H2)
print("fixed-beable metric exists:", d is not None)
for f in fails:
    print("  FAILS ->", f)
print("nullspace dim (numeric cross-check, expect 0):",
      diagonal_metric_nullspace_dim(H2))
print("=> consistent with the beable rotation observed in pt_barandes.py:")
print("   real spectrum, valid process, but NO diagonal metric (K1 broken).")
print("   n=2 has no nontrivial cycles, so within this PT family")
print("   fixed-beable <=> Hermitian; K4 only bites for n >= 3.")

# ----------------------------------------------------------------------
# B. Task (c): 3x3 genuinely non-Hermitian H that PASSES K1-K4
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("B. 3x3 non-Hermitian fixed-beable example (satisfies K1-K4)")
print("=" * 72)
# Build from target weights d = (1,2,4): choose upper entries freely,
# set H_ji = (d_i/d_j) * conj(H_ij). Magnitude-asymmetric => non-Hermitian.
d_target = np.array([1.0, 2.0, 4.0])
H3 = np.zeros((3, 3), dtype=complex)
np.fill_diagonal(H3, [0.3, -0.4, 1.0])                    # K1: real diagonal
uppers = {(0, 1): 1 + 1j, (0, 2): 0.8j, (1, 2): 1.5 * np.exp(1j * np.pi / 5)}
for (i, j), z in uppers.items():
    H3[i, j] = z
    H3[j, i] = (d_target[i] / d_target[j]) * np.conj(z)
print("H =\n", np.round(H3, 4))
print("non-Hermitian:", not np.allclose(H3, H3.conj().T),
      f"| ||H - H^dag|| = {np.linalg.norm(H3 - H3.conj().T):.3f}")
isreal, E3 = real_spectrum(H3)
print("spectrum:", np.round(E3, 4), "| real (Corollary 1):", isreal)
d3, fails = diagonal_metric(H3)
assert d3 is not None, fails
print("recovered diagonal metric d =", np.round(d3, 4),
      "| matches target up to scale:",
      np.allclose(d3 / d3[0], d_target / d_target[0]))
print("nullspace dim (expect 1, connected graph):",
      diagonal_metric_nullspace_dim(H3))
rho3 = np.diag(np.sqrt(d3))          # DIAGONAL rho => beables NOT rotated
U = expm(-1j * H3 * 1.3)
print("naive |U|^2 col sums (not stochastic):",
      np.round((np.abs(U) ** 2).sum(0), 4))
stochastic_report(H3, rho3, label="(fixed-beable) ")
print("beables preserved: rho is diagonal, so Gamma_ij = (d_i/d_j)|U_ij|^2")
Gdirect = np.outer(d3, 1 / d3) * np.abs(U) ** 2
print("  reweighting formula matches:",
      np.allclose(Gdirect, gamma_of(H3, rho3, 1.3)))

# ----------------------------------------------------------------------
# C. The sharp counterexample: K1-K3 hold, ONLY K4 (Kolmogorov) fails,
#    spectrum still real => valid process EXISTS but beables MUST rotate
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("C. 3x3 counterexample: only the Kolmogorov cycle condition fails")
print("=" * 72)
# Real matrix, real diagonal (K1 ok), all couplings positive (K2, K3 ok),
# asymmetric ring: cycle products 0.6^3 = 0.216 vs 0.3^3 = 0.027 (K4 FAILS).
# Real matrix + small coupling vs diagonal gaps => spectrum stays real.
K = np.array([[0, 0.6, 0.3], [0.3, 0, 0.6], [0.6, 0.3, 0]], dtype=complex)
HC = np.diag([1.0, 2.0, 3.0]).astype(complex) + K
print("H =\n", np.round(HC.real, 4))
isreal, EC = real_spectrum(HC)
print("spectrum:", np.round(EC, 4), "| real:", isreal)
dC, fails = diagonal_metric(HC)
print("fixed-beable metric exists:", dC is not None)
for f in fails:
    print("  FAILS ->", f)
print("nullspace dim (expect 0):", diagonal_metric_nullspace_dim(HC))
# ...yet a (non-diagonal) metric exists and gives a valid indivisible process:
_, etaC = biorthogonal_metric(HC)
print("biorthogonal metric eigs (positive definite):",
      np.round(np.linalg.eigvalsh(etaC), 4))
rhoC = sqrtm(etaC)
off = rhoC - np.diag(np.diag(rhoC))
print(f"rho off-diagonal fraction ||offdiag||/||rho|| = "
      f"{np.linalg.norm(off) / np.linalg.norm(rhoC):.4f}  (beables rotate)")
stochastic_report(HC, rhoC, label="(rotated-beable) ")
print("=> K4 gates FIXED BEABLES specifically, not process existence.")

# ----------------------------------------------------------------------
# D. Task (d): the classical detailed-balance dictionary
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("D. Detailed-balance dictionary on example B")
print("=" * 72)
# Rates q(i->j) := |H_ji| (Barandes column convention: U_ji = amplitude i->j).
# Claim: pi ∝ 1/d satisfies classical detailed balance pi_i q_ij = pi_j q_ji.
q = np.abs(H3).T                       # q[i, j] = q(i->j) = |H_{ji}|
pi = (1 / d3) / np.sum(1 / d3)
db = np.abs(pi[:, None] * q - (pi[:, None] * q).T)
print("pi (prop. to 1/d) =", np.round(pi, 4))
print("max detailed-balance violation |pi_i q_ij - pi_j q_ji| =",
      f"{db.max():.2e}")
print("=> metric weights d_i are the INVERSE Kolmogorov equilibrium")
print("   distribution of the classical rate graph q(i->j) = |H_ji|.")
# And on the counterexample the SAME construction has no DB distribution:
qc = np.abs(HC).T
r = np.array([qc[0, 1] / qc[1, 0] * qc[1, 2] / qc[2, 1] * qc[2, 0] / qc[0, 2]])
print(f"counterexample C cycle ratio (want 1 for DB): {r[0]:.3f}")

# ----------------------------------------------------------------------
# E. Randomized verification of the theorem, n = 3..6
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("E. Randomized tests")
print("=" * 72)
rng = np.random.default_rng(0)
n_ok = 0
N_TRIALS = 200
for trial in range(N_TRIALS):
    n = int(rng.integers(3, 7))
    dt = rng.uniform(0.3, 3.0, n)
    H = np.zeros((n, n), dtype=complex)
    np.fill_diagonal(H, rng.normal(size=n))
    for i in range(n):
        for j in range(i + 1, n):
            z = rng.normal() + 1j * rng.normal()
            z += 0.3 * np.sign(z.real) if z.real else 0.3   # keep away from 0
            H[i, j] = z
            H[j, i] = (dt[i] / dt[j]) * np.conj(z)
    # (1) constructor recovers a valid metric, matching target up to scale
    d, fails = diagonal_metric(H)
    assert d is not None, (trial, fails)
    assert np.allclose(d / d[0], dt / dt[0], rtol=1e-8), trial
    assert diagonal_metric_nullspace_dim(H) == 1, trial
    # (2) spectrum real, process doubly stochastic in the fixed beable basis
    isreal, _ = real_spectrum(H)
    assert isreal, trial
    G = gamma_of(H, np.diag(np.sqrt(d)), 0.7)
    assert np.allclose(G.sum(0), 1) and np.allclose(G.sum(1), 1), trial
    assert np.all(G >= -1e-12), trial
    # (3) break one cycle edge's modulus => K4 fails, no diagonal metric
    Hb = H.copy()
    Hb[1, 0] *= 1.7
    db_, fails_b = diagonal_metric(Hb)
    assert db_ is None and any("K4" in f for f in fails_b), (trial, fails_b)
    assert diagonal_metric_nullspace_dim(Hb) == 0, trial
    n_ok += 1
print(f"{n_ok}/{N_TRIALS} random trials passed:")
print("  - K1-K4 satisfied  => diagonal metric found (analytic = nullspace),")
print("    unique up to scale, real spectrum, doubly-stochastic fixed-beable")
print("    Gamma;")
print("  - one cycle modulus perturbed => K4 fails, diagonal metric gone")
print("    (nullspace dim 0).")
print()
print("THEOREM VERIFIED. Quotable form: a PT/pseudo-Hermitian dynamics admits")
print("a fixed-beable indivisible representation iff its coupling graph")
print("satisfies the Kolmogorov cycle (detailed-balance) conditions K1-K4;")
print("the metric weights are then the inverse detailed-balance distribution,")
print("and the fixed-beable process is unique.")
