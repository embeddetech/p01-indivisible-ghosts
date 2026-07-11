"""
Topological classification of the fixed-beable obstruction
(continuation of skin_effect_beables.py / paper Sec. 3.1).

COROLLARY (classification). For gauge-form couplings on a graph/lattice,
the fixed-beable obstruction is the class of the imaginary gauge field in
the first cohomology H^1(G, R): the imaginary FIELD STRENGTH must vanish
through every contractible cycle (no imaginary magnetic flux) and the
imaginary HOLONOMY through every non-contractible one (no winding). On a
d-torus this is an R^d of independent windings -- matching the
multi-directional classification of skin effects -- PLUS the pointwise
plaquette condition, which band-language winding misses.

FINER THAN NET WINDING (Z2-type test). Two Hatano-Nelson chains with
OPPOSITE imaginary fields (net winding zero -- the doubled/Kramers
structure of the Z2 skin effect) coupled by rungs: each chain alone is
pure gauge (open boundaries), but inter-chain cycles carry circulation
2w != 0: the beable obstruction detects the doubled skin structure that
net winding cannot.

Verifications:
 T1  2D torus (3 x 4): fixed-beable iff BOTH windings vanish; either
     winding alone obstructs; a single contractible plaquette of
     imaginary flux ALSO obstructs.
 T2  Cylinder (open in x, periodic in y): x-winding is gauge-removable
     (no x-cycle exists), y-winding obstructs.
 T3  Z2 ladder: uncoupled -> two independent fixed-beable metrics
     (solution space dim 2, weights e^{+2wi} and e^{-2wi}); rung-coupled
     -> dim 0 despite zero net winding.

Run:  python skin_topology_beables.py     (seconds)
"""

import numpy as np

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(7)
TOL = 1e-9


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


def lattice_H(Lx, Ly, open_x, open_y, wind_x=0.0, wind_y=0.0,
              plaquette=0.0, chi_scale=0.7):
    """Gauge-form couplings on an Lx x Ly lattice. Pure-gauge chi
    background + optional windings (uniform w on x-/y-links) + optional
    imaginary flux through the single plaquette at (0,0)."""
    n = Lx * Ly
    idx = lambda x, y: x * Ly + y
    chi = rng.normal(0, chi_scale, n)
    H = np.diag(rng.normal(0, 1, n)).astype(complex)

    def add_edge(i, j, wextra):
        t = rng.uniform(0.6, 1.4)
        phi = rng.uniform(-np.pi, np.pi)          # real gauge: arbitrary
        w = chi[i] - chi[j] + wextra
        H[i, j] = t * np.exp(1j * phi + w)
        H[j, i] = t * np.exp(-1j * phi - w)

    for x in range(Lx):
        for y in range(Ly):
            i = idx(x, y)
            if x + 1 < Lx or not open_x:
                j = idx((x + 1) % Lx, y)
                wex = wind_x / Lx
                if plaquette and x == 0 and y == 0:
                    wex += plaquette          # one link of plaquette(0,0)
                add_edge(i, j, wex)
            if y + 1 < Ly or not open_y:
                j = idx(x, (y + 1) % Ly)
                add_edge(i, j, wind_y / Ly)
    return H


print("=" * 72)
print("T1. 3 x 4 torus: obstruction = (windings in H^1) + plaquette flux")
print("=" * 72)
print(f"{'wind_x':>7} {'wind_y':>7} {'plaq':>6} {'diag-metric dim':>16}")
for wx, wy, pl in ((0, 0, 0), (0.8, 0, 0), (0, 0.8, 0), (0.8, 0.8, 0),
                   (0, 0, 0.5)):
    H = lattice_H(3, 4, open_x=False, open_y=False,
                  wind_x=wx, wind_y=wy, plaquette=pl)
    print(f"{wx:>7.1f} {wy:>7.1f} {pl:>6.1f} {nullspace_dim(H):>16}")
print("=> fixed-beable iff every entry vanishes: both non-contractible")
print("   windings AND the contractible imaginary magnetic flux obstruct.")

print()
print("=" * 72)
print("T2. Cylinder (open x, periodic y)")
print("=" * 72)
print(f"{'wind_x':>7} {'wind_y':>7} {'diag-metric dim':>16}")
for wx, wy in ((0.8, 0.0), (0.0, 0.8), (0.8, 0.8)):
    H = lattice_H(3, 4, open_x=True, open_y=False, wind_x=wx, wind_y=wy)
    print(f"{wx:>7.1f} {wy:>7.1f} {nullspace_dim(H):>16}")
print("=> 'winding' along the open direction is pure gauge (no cycle");
print("   exists to support it); the periodic direction obstructs: the")
print("   obstruction lives exactly in H^1 of the actual geometry.")

print()
print("=" * 72)
print("T3. Z2-type ladder: two opposite HN chains, net winding zero")
print("=" * 72)


def z2_ladder(N, w, rung):
    H = np.zeros((2 * N, 2 * N), dtype=complex)
    up = lambda i: i
    dn = lambda i: N + i
    for i in range(N - 1):
        H[up(i), up(i + 1)] = np.exp(w)      # up chain: field +w
        H[up(i + 1), up(i)] = np.exp(-w)
        H[dn(i), dn(i + 1)] = np.exp(-w)     # down chain: field -w
        H[dn(i + 1), dn(i)] = np.exp(w)
    for i in range(N):
        H[up(i), dn(i)] = rung               # reciprocal rungs
        H[dn(i), up(i)] = rung
    return H


for rung in (0.0, 0.3):
    H = z2_ladder(8, 0.25, rung)
    E = np.linalg.eigvals(H)
    print(f"rung = {rung:.1f}: diag-metric dim = {nullspace_dim(H)}, "
          f"max|Im E| = {np.abs(E.imag).max():.4f}")
print("=> uncoupled: TWO independent fixed-beable metrics (e^{+2wi} and")
print("   e^{-2wi} per chain). Any rung coupling creates inter-chain")
print("   cycles of circulation 2w: obstructed (dim 0) although the NET")
print("   winding of the doubled system is zero -- the beable obstruction")
print("   detects the Z2/doubled skin structure that net winding misses.")
