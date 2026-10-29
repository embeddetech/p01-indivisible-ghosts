"""
Stage 3 sharpened into a theorem: the EXPLOSION DICTIONARY.
(Follow-up to interacting_pu.py / quartic_pu_leak.py.)

MECHANISM MODEL. The malicious interacting ghost escapes along a direction
with a super-quadratically falling effective potential; the structure is
captured by H = p^2/2 + V on the line with V(x) -> -infinity like -|x|^a.

THEOREM (explosion dictionary; rigorous inputs: Weyl's limit-point/limit-
circle alternative, Reed-Simon II Thms X.9/X.10, von Neumann extension
theory, Feller boundary classification). Define the classical time of
flight T(E) = int^inf dx / sqrt(2(E - V(x))).

 (1) T = infinity (V falls at most quadratically): limit point at the
     escaping end. H is essentially self-adjoint: a UNIQUE unitary U(t), a
     unique conservative Barandes process. The ghost can be at most
     transient (stages 1-2).
 (2) T < infinity (super-quadratic fall, the malicious case): limit
     circle. THE ONE-LINE IDENTITY: WKB gives |psi_pm|^2 ~ [2(E-V)]^{-1/2}
     for BOTH solutions of (H - z)psi = 0, so
         ||psi_pm||^2 (near the escaping end)  =  classical time of flight.
     The deficiency norm IS the escape time; H loses essential
     self-adjointness exactly when the classical particle reaches infinity
     in finite time. Consequences:
       (a) No canonical unitary dynamics: a U(1) family of self-adjoint
           extensions per escaping end (U(2) for two ends, including
           completions that TRANSMIT through infinity from +inf to -inf).
           The extension is boundary data AT INFINITY, not contained in H.
       (b) Every extension is conservative but reflects/returns probability
           from infinity after the FINITE classical round trip: discrete
           spectrum with local level spacing dE = pi / T_cross(E).
       (c) The regulator-independent (minimal, Feller) object is
           SUB-stochastic: an explosive process losing mass at the
           classical escape rate. Conservativity costs extra-theoretic
           boundary data; explosion is the canonical physics.
       (d) One integral decides all three theories: classical completeness
           (escape time), quantum self-adjointness (Weyl), stochastic
           conservativity (Feller exit boundary).

NUMERICAL VERIFICATION BELOW (V = -x^4 as the malicious representative,
V = -x^2 as the marginal limit-point control):
 V1  the time-of-flight integral: convergent for a > 2, divergent a <= 2.
 V2  level-spacing law dE = pi/T_cross(E, L): quantitative match for both
     potentials; T_cross saturates with box size L for -x^4 (spacing stays
     finite: reflection from infinity) and grows for -x^2 (spacing -> 0:
     continuum, no boundary needed).
 V3  extension = regulator data: individual eigenvalues near E = 10 sweep
     erratically as the wall moves (no L -> inf limit), while the SPACING
     is stable.
 V4  the minimal process converges: 1D absorbing-boundary evolution (the
     resolution barrier that defeated the 2D lattice is beatable in 1D):
     absorbed-mass onset saturates with L and tracks the classical arrival
     time -- direct verification of finite-time probability escape.
 V5  completions differ observably: Dirichlet wall (reflection) vs periodic
     (transmission through infinity): probability returns from OPPOSITE
     SIDES at the classically predicted revival time. Same H on C_0^inf,
     different physics: the completion is genuinely new data.

Run:  python -u explosion_theorem.py    (~3-5 minutes)
"""

import functools
import numpy as np
from scipy.integrate import quad
from scipy import sparse
from scipy.sparse.linalg import eigsh
import scipy.fft as sfft

print = functools.partial(print, flush=True)


# ----------------------------------------------------------------------
# classical time-of-flight helpers  (V = -x^4 unless stated)
# ----------------------------------------------------------------------
def tof_rest(x0, x1):
    """Time from rest at x0 to reach x1 (> x0) in V = -x^4."""
    E = -x0 ** 4
    f = lambda u: 2 * u / np.sqrt(2 * (E + (x0 + u * u) ** 4))
    val, _ = quad(f, 1e-9, np.sqrt(x1 - x0), limit=400)
    return val


def t_cross(E, L, Vf):
    """Classical traversal time -L -> +L at energy E (> max V)."""
    f = lambda x: 1.0 / np.sqrt(2 * (E - Vf(x)))
    val, _ = quad(f, 0, L, limit=400)
    return 2 * val


# ----------------------------------------------------------------------
# V1. The integral that decides everything
# ----------------------------------------------------------------------
print("=" * 72)
print("V1. Time of flight T = int dx/sqrt(2(1+x^a)) from x=1 to R")
print("=" * 72)
print(f"{'a':>5} {'R=1e2':>10} {'R=1e4':>10} {'R=1e6':>10}   verdict")
for a in (1.5, 2.0, 2.5, 3.0, 4.0):
    row = []
    for R in (1e2, 1e4, 1e6):
        val, _ = quad(lambda x: 1 / np.sqrt(2 * (1 + x ** a)), 1, R,
                      limit=800)
        row.append(val)
    verdict = ("divergent -> limit point, unique process" if a <= 2
               else "CONVERGENT -> limit circle, explosion")
    print(f"{a:>5.1f} {row[0]:>10.4f} {row[1]:>10.4f} {row[2]:>10.4f}   "
          + verdict)

# ----------------------------------------------------------------------
# V2 + V3. Spectra of the wall-regularized completions
# ----------------------------------------------------------------------
DX = 8e-4


def box_spectrum(Vf, L, sigma, k=90):
    N = int(round(2 * L / DX)) - 1
    x = -L + DX * np.arange(1, N + 1)
    A = sparse.diags([-0.5 / DX ** 2 * np.ones(N - 1),
                      1.0 / DX ** 2 + Vf(x),
                      -0.5 / DX ** 2 * np.ones(N - 1)],
                     [-1, 0, 1], format="csc")
    vals = eigsh(A, k=k, sigma=sigma, which="LM",
                 return_eigenvectors=False)
    return np.sort(vals)


print()
print("=" * 72)
print("V2. Level spacing near E=11 vs the classical law pi/T_cross(11, L)")
print("=" * 72)
for name, Vf in (("-x^4 (malicious)", lambda x: -x ** 4),
                 ("-x^2 (marginal control)", lambda x: -x ** 2)):
    print(f"V = {name}:")
    print(f"{'L':>6} {'measured dE':>12} {'pi/T_cross':>11} {'T_cross':>8}")
    for L in (6.0, 9.0, 12.0, 16.0):
        ev = box_spectrum(Vf, L, sigma=11.0)
        win = ev[(ev > 6) & (ev < 16)]
        dE = np.diff(win).mean()
        T = t_cross(11.0, L, Vf)
        print(f"{L:>6.1f} {dE:>12.4f} {np.pi / T:>11.4f} {T:>8.4f}")
print("=> -x^4: T_cross saturates (finite trip to infinity): spacing stays")
print("   FINITE -- every completion reflects off infinity at a finite")
print("   recurrence time. -x^2: T_cross grows: spacing -> 0 (continuum),")
print("   no boundary at infinity needed. Law pi/T_cross matches both.")

print()
print("=" * 72)
print("V3. The completion is regulator data: eigenvalue nearest E=10 vs L")
print("=" * 72)
near = []
for L in np.arange(10.0, 10.51, 0.05):
    ev = box_spectrum(lambda x: -x ** 4, L, sigma=10.0, k=1)
    near.append(ev[0])
print("L      :", " ".join(f"{L:6.2f}" for L in np.arange(10.0, 10.51, 0.05)))
print("E near :", " ".join(f"{e:6.2f}" for e in near))
print("=> the nearest level sweeps erratically with the wall position (the")
print("   phase to the wall changes by ~2 k(L) dL ~ 14 rad per 0.05): the")
print("   L -> infinity limit of any individual completion DOES NOT EXIST,")
print("   while the spacing (V2) is stable. Extension = data, not physics.")

# ----------------------------------------------------------------------
# V4. The minimal (absorbed) process converges: 1D beats the lattice bound
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("V4. Minimal process: absorbed mass onset vs box size (V = -x^4,")
print("    packet at rest at x0 = 2, sigma = 0.5, CAP beyond 0.7 L)")
print("=" * 72)


def cap_run(L, dx=1.2e-3, dt=5e-5, tmax=1.5, x0=2.0, sig=0.5):
    N = int(round(2 * L / dx))
    x = -L + dx * np.arange(N)
    k = 2 * np.pi * sfft.fftfreq(N, d=dx)
    edge = 0.7 * L
    W = 400.0 * np.clip((np.abs(x) - edge) / (L - edge), 0, None) ** 2
    half = np.exp((-1j * (-x ** 4) - W) * dt / 2)
    kin = np.exp(-1j * k ** 2 * dt / 2)
    psi = np.exp(-(x - x0) ** 2 / (2 * sig ** 2)).astype(complex)
    psi /= np.linalg.norm(psi)
    nst = int(round(tmax / dt))
    rec = max(1, nst // 300)
    ts, A = [0.0], [0.0]
    for s in range(1, nst + 1):
        psi = half * sfft.ifft(kin * sfft.fft(half * psi))
        if s % rec == 0:
            ts.append(s * dt)
            A.append(1.0 - float(np.sum(np.abs(psi) ** 2)))
    return np.array(ts), np.array(A)


print(f"{'L':>5} {'CAP edge':>9} {'t_cl(2->edge)':>14} "
      f"{'onset(A>1%)':>12} {'A(t=1.0)':>9}")
for L in (8.0, 12.0, 16.0):
    ts, A = cap_run(L)
    edge = 0.7 * L
    tcl = tof_rest(2.0, edge)
    i = np.argmax(A > 0.01)
    onset = ts[i] if A[i] > 0.01 else None
    print(f"{L:>5.1f} {edge:>9.1f} {tcl:>14.4f} "
          f"{(f'{onset:.3f}' if onset else '  >1.5'):>12} "
          f"{A[np.searchsorted(ts, 1.0)]:>9.4f}")
print(f"classical escape to infinity from rest at 2: "
      f"T_esc = {tof_rest(2.0, 1e6):.4f}")
print("=> onset SATURATES with L and tracks the classical arrival time --")
print("   the direct verification (impossible on the 2D lattice) that")
print("   probability reaches infinity at finite time: the minimal process")
print("   is explosive, and it is the L-independent object.")

# ----------------------------------------------------------------------
# V5. Two completions, observably different: reflection vs wormhole
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("V5. Conservative completions at L=12: Dirichlet (reflection) vs")
print("    periodic (transmission through infinity). Same H on C_0^inf.")
print("=" * 72)


def wall_run(kind, L=12.0, dx=1.2e-3, dt=5e-5, tmax=2.0, x0=2.0, sig=0.5):
    if kind == "dirichlet":
        N = int(round(2 * L / dx)) - 1
        x = -L + dx * np.arange(1, N + 1)
        kn = np.pi * np.arange(1, N + 1) / (2 * L)
        kin = np.exp(-1j * kn ** 2 * dt / 2)
        fwd = lambda p: sfft.dst(p, type=1, norm="ortho")
        bwd = lambda p: sfft.idst(p, type=1, norm="ortho")
    else:
        N = int(round(2 * L / dx))
        x = -L + dx * np.arange(N)
        k = 2 * np.pi * sfft.fftfreq(N, d=dx)
        kin = np.exp(-1j * k ** 2 * dt / 2)
        fwd, bwd = sfft.fft, sfft.ifft
    half = np.exp(-1j * (-x ** 4) * dt / 2)
    psi = np.exp(-(x - x0) ** 2 / (2 * sig ** 2)).astype(complex)
    psi /= np.linalg.norm(psi)
    nst = int(round(tmax / dt))
    rec = max(1, nst // 200)
    ts, PL, PC, PR = [0.0], [0.0], [1.0], [0.0]
    mL, mC, mR = x < -5, np.abs(x) <= 5, x > 5
    for s in range(1, nst + 1):
        psi = half * bwd(kin * fwd(half * psi))
        if s % rec == 0:
            w = np.abs(psi) ** 2
            ts.append(s * dt)
            PL.append(float(w[mL].sum()))
            PC.append(float(w[mC].sum()))
            PR.append(float(w[mR].sum()))
    return (np.array(ts), np.array(PL), np.array(PC), np.array(PR))


t_out = tof_rest(2.0, 12.0)
print(f"classical: leave |x|<5 heading right, reach the wall at "
      f"t = {t_out:.3f}, revisit |x|<5 around t = "
      f"{t_out + (t_out - tof_rest(2.0, 5.0)):.3f}")
for kind in ("dirichlet", "periodic"):
    ts, PL, PC, PR = wall_run(kind)
    imin = np.argmin(PC[: len(PC) * 2 // 3])
    irev = imin + np.argmax(PC[imin:])
    print(f"  {kind:>10}: P_center min {PC[imin]:.3f} at t={ts[imin]:.3f}; "
          f"revival peak {PC[irev]:.3f} at t={ts[irev]:.3f}; "
          f"at revival P(x<-5) = {PL[irev]:.3f}, P(x>+5) = {PR[irev]:.3f}")
print("=> both completions conserve probability and revive it after the")
print("   finite round trip 'through infinity' -- but from OPPOSITE sides:")
print("   Dirichlet reflects (returns on the right), periodic transmits")
print("   (+inf -> -inf wormhole: returns on the left). Which one nature")
print("   picks is not in H: it is boundary data at infinity. The only")
print("   completion-independent object is the explosive minimal process.")
