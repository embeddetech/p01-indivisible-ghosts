"""
Generate all figures for paper/main.tex into paper/figs/.
Self-contained: recomputes every dataset from the model definitions
(formulas identical to the analysis scripts in the repository root).

Figures
  fig_generator.pdf    generator trace: terminal vs recurrent indivisibility
  fig_dissociation.pdf backflow order parameter vs continuous t_c across EP
  fig_ep_scaling.pdf   exceptional-point collapse scalings (log-log)
  fig_pu_ehrenfest.pdf PU ghost realization tracks the classical trajectory
  fig_cascade.pdf      quadratic ghost cascade: exact transience laws
  fig_explosion.pdf    explosion: box-independent leak; reflection off infinity
  fig_channels.pdf     channel-mixing return (S-matrix at infinity)

Run:  python -u make_figures.py     (~5-8 minutes)
"""

import functools
import os
import numpy as np
from scipy.linalg import expm, eig, eigh
from scipy.integrate import quad
import scipy.fft as sfft

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

print = functools.partial(print, flush=True)

plt.rcParams.update({
    "font.size": 9, "axes.labelsize": 9,
    "legend.fontsize": 7.5, "xtick.labelsize": 8, "ytick.labelsize": 8,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.25, "grid.linewidth": 0.5,
    "lines.linewidth": 1.4, "figure.dpi": 150,
    "savefig.bbox": "tight", "font.family": "serif",
    "mathtext.fontset": "cm", "legend.frameon": False,
})
# Okabe-Ito (CVD-safe), fixed identity assignment across all figures:
BLUE, VERM, GREEN, ORANGE = "#0072B2", "#D55E00", "#009E73", "#E69F00"
GRAY = "#666666"
CH = [BLUE, VERM, GREEN, ORANGE]          # channels n = 0..3, fixed order

FIGS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
os.makedirs(FIGS, exist_ok=True)

TH = np.pi / 4
SIN = np.sin(TH)
I2 = np.eye(2, dtype=complex)


def H_dimer(s):
    return np.array([[np.exp(1j * TH), s], [s, np.exp(-1j * TH)]],
                    dtype=complex)


def H_loss(s):
    return H_dimer(s) - 1j * SIN * I2


def pqr(s, t):
    k = np.sqrt(SIN ** 2 - s ** 2 + 0j)
    c = np.cosh(k * t)
    shc = t if abs(k) < 1e-14 else np.sinh(k * t) / k
    return ((c + SIN * shc).real, (c - SIN * shc).real, (s * shc).real)


def L_offdiag_analytic(s, t):
    p, q, r = pqr(s, t)
    det = 1 - 2 * r * r
    return 2 * s * p * r / det, 2 * s * q * r / det, det


def L_offdiag_numeric(s, t):
    Hl = H_loss(s)
    C = expm(-1j * Hl * t)
    G = np.abs(C) ** 2
    Gd = 2 * np.real(np.conj(C) * (-1j * Hl @ C))
    L = Gd @ np.linalg.inv(G)
    return L[0, 1], L[1, 0]


def t_c(s):
    k2 = SIN ** 2 - s ** 2
    if k2 > 0:
        k = np.sqrt(k2)
        return np.arcsinh(k / (s * np.sqrt(2))) / k
    if k2 < 0:
        ka = np.sqrt(-k2)
        return np.arcsin(ka / (s * np.sqrt(2))) / ka
    return 1 / (s * np.sqrt(2))


# ----------------------------------------------------------------------
print("fig_generator ...")
fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.5))
for ax, s, col, lab, tmax, ylim in (
        (axes[0], 0.5, BLUE, "broken, $s=0.5$", 8.0, (-6, 2)),
        (axes[1], 1.0, VERM, "unbroken, $s=1.0$", 12.0, (-6, 4))):
    ts = np.linspace(0.01, tmax, 3000)
    vals = []
    for t in ts:
        l12, l21, det = L_offdiag_analytic(s, t)
        v = min(l12, l21)
        vals.append(np.nan if (abs(det) < 0.02 or abs(v) > 8) else v)
    ax.plot(ts, vals, color=col, label="analytic")
    tn = np.arange(0.4, tmax, 0.6)
    vn = []
    for t in tn:
        v = min(L_offdiag_numeric(s, t))
        vn.append(np.nan if abs(v) > 8 else v)
    ax.plot(tn, vn, "o", ms=3.5, mfc="none", mec="k", mew=0.7,
            label="numerical", zorder=5)
    ax.axhline(0, color="k", lw=0.6)
    ax.set_xlabel("$t$")
    ax.set_ylim(*ylim)
    ax.text(0.02, 1.02, lab, transform=ax.transAxes, fontsize=8.5)
k = np.sqrt(SIN ** 2 - 0.25)
axes[0].axvline(t_c(0.5), color=GRAY, ls=":", lw=1)
axes[0].text(t_c(0.5) + 0.12, 1.2, "$t_c$", color=GRAY, fontsize=8.5)
axes[0].axhline(-(SIN + k), color=GRAY, ls="--", lw=1)
axes[0].text(4.6, -(SIN + k) + 0.25, r"$-(\sin\theta+\tilde\kappa)$",
             color=GRAY, fontsize=8.5)
axes[0].set_ylabel(r"$\min\,\mathrm{offdiag}\;L(t)$")
axes[0].legend(loc="lower right")
fig.savefig(os.path.join(FIGS, "fig_generator.pdf"))
plt.close(fig)

# ----------------------------------------------------------------------
print("fig_dissociation ...")


def backflow_windows(s, tmax=40.0, dt=0.05):
    Hl = H_loss(s)
    ts = np.arange(0.0, tmax + 1e-9, dt)
    D = []
    for t in ts:
        G = np.abs(expm(-1j * Hl * t)) ** 2
        pc = [G[:, j] / G[:, j].sum() for j in (0, 1)]
        D.append(0.5 * np.abs(pc[0] - pc[1]).sum())
    D = np.array(D)
    inc = np.clip(np.diff(D), 0, None)
    return inc[ts[:-1] < 20].sum(), inc[ts[:-1] >= 20].sum()


svals = np.concatenate([np.arange(0.30, 1.301, 0.05),
                        [0.69, SIN, 0.715, 0.73]])
svals = np.sort(svals)
bf1, bf2 = zip(*(backflow_windows(s) for s in svals))
fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.5))
ax = axes[0]
ax.plot(svals, bf1, "-o", ms=3, color=BLUE, label=r"window $t\in[0,20]$")
ax.plot(svals, bf2, "-s", ms=3, color=VERM, label=r"window $t\in[20,40]$")
ax.axvline(SIN, color=GRAY, ls=":", lw=1)
ax.text(SIN + 0.015, 6.2, "EP", color=GRAY, fontsize=8.5)
ax.set_xlabel("$s$")
ax.set_ylabel("conditional TV backflow")
ax.legend(loc="upper left")
ax = axes[1]
scurve = np.linspace(0.3, 1.3, 400)
ax.plot(scurve, [t_c(s) for s in scurve], color=GREEN, label="analytic $t_c(s)$")
sdots = [0.4, 0.6, 0.8, 1.0, 1.2]
tdots = []
for s in sdots:
    tt = np.arange(0.02, 4.0, 0.002)
    v = np.array([min(L_offdiag_numeric(s, t)) for t in tt])
    tdots.append(tt[np.argmax(v < -1e-8)])
ax.plot(sdots, tdots, "o", ms=3.5, mfc="none", mec="k", mew=0.7,
        label="numerical", zorder=5)
ax.axvline(SIN, color=GRAY, ls=":", lw=1)
ax.set_xlabel("$s$")
ax.set_ylabel("first indivisible time $t_c$")
ax.legend(loc="upper right")
fig.savefig(os.path.join(FIGS, "fig_dissociation.pdf"))
plt.close(fig)

# ----------------------------------------------------------------------
print("fig_ep_scaling ...")
eps = 10.0 ** (-np.arange(1, 8, dtype=float))
ce, cr, dg = [], [], []
for ep in eps:
    s = SIN * (1 + ep)
    E, V = eig(H_dimer(s))
    V = V / np.linalg.norm(V, axis=0, keepdims=True)
    eta = np.linalg.inv(V @ V.conj().T)
    eta = 0.5 * (eta + eta.conj().T)
    eta /= np.sqrt(np.linalg.det(eta).real)
    ev = np.linalg.eigvalsh(eta)
    ce.append(ev[1] / ev[0])
    w, u = np.linalg.eigh(eta)
    rho = (u * np.sqrt(w)) @ u.conj().T
    cr.append(np.linalg.cond(rho))
    h = rho @ H_dimer(s) @ np.linalg.inv(rho)
    h = 0.5 * (h + h.conj().T)
    G = np.abs(expm(-1j * h * 1.3)) ** 2
    dg.append(np.linalg.norm(G - np.eye(2)))
fig, ax = plt.subplots(figsize=(3.6, 2.7))
for y, col, mk, lab in ((ce, BLUE, "o", r"$\mathrm{cond}(\eta)\;(\sim\varepsilon^{-1})$"),
                        (cr, VERM, "s", r"$\mathrm{cond}(\rho)\;(\sim\varepsilon^{-1/2})$"),
                        (dg, GREEN, "^", r"$\|\Gamma(1.3)-\mathbf{1}\|\;(\sim\varepsilon)$")):
    ax.loglog(eps, y, mk + "-", ms=4, color=col, label=lab)
    sl = np.polyfit(np.log10(eps), np.log10(y), 1)[0]
    ax.annotate(f"slope ${sl:+.3f}$", xy=(eps[3], y[3]),
                xytext=(4, -11 if col == GREEN else 5),
                textcoords="offset points", fontsize=7.5, color=col)
ax.set_xlabel(r"$\varepsilon=(s-s_*)/s_*$")
ax.legend(loc="center left", fontsize=7)
fig.savefig(os.path.join(FIGS, "fig_ep_scaling.pdf"))
plt.close(fig)

# ----------------------------------------------------------------------
print("fig_pu_ehrenfest ... (two 1936-dim diagonalizations)")
GAM = 1.0


def spectral_ops(n=44, L=10.0):
    dx = 2 * L / n
    x = -L + dx * np.arange(n)
    F = np.fft.fft(np.eye(n), axis=0, norm="ortho")
    kv = 2 * np.pi * np.fft.fftfreq(n, d=dx)
    P = F.conj().T @ (kv[:, None] * F)
    P2 = F.conj().T @ ((kv ** 2)[:, None] * F)
    return x, 0.5 * (P + P.conj().T), 0.5 * (P2 + P2.conj().T)


def pu_track(w1, w2, tmax):
    x, P, P2 = spectral_ops()
    n = len(x)
    In = np.eye(n)
    H = (np.kron(P, np.diag(x)) + np.kron(In, P2) / (2 * GAM)
         + (GAM / 2) * (w1 ** 2 + w2 ** 2) * np.kron(In, np.diag(x ** 2))
         - (GAM / 2) * (w1 * w2) ** 2 * np.kron(np.diag(x ** 2), In))
    E, V = eigh(H)
    g1 = np.exp(-(x - 2.0) ** 2 / 2)
    g2 = np.exp(-x ** 2 / 2)
    psi0 = np.kron(g1, g2).astype(complex)
    psi0 /= np.linalg.norm(psi0)
    c0 = V.conj().T @ psi0
    xw = np.repeat(x, n)
    Om = w1 ** 2 + w2 ** 2
    K = np.array([[0, 1, 0, 0], [0, 0, 0, 1 / GAM],
                  [GAM * (w1 * w2) ** 2, 0, 0, 0], [0, -GAM * Om, -1, 0]])
    tq = np.linspace(0, tmax, 33)
    xq = [float(xw @ np.abs(V @ (np.exp(-1j * E * t) * c0)) ** 2)
          for t in tq]
    tc_ = np.linspace(0, tmax, 400)
    xc = [(expm(K * t) @ np.array([2.0, 0, 0, 0]))[0] for t in tc_]
    return tq, xq, tc_, xc


fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.5))
for ax, (w1, w2), tmax, lab in ((axes[0], (1.0, 0.5), 8.0,
                                 r"unequal, $\omega_{1,2}=(1,\,0.5)$"),
                                (axes[1], (0.75, 0.75), 3.5,
                                 r"equal (PU exceptional point), $\omega=0.75$")):
    tq, xq, tcl, xcl = pu_track(w1, w2, tmax)
    ax.plot(tcl, xcl, color=GRAY, lw=1.1, label="classical")
    ax.plot(tq, xq, "o", ms=3.5, mfc="none", mec=BLUE, mew=0.9,
            label=r"quantum $\langle x(t)\rangle$")
    if w1 == w2:
        env = np.sqrt(4 + (w1 * tcl) ** 2)
        ax.plot(tcl, env, ":", color=GRAY, lw=0.8)
        ax.plot(tcl, -env, ":", color=GRAY, lw=0.8)
    ax.set_xlabel("$t$")
    ax.text(0.02, 1.02, lab, transform=ax.transAxes, fontsize=8.5)
axes[0].set_ylabel(r"$\langle x\rangle$")
axes[0].legend(loc="lower left")
fig.savefig(os.path.join(FIGS, "fig_pu_ehrenfest.pdf"))
plt.close(fig)

# ----------------------------------------------------------------------
print("fig_cascade ... (two 1156-dim diagonalizations)")
NF = 34
g = 0.15


def two_mode(ghost):
    a = np.diag(np.sqrt(np.arange(1, NF)), 1)
    nmat = np.diag(np.arange(NF)).astype(float)
    In = np.eye(NF)
    A, B = np.kron(a, In), np.kron(In, a)
    sgn = -1.0 if ghost else 1.0
    return (np.kron(nmat, In) + sgn * np.kron(In, nmat)
            + g * (A.T @ B.T + A @ B)), np.kron(nmat, In)


tsc = np.linspace(0, 12, 33)
curves = {}
for ghost in (True, False):
    H, N1 = two_mode(ghost)
    E, V = eigh(H)
    psi0 = np.zeros(H.shape[0])
    psi0[0] = 1.0
    c0 = V.T @ psi0
    n1idx = np.arange(NF).repeat(NF)
    ns, pk = [], []
    for t in tsc:
        w = np.abs(V @ (np.exp(-1j * E * t) * c0)) ** 2
        ns.append(float(w @ N1.diagonal()))
        pk.append(float(w[n1idx <= 10].sum()))
    curves[ghost] = (np.array(ns), np.array(pk))
fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.5))
tt = np.linspace(0, 12, 400)
ax = axes[0]
ax.semilogy(tt, np.sinh(g * tt) ** 2 + 1e-12, color=GRAY, lw=1.1,
            label=r"$\sinh^2(gt)$")
ax.semilogy(tsc, curves[True][0] + 1e-12, "o", ms=3.5, mfc="none",
            mec=BLUE, mew=0.9, label="ghost (resonant)")
ax.semilogy(tsc, curves[False][0] + 1e-12, "s", ms=3, mfc="none",
            mec=VERM, mew=0.9, label="normal twin")
ax.set_xlabel("$t$")
ax.set_ylabel(r"$\langle n_1(t)\rangle$")
ax.set_ylim(1e-5, 30)
ax.legend(loc="lower right")
ax = axes[1]
ax.plot(tt, 1 - np.tanh(g * tt) ** 22, color=GRAY, lw=1.1,
        label=r"$1-\tanh^{2K+2}(gt),\;K=10$")
ax.plot(tsc, curves[True][1], "o", ms=3.5, mfc="none", mec=BLUE, mew=0.9,
        label="ghost (numerical)")
ax.set_xlabel("$t$")
ax.set_ylabel(r"$P(n_1\leq 10)$")
ax.set_ylim(0.55, 1.02)
ax.legend(loc="lower left")
fig.savefig(os.path.join(FIGS, "fig_cascade.pdf"))
plt.close(fig)

# ----------------------------------------------------------------------
print("fig_explosion ... (absorbing runs and two completions)")


def cap_run(L, dx=1.2e-3, dt=5e-5, tmax=1.5, x0=2.0, sig=0.5):
    N = int(round(2 * L / dx))
    x = -L + dx * np.arange(N)
    kv = 2 * np.pi * sfft.fftfreq(N, d=dx)
    edge = 0.7 * L
    W = 400.0 * np.clip((np.abs(x) - edge) / (L - edge), 0, None) ** 2
    half = np.exp((-1j * (-x ** 4) - W) * dt / 2)
    kin = np.exp(-1j * kv ** 2 * dt / 2)
    psi = np.exp(-(x - x0) ** 2 / (2 * sig ** 2)).astype(complex)
    psi /= np.linalg.norm(psi)
    nst = int(round(tmax / dt))
    rec = max(1, nst // 300)
    ts, A = [0.0], [0.0]
    for s_ in range(1, nst + 1):
        psi = half * sfft.ifft(kin * sfft.fft(half * psi))
        if s_ % rec == 0:
            ts.append(s_ * dt)
            A.append(1.0 - float(np.sum(np.abs(psi) ** 2)))
    return np.array(ts), np.array(A)


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
        kv = 2 * np.pi * sfft.fftfreq(N, d=dx)
        kin = np.exp(-1j * kv ** 2 * dt / 2)
        fwd, bwd = sfft.fft, sfft.ifft
    half = np.exp(-1j * (-x ** 4) * dt / 2)
    psi = np.exp(-(x - x0) ** 2 / (2 * sig ** 2)).astype(complex)
    psi /= np.linalg.norm(psi)
    mL, mC, mR = x < -5, np.abs(x) <= 5, x > 5
    nst = int(round(tmax / dt))
    rec = max(1, nst // 200)
    ts, PL, PC, PR = [0.0], [0.0], [1.0], [0.0]
    for s_ in range(1, nst + 1):
        psi = half * bwd(kin * fwd(half * psi))
        if s_ % rec == 0:
            w = np.abs(psi) ** 2
            ts.append(s_ * dt)
            PL.append(float(w[mL].sum()))
            PC.append(float(w[mC].sum()))
            PR.append(float(w[mR].sum()))
    return np.array(ts), np.array(PL), np.array(PC), np.array(PR)


def tof_rest(x0, x1):
    E = -x0 ** 4
    f = lambda u: 2 * u / np.sqrt(2 * (E + (x0 + u * u) ** 4))
    return quad(f, 1e-9, np.sqrt(x1 - x0), limit=400)[0]


fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.5))
ax = axes[0]
for L, col in ((8.0, BLUE), (12.0, VERM), (16.0, GREEN)):
    ts, A = cap_run(L)
    ax.plot(ts, A, color=col, label=f"$L={int(L)}$")
    ax.axvline(tof_rest(2.0, 0.7 * L), color=col, ls=":", lw=0.8)
Tesc = tof_rest(2.0, 1e6)
ax.axvline(Tesc, color="k", ls="--", lw=0.9)
ax.text(Tesc + 0.02, 0.35, r"$T_{\rm esc}$", fontsize=8.5)
ax.set_xlabel("$t$")
ax.set_ylabel("absorbed probability")
ax.legend(loc="center right")
ax.text(0.02, 1.02, r"minimal process, $V=-x^4$", transform=ax.transAxes,
        fontsize=8.5)
ax = axes[1]
for kind, col in (("dirichlet", BLUE), ("periodic", VERM)):
    ts, PL, PC, PR = wall_run(kind)
    disp = "Dirichlet" if kind == "dirichlet" else "periodic"
    ax.plot(ts, PC, color=col, label=f"{disp}: $P(|x|\\leq 5)$")
    side = PR if kind == "dirichlet" else PL
    slab = ("Dirichlet: $P(x>5)$" if kind == "dirichlet"
            else "periodic: $P(x<-5)$")
    ax.plot(ts, side, ls="--", lw=1.0, color=col, label=slab)
ax.set_xlabel("$t$")
ax.set_ylabel("probability")
ax.legend(loc="center right", fontsize=6.8)
ax.text(0.02, 1.02, "two conservative completions, $L=12$",
        transform=ax.transAxes, fontsize=8.5)
fig.savefig(os.path.join(FIGS, "fig_explosion.pdf"))
plt.close(fig)

# ----------------------------------------------------------------------
print("fig_channels ... (transverse basis + two wall runs)")
M = 4
ALPHA = 2.5
MU = 0.2


def transverse():
    n1, l1 = 1600, 9.0
    dx1 = 2 * l1 / (n1 + 1)
    x1 = -l1 + dx1 * np.arange(1, n1 + 1)
    A = (np.diag(1.0 / dx1 ** 2 + 0.5 * x1 ** 2)
         + np.diag(np.full(n1 - 1, -0.5 / dx1 ** 2), 1)
         + np.diag(np.full(n1 - 1, -0.5 / dx1 ** 2), -1))
    w, v = np.linalg.eigh(A)
    B = v[:, :M].T @ (np.tanh(x1)[:, None] * v[:, :M])
    return w[:M], 0.5 * (B + B.T)


EN, B0 = transverse()


def channel_run(L, dx=8e-3, dt=1e-4, tmax=4.0, x0=2.0, sig=0.5, mu=MU):
    N = int(round(2 * L / dx)) - 1
    x = -L + dx * np.arange(1, N + 1)
    kn = np.pi * np.arange(1, N + 1) / (2 * L)
    kin = np.exp(-1j * kn ** 2 * dt / 2)[:, None]
    gc = x ** 2 / (1 + 0.1 * x ** 2)
    Vm = (-(np.abs(x) ** ALPHA))[:, None, None] * np.eye(M) \
        + np.eye(M) * EN + (mu * gc)[:, None, None] * B0
    w, v = np.linalg.eigh(Vm)
    ph = np.exp(-1j * w * dt / 2)

    def apply_V(psi):
        c = np.einsum("inm,in->im", np.conj(v), psi)
        return np.einsum("inm,im->in", v, ph * c)

    psi = np.zeros((N, M), dtype=complex)
    psi[:, 0] = np.exp(-(x - x0) ** 2 / (2 * sig ** 2))
    psi /= np.linalg.norm(psi)
    mask = np.abs(x) < 4.0
    nst = int(round(tmax / dt))
    rec = max(1, nst // 200)
    ts, Pn = [0.0], [np.array([1.0, 0, 0, 0])]
    for s_ in range(1, nst + 1):
        psi = apply_V(psi)
        psi = sfft.idst(kin * sfft.dst(psi, type=1, axis=0),
                        type=1, axis=0)
        psi = apply_V(psi)
        if s_ % rec == 0:
            w2 = np.abs(psi) ** 2
            ts.append(s_ * dt)
            Pn.append(w2[mask].sum(axis=0))
    return np.array(ts), np.array(Pn)


fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.5), sharey=True)
for ax, L in ((axes[0], 6.0), (axes[1], 9.0)):
    ts, Pn = channel_run(L)
    for n in range(M):
        ax.plot(ts, Pn[:, n], color=CH[n], label=f"$n={n}$")
    ax.set_xlabel("$t$")
    ax.text(0.02, 1.02, f"regulator at $L={int(L)}$",
            transform=ax.transAxes, fontsize=8.5)
axes[0].set_ylabel(r"$P_n(|x|<4)$")
axes[0].legend(loc="center right", fontsize=7)
fig.savefig(os.path.join(FIGS, "fig_channels.pdf"))
plt.close(fig)

print("all figures written to", FIGS)
