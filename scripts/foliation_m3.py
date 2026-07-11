"""
M3 — the foliation experiment: who individuates the frame, the state
or the regulator?

Setup (1+1d lattice, fixed physical volume L): normal field phi and
ghost field chi coupled by lam*phi^2*chi^2, prepared in a BOOSTED
thermal state — classical Juttner occupations n(k) = T/(u.k),
u = gamma*(1, v), built as traveling waves so the phi-pi correlation
carries the propagation direction — with fixed spectral support
|k| <= K_C independent of the lattice. The lattice spacing (UV
regulator, and its non-invariant dispersion) defines a SECOND frame.
Switching on the ghost coupling transfers energy into the normal
sector ("vacuum decay" stimulated by the bath); we measure the frame
of the produced radiation via

    v* = Delta P_phi / Delta E_phi

evaluated when the normal sector has absorbed a fixed energy DE_THR.
Exact kinematic targets: production isotropic in the STATE frame
=> v* = v (pair momenta cancel in the state frame, boost supplies
gamma*v*DeltaE' / gamma*DeltaE' = v, mass-independent); production
anchored to the LATTICE frame => v* = 0.

The experiment: sweep the lattice cutoff N (16..128) at fixed state.
If v*(N) stays locked near v as N grows, the frame is selected by
the state (spontaneously, physically) — the "cosmological state
picks the foliation" claim, in silico. If v*(N) drifts toward 0,
the individuation is genuinely a UV/regulator effect (the CJM
picture). Controls: v = 0 (target 0 by symmetry), lam = 0 (no
transfer).

Remark (F3 in the notes): this experiment is POSSIBLE only because a
thermal state has a rest frame. The vacuum cannot be boosted — a
vacuum run has only the lattice frame, which is the foliation-
indeterminacy statement in experimental form.

Run:  python scripts/foliation_m3.py     (several minutes)
"""

import numpy as np
from scipy.integrate import solve_ivp

L, MASS = 32.0, 1.0
K_C, VSTATE, LAM = 1.2, 0.35, 0.3
T_PHI, T_CHI = 1.0, 2.0        # ghost bath hotter: GSTZ drift
                               # ~ T1*T2*(T2-T1) vanishes at equal T
NENS, TEND = 16, 80.0
rng = np.random.default_rng(11)


def omega(k):
    return np.sqrt(MASS**2 + k**2)          # continuum dispersion for ICs


def boosted_bath(N, v, temp):
    """Traveling-wave thermal state, occupations n(k)=T/(u.k),
    support |k|<=K_C. Returns (field, pi_field)."""
    dx = L / N
    x = np.arange(N) * dx
    gam = 1.0 / np.sqrt(1 - v**2)
    f = np.zeros(N)
    fp = np.zeros(N)
    jmax = int(np.floor(K_C * L / (2 * np.pi)))
    for j in range(1, jmax + 1):
        k = 2 * np.pi * j / L
        w = omega(k)
        for sgn in (+1, -1):                # right- and left-movers
            kk = sgn * k
            n_k = temp / (gam * (w - v * kk))
            A = np.sqrt(2 * n_k / (w * L))
            th = rng.uniform(0, 2 * np.pi)
            f += A * np.cos(kk * x + th)
            fp += w * A * np.sin(kk * x + th)
    return f, fp


def lap(f, dx):
    return (np.roll(f, 1) + np.roll(f, -1) - 2 * f) / dx**2


def e_phi(phi, pphi, dx):
    g = (np.roll(phi, -1) - phi) / dx
    return np.sum(0.5 * pphi**2 + 0.5 * g**2
                  + 0.5 * MASS**2 * phi**2) * dx


def p_phi(phi, pphi, dx):
    g = (np.roll(phi, -1) - np.roll(phi, 1)) / (2 * dx)   # centered
    return -np.sum(pphi * g) * dx


# ---------------------------------------------------------- self-test
N0 = 64
dx0 = L / N0
x0 = np.arange(N0) * dx0
k0 = 2 * np.pi * 3 / L
w0 = omega(k0)
phi_t = np.cos(k0 * x0)
pi_t = w0 * np.sin(k0 * x0)
ratio = p_phi(phi_t, pi_t, dx0) / e_phi(phi_t, pi_t, dx0)
print(f"self-test: right-mover P/E = {ratio:+.4f} vs k/w = "
      f"{k0/w0:+.4f}  ({'OK' if abs(ratio - k0/w0) < 0.02 else 'FAIL'})")


def run_case(N, v, lam):
    """Secular estimator: linear-regression slopes of E_phi(t) and
    P_phi(t) over t in [5, TEND]; v* = dP/dt / dE/dt (oscillations
    average out in the fit). Stops early if the transfer exceeds
    50% of the initial normal-sector energy (back-reaction guard)."""
    dx = L / N
    out = []
    tgrid = np.linspace(0.0, TEND, 161)
    for _ in range(NENS):
        phi, pphi = boosted_bath(N, v, T_PHI)
        chi, pchi = boosted_bath(N, v, T_CHI)
        e0 = e_phi(phi, pphi, dx)

        def rhs(t, y):
            ph, pp, ch, pc = y.reshape(4, N)
            return np.concatenate([
                pp, lap(ph, dx) - MASS**2 * ph - 2 * lam * ch**2 * ph,
                pc, lap(ch, dx) - MASS**2 * ch + 2 * lam * ph**2 * ch])

        guard = lambda t, y: e_phi(y[:N], y[N:2 * N], dx) - 2.0 * e0
        guard.terminal, guard.direction = True, 1
        s = solve_ivp(rhs, (0, TEND),
                      np.concatenate([phi, pphi, chi, pchi]),
                      rtol=1e-8, atol=1e-8, events=guard,
                      t_eval=tgrid, max_step=0.05)
        ts = s.t
        if len(ts) < 20:                 # need >= t~10 of secular data
            continue
        Es = np.array([e_phi(s.y[:N, i], s.y[N:2 * N, i], dx)
                       for i in range(len(ts))])
        Ps = np.array([p_phi(s.y[:N, i], s.y[N:2 * N, i], dx)
                       for i in range(len(ts))])
        m = ts >= 3.0
        dEdt = np.polyfit(ts[m], Es[m], 1)[0]
        dPdt = np.polyfit(ts[m], Ps[m], 1)[0]
        out.append((dPdt / dEdt if dEdt != 0 else np.nan,
                    dEdt, ts[-1]))
    return out


print()
print("=" * 72)
print(f"M3: frame of secular energy transfer, v* = (dP/dt)/(dE/dt),")
print(f"    regression over t in [5,{TEND:.0f}]")
print(f"    state: boosted thermal, v={VSTATE}, T_phi={T_PHI}, "
      f"T_chi={T_CHI}, |k|<={K_C} (fixed); lam={LAM}")
print(f"    targets: state-anchored v* = {VSTATE:.2f}; "
      f"lattice-anchored v* = 0")
print("=" * 72)
print(f"{'N':>4} {'k_lat':>6} | {'median v*':>9} {'IQR':>17} "
      f"{'med dE/dt':>9} {'runs':>5}")
for N in (16, 32, 64, 128):
    res = run_case(N, VSTATE, LAM)
    if res:
        vs = np.array([r[0] for r in res])
        rr = np.array([r[1] for r in res])
        print(f"{N:>4} {np.pi/(L/N):>6.2f} | {np.median(vs):>9.3f} "
              f"[{np.percentile(vs,25):>6.3f},{np.percentile(vs,75):>7.3f}]"
              f" {np.median(rr):>9.4f} {len(res):>4}/{NENS}")
    else:
        print(f"{N:>4} {np.pi/(L/N):>6.2f} | insufficient data")

print()
print("controls:")
res0 = run_case(64, 0.0, LAM)
if res0:
    vs0 = np.array([r[0] for r in res0])
    print(f"  v=0, N=64:   median v* = {np.median(vs0):+.3f} "
          f"[{np.percentile(vs0,25):+.3f},{np.percentile(vs0,75):+.3f}] "
          f"(target 0)")
resL = run_case(64, VSTATE, 0.0)
if resL:
    rr = np.array([r[1] for r in resL])
    print(f"  lam=0, N=64: median dE/dt = {np.median(rr):+.5f} "
          f"(target ~0 - no transfer)")
print()
print("verdict key: v*(N) ~ 0.35 and stable as N grows => the STATE")
print("individuates the frame (foliation is physical/spontaneous);")
print("v*(N) -> 0 with N => the REGULATOR individuates (CJM picture).")
print("done.")
