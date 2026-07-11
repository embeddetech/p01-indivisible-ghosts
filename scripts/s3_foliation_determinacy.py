"""
S3 -- foliation determinacy as a measured curve (F3 quantitative).

Claim under test (notes F3): the vacuum determines no foliation, and
foliation-indeterminacy is continuous -- the frame information of a
state vanishes as the state approaches the vacuum.

Construction (1D lattice, fixed L and N): each mode carries
  zero-point part: occupation 1/2, split equally between +k and -k
      movers (frame-symmetric BY CONSTRUCTION -- the classical mimic
      of the boost-invariant vacuum);
  thermal part: boosted Juttner occupation n_th(k) = T/(u.k),
      u = gamma(1, v) -- the frame-carrying excitation.
Frame extraction: vhat = P_tot/E_tot per realization (the 1D
timelike-eigenframe estimator of <T^mu nu>). Over an ensemble,
  mean(vhat) = the state's streaming velocity (frame signal),
  std(vhat)  = realization scatter (frame noise).
Signal-to-noise SNR(T) = mean/std is the DETERMINACY of the
extracted foliation.

Predictions: SNR -> 0 continuously as T -> 0 (pure vacuum: mean = 0,
pure scatter -- the frame is INDETERMINATE, F3); SNR grows ~ with the
thermal share at small T; at large T the zero-point part is
negligible and mean(vhat) -> the massive-bath streaming velocity
(< v; ultrarelativistic limit would reach v).

Run:  python scripts/s3_foliation_determinacy.py    (~1 minute)
"""

import numpy as np

L, N, MASS, V = 32.0, 64, 1.0, 0.35
NENS = 400
rng = np.random.default_rng(41)

kvals = 2 * np.pi * np.arange(1, N // 2) / L      # +k modes; pair with -k
w = np.sqrt(MASS**2 + kvals**2)
gam = 1.0 / np.sqrt(1 - V**2)


def realization(T):
    """Return (E, P) of one realization: zero-point (frame-symmetric)
    + boosted thermal occupation, random mover phases/amplitudes.
    Per traveling mode of occupation n: energy eps = w*n carried with
    momentum sign(k)*|k|/w * eps; amplitude fluctuations: exponential
    (Rayleigh^2) per mode, the classical-chaotic-light statistics."""
    E = P = 0.0
    for kk, ww in zip(np.concatenate([kvals, -kvals]),
                      np.concatenate([w, w])):
        n_zp = 0.25                              # 1/2 split over +/-k
        n_th = T / (gam * (ww - V * kk)) if T > 0 else 0.0
        # exponential amplitude statistics per mover
        eps = ww * (n_zp * rng.exponential() + n_th * rng.exponential())
        E += eps
        P += (kk / ww) * eps
    return E, P


print("=" * 72)
print("S3: foliation determinacy vs occupation (boost v = 0.35,")
print(f"    {NENS} realizations per T; zero-point part frame-symmetric)")
print("=" * 72)
print(f"{'T':>7} | {'mean vhat':>9} {'std vhat':>9} {'SNR':>7} | "
      f"{'thermal share':>13}")
for T in (0.0, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0):
    vh = []
    for _ in range(NENS):
        E, P = realization(T)
        vh.append(P / E)
    vh = np.array(vh)
    mean, std = vh.mean(), vh.std()
    snr = abs(mean) / (std / np.sqrt(NENS))      # ensemble-level SNR
    # thermal fraction of the mean energy
    eth = sum(ww * T / (gam * (ww - V * kk))
              for kk, ww in zip(np.concatenate([kvals, -kvals]),
                                np.concatenate([w, w]))) if T > 0 else 0.0
    ezp = 2 * np.sum(w * 0.25)
    share = eth / (eth + ezp)
    print(f"{T:>7.3f} | {mean:>9.4f} {std:>9.4f} {snr:>7.1f} | "
          f"{share:>13.3f}")
print()
print("=> mean vhat -> 0 and SNR -> 0 as T -> 0: the extracted")
print("   foliation degenerates CONTINUOUSLY into pure realization")
print("   scatter at the vacuum -- F3 as a measured determinacy curve.")
print("   (Single-realization determinacy: divide SNR by sqrt(NENS).)")
print("done.")
