"""
S2 -- the infinity-channel protocol: causality selects the minimal
process, quantified as a communication experiment.

Setup: 1D Schrodinger packet in V = -x^4 (explosive class: classical
time of flight to infinity FINITE) or V = -x^2 (marginal class:
time of flight DIVERGES), on x in [-L, L]. Alice sits near +L and
encodes one bit by toggling a reflecting barrier that gates the
right exit. Bob sits near -L and is DIRECTION-RESOLVED: he triggers
only on probability current J > 0 at his station -- flux entering
the interior from the left boundary, i.e. arrivals FROM INFINITY.
Two completions of the same interior dynamics:

  PERIODIC identification (+inf glued to -inf): the conservative
  "wormhole" completion of the explosion dictionary (paper 1, V5).
  ABSORBING boundaries: the minimal (Feller) sub-stochastic process.

Predictions (pre-registered):
  -x^4 + periodic:  Bob triggers at a latency t_B that SATURATES as
      L grows (the far region costs vanishing traversal time; t_B ->
      the classical round-trip integral, computed below), and t_B
      depends on Alice's bit: A WORKING CHANNEL THROUGH INFINITY
      whose latency is independent of the separation.
  -x^4 + absorbing: Bob never triggers, for either bit: the minimal
      process has NO channel -- causality is preserved by mass loss.
  -x^2 + periodic:  the channel exists but its latency GROWS with L
      (diverging time of flight): no distance-independent channel at
      or below the marginal class.
  -x^2 + absorbing: silence.

The acausality of conservative completions is thus operational: the
completion (boundary data at infinity), not the Hamiltonian, decides
whether Alice can message Bob through infinity -- and only the
explosive class delivers the distance-independent channel.

Run:  python scripts/s2_infinity_channel.py    (~5-10 minutes)
"""

import sys
import numpy as np

NGRID = 2048
X0, SIG = 3.0, 0.6          # launch: rest packet, accelerates right
JTHRESH = 1e-3


def potential(x, quartic):
    return -x**4 if quartic else -x**2


def make_run(L, quartic, periodic, bit):
    N = NGRID
    x = np.linspace(-L, L, N, endpoint=False)
    dx = x[1] - x[0]
    k = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    V = potential(x, quartic).astype(complex)
    xa = L - 2.5                              # Alice's station
    if bit:
        barrier = 3 * abs(potential(xa, quartic))
        V += barrier * np.exp(-(x - xa) ** 2 / (2 * 0.25**2))
    if not periodic:                          # absorbing (minimal)
        xc = 0.85 * L
        ramp = np.clip((np.abs(x) - xc) / (L - xc), 0, 1) ** 3
        # CAP must beat the edge speed: the marginal potential's edge
        # flux is far slower-decaying, so it needs a stronger layer
        eta0 = (0.5 if quartic else 2.5) * abs(potential(L, quartic))
        V -= 1j * eta0 * ramp
    # split-step: the kinetic factor is EXACT (no k_max stability
    # limit); dt is set by the potential phase per half-step and a
    # Trotter-accuracy cap
    vmax = np.max(np.abs(V))
    dt = min(0.3 / vmax, 2e-4)
    psi = np.exp(-(x - X0) ** 2 / (2 * SIG**2)).astype(complex)
    psi /= np.sqrt(np.sum(np.abs(psi) ** 2) * dx)
    expV = np.exp(-1j * V * dt / 2)
    expK = np.exp(-1j * (k**2 / 2) * dt)
    ib = np.argmin(np.abs(x - (-L + 3.0)))    # Bob's station
    tmax = 3.0 if quartic else 10.0
    t, tb = 0.0, np.inf
    jmax = 0.0
    check = max(1, int(0.01 / dt))
    step = 0
    while t < tmax:
        psi = expV * psi
        psi = np.fft.ifft(expK * np.fft.fft(psi))
        psi = expV * psi
        t += dt
        step += 1
        if step % check == 0:
            dpsi = (psi[ib + 1] - psi[ib - 1]) / (2 * dx)
            J = np.imag(np.conj(psi[ib]) * dpsi)
            if J > jmax:
                jmax = J
            if J > JTHRESH and not np.isfinite(tb):
                tb = t
    norm_end = np.sum(np.abs(psi) ** 2) * dx
    return tb, jmax, norm_end


def roundtrip_prediction(L_list, quartic):
    """Classical Alice->infinity->Bob time at the launch energy
    E = V(X0) (rest start): T = int_{X0}^inf dx/v + int_inf^{xB}."""
    E = potential(X0, quartic)
    def seg(a, b):
        xs = np.linspace(a, b, 200001)[1:]
        v2 = 2 * (E - potential(xs, quartic))
        v2 = np.maximum(v2, 1e-12)
        return np.trapezoid(1 / np.sqrt(v2), xs)
    out = []
    for L in L_list:
        far = 60.0                            # proxy for infinity
        t1 = seg(X0 + 1e-4, far)              # out through +inf
        t2 = seg(L - 3.0, far)                # -inf back to Bob
        out.append(t1 + t2)
    return out


print("=" * 72)
print("S2: messaging through infinity -- completion decides the channel")
print(f"    Bob = direction-resolved current at x=-L+3, J > {JTHRESH}")
print("=" * 72)

Ls = (6, 8, 10, 12)
for quartic, vlab in ((True, "V=-x^4 (explosive)"),
                      (False, "V=-x^2 (marginal)")):
    for periodic, clab in ((True, "PERIODIC (wormhole completion)"),
                           (False, "ABSORBING (minimal process)")):
        print(f"\n--- {vlab}, {clab} ---")
        print(f"{'L':>4} | {'bit=0: t_B':>10} {'Jmax':>9} | "
              f"{'bit=1: t_B':>10} {'Jmax':>9} | {'norm_end':>8}")
        for L in Ls:
            tb0, j0, n0 = make_run(L, quartic, periodic, 0)
            tb1, j1, n1 = make_run(L, quartic, periodic, 1)
            f0 = f"{tb0:>10.3f}" if np.isfinite(tb0) else f"{'--':>10}"
            f1 = f"{tb1:>10.3f}" if np.isfinite(tb1) else f"{'--':>10}"
            print(f"{L:>4} | {f0} {j0:>9.5f} | {f1} {j1:>9.5f} | "
                  f"{n0:>8.3f}")
            sys.stdout.flush()
        if quartic and periodic:
            pred = roundtrip_prediction(Ls, True)
            print("      classical round-trip prediction (bit=0): "
                  + ", ".join(f"{p:.3f}" for p in pred))

print()
print("verdict key: explosive+wormhole = distance-independent bit")
print("channel through infinity (t_B saturates, bit shifts t_B);")
print("minimal = silence (causality by mass loss); marginal = latency")
print("grows with L (no distance-independent channel).")
print("done.")
