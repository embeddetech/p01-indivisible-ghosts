"""
Follow-up to handoff section 5.4 (= paper Secs. 7-8): THE INTERACTING GHOST.
Does the Ostrogradski instability, once interactions are switched on, show
up as a STOCHASTIC pathology (loss of a valid indivisible process), or
still only as energetics?

Three layers, in increasing severity:

A. QUADRATIC INTERACTION (exact benchmark). H = w1 a^dag a - w2 b^dag b
   + g(a^dag b^dag + a b): Hermitian, so Gamma = |U|^2 stays exactly doubly
   stochastic FOREVER. But the mode-matrix eigenvalues are
   (w1+w2)/2 +- sqrt((w1-w2)^2/4 - g^2), so the ghost sign collapses the
   instability threshold from g > (w1+w2)/2 (normal twin: sum frequency,
   huge) to g > |w1-w2|/2 (difference frequency: ZERO at resonance). At
   resonance the vacuum cascades: <n1> = <n2> = sinh^2(gt), with the
   two-mode-squeezed occupation law P(n1 <= K) = 1 - tanh^{2K+2}(gt) -> 0.
   Stochastic reading: the process is VALID but TRANSIENT -- it escapes
   every finite region of configuration space at rate ~2g, while the energy
   books stay exactly balanced (E_normal grows, E_ghost = -w2<n2>
   compensates; <H> = 0 always). "Vacuum decay" is a configuration-space
   cascade, invisible in the total energy and harmless to stochasticity.

B. NONLINEAR INTERACTIONS, CLASSICAL. Quartic PU
   (x'''' + (w1^2+w2^2) x'' + w1^2 w2^2 x = (4 lam/gamma) x^3) admits
   finite-time blowup solutions (dominant balance x ~ A (t*-t)^{-2},
   A^2 = 30 gamma / lam, needs lam > 0), and the ghost-pair normal form
   H = (p1^2 + w1^2 x1^2)/2 - (p2^2 + w2^2 x2^2)/2 + lam x1^2 x2^2 opens an
   energy-transfer channel with no bottom. Numerical survey: which
   couplings / amplitudes actually escape, and is the escape finite-time?

C. NONLINEAR, QUANTUM. Split-step evolution of the ghost pair with an
   absorbing layer (CAP): survival S(t) vs box size. If the absorbed
   fraction persists (onset time saturating) as the box grows, probability
   genuinely reaches infinity: in the infinite-volume limit the CLOSED
   process on real configurations fails and only a SUB-stochastic (leaky,
   section-5.2-style) process exists -- the ghost instability finally
   becomes a probability pathology, exactly where the classical flow is
   incomplete.

Run:  python interacting_pu.py     (~4-6 minutes)
"""

import functools
import numpy as np
from scipy.linalg import eigh
from scipy.integrate import solve_ivp

np.set_printoptions(precision=4, suppress=True)
print = functools.partial(print, flush=True)

# ----------------------------------------------------------------------
# A. Quadratic cascade: exact thresholds, sinh^2 law, valid-but-transient
# ----------------------------------------------------------------------
print("=" * 72)
print("A. Quadratic ghost cascade (Hermitian, exactly benchmarked)")
print("=" * 72)
NF = 34


def two_mode(w1, w2, g, ghost):
    a = np.diag(np.sqrt(np.arange(1, NF)), 1)
    n = np.diag(np.arange(NF)).astype(float)
    I = np.eye(NF)
    A, B = np.kron(a, I), np.kron(I, a)
    sgn = -1.0 if ghost else 1.0
    H = (w1 * np.kron(n, I) + sgn * w2 * np.kron(I, n)
         + g * (A.T @ B.T + A @ B))
    return H, np.kron(n, I), np.kron(I, n)


def evolve_vacuum(H, N1, N2, ts, EV=None):
    E, V = eigh(H) if EV is None else EV
    psi0 = np.zeros(H.shape[0])
    psi0[0] = 1.0
    c0 = V.T @ psi0
    out = []
    for t in ts:
        psi = V @ (np.exp(-1j * E * t) * c0)
        w = np.abs(psi) ** 2
        n1 = np.arange(NF).repeat(NF)
        out.append((float(w @ N1.diagonal()), float(w @ N2.diagonal()),
                    float(w[n1 <= 10].sum()), psi))
    return E, V, out


g = 0.15
ts = np.array([0.0, 3.0, 6.0, 9.0, 12.0])
Hg, N1, N2 = two_mode(1.0, 1.0, g, ghost=True)
Hn, _, _ = two_mode(1.0, 1.0, g, ghost=False)
print(f"resonant, g = {g}: ghost threshold |w1-w2|/2 = 0  =>  unstable;")
print("                   normal threshold (w1+w2)/2 = 1  =>  stable")
Eg, Vg, outg = evolve_vacuum(Hg, N1, N2, ts)
_, _, outn = evolve_vacuum(Hn, N1, N2, ts)
print(f"{'t':>5} {'<n1> ghost':>11} {'sinh^2(gt)':>11} {'<n1> normal':>12} "
      f"{'P(n<=10)':>9} {'1-tanh^22':>10}")
for t, og, on in zip(ts, outg, outn):
    print(f"{t:>5.1f} {og[0]:>11.4f} {np.sinh(g * t) ** 2:>11.4f} "
          f"{on[0]:>12.6f} {og[2]:>9.4f} "
          f"{1 - np.tanh(g * t) ** 22:>10.4f}")
psi12 = outg[-1][3]
w = np.abs(psi12) ** 2
E1 = 1.0 * (w @ N1.diagonal())
E2 = -1.0 * (w @ N2.diagonal())
Etot = float(np.real(psi12.conj() @ (Hg @ psi12)))
print(f"energy books at t=12: E_normal = {E1:+.3f}, E_ghost = {E2:+.3f}, "
      f"<H> = {Etot:+.2e} (conserved 0)")
# the process is still exactly doubly stochastic
U = (Vg * np.exp(-1j * Eg * 1.3)) @ Vg.conj().T
G = np.abs(U) ** 2
print(f"Gamma(1.3) doubly-stochastic error: "
      f"{max(abs(G.sum(0) - 1).max(), abs(G.sum(1) - 1).max()):.2e} "
      f"on {G.shape[0]} Fock configs")
# detuning threshold check: growth rate sqrt(g^2 - delta^2/4)
print("detuning check (ghost, g=0.15):")
for delta, lab in ((0.40, "delta=0.40 > 2g: stable"),
                   (0.20, "delta=0.20 < 2g: unstable")):
    Hd, _, _ = two_mode(1.0 + delta / 2, 1.0 - delta / 2, g, ghost=True)
    tt = np.array([6.0, 9.0, 12.0, 15.0])
    _, _, od = evolve_vacuum(Hd, N1, N2, tt)
    ns = np.array([o[0] for o in od])
    rate = np.polyfit(tt, np.log(ns), 1)[0] / 2
    kappa = np.sqrt(max(g ** 2 - delta ** 2 / 4, 0))
    print(f"  {lab}:  <n1>(t=6..15) = {np.round(ns, 3)}"
          f"  | fitted rate {rate:.4f} vs sqrt(g^2-d^2/4) = {kappa:.4f}")
print("=> A valid, doubly stochastic, indivisible process at ALL times;")
print("   the ghost instability appears as TRANSIENCE (escape through")
print("   configuration space at rate 2g), with balanced energy books.")

# ----------------------------------------------------------------------
# B. Nonlinear classical escape survey
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("B. Classical escape survey (event: |state| > 1e6, window t <= 150)")
print("=" * 72)


def escape_time(rhs, z0, tmax=150.0):
    ev = lambda t, z: np.max(np.abs(z)) - 1e6
    ev.terminal, ev.direction = True, 1
    sol = solve_ivp(rhs, (0, tmax), z0, method="RK45", rtol=1e-8,
                    atol=1e-8, events=ev, dense_output=False)
    return sol.t_events[0][0] if len(sol.t_events[0]) else None


def pair_rhs(lam, w1=1.0, w2=0.5):
    def f(t, z):
        x1, v1, x2, v2 = z
        return [v1, -w1 ** 2 * x1 - 2 * lam * x1 * x2 ** 2,
                v2, -w2 ** 2 * x2 + 2 * lam * x1 ** 2 * x2]
    return f


def pu_rhs(lam, gam=1.0, w1=1.0, w2=0.5):
    Om, w4, c = w1 ** 2 + w2 ** 2, (w1 * w2) ** 2, 4 * lam / gam
    def f(t, z):
        x, d1, d2, d3 = z
        return [d1, d2, d3, -Om * d2 - w4 * x + c * x ** 3]
    return f


print("ghost pair  H = (p1^2+x1^2)/2 - (p2^2+0.25 x2^2)/2 + lam x1^2 x2^2,")
print("IC (x1, 0, x2=0.3, 0):")
for lam in (0.05, -0.05, 0.0):
    row = []
    for x10 in (1.5, 2.5, 3.5):
        te = escape_time(pair_rhs(lam), [x10, 0, 0.3, 0])
        row.append(f"x1={x10}: " + (f"t*={te:7.2f}" if te else "bounded"))
    print(f"  lam={lam:+.2f}:  " + " | ".join(row))
print("quartic PU  x'''' + 1.25 x'' + 0.25 x = 4 lam x^3, IC (x0,0,0,0):")
for lam in (0.05, -0.05):
    row = []
    for x0 in (2.0, 3.0, 4.0):
        te = escape_time(pu_rhs(lam), [x0, 0, 0, 0])
        row.append(f"x0={x0}: " + (f"t*={te:7.2f}" if te else "bounded"))
    print(f"  lam={lam:+.2f}:  " + " | ".join(row))

# ----------------------------------------------------------------------
# C. Quantum leak: split-step + absorbing layer, box-size comparison
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("C. Quantum ghost pair with absorber: survival vs box size")
print("=" * 72)


def survival_run(lam, L, n, tmax=20.0, dt=1e-3, x0=(2.5, 0.3), sig=0.7,
                 w1=1.0, w2=0.5):
    dx = 2 * L / n
    x = -L + dx * np.arange(n)
    k = 2 * np.pi * np.fft.fftfreq(n, d=dx)
    X1, X2 = np.meshgrid(x, x, indexing="ij")
    K1, K2 = np.meshgrid(k, k, indexing="ij")
    T = 0.5 * (K1 ** 2 - K2 ** 2)                       # ghost kinetic
    Vpot = (0.5 * w1 ** 2 * X1 ** 2 - 0.5 * w2 ** 2 * X2 ** 2
            + lam * X1 ** 2 * X2 ** 2)
    edge = 0.75 * L
    W = 5.0 * (np.clip((np.abs(X1) - edge) / (L - edge), 0, None) ** 3
               + np.clip((np.abs(X2) - edge) / (L - edge), 0, None) ** 3)
    half = np.exp((-1j * Vpot - W) * dt / 2)
    kin = np.exp(-1j * T * dt)
    psi = np.exp(-((X1 - x0[0]) ** 2 + (X2 - x0[1]) ** 2) / (2 * sig ** 2))
    psi = psi.astype(complex) / np.linalg.norm(psi)
    nsteps = int(round(tmax / dt))
    rec_every = max(1, nsteps // 50)
    ts_out, S_out = [0.0], [1.0]
    for step in range(1, nsteps + 1):
        psi = half * np.fft.ifft2(kin * np.fft.fft2(half * psi))
        if step % rec_every == 0:
            ts_out.append(step * dt)
            S_out.append(float(np.sum(np.abs(psi) ** 2)))
    return np.array(ts_out), np.array(S_out)


runs = [("lam=+0.05 (cl. bounded here; leaky), L=12", 0.05, 12.0, 96),
        ("lam=+0.05 (cl. bounded here; leaky), L=18", 0.05, 18.0, 144),
        ("free      lam= 0.00,               L=12", 0.00, 12.0, 96),
        ("lam=-0.05 (cl. escaping, sect. B),  L=12", -0.05, 12.0, 96)]
curves = {}
for label, lam, L, n in runs:
    t_, S_ = survival_run(lam, L, n)
    curves[label] = (t_, S_)
    idx = np.searchsorted(-S_, -0.99)
    onset = t_[idx] if idx < len(t_) else None
    print(f"  {label}:  S(10) = {S_[np.searchsorted(t_, 10.0)]:.4f}  "
          f"S(20) = {S_[-1]:.4f}  onset(S<0.99) = "
          + (f"{onset:.2f}" if onset else ">20"))
print()
print("Interpretation: compare the two lam=+0.05 rows. If the leak onset")
print("time saturates (stays ~equal) as the box grows L=12 -> 18, the")
print("escaping flux reaches ANY radius at essentially the same time --")
print("the infinite-volume closed process fails; probability genuinely")
print("leaves the configuration space and only a SUB-stochastic (dilated)")
print("process remains. If instead the onset drifts out with L, escape is")
print("asymptotic (transience only, as in section A).")
