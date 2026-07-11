"""
Section 5.3 of PT_stochastic_handoff.md:
The exceptional point -- what survives when the metric dies.

SETUP. Canonical dimer H(s) = [[e^{i th}, s], [s, e^{-i th}]], th = pi/4.
EP at s* = sin(th): eigenvalues cos(th) +- kappa with kappa = sqrt(s^2 -
sin^2 th) -> 0. Approach from the unbroken side, s = s*(1 + eps).

The deflationary argument (handoff section 4.2) rests on rho = eta^{1/2}
existing. At the EP, H is defective, eta singular, rho nonexistent. This
script quantifies the collapse and asks what survives in regularized limits:

 (A) Exactly at the EP: defectiveness; naive |U|^2 grows POLYNOMIALLY (~t^2,
     Jordan block), unlike the broken phase's exponential; the Hermitian
     intertwiner space contains no positive-definite solution -- only a
     singular PSD boundary ray.
 (B) eps -> 0+ scalings: cond(eta) ~ eps^{-1} ~ kappa^{-2} (the Petermann-
     factor divergence: eigenvector overlap 1 - O(kappa^2)), beable-rotation
     anisotropy cond(rho) ~ eps^{-1/2} ~ kappa^{-1}, and at fixed lab time
     ||Gamma_eps(t) - I|| ~ eps ~ (kappa t)^2: the metric-corrected process
     FREEZES to the trivial identity process.
 (C) Rescaled (critical) time tau = kappa * t: Gamma_eps(tau/kappa) converges
     to a nontrivial indivisible Rabi process -- but in coordinates whose
     beable map rho_eps diverges. An abstract process survives; its
     identification with the original configurations does not.
 (D) Reconciliation with section 5.2: the DILATED (open-system) sub-
     stochastic process and its indivisibility generator pass SMOOTHLY
     through the same point. The EP is a coordinate singularity of the
     Hermitian dictionary, not of the stochastic process.

Run:  python exceptional_point.py
"""

import numpy as np
from scipy.linalg import expm, eig

np.set_printoptions(precision=4, suppress=True)

TH = np.pi / 4
SIN, COS = np.sin(TH), np.cos(TH)
SSTAR = SIN
I2 = np.eye(2, dtype=complex)


def build_H(s):
    return np.array([[np.exp(1j * TH), s], [s, np.exp(-1j * TH)]],
                    dtype=complex)


def eta_of(s):
    """Canonical biorthogonal metric, unit-norm eigenvector convention,
    det-normalized so its eigenvalues are {c, 1/c}."""
    E, V = eig(build_H(s))
    V = V / np.linalg.norm(V, axis=0, keepdims=True)
    eta = np.linalg.inv(V @ V.conj().T)
    eta = 0.5 * (eta + eta.conj().T)
    return eta / np.sqrt(np.linalg.det(eta).real)


def psd_sqrt(A):
    w, v = np.linalg.eigh(0.5 * (A + A.conj().T))
    return (v * np.sqrt(np.clip(w, 0, None))) @ v.conj().T


def h_of(s):
    """Hermitian partner h = rho H rho^{-1} (symmetrized) and rho."""
    rho = psd_sqrt(eta_of(s))
    h = rho @ build_H(s) @ np.linalg.inv(rho)
    return 0.5 * (h + h.conj().T), rho


def gamma_metric(s, t):
    """Metric-corrected process via u = exp(-i h t): unitary by
    construction, numerically stable at any t."""
    h, _ = h_of(s)
    return np.abs(expm(-1j * h * t)) ** 2


def hermitian_intertwiners(H):
    """Real null space of eta -> H^dag eta - eta H over the Pauli basis;
    returns list of (eta, eigenvalues)."""
    paulis = [I2, np.array([[0, 1], [1, 0]], dtype=complex),
              np.array([[0, -1j], [1j, 0]], dtype=complex),
              np.array([[1, 0], [0, -1]], dtype=complex)]
    cols = []
    for B in paulis:
        M = H.conj().T @ B - B @ H
        cols.append(np.concatenate([M.real.ravel(), M.imag.ravel()]))
    A = np.array(cols).T
    _, sv, vh = np.linalg.svd(A)
    out = []
    for k in range(4):
        if sv[k] < 1e-10 * max(sv[0], 1):
            eta = sum(c * B for c, B in zip(vh[k], paulis))
            eta = 0.5 * (eta + eta.conj().T)
            out.append((eta, np.linalg.eigvalsh(eta)))
    return out


def loglog_slope(x, y):
    lx, ly = np.log10(np.asarray(x)), np.log10(np.asarray(y))
    return np.polyfit(lx, ly, 1)[0]


# ----------------------------------------------------------------------
# A. Exactly at the EP
# ----------------------------------------------------------------------
print("=" * 72)
print(f"A. At the EP: s* = sin(th) = {SSTAR:.6f}")
print("=" * 72)
Hep = build_H(SSTAR)
E, V = eig(Hep)
print("eigenvalues:", np.round(np.sort_complex(E), 6),
      f" (double, = cos th = {COS:.6f})")
print(f"defective: cond(V) = {np.linalg.cond(V):.3g}, "
      f"rank(H - cos(th) I) = "
      f"{np.linalg.matrix_rank(Hep - COS * I2, tol=1e-12)} (Jordan block)")
tt = np.array([10.0, 20.0, 40.0, 80.0, 160.0])
cs = [np.abs(expm(-1j * Hep * t)) ** 2 for t in tt]
growth = [c.sum(axis=0).max() for c in cs]
print("naive |U|^2 max column sum at t=10..160:", np.round(growth, 1))
print(f"log-log growth exponent: {loglog_slope(tt, growth):.3f} "
      "(expect 2: polynomial t^2 from the Jordan block --")
print(" between unbroken bounded and broken exponential)")
print("Hermitian intertwiners at the EP (eigenvalues):")
for eta, ev in hermitian_intertwiners(Hep):
    kind = ("singular PSD (rank 1)" if min(abs(ev)) < 1e-10 and max(ev) > 0
            else "indefinite" if ev[0] * ev[-1] < 0 else "definite?!")
    print(f"   eigs {np.round(ev, 6)}  -> {kind}")
print("=> no positive-definite metric; the PD cone is exited exactly")
print("   through a singular PSD ray. rho = eta^{1/2} does not exist.")

# ----------------------------------------------------------------------
# B. Approach from the unbroken side: scaling of the collapse
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("B. eps -> 0+ (s = s*(1+eps)): collapse scalings")
print("=" * 72)
eps_list = [10.0 ** (-k) for k in range(1, 8)]
rows = []
for ep in eps_list:
    s = SSTAR * (1 + ep)
    kappa = np.sqrt(s ** 2 - SIN ** 2)
    eta = eta_of(s)
    ev = np.linalg.eigvalsh(eta)
    h, rho = h_of(s)
    dG = np.linalg.norm(gamma_metric(s, 1.3) - np.eye(2))
    rows.append((ep, kappa, ev[1] / ev[0], np.linalg.cond(rho), dG))
print(f"{'eps':>8} {'kappa':>9} {'cond(eta)':>10} {'cond(rho)':>10} "
      f"{'||G(1.3)-I||':>12}")
for r in rows:
    print(f"{r[0]:>8.0e} {r[1]:>9.2e} {r[2]:>10.3e} {r[3]:>10.3e} "
          f"{r[4]:>12.3e}")
e_, k_, ce_, cr_, dg_ = zip(*rows)
print(f"log-log slopes vs eps:  cond(eta): {loglog_slope(e_, ce_):+.3f} "
      f"(expect -1, Petermann ~ kappa^-2) | cond(rho): "
      f"{loglog_slope(e_, cr_):+.3f} (expect -1/2, ~ kappa^-1) | "
      f"||Gamma(t)-I||: {loglog_slope(e_, dg_):+.3f} "
      "(expect +1, ~ (kappa t)^2)")
print("=> at ANY fixed lab time the metric-corrected process converges to")
print("   the FROZEN identity process: h -> cos(th) I, Rabi frequency")
print("   kappa -> 0. The regularized lab-time limit exists but is TRIVIAL --")
print("   and it is NOT the EP dynamics (which grows like t^2).")

# ----------------------------------------------------------------------
# C. Critical rescaling tau = kappa t: what genuinely survives
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("C. Rescaled time tau = kappa*t: the surviving critical process")
print("=" * 72)
taus = (0.5, 1.0, 2.0)
Gs_by_eps = {}
for ep in (1e-2, 1e-4, 1e-6):
    s = SSTAR * (1 + ep)
    kappa = np.sqrt(s ** 2 - SIN ** 2)
    Gs_by_eps[ep] = [gamma_metric(s, tau / kappa) for tau in taus]
for a, b in ((1e-2, 1e-4), (1e-4, 1e-6)):
    dmax = max(np.linalg.norm(x - y)
               for x, y in zip(Gs_by_eps[a], Gs_by_eps[b]))
    print(f"max diff Gamma_eps(tau/kappa), eps {a:.0e} vs {b:.0e}: "
          f"{dmax:.2e}")
Glim = Gs_by_eps[1e-6]
print("limit process Gamma_lim(tau) at tau = 0.5, 1.0, 2.0:")
for tau, G in zip(taus, Glim):
    print(f"  tau={tau}:\n{np.round(G, 4)}")
s6 = SSTAR * (1 + 1e-6)
k6 = np.sqrt(s6 ** 2 - SIN ** 2)
G1, G2 = gamma_metric(s6, 0.7 / k6), gamma_metric(s6, 1.4 / k6)
print(f"indivisibility of the limit family: ||G(2tau) - G(tau)^2|| = "
      f"{np.linalg.norm(G2 - G1 @ G1):.4f}  (> 0)")
h6, rho6 = h_of(s6)
n = (h6 - COS * I2) / k6
print("limit Rabi axis n.sigma (h = cos th I + kappa n.sigma):\n",
      np.round(n, 4))
print(f"...but the beable map at eps=1e-6 has cond(rho) = "
      f"{np.linalg.cond(rho6):.1f} and diverges: the surviving process is")
print("   ABSTRACT -- its identification with the original configurations")
print("   degenerates along with rho.")

# ----------------------------------------------------------------------
# D. The open-system (section 5.2) picture is smooth through the EP
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("D. Closed vs open description across the EP (s = 0.68 ... 0.735)")
print("=" * 72)


def open_quantities(s, t=2.0, tgen=8.0):
    Hl = build_H(s) - 1j * SIN * I2
    C = expm(-1j * Hl * t)
    G = np.abs(C) ** 2
    Cg = expm(-1j * Hl * tgen)
    Gg = np.abs(Cg) ** 2
    L = (2 * np.real(np.conj(Cg) * (-1j * Hl @ Cg))) @ np.linalg.inv(Gg)
    return G[0, 0], G[0, 1], G.sum(0).mean(), L[~np.eye(2, dtype=bool)].min()


print(f"{'s':>8} {'phase':>9} | {'Gred00(2)':>9} {'Gred01(2)':>9} "
      f"{'surv(2)':>8} {'genFloor(8)':>11} | {'cond(eta)':>10}")
for s in np.linspace(0.68, 0.735, 12):
    g00, g01, surv, lmin = open_quantities(s)
    if s > SSTAR + 1e-12:
        ce = f"{np.divide(*np.linalg.eigvalsh(eta_of(s))[::-1]):.3g}"
    elif abs(s - SSTAR) < 1e-6:
        ce = "inf (EP)"
    else:
        ce = "none"
    phase = "broken" if s < SSTAR else "unbroken"
    print(f"{s:>8.4f} {phase:>9} | {g00:>9.4f} {g01:>9.4f} {surv:>8.4f} "
          f"{lmin:>11.4f} | {ce:>10}")
print()
print("Open-side columns vary smoothly through s* = 0.7071 while the")
print("closed-side metric condition number diverges (and does not exist")
print("below). VERDICT: the EP is a coordinate singularity of the")
print("similarity-to-Hermitian dictionary, not of the stochastic process.")
print("Existence of an indivisible process is governed by the dilation")
print("(section 5.2); the deflation (section 4.2) fails AT the EP only")
print("because its coordinates do, and nothing physical is lost there.")
