"""
A genuine (non-compact) von Neumann certificate in 1D: WKB tails glued
to an exact interior solution.

LESSON FROM tail_certificate.py (and a small theorem): any compactly
supported smooth function lies in D(S-bar), where
||(S - iZ)psi|| >= Z ||psi|| holds unconditionally -- so NO windowed /
truncated candidate can ever witness deficiency, for any operator. The
completion data lives entirely at infinity. A real certificate must
supply candidates with controlled ANALYTIC TAILS.

CONSTRUCTION (1D, S = -a psi'' + U psi, z = iZ, q = (z - U)/a):
  right tail  k >= +K1:   psi = q^{-1/4} exp(+i int sqrt(q))     (WKB)
  interior    |k| <= K1:  exact ODE integration, C^1-matched at +K1
  left tail   k <= -K1:   the arrived solution decomposed into the two
                          left WKB branches and continued analytically.
The ONLY residual is the WKB remainder,
  (S - z) psi_WKB = -a [ q''/(4q) - (5/16)(q'/q)^2 ] psi_WKB,
which decays like k^{-2} psi for polynomial potentials: the candidate is
smooth, non-compact, in D(S*), and its ratio ||(S-z)psi||/(Z||psi||) is
computable with tail quadratures. Ratio < 1 PROVES the operator is not
essentially self-adjoint. The method is intrinsically sharp:
  - falling quartic (limit circle): both left branches are L^2
    (|psi|^2 ~ 1/k^2), remainder integrable  -> certificate expected;
  - confining quartic (e.s.a.): the left continuation contains a
    growing REAL exponential branch: no L^2 candidate exists;
  - falling quadratic (limit point, marginal): the growing branch is
    polynomial, |psi| ~ k^{-1/2 + Z/1.12}, whose density integral
    diverges for EVERY Z > 0: no candidate (the decaying branch is
    the unique L^2 solution -- limit point, as the dictionary
    requires). The constant 1.12 is ANALYTIC, not fitted: for
    U = -c k^2, sqrt(q) = sqrt(c/A)(k + iZ/(2ck) + O(k^-3)), so
    Im int sqrt(q) = (Z / (2 sqrt(A c))) ln k + O(1) and the WKB
    branches obey |psi| ~ k^{-1/2 -+ Z/(2 sqrt(A c))}; with A = 0.4,
    c = 0.78 this gives 2 sqrt(A c) = 1.117 ~ 1.12. The script
    computes this constant and checks the growing branch's log-log
    slope against it (marginal_exponent below).
The pipeline reports these failures via the divergence of the left-tail
norm integrand.

This machine-checks the 1D fiber case end-to-end and identifies exactly
what a full 2D proof must supply: the analytic beam tails of the
(k,p)-operator under the ridge drift.

Run:  python glued_certificate_1d.py     (seconds)
"""

import numpy as np
from scipy.integrate import solve_ivp, quad

A = 0.4          # 1/(2 gamma Omega)
Z = 6.0
LAMQ = 0.05


def make_case(Ufun, dU, d2U, label):
    q = lambda k: (1j * Z - Ufun(k)) / A
    qp = lambda k: -dU(k) / A
    qpp = lambda k: -d2U(k) / A

    def sqrt_q(k):
        r = np.sqrt(q(k) + 0j)
        return r if r.imag >= 0 else -r      # decaying-to-the-right

    def eps(k):                              # WKB remainder coefficient
        return A * (qpp(k) / (4 * q(k)) - (5 / 16) * (qp(k) / q(k)) ** 2)

    return dict(q=q, qp=qp, sq=sqrt_q, eps=eps, U=Ufun, label=label)


def run(case, K1=8.0, kfar=3000.0):
    q, qp, sq, eps = case["q"], case["qp"], case["sq"], case["eps"]
    lab = case["label"]

    # ---- right tail: psi_R = q^{-1/4} e^{+i Phi}, Phi' = sq ----------
    # densities relative to |psi(K1)| = |q(K1)|^{-1/4}
    def tail_pieces(sgn):
        """Integrate |psi|^2 and |eps psi|^2 along k = K1..kfar for the
        branch with phase sgn * i * int sq (right tail: sgn=+1 decaying).
        Returns (norm2, res2, growing?) with growth detection."""
        ks = np.geomspace(K1, kfar, 4000)
        phi_im = np.concatenate([[0.0], np.cumsum(
            0.5 * (np.array([sq(k).imag for k in ks[1:]])
                   + np.array([sq(k).imag for k in ks[:-1]]))
            * np.diff(ks))])
        lp = -0.5 * np.log(np.abs([q(k) for k in ks])) / 2
        logd = 2 * (lp - sgn * phi_im)        # log |psi|^2
        logd -= logd[0]
        d = np.exp(np.clip(logd, -700, 700))
        e2 = np.array([abs(eps(k)) ** 2 for k in ks])
        n2 = np.trapezoid(d, ks)
        r2 = np.trapezoid(e2 * d, ks)
        growing = logd[-1] > logd[0] + 2.0
        return n2, r2, growing

    nR, rR, gR = tail_pieces(+1)
    if gR:
        print(f"  {lab}: right tail not integrable -- no candidate")
        return
    # normalize tail densities to |psi(K1)|^2 = |q(K1)|^{-1/2} scale 1
    # (we work relative to psi(K1) = q(K1)^{-1/4})

    # ---- interior: exact ODE from +K1 to -K1 ------------------------
    k1v = K1
    psi1 = q(k1v) ** (-0.25)
    dpsi1 = psi1 * (-0.25 * qp(k1v) / q(k1v) + 1j * sq(k1v))

    def rhs(k, y):
        return [y[1], -q(k) * y[0]]

    sol = solve_ivp(rhs, (K1, -K1), [psi1, dpsi1], rtol=1e-11,
                    atol=1e-14, dense_output=True, max_step=0.01)
    kk = np.linspace(-K1, K1, 20001)
    vals = sol.sol(kk)[0]
    scale = abs(psi1)
    n_int = np.trapezoid(np.abs(vals) ** 2, kk) / scale ** 2

    # ---- left decomposition and tails --------------------------------
    pm, dpm = sol.sol(-K1)[0], sol.sol(-K1)[1]
    qm = q(-K1)
    sqm = sq(-K1)                      # branch with Im >= 0
    # left WKB branches: psi_pm ~ q^{-1/4} e^{ +- i int_{-K1}^{k} sq }
    # at k = -K1: value q^{-1/4}, derivative q^{-1/4}(-qp/(4q) +- i sq)
    w = qm ** (-0.25)
    dw_a = w * (-0.25 * qp(-K1) / qm + 1j * sqm)
    dw_b = w * (-0.25 * qp(-K1) / qm - 1j * sqm)
    M = np.array([[w, w], [dw_a, dw_b]])
    Aa, Ab = np.linalg.solve(M, np.array([pm, dpm]))

    def tail_left(sgn):
        ks = np.geomspace(K1, kfar, 4000)     # mirror variable k -> -k
        sqv_im = np.array([np.sqrt(q(-k) + 0j).imag for k in ks])
        # branch continued to the left with phase sgn: |e^{sgn i int}|:
        # moving left, d(phase)/d(-k): use symmetric potentials (all our
        # cases are even), so mirror of the right tail applies.
        phi_im = np.concatenate([[0.0], np.cumsum(
            0.5 * (np.abs(sqv_im[1:]) + np.abs(sqv_im[:-1]))
            * np.diff(ks))])
        lp = -0.5 * np.log(np.abs([q(-k) for k in ks])) / 2
        logd = 2 * (lp - sgn * phi_im)
        logd -= logd[0]
        d = np.exp(np.clip(logd, -700, 700))
        e2 = np.array([abs(eps(-k)) ** 2 for k in ks])
        n2 = np.trapezoid(d, ks)
        r2 = np.trapezoid(e2 * d, ks)
        growing = logd[-1] > logd[0] + 2.0
        return n2, r2, growing

    nLa, rLa, gLa = tail_left(+1)          # decaying-leftward branch
    nLb, rLb, gLb = tail_left(-1)          # growing-leftward branch
    if gLb and abs(Ab) > 1e-12 * abs(Aa):
        print(f"  {lab}: left continuation contains a non-L^2 branch "
              f"(|A_grow/A_decay| = {abs(Ab / Aa):.2e}) -- NO candidate;")
        print("    certificate unattainable, consistent with essential "
              "self-adjointness / limit point")
        return
    wm2 = abs(w) ** 2 / scale ** 2
    norm2 = (nR + n_int
             + wm2 * (abs(Aa) ** 2 * nLa + abs(Ab) ** 2 * nLb))
    res2 = (rR + wm2 * (abs(Aa) ** 2 * rLa + abs(Ab) ** 2 * rLb))
    ratio = np.sqrt(res2 / norm2) / Z
    print(f"  {lab}:")
    print(f"    ratio ||(S-iZ)psi|| / (Z||psi||) = {ratio:.5f}   "
          f"[{'CERTIFIED: NOT e.s.a.' if ratio < 1 else 'no certificate'}]")
    print(f"    (interior/right/left norm shares: {n_int/norm2:.2f} / "
          f"{nR/norm2:.2f} / {1 - (n_int + nR)/norm2:.2f})")


print("=" * 72)
print(f"Glued-tail von Neumann certificates, z = {Z}i")
print("=" * 72)
run(make_case(lambda k: -LAMQ * k ** 4, lambda k: -4 * LAMQ * k ** 3,
              lambda k: -12 * LAMQ * k ** 2,
              "falling quartic U = -0.05 k^4  (limit circle)"))
run(make_case(lambda k: +LAMQ * k ** 4, lambda k: 4 * LAMQ * k ** 3,
              lambda k: 12 * LAMQ * k ** 2,
              "confining quartic U = +0.05 k^4  (e.s.a.)"))
run(make_case(lambda k: -0.78 * k ** 2, lambda k: -1.56 * k,
              lambda k: -1.56 + 0 * k,
              "falling quadratic U = -0.78 k^2  (limit point, marginal)"))


def marginal_exponent(c=0.78, klo=2e2, khi=3e3, n=4000):
    """Provenance of the marginal-branch exponent k^{-1/2 + Z/1.12}
    quoted in the manuscript (S10).  For U = -c k^2,
        sqrt(q) = sqrt((iZ + c k^2)/A)
                = sqrt(c/A) (k + i Z/(2 c k) + O(k^-3)),
    so Im int sqrt(q) dk = (Z / (2 sqrt(A c))) ln k + O(1); with the
    WKB prefactor |q|^{-1/4} ~ k^{-1/2} the two branches obey
        |psi| ~ k^{-1/2 -+ Z / (2 sqrt(A c))}.
    Hence the constant is 2 sqrt(A c) = 1.117 ~ 1.12 (A = 0.4,
    c = 0.78) -- analytic, not fitted.  The growing branch's density
    ~ k^{-1 + Z/sqrt(A c)} is non-integrable for every Z > 0: limit
    point.  Numeric check: log-log slope of the exact (unexpanded)
    growing WKB branch against the analytic exponent."""
    ks = np.geomspace(klo, khi, n)
    qv = (1j * Z + c * ks ** 2) / A
    im = np.sqrt(qv).imag                     # exact Im sqrt(q) > 0
    phi = np.concatenate([[0.0], np.cumsum(
        0.5 * (im[1:] + im[:-1]) * np.diff(ks))])
    logpsi = -0.25 * np.log(np.abs(qv)) + phi     # growing branch
    slope = np.polyfit(np.log(ks), logpsi, 1)[0]
    const = 2 * np.sqrt(A * c)
    print()
    print(f"  marginal-branch exponent, U = -{c} k^2 (provenance of 1.12):")
    print(f"    analytic: |psi| ~ k^(-1/2 + Z/(2 sqrt(A c))),  "
          f"2 sqrt(A c) = {const:.5f}  (quoted as 1.12)")
    print(f"    numeric log-log slope of growing WKB branch = {slope:.4f}"
          f"   vs analytic -1/2 + Z/{const:.4f} = {-0.5 + Z / const:.4f}")
    print(f"    density exponent -1 + Z/sqrt(A c) = "
          f"{-1 + Z / np.sqrt(A * c):.4f} > -1 for every Z > 0: "
          f"never L^2 (limit point)")


marginal_exponent()
print()
print("The falling-quartic certificate is the 1D fiber of the quartic")
print("PU. The 2D extension requires the analytic beam tails of the")
print("(k,p) operator under the ridge drift -- the precise specialist")
print("gap for the M -> infinity question.")
