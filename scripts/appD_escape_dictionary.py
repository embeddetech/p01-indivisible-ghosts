"""
Appendix D (the multidimensional escape dictionary) -- numerical checks.
Backs the two quoted numeric claims in App D of paper1/main.tex:
  * cor:app-central  -- central potential H = -1/2 Delta - c|x|^alpha:
      radial escape time-of-flight T_ell, its ratio -> 10^{1/3}=2.154,
      and the shape constant C_alpha.
  * prop:app-ce1     -- shelf potential Counterexample I: per-channel
      T_m all <= 3/2 (T_1=1.17, T_3=1.01, T_8=1.00001) while the
      position-locked ride gives T_eff = infinity.
Standalone, runs in ~1 s. No long integrations.
"""
import numpy as np
from scipy import integrate
from scipy.optimize import brentq


# ------------------------------------------------------------------
# cor:app-central : T_ell = int_{r_ell}^inf dr / sqrt(2(E + c r^a - L^2/(2 r^2)))
#   escaping end r->inf (potential -c r^a); E=0; r_ell = outer turning point.
#   Softening substitution r = r_ell + s^2 kills the (r-r_ell)^{-1/2} edge.
# ------------------------------------------------------------------
def T_central(Lsq, alpha=4.0, c=1.0, E=0.0):
    def arg(r):
        return E + c * r**alpha - Lsq / (2.0 * r * r)
    r_scale = (Lsq / (2.0 * c)) ** (1.0 / (alpha + 2.0))     # E=0 turning point
    r_ell = brentq(arg, r_scale * 0.5, r_scale * 2.0)
    smax = np.sqrt(1e7)                                       # r up to ~1e7
    def integrand(s):
        r = r_ell + s * s
        return 2.0 * s / np.sqrt(2.0 * arg(r))
    val, _ = integrate.quad(integrand, 0.0, smax, limit=400)
    return r_ell, val

def C_alpha(alpha=4.0):
    # C_a = int_{rho0}^inf (2(rho^a - 1/2 rho^{-2}))^{-1/2} d rho, rho0 turning pt
    def arg(rho):
        return rho**alpha - 0.5 * rho**(-2.0)
    rho0 = (0.5) ** (1.0 / (alpha + 2.0))
    smax = np.sqrt(1e7)
    def integrand(s):
        rho = rho0 + s * s
        return 2.0 * s / np.sqrt(2.0 * arg(rho))
    val, _ = integrate.quad(integrand, 0.0, smax, limit=400)
    return val

print("== cor:app-central (alpha=4, c=1, E=0) ==")
Ts = []
for Lsq in [1e2, 1e4, 1e6]:
    r_ell, T = T_central(Lsq)
    Ts.append(T)
    print(f"  L^2={Lsq:.0e}: r_ell={r_ell:.4f}  T_ell={T:.4f}   (paper: 0.447/0.208/0.096)")
print(f"  successive ratios: {Ts[0]/Ts[1]:.4f}, {Ts[1]/Ts[2]:.4f}   (paper 2.154 vs 10^(1/3)={10**(1/3):.4f})")
print(f"  C_alpha={C_alpha():.4f}")


# ------------------------------------------------------------------
# prop:app-ce1 : shelf potential.  E=0, E_n = 16^n (n>=1).
#   V_1 = -E_n - 1/2 on [2n, 2n+1]; linear on [2n+1, 2n+2].
#   channel m open from x_m=2m; T_m = int_{2m}^inf dx / sqrt(2(-E_m - V_1)).
# ------------------------------------------------------------------
def En(n):
    return 16.0 ** n

def V1(x):
    n = int(np.floor(x / 2.0))
    if n < 1:
        n = 1
    xs = x - 2 * n
    if xs <= 1.0:                       # shelf n
        return -En(n) - 0.5
    # linear drop from -En(n)-1/2 to -En(n+1)-1/2 over xs in [1,2]
    frac = xs - 1.0
    return (-En(n) - 0.5) * (1 - frac) + (-En(n + 1) - 0.5) * frac

def T_shelf(m, n_top=40):
    Em = En(m)
    def integrand(x):
        val = 2.0 * (-Em - V1(x))
        return 1.0 / np.sqrt(val) if val > 1e-300 else 0.0
    # integrate shelf-by-shelf to keep the piecewise structure clean
    total = 0.0
    for n in range(m, n_top):
        a, b = 2 * n, 2 * n + 2
        seg, _ = integrate.quad(integrand, a, b, limit=200)
        total += seg
    return total

print("\n== prop:app-ce1 (shelf E_n=16^n) ==")
for m in [1, 3, 8]:
    print(f"  T_{m} = {T_shelf(m):.5f}   (paper: T_1=1.17, T_3=1.01, T_8=1.00001; all <= 3/2)")

# ride: n(x)=n on [2n,2n+2), effective speed on shelf n is sqrt(2*(1/2))=1
#   over unit length -> each shelf contributes exactly 1 -> T_eff = inf.
print("  T_eff (position-locked ride): sum of 1-per-shelf -> infinity  (analytic)")
