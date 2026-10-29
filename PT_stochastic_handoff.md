# Handoff Briefing: PT-Symmetric (Mannheim) meets Indivisible Stochastic Processes (Barandes)

**Purpose of this document.** This is a self-contained briefing for a fresh Claude Code
session. It captures a research thread exploring whether Philip Mannheim's antilinear /
PT-symmetric approach to unitarity has any real connection to Jacob Barandes'
"indivisible stochastic process" reconstruction of quantum mechanics. It includes the
motivating question, the reasoning, a **working numerical experiment (code + results)**,
the conclusions reached, and a ranked list of concrete next calculations. You should be
able to act on the "Next steps" section directly.

Assume no prior context. Everything needed is below.

---

## 1. The two research programs

### 1.1 Mannheim — conformal gravity, PT symmetry, antilinearity
Philip Mannheim (UConn) advocates **conformal (Weyl) gravity** as an alternative to
Einstein gravity — a fourth-order-derivative theory whose action is built from the
square of the conformal Weyl tensor. The toy model for its higher-derivative structure
is the **Pais–Uhlenbeck (PU) oscillator**. Such theories naively look non-unitary
(Ostrogradski instability / ghost states / spectrum unbounded below).

Mannheim's resolution (much of it with Carl Bender): the Hamiltonian is **not Hermitian**
but **PT-symmetric**, and the correct organizing principle for quantum theory is
**antilinearity (time-reversal invariance), not Hermiticity**. Key facts he leans on:
- **Antilinear-symmetry theorem:** if a Hamiltonian commutes with an antilinear operator
  (e.g. PT), its eigenvalues are either real or come in complex-conjugate pairs.
- **Unbroken PT phase:** eigenvalues real ⇒ evolution by pure phases ⇒ effectively
  unitary in a **modified inner product** (the C-operator / PT metric).
- **Broken PT phase:** complex-conjugate eigenvalue pairs ⇒ exponentially growing/decaying
  ("runaway") modes. This is the "exponential balancing": a decaying mode paired with a
  growing (time-reversed) partner in a biorthogonal inner product.
- Representative paper: *"Antilinearity Rather than Hermiticity as a Guiding Principle for
  Quantum Theory."*

### 1.2 Barandes — the stochastic-quantum correspondence
Jacob Barandes (Harvard) argues quantum theory is equivalent to a class of generalized
stochastic processes he calls **indivisible** (non-Markovian). Core structure:
- A configuration (a definite "beable", e.g. position) exists at all times. Transition
  matrix `Γ(t)`, entries `Γ_ij(t)` = prob. of config `i` at time `t` given config `j` at 0.
  Valid stochastic matrix: `Γ_ij ≥ 0`, columns sum to 1.
- **Divisible = Markovian:** `Γ(t₂,t₀) = Γ(t₂,t₁) Γ(t₁,t₀)` (Chapman–Kolmogorov).
  **Indivisible:** this factorization fails except at special times ("division events" =
  measurements).
- **Stochastic-quantum dictionary:** `Γ(t) = Θ(t) ⊙ Θ*(t)` (⊙ = entrywise/Hadamard),
  where in the unitary case `Θ(t) = U(t) = e^{-iHt}` and `Γ_ij = |U_ij|²`.
- `|U|²` is doubly stochastic **iff** `U` is unitary (columns of a unitary are unit
  vectors). Indivisibility comes from interference: `|UV|² ≠ |U|² |V|²` entrywise.
- Barandes treats unitarity as *derived* (via Stinespring dilation), not axiomatic.
- Papers: *The Stochastic-Quantum Correspondence* (arXiv:2302.10778); *Quantum Systems as
  Indivisible Stochastic Processes* (arXiv:2507.21192).

### 1.3 Literature check (already done)
Web search found **no** existing work connecting the two programs, and **no** mutual
citation. A related paper *"Divisible and indivisible Stochastic-Quantum dynamics"*
(arXiv:2505.08785) stays entirely within standard Hermitian maps. So the bridge below is
unexplored ground.

---

## 2. The core question

Both programs demote the standard Hilbert-space formalism to something derived, and both
elevate time-reversal / antilinearity. Concretely:

> Barandes builds his correspondence on **ordinary unitarity in a standard inner product**.
> Mannheim recovers unitarity only in a **modified (PT/C) inner product** for a
> non-Hermitian `H`. Can Mannheim's antilinear PT symmetry **predict / produce** indivisible
> stochastic processes — i.e., can you run Barandes' `Γ = Θ ⊙ Θ*` through the PT inner
> product and still get a legitimate stochastic matrix?

Hand-argument before computing: unbroken PT (real spectrum) ⇒ pure oscillatory phases ⇒
bounded interference cross-terms ⇒ plausibly a valid, indivisible `Γ`. Broken PT ⇒ real
exponentials ⇒ `|U|²` not normalizable ⇒ no valid process. So the conjecture was
"antilinear symmetry is the *gate* for a valid indivisible process to exist." The
calculation below tests this precisely.

---

## 3. The numerical experiment (this was run and works)

**Model:** canonical 2×2 PT-symmetric Hamiltonian
```
H = [[ e^{iθ},  s   ],
     [  s    , e^{-iθ}]]     P = σ_x,  T = complex conjugation   (P H* P = H ⇒ PT-symmetric)
```
Eigenvalues (with r=1): `E± = cosθ ± sqrt(s² − sin²θ)`.
- **Unbroken PT:** `s² > sin²θ` (real spectrum). Used `θ=π/4, s=1`.
- **Broken PT:** `s² < sin²θ`. Used `θ=π/4, s=0.5` ⇒ `E = 0.707 ± 0.5i`.

**Construction tested:**
1. Naive Barandes: `Γ = |U|²`, `U = e^{-iHt}`.
2. Metric-corrected: biorthogonal metric `η = (V V†)^{-1}` (V = right-eigenvector matrix),
   which satisfies `H†η = ηH` and is positive-definite in the unbroken phase. Canonical
   similarity `ρ = η^{1/2}` gives Hermitian partner `h = ρ H ρ^{-1}` and unitary
   `u = ρ U ρ^{-1}`. Metric-corrected `Θ = ρ U ρ^{-1}`, `Γ = |Θ|²`.

### 3.1 Working script
Save as `pt_barandes.py`. Requires `numpy`, `scipy`.
```python
import numpy as np
from scipy.linalg import expm, sqrtm, eig
np.set_printoptions(precision=4, suppress=True)

def build_H(r, theta, s):
    return np.array([[r*np.exp(1j*theta), s],
                     [s,                  r*np.exp(-1j*theta)]], dtype=complex)

P = np.array([[0,1],[1,0]], dtype=complex)
def PT_check(H):                       # PT symmetry: P H* P == H
    return np.allclose(P @ H.conj() @ P, H)

def biorthogonal_metric(H):            # canonical metric eta = (V V^dag)^{-1}
    E, V = eig(H)
    Vinv = np.linalg.inv(V)
    eta = Vinv.conj().T @ Vinv
    return E, V, 0.5*(eta + eta.conj().T)

def all_hermitian_intertwiners(H):     # Hermitian eta solving H^dag eta - eta H = 0
    I=np.eye(2,dtype=complex); sx=np.array([[0,1],[1,0]],dtype=complex)
    sy=np.array([[0,-1j],[1j,0]],dtype=complex); sz=np.array([[1,0],[0,-1]],dtype=complex)
    basis=[I,sx,sy,sz]; Hd=H.conj().T; rows=[]
    for B in basis:
        M = Hd@B - B@H
        rows.append([np.real(np.trace((1j*C).conj().T @ M))/2 for C in basis])
    A=np.array(rows).T
    u,sv,vh=np.linalg.svd(A); tol=1e-8
    null=vh[[i for i in range(4) if sv[i]<tol]] if np.any(sv<tol) else vh[[3]]
    out=[]
    for c in null:
        eta=sum(ci*Bi for ci,Bi in zip(c,basis)); eta=0.5*(eta+eta.conj().T)
        out.append((eta, np.linalg.eigvalsh(eta)))
    return out

def col_sums(G): return G.sum(axis=0).real

def report(label, r, theta, s, t=1.3):
    print("="*70); print(f"{label}:  r={r}, theta={theta:.4f}, s={s}")
    H=build_H(r,theta,s); print("PT-symmetric:", PT_check(H))
    E,V,eta=biorthogonal_metric(H); Es,_=eig(H)
    print("eigenvalues:", np.round(np.sort_complex(Es),4))
    real_spec = np.allclose(Es.imag,0,atol=1e-9); print("real spectrum:", real_spec)
    U=expm(-1j*H*t)
    print("naive |U|^2 column sums:", np.round(col_sums(np.abs(U)**2),4), "(want [1,1])")
    print("H^dag eta - eta H ~0 ?", np.allclose(H.conj().T@eta-eta@H,0,atol=1e-8),
          "| eta eigs:", np.round(np.linalg.eigvalsh(eta),4))
    if real_spec:
        rho=sqrtm(eta); rho_inv=np.linalg.inv(rho)
        h=rho@H@rho_inv; u=rho@U@rho_inv; G=np.abs(u)**2
        print("h Hermitian:", np.allclose(h,h.conj().T,atol=1e-8),
              "| u unitary:", np.allclose(u@u.conj().T,np.eye(2),atol=1e-8))
        print("metric-corrected Gamma:\n", np.round(G,4))
        print("col sums:", np.round(col_sums(G),4),
              "| doubly-stochastic:", np.allclose(col_sums(G),1) and np.allclose(G.sum(1),1))
        u2=rho@expm(-1j*H*2*t)@rho_inv; G2=np.abs(u2)**2
        print("indivisible? ||Gamma(2t)-Gamma(t)^2|| =",
              round(np.linalg.norm(G2-G@G),4), "(>0 => non-Markovian)")
    else:
        print("-> no positive-definite metric. Hermitian intertwiners:")
        for eta_s,ev in all_hermitian_intertwiners(H):
            print("   eigs:", np.round(ev,4), "indefinite:", ev[0]*ev[-1]<0)
        print("   ||U(t)|| at t=0.5,1,2,4,8:",
              np.round([np.linalg.norm(expm(-1j*H*tt)) for tt in [0.5,1,2,4,8]],3))

report("UNBROKEN PHASE", 1.0, np.pi/4, s=1.0)
report("BROKEN PHASE",   1.0, np.pi/4, s=0.5)
```

### 3.2 Actual results obtained
**Unbroken (θ=π/4, s=1, spectrum {0, 1.414}):**
- Naive `|U|²` column sums `[3.23, 1.30]` — **NOT stochastic**.
- `η` positive-definite (eigs 0.59, 3.41), `H†η=ηH` holds, `h` Hermitian, `u` unitary.
- Metric-corrected `Γ = [[0.368, 0.632],[0.632, 0.368]]` — **doubly stochastic, entries ≥ 0**.
- `||Γ(2t) − Γ(t)²|| ≈ 0.93` — **genuinely indivisible (non-Markovian)**.

**Broken (θ=π/4, s=0.5, spectrum 0.707 ± 0.5i):**
- Naive column sums `[5.34, 0.54]` and diverging with `t`.
- **No positive-definite metric exists** — every Hermitian intertwiner is indefinite
  (signatures `[-1.39, 0.24]`, `[-1, 1]`).
- `||U(t)||` grows exponentially: `1.58, 2.04, 3.61, 10.36, 77.2` at `t=0.5,1,2,4,8`.
- No valid stochastic matrix exists.

---

## 4. Conclusions reached

1. **Existence gates, but does not generate.** Unbroken antilinear (PT) symmetry is
   exactly the condition for a valid, probability-conserving indivisible process to exist;
   cross the exceptional point (PT breaking) and it vanishes totally. So the "gatekeeper"
   reading of the conjecture is **confirmed**.

2. **The deflationary core (main result).** The metric-corrected amplitude
   `Θ = ρ U ρ^{-1}` is just the ordinary unitary evolution `e^{-iht}` of the **isospectral
   Hermitian partner** `h = ρ H ρ^{-1}`. So the "PT-corrected Barandes process" is nothing
   but the *ordinary* Barandes process of `h`. This is an instance of a general theorem
   (**Mostafazadeh**): a diagonalizable non-Hermitian `H` with real spectrum and complete
   biorthogonal eigenbasis is similarity-equivalent to a Hermitian Hamiltonian. Hence
   **closed-system PT machinery cannot produce a new class of indivisible processes** — it
   is an isomorphism back to ordinary QM, not a generalization. "Predict" (strong sense):
   **no.**

3. **Loop-closure with the starting point.** Mannheim's "exponential balancing" *is* the
   metric similarity `ρ = η^{1/2}`: the operator that turns paired growing/decaying
   exponentials into bounded, norm-preserving phases. "Exponential balancing," "unbroken
   antilinear symmetry," and "a valid indivisible process exists" are three names for the
   same condition.

4. **Two conceptual costs uncovered.**
   - **Dynamics-dependent beables.** `ρ = η^{1/2}` is generally non-diagonal in the
     configuration basis, so it *rotates* the beables. Since `η` depends on `H`, the beable
     basis becomes dynamics-dependent — cutting against Barandes' core selling point of a
     fixed, non-contextual beable set.
   - **Metric non-uniqueness ⇒ process non-uniqueness.** The pseudo-Hermitian metric is not
     unique (unless pinned by extra observables), so there is a *family* of valid stochastic
     processes, one per metric choice.

5. **Caveat.** This is a 2-level toy. The deflationary core is robust (rests on the general
   Mostafazadeh isospectrality argument), but claims about field theory / many-body / the
   actual PU oscillator are not established.

**Reframed frontier question:** moved from "can PT predict indivisible processes?" (answer:
no, not in the closed unbroken case) to **"does broken-PT-as-open-dynamics give indivisible
processes the Hermitian case can't?"**

---

## 5. Next steps (ranked, actionable)

### 5.1 [DO FIRST] Fixed-beable / Kolmogorov-cycle characterization
**Question:** which non-Hermitian `H` admit a metric `η` that is **diagonal in the
configuration basis** (preserving the original beables)?

**Setup.** Impose `η = diag(d₁…d_n)`, `d_i > 0`, and `H†η = ηH`. Component form:
`H*_ji d_j = d_i H_ij`. Diagonal (`i=j`): forces `H_ii` **real**. Off-diagonal (`i≠j`):
`d_i/d_j = H*_ji / H_ij`, which requires `arg(H_ij) + arg(H_ji) = 0` and
`|H_ij|/|H_ji| = d_j/d_i`.

**Conjecture to prove/refute:** consistency of `d_i/d_j` around closed loops reduces to a
**Kolmogorov cycle condition** (product of coupling phases around any loop = 1) — i.e. the
detailed-balance criterion from stochastic-process theory. If true, the clean statement is:
*"A PT-symmetric dynamics admits a fixed-beable indivisible representation iff its couplings
satisfy a Kolmogorov cycle condition."* This directly resolves cost 4a and is the most
quotable potential result.

**Tasks:** (a) derive the condition for general `n`; (b) check the 2×2 example **fails**
(diagonal entries `e^{±iθ}` not real) — consistent with the observed basis rotation;
(c) construct a 3×3 example that **satisfies** it and verify a fixed-beable stochastic `Γ`;
(d) connect explicitly to Kolmogorov/detailed-balance in classical Markov-chain theory.
Mostly analytical; fully tractable.

### 5.2 [DEEPEST] Broken phase as an open subsystem via Stinespring dilation
Treat broken-PT dynamics not as a failed closed system but as a subsystem of a larger
**Hermitian** system (standard for gain/loss PT systems; also matches Barandes' own
dilation route to unitarity). **Tasks:** dilate the broken 2×2 `H` to a Hermitian
`H_big` (4×4), form the ordinary Barandes indivisible process on the enlarged config space,
then compute the **reduced process** on the original configurations. Ask: is it a
well-defined sub-stochastic process? Is it simultaneously non-Markovian in the
*open-system* (information-backflow) sense **and** indivisible in Barandes' sense? This is
the only place the two distinct "non-Markovianities" could genuinely meet. Numerical,
2×2→4×4, tractable but more involved.

### 5.3 [EDGE PROBE] The exceptional point
The deflation relies on `ρ = η^{1/2}` existing. At the EP, `H` is defective
(non-diagonalizable), `η` singular, `ρ` nonexistent — no Hermitian partner. Dynamics gains
polynomial×exponential terms (`t·e^{-iEt}` from the Jordan block). **Task:** approach the EP
from the unbroken side; watch a metric eigenvalue → 0, `ρ` become singular, the beable
rotation degenerate, and the metric-corrected `Γ` collapse. Determine whether anything
survives in a regularized limit. Short calculation, targets exactly the crack in the
argument.

### 5.4 [AMBITIOUS TARGET] The Pais–Uhlenbeck oscillator
The genuine Mannheim-relevant case: fourth-order, infinite-dimensional, real ghost. Ask
whether the stochastic-quantum correspondence even makes sense there (continuous config
space, nonlocal metric operator) and whether the PT-metric resolution yields a valid
indivisible process. This is the real prize and genuinely hard; name it as the destination,
not the next step.

### 5.5 [TRAP — AVOID] Naive non-Markovianity-vs-PT-breaking plots
Plotting a standard non-Markovianity measure (BLP/RHP) against the PT-breaking parameter
likely just reproduces known open-system PT results and silently swaps in the **wrong**
non-Markovianity (bath memory, not Barandes' intrinsic indivisibility). Only pursue if
carefully tied to closed-system indivisibility.

---

## 6. Practical notes
- Environment: Python 3, `pip install numpy scipy`. Script in §3.1 runs as-is.
- Conventions: column-stochastic `Γ` (columns sum to 1); `⊙` = entrywise product;
  `η` positive-definite metric; `ρ = η^{1/2}`; `h = ρHρ^{-1}` Hermitian partner.
- Suggested repo layout for continuation:
  `pt_barandes.py` (baseline, done) · `fixed_beable_kolmogorov.py` (§5.1) ·
  `dilation_bridge.py` (§5.2) · `exceptional_point.py` (§5.3) · `notes.md` (running log).

## 7. References
- Barandes, *The Stochastic-Quantum Correspondence*, arXiv:2302.10778
- Barandes, *Quantum Systems as Indivisible Stochastic Processes*, arXiv:2507.21192
- *Divisible and indivisible Stochastic-Quantum dynamics*, arXiv:2505.08785
- Mannheim, *Antilinearity Rather than Hermiticity as a Guiding Principle for Quantum Theory*
- Mannheim, *Making the Case for Conformal Gravity* (review) — background on conformal gravity
- Bender & Mannheim, PT-symmetric treatment of the Pais–Uhlenbeck oscillator
- Mostafazadeh, pseudo-Hermitian QM (metric operator, similarity-to-Hermitian) — the
  theorem behind conclusion §4.2

---
*End of briefing. The recommended concrete starting action is §5.1 (fixed-beable /
Kolmogorov-cycle characterization).*
