"""
The gauge form of the fixed-beable criterion:
THE NON-HERMITIAN SKIN EFFECT IS THE OBSTRUCTION TO FIXED BEABLES.

GAUGE-FORM LEMMA. A matrix H with symmetric support satisfies K3
(H_jk H_kj > 0) iff its couplings can be written uniquely as
    H_jk = t_jk exp( i phi_jk + w_jk ),
with t_jk = t_kj > 0 (bare hopping), phi antisymmetric real (a REAL gauge
field / Peierls phase) and w antisymmetric real (an IMAGINARY gauge
field, i.e. p -> p - A - iW on the lattice). K1 = real on-site potential
(no local gain/loss).

THEOREM (skin obstruction). For gauge-form H with real diagonal:
 (i)  A fixed-beable indivisible representation exists iff the IMAGINARY
      FLUX vanishes through every cycle: sum_C w = 0. Then w_jk =
      chi_j - chi_k is pure gauge, the metric is the exponentiated
      imaginary gauge transformation eta = diag(e^{-2 chi}), and
      Gamma_jk = e^{2(chi_k - chi_j)} |U_jk|^2. The REAL flux (magnetic
      field) is unconstrained.
 (ii) Classical dictionary: with hopping rates q(j->k) = |H_kj|, the
      imaginary flux is the cycle affinity of the rate graph: it vanishes
      iff the classical chain is reversible (Kolmogorov), and nonzero
      imaginary flux = nonzero steady-state cycle current
      (nonequilibrium irreversibility).
 (iii) Hatano-Nelson corollary: a ring with uniform w carries flux N w:
      no fixed beables -- indeed the PBC spectrum is a complex loop
      (spectral winding, the topological invariant of the skin effect),
      so no closed process exists at all. An OPEN chain is a tree: w is
      pure gauge, fixed beables exist at every finite N with metric
      weights d_i = e^{2wi}; the OBC skin localization of eigenvectors
      IS this gauge factor, and cond(eta) = e^{2w(N-1)} grows
      exponentially -- in the thermodynamic limit the fixed-beable
      metric becomes unbounded (the Pais-Uhlenbeck pathology in 1D
      lattice form).

Verified below; produces paper figure figs/fig_skin.pdf.
Run:  python skin_effect_beables.py     (< 1 minute)
"""

import os
import numpy as np
from scipy.linalg import expm, eig, null_space

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(1)
TOL = 1e-9


# ---------------------------------------------------------------- helpers
def diagonal_metric(H, tol=TOL):
    n = H.shape[0]
    fails = []
    if not np.allclose(H.diagonal().imag, 0, atol=1e-8):
        fails.append("K1")
    sup = (np.abs(H) > tol) & ~np.eye(n, dtype=bool)
    if not np.array_equal(sup, sup.T):
        return None, ["K2"]
    for i in range(n):
        for j in range(i + 1, n):
            if sup[i, j]:
                p = H[i, j] * H[j, i]
                if abs(p.imag) > 1e-8 * max(abs(p), 1) or p.real <= 0:
                    fails.append("K3")
    if fails:
        return None, fails
    d = np.zeros(n)
    for root in range(n):
        if d[root] > 0:
            continue
        d[root] = 1.0
        stack = [root]
        while stack:
            j = stack.pop()
            for i in range(n):
                if sup[i, j] and d[i] == 0:
                    d[i] = d[j] * abs(H[j, i]) / abs(H[i, j])
                    stack.append(i)
    resid = np.linalg.norm(np.diag(d) @ H - H.conj().T @ np.diag(d))
    if resid > 1e-7 * max(np.linalg.norm(H), 1):
        return None, ["K4"]
    return d, []


def nullspace_dim(H, tol=1e-8):
    n = H.shape[0]
    rows = []
    for i in range(n):
        for j in range(n):
            re, im = np.zeros(n), np.zeros(n)
            re[i] += H[i, j].real
            im[i] += H[i, j].imag
            re[j] -= H[j, i].real
            im[j] += H[j, i].imag
            rows += [re, im]
    sv = np.linalg.svd(np.array(rows), compute_uv=False)
    return int(np.sum(sv < tol * max(sv[0], 1)))


def real_spectrum(H):
    E = eig(H, right=False)
    return bool(np.allclose(E.imag, 0, atol=1e-8)), E


# ---------------------------------------------------------------- A
print("=" * 72)
print("A. Random gauge-form graphs: fixed beables <=> zero imaginary flux")
print("=" * 72)
ok = 0
TRIALS = 50
for trial in range(TRIALS):
    n = int(rng.integers(5, 9))
    edges = [(i, int(rng.integers(0, i))) for i in range(1, n)]  # tree
    extra = []
    while len(extra) < 2:                                  # ensure cycles
        i, j = rng.integers(0, n, 2)
        e = (max(i, j), min(i, j))
        if i != j and e not in edges and e not in extra:
            extra.append(e)
    chi = rng.normal(0, 0.7, n)
    H = np.diag(rng.normal(0, 1, n)).astype(complex)
    for (i, j) in edges + extra:
        t = rng.uniform(0.5, 1.5)
        phi = rng.uniform(-np.pi, np.pi)      # real gauge field: arbitrary
        w = chi[i] - chi[j]                   # imaginary field: pure gauge
        H[i, j] = t * np.exp(1j * phi + w)
        H[j, i] = t * np.exp(-1j * phi - w)
    d, fails = diagonal_metric(H)
    assert d is not None, (trial, fails)
    ratio = d * np.exp(2 * chi)
    assert np.allclose(ratio / ratio[0], 1, rtol=1e-8), trial
    assert real_spectrum(H)[0], trial
    # inject imaginary flux through the cycle containing an extra edge
    Hb = H.copy()
    i, j = extra[0]
    Hb[i, j] *= np.exp(0.4)
    Hb[j, i] *= np.exp(-0.4)                 # still gauge form, K3 intact
    db, fb = diagonal_metric(Hb)
    assert db is None and "K4" in fb, trial
    assert nullspace_dim(Hb) == 0, trial
    ok += 1
print(f"{ok}/{TRIALS} trials: pure-gauge w  => metric d = e^(-2 chi) exactly,")
print("real spectrum, despite arbitrary REAL gauge fluxes; one quantum of")
print("imaginary flux through any cycle => K4 fails, diagonal solution")
print("space dimension 0.")

# ---------------------------------------------------------------- B
print()
print("=" * 72)
print("B. Hatano-Nelson: ring (flux) vs open chain (pure gauge)")
print("=" * 72)


def hn(N, w, pbc, t=1.0):
    H = np.zeros((N, N), dtype=complex)
    for i in range(N - 1):
        H[i, i + 1] = t * np.exp(w)
        H[i + 1, i] = t * np.exp(-w)
    if pbc:
        H[N - 1, 0] = t * np.exp(w)
        H[0, N - 1] = t * np.exp(-w)
    return H


N, w = 12, 0.3
Hp = hn(N, w, pbc=True)
Er = eig(Hp, right=False)
print(f"ring N={N}, w={w}: imaginary flux = N w = {N * w:.1f}")
print(f"  PBC spectrum: max|Im E| = {np.abs(Er.imag).max():.4f} "
      f"(theory 2 sinh w = {2 * np.sinh(w):.4f}) -- a complex loop")
print("  (spectral winding, the skin-effect invariant): broken "
      "antilinearity, no closed")
print(f"  process; diagonal-metric solution space dim = "
      f"{nullspace_dim(Hp)}")
Ho = hn(N, w, pbc=False)
d, fails = diagonal_metric(Ho)
assert d is not None
print(f"chain N={N} (tree, flux-free): fixed beables EXIST:")
print(f"  d_i / e^(2wi) constant: "
      f"{np.allclose((d / np.exp(2 * w * np.arange(N))) / d[0], 1)}")
isreal, Eo = real_spectrum(Ho)
Eherm = 2 * np.cos(np.pi * np.arange(1, N + 1) / (N + 1))
print(f"  OBC spectrum real: {isreal}; equals Hermitian chain spectrum: "
      f"{np.allclose(np.sort(Eo.real), np.sort(Eherm), atol=1e-10)}")
rho = np.diag(np.sqrt(d))
U = expm(-1j * Ho * 1.3)
G = np.abs(rho @ U @ np.linalg.inv(rho)) ** 2
G2 = np.abs(rho @ expm(-1j * Ho * 2.6) @ np.linalg.inv(rho)) ** 2
print(f"  Gamma doubly stochastic err "
      f"{max(abs(G.sum(0) - 1).max(), abs(G.sum(1) - 1).max()):.2e}; "
      f"indivisibility {np.linalg.norm(G2 - G @ G):.3f}")
# skin eigenvectors = gauge factor times Hermitian eigenvectors
h = rho @ Ho @ np.linalg.inv(rho)
Eo_, V_ = eig(Ho)
hs = 0.5 * (h + h.conj().T)
Eh_, Vh_ = np.linalg.eigh(hs)
mx = 0.0
for k in range(N):
    m = np.argmin(np.abs(Eh_ - Eo_[k].real))
    pred = np.exp(-w * np.arange(N)) * Vh_[:, m]
    pred /= np.linalg.norm(pred)
    psi = V_[:, k] / np.linalg.norm(V_[:, k])
    psi *= np.exp(-1j * np.angle(psi[np.argmax(np.abs(psi))]))
    pred *= np.sign(pred[np.argmax(np.abs(psi))])
    mx = max(mx, min(np.linalg.norm(psi - pred), np.linalg.norm(psi + pred)))
print(f"  skin eigenvectors = e^(-wi) x Hermitian eigenvectors: "
      f"max deviation {mx:.2e}")
print("  metric growth (the finite-N price):")
for Nn in (8, 16, 24, 32):
    dd, _ = diagonal_metric(hn(Nn, w, pbc=False))
    print(f"    N={Nn:>3}: cond(eta) = {dd.max() / dd.min():.3e}   "
          f"(theory e^(2w(N-1)) = {np.exp(2 * w * (Nn - 1)):.3e})")

# ---------------------------------------------------------------- C
print()
print("=" * 72)
print("C. Classical dictionary: imaginary flux = cycle affinity = NESS "
      "current")
print("=" * 72)


def ring_current(wlinks):
    Nc = len(wlinks)
    H = np.zeros((Nc, Nc), dtype=complex)
    for i in range(Nc):
        j = (i + 1) % Nc
        H[i, j] = np.exp(wlinks[i])
        H[j, i] = np.exp(-wlinks[i])
    q = np.abs(H).T                       # q[i, j] = rate i -> j = |H_ji|
    L = q.T - np.diag(q.sum(axis=1))      # column-source generator
    pi = null_space(L)[:, 0].real
    pi = np.abs(pi) / np.abs(pi).sum()
    i, j = 0, 1
    return pi[i] * q[i, j] - pi[j] * q[j, i]


w0 = rng.normal(0, 0.4, 8)
w_pure = w0 - w0.mean()                   # zero total flux (pure gauge)
print(f"ring of 8 random links, zero imaginary flux:  "
      f"J = {ring_current(w_pure):+.2e}  (reversible, Kolmogorov holds)")
for f in (0.4, 0.8, 1.6):
    print(f"same ring, total imaginary flux {f:+.1f}:          "
          f"J = {ring_current(w_pure + f / 8):+.4f}")
print("=> steady-state cycle current is nonzero exactly when the")
print("   imaginary flux is: the skin effect is the quantum image of a")
print("   detailed-balance-violating (irreversible) classical cycle.")

# ---------------------------------------------------------------- D
print()
print("=" * 72)
print("D. Below the antilinear transition: obstruction is quantitative")
print("=" * 72)
print("triangle diag(1,2,3) + gauge ring t=0.45, uniform link field w:")
print(f"{'w':>6} {'flux':>6} {'real spec':>10} {'diag dim':>9} "
      f"{'rho offdiag frac':>17}")
for wl in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5):
    H = np.diag([1.0, 2.0, 3.0]).astype(complex)
    for (i, j) in ((0, 1), (1, 2), (2, 0)):
        H[i, j] = 0.45 * np.exp(wl)
        H[j, i] = 0.45 * np.exp(-wl)
    isreal, _ = real_spectrum(H)
    ndim = nullspace_dim(H)
    E, V = eig(H)
    Vn = V / np.linalg.norm(V, axis=0, keepdims=True)
    eta = np.linalg.inv(Vn @ Vn.conj().T)
    eta = 0.5 * (eta + eta.conj().T)
    ww, vv = np.linalg.eigh(eta)
    rho = (vv * np.sqrt(np.abs(ww))) @ vv.conj().T
    off = rho - np.diag(np.diag(rho))
    frac = np.linalg.norm(off) / np.linalg.norm(rho)
    print(f"{wl:>6.1f} {3 * wl:>6.1f} {str(isreal):>10} {ndim:>9} "
          f"{frac:>17.4f}")
print("=> the binary criterion (diag dim 1 -> 0) trips at any nonzero")
print("   flux, while the beable rotation grows continuously with it.")

# ---------------------------------------------------------------- figure
print()
print("writing paper/figs/fig_skin.pdf ...")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.size": 9, "axes.labelsize": 9, "legend.fontsize": 7.5,
    "xtick.labelsize": 8, "ytick.labelsize": 8,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.25, "grid.linewidth": 0.5,
    "lines.linewidth": 1.4, "savefig.bbox": "tight",
    "font.family": "serif", "mathtext.fontset": "cm",
    "legend.frameon": False,
})
BLUE, VERM, GREEN, GRAY = "#0072B2", "#D55E00", "#009E73", "#666666"

fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.5))
fig.subplots_adjust(wspace=0.32)
ax = axes[0]
Nf = 40
for wv, col, lab in ((0.4, VERM, "$w=0.4$"), (0.2, BLUE, "$w=0.2$")):
    Ec = eig(hn(Nf, wv, pbc=True), right=False)
    idx = np.argsort(np.angle(Ec))
    ax.plot(Ec.real[idx], Ec.imag[idx], "-", color=col, label=f"PBC, {lab}")
E0 = eig(hn(Nf, 0.0, pbc=True), right=False)
ax.plot(E0.real, E0.imag, "|", color=GRAY, ms=7, label="PBC, $w=0$")
Eob = eig(hn(Nf, 0.4, pbc=False), right=False)
ax.plot(Eob.real, Eob.imag, "o", ms=3, mfc="none", mec="k", mew=0.7,
        label="OBC, $w=0.4$")
ax.set_xlabel(r"$\mathrm{Re}\,E$")
ax.set_ylabel(r"$\mathrm{Im}\,E$")
ax.legend(loc="upper right", fontsize=6.6)
ax.text(0.02, 1.02, "Hatano–Nelson spectra (PBC vs. OBC)",
        transform=ax.transAxes, fontsize=8.5)
ax = axes[1]
Nsk, wsk = 40, 0.15
Hsk = hn(Nsk, wsk, pbc=False)
Esk, Vsk = eig(Hsk)
sites = np.arange(Nsk)
for k, col in zip(np.argsort(Esk.real)[[3, 19, 36]], (BLUE, VERM, GREEN)):
    psi = np.abs(Vsk[:, k]) / np.linalg.norm(Vsk[:, k])
    ax.semilogy(sites, psi, color=col, lw=1.1)
env = np.exp(-wsk * sites)
env *= 0.55 / env[0]
ax.semilogy(sites, env, "--", color="k", lw=1.0,
            label=r"gauge factor $e^{-w i}$")
ax.set_xlabel("site $i$")
ax.set_ylabel(r"$|\psi_k(i)|$")
ax.set_ylim(1e-4, 1)
ax.legend(loc="upper right")
ax.text(0.02, 1.02, "OBC skin modes, $w=0.15$",
        transform=ax.transAxes, fontsize=8.5)
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "..", "paper", "figs")
os.makedirs(figdir, exist_ok=True)
fig.savefig(os.path.join(figdir, "fig_skin.pdf"))
plt.close(fig)
print("done.")
