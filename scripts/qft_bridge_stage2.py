"""
Stage-2 numerics for the QFT bridge (notes.md 2026-07-11, follow-up
thread): does "the ghost is an explosion problem" survive the passage
to QFT vacuum decay?

Four experiments, each with a sharp predicted signature:

E1  FELLER ONSET. Pure-birth ladder with rates lam_n = n^alpha,
    absorbing top at N. Feller: explosion iff sum 1/lam_n < infinity
    iff alpha > 1. Signature (the V4 box-independence diagnostic of
    explosion_theorem.py, transported to Fock space): absorbed mass at
    fixed t is N-INDEPENDENT and -> 1 for alpha > 1; -> 0 with growing
    N for alpha <= 1.

E2  GROWTH-LAW SLOPE. For mean-field growth n(t), the ladder exponent
    is alpha_eff = d log(dn/dt) / d log n. Identity: algebraic blowup
    n ~ (t*-t)^-m gives alpha_eff = 1 + 1/m > 1 (explosive); pure
    exponential growth gives alpha_eff = 1 (transient, marginal).
    Check: (a) quadratic cascade n = sinh^2(gt) -> slope 1.000;
    (b) classical quartic PU blowup (s ~ S tau^-2, energy-proxy
    n ~ s'^2/2 ~ tau^-6) -> slope 7/6 = 1.1667.

E3  CHANNEL MULTIPLICITY (boost-orbit toy). Vacuum |0> at E=0 coupled
    to M identical flat quasi-continua ("channels"; stand-in for the
    non-compact boost orbit of ghost+normal final states). Golden
    rule per channel: Gam_1 = 2 pi g^2 rho. Signature of the CJM side
    of the dichotomy (channels = multiplicity): fitted decay rate
    Gam(M) ~ M * Gam_1, no M -> infinity limit (instantaneous-state
    trend). Control (the GSTZ/cutoff side: orbit measure falls):
    g_k = g e^{-k/4} -> Gam(M) converges.

E4  CLASSICAL LATTICE VACUUM DECAY vs UV CUTOFF. Normal field phi and
    ghost field chi on N sites at FIXED physical volume L (so k_max
    grows with N), coupling +lam phi^2 chi^2, vacuum-mimic
    initial data (zero-point amplitudes 1/sqrt(2 w_k), random phases,
    ensemble-averaged). Observable: time for the normal-sector energy
    to grow by a fixed factor, t_thr(N). Question: does the classical
    decay rate diverge with the UV cutoff (CJM trend) or converge
    (classically UV-finite; the divergence would then be a genuinely
    quantum + Lorentz-measure effect)? No prediction is imposed; the
    trend is the result. lam=0 control must show no growth.

Honest scope: E3 is quantum but zero-dimensional (no boost measure,
just channel counting); E4 is classical field theory. The genuinely
relativistic-quantum statement remains theory-level (notes B2/B4).

Run:  python scripts/qft_bridge_stage2.py     (~1-2 minutes)
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply

rng = np.random.default_rng(7)


# ------------------------------------------------------------------ E1
print("=" * 72)
print("E1. Feller onset: birth ladder lam_n = n^alpha, absorbing top N")
print("    explosion iff alpha > 1;  absorbed mass at t=6, N-dependence")
print("=" * 72)
T_OBS = 6.0
print(f"{'alpha':>6} | " + " ".join(f"N={N:>5}" for N in (200, 400, 800, 1600))
      + " | sum 1/lam_n (N=1600 partial)")
for alpha in (0.8, 1.0, 1.25, 1.5):
    row = []
    for N in (200, 400, 800, 1600):
        lam = np.arange(1, N + 1, dtype=float) ** alpha
        A = diags([-lam, lam[:-1]], [0, -1], format="csc") * T_OBS
        p0 = np.zeros(N)
        p0[0] = 1.0
        p = expm_multiply(A, p0)
        row.append(1.0 - p.sum())
    S = np.sum(1.0 / np.arange(1, 1601, dtype=float) ** alpha)
    print(f"{alpha:>6} | " + " ".join(f"{a:>7.4f}" for a in row)
          + f" | {S:8.3f}")
print("=> alpha>1: absorbed mass ~1, N-independent (EXPLOSIVE, mass")
print("   reaches infinite occupation in finite time); alpha<=1: absorbed")
print("   mass decays with N (regular / at most transient).")

# ------------------------------------------------------------------ E2
print()
print("=" * 72)
print("E2. Growth-law slope alpha_eff = d log(dn/dt) / d log n")
print("=" * 72)
# (a) quadratic cascade, exact law
g = 0.15
t = np.linspace(1.0, 60.0, 4000)
n = np.sinh(g * t) ** 2
ndot = g * np.sinh(2 * g * t)
m = (n > 1e3) & (n < 1e6)
sl_casc = np.polyfit(np.log(n[m]), np.log(ndot[m]), 1)[0]
# (b) classical quartic PU blowup
GAM, W1, W2, LAM = 1.0, 1.0, 0.5, 0.05
OMEGA, WBAR2 = W1**2 + W2**2, (W1 * W2) ** 2


def rhs4(t, y):
    s, s1, s2, s3 = y
    return [s1, s2, s3, 4 * LAM / GAM * s**3 - OMEGA * s2 - WBAR2 * s]


ev = lambda t, y: abs(y[0]) - 1e6
ev.terminal, ev.direction = True, 1
sol = solve_ivp(rhs4, (0, 100), [2.0, 0, 0, 0], rtol=1e-11, atol=1e-11,
                events=ev, dense_output=True)
tt = np.linspace(0.5 * sol.t[-1], 0.999 * sol.t[-1], 3000)
ys = sol.sol(tt)
npu = 0.5 * (ys[1] ** 2 + ys[0] ** 2)
npudot = ys[1] * ys[2] + ys[0] * ys[1]
m = (npu > 1e4) & (npu < 1e9) & (npudot > 0)
sl_pu = np.polyfit(np.log(npu[m]), np.log(npudot[m]), 1)[0]
print(f"quadratic cascade n=sinh^2(gt):  slope = {sl_casc:.4f}  "
      f"(predict 1.0000: exponential growth, transient)")
print(f"quartic PU blowup (energy proxy): slope = {sl_pu:.4f}  "
      f"(predict 7/6 = {7/6:.4f}: algebraic blowup n~tau^-6, explosive)")
print("=> the transient/explosive dichotomy of the paper IS the Feller")
print("   dichotomy alpha_eff = 1 vs alpha_eff > 1 of E1.")

# ------------------------------------------------------------------ E3
print()
print("=" * 72)
print("E3. Channel multiplicity: vacuum coupled to M flat quasi-continua")
print("=" * 72)
G0, WBAND, NB = 0.02, 8.0, 161
RHO = NB / (2 * WBAND)
GAM1 = 2 * np.pi * G0**2 * RHO
T_REC = 2 * np.pi * RHO          # level-spacing recurrence time
Elev = np.linspace(-WBAND, WBAND, NB)


def fitted_rate(M, cutoff):
    gks = G0 * (np.exp(-np.arange(M) / 4.0) if cutoff else np.ones(M))
    dim = 1 + M * NB
    H = np.zeros((dim, dim))
    for k in range(M):
        i0 = 1 + k * NB
        H[i0:i0 + NB, i0:i0 + NB] = np.diag(Elev)
        H[0, i0:i0 + NB] = gks[k]
        H[i0:i0 + NB, 0] = gks[k]
    w, V = np.linalg.eigh(H)
    c0 = V[0, :]
    gam_pred = 2 * np.pi * np.sum(gks**2) * RHO
    tf = min(2.5 / gam_pred, 0.4 * T_REC)
    ts = np.linspace(0.15 * tf, tf, 12)
    amp = np.array([np.sum(np.abs(c0) ** 2 * np.exp(-1j * w * t))
                    for t in ts])
    surv = np.abs(amp) ** 2
    sl = np.polyfit(ts, np.log(surv), 1)[0]
    return -sl, gam_pred


print(f"per-channel golden-rule rate Gam_1 = 2 pi g^2 rho = {GAM1:.4f}")
print(f"{'M':>4} | {'flat: fit':>10} {'pred M*Gam1':>12} | "
      f"{'cutoff: fit':>11} {'pred':>8}")
for M in (1, 2, 4, 8, 16, 32):
    gf, pf = fitted_rate(M, cutoff=False)
    gc, pc = fitted_rate(M, cutoff=True)
    print(f"{M:>4} | {gf:>10.4f} {pf:>12.4f} | {gc:>11.4f} {pc:>8.4f}")
print("=> flat orbit measure: Gam ~ M Gam_1, grows without bound with")
print("   channel count while Gam << bandwidth (instantaneous-state")
print("   trend, the CJM horn); decaying measure: Gam converges (the")
print("   metastable/GSTZ horn). Channel counting is the whole")
print("   difference. (With a FINITE band the growth would eventually")
print("   saturate at the hybridization ceiling Gam ~ W -- absent for")
print("   the genuinely unbounded boost-orbit continua.)")

# ------------------------------------------------------------------ E4
print()
print("=" * 72)
print("E4. Classical lattice vacuum decay vs UV cutoff (fixed volume)")
print("=" * 72)
L, MASS, LAMF, NENS, DE_ABS = 32.0, 1.0, 0.25, 8, 25.0


def omega_k(N):
    k = 2 * np.pi * np.fft.fftfreq(N, d=L / N)
    dx = L / N
    return np.sqrt(MASS**2 + (2 / dx**2) * (1 - np.cos(k * dx)))


def vacuum_field(N):
    wk = omega_k(N)
    c = (rng.standard_normal(N) + 1j * rng.standard_normal(N)) / np.sqrt(2)
    f = np.fft.ifft(c * np.sqrt(N / (2 * wk))).real * np.sqrt(2)
    cp = (rng.standard_normal(N) + 1j * rng.standard_normal(N)) / np.sqrt(2)
    fp = np.fft.ifft(cp * np.sqrt(N * wk / 2)).real * np.sqrt(2)
    return f, fp


def lap(f, dx):
    return (np.roll(f, 1) + np.roll(f, -1) - 2 * f) / dx**2


def e_phi(phi, pphi, dx):
    gphi = (np.roll(phi, -1) - phi) / dx
    return np.sum(0.5 * pphi**2 + 0.5 * gphi**2 + 0.5 * MASS**2 * phi**2) * dx


def t_threshold(N, lam):
    dx = L / N
    times = []
    for _ in range(NENS):
        phi, pphi = vacuum_field(N)
        chi, pchi = vacuum_field(N)
        e0 = e_phi(phi, pphi, dx)

        def rhs(t, y):
            ph, pp, ch, pc = y.reshape(4, N)
            dph = pp
            dpp = lap(ph, dx) - MASS**2 * ph - 2 * lam * ch**2 * ph
            dch = pc
            dpc = lap(ch, dx) - MASS**2 * ch + 2 * lam * ph**2 * ch
            return np.concatenate([dph, dpp, dch, dpc])

        hit = lambda t, y: e_phi(y[:N], y[N:2 * N], dx) - (e0 + DE_ABS)
        hit.terminal, hit.direction = True, 1
        s = solve_ivp(rhs, (0, 400.0),
                      np.concatenate([phi, pphi, chi, pchi]),
                      rtol=1e-8, atol=1e-8, events=hit, max_step=0.05)
        times.append(s.t_events[0][0] if len(s.t_events[0]) else np.inf)
    return np.array(times)


print(f"time for the normal sector to ABSORB a fixed energy "
      f"DE={DE_ABS:.0f} (lam={LAMF}, L={L:.0f}, median of {NENS}; "
      f"absolute threshold, so the rising zero-point baseline at "
      f"large N cannot mask the trend):")
print(f"{'N':>4} {'k_max':>7} | {'median t_thr':>12} {'rate 1/t':>9} | "
      f"{'lam=0 control':>13}")
for N in (8, 16, 32, 64):
    tt_i = t_threshold(N, LAMF)
    tt_c = t_threshold(N, 0.0)
    med = np.median(tt_i)
    ctrl = ("no growth" if np.all(np.isinf(tt_c))
            else f"{np.median(tt_c):.1f}")
    kmax = np.pi / (L / N)
    rate = (1.0 / med) if np.isfinite(med) else 0.0
    print(f"{N:>4} {kmax:>7.2f} | {med:>12.2f} {rate:>9.4f} | {ctrl:>13}")
print("=> trend of rate vs k_max is the result (divergent = CJM-like UV")
print("   sensitivity already classically; convergent = classical decay")
print("   is UV-finite and the QFT divergence is quantum/measure-driven).")
print()
print("done.")
