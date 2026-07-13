"""
The M -> infinity channel tail, attacked directly on the FULL operator:
a von Neumann certificate probe of (non-)essential-self-adjointness for
the exact quartic Pais-Uhlenbeck operator.

OPERATOR (unitarily equivalent to H_PU + lam q1^4), (k,p) representation:
    S = -a d^2/dk^2 + b d^2/dp^2 + U(k,p),
    a = 1/(2gO), b = gO/2, c = 1/(gO),
    U = -lam (k+cp)^4 + (g wb/2)(k+cp)^2 - p^2/(2g).

IMPORTANT CORRECTION (see glued_certificate_1d.py for the fixed
method). The original intent -- windowed near-solutions beating the von
Neumann bound ||(S - iZ)psi|| >= Z||psi|| -- is MATHEMATICALLY
IMPOSSIBLE: every compactly supported smooth psi lies in D(S-bar),
where the bound holds unconditionally, for EVERY operator. No compact
probe can witness deficiency: the completion data lives entirely at
infinity. The numbers produced here obey the bound throughout
(validating the numerics), and what this script actually measures is a
CLOSURE-DEFECT DIAGNOSTIC: how closely the best windowed candidate
approaches the forbidden bound.

Empirical classes: falling (limit-circle-type) channels hug the bound
(ratio ~ 1.2), while confining/e.s.a. operators sit far above (4.9 for
+k^4; 641 for the 2D lam < 0 control). The five 2D lam > 0 beam
launches all land in the falling class (1.21-1.29) -- evidence, never
proof. A genuine certificate requires candidates with analytic tails
supplied to infinity: implemented in 1D in glued_certificate_1d.py;
the 2D extension (analytic beam tails under the ridge drift, where the
ridge channel is only quadratically falling = limit-point-marginal) is
the precise remaining gap for the M -> infinity question.

Run:  python -u tail_certificate.py     (~2-4 minutes)
"""

import functools
import numpy as np

print = functools.partial(print, flush=True)

GAM, W1, W2, LAM = 1.0, 1.0, 0.5, 0.05
OMEGA, WBAR = W1 ** 2 + W2 ** 2, (W1 * W2) ** 2
A = 1.0 / (2 * GAM * OMEGA)
B = GAM * OMEGA / 2
C = 1.0 / (GAM * OMEGA)


def smooth_rise(x):
    """C^1 smoothstep 0->1 on [0,1] (sin^2)."""
    return np.sin(0.5 * np.pi * np.clip(x, 0, 1)) ** 2


def fd8_axis0(F, dx):
    c = np.array([-1 / 560, 8 / 315, -1 / 5, 8 / 5, -205 / 72,
                  8 / 5, -1 / 5, 8 / 315, -1 / 560])
    out = np.zeros_like(F)
    n = F.shape[0]
    for j, cj in enumerate(c):
        out[4:n - 4] += cj * F[j:n - 8 + j]
    return out / dx ** 2


def certificate(label, Ufunc, Z, Kin, Kout, ell_in, ell_out,
                Np=1, pmax=1.0, p0=0.0, sigp=1.0, dk=1.5e-3, sstore=4):
    """March the decaying branch from Kout down to Kin, window, and
    evaluate the von Neumann ratio."""
    if Np > 1:
        dp = 2 * pmax / (Np + 1)
        p = -pmax + dp * np.arange(1, Np + 1)
    else:
        dp, p = 1.0, np.zeros(1)
    nsteps = int(round((Kout - Kin) / dk))

    def Lapply(psi, k):
        out = (Ufunc(k, p) - 1j * Z)[:, None] * psi
        if Np > 1:
            lap = np.zeros_like(psi)
            lap[1:-1] = psi[2:] - 2 * psi[1:-1] + psi[:-2]
            lap[0] = psi[1] - 2 * psi[0]
            lap[-1] = psi[-2] - 2 * psi[-1]
            out += (B / dp ** 2) * lap
        return out / A

    # initial decaying-branch data at Kout (pointwise WKB in p)
    kap = np.sqrt((Ufunc(Kout, p) - 1j * Z) / A + 0j)
    kap = np.where(kap.real >= 0, kap, -kap)
    prof = np.exp(-(p - p0) ** 2 / (2 * sigp ** 2)) if Np > 1 \
        else np.ones(1)
    psi = prof.astype(complex)[:, None]
    psip = (prof * np.exp(-kap * dk))[:, None]      # slice at Kout + dk
    stored = [psi[:, 0].copy()]
    scale_log = 0.0
    for n in range(nsteps):
        k = Kout - n * dk
        new = 2 * psi - psip + dk ** 2 * Lapply(psi, k)
        psip, psi = psi, new
        m = np.abs(psi).max()
        if m > 1e100:                                # rescale, track log
            psi /= m
            psip /= m
            stored = [s / m for s in stored]
        if (n + 1) % sstore == 0:
            stored.append(psi[:, 0].copy())
    F = np.stack(stored[::-1])                       # ascending k
    kk = np.linspace(Kin, Kout, F.shape[0])
    dks = kk[1] - kk[0]
    F = F / np.abs(F).max()

    # window
    wk = smooth_rise((kk - Kin) / ell_in) * smooth_rise((Kout - kk)
                                                        / ell_out)
    W = wk[:, None] * F
    if Np > 1:
        wp = smooth_rise((p + pmax - 0.5) / 2.0) * smooth_rise(
            (pmax - 0.5 - p) / 2.0)
        W = W * wp[None, :]

    # residual of the (semi-discrete in p) operator
    res = -A * fd8_axis0(W, dks)
    if Np > 1:
        lap = np.zeros_like(W)
        lap[:, 1:-1] = W[:, 2:] - 2 * W[:, 1:-1] + W[:, :-2]
        lap[:, 0] = W[:, 1] - 2 * W[:, 0]
        lap[:, -1] = W[:, -2] - 2 * W[:, -1]
        res += (B / dp ** 2) * lap
    Ug = np.array([Ufunc(k, p) for k in kk])
    res += (Ug - 1j * Z) * W
    sl = slice(4, len(kk) - 4)
    ratio = (np.sqrt(np.sum(np.abs(res[sl]) ** 2))
             / (Z * np.sqrt(np.sum(np.abs(W[sl]) ** 2))))
    conc = np.abs(F).max(axis=1) if Np > 1 else np.abs(F[:, 0])
    sat = conc[0] / max(conc[len(conc) // 2], 1e-300)
    print(f"  {label}")
    print(f"    ratio ||(S-iZ)psi||/(Z||psi||) = {ratio:8.4f}   "
          f"[{'PASS: NOT e.s.a.' if ratio < 1 else 'no certificate'}]"
          f"   growth K_in/mid = {sat:.2e}")
    return ratio


print("=" * 72)
print("Von Neumann certificates (pass = NOT essentially self-adjoint;")
print("e.s.a. operators can never pass -- controls validate numerics)")
print("=" * 72)
Z = 30.0
print()
print("T1. 1D calibration:")
certificate("falling quartic  U=-0.05k^4    (LC: hugs bound ~1.2)",
            lambda k, p: np.full_like(p, -LAM * k ** 4, dtype=float),
            Z, 6.5, 13.0, 2.0, 2.0)
certificate("falling quadratic U=-0.78k^2   (LP-marginal: hugs bound)",
            lambda k, p: np.full_like(p, -0.78 * k ** 2, dtype=float),
            Z, 6.5, 13.0, 2.0, 2.0)
certificate("confining quartic U=+0.05k^4   (e.s.a.: far above bound)",
            lambda k, p: np.full_like(p, +LAM * k ** 4, dtype=float),
            Z, 6.5, 13.0, 2.0, 2.0)

print()
print("T2. Full 2D quartic PU, lam = +0.05 (beam launch points scanned):")


def U_pu(lam):
    def U(k, p):
        s = k + C * p
        return (-lam * s ** 4 + (GAM * WBAR / 2) * s ** 2
                - p ** 2 / (2 * GAM))
    return U


best = np.inf
for (p0, sigp, Kin, Kout, tag) in (
        (0.0, 1.0, 6.5, 13.0, "fixed-p fiber launch, p0 = 0"),
        (0.0, 2.0, 6.5, 13.0, "wider beam, p0 = 0"),
        (-5.0, 1.0, 6.5, 13.0, "off-ridge launch, p0 = -5"),
        (0.0, 1.0, 9.0, 16.0, "outer window, p0 = 0"),
        (-12.0, 1.5, 8.0, 14.0, "near-ridge launch, p0 = -12")):
    r = certificate(f"lam=+0.05: {tag}", U_pu(+LAM), Z, Kin, Kout,
                    2.0, 2.0, Np=601, pmax=30.0, p0=p0, sigp=sigp)
    best = min(best, r)

print()
print("T3. 2D control, lam = -0.05 (predicted complete: must fail):")
certificate("lam=-0.05: fixed-p launch, p0 = 0", U_pu(-LAM), Z,
            6.5, 13.0, 2.0, 2.0, Np=601, pmax=30.0, p0=0.0, sigp=1.0)

print()
print(f"Best lam=+0.05 ratio: {best:.4f}")
print("Read-out (closure-defect diagnostic; see header): all ratios are")
print(">= 1 as the von Neumann bound demands of compactly supported")
print("candidates -- no window can ever witness deficiency. Falling-")
print("channel operators hug the bound (~1.2); confining/e.s.a. ones sit")
print("far above. The 2D lam > 0 PU lands in the falling class at every")
print("launch point; the lam < 0 control lands in the e.s.a. class.")
