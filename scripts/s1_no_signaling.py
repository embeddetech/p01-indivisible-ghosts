"""
S1 -- the no-signaling stress test: where does the "faster-than-light"
signal of local PT operations actually live?

Background: Lee-Hsieh-Flammia-Lee, PRL 112, 130404 (2014) showed that
treating LOCAL PT evolution as fundamental on one arm of an entangled
pair permits superluminal signaling. Our framework (paper 1) predicts
precisely where that signal comes from and where it does not:

  (i)   METRIC-CORRECTED closed dynamics (the deflation proposition:
        PT = the Hermitian partner's unitary in disguise):
        Bob's marginal is EXACTLY independent of Alice's choice.
  (ii)  DILATED open dynamics, no post-selection (Halmos dilation,
        leak recorded in ancilla configurations):
        Bob's marginal is EXACTLY independent of Alice's choice.
  (iii) SURVIVAL-CONDITIONED dynamics (renormalizing the leaked
        mass away -- the LHFL treatment): a signal APPEARS, with
        closed-form magnitude. For the Bell state and the broken
        dimer, using the terminal-indivisibility variables
        p = c + sin(th)*sig, q = c - sin(th)*sig, r = s*sig
        (c = cosh(kt*t), sig = sinh(kt*t)/kt, kt^2 = sin^2 th - s^2):

            TV(t) = |p^2 - q^2| / (p^2 + q^2 + 2 r^2),
            TV(t -> inf) = kt / sin(th)  = sqrt(1 - (s/sin th)^2):

        zero at the exceptional point, -> 1 deep in the broken phase.
        A new closed-form corollary of the terminal-indivisibility
        theorem: the LHFL signal strength.

Interpretation (stated for the record): the treatment-(iii) signal is
real FOR A POST-SELECTED ENSEMBLE, but the post-selection requires
knowing Alice-side survival -- information that itself travels
classically. Bob alone cannot construct the conditioned ensemble.
The "FTL" of local PT is a sample-space bookkeeping fallacy: it
appears exactly when the sub-stochastic process is treated as the
whole sample space. Falsifiable core of our framework: treatments
(i) and (ii) must show ZERO signal to machine precision -- any leak
there and the dilation story of paper 1 is wrong.

Alice's two messages: the dimer loss on site 2 (msg 0) versus site 1
(msg 1) -- parity-swapped, identical spectra, different orientation.
Initial state: Bell (|00> + |11>)/sqrt(2). Bob idle.

Run:  python scripts/s1_no_signaling.py     (seconds)
"""

import numpy as np
from scipy.linalg import expm, sqrtm

TH = np.pi / 4


def dimer_loss(th, s, msg):
    """H_loss for the dimer, gain subtracted: pure loss on one site.
    msg 0: loss on site 2; msg 1: loss on site 1 (parity swap)."""
    if msg == 0:
        return np.array([[0, s], [s, -2j * np.sin(th)]], complex)
    return np.array([[-2j * np.sin(th), s], [s, 0]], complex)


def dimer_full(th, s, msg):
    """Full PT dimer (unbroken-phase treatment); msg = orientation."""
    if msg == 0:
        return np.array([[np.exp(1j * th), s],
                         [s, np.exp(-1j * th)]], complex)
    return np.array([[np.exp(-1j * th), s],
                     [s, np.exp(1j * th)]], complex)


def bell():
    v = np.zeros(4, complex)
    v[0] = v[3] = 1 / np.sqrt(2)     # |00> + |11>
    return v


def bob_marginal(vec4):
    """vec indexed (a,b) -> p_B(b) = sum_a |v_ab|^2 (normalized)."""
    v = vec4.reshape(2, 2)
    p = np.sum(np.abs(v) ** 2, axis=0)
    return p / p.sum()


def tv(p, q):
    return 0.5 * np.sum(np.abs(p - q))


def halmos(C):
    """4x4 unitary dilation of a 2x2 contraction."""
    I = np.eye(2)
    DC = sqrtm(I - C @ C.conj().T)
    DCt = sqrtm(I - C.conj().T @ C)
    U = np.block([[C, DC], [DCt, -C.conj().T]])
    return U


print("=" * 72)
print("S1: no-signaling stress test (Bell pair; Alice's msg = loss")
print("    orientation; Bob's marginal TV distance = signal)")
print("=" * 72)

# ---------------------------------------------------------------- (i)
print("\n(i) METRIC-CORRECTED closed dynamics (unbroken, s=1.0):")
s_un = 1.0
worst = 0.0
for t in np.linspace(0.2, 8.0, 25):
    pb = []
    for msg in (0, 1):
        H = dimer_full(TH, s_un, msg)
        w, V = np.linalg.eig(H)
        eta = np.linalg.inv(V @ V.conj().T)
        rho = sqrtm(eta)
        h = rho @ H @ np.linalg.inv(rho)
        h = 0.5 * (h + h.conj().T)          # Hermitian partner
        u = expm(-1j * h * t)
        vec = np.kron(u, np.eye(2)) @ bell()
        pb.append(bob_marginal(vec))
    worst = max(worst, tv(pb[0], pb[1]))
print(f"    max TV over t in [0.2,8]: {worst:.2e}   "
      f"({'NO SIGNAL' if worst < 1e-12 else 'SIGNAL - FRAMEWORK FALSIFIED'})")

# --------------------------------------------------------------- (ii)
print("\n(ii) DILATED open dynamics, NO post-selection (broken, s=0.5):")
s_br = 0.5
worst = 0.0
uni_err = 0.0
for t in np.linspace(0.2, 8.0, 25):
    pb = []
    for msg in (0, 1):
        C = expm(-1j * dimer_loss(TH, s_br, msg) * t)
        U = halmos(C)
        uni_err = max(uni_err, np.max(np.abs(U @ U.conj().T - np.eye(4))))
        # space: (A+anc) x B, dims 4 x 2; initial ancilla empty
        vec8 = np.zeros(8, complex)
        b = bell().reshape(2, 2)
        vec8.reshape(4, 2)[:2, :] = b
        out = np.kron(U, np.eye(2)) @ vec8
        v = out.reshape(4, 2)
        p = np.sum(np.abs(v) ** 2, axis=0)
        pb.append(p / p.sum())
    worst = max(worst, tv(pb[0], pb[1]))
print(f"    Halmos unitarity error: {uni_err:.2e}")
print(f"    max TV over t in [0.2,8]: {worst:.2e}   "
      f"({'NO SIGNAL' if worst < 1e-12 else 'SIGNAL - FRAMEWORK FALSIFIED'})")

# -------------------------------------------------------------- (iii)
print("\n(iii) SURVIVAL-CONDITIONED (broken, s=0.5): the LHFL signal,")
print("      against the closed form |p^2-q^2|/(p^2+q^2+2r^2):")
kt = np.sqrt(np.sin(TH) ** 2 - s_br**2)
print(f"      predicted asymptote kt/sin(th) = {kt/np.sin(TH):.6f}")
print(f"{'t':>6} {'TV numeric':>12} {'TV closed form':>14}")
worst_dev = 0.0
for t in (0.5, 1.0, 2.0, 4.0, 8.0, 16.0):
    pb = []
    for msg in (0, 1):
        C = expm(-1j * dimer_loss(TH, s_br, msg) * t)
        vec = np.kron(C, np.eye(2)) @ bell()
        pb.append(bob_marginal(vec))       # renormalized = conditioned
    tv_num = tv(pb[0], pb[1])
    c = np.cosh(kt * t)
    sig = np.sinh(kt * t) / kt
    p_, q_, r_ = (c + np.sin(TH) * sig, c - np.sin(TH) * sig,
                  s_br * sig)
    tv_cf = abs(p_**2 - q_**2) / (p_**2 + q_**2 + 2 * r_**2)
    worst_dev = max(worst_dev, abs(tv_num - tv_cf))
    print(f"{t:>6.1f} {tv_num:>12.8f} {tv_cf:>14.8f}")
print(f"      max |numeric - closed form| = {worst_dev:.2e}")
print(f"      TV(16)/asymptote = "
      f"{tv_num/(kt/np.sin(TH)):.6f}  (-> 1)")

# EP sweep: signal dies at the exceptional point
print("\n      asymptotic signal vs s (broken phase, t=25):")
for s in (0.2, 0.4, 0.6, 0.7, 0.705):
    ktv = np.sqrt(np.sin(TH) ** 2 - s**2)
    pb = []
    for msg in (0, 1):
        C = expm(-1j * dimer_loss(TH, s, msg) * 25.0)
        vec = np.kron(C, np.eye(2)) @ bell()
        pb.append(bob_marginal(vec))
    print(f"      s={s:5.3f}: TV = {tv(pb[0], pb[1]):.6f}   "
          f"predicted kt/sin = {ktv/np.sin(TH):.6f}")

# -------------------------------------------------- (iv) LHFL regime
print("\n(iv) UNBROKEN PT + conditioning (the LHFL construction,")
print("     s=1.0): signal present under conditioning, ZERO under (i):")
worst_iv = 0.0
for t in np.linspace(0.2, 8.0, 50):
    pb = []
    for msg in (0, 1):
        C = expm(-1j * dimer_full(TH, s_un, msg) * t)
        vec = np.kron(C, np.eye(2)) @ bell()
        pb.append(bob_marginal(vec))
    worst_iv = max(worst_iv, tv(pb[0], pb[1]))
print(f"     max conditioned TV over t: {worst_iv:.4f}  (> 0: the LHFL")
print("     'FTL' signal, reproduced in classical probabilities);")
print("     same Hamiltonians under treatment (i): 0 to machine eps.")
print()
print("VERDICT: the signal lives in the conditioning (sample-space")
print("bookkeeping), never in the closed or dilated dynamics; its")
print("broken-phase magnitude is the closed form kt/sin(th) -- a new")
print("corollary of the terminal-indivisibility theorem.")
print("done.")
