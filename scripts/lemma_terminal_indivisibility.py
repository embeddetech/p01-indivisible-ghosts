"""
Analytic lemma: TERMINAL INDIVISIBILITY of the broken-PT reduced process.
(Promotes finding 1 of section 5.2 / dilation_bridge.py to a theorem.)

SETUP. Dimer H = cos(th) I + i sin(th) sigma_z + s sigma_x; loss frame
H_loss = H - i sin(th) I; reduced process Gamma(t) = |exp(-i H_loss t)|^2
(entrywise). Write A = i sin(th) sigma_z + s sigma_x. Then A^2 =
(s^2 - sin^2 th) I, so with kappa~ = sqrt(sin^2 th - s^2) > 0 (broken phase):

    exp(-iAt) = cosh(kt) I - i (sinh(kt)/k) A,   k = kappa~ ,

and with  c = cosh kt, shc = sinh(kt)/k,
    p = c + sin(th) shc,  q = c - sin(th) shc,  r = s shc:

    Gamma(t) = e^{-2 sin(th) t} [[p^2, r^2], [r^2, q^2]],
    det Gamma = e^{-4 sin(th) t} (1 - 2 r^2).

LEMMA. The generator L = Gamma' Gamma^{-1} has EXACT off-diagonals
    L_12 = 2 s p r / (1 - 2 r^2),      L_21 = 2 s q r / (1 - 2 r^2),
because the Wronskian-type combinations r'p - p'r and r'q - q'r are both
identically equal to s (constant in t). Consequences (broken phase):

 (i)   P-divisible precisely on [0, t_c),
         t_c = (1/k) arcsinh( k / (s sqrt(2)) ),
       which is EXACTLY the time at which det Gamma crosses zero
       (r^2 = 1/2). Divisibility dies when and because the process
       becomes singular.
 (ii)  For ALL t > t_c: 1 - 2r^2 < 0 while p, r > 0, hence L_12 < 0
       strictly, FOREVER: permanent (terminal) indivisibility.
 (iii) L_12 -> -( sin(th) + k ) as t -> infinity: a strictly negative
       floor (numerically observed -1.207 at th=pi/4, s=0.5: here
       sin th + k = 0.7071 + 0.5 = 1.2071).
 (iv)  q flips sign at t_0 = (1/k) artanh(k / sin th) > t_c, after which
       L_21 > 0 again: only ONE off-diagonal remains negative at late
       times.
 (v)   The SAME formulas continue to the unbroken phase (k -> i kappa,
       cosh -> cos, sinh/k -> sin/kappa): 1 - 2r^2 = 1 - 2(s/kappa)^2
       sin^2(kappa t) oscillates through zero forever (note (s/kappa)^2 =
       s^2/(s^2 - sin^2 th) > 1 always), giving the RECURRENT
       indivisibility windows; and at the EP everything is polynomial
       (r = s t, t_c = 1/(s sqrt(2))), with t_c continuous across the
       transition.

This script verifies every claim numerically against brute-force
Gamma' Gamma^{-1} computed from matrix exponentials.

Run:  python lemma_terminal_indivisibility.py
"""

import numpy as np
from scipy.linalg import expm

np.set_printoptions(precision=4, suppress=True)
I2 = np.eye(2, dtype=complex)


def H_loss(th, s):
    H = np.array([[np.exp(1j * th), s], [s, np.exp(-1j * th)]],
                 dtype=complex)
    return H - 1j * np.sin(th) * I2


def pqr(th, s, t):
    """Unified analytic elements (complex k handles both phases)."""
    k = np.sqrt(np.sin(th) ** 2 - s ** 2 + 0j)
    c = np.cosh(k * t)
    shc = t if abs(k) < 1e-14 else np.sinh(k * t) / k
    p = (c + np.sin(th) * shc).real
    q = (c - np.sin(th) * shc).real
    r = (s * shc).real
    return p, q, r


def L_analytic(th, s, t):
    p, q, r = pqr(th, s, t)
    det = 1 - 2 * r ** 2
    return 2 * s * p * r / det, 2 * s * q * r / det


def gamma_analytic(th, s, t):
    p, q, r = pqr(th, s, t)
    return np.exp(-2 * np.sin(th) * t) * np.array([[p * p, r * r],
                                                   [r * r, q * q]])


def L_numeric(th, s, t):
    Hl = H_loss(th, s)
    C = expm(-1j * Hl * t)
    G = np.abs(C) ** 2
    Gdot = 2 * np.real(np.conj(C) * (-1j * Hl @ C))
    L = Gdot @ np.linalg.inv(G)
    return L[0, 1], L[1, 0], G


def tc(th, s):
    k2 = np.sin(th) ** 2 - s ** 2
    if k2 > 0:
        k = np.sqrt(k2)
        return np.arcsinh(k / (s * np.sqrt(2))) / k
    if k2 < 0:
        ka = np.sqrt(-k2)
        return np.arcsin(ka / (s * np.sqrt(2))) / ka
    return 1 / (s * np.sqrt(2))


# ----------------------------------------------------------------------
# 1. Exactness of the closed forms (both phases, several parameters)
# ----------------------------------------------------------------------
print("=" * 72)
print("1. Closed forms vs brute numerics")
print("=" * 72)
cases = [(np.pi / 4, 0.3), (np.pi / 4, 0.5), (np.pi / 3, 0.5),   # broken
         (np.pi / 4, 1.0), (np.pi / 6, 0.8), (np.pi / 4, 0.72)]  # unbroken
worst_G, worst_L = 0.0, 0.0
for th, s in cases:
    for t in np.arange(0.1, 10.01, 0.1):
        Ga = gamma_analytic(th, s, t)
        l12n, l21n, Gn = L_numeric(th, s, t)
        worst_G = max(worst_G, np.abs(Ga - Gn).max() / max(Gn.max(), 1e-30))
        _, _, r = pqr(th, s, t)
        if abs(1 - 2 * r * r) < 5e-3:        # skip the det-zero singularity
            continue
        l12a, l21a = L_analytic(th, s, t)
        worst_L = max(worst_L,
                      abs(l12a - l12n) / max(abs(l12a), 1),
                      abs(l21a - l21n) / max(abs(l21a), 1))
print(f"max relative error, Gamma formula:      {worst_G:.2e}")
print(f"max relative error, L_12/L_21 formulas: {worst_L:.2e}")
print("(over 6 parameter sets x t in [0.1, 10], both phases)")

# ----------------------------------------------------------------------
# 2. Claim (i): t_c = divisibility loss = det-zero crossing
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("2. t_c: divisibility dies exactly where det Gamma crosses zero")
print("=" * 72)
for th, s in [(np.pi / 4, 0.3), (np.pi / 4, 0.5), (np.pi / 3, 0.5)]:
    t_c = tc(th, s)
    # bracket the numerical sign change of min offdiag L around t_c
    eps = 1e-6
    lo = min(L_numeric(th, s, t_c - eps)[:2])
    hi = min(L_numeric(th, s, t_c + eps)[:2])
    detG = np.linalg.det(L_numeric(th, s, t_c)[2])
    print(f"th={th:.4f} s={s}:  t_c = {t_c:.6f} | min offdiag L at "
          f"t_c -+ 1e-6: {lo:+.4e} / {hi:+.4e} | det Gamma(t_c) = "
          f"{detG:+.2e}")
print("=> sign change straddles t_c; det Gamma vanishes there. Matches")
print("   dilation_bridge.py numerics (s=0.5: t* = 1.35 on a 0.05 grid;")
print(f"   exact t_c = {tc(np.pi / 4, 0.5):.4f}).")

# ----------------------------------------------------------------------
# 3. Claims (ii)+(iii): permanent negativity and the exact floor
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("3. Permanence and the asymptotic floor  L_12 -> -(sin th + k)")
print("=" * 72)
for th, s in [(np.pi / 4, 0.3), (np.pi / 4, 0.5), (np.pi / 3, 0.5)]:
    k = np.sqrt(np.sin(th) ** 2 - s ** 2)
    t_c = tc(th, s)
    grid = np.arange(t_c + 0.01, 14.0, 0.01)
    l12 = np.array([L_analytic(th, s, t)[0] for t in grid])
    floor = -(np.sin(th) + k)
    l12_num = L_numeric(th, s, 12.0)[0]
    print(f"th={th:.4f} s={s}:  max L_12 on (t_c, 14] = {l12.max():+.4f} "
          f"(< 0) | predicted floor {floor:+.4f} | numeric L_12(12) = "
          f"{l12_num:+.4f}")
print("=> strictly negative for every t > t_c; floor exact. The observed")
print("   -1.207 at s=0.5 is -(sin(pi/4) + 0.5) = -1.2071.")

# ----------------------------------------------------------------------
# 4. Claim (iv): L_21 returns positive after t_0 (one-sided negativity)
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("4. t_0 = artanh(k/sin th)/k: L_21 flips back positive")
print("=" * 72)
th, s = np.pi / 4, 0.5
k = np.sqrt(np.sin(th) ** 2 - s ** 2)
t0 = np.arctanh(k / np.sin(th)) / k
for t in (tc(th, s) + 0.1, t0 - 0.05, t0 + 0.05, 6.0):
    l12, l21 = L_analytic(th, s, t)
    print(f"  t = {t:6.3f}:  L_12 = {l12:+8.4f}   L_21 = {l21:+8.4f}")
print(f"t_0 = {t0:.4f} > t_c = {tc(th, s):.4f}: late-time indivisibility is")
print("carried entirely by L_12 (transitions INTO the gain site).")

# ----------------------------------------------------------------------
# 5. Claim (v): unbroken recurrence and EP continuity from one formula
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("5. One formula, three regimes")
print("=" * 72)
th = np.pi / 4
s_up, s_dn = np.sin(th) * (1 + 1e-4), np.sin(th) * (1 - 1e-4)
print(f"t_c continuity at the EP: broken side {tc(th, s_dn):.6f} | "
      f"EP 1/(s sqrt2) = {1 / (np.sin(th) * np.sqrt(2)):.6f} | "
      f"unbroken side {tc(th, s_up):.6f}")
s = 1.0
kappa = np.sqrt(s ** 2 - np.sin(th) ** 2)
zeros = []
grid = np.arange(0.01, 12.0, 0.005)
vals = 1 - 2 * (s / kappa) ** 2 * np.sin(kappa * grid) ** 2
sign_flips = np.sum(np.abs(np.diff(np.sign(vals))) > 0)
print(f"unbroken s=1: det factor 1 - 2(s/kappa)^2 sin^2(kappa t) has "
      f"{sign_flips} sign changes on (0, 12]")
print("=> recurrent divisible/indivisible windows, period pi/kappa = "
      f"{np.pi / kappa:.3f} -- the closed-system quasi-periodicity;")
print("   broken phase: hyperbolic, ONE crossing, permanent. QED.")
