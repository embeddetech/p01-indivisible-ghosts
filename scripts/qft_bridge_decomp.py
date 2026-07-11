"""
Exponent decomposition for the E4-2D dimensional reversal
(see notes.md 2026-07-11, qft_bridge_e4_2d.py).

The corrected reversal experiment found the d=2 classical ghost decay
rate growing ~ k_max^2.7 with the UV cutoff, steeper than the
marginal-log predicted by pure channel counting. Hypothesis:

    rate  ~  lam^2 <phi^2><chi^2>  x  (channel factor)
              [source: ~k_max^2 in d=2]   [log at d=2; const at d=1]

so 2.7 ~ 2 (growing zero-point source) + log. This script separates
the factors:

RUN 1 (fix the source, free the channels). Zero-point data TRUNCATED
to |k| <= K_C (fixed physical support, N-independent source; the
high-k lattice modes are empty and available only as FINAL states).
Sweep N. Prediction: d=2 rate grows ~log(k_max) (slow, decelerating
in a log-log plot); d=1 rate saturates. This isolates the channel
factor and answers the "hotter start" objection to the reversal.

RUN 2 (fix the channels, scale the source). Full-shape vacuum data
multiplied by amplitude a at fixed N. Prediction: rate ~ a^4 (two
powers of variance per sector through lam^2 phi^2 chi^2).

Cross-check: 2 (from Run 2, since variance ~ a^2 and zero-point
variance ~ k_max in d=2) + log (Run 1) should reconstruct the ~2.7
of the full experiment.

Run:  python scripts/qft_bridge_decomp.py     (~15-30 minutes)
"""

import numpy as np

MASS = 1.0
rng = np.random.default_rng(29)


def omega2_lattice(N, L, d):
    dx = L / N
    k1 = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    if d == 1:
        return MASS**2 + (2 / dx**2) * (1 - np.cos(k1 * dx))
    kx, ky = np.meshgrid(k1, k1, indexing="ij")
    return (MASS**2 + (2 / dx**2) * (2 - np.cos(kx * dx)
                                     - np.cos(ky * dx)))


def kmag(N, L, d):
    k1 = 2 * np.pi * np.fft.fftfreq(N, d=L / N)
    if d == 1:
        return np.abs(k1)
    kx, ky = np.meshgrid(k1, k1, indexing="ij")
    return np.sqrt(kx**2 + ky**2)


def vacuum_field(N, L, d, kc=None, scale=1.0):
    """Correctly normalized zero-point data (mode energy w_k/2),
    optionally truncated to |k|<=kc, optionally amplitude-scaled."""
    w = np.sqrt(omega2_lattice(N, L, d))
    shape = (N,) if d == 1 else (N, N)
    amp_f = np.sqrt(N ** (2 * d) / (2 * w * L**d)) * scale
    amp_p = np.sqrt(N ** (2 * d) * w / (2 * L**d)) * scale
    if kc is not None:
        mask = kmag(N, L, d) <= kc
        amp_f = amp_f * mask
        amp_p = amp_p * mask
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


def run_trial(N, L, d, lam, DE, tmax, kc=None, scale=1.0):
    dx = L / N
    wmax = np.sqrt(omega2_lattice(N, L, d).max())
    dt = min(0.05, 0.15 / wmax)
    phi, pphi = vacuum_field(N, L, d, kc, scale)
    chi, pchi = vacuum_field(N, L, d, kc, scale)
    e0 = e_sector(phi, pphi, dx, d)

    def forces(ph, ch):
        return (lap(ph, dx, d) - MASS**2 * ph - 2 * lam * ch**2 * ph,
                lap(ch, dx, d) - MASS**2 * ch + 2 * lam * ph**2 * ch)

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
                return t
    return np.inf


# ------------------------------------------------------------- RUN 1
print("=" * 72)
print("RUN 1: fixed truncated source, channel sweep")
print("  d=2: K_C=2.0, L=16, lam=0.35, DE=6   (predict ~log growth)")
print("  d=1: K_C=1.2, L=32, lam=0.6,  DE=10  (predict saturation)")
print("=" * 72)


def sweep_channels(d, L, lam, DE, kc, sizes, nens, tmax):
    print(f"--- d={d} ---")
    print(f"{'N':>5} {'k_max':>7} {'<phi^2>_0':>9} | {'median t':>9} "
          f"{'rate':>8} | {'ctrl':>9}")
    rates, kmaxs = [], []
    for N in sizes:
        w = np.sqrt(omega2_lattice(N, L, d))
        msk = kmag(N, L, d) <= kc
        phibar2 = np.sum(msk / (2 * w)) / L**d
        ts = [run_trial(N, L, d, lam, DE, tmax, kc) for _ in range(nens)]
        tc = run_trial(N, L, d, 0.0, DE, min(tmax, 150.0), kc)
        med = np.median(ts)
        rate = 1.0 / med if np.isfinite(med) else 0.0
        rates.append(rate)
        kmaxs.append(np.pi / (L / N))
        ctrl = "no growth" if not np.isfinite(tc) else f"{tc:.0f}"
        print(f"{N:>5} {kmaxs[-1]:>7.2f} {phibar2:>9.3f} | {med:>9.1f} "
              f"{rate:>8.4f} | {ctrl:>9}")
    good = [(k, r) for k, r in zip(kmaxs, rates) if r > 0]
    if len(good) >= 3:
        kk = np.array([g[0] for g in good])
        rr = np.array([g[1] for g in good])
        p_pow = np.polyfit(np.log(kk), np.log(rr), 1)[0]
        r_log = np.corrcoef(np.log(kk), rr)[0, 1] ** 2
        print(f"  power-law exponent {p_pow:+.2f}; "
              f"R^2 of rate ~ log(k_max): {r_log:.3f}")
    return rates


r1_d2 = sweep_channels(2, 16.0, 0.35, 6.0, 2.0, (16, 32, 48, 64),
                       6, 500.0)
r1_d1 = sweep_channels(1, 32.0, 0.6, 10.0, 1.2, (16, 32, 64, 128),
                       8, 500.0)

# ------------------------------------------------------------- RUN 2
print()
print("=" * 72)
print("RUN 2: fixed lattice, amplitude-scaled full-shape source")
print("  rate(a) with vacuum data x a; predict rate ~ a^4")
print("=" * 72)


def sweep_amplitude(d, L, N, lam, DE, avals, nens, tmax):
    print(f"--- d={d}, N={N} ---")
    print(f"{'a':>6} | {'median t':>9} {'rate':>8}")
    rates = []
    for a in avals:
        ts = [run_trial(N, L, d, lam, DE, tmax, None, a)
              for _ in range(nens)]
        med = np.median(ts)
        rate = 1.0 / med if np.isfinite(med) else 0.0
        rates.append(rate)
        print(f"{a:>6.2f} | {med:>9.1f} {rate:>8.4f}")
    good = [(a, r) for a, r in zip(avals, rates) if r > 0]
    if len(good) >= 3:
        aa = np.array([g[0] for g in good])
        rr = np.array([g[1] for g in good])
        sl = np.polyfit(np.log(aa), np.log(rr), 1)[0]
        print(f"  fitted exponent d(log rate)/d(log a) = {sl:+.2f} "
              f"(predict +4)")
    return rates


r2_d2 = sweep_amplitude(2, 16.0, 32, 0.1, 10.0,
                        (0.7, 1.0, 1.4, 2.0), 6, 500.0)
r2_d1 = sweep_amplitude(1, 32.0, 64, 0.25, 25.0,
                        (0.7, 1.0, 1.4, 2.0), 8, 500.0)

print()
print("Reconstruction check: full-experiment d=2 exponent ~2.7 should")
print("decompose as ~2 from the source (zero-point variance ~ k_max in")
print("d=2, entering squared per Run 2) plus the slow channel factor")
print("(Run 1). d=1: channel factor saturates; full growth was mild.")
print("done.")
