# Running log — PT-symmetric / indivisible-stochastic bridge

Continuation of `PT_stochastic_handoff.md`. Baseline experiment: `pt_barandes.py`.

---

## 2026-07-10 — §5.1 DONE: Fixed-beable / Kolmogorov-cycle characterization

**Question.** Which non-Hermitian `H` admit a metric `η` diagonal in the
configuration basis, so the Barandes beables are preserved rather than rotated?

**Answer: the conjecture in the handoff is TRUE, and sharper than expected.**
Code + numerical verification: `fixed_beable_kolmogorov.py` (all checks pass,
including 200/200 randomized trials at n = 3..6).

### Theorem (fixed-beable characterization)

`H` admits a positive diagonal metric `η = diag(d)`, `d_i > 0`, with
`H†η = ηH`, **iff** all of:

- **K1** — every diagonal entry `H_ii` is real;
- **K2** — symmetric coupling support: `H_ij = 0 ⇔ H_ji = 0`;
- **K3** — `H_ij H_ji > 0` for every coupled pair (equivalently
  `arg H_ij + arg H_ji = 0`);
- **K4** — **Kolmogorov cycle condition**: around every cycle of the coupling
  graph, the product of coupling moduli one way equals the product the other
  way.

*Derivation.* The component form of `H†η = ηH` with `η = diag(d)` is
`d_i H_ij = d_j H*_ji`. The `i=j` component gives K1; existence of positive
`d` forces K2; the phase of the off-diagonal relation gives K3; its modulus
gives `d_i/d_j = |H_ji|/|H_ij|`, whose loop-consistency is exactly K4.
Conversely, build `d` along a spanning forest; K4 makes it well defined.

### Corollaries (each verified numerically)

1. **Reality of the spectrum is derived, not assumed.** K1–K4 imply
   `h = η^{1/2} H η^{-1/2}` is Hermitian, so the spectrum is automatically
   real — unbroken antilinearity falls out of the combinatorial conditions.
2. **Uniqueness — cost 4b resolved in this class.** `d` is unique up to one
   scale per connected component of the coupling graph, and the fixed-beable
   process `Γ_ij(t) = (d_i/d_j)|U_ij(t)|²` is invariant under those scales, so
   the process is **unique**. The metric non-uniqueness problem disappears
   exactly when the beables are fixed.
3. **The correction is a pure reweighting.** With diagonal `ρ = diag(√d)`,
   `Γ_ij = (d_i/d_j)|U_ij|²`: same configurations, same beable set; the metric
   enters only as importance weights on the naive transition probabilities.
4. **Classical dictionary (task d).** With hopping rates `q(i→j) := |H_ji|`
   (Barandes column convention), the distribution `π_i ∝ 1/d_i` satisfies
   classical detailed balance `π_i q(i→j) = π_j q(j→i)`. So the metric weights
   are the *inverse* of the Kolmogorov equilibrium distribution of the modulus
   rate graph, and K4 is literally Kolmogorov's criterion from Markov-chain
   theory. Structural characterization: fixed-beable `H` = the positive
   diagonal similarity orbit of Hermitian matrices ("detailed-balanced
   gain/loss").

### Numerical results (from `fixed_beable_kolmogorov.py`)

- **(b) 2×2 canonical PT model fails, as predicted** — via K1 (diagonal
  `e^{±iθ}` not real), consistent with the beable rotation seen in
  `pt_barandes.py`. Note: at n=2 there are no cycles beyond pairs, so K4 is
  vacuous and fixed-beable ⇔ Hermitian *within that family*. The cycle
  condition only bites at n ≥ 3.
- **(c) 3×3 non-Hermitian example passing K1–K4** (built from `d = (1,2,4)`
  with magnitude-asymmetric, phase-antisymmetric complex couplings;
  `‖H − H†‖ ≈ 1.69`): spectrum real `{−1.319, 0.210, 2.009}`; recovered
  `d = (1,2,4)` exactly; naive `|U|²` column sums `(0.40, 1.17, 3.04)` — not
  stochastic — while the reweighted `Γ` is doubly stochastic with
  `‖Γ(2t) − Γ(t)²‖ ≈ 0.41` (genuinely indivisible), **with beables fixed**.
- **Sharp counterexample: only K4 fails.** `H = diag(1,2,3) +` an asymmetric
  positive ring (cycle products 0.216 vs 0.027). Spectrum still real
  `{0.847, 1.840, 3.313}`, positive-definite biorthogonal metric exists, valid
  indivisible process exists (`‖Γ(2t) − Γ(t)²‖ ≈ 0.49`) — but the diagonal
  intertwiner solution space is exactly zero and `ρ` has an 18% off-diagonal
  fraction. **K4 gates fixed beables specifically, not process existence.**
- **Randomized theorem check**: 200/200 trials, n = 3..6 — constructor and
  independent null-space solver agree; K1–K4 ⇒ unique-up-to-scale `d`, real
  spectrum, doubly stochastic fixed-beable `Γ`; perturbing one cycle edge's
  modulus ⇒ K4 fails ⇒ diagonal solution space dimension 0.

### Quotable statement

> A PT/pseudo-Hermitian dynamics admits a fixed-beable indivisible stochastic
> representation iff its coupling graph satisfies the Kolmogorov
> detailed-balance conditions (real diagonal, phase-antisymmetric couplings,
> cycle condition on coupling moduli). The metric weights are then the inverse
> of the detailed-balance stationary distribution, and the fixed-beable
> process is unique.

This resolves conceptual cost 4a of the handoff (dynamics-dependent beables)
by exactly delimiting when it does and doesn't occur, and resolves cost 4b
(metric/process non-uniqueness) within the fixed-beable class. The
deflationary reading deepens: the non-Hermiticity compatible with fixed
beables is precisely classical-detailed-balance gain/loss — a diagonal gauge
of a Hermitian theory.

---

## 2026-07-10 — §5.2 DONE: Broken phase as an open subsystem via dilation

Code: `dilation_bridge.py`. **Result: the broken phase supports a valid,
permanently indivisible sub-stochastic process with zero information
backflow — the two non-Markovianities dissociate, and Barandes
indivisibility is the strictly stronger notion.**

### Construction

1. **Broken PT = post-selection (exact identity).** The canonical dimer is
   balanced gain/loss: `H = cosθ·I + i sinθ σ_z-type + s σ_x`. Subtracting
   the uniform gain, `H_loss = H − i sinθ·I` is pure loss and
   `e^{-iHt} = e^{+sinθ·t} · C(t)` with `C(t) = e^{-iH_loss t}` a contraction
   (verified: singular values ≤ 1 for all t, identity to machine precision).
   The notorious broken-phase runaway is a *scalar normalization*; the
   conditional (normalized) dynamics coincide. Mannheim's broken phase is
   survival-conditioned dynamics of a lossy system.
2. **Halmos dilation, per time t.** `U_big(t) = [[C, √(1−CC†)],[√(1−C†C), −C†]]`
   is exactly unitary (error ~1e-15) with `Γ_big(0) = I`. Barandes needs only
   per-time unistochasticity — the family need not be a group (indivisibility
   *is* the failure to compose) — so `Γ_big(t) = |U_big(t)|²` is an ordinary
   Barandes indivisible process on 4 configs {1, 2, a1, a2}. A finite
   Hermitian generator can't reproduce decay for all t (quasi-periodicity),
   but the per-time dilation sidesteps that entirely.
3. **Reduced process** `Γ_red(t) = |C(t)_ij|²` = top-left block: entries ≥ 0,
   column sums ≤ 1 for all t (verified). Column-sum deficit = leak
   probability; broken-phase survival decays monotonically.

### Diagnostics

- **Divisibility (Barandes-intrinsic).** With `Γ(t₁)` invertible the unique
  divisor candidate is `M = Γ(t₂)Γ(t₁)⁻¹` (column sums automatic), so
  divisibility ⇔ `M` entrywise ≥ 0 (+ col sums ≤ 1 if sub-stochastic).
  Infinitesimal version: classical P-divisibility ⇔ generator
  `L(t) = Γ̇Γ⁻¹` has nonnegative off-diagonals (exact derivative via
  `Ċ = −iH_loss C`; condition-number guarded — early runs showed the
  *magnitudes* of finite-gap violations are conditioning-sensitive, but sign
  and location are robust, e.g. worst broken-phase point has cond(Γ) ≈ 830).
- **Backflow (BLP analog).** TV distance between the two basis-state
  initializations: (a) extended 3-outcome space {1, 2, leaked} — linear;
  (b) conditional (survival-post-selected). Reported in windows [0,20] and
  [20,40].

### Findings (θ = π/4, sweep s = 0.3 … 1.3, EP at s = sinθ ≈ 0.7071)

1. **The reduced process is indivisible in BOTH phases** (t* ≈ 1 everywhere),
   but the *temporal structure* flips at the EP:
   - **Broken/EP**: `min offdiag L(t)` goes negative at t* and **stays
     negative forever**, smoothly approaching a strictly negative constant
     (e.g. −1.207 at s=0.5) — *terminal, persistent indivisibility*, no
     revivals (lock-in to the slow decay mode).
   - **Unbroken**: `L(t)` **oscillates** through recurrent positive
     (divisible) and negative windows at the Rabi period — *recurrent
     indivisibility*, the open-system shadow of closed-system quasi-periodic
     interference.
2. **Information backflow transitions exactly at the EP.** Late-window
   conditional backflow (bf[20,40]) = 0.0000 for every broken s and at the
   EP; jumps to 1.32 at s = 0.72. Broken-phase backflow is a finite
   early-time transient; unbroken accrues per oscillation forever.
   (Matches known PT open-system results, but here derived at the
   stochastic-process level.) Extended-space (linear) classical backflow is
   **identically zero in both phases** — classical marginals with a leak
   outcome never show backflow in this dilation.
3. **Answer to the frontier question: YES, with a precise meaning.** Broken
   PT gives an indivisible process the closed/Hermitian case cannot:
   *terminally* indivisible with monotone leak and zero backflow. A closed
   Hermitian system's `Γ = |U|²` is quasi-periodic — its indivisibility is
   necessarily recurrent. So the two "non-Markovianities" genuinely meet
   here and **dissociate**: broken PT is backflow-Markovian yet
   Barandes-indivisible. Indivisibility is the finer probe of the PT phase:
   it doesn't vanish at the EP — it changes character (recurrent ↔
   terminal).
4. Bonus identity: any 2-site lossy Hamiltonian is a shifted PT dimer, so
   "overdamped open dynamics" and "broken PT" coincide at n=2; the
   stochastic signature of PT breaking is the recurrent→terminal
   indivisibility transition plus loss of backflow.

### Caveats

- Near the EP the oscillation period π/√(s²−sin²θ) diverges; any finite
  window smooths the transition (s=0.72 shows lateNeg=1.00 in [6,12] only
  because its first revival is at t≈23 — the [20,40] backflow window
  correctly catches it). The dichotomy is exact as T→∞.
- Finite-gap violation *magnitudes* are not calibrated (conditioning-
  sensitive); only sign/location are meaningful. Generator trace is the
  robust diagnostic.
- 2×2 toy; terminal-indivisibility asymptote not yet proven analytically.

---

## 2026-07-10 — §5.3 DONE: The exceptional point

Code: `exceptional_point.py`. **Verdict: the EP is a coordinate singularity
of the similarity-to-Hermitian dictionary, not of the stochastic process.**
The crack in the deflationary argument is real (no Hermitian partner exists
at the EP) but harmless at the process level: existence of an indivisible
process is governed by the dilation (§5.2), which is smooth there.

### At the EP (s* = sinθ)

- `H` defective as expected: double eigenvalue cosθ, rank(H − cosθ·I) = 1,
  cond(eigenvector matrix) ~ 1e8 (numerically Jordan).
- Naive `|U|²` grows **polynomially**, fitted exponent 1.95 ≈ 2 (Jordan
  `t·e^{-iEt}` ⇒ t² in probabilities) — sitting exactly between unbroken
  (bounded) and broken (exponential).
- The Hermitian intertwiner space at the EP is 2-dimensional: one **singular
  PSD rank-1** ray and one indefinite direction. The positive-definite cone
  is exited exactly through the singular boundary — no `ρ`, no Hermitian
  partner, the Mostafazadeh deflation genuinely fails *at* this point.

### Collapse scalings from the unbroken side (s = s*(1+ε), κ ~ √(2ε)·sinθ)

Verified over ε = 1e-1 … 1e-7 with log-log slope fits (all to ±0.002):

| quantity | scaling | fitted slope |
|---|---|---|
| cond(η) | ε⁻¹ ~ κ⁻² (Petermann-factor divergence) | −0.998 |
| cond(ρ) (beable-map anisotropy) | ε^(−1/2) ~ κ⁻¹ | −0.499 |
| ‖Γ_ε(t) − I‖ at fixed lab t | ε ~ (κt)² | +0.999 |

So at any fixed lab time the metric-corrected process **freezes to the
trivial identity process** (`h → cosθ·I`, Rabi frequency → 0). A regularized
lab-time limit exists but is trivial — and it is *not* the EP dynamics,
which grows like t². The limit is discontinuous with respect to the physics.

### What genuinely survives: the critical process in rescaled time

On the critically-slowed clock τ = κt, `Γ_ε(τ/κ)` converges (to 1e-10
between ε = 1e-4 and 1e-6) to the universal Rabi process
`Γ_lim(τ) = [[cos²τ, sin²τ],[sin²τ, cos²τ]]` (Rabi axis exactly σ_x — the
same symmetric form as the baseline's unbroken result), which is genuinely
indivisible (‖Γ(2τ) − Γ(τ)²‖ ≈ 0.97). The Jordan linear growth is the
κ → 0 limit of sin(κt)/κ. **But** this survivor is abstract: the beable map
`ρ_ε` that identifies its states with the original configurations diverges
(cond ~ κ⁻¹), so the process outlives the EP while its beable interpretation
does not — the §5.1 beable-rotation cost becoming infinite.

### Reconciliation with §5.2 (the punchline)

Dense sweep s = 0.68 … 0.735 through the EP: every open-side quantity
(reduced-process entries, survival, indivisibility generator floor) varies
smoothly and monotonically through s*, while the closed-side cond(η)
diverges approaching it from above and doesn't exist below. Nothing physical
happens at the EP in the process description; only the Hermitian dictionary
blows up. Combined three-phase picture of the naive process growth —
unbroken: bounded / EP: polynomial / broken: exponential — versus the
dilated sub-stochastic process, which is valid and indivisible throughout.

---

## 2026-07-10 — LEMMA PROVED: terminal indivisibility is exact and analytic

Code: `lemma_terminal_indivisibility.py` (verifies every claim to 1e-11).
§5.2 finding 1 is now a theorem, with sharper structure than the numerics
suggested.

**Lemma.** For the dimer in the broken phase (κ̃ = √(sin²θ − s²) > 0), with
c = cosh κ̃t, shc = sinh(κ̃t)/κ̃ and
`p = c + sinθ·shc`, `q = c − sinθ·shc`, `r = s·shc`:

- `Γ_red(t) = e^{-2sinθ·t} [[p², r²],[r², q²]]`, `det Γ_red = e^{-4sinθ·t}(1−2r²)`;
- the generator off-diagonals are **exactly**
  `L₁₂ = 2spr/(1−2r²)`, `L₂₁ = 2sqr/(1−2r²)`
  (the Wronskian-type combinations r′p − p′r and r′q − q′r are both
  identically the constant s — that is the whole proof).

**Consequences (all verified numerically):**
1. P-divisibility holds precisely on [0, t_c) with
   `t_c = κ̃⁻¹ arcsinh(κ̃/(s√2))` — exactly the time at which `det Γ_red`
   crosses zero. Divisibility dies when and because the process becomes
   singular. (Explains the finite-gap spikes near t ≈ 1.3 in
   `dilation_bridge.py`; exact t_c = 1.3170 at s = 0.5 vs the observed
   grid value 1.35.)
2. For all t > t_c: `L₁₂ < 0` strictly, forever — permanent indivisibility.
3. `L₁₂ → −(sinθ + κ̃)`: the numerically observed floor −1.207 at s = 0.5
   is −(sin(π/4) + 0.5) = −1.2071 exactly; also confirmed at (π/4, 0.3) →
   −1.3474 and (π/3, 0.5) → −1.5731.
4. `L₂₁` flips back positive at `t₀ = κ̃⁻¹ artanh(κ̃/sinθ) > t_c`: late-time
   indivisibility is carried entirely by L₁₂ — transitions *into* the gain
   site.
5. One formula, three regimes: analytic continuation κ̃ → iκ gives the
   unbroken phase, where `1 − 2(s/κ)² sin²(κt)` oscillates through zero
   forever (recurrent windows; note (s/κ)² > 1 always); at the EP
   everything is polynomial with `t_c = 1/(s√2)`, and t_c is continuous
   across the transition (verified to 1e-4).

---

## 2026-07-10 — §5.4 DONE: Pais–Uhlenbeck

Code: `pais_uhlenbeck.py` (grid 44² = 1936 configs, spectral derivatives).
**Verdict: the stochastic-quantum correspondence and the PT no-ghost
construction part ways at PU — they resolve the ghost in incompatible
currencies (beable reality vs energy positivity).**

### A. The ghost realization IS a valid Barandes process (answer to Q-a)

The Ostrogradski Hamiltonian
`H = p₁q₂ + p₂²/2γ + (γ/2)(ω₁²+ω₂²)q₂² − (γ/2)ω₁²ω₂²q₁²` is **Hermitian on
the real configuration space (x, ẋ)**. On the grid: `‖H − H†‖ = 0`,
`Γ = |U|²` doubly stochastic to 2e-14 on 1936 configs, genuinely indivisible
(‖Γ(2t) − Γ(t)²‖ ≈ 2.7), and validated dynamically — Ehrenfest is exact for
quadratic H, and ⟨x(t)⟩ tracks the exact classical fourth-order trajectory
to 3e-3 (residual = packet tails at the box walls). Spectrum runs from −26
to +140: **unbounded below, and completely irrelevant** — the ghost is an
energy-accounting pathology, invisible to the free stochastic process.
Beables are fixed (Hermitian ⇒ K1–K4 with η = 1). Barandes' correspondence
makes perfect sense for free PU, negative energies and all.

### B. The no-ghost move has no stochastic counterpart (answer to Q-b)

Mannheim's positive spectrum requires the ghost mode's vacuum to satisfy
`b†Ω = 0` (position space: e^{+y²/2}) — normalizable only on a rotated
contour. This is a **domain change, not a similarity** (a similarity can't
flip the spectrum), and finite-dimensional machinery can never see it:
- null(b) = |0⟩ at every truncation N (the true vacuum, stable);
  null(b†) = |N−1⟩ — pinned to the truncation edge, escaping to infinite
  energy as N grows; restricted to any fixed low-energy sector,
  σ_min(b†) = 1 exactly. **The PT vacuum has no shadow in the
  real-configuration theory at any cutoff.** Not a beable rotation (§5.1),
  not a coordinate collapse (§5.3) — an exit from the sample space.
- The contour-rotation operator `R = e^{(π/2)D}`, `D = (i/2)(a†² − a²)`
  (the y → −iy dilation): log₁₀ cond(R_N) grows at ~1.2 decades per Fock
  level (53 decades at N = 48); the would-be metric ~(RR†)⁻¹ is unbounded
  with unbounded inverse. The §5.3 collapse at every scale at once, with no
  critical-rescaling survivor.

So: **no valid stochastic process on the original beables realizes the
positive-energy PU.** Barandes keeps real beables and pays in negative
energies; Mannheim buys positive energies and pays with the sample space
itself. The handoff's §4.4a cost (dynamics-dependent beables), taken to the
PU limit, becomes beable *non-existence*.

### C. Equal frequencies (the PU exceptional point)

Classical normal-mode matrix defective (eigenvector cond ~1e8, Jordan
block, secular t·sin(ωt) growth) — yet the Hermitian grid realization
passes through smoothly: ⟨x(t)⟩ tracks the secular classical solution
`2cos(ωt) + ωt·sin(ωt)` to 9e-4 and Γ stays exactly doubly stochastic.
PU-scale confirmation of §5.3: the Jordan/EP pathology lives in the
normal-mode (non-Hermitian) dictionary, never in the process.

### Caveats

Free theory only — interactions (where the ghost instability becomes
physical via vacuum decay) not addressed; dense-spectrum subtleties
(ω₁/ω₂ irrational) not probed; Mannheim's specific PU operator equivalences
not re-derived (the contour-rotation structure of the quadratic ghost mode
is standard and suffices for the structural conclusion); IR/UV grid cutoffs.

---

## 2026-07-10 — INTERACTING PU: the ghost enters the process in three stages

Code: `interacting_pu.py` (quadratic cascade + classical survey + ghost-pair
quantum leak) and `quartic_pu_leak.py` (the decisive probe test).
**Answer to the open question: the instability becomes stochastically
visible in stages — recurrent → transient → explosive — and becomes a
genuine probability pathology exactly when the classical flow is
incomplete.**

### Stage 1 — quadratic interaction: valid process, now TRANSIENT

`H = ω₁a†a − ω₂b†b + g(a†b† + ab)` is Hermitian, so `Γ = |U|²` stays
exactly doubly stochastic forever (verified 2e-14). But the ghost sign
collapses the instability threshold from `g > (ω₁+ω₂)/2` (normal twin, sum
frequency) to `g > |ω₁−ω₂|/2` (difference frequency — zero at resonance).
Exact benchmarks, all matched to ~4 decimals: cascade `⟨n⟩ = sinh²(gt)`;
escape law `P(n ≤ K) = 1 − tanh^{2K+2}(gt) → 0` (rate 2g); detuned growth
consistent with `(g²/κ²)sinh²(κt)`, `κ = √(g²−δ²/4)`; normal twin bounded at
⟨n⟩ ~ 0.006. Energy books exactly balanced throughout: `E_normal = +8.301`,
`E_ghost = −8.301`, `⟨H⟩ = 0` conserved. **"Vacuum decay" is a
configuration-space cascade with balanced energy books: the process is
valid and indivisible but transient — it permanently escapes every finite
region.** First stage where the ghost is *visible* to the process
(transience), still not a pathology.

### Stage 2 — nonlinear, benign regime (Smilga): still only transience

Classical survey: the ghost pair
`(p₁²+ω₁²x₁²)/2 − (p₂²+ω₂²x₂²)/2 + λx₁²x₂²` at moderate amplitude is mostly
*bounded* (benign islands; one escape found at λ=−0.05, x₁=3.5, t*≈72).
Quantum leak test with absorber: onset drifts strongly with box size
(4.4 → 14.4 for L = 12 → 18) — tail-driven asymptotic escape at most.
Benign classically ⇒ transient (at most) stochastically.

### Stage 3 — malicious nonlinearity: EXPLOSIVE — no closed process

Quartic PU (`x⁗ + Ωẍ + ω̄x = (4λ/γ)x³`): classical **finite-time blowup**
for both signs of λ at every amplitude tested (t* = 3.3–6.9, decreasing
with amplitude; dominant balance `x ~ A(t*−t)⁻²`, `A = √(30γ/λ)`).
Quantum (split-step with the three-factor Strang decomposition for the
`p₁q₂` coupling, absorbing layer):
- **Lattice subtlety (decisive for methodology):** finite-time escape needs
  unbounded acceleration, so a grid transports the wavefront only while the
  classical arrival speed < k_max = π/dx. Box-scaling onsets (2.3 → 3.4 →
  9.5 for L = 12/18/24) correlate exactly with v_cl(edge)/k_max =
  1.4/2.4/3.4: the drift is the lattice confining, not the physics. This is
  the same structural fact as §5.4-B: a non-essentially-self-adjoint H has
  **no faithful finite truncation**.
- **Probe test (resolved regime):** quantum probability arrives at radii
  r = 5–8 at t ≈ 1.8–2.2 with bulk weight (>5%), *earlier* than the
  classical center-trajectory law t_cl ≈ 3.0–3.5 (the packet ensemble
  contains faster-escaping ICs), while the free control never passes r ≈ 6.
  Quantum arrival tracks/undercuts the classical finite-time law wherever
  the grid can resolve it; that law saturates at t* < ∞ as r → ∞.

Conclusion: in the continuum/infinite-volume limit, probability reaches
infinity at finite time. **No closed stochastic process on the real
configurations exists for the malicious interacting ghost — only a
sub-stochastic leaky one (the §5.2 dilation structure, now forced by
Hermitian physics rather than PT breaking).**

### The dictionary (closing entry)

In standard stochastic-process language the hierarchy is exactly:
- free / normal-sign: **conservative, recurrent** process;
- ghost + quadratic (and benign nonlinear): **transient** process — valid,
  indivisible, escapes to infinity asymptotically at rate 2g;
- ghost + malicious nonlinear: **explosive** process (the probabilist's
  term of art: infinitely many transitions in finite time, mass leaves the
  state space) — the semigroup is non-conservative and the closed Barandes
  representation fails.

So the Ostrogradski ghost was never an energy problem for the
stochastic-quantum correspondence: it is a *recurrence-classification*
problem. Energetics (unboundedness below) is the classical-physics
diagnosis; transience/explosion is the same disease expressed in the
process's own currency.

### Caveats

- Blowup times are tolerance-sensitive (t* = 5.13 at rtol 1e-8 vs 5.336 at
  1e-11 for the same IC); qualitative structure robust.
- Probe onsets use a 5% bulk-weight threshold; the quantum-earlier-than-
  classical arrivals reflect ensemble spread, not superluminal transport.
- The r → ∞ saturation itself is inferred from (proven) classical blowup +
  quantum tracking in the resolved window — no fixed grid can verify it
  directly (that impossibility being itself one of the findings).
- 2-DOF quantum mechanics; field-theoretic vacuum decay not addressed.

---

## 2026-07-10 — THEOREM: the explosion dictionary (stage 3 sharpened)

Code: `explosion_theorem.py` (all five verifications pass). Stage 3 of the
interacting-ghost result is now a theorem (physics rigor: Weyl alternative
and Reed–Simon II Thms X.9/X.10 cited as rigorous inputs; WKB and
semiclassical quantization used at standard validity; Feller boundary
classification for the stochastic leg).

### Theorem (explosion dictionary, 1D mechanism model)

For `H = p²/2 + V` on the line with an escaping end (`V → −∞`), define the
classical time of flight `T(E) = ∫^∞ dx/√(2(E−V))`.

1. **T = ∞** (sub-quadratic fall, e.g. `V ≳ −Kx²`): limit point ⇒ H
   essentially self-adjoint ⇒ unique unitary `U(t)` ⇒ unique conservative
   Barandes process. The ghost is at most transient.
2. **T < ∞** (super-quadratic fall — the malicious case): limit circle.
   **The one-line identity that runs the whole theorem:** WKB gives
   `|ψ±|² ≈ [2(E−V)]^(−1/2)` for *both* solutions of `(H−z)ψ = 0`, so the
   deficiency solution's L² norm near the escaping end **is** the classical
   time of flight. H loses essential self-adjointness exactly when the
   classical particle reaches infinity in finite time. Consequently:
   - (a) no canonical unitary dynamics: a U(1) family of self-adjoint
     extensions per escaping end (U(2) for two ends, including completions
     that *transmit through infinity*) — boundary data at infinity, not
     contained in H;
   - (b) every extension is conservative but returns probability from
     infinity after the finite classical round trip: discrete spectrum with
     local level spacing `ΔE = π/T_cross(E)`;
   - (c) the regulator-independent (Feller-minimal) object is
     sub-stochastic: an **explosive** process losing mass at the classical
     escape rate; conservativity costs extra-theoretic boundary data;
   - (d) one integral decides all three theories: classical completeness,
     quantum self-adjointness (Weyl), stochastic conservativity (Feller
     exit boundary).

### Verifications (V = −x⁴ malicious vs V = −x² marginal control)

- **V1** — the integral: convergent exactly for α > 2 (α=4: 0.6484 →
  0.6555 over four decades of cutoff; α=2: log-divergent 3.1 → 9.6).
- **V2** — level-spacing law `ΔE = π/T_cross(E, L)` matches measured
  spacings to ~1–3% in all 8 (potential, L) cases; for −x⁴ the spacing
  *saturates* (2.32 vs predicted 2.32 at L=16 — reflection off infinity at
  finite recurrence time), for −x² it decays toward the continuum.
- **V3** — extension = regulator data: the eigenvalue nearest E=10 sweeps
  erratically as the wall moves (10.06, 8.84, 9.82, 10.72, …): no L→∞
  limit for any individual completion, while the spacing is stable.
- **V4** — the minimal process converges and explodes: 1D absorbing-layer
  evolution (1D beats the lattice resolution barrier that blocked the 2D
  runs): absorbed mass at t=1 is 98.6–98.8% **independent of box size**
  (L = 8/12/16), and the onset saturates tracking the classical arrival
  times (0.34/0.38/0.40 → T_esc = 0.4635). Direct verification that
  probability reaches infinity at finite time.
- **V5** — completions observably differ: with a Dirichlet wall the
  probability leaves rightward and returns from the right (P(x>5) = 0.047,
  P(x<−5) = 0.000 at revival); with periodic identification it returns
  from the **left** (0.035 vs 0.013) — a +∞→−∞ wormhole. Both revive
  ~95% of the probability after the finite round trip. Same H on C₀^∞,
  different physics: the completion is genuinely new data.

### Interpretation, tied back to the program

The malicious interacting ghost forces a trilemma, and each horn is now a
computed object: (i) accept the **minimal explosive process** — exactly the
§5.2 sub-stochastic dilation structure, and the only regulator-independent
choice; (ii) buy conservativity with **boundary data at infinity** —
unphysical completions that resurrect probability from infinity (from a
side of your choosing); (iii) repair the spectrum à la Mannheim by moving
the domain — which §5.4-B showed exits the sample space entirely. The
Barandes currency makes (i) the canonical answer: vacuum decay of the
malicious ghost *is* explosion in the standard probabilistic sense.

### Caveats

- The theorem is for the 1D mechanism model; the reduction of the 2-DOF
  malicious systems to it is by dominant-balance structure (super-quadratic
  effective fall along the escape direction), not a rigorous
  multi-dimensional deficiency analysis.
- Spacing law and WKB norms are semiclassical-standard, not re-proven;
  R–S X.9/X.10 supply the rigorous LP/LC inputs.
- V4 onset is earlier than the classical rest-start arrival (packet
  momentum tails), as expected; the L-trend is the claim being tested.

---

## 2026-07-10 — MULTIDIMENSIONAL DEFICIENCY ANALYSIS (the rigorous layer)

Code: `deficiency_multiD.py` (all verifications pass). The 1D explosion
dictionary is upgraded to a channel-based multidimensional theory. Crucial
context: in n ≥ 2 the naive dictionary "classical incompleteness ⇔ quantum
non-self-adjointness" is **false in general** (Rauch & Reed, Commun. Math.
Phys. 29, 105 (1973)) — so the correct structure is channel-wise, and
proving it adds content the 1D story cannot supply.

### Theorem C — quadratic ghosts are rigorously safe

Any at-most-quadratic Hamiltonian on ℝⁿ — including the indefinite
cascade `H = ω₁a†a − ω₂b†b + g(a†b†+ab)` at *any* coupling (even deep in
the unstable phase) and the free PU Ostrogradski operator — is essentially
self-adjoint on the Hermite span. *Proof:* quadratics map Hermite level N
into level ≤ N+2 with coefficients O(N), so
`‖Hⁿψ_N‖ ≤ (2C)ⁿ(N/2+n)!/(N/2)!` and every Hermite function is an analytic
vector; Nelson's analytic vector theorem applies. ∎
**Consequence:** unique unitary, unique conservative Barandes process —
"instability ≠ non-uniqueness/explosion" is now a theorem. The
transient/explosive dichotomy of the interacting-ghost section is rigorous
on the transient side.

### Theorem A — channel additivity of deficiency (separable multiD)

Let `H = h₁⊗1 + 1⊗h_⊥` on L²(ℝ×ℝᵐ), with `h₁ = ½p² + V₁`, `V₁`
super-quadratically falling (finite time of flight; limit circle by
R–S X.10), and `h_⊥` self-adjoint with orthonormal eigenbasis {φₙ, Eₙ}.
Since the limit-circle property is independent of the spectral parameter
(Weyl), for **every** channel n, **every** solution u of
`(h₁ − (±i − Eₙ))u = 0` is L², and a two-line distributional computation
gives `H*(u⊗φₙ) = ±i(u⊗φₙ)`, i.e. `u⊗φₙ ∈ ker(H* ∓ i)`. Orthogonality
across n ⇒ **deficiency indices (∞,∞)** (2 per channel for a two-ended
escape; (2M,2M) in an M-channel truncation). ∎
**Consequence:** the conservative completions are parametrized by
unitaries between infinite-dimensional deficiency spaces — a genuine
**S-matrix at infinity**, including completions that scramble the
transverse state on reflection.

### Theorem B — central malicious potentials in ℝᵈ

`−½Δ − c|x|^α`, α > 2: partial-wave separation reduces to radial channels
whose effective potentials differ by subquadratic centrifugal terms ⇒
each channel is limit-circle at infinity ⇒ deficiency indices (∞,∞). ∎

### Theorem D — non-separable channel mixing, rigorously

`H = ½p₂² − |x₂|^α + h_⊥(x₁) + μ f(x₁)g(x₂)` with f, g **bounded**, α > 2:
a bounded symmetric perturbation preserves deficiency indices exactly
(Kato stability), so the indices remain infinite while the coupling
genuinely mixes channels (f odd ⇒ n ↔ n±1). ∎
**Honest boundary:** the physically-arising *unbounded* diagonal couplings
(λx₁²x₂² in the ghost pair, λq₁⁴ in the PU chain) defeat both separation
and relative-boundedness. Whether they preserve infinite deficiency — or
even *restore* essential self-adjointness (a quantum completion, which
Rauch–Reed shows is possible in principle) — is genuinely open. Note the
indefinite-kinetic structure adds a second obstruction: for
`H₀ = h₁⊗1 + 1⊗h_⊥` with h₁ unbounded below, transverse observables are
NOT H₀-bounded (joint spectral cancellations), so the standard
Kato–Rellich transfer fails even for mildly unbounded couplings.

### Numerical fingerprints (M = 4 channels, V₁ = −|x|^{5/2}, bounded
### coupling μ·tanh(x₁)·x₂²/(1+x₂²/10), μ = 0.2)

- **N1 — channel additivity**: wall-regularized level counts in [5,17]:
  measured 34 (L=8) and 37 (L=12) vs channel-sum semiclassical prediction
  `Σₙ∫ T_cross(E−Eₙ,L)/π dE` = 32.3 and 37.1 (3–5%, i.e. ±1–2 levels).
  At μ=0 the spectrum is *exactly* the union of shifted 1D ladders
  (deviation 1e-12).
- **N2 — Kato stability visible**: switching the coupling on (μ: 0 → 0.2)
  shifts individual levels but leaves the window count unchanged
  (34 → 34, 37 → 36).
- **N3 — the S-matrix at infinity (star demo)**: a channel-0 packet slides
  out, reflects off the regulator, and **returns as a channel mixture
  whose content depends on where "infinity" was regularized**:
  fractions (n = 0..3) = (0.583, 0.346, 0.058, 0.014) for L=6 versus
  (0.401, 0.421, 0.143, 0.035) for L=9, with 96%/93% of the probability
  returning and revival times tracking the classical round trips
  (arrivals 0.88/1.06). The completion doesn't just choose a reflection
  phase — it chooses how the transverse state is scrambled.

### Upshot for the program

1. Both sides of the transient/explosive dichotomy are now theorem-level
   for their model classes: quadratic/transient ⇒ rigorously unique and
   conservative (Theorem C); channelized malicious ⇒ rigorously infinite
   deficiency (Theorems A, B, D).
2. In multi-D the trilemma's second horn gets much worse: conservative
   completions of a malicious ghost require an infinite-dimensional,
   channel-scrambling S-matrix at infinity — decoherence-like data
   injected at infinity. The canonical status of the minimal explosive
   (sub-stochastic, §5.2-structured) process is correspondingly stronger.
3. Sharp open problem, precisely delimited: essential self-adjointness of
   the exact quartic-PU Ostrogradski operator and of the λx₁²x₂² ghost
   pair — obstructed by unbounded diagonal coupling + indefinite kinetic
   form; either outcome (infinite deficiency or quantum completion) would
   be interesting.

---

## 2026-07-10 — LITERATURE SWEEP (novelty check; paper updated)

Verdict per result; the paper was amended (8 new citations, attribution
remarks inserted; recompiles clean at 19 pp.):

1. **Dissociation theorem — novelty intact, framing sharpened.** Key prior
   art: Kawabata–Ashida–Ueda, PRL 119, 190401 (2017) — information
   retrieval possible only in the unbroken phase, power-law criticality at
   the EP, and a unitary-embedding ("hidden entangled partner")
   perspective. They did NOT compute divisibility or generators, and work
   with quantum states, not the classical configuration process; no exact
   t_c/floor forms; no terminal-vs-recurrent structure. Also:
   divisibility- vs information-flow-Markovianity are known to be
   inequivalent for quantum channels (Chruściński–Rivas–Størmer, PRL 121,
   080407 (2018)) — our contribution is that the dissociation is exact,
   phase-locked, and permanent at the classical process level. Paper now
   cites both and presents the dilation as the process-level counterpart
   of KAU's embedding. No paper found computing P-divisibility/generator
   negativity of the PT dimer's conditional process.
2. **K1–K4 — matrix core is classical, as suspected.** Parter–Youngs,
   J. Math. Anal. Appl. 4, 102 (1962); Engel–Schneider, Linear Algebra
   Appl. 7, 301 (1973). Paper now attributes the algebra and claims only
   the beables/detailed-balance/uniqueness/real-spectrum reading.
   Reverse direction cited: Van Wesemael et al., arXiv:2510.09467 (Dyson
   maps restoring detailed balance in classical Markov processes).
3. **Barandes × PT bridge — clear.** Nothing found connecting the
   stochastic-quantum correspondence to non-Hermitian/PT systems.
4. **Ghost/explosion framing — clear, and timely.** Two April-2026 papers
   (Deffayet–Fathe Jalali–Held–Mukohyama–Vikman, arXiv:2604.21823;
   Ewasiuk–Profumo, arXiv:2604.21348) prove interacting-ghost stability
   via conserved quantities / moment bounds — complementary
   (recurrence-enforcing mechanisms in our language); no domain theory,
   explosion, or stochastic reading. Salvio–Strumia, EPJC 76, 227 (2016)
   cited in §6 as the negative-norm-configuration-space alternative. No
   prior essential-self-adjointness/deficiency/Feller treatment of
   interacting PU found.
5. **Skin-effect/K1–K4 follow-up — open.** No beables/ontology reading of
   the skin effect found; non-Bloch methods for classical stochastic
   processes exist (useful related work, not preemption).

Net: all three headline claims survive; attribution is now correct; the
interacting-ghost topic is demonstrably active (two 2026 papers).

---

## 2026-07-10 — THEOREM: the skin effect is the obstruction to fixed beables

Code: `skin_effect_beables.py` (all checks pass; produces
`paper/figs/fig_skin.pdf`). The K1–K4 gauge/continuum question is closed;
the paper gained §3.1 ("Gauge form: the non-Hermitian skin effect is the
obstruction"), Theorem 3.4, Fig. 8, and the Okuma–Kawabata–Shiozaki–Sato
citation (PRL 124, 086801 (2020)). Now 21 pages, compiles clean.

### Gauge-form lemma

K2+K3 ⟺ the couplings can be written uniquely as
`H_jk = t_jk e^{iφ_jk + w_jk}` with `t` symmetric positive, `φ, w`
antisymmetric real — a lattice Peierls substitution `p → p − A − iW` with
real gauge field φ and **imaginary gauge field w** (Hatano–Nelson). K1 =
no on-site gain/loss.

### Theorem (skin obstruction)

1. Fixed beables exist iff the **imaginary flux vanishes through every
   cycle** (Σ_C w = 0 — this is exactly K4). Then `w_jk = χ_j − χ_k` is
   pure gauge, `η = diag(e^{−2χ})` is the exponentiated imaginary gauge
   transformation, and `Γ_jk = e^{2(χ_k−χ_j)}|U_jk|²`. **Real magnetic
   flux is unconstrained.**
2. Classical dictionary: with rates `q(j→k) = |H_kj|`, imaginary flux =
   cycle affinity; zero iff the chain is reversible (Kolmogorov); nonzero
   iff there is a steady-state cycle current. **The skin effect is the
   quantum image of a detailed-balance-violating (irreversible) classical
   cycle.**
3. Hatano–Nelson: a ring with uniform w carries flux Nw ⇒ no fixed
   beables; the PBC spectrum is a complex loop (spectral winding — the
   topological invariant of the skin effect) ⇒ no closed process at all.
   An open chain is a tree ⇒ fixed beables exist at every finite N with
   `d_i = e^{2wi}`; the OBC/PBC dichotomy of the skin effect IS the
   pure-gauge/flux dichotomy.

### Verification (all exact)

- 50/50 random gauge-form graphs with arbitrary real fluxes: constructed
  metric = e^{−2χ} exactly, spectrum real; one quantum of imaginary flux
  through any cycle ⇒ diagonal solution space dim 0.
- HN chain: OBC spectrum = Hermitian chain spectrum to 1e-10; skin
  eigenvectors = e^{−wi} × Hermitian eigenvectors to 5e-15;
  cond(η) = e^{2w(N−1)} to 4 digits at N = 8/16/24/32 — fixed beables
  exact at finite N, exponentially degenerate as N → ∞ (the PU
  unbounded-metric pathology in 1D lattice form).
- HN ring: max|Im E| = 2 sinh w exactly (complex loop).
- Classical ring current: J = −3e-17 at zero imaginary flux, monotone
  nonzero with flux (reversibility ⟺ K4, verified).
- Sub-transition regime (diagonally dominated triangle): binary criterion
  trips at any nonzero flux; beable rotation grows continuously
  (0 → 0.31 for flux 0 → 1.5).

---

## 2026-07-10 — PU-DEFICIENCY EVIDENCE CAMPAIGN (Open Problem 9.6)

Code: `pu_deficiency_evidence.py`. Design: Fock-space (Hermite)
compression as the regulator (regulates position AND momentum — the PU
escape accelerates without bound — and avoids lattice doublers from
p₁q₂; a mode-1 Fourier rotation makes the quartic PU real symmetric);
diagnostic = matched-eigenvalue drift between successive truncations,
measured relative to local spacing in a window near E = 0; calibrated on
known 1D operators; verdicts required to be robust under a basis-scale
change.

### Calibration (window E ∈ [5,15])

- discrete e.s.a. (`p²/2 + x⁴`): drift ratio exactly 0.000 ✓
- continuous e.s.a. (`p²/2 − x²`): ratio → ~0.15, spacing shrinking ✓
- limit circle (`p²/2 − x⁴`, indices (2,2)): spacing saturates, ratio
  stays O(1) erratically forever (0.54, 2.02, 0.42, 0.77) ✓ — the Fock
  analog of the sweeping-wall diagnostic.
- free PU (e.s.a. by the quadratic/Nelson theorem): the 2D baseline:
  ratio ~0.15–0.3, spectrum densifying, old states persisting ✓.

### Verdicts (N per mode = 24…48)

1. **Quartic PU (λ = 0.05): limit-circle-like — evidence AGAINST
   essential self-adjointness.** Drift ratios 1.21, 0.85, 0.79, 1.57
   (basis scale ν₁ = 1.0) and 0.34, 0.98, 0.98, 1.96 (ν₁ = 0.7):
   persistently O(1), NOT decaying with N (largest at the finest
   truncation), ~5× the free-PU baseline computed with identical
   machinery minus the quartic term. The window spectrum reorganizes
   completely between truncations at both basis scales. Evidence that
   the explosion dictionary applies to the physical Mannheim operator
   with (presumably infinite) deficiency indices.
2. **Ghost pair λ = +0.05: quantum-complete, as predicted.**
   Born–Oppenheimer channels W_n(x₂) = ½ω₂²x₂² − (n+½)√(ω₁²+2λx₂²) are
   all confining (quadratic dominates); drift ratios 0.07–0.28 = e.s.a.
   baseline. Prediction → confirmation.
3. **Ghost pair λ = −0.05: SURPRISE — looks quantum-complete despite
   classical maliciousness.** Transverse collapse beyond x₂ = 3.16 and
   classical finite-time escape, yet drift ratios 0.22–0.29,
   indistinguishable from λ > 0. Either diagnostic insensitivity at
   these truncations, or a genuine **Rauch–Reed-type quantum
   completion**: the escape valley is a narrow diagonal channel that
   zero-point energy may wall off. If real: *interactions can
   quantum-cure a classically malicious ghost* — the most interesting
   single finding of the campaign. Tentative; needs larger truncations
   and a valley-resolved (adapted-basis) diagnostic.

### Caveats

Evidence, not proof (no finite computation decides a domain question);
the drift diagnostic's regimes are empirical calibrations; the λ<0
verdict in particular is sensitive to whether N ≤ 48 resolves the
escape valley. The quartic-PU verdict is the strongest (two basis
scales, growing-with-N signal, clean e.s.a. control on the same
operator family).

---

## 2026-07-11 — CONTINUATION 1: exact channelization of the quartic PU

Code: `pu_bo_channels.py`. Open Problem 9.6 advanced from "drift
evidence" to "structural argument + confirmed sign prediction".

### Proposition (exact displaced-oscillator channelization)

In the Fourier-rotated rep (p₁→y, q₁→−p_y), with
`U = exp(−iyp₂/(γΩ))`:
`U(H_PU + λq₁⁴)U† = T(p_y + p₂/(γΩ)) + p₂²/2γ + (γΩ/2)q₂² − y²/(2γΩ)`,
`T(p) = λp⁴ − (γω̄²/2)p²`. **Exact** (hand algebra + Fock-space check via
the terminating BCH series, residual 1.3e-9; note: a naive expm-based
check fails at truncation — displacement operators aren't banded — the
BCH form is the right numerical test). Channel-diagonal part in the
k = p_y representation = **minus** `p̂²/(2γΩ) − λk⁴ + (γω̄²/2)k²`;
interchannel couplings degree ≤ 3 in k (subordinate).

- **λ>0: every channel limit-circle** (channel time of flight 1.74 +
  convergent tail) ⇒ channel-additivity argument for indices (∞,∞).
  Gap to rigor: deficiency stability under the subordinate degree-3
  couplings.
- **λ<0: every channel confining** ⇒ predict quantum completion —
  despite classical finite-time blowup at BOTH signs.

### The sign prediction tested (drift diagnostic)

- Quartic PU λ=−0.05: ratios 0.46, 0.26, 0.36, 0.37 (ν₁=1.0) and 0.17,
  0.33, 0.35, 0.38 (ν₁=0.7): near e.s.a. baseline, sharply separated
  from λ=+0.05 (0.79–1.96). **Prediction confirmed** — the strongest
  evidence yet, being differential (same operator family, same
  diagnostic, opposite verdicts as predicted).
- Extended truncations: λ=+0.05 stays LC-like at N=48→64 (ratios 3.77,
  1.06); ghost pair λ=−0.05 stays at baseline (0.49, 0.32).
- Verdict picture: λ>0 quartic PU escapes through MOMENTUM space along
  LC channels (deficiency); λ<0 quartic PU and λ<0 ghost pair are
  Rauch–Reed quantum-completion candidates (classical escape walled off
  quantum mechanically).

Paper: Proposition 9.7 added to §9 with the confirmed prediction;
`pu_bo_channels.py` in code availability.

---

## 2026-07-11 — CONTINUATION 2: topological classification of the
## skin obstruction

Code: `skin_topology_beables.py`. Paper: Corollary 3.5 added to §3.1.

**Corollary.** For gauge-form couplings, the fixed-beable obstruction is
the class of the imaginary gauge field in H¹(G, ℝ): imaginary FIELD
STRENGTH must vanish through every contractible cycle (no imaginary
magnetic flux — a pointwise condition band-language winding does not
see) and the imaginary HOLONOMY through every non-contractible one (on a
d-torus: ℝ^d of windings, matching the multi-directional skin
classification).

Verified: 3×4 torus — diagonal-metric dim 1 iff (wind_x, wind_y, plaq)
= (0,0,0); each of the three obstructs alone. Cylinder — winding along
the open direction is gauge-removable, periodic direction obstructs
(obstruction lives in H¹ of the actual geometry). **Z₂-type ladder** —
two opposite HN chains (net winding zero, the doubled/Kramers structure
of the Z₂ skin effect): uncoupled dim 2 (metrics e^{±2wi} per chain);
any reciprocal rung coupling ⇒ dim 0 via inter-chain cycles of
circulation 2w (and, in this instance, complex eigenvalues too): **the
beable obstruction detects the doubled skin structure that net winding
misses.** (Side observation for future work: non-gauge-form couplings —
e.g. complex-symmetric hoppings of reciprocal skin classes — are
obstructed at the pairwise level K3, so the full obstruction is graded:
K1 gain/loss ⊕ K3 non-gauge phases ⊕ K4 = H¹ class.)

---

## 2026-07-11 — GAP CLOSED (finite-channel): deficiency stability theorem

Code: `gap_closure_channels.py`. Paper: Theorem 9.8 added after Prop 9.7.

**The observation that closes it:** the PU interchannel couplings are
NOT generic subordinate couplings — `T(k𝟙 + cP₂)` is a polynomial in the
single Hermitian operator P₂, so it is EXACTLY diagonal in the constant
(k-independent) eigenframe of the truncated P₂,M (simple eigenvalues p_ν
= scaled Gauss–Hermite points). No Levinson asymptotics needed.

**Theorem (finite-channel deficiency stability).** For every M, the
M-channel Galerkin model
`S_M = p̂²/(2γΩ) − T(k𝟙 + cP₂,M) − √Ω(N+½)|_M` (λ>0) has deficiency
indices (2M, 2M).
*Proof:* exact frame decoupling into scalar branches
`p̂²/(2γΩ) − T(k + cp_ν)` — each limit-circle at both ends (R–S X.10),
contributing (2,2) — plus the rotated channel-energy matrix, a CONSTANT
BOUNDED Hermitian perturbation, which preserves deficiency indices
(Kato, relative bound 0). ∎

**Verification (all pass):**
- Frame identity: eig(−T(k𝟙+cP₂,M)) = −T(k+cp_ν) to 1.3e-13; the exact
  Fock compression differs from the Galerkin model ONLY on the top ~4
  channels (0.00e0 on the bulk, O(13) on the edge at k=3.7, M=8).
- Falsifiable consequence: with couplings ON, the wall-regularized level
  density equals the all-2M-branch sum Σ_ν T_cross,ν/π: count-based
  spacing matches the prediction at every (M, L) tested (M=1: 1.33 vs
  1.30; M=2: 0.67 vs 0.66; M=3: 0.44 vs 0.45; etc.). Statistics note:
  the MEDIAN gap is biased low where the ±p_ν branch ladders lock into
  near-degenerate parity doublets (M=2 at small L) — count-based density
  is the right statistic.
- Regulator sweep (M=2): the eigenvalue nearest E never converges (LC
  behavior of the coupled system).

**Remaining (sharply delimited, full operator only):** channel-tail
control as M→∞ — the exact compression's top-4-channel edge terms, and
decay of deficiency vectors in channel number. Structurally: the full
operator is a direct integral of LC fibers over spec(p₂) coupled across
fibers by the transverse oscillator (a hybrid of Theorem-A summands and
a fiber-kinetic term). This, plus the rigorous status of the two
quantum-completion candidates (λ<0 quartic PU, λ<0 ghost pair), is what
a specialist would take up.

---

## 2026-07-11 — COMPLETION CANDIDATES: rigorous status + mechanisms

Code: `completion_candidates.py`. Paper: Corollary 9.9 (sign dichotomy)
+ mechanisms paragraph added to §9.

### Corollary (sign dichotomy at every finite channel number) — RIGOROUS

For λ<0 the Theorem-9.8 frame decoupling gives confining branches
`p̂²/(2γΩ) + |λ|(k+cp_ν)⁴ + O(k²)` — each e.s.a. — plus the bounded
rotated channel-energy term (Kato–Rellich): every finite-channel
Galerkin model of the λ<0 quartic PU is essentially self-adjoint. So at
every M: indices (2M,2M) for λ>0, (0,0) for λ<0.
Verified: λ<0 wall spectra converge exponentially (matched drift 2.9e-8
at L 6→8, then 1.1e-13 at 8→10) — maximal contrast to the λ>0 sweep.

### Null-escape analysis: one confirmation, one falsification

Kinetic-form ratio on the escaping momentum (0 = null, 1 = definite),
tracked along actual blowup trajectories at amplitudes 1e2…1e5:
- PU λ>0 (deficiency case): 0.94 → 0.9997 — DEFINITE ✓ (as computed
  analytically: p_u ~ 24γAτ⁻⁵ dominates).
- Ghost pair λ<0: 0.066, 0.014, 0.021, 0.063 — NULL ✓ (diagonal escape,
  p₁² − p₂² ≈ 0): structural rationale for quantum completion (no
  definite-kinetic WKB transport along a null direction).
- **PU λ<0: 0.35 → 0.9998 — FALSIFIES the naive "completion ⇔ null
  escape" conjecture.** Mechanism identified: it climbs a RISING
  potential using negative kinetic energy while hugging u = −cv — i.e.,
  escapes through arbitrarily high mode-2 channels: exactly the channel
  tail the Galerkin models exclude. Two distinct completion mechanisms:
  null-direction escape (ghost pair) vs channel-tail escape (λ<0 PU),
  the latter more tail-sensitive.

### Valley-adapted drift test (λ<0 ghost pair) — verdict robust

Rotated (s,d) Fock bases aligned with the escape diagonal,
(ν_s, ν_d) ∈ {(1,1), (0.5,1.5), (0.3,2.0)}: drift ratios 0.16–0.45 in
all cases, interleaving the free (λ=0, e.s.a.) control's range
(0.09–0.30); nothing near the LC band (0.8–3.8). The completion verdict
is not a basis artifact.

---

## 2026-07-11 — THE M→∞ TAIL: no-compact-witness theorem, 1D certified,
## 2D reduced to fiber-vs-ridge

Code: `tail_certificate.py` (closure-defect diagnostic; original
certificate design corrected) and `glued_certificate_1d.py` (genuine
certificate). Paper: Proposition 9.11 + Remark 9.12 + status paragraph.

### The conceptual result (found by falsifying my own design)

**No compact witnesses.** For any symmetric operator on C₀^∞ and any
Im z ≠ 0, EVERY compactly supported smooth ψ lies in D(S̄), where
‖(S−z)ψ‖ ≥ |Im z|‖ψ‖ holds unconditionally. So no truncated, windowed,
or lattice-regularized function can ever witness deficiency — the
completion data lives entirely at infinity (the domain-side twin of the
S-matrix-at-infinity picture). Consequence: ALL truncation-based
diagnostics (drift, spectra, windows — everything we and anyone else
can run on finite data) are evidence in principle, never proof. My
first certificate design violated this and the numerics faithfully
enforced the bound (all ratios ≥ 1) — theorem as bug-detector.

### The genuine certificate (1D, machine-checked)

Glue WKB tails (only residual: the explicit remainder
a[q″/4q − (5/16)(q′/q)²]) to an exactly integrated interior, C¹ at the
junction: non-compact candidate in D(S*). Results:
- falling quartic (the PU fiber): ratio = **0.0011** ≪ 1 —
  **CERTIFIED not essentially self-adjoint** (von Neumann inequality
  violated by three orders of magnitude).
- confining control: left continuation contains a non-L² real
  exponential — no candidate exists (correct failure).
- falling quadratic (LP-marginal): growing branch polynomial k^{Z/1.12},
  non-L² for Z > 1.12 — no candidate (correct, sharp failure).

### The 2D status (closure-defect diagnostic + reduction)

Windowed 2D candidates measure proximity to the forbidden bound:
falling-channel class hugs it (all five λ>0 beam launches: 1.21–1.29;
1D LC control 1.22), e.s.a. class sits far above (1D confining 4.9;
2D λ<0 control **641**). Evidence-grade: λ>0 behaves LC-like, λ<0
e.s.a.-like, consistent with everything prior.

**Proposition (direct-integral).** The oscillator-free part
A = P̂_k²/(2γΩ) − T(k+cp₂) commutes with p₂: direct integral of LC
fibers, n±(A) = ∞ (rigorous). The full operator adds the transverse
oscillator — unbounded in this frame (Galerkin norms √Ω(M−½) → ∞):
the exact form of the tail question.

**The reduction.** The potential ridge p ≈ −k/c falls only
QUADRATICALLY (limit-point-marginal); fixed-p fibers fall quartically
(LC); beams drift ridge-ward at dp/dk = O(1). A 2D certificate needs
analytic beam tails under the ridge drift: **the fiber-vs-ridge
competition is the mathematical heart of the M→∞ question** — now
precisely what a specialist must resolve, with the 1D machinery
validated end-to-end as the template.

---

## 2026-07-11 — MASLOV FEASIBILITY STUDY: the 2D certificate is
## assembly, not new mathematics

Code: `maslov_feasibility.py`. Paper: feasibility paragraph added to §9.

### Setup insights (before computing)

- In the null-frame (s,w) coordinates the ray equations of the symbol
  reduce EXACTLY to the quartic-PU law s⁗ + γΩs̈ + γω̄²s = 4λs³: the
  escape-ray family IS the classical blowup, with universal amplitude
  S = √(30γ/λ) — a sharp numerical check.
- Time-reversal symmetry ⇒ rest-data rays are DOUBLY explosive (escape
  at both temporal ends) ⇒ the time-integral quasimode
  ψ = ∫e^{izt}φ_t dt has only e^{−Zt*} ≈ 1e-14 boundary terms.
- My earlier "ridge-drift obstacle" applied to artificial fixed-p beam
  launches; true rays don't drift off themselves — beams follow rays.

### Results (all criteria computed)

- **F1**: exponent −1.999; amplitude 24.546/24.547/24.547/24.545 vs
  √600 = 24.4949 (0.2% = finite-s harmonic correction), at four launch
  points, both time directions ✓. (Two numerical traps fixed en route:
  event-time ≠ true t* biases naive exponent fits — extract t* from the
  exact linear law 1/√s = (t*−t)/√S; and the Schur-complement
  transverse curvature is noise-dominated when Im M degenerates along
  the flow — use the second eigenvalue + flow-alignment check.)
- **F2**: Siegel positivity holds along the whole ray (min eig −7e-11 =
  numerical zero, null direction aligned with flow to 1.0000 — benign);
  transverse curvature stays positive (min 1.0e-4), strong terminal
  focusing (σ⊥ = 5.3e-3 at the escape end); zero caustics.
- **F3**: |det δq| ~ τ^{−3.1} ⇒ beam-norm integrand ~ τ^{3.1} → 0:
  N = 0.0824 at Z=6, converged. Anharmonic residual proxy
  η = |U_sss|σ³/(|U|+Z): weighted integral 0.026, decaying fast along
  the escape; η fails (peak 8.2e3) ONLY in a compact interior episode
  of transverse defocusing.

### Verdict

The escape-ray family supports L²-transportable Gaussian-beam tails
exactly where the certificate needs them (the asymptotic ends); the
single-Gaussian ansatz breaks only on a compact interior segment —
which is precisely what the validated 1D template handles by exact
numerical solution. **The 2D glued certificate architecture: numeric
interior (compact) + Gaussian-beam tails along the numerically known
rays + gluing where η is small. Remaining work is assembly and
quantitative error control, not new asymptotic machinery.** All beam
data (t*, S, curvatures, widths, det-exponent, N, η-profile) are
computed and reproducible for whoever assembles it.

---

## 2026-07-11 — FINAL AUDIT + SECOND REFERENCE SWEEP

Full read-through of main.tex (all ~1700 lines) + reference sweep for
the newest material. Findings, all fixed:

1. **Front matter staleness**: abstract and intro item 8 predated the
   last five results — extended to cover channelization + sign
   prediction, finite-channel stability + sign dichotomy,
   no-compact-witness principle, 1D glued-tail certificate, Maslov
   feasibility reduction.
2. **Formatting**: two `\end{figure} Text` jams (Secs. 6 and 7) fixed;
   local-notation note added to the terminal-indivisibility theorem
   (c, σ, p, q, r reused there); outlook updated to state the
   assembly-only reduction; remaining overfulls are 3.7pt and 0.6pt
   (sub-visible).
3. **Bibliography usage**: all entries cited ✓ (34 → 36 after sweep).
4. **Reference sweep finds**: (a) Ralston, MAA Studies in Math 23,
   206 (1982) — the standard Gaussian-beam citation, now cited in the
   feasibility paragraph; (b) **Fischer–Burgarth–Lonigro, J. Phys. A
   59, 255203 (2026)** (arXiv:2508.09044): deficiency indices of
   higher-order squeezing (polynomial-oscillator) operators, including
   cases where added terms RESTORE essential self-adjointness — an
   operator-theoretic precedent for completion-by-interaction, cited
   next to the Open Problem. Nothing found preempting the main claims.
5. **Authorship/AI disclosure**: "we" is the standard authorial
   convention (kept); an Acknowledgments section added disclosing
   extensive AI (Claude/Anthropic) assistance — user may rephrase.

Final: 25 pages, clean compile, submission-grade front-to-back.

### Program status

Sixteen results. Handoff to the physicist reviewer:
1. 2D certificate: architecture + all beam data supplied
   (`maslov_feasibility.py`); assembly/error-control remains.
2. Rigorous e.s.a. for the two completion candidates (λ<0 PU:
   channel-tail escape; λ<0 ghost pair: null-direction escape) —
   genuinely open, mechanisms identified.
- Paper: 25 pp., all claims labeled theorem / certified / evidence;
  review-ready.

---

## 2026-07-11 — FOLLOW-UP THREAD: the QFT bridge (theory stage)

Post-v1.0 work; the released paper is frozen. Question (paper's
Outlook, item 2): does "the ghost is an explosion problem" survive the
passage to QFT vacuum decay?

### Literature anchors (all verified by web search 2026-07-11)

- **Carroll–Hoffman–Trodden**, PRD 68, 023509 (2003)
  (astro-ph/0301273): phantom (ghost) dark energy vacuum decays into
  positive-energy matter + negative-energy phantoms; "the decay rate
  is naively infinite because there is no boundary to the allowed
  phase space"; a ~10⁻³ eV momentum cutoff keeps the vacuum alive for
  the age of the universe.
- **Cline–Jeon–Moore**, PRD 70, 043543 (2004) (hep-ph/0311312), "The
  phantom menaced": vacuum → ghost pairs + photon pairs through
  GRAVITY alone; divergent final-state phase-space integral; only a
  LORENTZ-VIOLATING UV cutoff Λ tames it (Λ ≲ 3 MeV from the cosmic
  gamma-ray background); "theories of ghosts with a Lorentz-conserving
  cutoff are completely excluded."
- **Gross–Strumia–Teresi–Zirilli**, PRD 103, 115025 (2021)
  (arXiv:2007.05541), "Is negative kinetic energy metastable?": the
  divergence is an integral over the NON-COMPACT LORENTZ BOOST ORBIT
  of the final state; whether this means fast decay or exponentially
  suppressed (metastable) decay is NOT settled; they argue
  metastability up to cosmological times is possible.
- **Novelty check**: no prior work found connecting ghost vacuum decay
  to Markov explosion / instantaneous states / non-conservative
  minimal semigroups. The bridge below appears to be new.
- **Probability side (standard)**: a birth-type continuous-time Markov
  chain with rates λ_n explodes (infinitely many jumps in finite time,
  mass exits the state space) iff Σ 1/λ_n < ∞ (Feller); a state with
  TOTAL exit rate q = ∞ is an *instantaneous state*, and no honest
  (stable, standard) Markov process exists with one.

### The bridge

Configuration space: Fock occupation configurations n = {n_k} over
momentum modes (countable at finite volume + cutoff) — beables in the
Barandes sense. At lowest order the effective dynamics out of a
configuration is a jump process with golden-rule rates; the
regulator-independent object is the MINIMAL semigroup (paper §8).

**B1 (dictionary extension — time of flight has a Fock-space
sibling).** The 1D dictionary's classical integral T = ∫dx/√(2(E−V))
= Σ(sojourn times to infinity) has the exact jump-process image
T_Fock = Σ_n 1/λ_n = expected time to reach infinite occupation.
Explosion ⇔ T_Fock < ∞ is Feller's criterion — the same "finite total
time to infinity" statement in the fourth currency. (QM cross-check:
the quadratic cascade grows coherently, ⟨n⟩ = sinh²(gt), classical
field-space escape time = ∞ → transient ✓ matches Theorem-C
uniqueness; the malicious quartic has field-space T < ∞ → explosive ✓.
The coherent/incoherent distinction matters: naive golden-rule ladder
rates λ_n ∝ n² for the two-mode cascade would wrongly predict
explosion — the incoherent-jump reduction is only valid with a dense
final-state continuum, i.e., genuine QFT, not two isolated modes.
This validity condition must be stated honestly in any writeup.)

**B2 (the Lorentz-invariant ghost vacuum is an INSTANTANEOUS state).**
CJM's divergence, read stochastically: the vacuum's total exit rate
q_vac = Σ_channels (finite per-channel rates) diverges because the
channels form a non-compact Lorentz-orbit family. q = ∞ is precisely
the instantaneous-state pathology: NO Markov process — conservative,
minimal, or otherwise — exists. This is strictly WORSE than the QM
malicious case (explosive: finite nonzero t*). The QM → QFT passage
upgrades the pathology: explosion (t* > 0) → instantaneity (t* = 0⁺),
driven not by faster per-channel escape but by infinite channel
multiplicity — the field-theoretic image of the deficiency channel
count going from (2M,2M) → (∞,∞) → continuum-per-unit-volume.

**B3 (the cutoff is conservativity data, and it must break Lorentz).**
A UV cutoff compactifies the channel orbit → q < ∞ → the minimal
process exists again (explosive or transient by B1). CJM's "no
Lorentz-conserving cutoff" becomes: *the data needed to make the ghost
vacuum a valid stochastic process cannot be specified
Lorentz-invariantly* — the same structural statement as the paper's
"conservative completions are an S-matrix at infinity, data not
contained in H," now with the twist that in QFT even the MINIMAL
process needs regulator data (because instantaneity, unlike explosion,
kills the minimal semigroup too). Choose: Lorentz invariance or a
well-defined process on the beables — not both, for a coupled ghost.

**B4 (the CJM ↔ GSTZ dispute is a sharp dichotomy in this currency).**
The open QFT question "fast decay vs metastable" is exactly: does the
boost orbit contribute CHANNEL MULTIPLICITY (distinct final
configurations ⇒ rates add ⇒ q = ∞ ⇒ instantaneous) or GAUGE
REDUNDANCY (boost-related finals identified / measure-zero overlap ⇒
finite physical rate ⇒ transient/metastable)? The stochastic framing
does not resolve the dispute but states it as a single binary question
about the configuration space — which configurations are distinct
beables — rather than about regularization technique. Note the
resonance with the paper's H¹ theme: what must be quotiented is a
group orbit.

**B5 (trilemma, QFT edition).** The paper's trilemma survives with
sharpened horns: (i) minimal explosive process — now requires Lorentz
violation even to EXIST (B3); (ii) conservativity via S-matrix at
infinity — now an infinite-dimensional reflection law per unit volume;
(iii) exit the sample space (PT/no-ghost quantization) — unchanged,
and now visibly the only Lorentz-invariant option on the menu, at the
price of no configuration-space probability at all. This may be the
sharpest available statement of what Mannheim's program is buying.

### Stage-2 numerics (planned, laptop-scale)

1. Mode-scaling: 1+1D lattice ghost+normal fields, N modes; classical
   field-space escape time vs N (does inf over escape family → 0?);
   total quantum leak rate vs N (extensive = transient per volume vs
   super-extensive = instantaneity fingerprint).
2. Rate-growth dichotomy at QM level: engineered ladders with
   λ_n ~ n^α — verify explosion onset at α > 1 (Feller) with the Fock
   drift/leak machinery; the malicious quartic should sit in the
   explosive class via its ladder image.
3. Boost-orbit toy: non-relativistic stand-in for channel multiplicity
   (couple the escape to a k-continuum of transverse channels with
   flat measure) — watch q_vac diverge with channel count.

### Caveats

Perturbative (golden-rule) reasoning where CJM/GSTZ are perturbative;
the instantaneous-state statement B2 inherits whichever side of the
B4 dichotomy is true — B2 is CJM's horn, stated sharply, not a
resolution; no gravity constraints; 1+1D toys only at stage 2.

---

## 2026-07-11 — QFT BRIDGE STAGE 2: numerics (all four experiments)

Code: `qft_bridge_stage2.py` (~2 min). All four signatures came out as
designed; E4's verdict is the one genuinely new datum.

**E1 (Feller onset, the V4 diagnostic transported to Fock space).**
Pure-birth ladder λ_n = n^α, absorbing top N ∈ {200…1600}, absorbed
mass at t=6:
- α=0.8: 0.0000 at every N; α=1.0 (Yule, marginal): 0.61 → 0.02,
  decaying with N — regular;
- α=1.25: 0.961/0.954/0.947/0.941 and α=1.5: 0.988/0.987/0.987/0.987 —
  **N-independent absorption ≈ 1 = explosion**, exactly the
  box-independence signature of `explosion_theorem.py` V4.

**E2 (the paper's dichotomy IS Feller's).** Ladder exponent
α_eff = d log ṅ / d log n: identity α_eff = 1 + 1/m for algebraic
blowup n ~ (t*−t)^{−m}, = 1 for exponential growth. Measured:
quadratic cascade slope 1.0000 (transient/marginal ✓); classical
quartic-PU blowup slope 1.1720 vs predicted 7/6 = 1.1667 (energy
proxy n ~ τ^{−6}) ✓ explosive. One-line lemma worth keeping:
*finite-time blowup ⇔ α_eff > 1 ⇔ Feller explosion of the ladder
image* — the growth LAW, not the growth amount, decides.

**E3 (channel multiplicity vs orbit measure — B4 made concrete).**
Vacuum coupled to M flat quasi-continua (g=0.02, band ±8, ρ=10,
Γ₁ = 0.0253, exact eigendecomposition up to dim 5153):
- flat measure (boost-orbit stand-in): fitted Γ = 0.0252, 0.0504,
  0.1009, 0.2027, 0.4088, 0.8302 for M = 1…32 vs prediction M·Γ₁ =
  0.0253…0.8093 — **within 3% throughout, unbounded growth**: the
  instantaneous-state trend (CJM horn);
- decaying measure g_k = g e^{−k/4}: Γ converges to 0.0640 vs
  predicted plateau 0.0643 (GSTZ/metastable horn).
Channel counting is the entire difference; with a finite band the
flat case would eventually hit the hybridization ceiling Γ ~ W
(observed in a first run with Γ ≈ W — kept as a methodological note:
golden-rule fits need Γ ≪ bandwidth ≪ recurrence).

**E4 (classical lattice vacuum decay vs UV cutoff — SUPPRESSED, not
divergent).** φ (normal) + χ (ghost) on N sites at FIXED volume
L=32, coupling 2λφ²χ² in the eqs (λ=0.25), vacuum-mimic zero-point
initial data, absolute energy-transfer threshold ΔE_φ = 25, median
ensemble times:
- N = 8/16/32: t_thr = 106/64/46 (rate rising with cutoff);
- N = 64: t_thr = 149 — rate DROPS ~3×. Confirmed with an
  independent seed and 16 samples: N=32 median 55.9 [45.3, 68.2] vs
  N=64 median 158.9 [120.9, 194.2] — non-overlapping quartiles.
- λ=0 control: no growth at any N ✓.
**Verdict: the classical zero-point cascade is UV-finite — even
UV-suppressed.** Plausible mechanism (conjectural): self-consistent
effective-mass shifts m_φ² += 2λ⟨χ²⟩, m_χ² −= 2λ⟨φ²⟩ grow with the
cutoff (⟨φ²⟩ ~ log Λ in 1+1D) and detune the φ↔χ pair resonance.
Consequence for the bridge: the instantaneity danger is NOT visible
in classical lattice dynamics at fixed volume — it lives in the
quantum channel measure (E3), i.e., precisely in the B4 question of
whether the boost orbit counts as multiplicity. Coherent with B2.

### Combined stage-2 statement

The explosion dictionary acquires a verified Fock-space column
(E1+E2); the QFT vacuum question is isolated into a single measured
dichotomy (E3): rate ∝ channel count (no limit) vs rate ∝ measure
(finite) — and the classical field theory (E4) declines to produce
the divergence on its own. What remains for a real QFT statement:
compute the golden-rule channel measure of the actual boost orbit
(relativistic 2-ghost + 2-photon final states) and decide
multiplicity-vs-redundancy — a calculation, not a simulation.

### Caveats

E3 is channel counting without Lorentz kinematics; E4 is classical,
1+1D, median-of-8/16, and the detuning mechanism is unproven;
`qft_bridge_stage2.py` runtime dominated by E4's stiff ensembles.

---

## 2026-07-11 — QFT BRIDGE STAGE 3: the relativistic channel measure

Code: `qft_bridge_stage3.py` (~1 min). The boost-orbit structure of
ghost vacuum decay, computed and numerically verified.

### Theorem (orbit factorization of the ghost vacuum rate)

For vacuum → (normal pair) + (ghost pair) with any Lorentz-invariant
|M|², total 4-momentum zero forces the normal pair's 4-momentum q to
equal the sign-flipped ghost pair's, and (shown in 1+1d; the
structure is general)

  Γ/V = ∫ d²q/(2π)² ρ_n(q) ρ_g(q) |M|²
      = [∫ dη] × (1/2)(2π)⁻² ∫ ds ρ_n(s) ρ_g(s) |M(s)|²,

with ρ(s) the invariant two-body phase-space density and η the pair
rapidity. The first factor — the boost-orbit volume — is INFINITE in
every spatial dimension d; all d-dependence lives in the reduced
∫ds. **Numerical verification (V1, m_n=1, m_g=0.7, contact |M|²=1):**
brute-force integration of the constrained (k1,k2) phase space with
rapidity cutoff |η|<H gives Γ(H)/[H·I_s/(2π)²] = 0.999, 1.000,
1.001, 1.000 at H = 1,2,3,4 (I_s = 0.619222) — linear in the orbit
volume, slope the reduced integral, to 0.1%.

**Self-correction logged:** the stage-1 back-of-envelope "d=1
converges" (scale counting E^{3d−6}) samples a NON-orbit direction
and misses a vanishing Jacobian (v₃ → v₄ van Hove line) along the
boost flow; the orbit-volume divergence is present in d=1 too. The
numerics confirmed the invariance argument over the naive counting.

### Corollary 1 (dimension ladder of the REDUCED measure)

V2, fitted log-log slopes vs the s-cutoff (exact to 3 decimals):
d=1 contact: 0.000 (UV-FINITE reduced integral); d=3 contact: 2.000
(= Λ⁴ in energy); d=3 with the CJM gravitational vertex |M|² ~
s²/M_Pl⁴: 4.000 (= Λ⁸/M_Pl⁴) — **Cline–Jeon–Moore's published
scaling recovered from the orbit-quotiented measure alone.**

### Corollary 2 (E4 coherence)

The classical 1+1D lattice (stage 2, E4) follows single trajectories
— no sum over orthogonal orbit channels — and its rate was UV-finite
/ suppressed: consistent with the d=1 reduced integral's slope 0.
The stage-2 surprise is the quotient-side physics, as it must be.

### Corollary 3 (frame individuation; B3/B4 sharpened)

Members of a boost orbit are distinct outcomes only relative to a
frame (a detector, a bath, a cutoff surface). CJM's conclusion that
only a Lorentz-VIOLATING cutoff regulates the rate is, in this
currency, the statement that the frame which individuates the
channels must be supplied before q_vac is finite: **a coupled ghost
admits a well-defined configuration-space stochastic process only
relative to a preferred frame.** The B4 dichotomy
(multiplicity/instantaneous vs redundancy/metastable) is the choice
of sample space: momentum configurations in a frame vs boost-orbit
equivalence classes. GSTZ metastability = the quotient choice, whose
rate is the reduced integral (UV-finite in d=1, Λ⁴ or Λ⁸/M_Pl⁴ in
d=3).

### Status of paper #2

Theory bridge (B1–B5) + stage-2 numerics (E1–E4) + stage-3 theorem,
corollaries, and verifications now form a complete arc: *the
Ostrogradski ghost's QFT catastrophe is the divergence of a channel
measure over the Lorentz group; whether it is instantaneity or
metastability is the choice of beables; either way the sample space
requires a frame.* Remaining before drafting: (i) check the
factorization statement in d=3 numerically (only d=1 verified);
(ii) read GSTZ §-level to align the redundancy horn with their
actual argument (only the abstract-level claim used so far);
(iii) decide venue/format (letter-length follow-up vs section in a
v2).

### Caveats

Contact-model kinematics; perturbative golden rule throughout; the
d>1 factorization asserted by invariance, verified only in d=1; the
frame-individuation corollary is an interpretation of CJM's result,
not new mathematics; GSTZ engaged only at abstract level so far.

---

## 2026-07-11 — QFT BRIDGE: LITERATURE DEEP READ + ATTRIBUTION
## CORRECTIONS (three parallel full-text reads)

Full-text reads of CJM (hep-ph/0311312), GSTZ (2007.05541), and a
wide sweep. Everything below supersedes the attribution language of
the stage-3 entry.

### CORRECTION 1 — the factorization is GSTZ's, not ours.

GSTZ eq. (88) (quartic coupling, vacuum rate in d spatial dims) is
EXACTLY the [reduced ∫ds] × [divergent boost-orbit ∫dK₀] structure of
our stage-3 "theorem":
  ρ̇₁ ∝ ∫_{4m²}^∞ ds (s−4m²)^{d−2}/s × ∫_{√s}^∞ dK₀ K₀ (K₀²−s)^{d/2−1},
with their diagnosis verbatim: "the vacuum initial state ∅ is now
Lorentz-invariant so that the final state too must be the same in all
frames. This is why the rate contains a dK₀ integral over the
non-compact Lorentz group." CJM's eq. (9) is the regulated special
case (boost capped by formation time γ < t₀√s → Λ¹⁰t₀²/M_Pl⁴; their
Λ⁸/M_Pl⁴ is dimensional analysis under a CMB-frame 3-momentum
cutoff). **Status of our stage 3, corrected: independent rederivation
+ first numerical verification (0.1%, d=1 brute force) of the
GSTZ/CJM decomposition — not a new theorem.** GSTZ is the mandatory
citation for the decomposition; CJM for the Lorentz-violating-cutoff
horn.

### What remains genuinely novel (triple-checked, no prior art found
### under any phrasing)

1. The Markov reading: instantaneous states / Feller explosion /
   minimal non-conservative semigroups applied to ghost vacua; the
   Fock-ladder column of the explosion dictionary (Σ1/λ_n as time to
   infinity); the E1/E2 verifications.
2. Naming the crux: CJM-vs-GSTZ as CHANNEL MULTIPLICITY vs GAUGE
   REDUNDANCY of the boost orbit. GSTZ draw the split only in
   footnote 11 ("other authors regulate the boost divergence ...
   adding a Lorentz-breaking or non-local cut-off"); nobody develops
   it as the decisive question, and nobody ports the bubble
   literature's resolution machinery (below) to ghosts.
3. Frame individuation as a sample-space statement — precedented for
   BUBBLES (Garriga–Kanno–Tanaka 1304.6681: detectors individuate
   the nucleation frame), never applied to ghosts; supported by the
   ghost-condensate mechanism (healthy precisely because the
   background selects a frame).
4. First contact of the stochastic–quantum correspondence with QFT:
   Barandes' corpus is finite-configuration-space throughout and
   explicitly defers infinite ones.

### The decisive map (GSTZ section 5, at equation level)

GSTZ's ladder: classical mechanics = metastable (Nekhoroshev/KAM
"spontaneous lockdown", exponentially long); QM = metastable
(ground-like state, exponentially small outgoing flux, "analogously
to usual tunnelling"); CLASSICAL field theory = NOT metastable
(resonances destroy the hidden invariants; no thermal equilibrium —
ghost temperature T₂<0, entropy grows forever; drift ∝ λ²,
polynomial, lattice-verified); QFT = OPEN: "we do not know the true
rate." Their hoped-for resolution: the V-instability precedent —
Zeldovich/Kobzarev–Okun–Voloshin found the SAME divergent boost
integral for ordinary vacuum decay; Coleman (and Garriga–Shlaer–
Vilenkin) resolved it by expanding around the Lorentz-invariant
bounce, the boost integral being "an over-counting of the same
configuration" (redundancy!). For ghosts, no positive Euclidean
action → no bounce formulation found → question mark in their title
is genuine. They never advocate a preferred frame.

### The bubble-literature precedent (the strongest structural prior)

Kobzarev–Okun–Voloshin (1975) → Coleman (O(4) bounce: boost orbit =
stabilizer of the saddle, not moduli) → Dvali 1109.3422 (revival) →
Dine–Draper–Park 1206.5880 (boosted bubble = DIFFERENT process but
amplitude-suppressed like exp(−(ΔE³/S₁)^{1/2}) → sum converges) →
Garriga–Kanno–Tanaka 1304.6681 (detector individuates the frame).
**The sharp new statement available to us: both bubble resolutions —
saddle symmetry and excitation cost — are structurally ABSENT for
perturbative ghost pair creation, where boost-orbit members are
exactly degenerate in |M|. That absence is what makes the ghost
divergence resistant, and is exactly why the sample-space question
(which configurations are distinct beables) is forced.**

### Other load-bearing reads

- Garriga–Vilenkin 1202.1239 (closest metastable-side precedent):
  D=2 Lorentz-invariant rate FINITE, log-growing in time — matches
  our d=1 reduced integral (slope 0) + causally-capped orbit
  (η_max ~ ln t). In D>2: divergent for point vertices, tamed by
  UV-soft NONLOCAL form factors. They accept multiplicity (boost
  integral = real phase space) and tame |M| instead. [To verify at
  equation level before citing: how an invariant form factor
  interacts with the orbit volume — likely via the same causal
  regulator.]
- CJM details: process is vacuum → 2 ghosts + 2 photons via ONE
  virtual graviton; |M|² effectively s²/M_Pl⁴; Λ ≲ 3 MeV from EGRET
  diffuse gamma flux (Eqs. 4–8); "Lorentz-invariant cutoff fails"
  argument = cutting s leaves the boost integral divergent (their
  words); they DEBUNK CHT's specific φ→gφφ process (vertex removable
  by field redefinition; CHT's 10⁻³ eV bound "incorrect") — cite CHT
  qualitatively only.
- Deffayet–Held–Mukohyama–Vikman 2504.11437 (2025): classical 1+1d
  ghost fields can be benign; high-frequency modes MORE stable
  ("heavy high-frequency ghost fields seem to not violate the
  decoupling theorem") — independent support for our E4 UV
  suppression. Held 2509.18049: global stability results.
- GSTZ sec. 4 vs our E4: their thermal classical drift ∝ λ²T₁T₂(...)
  is the THERMAL regime; our E4 is vacuum-mimic amplitudes — E4
  should be positioned as the zero-point analogue, with their
  lattice-verified Boltzmann drift as the calibrated thermal limit.
- Also for paper #2's related-work section: Hawking–Hertog
  hep-th/0107088 (definition-level rescue — same CATEGORY as
  Mannheim's, exits the state space); Könnig et al. 1605.08757
  (heavy ghosts decay slowly even with trans-Planckian cutoff);
  ghost condensate hep-th/0312099 (frame-selection as cure);
  Babichev 2412.20093 (ghost decay = Cherenkov, manifestly
  frame-anchored); Buoninfante 2606.18349 (ghosts vs unstable
  particles: whether "decay" is even the word); Gomes 2605.21689
  (Lindblad-dissipative ghost stabilization — nearest THEMATIC
  neighbor to a stochastic framing, no explosion mathematics);
  Andreassen–Farhi–Frost–Schwartz 1604.06090 (modern Γ/V
  derivation); Kaplan–Sundrum hep-th/0505265; Rubakov
  hep-th/0604153.

### PRECISION FIXES (referee-hardening, soft spots 2 and 4)

**Fix A — the instantaneous-state statement, probabilist-proof form.**
Overstated version (retire it): "q = ∞ ⇒ no Markov process exists."
Correct version: a state with infinite total exit rate is
*instantaneous*; chains with instantaneous states exist (Kolmogorov's
and Blackwell's examples) but are non-standard — no STABLE, standard,
right-continuous realization. For the regulated family with cutoff Λ,
q_vac(Λ) < ∞ and the minimal semigroup exists; as Λ → ∞ the vacuum
survival probability e^{−q_vac(Λ)t} → 0 for every t > 0: **the
minimal object degenerates to instantaneous killing — the process
exists in the limit only as "the vacuum has zero lifetime."** This is
the sharp statement: not nonexistence, but a zero-lifetime beable
state, with the regulator (= frame) the only thing standing between
the theory and that limit.

**Fix B — two distinct pathologies, kept separate.** (i) LADDER
EXPLOSION: exit rates finite everywhere but growing with occupation,
Σ1/λ_n < ∞ — infinitely many jumps accumulate in finite NONZERO time
(the paper-#1 malicious class; E1/E2). (ii) INSTANTANEITY: infinite
exit rate AT the vacuum itself, from summing finitely-contributing
channels over a non-compact orbit — zero lifetime, t* = 0⁺ (the
Lorentz-invariant QFT ghost, on the multiplicity horn). Both are
failures of conservativity, but (i) is a tail phenomenon in
configuration space while (ii) is a local divergence of the Q-matrix;
paper #2 must not let readers conflate them. The QM→QFT passage is:
malicious QM ghosts realize (i); Lorentz-invariant coupled QFT ghosts
threaten (ii); cutoff-regulated QFT ghosts sit between (transient or
explosive by the ladder criterion, with q_vac(Λ) finite).

**Fix C — Born–Markov scope (soft spot 3, the physicist's
objection).** The jump process is DERIVED from the golden rule; the
instantaneity diagnosis is a translation of the divergent
perturbative rate, inheriting its validity and its doubts (GSTZ: "we
do not know the true rate"). The framework's contribution is that the
translation exposes the disputed assumption — whether boost-orbit
members are distinct outcomes — as a statement about the sample
space, not that it independently settles the rate. State this
verbatim-ish in paper #2.

**Fix D — bubble-contrast scope (soft spot 7).** The degeneracy of
orbit members in |M| is a TREE-LEVEL statement. Whether resummation
generates a Dine–Draper–Park-style suppression for ghost pairs is
open — indeed that unknown IS GSTZ's open question restated. Claim
the absence of the bubble mechanisms only at the order computed.

### Paper #2 thesis, sharpened by the read

The ghost QFT question GSTZ left open ("we do not know the true
rate") is, in the stochastic currency, the question of the sample
space: beables = frame-anchored momentum configurations ⇒ the boost
orbit is channel multiplicity ⇒ q_vac = ∞ ⇒ instantaneous state (no
process; CJM's cutoff = the frame that restores one); beables =
boost-equivalence classes ⇒ redundancy ⇒ rate = the reduced integral
(GSTZ's hoped-for Coleman-analogue; UV-finite in d=1 per our slope-0
result and Garriga–Vilenkin's D=2 finiteness). The bubble literature
resolved the same dichotomy toward redundancy USING structures
(Euclidean saddle symmetry, excitation cost) that ghosts lack — so
for ghosts the dichotomy is not a calculation error but a genuine
ontological fork, which is precisely what a beables-first
reformulation is equipped to say. Barandes-side novelty: first
infinite-configuration-space / QFT contact for the correspondence.

---

## 2026-07-11 — THE FOLIATION THREAD (QFT bridge, stage 4 theory)

Soft spot 5 developed. The pieces assemble into the sharpest
statement of the program so far.

**F1 (structural).** A beables-first QFT needs configurations, and
field configurations (or mode occupations) live on SPATIAL SLICES:
choosing the configuration space is choosing a foliation. This is
not a defect peculiar to us — it is the well-known structure of
Bohmian QFT (hypersurface Bohm–Dirac models), and Barandes' own
corpus stays on finite configuration spaces, deferring exactly this
question. So the natural extension of the correspondence to QFT is
foliation-anchored BY CONSTRUCTION, and the B4 dichotomy is answered
structurally within it: relative to its own foliation, boost-orbit
members are distinct configurations — the MULTIPLICITY horn.

**F2 (the equilibrium shield, and where it fails).** Bohmian lore:
the preferred foliation is empirically invisible in quantum
equilibrium (no-signaling); statistical predictions stay Lorentz
invariant though the ontology is not. Our result says exactly where
this shield BREAKS: a coupled ghost sector makes the foliation
OBSERVABLE, because q_vac — and the decay spectrum, isotropic
precisely in the preferred frame, peaked at the cutoff Λ measured in
that frame — depends on the channel individuation. **Ghosts are
foliation detectors.** For healthy sectors the foliation hides; for
ghost sectors it prints itself on a gamma-ray spectrum (CJM's
EGRET bound is literally this measurement, null so far).

**F3 (the vacuum determines no foliation — instantaneity as
foliation-indeterminacy).** DGNSZ (arXiv:1307.1714, Proc. R. Soc. A
2014) propose extracting the foliation covariantly FROM the wave
function — no absolute structure. Apply it here: the Minkowski
vacuum is Lorentz-invariant, so it determines NO foliation. For a
ghost-coupled theory in pure Minkowski, the beables-first process is
therefore ill-posed in a precise dynamical sense — our zero-lifetime
/ instantaneous-killing statement is the DYNAMICAL EXPRESSION of the
foliation's indeterminacy on a Lorentz-invariant state. The
mathematical pathology and the ontological indeterminacy are the
same fact in two languages.

**F4 (the real universe supplies the foliation — CJM's frame choice
is canonical, not ad hoc).** The actual cosmological quantum state
is NOT the Minkowski vacuum: it has a rest frame (the comoving/CMB
frame), so the DGNSZ extraction succeeds and yields the comoving
foliation. Consequence: CJM's decision to impose the cutoff in the
CMB frame — presented by them as a pragmatic choice — is exactly
what a wave-function-determined-foliation beables theory PRESCRIBES.
In this reading: ghost decay in our universe is well-posed, frame =
comoving, rate finite for finite Λ, and the phantom phenomenology
(isotropy of the would-be gamma-ray signal in the CMB frame; a
dipole matching the CMB dipole from any moving detector) is a
direct empirical probe of the preferred foliation. If DESI-era
w < −1 were confirmed AND the CJM signal ever seen with the CMB
dipole — that would be a foliation detection.

**F5 (the pick-two trilemma — the slogan-grade statement).**
  GHOSTS, LORENTZ INVARIANCE, DEFINITE CONFIGURATIONS: PICK TWO.
- ghosts + beables ⇒ preferred foliation (ghost condensate, Hořava,
  CJM's cutoff frame — all existing rescues in fact pick frames);
- Lorentz + beables ⇒ no coupled ghosts (healthy QFT; the foliation
  exists ontologically but hides at equilibrium);
- ghosts + Lorentz ⇒ no beables (Mannheim/PT, Hawking–Hertog:
  definition-level rescues that exit the sample space — the paper-#1
  verdict, now seen as one horn of a three-way trade).
This upgrades paper #1's trilemma from a menu of completions to a
statement about what any ontology of QFT can simultaneously hold.

**Honesty flags (must appear in any writeup).** (a) F1 states the
NATURAL extension of Barandes' framework, not his committed
position — he explicitly defers infinite configuration spaces; other
extensions (e.g., genuinely covariant beables, if constructible)
would evade F1. (b) The equilibrium-shield leg (F2) is imported from
Bohmian analysis; its transfer to indivisible-process dynamics needs
its own proof. (c) F3/F4 apply DGNSZ's extraction idea in a context
they never considered. (d) All of F2–F4 presume the multiplicity
horn, which the beables framing motivates but which fundamental
frameworks without beables can still dispute (GSTZ's hoped-for
bounce). The trilemma F5 is robust to (d): it is a statement about
combinations, not about which is true.

**Next concrete steps for this thread:** (i) check whether the
equilibrium shield (F2) can be proven within the correspondence
(does no-signaling of the indivisible process protect foliation
invisibility for conservative sectors?); (ii) the dipole
phenomenology of F4 (one paragraph of kinematics — decay products
isotropic in the comoving frame, detector moving at 370 km/s sees a
computable dipole); (iii) position against Kawabata–Ashida–Ueda-type
information results if any apply.

---

## 2026-07-11 — GARRIGA–VILENKIN DEEP READ: soft spot 1 RESOLVED;
## the foliation thread gains its third leg

Full equation-level read of 1202.1239 (+ companion GSV 1109.3422).
Classification of their D>2 rescue against our (a)–(e) menu:
**(a) finite-vacuum-age orbit cutoff, with (d) as the phenomenology
step; explicitly NOT frame-dependent form factors, NOT a different
observable.** Details:

1. **They CONFIRM our premise.** Their own Secs. II–III prove a
   Lorentz-invariant form factor cannot cut the orbit: local vertex
   in D=4 diverges linearly in |P| EVEN AT FINITE T (the energy
   defect Ω → 0 along the orbit, so the time window "provides no
   suppression there"); a single-invariant form factor tames the
   orbit only via the T-window, and then the invariant-mass
   integrals blow up instead (their surprise: "energy is not
   conserved because the interaction is switched on and off").
   Full rescue needs BOTH: (i) the vacuum's finite age — creation
   on a spacelike surface Σ, Gaussian window e^{−x₀²/T²}, "this
   surface breaks Lorentz invariance spontaneously" — cutting the
   orbit at P_max ~ μ²t; AND (ii) full LI nonlocality in all SIX
   vertex invariants, which collimates the decay products
   (θ ≲ μ/p_*) and bounds the invariant masses. Result: Γ_total(t)
   ~ 10⁻⁶(μ⁸/M_Pl⁴)(μt)² — finite at every t, GROWING as t²
   (D=2 analog: ln(mT)). "Metastable" = born-and-aging, never a
   constant rate. They explicitly fault CJM for missing the
   essential role of nonlocality, and Kaplan–Sundrum's
   invariant-softening for the s,s′ runaway.

2. **The literature's own criterion for multiplicity vs redundancy**
   (GV footnote 5 + GSV 1109.3422): the boost integral is an
   OVERCOUNTING precisely when the final state is a boost SINGLET —
   the fluctuation-dressed bubble state is boost-invariant, so
   boosts map it to itself (GSV's answer to Dvali, with Schwinger
   pair creation as the controlled prototype). Non-invariant
   perturbative multiparticle finals (ghost + matter with definite
   P) are genuinely distinct channels; the orbit volume is real,
   and only the vacuum's age regulates it. **So the B4 dichotomy is
   not a global ontology switch — the literature resolves it
   state-by-state via the invariance of the final state, and
   perturbative ghost decay sits on the multiplicity side by this
   criterion.** Our beables framing agrees and explains WHY
   (configurations are frame-anchored); the open GSTZ hope is
   equivalent to finding a boost-singlet saddle for ghost decay.

3. **Fix A, refined (the sharpest form of the instantaneity
   statement):** q_vac is infinite only for the ETERNAL
   Lorentz-invariant vacuum. A vacuum with a birth surface Σ has
   finite, growing exit rate (GV's (μt)²; survival
   S(t) = exp(−V∫Γdt) finite for all finite t). **"A
   Lorentz-invariant ghost vacuum can exist only if it was born —
   and its birth certificate is a foliation."** The instantaneous
   state is the eternal-vacuum idealization, exactly the state
   that (F3) determines no foliation.

4. **Foliation thread, third leg (F4').** Every rescue on record
   supplies a frame/foliation somewhere: CJM — CMB-frame momentum
   cutoff; ghost condensate — the condensate background; Hořava —
   explicit; **GV — the creation surface Σ, doing its work through
   "spontaneous" Lorentz breaking by the vacuum's own history.**
   The pick-two trilemma survives every known example: ghosts +
   beables/calculability ⇒ a foliation enters (as cutoff frame or
   birth surface); ghosts + Lorentz ⇒ exit the sample space;
   Lorentz + beables ⇒ no coupled ghosts.

5. Technical notes for paper #2: GV's loop remark (the orbit
   divergence lives in external momenta only — vacuum-energy loops
   cut at μ, so Λ ~ μ⁴ survives); their allowed window μ ≈
   2×10⁻³ eV (gamma-ray cascade bound vs 0.1 mm gravity tests,
   "marginally consistent"); their P_max ~ μ²T dominance in the
   fully nonlocal model is an ESTIMATE, rigorous only in the
   restricted model — flag if we lean on it. Novelty intact: no
   Fock/rate-equation/Markov treatment of the vacuum anywhere in
   GV or GSV.

---

## 2026-07-11 — M3 RUN: who individuates the frame — RESULT:
## a two-epoch structure (state first, regulator ultimately)

Code: `foliation_m3.py` (+ scratch diagnostics). Design: boosted
thermal baths (classical Jüttner n(k)=T/(u·k), traveling-wave
construction so the φ–π correlation carries direction; fixed spectral
support |k| ≤ 1.2 so the STATE is N-independent), ghost bath hotter
(T_χ=2, T_φ=1; GSTZ drift ∝ T₁T₂(T₂−T₁) vanishes at equal T), frame
estimator v* = (dP_φ/dt)/(dE_φ/dt) by regression (kinematic identity:
production isotropic in the state frame ⇒ v* = v exactly,
mass-independent; lattice-anchored ⇒ v* = 0). Self-test: right-mover
P/E = k/ω ✓. Controls: λ=0 → dE/dt = 0.00000 ✓; v=0 → v* ≈ 0 ✓.

**Run 1 (v=0.35, full window to back-reaction guard):** v*(N) =
0.045 / −0.001 / −0.031 / −0.036 for N = 16/32/64/128 (IQR ~ ±0.15)
— consistent with ZERO at every cutoff, rejecting the naive
state-anchored 0.35.

**Run 2 (spectral diagnosis, N=64, t=80 deep cascade):** the
transferred energy is UV-DIRECTED: fractions 0.10 / 0.27 / 0.57 /
0.05 in bands |k|≤1.3 / 1.3–3 / 3–6 / >6 — the classical ghost
cascade (GSTZ sec. 4 turbulence) pumps energy far above the bath
support; and EVERY band shows v*_band ≈ 0 ± 0.1: deep in the
cascade, the state's frame is erased. Even at N=128 the
energy-carrying band sits where lattice dispersion is ~15%
non-covariant: the cascade always terminates in regulator-owned
territory.

**Run 3 (decisive early-window test, v=0.6, t ∈ [3,25]):**
v* = +0.022 [−0.18, +0.22] at N=64 → **+0.230 [−0.01, +0.45] at
N=128** — the EARLY transfer carries the state's frame, more
faithfully as the lattice recedes (bath streaming P/E ≈ 0.2 for
these massive quanta; isotropic-in-state-frame target 0.6; the
measured value sits in that band at N=128 and nowhere near it at
N=64).

### Interpretation (the M3 theorem-shape)

**Two epochs. Early, covariant epoch: the state individuates — the
transfer is comoving with the bath, and better so as the cutoff
recedes (foliation-from-state confirmed where the dynamics is
continuum-covariant). Late, cascade epoch: ghost dynamics is
UV-seeking, the energy runs to the regulator's territory, and the
state's frame is erased — the regulator individuates.** Whoever owns
the UV ultimately owns the frame. This is precisely the dynamical
content of Garriga–Vilenkin's requirement: without UV-softness
(their nonlocality) the state/age frame cannot hold the line against
the cascade; UV-soft couplings are what let the state's frame
survive its own ghost. Our lattice model exhibits the REASON for
their condition. For the foliation thread: F4 ("the cosmological
state picks the frame") holds in the covariant window but is NOT
sufficient in a UV-local theory — the honest statement is
conditional: state-individuation survives iff the ghost coupling is
UV-soft below the scale where the regulator's frame takes over.

### Caveats

Classical 1+1D, one coupling; wide IQRs (16 runs); N=256
unconfirmed (trend N=64→128 is one step); early-window target band
[bath P/E ≈ 0.2, isotropic 0.6] not sharply discriminated within
noise; the two-epoch reading rests on Run 2's spectral bands plus
Run 3's trend — a dedicated scan (v*, band-resolved, vs time and N)
would firm it. Vacuum runs are impossible in principle (the vacuum
cannot be boosted) — which is F3 in experimental form.

---

## 2026-07-11 — E4-2D: THE DIMENSIONAL REVERSAL, CONFIRMED — after
## two caught artifacts and one formal RETRACTION

Code: `qft_bridge_e4_2d.py` (identical leapfrog machinery in d=1 and
d=2; pre-registered prediction in the docstring BEFORE the data:
d=1 flat/suppressed, d=2 growing — the marginal dimension of the
reduced measure ∫dE E^{3d−6}).

### RETRACTION: the E4-1D "UV-suppression" result was an artifact.

The original E4 vacuum construction (`qft_bridge_stage2.py`,
`vacuum_field`) underweights fine lattices: mode amplitudes were
N^{d}/(2ω)-normalized instead of N^{2d}/(2ω L^d), an error of
(N/L)^{d/2} — the zero-point source SHRANK as the cutoff grew, and
the observed "suppression" (t_thr 46→149 at N=32→64, "confirmed"
with independent seed) was the shrinking source, not physics.
Diagnosed by the ⟨φ²⟩₀ column of the new script (fell with N; the
physical vacuum variance must rise — log in d=1, linear in d=2);
verified by the zp≈1.00 self-check after the fix.
**Scope of contamination:** stage-2 E4's verdict ("classical
cascade UV-finite, even UV-suppressed") — RETRACTED, replaced
below; the "self-consistent mass-detuning" conjecture — retracted;
stage-3 "Corollary 2 (E4 coherence)" — superseded (the corrected
d=1 result is coherent with the slope-0 reduced measure via
SATURATION, see below). **Unaffected:** E1–E3 (no field
construction), all of stage 3's phase-space numerics, M3 entirely
(its thermal bath used the explicit per-mode loop, correctly
normalized), and everything in paper #1.
Second artifact caught in the same sweep: at dt·ω_max = 0.5 the
Verlet drift (up to 21 energy units) exceeded the d=2 threshold and
made the λ=0 CONTROL fire at N≥48 — fixed with dt·ω_max ≤ 0.15;
final run has all controls silent and max drift 1.0 vs thresholds
10/25. Methods lesson, banked: the ⟨φ²⟩₀ column caught bug 1, the
λ=0 control column caught bug 2; each alone would have produced a
publishable-looking false trend.

### RESULT (corrected, controls clean)

Classical ghost vacuum decay rate (1/median t_thr to absorb fixed
ΔE) vs UV cutoff k_max = πN/L at fixed volume, vacuum-mimic data:

d=1 (L=32, λ=0.25, ΔE=25):  N=16..128 → rate 0.0127 / 0.0175 /
  0.0242 / 0.0249 — rising then SATURATING (64→128: +3%): the
  classical decay has a CONTINUUM LIMIT in 1+1d. Consistent with
  the UV-convergent d=1 reduced measure (stage-3 slope 0) and with
  Garriga–Vilenkin's finite D=2 rate.
d=2 (L=16, λ=0.1, ΔE=10):  N=16..64 → rate 0.0205 / 0.1034 /
  0.2712 / 0.8186 — ×40 over ×4 in cutoff, effective power
  k_max^{~2.7}, NO saturation: no continuum limit. THE REVERSAL,
  in the pre-registered direction.

Exponent honesty: the naive channel-counting prediction at the
marginal dimension is log growth; the observed ~k_max^{2.7} is
steeper because the zero-point amplitudes themselves grow with the
cutoff in d≥2 (⟨φ²⟩₀ ∝ k_max: 0.243→1.205 across the sweep),
enhancing the effective vertex — a classical-statistical effect on
top of the phase-space counting. Decomposing the exponent
(amplitude² ~ k_max² × residual log?) is a clean follow-up; the
DIRECTION of the dichotomy (saturation vs unbounded growth) is the
claim, and it is unambiguous.

### Upshot

The dimension ladder is now DYNAMICAL, not just kinematic:
1+1d classical ghost decay converges to a finite continuum rate;
2+1d grows without bound as the regulator recedes — the classical
field theory tracks the reduced-measure dichotomy across its
critical dimension. This patches the "everything numerical was
d=1" vulnerability, replaces a wrong result with a stronger correct
one, and sharpens the M3/GV story: in d=1 the state's frame has a
covariant window because the UV is tame; in d≥2 the UV owns the
dynamics outright — UV-softness (GV nonlocality) is not optional
garnish but the price of any state-anchored frame in the physical
dimension.
[SUPERSEDED IN PART by the decomposition below: the dichotomy is
real but its mechanism is the TADPOLE ladder, not the channel
ladder.]

---

## 2026-07-11 — EXPONENT DECOMPOSITION: the reversal is
## SOURCE-DRIVEN; classical lattices probe the tadpole ladder,
## not the channel ladder

Code: `qft_bridge_decomp.py`. Two runs, all λ=0 controls silent.

**Run 1 (source fixed by spectral truncation |k| ≤ K_C; channels
swept via N).** The purified channel factor is FLAT in both
dimensions: d=2 rates 0.0317/0.0278/0.0229/0.0253 over k_max
3.14→12.57 (power exponent −0.20; even the log fit is weak,
R²=0.80 with the wrong trend); d=1: 0.0222/0.0374/0.0392/0.0281
(exponent +0.11, noise). If the golden-rule channel-log applied
classically, d=2 should have grown ×2.2 across this sweep; it did
not. **The entire ×40 growth of the full d=2 experiment was
source-driven.**

**Run 2 (channels fixed at one N; source amplitude scaled by a).**
rate ∝ a^{+4.96} (d=2, N=32) and a^{+4.45} (d=1, N=64) vs the
perturbative prediction a⁴ — consistent with rate ∝ variance², the
mild excess plausibly from approach to the parametric-instability
threshold at large a (noted, not pursued).

**Reconstruction closes:** full d=2 experiment had ⟨φ²⟩₀ ∝
k_max^{1.16} (measured); rate ∝ variance^{2.48} (Run 2) gives
k_max^{2.9}, vs the observed k_max^{2.7}. ✓ Within fit noise, the
exponent is fully accounted: ~2.7 = (source)^{~2.5×1.16} +
(channels)^{~0}.

### The corrected interpretation (important for paper #2)

There are TWO dimension ladders, and the classical experiment
measures the other one:
- **Tadpole ladder** (source): the zero-point variance
  ⟨φ²⟩ = ∫d^dk/(2ω(2π)^d) diverges as k_max^{d−1} — log at d=1,
  LINEAR at d=2. This is what the classical-statistical lattice
  tracks (Runs 1+2 prove it), and it is the true mechanism of the
  E4-2D continuum-limit dichotomy (still a real dichotomy: d=1
  converges because the tadpole is log; d≥2 has no continuum limit
  because the tadpole is power-divergent).
- **Channel ladder** (golden rule): the reduced decay measure
  ∫dE E^{3d−6} — convergent d=1, marginal-log d=2 — plus the
  always-infinite boost orbit. This is the CJM/GSTZ object. The
  classical dynamics does NOT track it (Run 1 flat), for a clean
  reason: classical fields cannot spontaneously radiate into EMPTY
  modes — spontaneous emission into unoccupied channels is
  intrinsically quantum, and the classical cascade populates high-k
  only by local-in-k flux, insensitive to where the far cutoff
  sits. The known classical-statistical limitation (vacuum
  overcounting/undercounting of spontaneous processes), here
  measured rather than assumed.

Consequences: (i) the "hotter start" objection to E4-2D is
CONCEDED and quantified — and conceding it yields the sharper true
statement above; (ii) numerical support for the channel ladder
rests on the quantum channel toy (stage-2 E3) and the phase-space
integrals (stage 3), NOT on lattice dynamics — paper #2 must say
so; (iii) methods claim for the paper: classical-statistical
vacuum simulations are tadpole-ladder probes; channel-ladder
questions require quantum treatment. (iv) The M3/GV framing
survives unchanged — M3 used thermal (occupied) states where
classical stimulated dynamics is the right physics.

### Caveats

Run-1 flatness is bounded by ensemble noise (±~20%): a channel-log
as large as ~×1.3 across the sweep is not excluded, only the ×2.2
naive prediction; Run-2 exponents carry the threshold-proximity
systematic; K_C truncation leaves nonlinearly-generated support
growth unquantified (the local-cascade reading is an
interpretation, standard in wave turbulence but not proven here).

---

## 2026-07-11 — S1: THE NO-SIGNALING STRESS TEST — all four
## treatments as predicted; NEW COROLLARY (the LHFL signal in
## closed form)

Code: `s1_no_signaling.py` (seconds). Context: Lee–Hsieh–Flammia–
Lee, PRL 112, 130404 (2014) — local PT evolution on one arm of an
entangled pair, treated as fundamental, permits superluminal
signaling. Our framework predicts exactly where the signal lives.
Setup: Bell pair; Alice's message = loss orientation (site 1 vs
site 2 of the dimer); signal = TV distance between Bob's marginals.

**(i) Metric-corrected closed dynamics: NO SIGNAL — max TV
1.7e-16** over t ∈ [0.2,8] (deflation: PT = Hermitian partner's
unitary; local unitaries cannot signal).
**(ii) Dilated open dynamics, no post-selection: NO SIGNAL — max
TV 4.4e-16** (Halmos unitarity 2.6e-15). This was the framework's
kill-shot test: any leak here would falsify paper 1's dilation
story. It is clean.
**(iii) Survival-conditioned (broken phase): the signal appears,
with closed-form magnitude** — verified to 2.2e-16 against

    TV(t) = |p²−q²| / (p²+q²+2r²),   p,q,r as in the
    terminal-indivisibility theorem;  TV(∞) = κ̃/sinθ
           = sqrt(1 − (s/sinθ)²).

Numerics: asymptote 0.707107 hit to 6 digits at t=16 (s=0.5,
θ=π/4); s-sweep at t=25 matches κ̃/sinθ to 6 digits away from the
EP (0.959166, 0.824621, 0.529150 at s=0.2/0.4/0.6; residuals at
s≥0.7 are finite-t, κ̃t ≲ 1.4). TV is non-monotonic: peaks ~0.797
near t≈1 before settling to the asymptote. **NEW COROLLARY of the
terminal-indivisibility theorem: the conditioning ("LHFL") signal
strength of a broken-PT local operation is κ̃/sinθ — zero at the
exceptional point, → 1 deep in the broken phase.**
**(iv) Unbroken PT + conditioning (the actual LHFL construction):
signal present (max TV 0.5774 ≈ 1/√3) under conditioning, ZERO
under treatment (i) with the SAME Hamiltonians.**

### Interpretation (paper-2 FTL section, ready)

The "faster-than-light" capability of local PT operations is
located exactly: it lives in the CONDITIONING — treating the
sub-stochastic (survival-renormalized) process as the whole sample
space — and nowhere else. The closed and dilated dynamics are
no-signaling to machine precision. And the conditioned "signal" is
not operational FTL: constructing the post-selected ensemble
requires Alice-side survival information, which travels
classically; Bob alone cannot filter. So the stochastic currency
resolves the LHFL controversy constructively: same Hamiltonians,
three bookkeepings, signal in precisely one of them, with its
magnitude now a theorem. Connects to the paper-1 theme (the broken
phase is survival-conditioned dynamics) and the paper-2 theme (the
pathology enters through the choice of sample space).

---

## 2026-07-11 — S3: FOLIATION DETERMINACY CURVE (F3 quantitative)

Code: `s3_foliation_determinacy.py` (~1 min; 400 realizations per
point). Construction: 1D lattice ensembles = frame-symmetric
zero-point part (n=1/2 per mode, split ±k — the classical mimic of
the boost-invariant vacuum) + boosted thermal part n_th = T/(u·k)
at v=0.35; frame extraction v̂ = P/E per realization (the 1D
timelike-eigenframe estimator of ⟨T^μν⟩).

Result — the determinacy curve:
  T=0 (vacuum): mean v̂ = 0.0013, scatter 0.121, SNR ≈ 0 — the
  extracted foliation is PURE NOISE; T=0.01: mean −0.012 (wrong
  sign, SNR 1.8 — indeterminacy regime made vivid); T=0.1: 0.024
  (SNR 4); T=1: 0.150 (SNR 34); T=3: 0.219 (SNR 51), tracking the
  thermal (frame-carrying) energy share (0.012 → 0.79) toward the
  massive-bath streaming velocity.

**F3 upgraded from algebra (⟨T^μν⟩ ∝ η^μν has no eigenframe) to a
measured, continuous determinacy curve: the foliation information
content of a state vanishes smoothly at the vacuum.** Ties to F4:
any real cosmological state (thermal share > 0) sits at finite SNR
— the comoving frame is extractable in practice, not just in
principle. Caveat: classical amplitude statistics (exponential/
chaotic-light per mode); a quantum treatment would replace scatter
with quantum estimation bounds — the shape, not the scale, is the
claim.
