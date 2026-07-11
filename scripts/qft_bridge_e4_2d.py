"""
E4-2D: the dimensional-reversal experiment for classical ghost vacuum
decay (QFT bridge; see notes.md 2026-07-11).

The orbit-quotiented (reduced) measure of ghost vacuum decay scales as
int dE E^{3d-6}: UV-CONVERGENT in d=1 spatial dimension, exactly
MARGINAL (log) in d=2, power-divergent in d=3. Our 1+1d lattice
experiment (E4) found the classical zero-point cascade rate is
UV-suppressed at large cutoff -- consistent with d=1 convergence.

PRE-REGISTERED PREDICTION: repeating the identical experiment in
2+1d, the suppression should DISAPPEAR -- the rate should be flat to
logarithmically GROWING with the cutoff (d=2 is the marginal
dimension of the reduced measure). Observing this reversal would be
a dynamical verification of the dimension ladder; its absence would
mean the classical cascade does not track the golden-rule channel
counting.

Method (identical machinery in d=1 and d=2): normal field phi and
ghost field chi on a periodic lattice of FIXED physical size, coupling
2*lam*phi^2*chi^2 in the equations of motion; vacuum-mimic initial
data (zero-point amplitudes 1/sqrt(2 w_k), random phases); absolute
energy-transfer threshold DE (so the rising zero-point baseline
cannot mask the trend); observable t_thr = median time for the normal
sector to absorb DE, rate = 1/t_thr, versus lattice cutoff
k_max = pi*N/L at fixed L. Velocity-Verlet integrator (forces are
position-only); the conserved energy is H = E_phi - E_chi + V_int,
whose drift is monitored. lam=0 control at every size.

Run:  python scripts/qft_bridge_e4_2d.py     (~5-15 minutes)
"""

import numpy as np

MASS = 1.0
rng = np.random.default_rng(17)


def omega2_lattice(N, L, d):
    dx = L / N
    k1 = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    if d == 1:
        return MASS**2 + (2 / dx**2) * (1 - np.cos(k1 * dx))
    kx, ky = np.meshgrid(k1, k1, indexing="ij")
    return (MASS**2 + (2 / dx**2) * (2 - np.cos(kx * dx)
                                     - np.cos(ky * dx)))


def vacuum_field(N, L, d):
    """Correctly normalized zero-point data: each lattice mode carries
    energy w_k/2, i.e. <|Phi_k|^2> = N^{2d}/(2 w_k L^d) for the fft
    convention Phi = fft(f). (An earlier construction used
    N^d/(2 w_k), underpopulating fine lattices by (N/L)^{d/2} --
    the E4-1D 'suppression' must be re-examined with this fix.)"""
    w = np.sqrt(omega2_lattice(N, L, d))
    shape = (N,) if d == 1 else (N, N)
    amp_f = np.sqrt(N ** (2 * d) / (2 * w * L**d))
    amp_p = np.sqrt(N ** (2 * d) * w / (2 * L**d))
    c = (rng.standard_normal(shape) + 1j * rng.standard_normal(shape)) \
        / np.sqrt(2)
    cp = (rng.standard_normal(shape) + 1j * rng.standard_normal(shape)) \
        / np.sqrt(2)
    ifft = np.fft.ifft if d == 1 else np.fft.ifft2
    f = ifft(c * amp_f).real * np.sqrt(2)
    fp = ifft(cp * amp_p).real * np.sqrt(2)
    return f, fp


def lap(f, dx, d):
    out = (np.roll(f, 1, axis=0) + np.roll(f, -1, axis=0) - 2 * f)
    if d == 2:
        out = out + (np.roll(f, 1, axis=1) + np.roll(f, -1, axis=1)
                     - 2 * f)
    return out / dx**2


def e_sector(f, fp, dx, d):
    e = 0.5 * fp**2 + 0.5 * MASS**2 * f**2
    g = (np.roll(f, -1, axis=0) - f) / dx
    e = e + 0.5 * g**2
    if d == 2:
        g2 = (np.roll(f, -1, axis=1) - f) / dx
        e = e + 0.5 * g2**2
    return e.sum() * dx**d


def run_trial(N, L, d, lam, DE, tmax):
    dx = L / N
    wmax = np.sqrt(omega2_lattice(N, L, d).max())
    dt = min(0.05, 0.15 / wmax)   # dt*w_max <= 0.15: drift << thresholds
                                   # (0.5/wmax made the lam=0 control fire
                                   # at large N in d=2 - integrator noise)
    phi, pphi = vacuum_field(N, L, d)
    chi, pchi = vacuum_field(N, L, d)
    e0 = e_sector(phi, pphi, dx, d)
    h0 = (e0 - e_sector(chi, pchi, dx, d)
          + lam * np.sum(phi**2 * chi**2) * dx**d)

    def forces(ph, ch):
        fph = lap(ph, dx, d) - MASS**2 * ph - 2 * lam * ch**2 * ph
        fch = lap(ch, dx, d) - MASS**2 * ch + 2 * lam * ph**2 * ch
        return fph, fch

    fph, fch = forces(phi, chi)
    t, steps = 0.0, 0
    check = max(1, int(0.5 / dt))
    while t < tmax:
        pphi += 0.5 * dt * fph
        pchi += 0.5 * dt * fch
        phi += dt * pphi
        chi += dt * pchi
        fph, fch = forces(phi, chi)
        pphi += 0.5 * dt * fph
        pchi += 0.5 * dt * fch
        t += dt
        steps += 1
        if steps % check == 0:
            if e_sector(phi, pphi, dx, d) - e0 >= DE:
                h1 = (e_sector(phi, pphi, dx, d)
                      - e_sector(chi, pchi, dx, d)
                      + lam * np.sum(phi**2 * chi**2) * dx**d)
                return t, abs(h1 - h0)
    return np.inf, 0.0


def sweep(d, L, lam, DE, sizes, nens, tmax):
    print(f"--- d={d}, L={L}, lam={lam}, DE={DE}, ensemble {nens} ---")
    print(f"{'N':>5} {'k_max':>7} {'<phi^2>_0':>9} | {'median t_thr':>12} "
          f"{'rate':>8} | {'ctrl':>9} {'Hdrift':>8}")
    rates = []
    for N in sizes:
        w = np.sqrt(omega2_lattice(N, L, d))
        phibar2 = np.sum(1.0 / (2 * w)) / L**d   # physical <phi^2>
        # zero-point self-check: measured E_phi(0) vs sum(w_k)/2
        fchk, fpchk = vacuum_field(N, L, d)
        ezp = e_sector(fchk, fpchk, L / N, d) / (0.5 * np.sum(w))
        ts, hds = [], []
        for _ in range(nens):
            tt, hd = run_trial(N, L, d, lam, DE, tmax)
            ts.append(tt)
            hds.append(hd)
        tc, _ = run_trial(N, L, d, 0.0, DE, min(tmax, 150.0))
        med = np.median(ts)
        rate = 1.0 / med if np.isfinite(med) else 0.0
        rates.append(rate)
        ctrl = "no growth" if not np.isfinite(tc) else f"{tc:.0f}"
        print(f"{N:>5} {np.pi/(L/N):>7.2f} {phibar2:>9.3f} | "
              f"{med:>12.1f} {rate:>8.4f} | {ctrl:>9} "
              f"{max(hds):>8.1e}  zp={ezp:.2f}")
    return rates


print("=" * 72)
print("E4-2D: classical ghost vacuum-decay rate vs UV cutoff,")
print("       d=1 vs d=2 at fixed physical volume (identical machinery)")
print("PREDICTION: d=1 rate SUPPRESSED at large k_max (reduced measure")
print("UV-finite); d=2 rate flat-to-GROWING (marginal dimension).")
print("=" * 72)
r1 = sweep(1, 32.0, 0.25, 25.0, (8, 16, 32, 64, 128), 8, 400.0)
print()
r2 = sweep(2, 16.0, 0.10, 10.0, (8, 16, 32, 48, 64), 6, 400.0)
print()
print(f"d=1 rate trend (largest 3 N): {r1[-3]:.4f} -> {r1[-2]:.4f} -> "
      f"{r1[-1]:.4f}")
print(f"d=2 rate trend (largest 3 N): {r2[-3]:.4f} -> {r2[-2]:.4f} -> "
      f"{r2[-1]:.4f}")
print("done.")
