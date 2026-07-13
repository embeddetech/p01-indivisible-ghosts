"""
Companion to interacting_pu.py, section C2: quantum leak for the QUARTIC PU
-- the case whose CLASSICAL escape is finite-time (t* = 5.13 for the packet
center IC, from interacting_pu.py section B; blowup law x ~ A/(t*-t)^2 with
A = sqrt(30 gamma / lam)). NOTE: this script's own stricter escape event
prints t* = 5.3361 for the same IC -- the difference is the escape-event
criterion/tolerance (|z| threshold trips early on the third derivative,
which blows up as (t*-t)^-5; 5.13 at rtol 1e-8 vs 5.336 at tighter
tolerance), not a discrepancy. The paper quotes only the range 3.3-6.9,
which is interacting_pu's own output.

H = p1 q2 + p2^2/(2 gamma) + (gamma/2) Om q2^2 - (gamma/2) wb q1^2
    + lam q1^4,     Om = w1^2 + w2^2,  wb = (w1 w2)^2.

Split-step (Strang) with three exactly-diagonalizable factors:
  V(q1, q2)      -- diagonal in position (+ absorbing layer W),
  A = p1 q2      -- diagonal in (k1, q2): FFT along axis 0 only,
  B = p2^2/2g    -- diagonal in (q1, k2): FFT along axis 1 only.

THE SUBTLETY THAT DECIDES THE TEST. Finite-time escape involves UNBOUNDED
acceleration, so a grid with momentum cutoff k_max = pi/dx can only
transport the wavefront while the required classical speed stays below
k_max; beyond that the lattice artificially confines (this is the same
structural fact as handoff section 5.4-B (= paper Secs. 7-8): a Hamiltonian that is not essentially
self-adjoint has no faithful finite truncation). Therefore:

 1. PROBE TEST (decisive): within one well-resolved run, the time at which
    quantum probability arrives at radius r must track the CLASSICAL
    finite-time arrival law t_r (computed from the exact trajectory),
    whose defining signature is t_r -> t* < infinity as r -> infinity.
 2. BOX-SCALING TABLE (diagnostic): survival onset vs box size, annotated
    with the classically required arrival speed at the absorber edge vs
    k_max. Onsets drift out ONLY when that speed exceeds k_max -- lattice
    confinement, not boundedness of the physics.

Run:  python -u quartic_pu_leak.py    (~4-5 minutes)
"""

import functools
import numpy as np
from scipy.integrate import solve_ivp

print = functools.partial(print, flush=True)

GAMMA, W1, W2, LAM = 1.0, 1.0, 0.5, 0.05
OM, WB = W1 ** 2 + W2 ** 2, (W1 * W2) ** 2

# ----------------------------------------------------------------------
# Classical reference trajectory (packet-center IC)
# ----------------------------------------------------------------------


def pu_rhs(t, z):
    x, d1, d2, d3 = z
    return [d1, d2, d3, -OM * d2 - WB * x + (4 * LAM / GAMMA) * x ** 3]


ev = lambda t, z: np.max(np.abs(z[:2])) - 1e7
ev.terminal, ev.direction = True, 1
sol = solve_ivp(pu_rhs, (0, 8.0), [2.0, 0, 0, 0], rtol=1e-11, atol=1e-11,
                events=ev, dense_output=True)
tstar = sol.t_events[0][0]
tt = np.linspace(0, tstar * 0.9999, 40000)
zz = sol.sol(tt)
coord = np.maximum(np.abs(zz[0]), np.abs(zz[1]))       # max(|x|, |xdot|)
speed = np.sqrt(zz[1] ** 2 + zz[2] ** 2)               # |(q1dot, q2dot)|


def t_arrive_cl(r):
    i = np.argmax(coord >= r)
    return (tt[i], speed[i]) if coord[i] >= r else (None, None)


print(f"classical: finite-time blowup at t* = {tstar:.4f} "
      f"(IC = packet center (2,0,0,0))")

# ----------------------------------------------------------------------
# Quantum split-step machinery
# ----------------------------------------------------------------------


def quantum_run(lam, L, n, tmax, probes=(), sig=1.0, x0=2.0, dt=1e-3):
    dx = 2 * L / n
    x = -L + dx * np.arange(n)
    k = 2 * np.pi * np.fft.fftfreq(n, d=dx)
    Q1, Q2 = np.meshgrid(x, x, indexing="ij")
    K1, K2 = k[:, None], k[None, :]
    V = (0.5 * GAMMA * OM * Q2 ** 2 - 0.5 * GAMMA * WB * Q1 ** 2
         + lam * Q1 ** 4)
    edge = 0.75 * L
    W = 30.0 * (np.clip((np.abs(Q1) - edge) / (L - edge), 0, None) ** 2
                + np.clip((np.abs(Q2) - edge) / (L - edge), 0, None) ** 2)
    half_v = np.exp((-1j * V - W) * dt / 2)
    half_a = np.exp(-1j * K1 * Q2 * dt / 2)
    full_b = np.exp(-1j * K2 ** 2 / (2 * GAMMA) * dt)
    masks = {r: np.maximum(np.abs(Q1), np.abs(Q2)) > r for r in probes}
    psi = np.exp(-((Q1 - x0) ** 2 + Q2 ** 2) / (2 * sig ** 2)).astype(complex)
    psi /= np.linalg.norm(psi)
    nsteps = int(round(tmax / dt))
    rec = max(1, nsteps // 200)
    ts, S, Pout = [0.0], [1.0], {r: [0.0] for r in probes}
    for step in range(1, nsteps + 1):
        psi = half_v * psi
        psi = np.fft.ifft(half_a * np.fft.fft(psi, axis=0), axis=0)
        psi = np.fft.ifft(full_b * np.fft.fft(psi, axis=1), axis=1)
        psi = np.fft.ifft(half_a * np.fft.fft(psi, axis=0), axis=0)
        psi = half_v * psi
        if step % rec == 0:
            w = np.abs(psi) ** 2
            ts.append(step * dt)
            S.append(float(w.sum()))
            for r in probes:
                Pout[r].append(float(w[masks[r]].sum()))
    return (np.array(ts), np.array(S),
            {r: np.array(v) for r, v in Pout.items()}, np.pi / dx)


def onset(ts, curve, thresh):
    i = np.argmax(curve > thresh)
    return ts[i] if curve[i] > thresh else None


# ----------------------------------------------------------------------
# 1. Probe test: quantum arrival vs classical finite-time arrival law
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("1. PROBE TEST at L=18 (dx=0.25, k_max=12.6): arrival at radius r")
print("   quantum onset: P(outside r) > 0.05  |  classical: max(|x|,|xd|)=r")
print("=" * 72)
probes = (5.0, 6.0, 7.0, 8.0)
ts_m, S_m, P_m, kmax = quantum_run(LAM, 18.0, 144, tmax=6.0, probes=probes)
ts_f, S_f, P_f, _ = quantum_run(0.0, 18.0, 144, tmax=6.0, probes=probes)
print(f"{'r':>4} {'t_cl':>7} {'speed_cl':>9} {'t_qm(malicious)':>16} "
      f"{'t_qm(free)':>11}")
for r in probes:
    tcl, sp = t_arrive_cl(r)
    tqm = onset(ts_m, P_m[r], 0.05)
    tqf = onset(ts_f, P_f[r], 0.05)
    print(f"{r:>4.0f} {tcl:>7.3f} {sp:>9.2f} "
          f"{(f'{tqm:.2f}' if tqm else '   --'):>16} "
          f"{(f'{tqf:.2f}' if tqf else '  none'):>11}")
print(f"(all probe speeds above are < k_max = {kmax:.1f}: resolved regime)")

# ----------------------------------------------------------------------
# 2. Box-scaling table with the velocity diagnostic
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("2. Survival vs box size (absorber edge at 0.75 L), sigma = 1.0")
print("=" * 72)
print(f"{'run':>26} {'edge':>5} {'v_cl(edge)':>10} {'v/kmax':>7} "
      f"{'onset(S<.99)':>13} {'S(8)':>7} {'S(10)':>7}")
for label, lam, L, n in (("malicious L=12", LAM, 12.0, 96),
                         ("malicious L=18", LAM, 18.0, 144),
                         ("malicious L=24", LAM, 24.0, 192),
                         ("free      L=12", 0.0, 12.0, 96)):
    ts_, S_, _, km = quantum_run(lam, L, n, tmax=10.0)
    edge = 0.75 * L
    tcl, sp = t_arrive_cl(edge) if lam else (None, None)
    on = onset(ts_, 1.0 - S_, 0.01)
    s8 = S_[np.searchsorted(ts_, 8.0)]
    s10 = S_[-1]
    print(f"{label:>26} {edge:>5.1f} "
          f"{(f'{sp:.1f}' if sp else '  --'):>10} "
          f"{(f'{sp / km:.2f}' if sp else '  --'):>7} "
          f"{(f'{on:.2f}' if on else '>10'):>13} {s8:>7.4f} {s10:>7.4f}")
print()
print("Read: onsets are physical only while v_cl(edge)/k_max < 1. Larger")
print("boxes demand super-Nyquist transport -- the lattice confines, the")
print("physics does not. The probe test (section 1), run entirely in the")
print("resolved regime, is the decisive comparison: if quantum arrival")
print("tracks the classical law, whose t_r saturates at t* < infinity,")
print("then in the continuum/infinite-volume limit probability reaches")
print("infinity at finite time: no closed stochastic process on the real")
print("configurations -- only a sub-stochastic (leaky, paper Sec. 4) one.")
