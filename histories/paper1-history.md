# Process history — Paper 1: "Indivisible stochastic processes for non-Hermitian and higher-derivative quantum systems"

Sources: notes.md (dated entries), README timeline (user-attested),
git history including the Gitea `pre-release-history` branch (original
overnight commit timestamps; first commit 2026-07-11 02:34 CDT), the
archived session transcript, memory records. Fine-grained timings:
`process_timeline_papers12.md` in this directory (mined from the full
26-hour transcript; timestamps UTC = local + 5). Transcript-verified
anchors: paper drafted 03:50--04:26 UTC (= ~11 P.M. local, matching
the README timeline independently); publication 07:28--08:11 UTC
(= ~2:30--3 A.M. local); v1.0 release 08:01 UTC; provenance/audit/
squash block 14:43--15:29 UTC; inline literature sweeps at 04:33 and
07:11; audit agents launched 14:58. One event the notebook did not
record: at 15:29 UTC the USER caught an over-squash of the Gitea
remote during the squash operation --- a human-detector event ---
and the archive branch was restored.

## Timeline

**2026-07-10, ~6 P.M. — the seed question** (user, in a Claude
Desktop conversation, preserved verbatim as PDF in the repo):
"Is it not possible that the antilinear PT/time-reversal symmetry
element could maybe predict indivisible non-Markovian processes?"
A project briefing (`PT_stochastic_handoff.md`) was distilled from
that conversation and seeded the working session.

**Evening, in order (notes.md §5.1–5.4):** the K1–K4 detailed-balance
theorem (with 200/200 randomized verification); the broken phase as
Halmos dilation (terminal-vs-recurrent indivisibility; backflow
dissociation); the exceptional point as coordinate singularity
(scaling table); Pais–Uhlenbeck (ghost realization valid; no-ghost
quantization exits the sample space). Paper fully drafted by
~11 P.M. per the README timeline.

**Extensions to ~2 A.M.:** terminal-indivisibility lemma proved
exactly; interacting PU (conservative/transient/explosive stages);
the explosion-dictionary theorem (V1–V5 verifications, including the
wormhole completion); multidimensional deficiency theory (Theorems
A–D; the S-matrix at infinity).

**First literature sweep (same night).** PRIOR ART FOUND for the
K1–K4 matrix core (Parter–Youngs 1962; Engel–Schneider 1973) —
repositioned immediately: the paper claims the beables/detailed-
balance/uniqueness reading, attributes the algebra. Also found: the
two 2026 interacting-ghost stability papers (complementary), KAU
2017 (dissociation framing sharpened against it), Chruściński–
Rivas–Størmer (inequivalence known for quantum channels; ours exact
and classical). Verdict pattern: three headline claims survived;
attribution corrected before first publication.

**Skin-effect theorem + topology corollary** (H¹ classification);
**PU-deficiency evidence campaign** (calibrated drift diagnostic;
split verdicts; the λ<0 surprise flagged as tentative).

**First publication, ~2:30–3 A.M. 2026-07-11:** repo created;
user chose to SQUASH the public GitHub history to a single commit
while preserving the true overnight timestamps on the Gitea
`pre-release-history` branch — a deliberate provenance decision
(publish clean; keep the tape).

**Next-morning continuations:** exact channelization of the quartic
PU with a CONFIRMED SIGN PREDICTION (λ>0 limit-circle vs λ<0
completion — differential evidence); finite-channel stability
theorem; completion-candidate mechanisms (a conjecture FALSIFIED by
its own diagnostic: "completion ⇔ null escape" — the λ<0 PU
escapes through the channel tail instead; both mechanisms kept);
**the no-compact-witness theorem, found by falsifying our own
certificate design** — the first design violated a bound the numerics
then enforced ("theorem as bug-detector"); the certified 1D
glued-tail certificate; the Maslov feasibility study.

**Final audit + second reference sweep (2026-07-11):** front-matter
staleness (abstract predated five results — extended); two figure/
text jams; all bibliography entries engaged (34→36; Ralston and
Fischer–Burgarth–Lonigro found and integrated); AI-disclosure
section added.

**Three-agent audit (morning after v1.0):** all 37 references
confirmed; FIXED: a `sec:code` starred-section \ref bug; the
`skin_effect_beables.py` figure path broken by the scripts/ move;
drift-range honesty (a 0.34 window disclosed rather than smoothed);
Reed–Simon theorem numbers (X.8–X.10); Rauch–Reed 1D attribution.

**v1.1 (same day):** Section 10 (experimental probes) added,
apparatus-cited. ENCROACHMENT handled honestly: the Z₂ skin effect
had been observed in 2025–26 — the prediction was repositioned from
existence to the beable-obstruction observable. v1.0 stays frozen as
the public release; v1.1 carries a dated header.

**2026-07-12 — the late-caught miss.** Paper 4's adversarial audit
traced a false proof step to paper 1's Section 2: "|U|² is doubly
stochastic **iff** U is unitary" — only the forward direction holds
(counterexample: singular matrices with unistochastic modulus
squares). The word had survived paper 1's own four audit rounds and
one external circulation. Fixed in v1.1 ("if", with the
converse-fails parenthetical). See paper5-history.md, items 4.9/4.10.

## Errors & misses ledger

| # | What | Caught by | Fate |
|---|---|---|---|
| 1.1 | K1–K4 matrix core already classical (1962/1973) | first lit sweep, pre-publication | attributed; claims rescoped to the beables reading |
| 1.2 | certificate design violating what became the no-compact-witness theorem | own numerics enforcing the bound | became a THEOREM + design fixed |
| 1.3 | "completion ⇔ null escape" conjecture | own diagnostic (λ<0 PU) | falsified; two mechanisms kept |
| 1.4 | front-matter staleness | self-audit read-through | extended |
| 1.5 | sec:code \ref bug; figure path bug | three-agent audit | fixed |
| 1.6 | drift-range honesty (0.34 window) | three-agent audit | disclosed, not smoothed |
| 1.7 | Z₂-skin prediction encroached by 2025–26 experiments | prior-art sweep (v1.1) | repositioned to the un-measured observable |
| 1.8 | "doubly stochastic iff unitary" false converse | paper 4's adversarial audit, 2026-07-12 | fixed in v1.1; survived 4 prior audits |

## Process events (high level)

prior-art searches: 3 (first sweep; second sweep at final audit;
v1.1 probes/encroachment sweep). adversarial/verification rounds: 3+
(final audit; three-agent post-publication audit; the program's
later audits reaching back). controls: every script self-verifying;
two results (1.2, 1.3) exist BECAUSE a self-check failed. human
steering: seed question; squash-but-preserve provenance decision;
freeze-v1.0 policy; circulation to a physicist reviewer. Status:
v1.1 current; under external review.

## WAVE 7 (2026-07-16) — claims pass 29 (Opus, adversarial). CLEAN.
No CRITICAL/MAJOR/MINOR. 20+ theorems/props re-derived; exact spine (deflation,
Kolmogorov, skin, terminal-indivisibility) reconfirmed by hand + numerically
(L12/L21 to 1e-11; floor -1.20711, t_c 1.31696, t_0 1.76275). All four adversarial
modes cleared (no false converse, no overclaim, no half-domain, no missing
hypothesis; signs and def-vs-estimator clean). 2 NIT HELD (optional micro-pass):
(a) abstract item (ii) folds K3 (HijHji>0) into "detailed-balance" wording — K3 is
coupling reciprocity, distinct from cycle condition K4; full thm:kolmogorov lists
all of K1-K4 correctly. (b) prop:deflation "no process at all" could be over-read as
excluding time-dependent maps; scope ("fixed invertible B") is already stated.
No manuscript change. Claims counter 0->1. Biblio + numerics remain 3/3 CERT
(not re-run this wave). Agent acfa61e8.

## WAVE 8 (2026-07-16) — claims pass 30 (FABLE, adversarial). CLEAN at CRITICAL/MAJOR; 1 MINOR applied.
Cross-model diversity check (wave 7 was all-Opus). ~27 statements re-derived + machine-checked to 1e-16.
- [MINOR APPLIED] rem:nocompact — "No compactly supported---hence no truncated, windowed, or lattice-regularized---function can witness deficiency" overreached: a Fock/Hermite basis TRUNCATION is not compactly supported, so the C0^inf bound doesn't literally cover it (conclusion holds because finite Hermite combos lie in D(S-bar), but that step was unstated). Reworded: "No compactly supported---windowed or lattice-regularized---function ... nor any finite basis (Fock/Hermite) truncation, which lies in the closure's domain by the same argument". Recompiled 49pp clean.
- HELD (NIT micro-pass): thm:dictionary(2)(a) "U(1) per escaping end" wording (parenthetical already says U(2) for two ends); abstract(vi) trichotomy conservative/transient/explosive not mutually exclusive (App multiD states it right); thm:extlat(3) "generically dim 3" vs proof "torus dim >=2".
Counter: claims 1->0 (applied finding). Biblio + numerics remain 3/3 CERT (not run). Agent a587dcd2.

## WAVE 9 (2026-07-16) — claims pass 31 (OPUS, adversarial). CLEAN (convergence re-check of wave-8).
All-Opus flip from wave-8 Fable. Full spine independently re-derived from scratch: thm:kolmogorov iff (both directions genuine), thm:terminal-indivisibility (det, both Wronskians, L12/L21 closed forms = brute force to 5 digits, floor -1.2071, t_c=1.3170<t_0=1.7627, all five items i-v), Prop 6.9 metaplectic identity term-by-term exact, App C/D counterexamples (Prop D.7/D.8) valid, cascade thresholds correct. Scope discipline holds (1D monotone model, separable/central "model cases", computer-assisted cert flagged). Wave-8 rem:nocompact MINOR fix area re-checked, sound. ZERO CRITICAL/MAJOR/MINOR.
- HELD (NIT micro-pass): abstract L70 / thm:terminal(iii) "floor approached from below by the signed entry" reads as a floor on L12 but is a floor on |L12| / ceiling on the signed entry (needs careful re-derivation before rewording — do NOT hasty-fix a theorem statement); transient/explosive Markov-recurrence vocabulary caveat; Thm 3.4(iii) link-field sign convention unpinned; Thm 6.9 "minus the Schrodinger operator" forward-pointer.
Counter: claims 0->1. Biblio + numerics remain 3/3 CERT (not run). Agent aa87d73b.

## WAVE 9 STATE: claims 1 / biblio 3 CERT / numerics 3 CERT.

## WAVE 10 (2026-07-16) — claims pass 32 (FABLE, adversarial). CLEAN. Counter 1->2.
All-Fable flip from wave-9 Opus (diversity check on the wave-9 "clean" verdict). Full spine re-derived independently (prop:deflation 0.930; thm:kolmogorov iff + converse; thm:terminal det/both Wronskians/t_c<t_0; prop:bo displaced-oscillator by hand; App C signature-(n,n) + 4 exclusions; Table L=16 spacings 2.3247/0.9754). ZERO CRITICAL/MAJOR/MINOR. 4 NIT held (thm:terminal 1^T L=(0,-4 sin theta) one-line algebra; lem:feller variant sentence; l.906 "real coupling" qualifier; abstract (ii) K2-K4). **Wave-9 held floor NIT RESOLVED as over-flag** — this pass explicitly re-derived the floor direction and confirmed the abstract's floor-on-|L12| phrasing is correctly modulus-scoped (logged to auditor-error-log). Counter: claims 1->2. Agent a027b2e4.

## WAVE 10 STATE: claims 2 / biblio 3 CERT / numerics 3 CERT.

## WAVE 11 (2026-07-17) — claims pass 33 (FABLE, adversarial; user-directed all-Fable wave). 1 MINOR applied. Counter 2->0.
Spine re-derived to machine precision (prop:deflation; thm:kolmogorov iff + converse; thm:terminal all closed forms + floor identity to 4e-16; prop:bo by hand + Fock 3e-14; thm:stability Gauss-Hermite nodes 8e-16; App C/D counterexamples). Floor phrasing re-confirmed correctly modulus-scoped (L12 < -(sin theta + kappa~) strictly for t>t_c). 1 MINOR APPLIED:
- thm:app-separable(i)-(ii) (App D, L2266-2270): Feller integrals Sigma=N=T^2 and mean lifetime T^2 for beta=0 stated unconditionally, but the generator carries general eps (the sibling beta=1 formula carries eps explicitly) -> true only at unit noise. Fix: "(unit noise, eps=1)" + "(in general T^2/eps^2)". Classification unaffected.
3 NIT held (lem:feller hypothesis weakening; thm:skin "on a complex loop"; rem:nocompact Fock/Hermite cutoff-in-graph-norm step). Counter: claims 2->0. Agent a4f8b817.

## WAVE 11 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 12 (2026-07-17) — claims pass 34 (FABLE + abstract-consistency sweep). 2 MINOR applied. Counter stays 0.
Spine re-derived intact (Thm 4.2 floor identity, displaced-oscillator, Gauss-Hermite, App B/C class-level, all 8 Table-2 pi/T_cross to the digit; floor phrasing re-confirmed a floor on |L12|). 2 MINOR APPLIED (abstract-vs-body):
- abstract (viii) L84: "a rigorous channel-based multidimensional extension ... S-matrix at infinity" dropped the model-class scope the intro (item 8) + body carry; App B (Props B.9/B.10) proves the dictionary FAILS beyond separable/central/boundedly-coupled -> added "(for separable, central, and boundedly-coupled model classes)".
- abstract (iii) L73: "late-time information backflow vanishes" stated flatly; body Sec 4.3 is numerical ("no classical backflow observed") -> "vanishes numerically".
4 NIT held (generically-indivisible unhedged; "reflect"->"returns" verb; reading-path dependency; Sec 5.2 "1.2 decades/level -> 53 at N=48" arithmetic 1.2x48=58). Recompiled 50pp clean. Agent a6cf8631.

## WAVE 12 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 13 (2026-07-17) — claims pass 35 (FABLE; broadened to cross-ref/notation/hypothesis-completeness). 1 MAJOR applied. Counter stays 0.
Spine re-derived clean (thm:terminal to 1e-16; thm:kolmogorov iff; prop:bo; lem:feller; App D Khasminskii; cor:app-central scalings; all dimer numbers + spacing table). 1 MAJOR APPLIED (ledger 37):
- prop:revival proof + app:completions frame-pinning: the Olver/Liouville-Green error bound was claimed to follow from |V'||V|^-3/2 bounded + V->-inf monotone, but (v^-1/2)'' involves V'', which the C^1-only mechanism model does NOT control. Counterexample V'=-x^3(2+sin e^x) (orchestrator-verified: error integral ~ int x^-0.5 e^x diverges). Fix: added "V in C^2, |V''||V|^-2 integrable" at both Olver-frame invocations; noted the V'' term needs it, the (V')^2 term follows from the old bound. Affects the Olver-pinned frame + thm:extlat(3) segment; LC/LP dichotomy + frame-independent legs unaffected.
4 MINOR HELD for a dedicated NOTATION pass (Gamma trace-map rename; T kinetic-poly overload; kappa triple-booked; prop:deflation call-site generality-note). 5 NIT held. Counter claims stays 0. Recompiled 50pp clean. Agent a8aa8750.

## WAVE 13 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 14 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 36 OPUS (cross-model check after 4 straight Fable waves; hypothesis-completeness + abstract-consistency).
ZERO MAJOR -- all 8 load-bearing theorems + App C/D/E re-derived SOUND by Opus (prop:deflation, thm:kolmogorov both directions, thm:terminal generator-floor exact, thm:channels/central, thm:stability/dichotomy, prop:bdyS/thm:extlat n=1 collapse + n=2, Lemma 8.2 Feller scale/speed, interacting-ghost TMSV tail, App-D counterexamples). Abstract (i)-(viii) + Table-1 status tags consistent with body; no dropped hedges. Applied:
- [MINOR APPLIED] Thm 8.1(2) thm:dictionary: the WKB norm identity eq:onelineidentity was stated under the theorem's global "C^1, |V'||V|^-3/2 bounded" hypothesis, but its Olver error bound needs the C^2 control that prop:revival (ledger 37, wave 13) ALREADY carries. FIX-PROPAGATION MISS on ledger 37 itself -- the wave-13 fix went to prop:revival + app:completions but not to the theorem that first STATES the identity. Fix: added parenthetical at the identity "its Olver error bound requiring the added control V in C^2, |V''||V|^-2 integrable, as in Prop. revival, holding automatically for the power-law potentials of the mechanism model." Grep-all-copies lesson (ledger-38 class) re-confirmed by Opus.
- [NIT APPLIED] Halmos-dilated 4-config family (eq:halmos): "is an ORDINARY Barandes indivisible process" -> "is a Barandes indivisible process (per-time unistochastic, not one-parameter-group-generated)" -- the Halmos dilation is per-time, not e^{-iH_big t}; "ordinary" wrongly invited a Hamiltonian-generated reading. Substantive object (Gamma_red=|C(t)|^2, a genuine one-parameter contraction semigroup) unaffected.
- [NIT HELD] Thm 8.1(2)(b) semiclassical spacing law inherits the same C^2 caveat -- now covered by the added parenthetical just above it; no separate edit.
Counter claims stays 0 (applied MINOR+NIT). Recompiled 50pp clean. Agent a6cb010e.

## WAVE 14 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 15 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 37 FABLE (adversarial diversity check on wave-14 Opus fixes).
1 MAJOR (ledger 40) + 2 MINOR + 1 NIT applied; entire skeleton re-derived SOUND (deflation, kolmogorov, terminal, channels, stability, bo, extlat class-level, skin, Feller, App-D counterexamples -- ~15 results).
- [MAJOR ledger 40 APPLIED] Olver error-bound WRONG EXPONENT: the wave-13/14 "|V''||V|^-2 integrable" -> "|V''||V|^-3/2" (LG error integrand (5/16)q^-5/2(q')^2 - (1/4)q^-3/2 q'' scales as |V''||V|^-3/2). The BV parenthetical was already correct -> the two halves were contradictory. Fixed at all 3 sites (thm:dictionary, app:completions, prop:revival) + replaced the invalid (V')^2 justification with the IBP identity. OPUS VERIFIER CONFIRMED + gave its own staircase counterexample. Corrects ledger 37.
- [MINOR F2/F3 APPLIED] the added C^2 control now carried into the App-D WKB leg + the thm:extlat header (frame-dependent R=|S_ii|^2 states its hypothesis).
- [NIT APPLIED] results-map rows F (EP) + G (free PU) status E->E+N (both have numerical figures, matching row H's convention).
- [DEFENSIBLE, no edit -> auditor-error-log] abstract-ii gauge-flux iff (gauge gloss of a full condition already stated); F4 LC-criterion suspicion (cited to RS X.7-X.10 + RauchReed sharpness; WKB leg separately hardened).
Counter claims stays 0. Recompiled 50pp clean. Agents a0ba7933 (claims) / a216d9d7 (Opus verifier).

## WAVE 15 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 16 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 38 FABLE lane FAILED on a session limit (API error "session limit, resets 12pm America/Chicago") -- no result produced. No p1 edits this wave; unchanged 50pp. Counter claims unchanged. Re-run relaunched fresh in WAVE 17 (pass 38 re-run).

## WAVE 16 STATE: claims 0 (lane failed, re-run owed) / biblio 3 CERT / numerics 3 CERT.

## WAVE 17 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 38 FABLE (re-run after the wave-16 session-limit failure -- full session this time). 1 CRITICAL + 1 MAJOR + MINORs. Whole algebraic core re-derived SOUND (deflation, kolmogorov, terminal, bo, quadratic, channels, stability, Feller, skin -- all independently re-derived w/ numerics).
- [CRITICAL ledger 44 APPLIED] thm:dictionary(2) LC hypothesis INSUFFICIENT: C^1 + |V'||V|^-3/2 bounded + T<inf does NOT imply limit circle (phase-tuned monotone-C^inf staircase counterexample, sigma_max^2>1/2 verified at 5 widths -> limit POINT). Strengthened item (2) + App-C setup to require V in C^2, |V''||V|^-3/2 integrable; rewrote "dichotomy itself is exact" -> the added control makes both LC classification + norm identity rigorous, w/ the staircase note. Item (1) LP leg keeps C^1. **This VINDICATES the wave-15 F4 suspicion the orchestrator wrongly dismissed as "defensible" (auditor-error-log corrected).**
- [MAJOR ledger 45 APPLIED] prop:revival "|V''||V|^-3/2 integrable (EQUIVALENTLY V'(-V)^-3/2 BV)" is FALSE (BV is strictly weaker; the two BV-integrand terms can cancel). -> "(which implies, but is not implied by, ...)". Corrects the ledger-37/40 wording + the wave-15 Opus verifier.
- [MINOR applied] prop:deflation "no process at all (not merely none of this form)" -> scoped to fixed-invertible maps (time-dependent = separate, cf sec:ep). fig:explosion caption + body "conservative completions" (finite-box) -> "finite-box stand-ins for the extreme completions R=1,0" (matches rem:nocompact). "divisibility onset t_c" -> "indivisibility onset" (2 copies, sibling-swept vs the correct L878).
Counter claims stays 0. Recompiled 50pp clean. Agent a42691827 (the 1st attempt a962f1bc failed on the session limit).

## WAVE 17 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 18 (2026-07-17, conv 954cb52d) — notation pass + Fable claims pass 39 (full session)
NOTATION: freed central Gamma (App-C boundary trace map -> new macro tr_d), unified doubly-named constant (Maslov S->A) + kinetic poly T->Q + App-B Poisson kappa->qbar + switching lambda->q + spectral radius rho->spr + oscillator-free op A->A_0 + Thm-app-kato p_0->p_* + cascade kappa->kappa_g. CLAIMS (full-session Fable): re-derived the ENTIRE spine SOUND incl. thm:dictionary LP+LC legs (ledger 44/45 HOLD -- "C^2 hypothesis and implies-BV parenthetical both check out"). 1 MAJOR (ledger 46): App-C prop:bdyS "for comparison" dissipative characterization sign error (maximal nonpositive->nonnegative, Omega<=0 -> >=0, 2 sites L2836+L2937; internally self-contradictory; main self-adjoint<->U(n) untouched). MINOR/NIT applied: abstract (i) "(via a fixed beable map)"; rem:nocompact "same argument"->"a cutoff argument"; glued-tail q=(z-U)/a symbols defined; thm:skin(iii) uniform w->w!=0; indivisibility->divisibility. Left defensible: null-frame u=-cv; abstract (ii) Kolmogorov compression. Recompiled 50pp clean. Counter claims 0.

## WAVE 19 (2026-07-17, conv 954cb52d) — Fable claims pass 40 (relaunched after 64k-cap crash)
Re-verified the wave-18 Omega-sign fix (ledger 46) + thm:dictionary LP/LC (44/45) + app-ghost + Feller SOUND. MAJOR (ledger 47): indivisibility DIAGNOSTIC quoted the semigroup deviation ||Gamma(2t)-Gamma(t)^2|| (0.93/0.41/2.7) but the paper own definition (eq:divisor) is divisor negativity M=Gamma(t2)Gamma(t1)^-1<0; VERIFIED dimer indivisible (min M=-1.13, exact numerics) + 3x3 (min -0.275); fixed 4 sites (def L372, dimer leads with -1.13, 3x3+PU-grid reframed), no result change. MINOR ledger-44 SIBLING: thm:channels "super-quadratic fall (limit circle)" conflated fall-off with LC -> LC made operative hyp + C^2 example. MINOR (cross-wave escalation of wave-18 NIT): abstract(ii)+intro Kolmogorov dropped K3 (positive pair products); counterexample H12=1,H21=-1; added "reciprocal with positive pair products" both sites. TRIVIAL: thm:extlat(3) fiber dim 3 vs proof >=2 -> proof strengthened to 3. Recompiled 50pp clean. Counter claims 0.

## WAVE 20 (2026-07-17, conv 954cb52d) — Fable claims pass 41 (hard output budget, no crash)
Spine SOUND; ledger 44/45/46/47 HELD; LP/LC-vs-falloff trap defended everywhere except two summary sites (fixed). Residual = ledger-44 C^2 propagation + siblings: abstract(vii)+intro item 7 mechanism-model summary got "under C^2 error control"; Thm 8.1 preamble "LP/LC criteria"->"limit-POINT criterion; LC leg adds C^2"; reconciled the "mechanism model" DEFINITION FORK (App C now "in its limit-circle regime, the added C^2 control of leg 2"); intro item 1 "(via a fixed beable map)" (wave-18 abstract sibling); self-corrected my wave-19 dimer "equivalently"->"the family also". Recompiled 50pp clean. Counter claims 0.

## WAVE 21 (2026-07-17, conv 954cb52d) -- OPUS cross-model claims pass 42
CROSS-MODEL CONVERGENCE: Opus re-derived every spine SOUND, ZERO CRITICAL/MAJOR, VALIDATED ledger 44/45/46/47 + the ledger-44 C^2 sibling hunt ("no live defect") + mechanism-model consistency + indivisibility def-vs-exhibit. LOW fixes (tightening wave-20 wording): abstract+intro C^2 scoped to "its limit-circle leg" (LP leg needs only C^1); cor:central LC justification completed (super-quadratic fall governs, not subquadratic centrifugal). Recompiled 50pp clean. Counter claims 0.

## WAVE 22 (2026-07-17, all-lane all-Fable; user: "run until Fable returns NOTHING 3x each lane")
- CLAIMS (Fable): no CRITICAL/MAJOR (spine re-derived sound). 2 MIN + 2 NIT applied: (1) "malicious nonlinearity = explosive" scoped to the classical mechanism / minimal escape process (lambda>0; the lambda<0 quantum completions can resist) at Sec-7.2 + intro item 6; (2) intro item 5 given the "truncated (discretized) configuration space" hedge + results-map row G; (NIT) results-map row E status E+R -> E+R+N (backflow half numerical); (NIT) reading-path shortcut now needs from Sec-kolmogorov only the Thm-kolmogorov statement.
- NUMERICS (Fable): 1 MIN (SCRIPT provenance, no ms change): the in-text divisor minima -1.13 / -0.26 / -24.5 were correct but not printed by the cited scripts; added divisor-min prints to pt_barandes.py (-1.1259), fixed_beable_kolmogorov.py (-0.2598), pais_uhlenbeck.py (-24.55). Closes the ledger-47 script gap.
- BIBLIO (Fable): 1 MIN: VanWesemael2025 now published Phys. Rev. E 114, 014131 (2026) (Crossref-verified); journal ref added. All 58 bibitems + claim-support otherwise clean.
- Recompiled 50pp clean. Counters: claims 0; numerics CERT->0 (script fix); biblio CERT->0. Fable-clean streak: all p1 lanes 0/3.

## WAVE 23 (2026-07-18, all-lane all-Fable; convergence re-check + streak-build)
- CLAIMS (Fable): no CRITICAL/MAJOR (full spine re-derived sound; wave-22 fixes re-validated). 2 MIN + 2 NIT: fig:channels caption reworded (no L->inf limit; unitary parametrization is von Neumann's theory, indices by thm:channels); abstract item (vi) explosive verdict given the "at the mechanism level" hedge (SIBLING of the wave-22 Sec-7.2/intro-6 fix, missed then); thm:dictionary(2)(a) "U(1) per end" -> "U(n) for n ends" (+ the Sec recap sibling); thm:terminal hypothesis "0<s<sin theta" added (cross-paper sibling of the wave-22 p3 Thm 6.1 fix).
- NUMERICS (Fable): CLEAN -> Fable-clean 1/3 (divisor-min prints from wave 22 confirmed reproducing -1.1259/-0.2598/-24.55).
- BIBLIO (Fable): 1 NIT -- arXiv-year format inconsistency (dropped "(2025)"/"(2026)" from Dahya2025 + LanMaYang2026 to match the other arXiv-only entries); VanWesemael->PRE 114 014131 (2026) re-confirmed.
- Recompiled 50pp clean. Counters: claims 0/3, numerics 1/3, biblio 0/3.


## WAVE 24 (2026-07-18, all-lane all-Fable)
- CLAIMS (Fable): CLEAN -> Fable-clean 1/3. (First attempt CRASHED on the 64k output cap -- the recurring p1-lane failure; relaunched with a hard TOTAL-output constraint (terse throughout, not just the report), which worked. Wave-22/23 fixes re-validated: mechanism-level explosivity, thm:dictionary LC C^2 control, thm:terminal closed forms + column-sum (0,-4 sin theta), U(n) graph argument.)
- NUMERICS (Fable): 1 NIT -- PU-grid divisor minimum "-24.5" -> "-24.55" (matches the script print -24.55 and the 2-decimal precision of the sibling minima -1.13/-0.26). Resets numerics 1/3 -> 0/3.
- BIBLIO (Fable): 1 MINOR -- KarlinTaylor cite at L2661 (Feller pure-birth explosion criterion) given a local "Ch.~14" pinpoint (the bibitem's Ch.~15 is diffusion; explosion is the CTMC chapter). Resets biblio 0/3.
- Recompiled 50pp clean. Counters: claims 1/3, numerics 0/3, biblio 0/3.

## WAVE 25 (2026-07-18, all-lane all-Fable)
- CLAIMS (Fable): no CRITICAL/MAJOR; NO 64k crash this time (hard total-output-budget prompt + a live terse-finalize nudge). 2 MIN + 1 NIT: App-B thm:app-separable(ii) "zeta->T_n a.s." qualified "(beta=1)" (false for the driftless variant) + 2 proof-site siblings (L2173, L3043) swept; abstract+intro "reciprocal with positive pair products" -> "two-way" (the K2 mutually-nonzero sense collided with the symmetric-hopping sense used at Cor 3.5/§11, wrongly excluding the nonreciprocal Hatano-Nelson chain that Thm 3.4(iii) proves IS fixed-beable; 7 symmetric-hopping uses left intact); lem:feller(ii) "(drifted variant)".
- NUMERICS (Fable): 1 MIN -- quartic_pu_leak.py footer contradicted its own r=8 row (classical speed 14.95 > k_max 12.57); fixed the script footer + scoped the manuscript "every probed radius" to r<=7. All numbers reproduce (divisor minima incl. -24.55 exact).
- BIBLIO (Fable): 1 MIN + 1 NIT -- added Schnakenberg1976 (RMP 48, 571 (1976), Crossref-verified) + \cite at the "cycle affinity"/"steady-state cycle current" clauses (was attributed to nothing; Kolmogorov1936 covers only reversibility<=>cycle-product); dropped the hard-coded "Ch.~15" from the KarlinTaylor bibitem (in-text pinpoints §15.3/§15.6/Ch.14 carry it).
- Recompiled 50pp clean. Counters: claims 0/3, numerics 0/3, biblio 0/3.

## WAVE 26 (2026-07-18, all-OPUS cross-model check; Fable exhausted)
- CLAIMS (Opus): CLEAN. Full monolith (Parts I-III + App C/D/E) independently re-derived cross-model; the wave-25 fixes (beta=1 lifetime, reciprocal->two-way, lem:feller) all validated. NO 64k crash (hard-budget prompt held for Opus).
- NUMERICS (Opus): CLEAN. Every number re-traced; the wave-25 quartic_pu_leak r<=7 fix corroborated ("r=8 marginal").
- BIBLIO (Opus, confirms wave-26 Fable): 1 MIN applied -- author-list "et al." truncation made uniform (rule: list all if <=3 authors, else "First et al."); 9 entries truncated (SzNagy2010, BreuerReview2016, VanWesemael2025, Deffayet2026, Okuma2020, Klauck2019, Xiao2019, BottomlessPotentials, InvertedHO2026); final 47 full / 13 et-al. Schnakenberg1976 (wave 25) re-validated.
- Recompiled 50pp clean. Fable-clean streaks UNCHANGED (Opus wave doesn't advance them): claims 0/3, numerics 0/3, biblio 0/3 -- but all three now Opus-cross-model-validated.

## WAVE 27 (2026-07-18, all-OPUS cross-model check, 2nd consecutive; Fable exhausted)
- CLAIMS (Opus): CLEAN. Second full monolith re-derivation cross-model (Parts I-III + appendices, boundary S-matrix/flux functor, interacting cascade thresholds); no 64k crash. Every hedge/scope caveat re-checked against the body; zero findings.
- NUMERICS (Opus): CLEAN. Every number in both tables + all captions re-traced to script outputs at quoted precision (divisor minima, skin cond(eta), spacing-law 3.5%/0.3% bounds, EP slopes within +-0.0025, App-D T_ell ratios 2.154=10^{1/3}). Rail-compliant.
- BIBLIO (Opus): CLEAN. All 60 bibitems re-verified field-by-field; the wave-26 author-list uniformity fix CONFIRMED consistent cross-model (uniform <=3-full / >=4-et-al rule across every entry). Schnakenberg/VanWesemael/RauchReed re-confirmed. (Disclosed coverage gap: WebSearch budget exhausted before a fresh novelty sweep -- not a finding.)
- Recompiled 50pp clean (no edits). Fable-clean streaks UNCHANGED: claims 0/3, numerics 0/3, biblio 0/3 -- all three Opus-cross-model-validated a 2nd time.


## SESSION 2026-07-18/19 (numbering unification + claim-support + rotation-four Fable)
- Folder paper/ -> paper1/ (series 1); bibitem cite keys Companion* -> codenames; "release gate / AUDIT.md / histories" leak sentence removed from the provenance note; biblio %-comment verification notes stripped.
- Claim-support sweep (Opus + Fable cross-model): CLEAN, no fabrication class. 4 provisional items resolved SUPPORTED (RauchReed "both directions" via CMP 29,105; Tang2016 post-selection; BenderMannheim rising-Gaussian/contour; Smilga benign threshold). Smilga "benign islands" -> "benign in the sense of" (word not Smilga's). REJECTED a false agent finding that the bibitems "list wrong arXiv IDs" (they cite journal refs only) -> auditor-error-log.
- Rotation-four Fable: NUMERICS CLEAN (16/21 scripts re-run fresh, 4 analytic recomputations). CLAIMS 1 MINOR + 3 NIT fixed (Galerkin hedge on Thm 10.7; uniform-ring zero-real-phase; "numerically" hedge on backflow; "fixed beable map" disambiguation) -- full 50pp + appendices re-derived, no 64k crash. BIBLIO inconclusive (garbled agent report; no findings; substance two-model-clean). Fresh streaks: num 1/3, claims 0/3, biblio 0/3.

## FABLE CLAIMS PASS 2026-07-19 (Fable-spend rotation-four wave; the 50pp monolith, terse-output recipe held -- NO 64k crash)
- **SOUND: zero CRITICAL/MAJOR.** Full analytic spine independently re-derived by hand cross-model: Prop 2.1 (deflation + spectral-radius exclusion incl. Jordan-EP), Thm 3.1/Cor 3.2 (detailed-balance dj|Hji|=di|Hij| <=> reversibility), Thm 3.4 skin obstruction, Thm 4.1 terminal indivisibility (A^2=-κ̃^2, closed forms p/q/r, det, floor identity, EP/unbroken continuations, t_c<t0), Thm 8.1 LP/LC legs incl. the C^2 error-control bound, Lemma 8.2/App A (scale/speed, Σ=N=T^2), Thm 9.2/C.4/C.5 (U(n) completions), Thm 10.2/10.3/10.6 (Nelson/Kato), Prop 10.7 displaced-oscillator (exact), Thm 10.8/Cor 10.10 (n+=n-), App B (class equality, cascade eigenvalues, T_l scaling, Khasminskii). Abstract/intro item-by-item consistent.
- Applied: **MINOR 1** (Thm 8.1(1) LP leg cited only ReedSimon2 X.7-X.10, which give the Weyl alternative + power-law LP; the GENERAL monotone "T=inf => LP" is Levinson's criterion -- verified via WebSearch the exact V'|V|^{-3/2}-bounded + ∫dx/√(K-V)=∞ form; ADDED \cite{CoddingtonLevinson} [Theory of ODEs, McGraw-Hill 1955, Ch.9] + reworded the LP-leg line; math was already sound, this closes the citation gap); **MINOR 2** (Thm 8.1(2) sharpness parenthetical asserted an uncertified staircase counterexample "smoothness cannot be dropped" -> hedged "we expect ... should not be dropped"); **NIT** (8.1(2)(b) "returns probability from infinity after the round trip" -> "semiclassically, returns..."). 
- DEFERRED NITs (too risky/borderline for the monolith): Ω triple-duty (vacuum / ω1^2+ω2^2 / boundary form) + τ quadruple-duty (κt / Feller clock / SL expression / channel clocks) collisions -- auditor found NO induced errors, local contexts disambiguate; a rename across 50pp is high-regression-risk for a nit -> a dedicated p1 notation pass if ever. "computer-assisted" abstract wording (already hedged "in a computer-assisted sense").
- Streak: p1-claims had findings this pass -> NOT a clean-streak pass. Recompiled 50pp, 0 undefined (new citation resolves); both gates PASS.

## FABLE BIBLIO PASS 2026-07-19 (Fable-spend rotation-four wave, biblio round)
- **56/59 bibitems fully CLEAN** (59 bibitems / 60 refs; DAG root, no self-cites). No fabricated authors, no wrong initials, no arXiv-id/paper mismatches. The session-added CoddingtonLevinson entry independently CONFIRMED correct (McGraw-Hill 1955, Ch.9 = Singular Self-adjoint BVPs incl. LP/LC).
- Applied: **1 FIX** -- Smilga2005 title "Benign vs.\ malicious ghosts" -> "Benign **versus** malicious ghosts"; arXiv abbreviates "vs", but the PUBLISHED Nucl. Phys. B 706 title is "versus" (orchestrator confirmed via INSPIRE, which carries the published title; publisher-governs house rule). NOT applied on the Fable machine-read alone -- INSPIRE-verified first (the GSTZ/DonoghueMenezes discipline).
- HELD (LOW confidence, needs full-text not abstract): RauchReed1973 described as "oscillatory one-dimensional counterexamples" (L1199) -- the auditor (abstract-only) reads them as step/barrier potentials, but "oscillatory" may be justified by the full text; the substantive both-directions claim IS fully supported. Not changed on an abstract-only characterization read. Style option skipped: Petermann QE-15.
- UNVERIFIABLE sub-items (machine-read caveats, logged, no action): exact RS Thm X.9 statement; in-chapter location of Levinson's criterion in C&L Ch.9; KarlinTaylor Ch.14 explosion-formula page. (Metadata all solid; these are internal-locator precision only.)
- Streak: p1-biblio had a fix this pass -> NOT a clean-streak pass. Recompiled 50pp, 0 undefined; both gates PASS.

## OPUS CROSS-MODEL WAVE 2026-07-20 (Wave A; claims + numerics; biblio was Fable 56/59 earlier this session)
- **FULLY CONVERGED cross-model.** Claims (Opus): entire 50pp spine re-derived line-by-line -- Prop 2.1, Thm 3.1/3.4/4.1 (+ numeric anchors s=0.5: t_c=1.317, floor -1.2071), dictionary LP/LC legs, Thm 9.x/10.x, App B all SOUND; the session-added CoddingtonLevinson citation + the 2 hedges read correctly; no overclaim; 1 context-disambiguated notation NIT (σ/L/n reuse, no fix needed). Numerics (Opus, completing the Fable lane that was interrupted at 98% Fable): ALL 23 scripts run (heavy ones fresh incl. interacting_pu ~8min, completion_candidates Part A), EVERY value reproduces CLEAN, zero mismatch. The interrupted Fable item **1.12=2√(Ac)=1.11714 CONFIRMED genuinely analytic** (WKB log-log slope 4.8709 matches the closed form to all digits, not a fit); other "analytic" values (floor, cond(η)=e^{2w(N-1)}, 10^{1/3}=2.1544, amplitude √600=24.49) all verified closed-form. Deterministic (RNG seeded, no PYTHONHASHSEED). No CRITICAL/MAJOR/MINOR either lane. No manuscript change this wave.

## OPUS DEEP CLAIMS 2026-07-20 (Wave D; Nth adversarial pass, "hunt what was rationalized") -- SOUND
- No hard error. Seams re-derived from scratch: thm:terminal (Wronskian r'p-p'r=s, det=e^{-4sinθt}(1-2r²) via pq=1-s²σ², floor sign 2s²σe^{-κ̃t}+(sinθ+κ̃)>0), U(n) completions (signature (n,n)->maximal-neutral->U(n), Olver-frame pins |S_ij|² invariant, extreme-vs-boundary hedged for n=1), Kato/Nelson deficiency, Maslov blowup A=√(30γ/λ). One LOW coincidence flag RESOLVED: "24.55" appears for two UNRELATED quantities (free-PU divisor min entry L~1012 vs quartic-PU Maslov amplitude L~1894); NOT copy-paste -- Wave A numerics independently script-reproduced BOTH (pais_uhlenbeck.py min M=-24.55; maslov_feasibility.py √600=24.49->24.55). Harmless coincidence, no action. No manuscript change.

## OPTIONAL POLISH NITS APPLIED 2026-07-20 (the two deferred items -- now done)
- **RauchReed "oscillatory" -> dropped** (L~1199): "Rauch--Reed's oscillatory one-dimensional counterexamples" -> "...one-dimensional counterexamples". Two independent abstract reads this session (Wave-B p1-biblio + this) characterize the RauchReed 1973 examples as step/barrier (sharp-step reflection + tunneling barriers), NOT oscillatory; neutralized the inaccurate modifier (safe -- exact potential shape not load-bearing; the point is the hypotheses can't be dropped).
- **Ω/τ notation collisions -> DISAMBIGUATED (house-style local note, not a risky 50pp mass-rename at 92% context).** Added a note at the App-C boundary-form intro (~L2754) flagging Ω there = the boundary current form, distinct from the Sec-5.2 vacuum Ω and the Sec-10 frequency sum Ω=ω₁²+ω₂²; and τ (τ_max/τ_min) = the Sturm-Liouville expression, not the rescaled clock τ=κt (Sec 4) or the Feller clock coordinate (Lemma feller). Matches the paper's own "notation local to this theorem" style; auditors had confirmed the collisions induce NO errors (context-disambiguated) -- this makes the disambiguation explicit for the reader. Recompiled 50pp, 0 undefined (new \ref{lem:feller} resolves); both gates PASS.

## OPUS DEEP CLAIMS 2026-07-20 (hunt-what-was-rationalized wave, p1-p4) -- CLEAN (2 defensible NITs held, no edit)
- Opus re-derived the load-bearing algebra by hand/numerically: terminal-indivisibility theorem (det, both generator entries $L_{12}/L_{21}$, floor inequality + $-(\sin\theta+\tilde\kappa)$ limit, the $1^T L=(0,-4\sin\theta)$ column-sum identity used in the proof, $t_c/t_0$), Kolmogorov K1-K4 + detailed-balance corollary, skin/flux sign chain, both Bogoliubov thresholds ($g>|\omega_1-\omega_2|/2$ ghost, $g>(\omega_1+\omega_2)/2$ normal), EP exponents, central-potential $T_\ell$ exponent, prop:bo channel-operator sign -- ALL internally consistent. Zero CRITICAL/MAJOR/MINOR on the four lanes; abstract (i)-(viii) match theorem bodies incl. qualifiers (C^2 attributed to leg (2) only; "computer-assisted" carried to abstract).
- 2 NIT-level exposition items HELD as DEFENSIBLE (auditor-error-log 07-20): (NIT-1) thm:dictionary leg(1) bundles the $C^1$ $|V'||V|^{-3/2}$ control it doesn't strictly need -- limit-point needs only the Levinson growth bound $V\gtrsim-Kx^2$; a deliberate uniform "mechanism model" hypothesis, SAFE over-assumption. (NIT-2) top-level "an escaping end" framing vs the double-ended flagship $V=-x^4$ -- RE-CONFIRM of the 07-13 rejected lead (leg 2(a) already handles $n$ ends "$U(1)$ for one, $U(2)$ for two"; generalizing the setup would break leg(1)'s e.s.a. hypothesis). No manuscript edit. Both gates PASS.

## OPUS NUMERICS 2026-07-20 (Wave 6; reproduce-from-scripts) -- CLEAN
- Ran all 21 numeric scripts. EVERY quantitative claim reproduces exactly, no discrepancy at any severity, no over-precision. Spine: deflationary dimer (Gamma 0.368/0.632, min M -1.1259, ||e^{-iHt}|| 1.58..77.2); terminal-indivisibility (closed forms 1.7e-14, floor -1.2071, t_c=1.316958, det Gamma(t_c)=-4e-18, t0=1.7627); EP Petermann scaling (cond eta ~eps^-1, cond rho ~eps^-1/2, rescaled-clock 1.4e-10, backflow jump 1.3157); skin/flux cond(eta)=e^{2w(N-1)} exact + ring current -2.8e-17; Bogoliubov thresholds + sinh^2(gt) (<n1> 1.0537, energy books +/-8.301); quartic-PU -24.55; 1D-fiber glued certificate 0.00109 + 2sqrt(Ac)=1.11714; central-potential T_l 0.447/0.208/0.096, ratios 10^{1/3}. SS9_NUMERICS map accurate. 0 findings.
- No manuscript change.

## FABLE CLAIMS 2026-07-20 (cross-model diversity wave, p1/p3/p5/p6) -- 1 MINOR + 2 NIT applied; spine re-derived intact
- Fable independently re-derived every theorem (terminal-indivisibility full spine, K1-K4 iff BOTH directions, thm:dictionary LP/LC incl. the Olver C^2 chain, Bogoliubov, prop:bo, Feller, App D) + numerics to 1e-15. Zero CRITICAL/MAJOR, zero false converses. **Independently confirmed the 2 held thm:dictionary NITs DEFENSIBLE** (C1-bundling; double-ended).
- Applied: (MINOR #51) thm:extlat(4) converse "preserves total probability and measure class" enforces only c1/c2; c3/c4 need boundary-flux-data -> added ", and the boundary flux data". (NIT #52) intro "unbroken=real spectrum" false at EPs -> "real spectrum and a complete set of symmetry-respecting eigenvectors". (NIT #53) leg(1) e.s.a. didn't cover the paper's own V=-x^2 double-escaping-end control -> added "(or a second escaping end likewise at T=inf, as in V=-x^2)" -- RESOLVES this session's held p1 NIT-2 via a SAFE ADDITIVE alt; the auditor-error-log entry-34 clause-MOVE stays rejected.
- HELD-defensible (NITs, no change): F3 leg(1) C1-apposition (Levinson needs only monotonicity; optional); F5 cor:central r=0 origin per-channel deficiency 1 not 2 (conclusion (inf,inf) unaffected); F6 fig:generator "floor" caption shorthand (correct in the |L12| sense per Thm 4.1(iii)).
- Recompiled 50pp, 0 undefined. Both gates PASS. No MAJOR.

## 4-WIDE FABLE CLAIMS AUDIT 2026-07-23 (50pp full re-derive) — spine SOUND, 1 MINOR applied
- Fable read all 3526 lines and re-derived the spine: thm:terminal (floor identity 2spr+(sinθ+κ̃)(1-2r²)=..., t_c=1.3170, floor -1.2071), prop:bo displaced-oscillator (exact incl. -y²/2γΩ term + degree≤3 interchannel), lem:feller (Σ=N=T², drifted lifetime ODE), thm:dictionary (C¹ bound = Levinson leg-1; C² closes (V')²W^{-5/2} via the IBP), thm:kolmogorov/skin/quadratic, thm:app-ghost Khasminskii — all check exactly. Independent numerics reproduce (spacing table, A=√600=24.49, backflow window, e² growth ratio). Hypothesis-sufficiency lane CLEAN (the program's usual defect class absent); abstract-vs-body every universal hedged both places; ~40 cross-refs resolve; symbol collisions (Ω/τ) disambiguated in-text.
- APPLIED (minor-ledger #87): MINOR — footnote at eq:onelineidentity clarifying $\psi_\pm$/$u_n$ are the L² solutions at the REAL mechanism energy $E$; genuine deficiency vectors (τ∓i)u=0 carry a bounded WKB factor e^{O(T)}, so the limit-circle CLASSIFICATION is untouched but the norm identity "≈T" holds up to an O(1) factor. Covers all 3 sites.
- HELD (3 NITs): reading-path independence vs §5.2 EP callback; "distinct exact invariant" overstates by one (c4 reuses c1's unitarity); "standard vocabulary" transient/recurrent on a non-Markov process.
- Recompiled clean, both gates PASS. p1 is cross-model CONVERGED.

## W21 WIDE-OPEN AUDIT 2026-07-26 (Fable, adversarial; claims+numerics+biblio) — 1 MINOR applied; NO MAJOR
- **CLAIMS spine re-derived CLEAN** (Prop 2.1 deflation; Thm 3.1 K1-K4 both directions + detailed balance pi ~ 1/d; Thm 3.3 flux<->K4, ring dispersion E_k, cond(eta)=e^{2w(N-1)}; Thm 4.1 all closed forms + floor identity + column-sum; cascade mode eigenvalues + TMSV laws; Ostrogradski H; blowup A=sqrt(30gamma/lambda); Prop 9.6 displaced-osc; Thm 9.2/9.4/9.8 Kato; App A-C). **NUMERICS CLEAN + model-congruent** (all ~17 scripts' models/params match the stated dimer theta=pi/4 t=1.3, PU family gamma=1 omega1=1 omega2=0.5 lambda=0.05, resonance omega1=omega2=1 g=0.15; the prior undisclosed-parameter failure mode is ABSENT; all fast scripts reproduce, long ones hand-checked). **BIBLIO** sound; post-cutoff 2026 IDs standing provisional (unchanged).
- **MINOR applied — Thm 3.3(iii) thm:skin, L618:** "A ring with uniform $w\ne0$ carries flux $Nw$: no fixed beables exist" quantified the fixed-beable non-existence over ALL rings, but the spectral sub-clause is guarded "for every $N\ge3$" and the fixed-beable one was not. At $N=2$ the ring degenerates: the two parallel links between the one site-pair combine to $H_{12}=2t\cosh w=H_{21}$ (Hermitian, zero real phase) so fixed beables DO exist and there is no oriented 2-cycle to carry flux. Added the guard: "A ring ($N\ge3$) with uniform $w\ne0$...". Sibling-sweep: L627 "non-uniform ring with nonzero net flux still has no fixed beables" is self-guarding (a 2-ring carries no net imaginary flux); L620 spectral clause already carries $N\ge3$. Same missing-quantifier failure mode as many prior p1 findings.
- **HELD/noted (not applied):** NIT ChruscinskiRS2018 (PRL 121 080407) cited for the *invertible*-map equivalence though its title is the *noninvertible* case — defensible (the 2018 paper contains the invertible case) + machine-provisional -> HOLD for human confirmation. NIT long \texttt tokens (Code-availability filename, script paths) flagged as overfull RISK — but fresh `-g` build shows 0 overfull >10pt, so no action.
- Recompiled 50pp, 0 undefined, 0 overfull >10pt. Both gates PASS. **p1 -> 0/3 (took a MINOR).**

## W22 WIDE-OPEN AUDIT 2026-07-26 (Opus, adversarial; claims+numerics+biblio) — CLEAN cross-model; NO findings; counter 0->1
- **CLAIMS CLEAN:** every spine re-derived by hand — Prop 2.1 deflation (√n≥spr chain, EP/Jordan case); Thm 3.1 K1-K4 + detailed balance π∝1/d; **Thm 3.3(iii): the W21 N≥3 guard CONFIRMED in place** ("A ring (N≥3)..."; E_k non-real for every N≥3 since Im E_k=2t sinh w sin k≠0; example (a) notes "(K4) vacuous" at n=2, "first bites at n≥3"); Thm 4.1 fully re-derived symbolically (A²=−κ̃², floor identity 2s²σe^{−κ̃t}+sinθ+κ̃>0, EP t_c=1/(s√2), unbroken continuation); cascade eigenvalues ω̄±√(δ²/4−g²) + TMSV laws; channels/Halmos dilation (unitary to 3e-15, C(t) SVs≤1). Abstract↔body↔intro consistent; 0 dangling refs/cites.
- **NUMERICS CLEAN:** ~30 quoted numbers reproduced independently from RHS+constants (naive col sums (3.23,1.30); corrected Γ; min divisor −1.13; norm growth 1.58..77.2; Kolmogorov (b)/(c) full; EP slopes −0.998/−0.499/+0.999; floor −1.2071/t_c 1.3170; Cor central C_α 0.964, T_ℓ ratio 2.154; Table 2 all 8 π/T_cross). Long/stiff scripts (interacting_pu, completion_candidates, 1936-dim PU grid) NOT run per protocol — their exclusive numbers (PU grid −24.55, drift ratios, displaced-osc 1e-9) remain machine-provisional, but every standalone-reproducible number matched.
- **BIBLIO CLEAN:** classic refs all claim-appropriate; standing-provisional post-2025 arXiv IDs (note, no re-alarm); cite-key-year vs pub-year mismatches cosmetic (keys track arXiv year).
- No manuscript change. Both gates PASS (unchanged). **p1 -> 1/3** (first clean cross-model wave after the W21 N≥3 reset; the guard is confirmed correctly present and mirrored in Cor example (a)).

## W23 WIDE-OPEN AUDIT 2026-07-31 (Fable, adversarial; claims+numerics+biblio) - CLAIMS CLEAN; 2 NIT + 1 MINOR; counter -> 0
- **CLAIMS CLEAN on a full from-scratch re-derivation of the whole 50pp spine** (Props 2.1/9.4/C.2, Thms 3.1/3.4/4.1/8.1/8.2/9.6 and the App A-C lemmas, with symbolic re-checks of the generator, the floor identity, 1^T L and the displaced-oscillator identity; blowup balance A = sqrt(30 gamma/lambda) => sqrt(600) = 24.49). Small-N/degenerate cases (n=1,2; N>=3 ring restriction; N=2 excluded) all correctly scoped; the C^2 hypothesis is propagated to Thm 8.2, Cor 8.3 and the App C setup -- the ledger-37/40 propagation failure mode is ABSENT.
- **NIT applied:** results-map status letter "R" (legend: "rigorous, theorem with full proof") over-compressed rows whose theorems carry an Olver-frame / normalization hypothesis. The theorem statements are themselves scrupulously hedged; only the table letter flattened them. Fixed by qualifying the LEGEND ("under the hypotheses stated in the cited theorem -- including, where present, frame or normalization hypotheses such as the Olver frame") rather than re-marking individual rows, which would have asserted a per-row judgement this audit did not establish.
- **NIT applied (biblio):** Smilga2005 read "Benign **versus** malicious ghosts"; Crossref (10.1016/j.nuclphysb.2004.10.037) gives "Benign **vs.** malicious ghosts", and p3/p5 both already carried "vs.". **This is a 4th instance of major-ledger #84** -- and it came from an INSPIRE form, not an arXiv one, which shows the underlying defect is the general "non-publisher source overrides the publisher" error rather than anything arXiv-specific. #84 amended accordingly.
- **NUMERICS: 1 MINOR, a coverage gap rather than a discrepancy.** The kinetic-form-ratio claims and the lambda<0 wall-convergence pair ride on completion_candidates.py, a ~30-min blowup integration the auditor skipped for runtime. Orchestrator re-ran it in-session rather than let the lane be recorded clean on unrun code. **RESULT: gap CLOSED, all four claim sets CONFIRMED** -- 0.9997 definite-escape ratio; ghost null-escape 0.0139-0.0663 (quoted 0.01-0.07); rotated-basis drift 0.158-0.445 (quoted 0.16-0.45); wall convergence 2.90e-08 -> 4.78e-13 (quoted 3e-8 -> 1e-13). p1's numerics lane is now genuinely fully covered. Everything else reproduced exactly and model-congruent (~40 claims across 15 scripts), plus two standalone RHS re-integrations of the quartic PU equation confirming finite-time blowup on both signs.
- **BIBLIO:** 50 entries verified MATCH against raw Crossref/arXiv/Project Euclid incl. every post-2025 id; load-bearing claim-support attributions all checked. Standing machine-provisional (human-PDF before circulation): Halmos Summa Brasil. Math. 2, 125 (1950) -- journal not in Crossref, only the 1983 Selecta reprint is indexed -- and the book-internal chapter/theorem locators. minor-ledger #161.

## W25 WIDE-OPEN AUDIT 2026-08-01 (Fable, adversarial) - **NO CRITICAL/MAJOR/MINOR DEFECT FOUND**; 1 script-header NIT, no paper change; counter -> 1/3
- **The cleanest pass this paper has had.** Every load-bearing result re-derived from scratch: Prop 2.1 both directions including the EP case; Thm 3.1 and Cor 3.2 with the converse spanning-forest construction; Thm 3.3 including why N>=3 is genuinely required; **Thm 4.2 in full** (A^2 = -kappa~^2 1, pq = 1-r^2, the Wronskian identity, L_12, the floor identity, the t_c < t_0 ordering, column sums verified to 1e-9, and both the unbroken and EP continuations); the cascade mode matrix and P(n<=K) = 1 - tanh^{2K+2}(gt); Thm 8.1 with the Feller lemma, the drifted mean-hitting-time formula solved from scratch; **Prop 10.6's displaced-oscillator identity verified symbolically by hand, with BCH terminating and every cross term cancelling as printed**; and a genuine deep read of Appendices A-C (shelf counterexample arithmetic, CE-II, the Khasminskii test, the boundary-form/flux-functor algebra, the n=1 total-reflection argument).
- **Interpretive mechanisms checked in-model** per the new prompt rule that caught #87 and #91 elsewhere: the Nyquist-confinement ratios reproduce the quoted values and the BO channels are confining for lambda>0 by explicit asymptotics. Hedge propagation is consistent; the abstract does not outrun the body.
- **NUMERICS: 17 of 21 scripts run to completion, exit 0, every quoted number reproduced.** Skips named explicitly. One of them -- completion_candidates sections B/C -- **the orchestrator had already run to completion in W23**, confirming all four claim sets, so that coverage gap is closed from the other direction and p1's numerics are now fully covered between the two passes.
- **BIBLIO CLEAN**, 25 entries verified against raw sources including every post-2025 entry and both cases where the published form governs. Only residue is a NIT on a script header, explicitly recorded as needing no paper change so a future pass does not re-flag it as a defect. minor-ledger #176.

## W26 OPUS CROSS-MODEL AUDIT 2026-08-02 - the W25 CLEAN verdict SPLITS: mathematics holds, configuration provenance does not; 6 MINOR applied; counter 1/3 -> 0
- **This is why the clean verdict was re-tested rather than inherited.** Opus re-derived the spine independently and CONFIRMED W25's mathematical result -- including both components of the proof's unproved aside 1^T L = (0, -4 sin theta), t_0 > t_c swept over 4800 (theta,s) pairs with zero violations, Prop bo's displaced-oscillator identity re-derived by hand and correct as printed, and a genuine deep read of Appendices A-C. All four interpretive mechanisms check out as possible in-model.
- **But five quoted numbers are not reproducible from what the paper states**, which W25 did not catch: T_esc = 0.4635 (release from rest at x=2 -- and at least six other (E,x_0) pairs give the same value, so it was genuinely non-recoverable); the equal-frequency run's silent switch to omega = 0.75; **the quartic coupling lambda is never given a value anywhere in the paper** though three quoted numbers depend on it, alongside an unstated grid half-width L = 10 and a "1.74" that is a truncated window at E_0 = 1 rather than the channel time of flight; E = +-8.301 quoted without its time, at a t where truncation already costs ~4%; and a parameter-homogeneity mismatch comparing lambda<0 at N=24-42 against lambda>0 at N=48-64. All five now carry their configuration. **The dichotomy claim itself SURVIVES at matched N** (0.79-1.96 for lambda>0 there), so this is presentation, not result.
- **Biblio:** the ReedSimon2 locator was right for the limit-point use and wrong for the von Neumann extension use; widened to X.1-X.2, X.7-X.10. **Two ItoMcKean section locators HELD** -- the auditor's reads are machine-extracted TOC reads and it asked for print confirmation itself; per this session's ar5iv lesson, not acted on. Six further items held as genuinely unverifiable (Halmos1950 has no Crossref record and its journal is not digitized). **Zero fabrications; 55/61 verified end to end.**
- Root indivisible-ghosts-paper.pdf refreshed. minor-ledger #181.
