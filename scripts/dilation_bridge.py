"""
Section 5.2 of PT_stochastic_handoff.md (= paper Sec. 4):
Broken-PT dynamics as an OPEN SUBSYSTEM via unitary (Halmos) dilation.

IDEA. The canonical 2x2 PT Hamiltonian is a balanced gain/loss dimer:
    H = cos(th) I + [ i sin(th)   s        ]
                    [ s          -i sin(th)]
Subtracting the uniform gain, H_loss = H - i sin(th) I, gives a PURE-LOSS
Hamiltonian (site 2 decays at rate 2 sin(th)), and identically
    exp(-iHt) = exp(+sin(th) t) * exp(-i H_loss t).
So broken-PT evolution differs from a CONTRACTION C(t) = exp(-i H_loss t) by
an overall scalar: the notorious runaway is pure normalization, and the
conditional (normalized) dynamics of H and H_loss coincide. Broken PT is
POST-SELECTED dynamics.

DILATION. For each t, the Halmos unitary dilation
    U_big(t) = [ C(t)              sqrt(I - C C^dag) ]
               [ sqrt(I - C^dag C)   -C(t)^dag       ]
is a genuine 4x4 unitary with Gamma_big(0) = I. Barandes' framework needs
only per-time unistochasticity (the family need not be a group --
indivisibility is precisely its failure to compose), so
    Gamma_big(t) = |U_big(t)|^2
is an ORDINARY Barandes indivisible process on the enlarged config space
{1, 2, a1, a2}: two system sites + two ancilla ("leaked") configurations.

REDUCED PROCESS. Gamma_red(t) = |C(t)_ij|^2 = top-left 2x2 block of
Gamma_big(t): a SUB-stochastic process; column-sum deficits = leak
probability.

TESTS.
 (1) Validity: entries >= 0, column sums <= 1.
 (2) Barandes divisibility, finite-gap: with Gamma(t1) invertible the ONLY
     candidate divisor is M = Gamma(t2) Gamma(t1)^{-1} (column sums are
     automatic), so divisible on (t1,t2) iff M has no negative entries (and
     column sums <= 1 in the sub-stochastic case). Condition-number guarded.
 (3) Barandes divisibility, infinitesimal: classical P-divisibility <=>
     the generator L(t) = dGamma/dt * Gamma^{-1} has nonnegative
     off-diagonals. Exact derivative: dC/dt = -i H_loss C, so
     dGamma_ij/dt = 2 Re( conj(C_ij) (dC/dt)_ij ). Negative off-diagonal of
     L at time t = the process is indivisible across t. We track WHERE the
     negativity lives in time (recurrent windows vs terminal).
 (4) Open-system non-Markovianity (classical BLP analog): total-variation
     distance between the two basis-state initializations, on the extended
     3-outcome space {1, 2, leaked} (linear) and for the conditional
     (survival-post-selected, normalized) process. Backflow reported in two
     windows [0,20] and [20,40] to distinguish a finite early-time amount
     from per-oscillation accrual. NOTE: near the EP the oscillation period
     pi/sqrt(s^2-sin^2 th) diverges, so any finite window smooths the
     transition -- the dichotomy is exact only as T -> infinity.

Run:  python dilation_bridge.py
"""

import numpy as np
from scipy.linalg import expm, eig

np.set_printoptions(precision=4, suppress=True)

TH = np.pi / 4
SIN, COS = np.sin(TH), np.cos(TH)
I2 = np.eye(2, dtype=complex)
DT = 0.05
T_MAX = 40.0
T_GEN = 12.0          # generator diagnostics window
COND_MAX = 1e8


def build_H(s, th=TH):
    return np.array([[np.exp(1j * th), s], [s, np.exp(-1j * th)]],
                    dtype=complex)


def H_loss_of(s):
    return build_H(s) - 1j * SIN * I2


def psd_sqrt(A):
    w, v = np.linalg.eigh(0.5 * (A + A.conj().T))
    return (v * np.sqrt(np.clip(w, 0, None))) @ v.conj().T


def dilate(Ct):
    """Halmos unitary dilation of a contraction (4x4, top-left block = C)."""
    Dc = psd_sqrt(I2 - Ct.conj().T @ Ct)
    Dcd = psd_sqrt(I2 - Ct @ Ct.conj().T)
    return np.block([[Ct, Dcd], [Dc, -Ct.conj().T]])


def family(s, tmax=T_MAX, dt=DT):
    ts = np.arange(0.0, tmax + 1e-9, dt)
    Hl = H_loss_of(s)
    Cs = [expm(-1j * Hl * t) for t in ts]
    return ts, Hl, Cs


def generator_trace(ts, Hl, Cs):
    """min off-diagonal of L(t) = Gdot Gamma^{-1} (exact derivative),
    None where Gamma too ill-conditioned."""
    out = []
    for t, C in zip(ts, Cs):
        if t == 0.0 or t > T_GEN:
            out.append(None)
            continue
        G = np.abs(C) ** 2
        if np.linalg.cond(G) > COND_MAX:
            out.append(None)
            continue
        Cdot = -1j * Hl @ C
        Gdot = 2 * np.real(np.conj(C) * Cdot)
        L = Gdot @ np.linalg.inv(G)
        out.append(L[~np.eye(2, dtype=bool)].min())
    return out


def gen_metrics(ts, trace):
    """(t* = first indivisible time, fraction of [6,12] indivisible,
    value at the latest admissible t)."""
    tol = 1e-7
    tstar = next((t for t, v in zip(ts, trace)
                  if v is not None and v < -tol), None)
    late = [(t, v) for t, v in zip(ts, trace)
            if v is not None and 6.0 <= t <= T_GEN]
    frac = (sum(v < -tol for _, v in late) / len(late)) if late else np.nan
    last = late[-1][1] if late else np.nan
    return tstar, frac, last


def finite_gap_violation(Gs, ts, sub, step=10):
    """Worst violation of the unique-divisor test over well-conditioned
    pairs (t1, t2 = t1 + step*DT)."""
    worst, at = 0.0, None
    for i in range(0, len(ts) - step):
        if ts[i + step] > T_GEN:
            break
        G1, G2 = Gs[i], Gs[i + step]
        if np.linalg.cond(G1) > 1e6:
            continue
        M = G2 @ np.linalg.inv(G1)
        v = max(0.0, -M.min())
        if sub:
            v = max(v, max(0.0, M.sum(axis=0).max() - 1.0))
        if v > worst:
            worst, at = v, (round(ts[i], 2), round(ts[i + step], 2))
    return worst, at


def backflows(ts, Cs):
    """(extended-space total, conditional in [0,20], conditional in
    [20,40]) TV-backflow between the two basis-state initializations."""
    D_ext, D_cond = [], []
    for C in Cs:
        G = np.abs(C) ** 2
        a = np.append(G[:, 0], 1 - G[:, 0].sum())
        b = np.append(G[:, 1], 1 - G[:, 1].sum())
        D_ext.append(0.5 * np.abs(a - b).sum())
        pc = [G[:, j] / G[:, j].sum() for j in (0, 1)]
        D_cond.append(0.5 * np.abs(pc[0] - pc[1]).sum())
    def bf(D, lo, hi):
        return sum(max(0.0, D[k + 1] - D[k]) for k in range(len(ts) - 1)
                   if lo <= ts[k] < hi)
    return bf(D_ext, 0, T_MAX), bf(D_cond, 0, 20), bf(D_cond, 20, T_MAX)


# ----------------------------------------------------------------------
# A. Identities in the broken phase (s = 0.5, baseline from handoff)
# ----------------------------------------------------------------------
print("=" * 72)
print("A. Broken phase s=0.5: gain/loss decomposition and conditioning")
print("=" * 72)
s = 0.5
H = build_H(s)
print("spectrum of H:", np.round(np.sort_complex(eig(H, right=False)), 4),
      " (broken: complex pair)")
ok_id = all(np.allclose(expm(-1j * H * t),
                        np.exp(SIN * t) * expm(-1j * H_loss_of(s) * t))
            for t in (0.7, 2.0, 5.0))
print("exp(-iHt) = e^{sin(th) t} C(t) identity holds:", ok_id)
sv = [np.linalg.svd(expm(-1j * H_loss_of(s) * t), compute_uv=False).max()
      for t in (0.5, 1, 2, 4, 8)]
print("max singular value of C(t) at t=0.5,1,2,4,8:", np.round(sv, 4),
      " (<= 1: contraction)")
print("=> the broken-phase 'runaway' is a scalar normalization;")
print("   broken-PT evolution = survival-conditioned dynamics.")

# ----------------------------------------------------------------------
# B. Dilation validity
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("B. Halmos dilation: Gamma_big(t) = |U_big(t)|^2 on {1, 2, a1, a2}")
print("=" * 72)
ts, Hl, Cs = family(s)
unit_err = max(np.linalg.norm(dilate(C) @ dilate(C).conj().T - np.eye(4))
               for C in Cs[::40])
Gbig = [np.abs(dilate(C)) ** 2 for C in Cs]
ds_err = max(max(abs(G.sum(0) - 1).max(), abs(G.sum(1) - 1).max())
             for G in Gbig[::40])
print(f"max unitarity error of U_big: {unit_err:.2e} | "
      f"max double-stochasticity error of Gamma_big: {ds_err:.2e}")
print("Gamma_big(0) = I:", np.allclose(Gbig[0], np.eye(4)))
vb, atb = finite_gap_violation(Gbig, ts, sub=False)
print(f"Gamma_big indivisible (unique-divisor test): violation "
      f"{vb:.4f} at {atb}  (> 0 => ordinary Barandes indivisible process)")

# ----------------------------------------------------------------------
# C. The reduced process on the original two configurations
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("C. Reduced process Gamma_red(t) = |C(t)|^2 (sub-stochastic)")
print("=" * 72)
Gred = [np.abs(C) ** 2 for C in Cs]
valid = all(np.all(G >= -1e-12) and np.all(G.sum(0) <= 1 + 1e-9)
            for G in Gred)
print("entries >= 0 and column sums <= 1 for all t:", valid)
for t in (0.5, 1.3, 3.0, 6.0):
    G = Gred[int(round(t / DT))]
    print(f"  t={t}: survival (col sums) = {np.round(G.sum(0), 4)}")
print("=> a WELL-DEFINED sub-stochastic process exists in the broken phase,")
print("   where the closed-system construction failed totally.")

# ----------------------------------------------------------------------
# D. WHERE the indivisibility lives: generator sign traces, both phases
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("D. Generator L(t) = Gdot Gamma^{-1}: min off-diagonal vs time")
print("   (negative = indivisible across t; classical P-divisibility test)")
print("=" * 72)
for sv_, lab in ((0.5, "BROKEN  s=0.5"), (1.0, "UNBROKEN s=1.0")):
    tsl, Hll, Csl = family(sv_, tmax=T_GEN)
    tr = generator_trace(tsl, Hll, Csl)
    line = []
    for t in np.arange(0.5, T_GEN + 1e-9, 0.5):
        v = tr[int(round(t / DT))]
        line.append("   n/a " if v is None else f"{v:7.3f}")
    print(f"{lab}:  t = 0.5, 1.0, ..., {T_GEN}:")
    for k in range(0, len(line), 8):
        print("   ", " ".join(line[k:k + 8]))
    tstar, frac, last = gen_metrics(tsl, tr)
    print(f"    first indivisible time t* = {tstar} | "
          f"fraction of [6,12] indivisible = {frac:.2f} | "
          f"latest value = {last:.3f}")

# ----------------------------------------------------------------------
# E. Sweep across the EP (th = pi/4, EP at s = sin th = 0.7071)
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("E. Sweep across the EP: indivisibility structure vs backflow")
print("=" * 72)
print(f"{'s':>7} {'phase':>9} {'t*':>6} {'lateNeg':>8} {'L@12':>8} "
      f"{'gapViol':>8} {'bfCond<20':>10} {'bfCond>20':>10} {'bfExt':>6} "
      f"{'surv(4)':>8}")
for sv_ in (0.30, 0.50, 0.60, 0.68, SIN, 0.72, 0.75, 0.85, 1.00, 1.30):
    tsf, Hlf, Csf = family(sv_)
    Grf = [np.abs(C) ** 2 for C in Csf]
    tr = generator_trace(tsf, Hlf, Csf)
    tstar, frac, last = gen_metrics(tsf, tr)
    gv, _ = finite_gap_violation(Grf, tsf, sub=True)
    bf_ext, bf_c1, bf_c2 = backflows(tsf, Csf)
    surv = Grf[int(round(4.0 / DT))].sum(0).mean()
    phase = ("EP" if abs(sv_ - SIN) < 1e-9
             else "broken" if sv_ < SIN else "unbroken")
    print(f"{sv_:>7.4f} {phase:>9} "
          f"{('%.2f' % tstar) if tstar else '  --':>6} {frac:>8.2f} "
          f"{last:>8.3f} {gv:>8.3f} {bf_c1:>10.4f} {bf_c2:>10.4f} "
          f"{bf_ext:>6.3f} {surv:>8.4f}")
print()
print("Columns: t* = first indivisible time; lateNeg = fraction of t in")
print("[6,12] with negative generator off-diagonal (1.00 = terminally,")
print("persistently indivisible; intermediate = recurrent windows);")
print("L@12 = generator floor at late time; gapViol = worst finite-gap")
print("unique-divisor violation (cond-guarded); bfCond = conditional TV")
print("backflow in [0,20] / [20,40]; bfExt = extended-space (linear,")
print("3-outcome) TV backflow over [0,40]; surv(4) = mean survival at t=4.")
