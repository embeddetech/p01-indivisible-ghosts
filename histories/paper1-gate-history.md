# Paper 1 release-gate ledger (K=2 gate era)

Pre-gate history: histories/paper1-history.md (the original audit
rounds, including the four-round-surviving "doubly stochastic iff
unitary" false-iff found via paper 4 and fixed in v1.1).

## 2026-07-12 — GATE PASS 1 (three fresh Opus agents). NOT CLEAN.
Counter: 0. First K=2-gate pass for the flagship (v1.1, 29 pp,
19 scripts + figures). Totals: claims 2 MINOR + 1 NIT (no
crit/major; ALL eight theorem groups re-derived clean, incl.
adversarial counterexample attempts on every biconditional);
numerics 1 MAJOR + 1 MINOR (~95 traced, 93 exact; all scripts
rc=0, all 8 figures regenerate; runtimes logged, longest
completion_candidates ~17 min); biblio 2 MAJOR + 1 MAJOR-
engagement + 3 MINOR (all 46 items verified, zero chimeras, all
quotations verbatim, novelty claims SURVIVE adversarial 2024-26
search incl. the full Barandes citation graph).

Fixes applied (factual corrections all primary-source verified
BEFORE editing; see notes.md wind-down entry):
- CLAIMS: abstract (i) now scoped "on the original configuration
  space" (the dilated Gamma_big is probability-conserving in the
  broken phase — the qualifier makes the iff true as stated);
  explosion dictionary scoped to the 1-D monotone mechanism model
  in abstract + intro (vii) with a pointer to Sec-multiD's own
  failure discussion; Thm 6.1 one-line identity now labeled
  WKB-asymptotic (approx, not =; the limit-point/limit-circle
  dichotomy stays exact).
- NUMERICS MAJOR: Sec-10 drift text contradicted its script —
  "largest at the finest truncation N=64 ... trend never decays"
  replaced by the reproducible fact (3.77 at N=48->56, 1.06 at
  56->64, an order of magnitude above the ~0.2 esa baseline at
  every step). Verdict unaffected (ratios stay >> baseline).
  MINOR: beam-launch range corrected to 1.21-1.41 (four at
  1.21-1.29, outer-window launch 1.41 — bracketing, not
  "indistinguishable from", the 1.22 control).
- BIBLIO: "Mendas" -> MENDE (Crossref DOI 10.1016/0003-4916(90)
  90125-8); InvertedHO2026 author list added (9 authors, arXiv-
  verified); Mostafazadeh JMP 43,205 subtitle completed
  (Crossref); Chruscinski attribution corrected (equivalence for
  invertible maps) + Rivas OSID 29, 2250012 (2022) ADDED (full
  title verified untruncated — first extrapolation caught by
  re-query); Pimenta framing reworded (standard Hermitian/unitary-
  generated setting, not "Hermitian maps"); ENGAGEMENT: Errasti
  Diez-Gaset Rifa-Staudt, Fortschr. Phys. 73, 2400268 (2025)
  (Crossref-verified) + Held arXiv:2509.18049 added to the
  Sec-6 recurrence-mechanisms sentence with an explicit
  none-use-the-stochastic-currency delimiter.

Recompiled clean (29 pp). Counter: 0. PASS 2 NOT LAUNCHED (user
hold: session limit; no new passes). On resume: pass 2 with Opus
agents.

## 2026-07-12/13 — GATE PASS 2 (Opus). NOT CLEAN. Counter: 0.
(Entry recorded earlier, see above pass-2 section appended
2026-07-12; fixes applied same session incl. Thm-6.1 monotone
hypothesis, abstract (i) adjudication, completion_candidates
stale-conclusion repair.)

## 2026-07-13 — GATE PASS 3 (three fresh Opus agents). NOT CLEAN.
Counter: 0. Totals: biblio 1 MINOR (T. Liu — the ONLY error in 49
items/52 sub-entries; Smilga2005 "vs." adjudicated CORRECT via
Elsevier record, overruling an arXiv-based child flag); claims
3 MINOR + 2 NIT (zero crit/major, all theorems re-derived again);
numerics 1 MINOR (95/95 traced; 14/14 deterministic scripts
byte-identical; seed-robustness confirmed at 4 fresh seeds).

Fixes applied:
- T.~Liu (Crossref-verified Tingzhi Liu, Adv. Mater. 2506739).
- Backflow claims scoped LATE-WINDOW in abstract + intro + the
  body headline ("backflow-Markovian in the late window yet
  permanently Barandes-indivisible") — the early-window
  conditional backflow is nonzero and printed; the body's own
  late-window scoping now propagated to every locus.
- Pass-2's own fix corrected: "an order of magnitude above the
  baseline at every step" -> "several times to an order of
  magnitude" (second step is 5.3x = half an order; the gate now
  audits its own repairs).
- "certified" -> computer-assisted sense stated inline (numerical
  residual with three-orders margin, not rigorously bounded).
- "generator floor" defined at first use as a floor on the
  indivisibility strength |L12| (signed L12 RISES to the plateau;
  cross-doc note: paper 3 + proposal use the same term — inherit
  the clarification when they enter the gate).
- Prop 9.5 retitled "displaced-oscillator identity (exact) and
  channelization (to O(k^2))".
- Cascade "~4 decimals" scoped to the resolved regime (Fock
  truncation bites at the last tabulated time; script table
  shows 8.30 vs 8.66 at t=12).
Numerics also confirmed the pass-2 completion_candidates repair
now matches its own data, and flagged (no-action) three benign
eigensolver residuals at 1e-12/-13.

Recompiled clean (30 pp). Counter: 0. PASS 4 launching (Opus).

## 2026-07-12 — GATE PASS 2 (three fresh Opus agents). NOT CLEAN.
Counter: 0. Biblio CLEAN (49/49 verified, all pass-1 fixes
re-confirmed, novelty survives 2nd sweep). Numerics: NO manuscript
number wrong (~150 traced; robustness holds under seed/grid
changes); 1 MAJOR = completion_candidates.py printed a stale
PRE-FALSIFICATION conclusion ("both candidates escape null")
contradicting its own 0.9998 table row and the paper's correct
Sec-8 narrative — print + docstring fixed to match data; 1 MINOR =
"leaves the counts unchanged" vs the script's 37->36 at L=12 —
softened with the actual counts in paper + script docstring;
optional precision items applied (spacing "3.5% or better").
Claims: 1 MAJOR + 3 MINOR + 1 NIT — Thm 6.1 now carries the
eventual-monotonicity hypothesis INSIDE the theorem environment
(Rauch-Reed cited as showing it necessary); spacing law marked
semiclassical in-theorem; abstract (i) qualifier ADJUDICATED
between pass-1 and pass-2 agents (pass-1's "on the original
configuration space" was also wrong — beables rotate; correct
distinguishing property is "without enlarging the configuration
space", now stated with the rotation parenthetical); abstract
M->infty step now "conjecturally reduce ... assembly and error
control"; bar-omega collision resolved (Prop-8.6 quantity renamed
Omega_0, 4 sites). NOT applied (session limit, noted for pass 3's
auditors): the intro-enumerate Maslov line still says "reducing"
without "conjecturally" (line ~240) — align on next fix round.
Recompiled clean (29 pp). Counter: 0. PASS 3 ON HOLD (user:
session limit; no new audits).

BOILERPLATE LOG (2026-07-13, rule-3 exception, no counter effect):
the audit-gate provenance sentence now reads "repeated adversarial
audit passes" (user request — the sentence should say the agents
are prompted as hostile referees, which they are); identical edit
across all seven papers, recompiled clean.

## Pass 4 — 2026-07-13 (claims + numerics, Opus; biblio ran pass 3)

- Numerics: 1 MINOR + 3 NIT, no number wrong. All 19 scripts +
  make_figures rerun to completion (exit 0), all 8 figures
  regenerated; 154 numeric claims traced, 151 exact against fresh
  reruns (randomized trials re-passed unseeded, 200/200 and
  50/50); 7 independent robustness re-implementations passed.
  MINOR: "free control never passes r~=6" contradicted the
  script's own probe table (free onset at r=5 AND r=6; "none"
  first at r=7) — fixed to r~=7. NITs: "none growing with
  truncation" failed literally on the monotone nu1=0.7 column
  (0.170->0.382, still inside the e.s.a. band) — reworded to
  "none leaving the essentially-self-adjoint baseline band";
  "0.3% at the largest box" holds only for the -x^4 column
  (marginal -x^2 control: 1.15% at L=16) — scoped; stale t*=5.13
  vs 5.3361 juxtaposition in quartic_pu_leak.py docstring —
  event-criterion note added.
- Claims: 2 MINOR, no correctness error, no substantive
  over-claim ("accept with minor revisions"). Both central
  theorems re-derived by hand end-to-end (Thm 3.1 K1-K4 + unique-
  up-to-scale; Thm 4.2 all closed forms incl. floor, t_c, t_0,
  continuations); biconditionals probed in the non-obvious
  direction, no false converse. MINOR 1: abstract's bare
  "certify" read theorem-grade vs body's "computer-assisted, not
  rigorously error-bounded" — abstract now says "in a computer-
  assisted sense". MINOR 2: completion_candidates.py Section B
  (no max_step on a (t*-t)^-2 blowup) can look stalled for tens
  of minutes and the Code-availability blanket "seconds to
  minutes" undershot it — runtime claim scoped honestly (two
  long scripts called out) + RUNTIME NOTE in the docstring
  (integrator left untouched: the printed numbers were verified
  by two complete exit-0 reruns this pass; changing stepping
  would invalidate that verification for a cosmetic gain).
- Cross-lane note: claims' r~=6 NIT = numerics' MINOR (already
  fixed); claims independently reproduced Sec-C drift ratios
  0.158-0.445 and Sec-B limits with its own guarded integrator.

Recompiled clean (30 pp). Counter: 0 of K=3. PASS 5 NOT launched
(user hold: account switch; no new subagents). K=3 + Fable-
confirming-pass policy in force as of this date.

## Pass 5 — 2026-07-13 overnight (Opus x3)

- Bibliography: CLEAN. All 49 bibitems verified against primary
  records (43 fresh fetches + 6 standard references); all three
  %-comments independently re-confirmed (Rivas jref, ErrastiDiez
  DOI, BottomlessPotentials 4th author Mende); RauchReed both-
  directions characterization verified against the source; prior-
  art sweep: all four novelty claims unpreempted through mid-July
  2026. Two hyphen/en-dash NITs = deliberate house style,
  no-action.
- Claims: 1 MINOR + 2 NIT, no correctness error. Every theorem
  re-derived including Thm 4.2's floor identity proved exact
  (L12+(sin theta+kappa~)<0 for all t>t_c). MINOR: abstract/intro
  "exact channelization" overstated Prop bo's own calibration
  (identity exact, channelization to O(k^2)) — reworded at both
  sites, exactness now attaches to the displaced-oscillator
  identity. NIT: Frobenius norm never defined — defined at first
  use (verified np.linalg.norm default = Frobenius in the
  scripts). NIT "E=10 -> E=11" REJECTED with evidence: the script
  runs V3 (eigenvalue sweep) at E=10 and V2 (spacing table) at
  E=11 — the manuscript matches its script at both sites.
- Numerics: CLEAN verdict, 2 NIT applied. ~180 numbers traced,
  all match; all 8 figures regenerated and content-verified.
  NIT-1: fig_cascade caption said the normal twin "stays bounded
  near 10^-3"; VERIFIED by independent recomputation of the
  figure's own 1156-dim diagonalization (peak <n1> = 0.023 at
  t~7.9; 0.0027/0.0096 at t=6/12, matching the agent) — caption
  now "bounded below 3x10^-2". NIT-2: stale handoff-era section
  labels in 7 scripts' docstrings/prints — mapped to paper
  sections (handoff 4.2->Sec 2, 5.1->3, 5.2->4, 5.3->5, 5.4->6,
  5.4-B->7-8), provenance retained; all 7 scripts parse OK.

Recompiled clean (30 pp). Counter: 0 of K=3. PASS 6 launching
(Opus x3). Note for the morning: three consecutive passes now
report zero correctness errors; all remaining findings are
wording-calibration and label hygiene.

## Pass 6 — 2026-07-13 overnight (Opus x3)

FIFTH consecutive pass with zero correctness errors.
- Bibliography: CLEAN (all 49 records re-verified independently;
  %-comments re-confirmed; prior-art pillars clear; optional
  KAU2017-arXiv-ID suggestion explicitly no-action — left
  untouched).
- Numerics: CLEAN (~150 numbers traced, all match; 5 of 7
  make_figures PDFs regenerate BYTE-IDENTICAL, other two differ
  only in PDF metadata hash; working tree restored clean; the
  3.44% margin on "3.5% or better" noted as thin but holding).
- Claims: 3 NIT, no correctness error (every theorem re-derived
  again; Thm 4.2 floor language verified subtle-but-correct).
  Applied: (1) Thm 9.3 hypothesis tightened to "limit circle at
  both +-infinity" with the parenthetical scoped per-end — the
  physical -k^4 channel satisfies it; (2) Thm kato: f,g now
  "bounded and real-valued" (symmetry needs it); (3) E=10 site
  now says "(a tracked-level probe, distinct from the spacing
  window at E=11)" — two passes tripped on the juxtaposition;
  the numbers themselves were always right (script V3 at E=10,
  V2 at E=11).

Recompiled clean (30 pp). Counter: 0 of K=3. PASS 7 launching
(Opus x3).

## Pass 7 — 2026-07-13 overnight (Opus x3)

SIXTH consecutive pass with zero result-level errors.
- Bibliography: CLEAN (all 49 verified a third consecutive time;
  four cosmetic no-action NITs).
- Numerics: CLEAN (~97 values traced; 6 of 8 figures
  BYTE-IDENTICAL, 2 PDE figures pixel-identical; T_esc=0.4635
  independently recomputed; 3.44% worst-case margin noted thin
  but holding under the natural convention). Script hygiene
  applied gratis: completion_candidates stale "(~4-6 minutes)"
  Run line (leftover of the pass-4 RUNTIME NOTE edit) now points
  at the note (~30 minutes observed).
- Claims: 1 MINOR + 1 NIT, no result-level error. MINOR: the
  displayed Maslov ray equation mixed normalizations
  (s''''+gamma Omega s''+gamma Omega_0^2 s = 4 lambda s^3 is not
  the PU law and its dominant balance gives S=sqrt(30/lambda),
  contradicting the quoted sqrt(30 gamma/lambda)); invisible at
  the script's gamma=1 — fixed to the divided form
  (4 lambda/gamma) s^3, which reproduces the quoted amplitude;
  maslov_feasibility docstring/print relabeled to
  sqrt(30 gam/lam), output verified unchanged (24.4949). NIT:
  Thm 8.1(1) now states the non-escaping end is confining/limit
  point (e.s.a. is two-ended on the line).

Recompiled clean (30 pp). Counter: 0 of K=3. PASS 8 launching
(Opus x3).

## Pass 8 — 2026-07-13 overnight (Opus x3) — CLEAN (counter 1)

FIRST FULLY-CLEAN PASS for paper 1 (and its 7th consecutive pass
with zero result-level errors).
- Claims: CLEAN, zero findings. Every theorem re-derived from
  scratch again; the agent PROVED t0>t_c across the whole broken
  phase (reduces to s^2>0) and confirmed the floor is a genuine
  infimum to 12 digits; both cascade thresholds re-derived from
  the Heisenberg mode matrices; every biconditional checked in
  the non-obvious direction. Two no-action observations (w-sign
  bookkeeping cosmetic; WKB "~" clearly labeled in-environment).
- Numerics: CLEAN, zero findings. ~130 values traced; 4 figures
  byte-identical, 4 pixel-identical (metadata/ULP only); no
  expectation contamination; working tree restored.
- Bibliography: CLEAN, zero findings (4th consecutive all-49
  verification; optional Barandes 2309.03085 explicitly
  no-action).

Counter: 1 of K=3. PASS 9 launching on FABLE (counter-1
confirming pass per model policy).

## Pass 9 — 2026-07-13 ~02:50 (FABLE x3, counter-1 confirming) — counter RESET 1 -> 0

ESCALATION TRIGGER #4: the numerics MAJOR below existed during
declared-clean pass 8. Queued for the morning ruling with
triggers #2 and #3.

- Bibliography (Fable): CLEAN (49/49 vs primary records incl.
  Springer-source Rauch-Reed verbatim; full-text Pimenta scope
  check; Doukas/Hao-Chan-Lee adjacents cleared; three %-comments
  re-verified).
- Numerics (Fable): 1 MAJOR + 1 MINOR + 1 NIT, all APPLIED.
  MAJOR: "growing branch ... k^{+Z/1.12}, non-L2 precisely for
  Z>1.12" was FALSE — |psi| ~ k^{-1/2+Z/1.12} has density
  k^{2Z/1.12-1}, divergent for EVERY Z>0; the threshold reading
  would make -0.78k^2 limit-circle for small Z, contradicting
  Thm dictionary(1). Arithmetic independently verified
  (2*sqrt(0.4*0.78)=1.117) before applying. Fixed in main.tex
  (now cites consistency with the dictionary) + the
  glued_certificate_1d.py docstring. Constant 1.12 itself
  correct; Z=6 run conclusions unaffected. MINOR: slope bound
  +-0.002 -> +-0.0025 (worst actual 0.00243). NIT:
  pais_uhlenbeck docstring 1296 -> 1936. ~150 other numbers all
  exact; figures byte/pixel-identical. Also noted: my commit
  ba64d99 swept in a byte-identical fig_skin.pdf regenerated by
  a concurrent audit lane — no content drift, logged for
  transparency.
- Claims (Fable): LANE DIED MID-RUN — session limit (resets
  4:50am). RELAUNCH after reset to complete pass 9's record,
  then pass 10 (Opus, counter 0).

Recompiled clean (30 pp). Counter: 0 of K=3.

## Pass 9 — CLAIMS LANE CLOSED (Fable relaunch, 2026-07-13 morning)

Pass 9 final: biblio CLEAN, numerics 1 MAJOR + 1 MINOR + 1 NIT
(applied earlier: Z-threshold, slope bound, docstring dim),
claims 1 MAJOR + 2 MINOR + 3 NIT (applied now). Counter 0.
The claims MAJOR extends escalation trigger #4's scope (all
findings existed during declared-clean pass 8).

- MAJOR: Thm skin(iii) claimed "no closed process exists at all"
  for ANY ring with uniform w, but the theorem's generality
  admits non-uniform hoppings/potentials whose spectrum stays
  real (VERIFIED: 3-ring, w=0.1, hoppings (1,1,0.01) — spectrum
  fully real; uniform control loops with Im=0.17). The paper's
  own diagonally-dominated-triangle numerics conceded this.
  FIX: spectral-loop/no-closed-process claim now scoped to the
  UNIFORM ring, with the non-uniform hedge naming the triangle
  example.
- MINOR: Thm dictionary hypothesis now carries the C^1 +
  |V'||V|^{-3/2}-bounded regularity clause so the cited RS
  X.8-X.10 criteria literally apply (the bare-monotone class
  needs a minorant construction the paper never states; all
  examples satisfy the clause). MINOR: the "every lossy two-site
  Hamiltonian is a shifted PT dimer" parenthetical now requires
  degenerate site frequencies (detuning adds a real sigma_z the
  PT form lacks).
- NITs: imaginary flux = HALF the cycle affinity (ratios are
  e^{2 sum w}); n=2 case (a) gains the decoupled
  H12=H21=0 branch; Prop deflation now carries its promised
  proof (h Hermitian by intertwining conjugation; unitarity;
  broken-phase contradiction) — pledge-consistency.

Everything else in the deepest claims audit yet checked out
exactly (incl. sub-stochastic divisibility verified on the FULL
[0,t_c) definition, and the glued-certificate exponent
re-derivation confirming the pass-9 numerics fix).

Recompiled clean. Counter: 0 of K=3. NOTE: pass 10 (in flight)
audits the PRE-fix text — its reports will be used as
information only; the streak restarts at pass 11 on the fixed
text.

## Pass 10 — 2026-07-13 morning (Opus x3) — INFORMATIONAL

Launched during the K=3 sprint in parallel with the pass-9 Fable
claims relaunch; the pass-9 claims fixes (0e0644d) landed
mid-pass, so pass 10 audited the PRE-fix text and does NOT count
toward the streak. For the record, all three lanes returned
CLEAN on that text: claims CLEAN (Opus — notably it passed the
ring claim that the Fable lane refuted an hour later, the
sharpest cross-model divergence of the program), numerics CLEAN
(~120 traced; 6/8 figures byte-identical, 2 length-identical
modulo PDF nondeterminism), bibliography CLEAN (49/49, fifth
consecutive). None of the pass-9 fixes touched numbers or
bibitems. The counted streak restarts at PASS 11 on the fixed
text (Opus x3, counter 0).

## Pass 11 — 2026-07-13 morning (Opus x3)

COUNTER stays 0 (streak-starter broken by numerics findings).
- Claims: CLEAN — all six pass-9 Fable fixes independently
  verified (own N=6 uniform-ring computation confirmed the
  scoping; deflation proof, regularity clause, affinity factor,
  PT-dimer scope all endorsed); three no-action observations
  (Fock-truncation conjugation artifact warning for reproducers;
  radial channels (1,1) not (2,2), conclusion unaffected; N>=3
  implicit for rings).
- Bibliography: CLEAN (sixth consecutive all-49).
- Numerics: 2 MINOR + 1 NIT, ~170 numbers traced with ZERO
  mismatches otherwise. MINOR-1 (script): interacting_pu.py
  section-C run labels inverted the classical behavior shown by
  the same run's section B (lam=+0.05 bounded at those ICs was
  labeled "malicious"; lam=-0.05 escaping was labeled "benign?")
  — pre-run expectation leftover; labels + interpretation line
  fixed, no manuscript number affected. MINOR-2 (manuscript):
  "the lambda<0 ghost pair remains at baseline up to N=64"
  understated its own data — the 0.489 (N=48->56) ratio exceeds
  every control band; now quotes 0.49/0.32 explicitly, "first
  value above the control bands but both well below the
  limit-circle signature" (honest strengthening of disclosure,
  weaker claim). NIT: quartic_pu_leak.py printed handoff-era
  "section-5.2" -> "paper Sec. 4".

Recompiled clean (31 pp). Counter: 0 of K=3. PASS 12 launching
(Opus x3).

## Pass 12 — 2026-07-13 (Opus x3)

- Bibliography: CLEAN (seventh consecutive all-49).
- Numerics: CLEAN (~90+ traced; ALL 8 figures byte-identical with
  max pixel diff 0; run-label integrity probe added post-pass-11;
  working tree clean without restore).
- Claims: 1 MINOR applied — the pass-9 non-uniform-ring hedge
  needed "with nonzero net flux" (a zero-net-flux non-uniform
  ring is pure gauge = part (i), so fixed beables exist there).
  OPUS caught a FABLE-authored error: complementarity cuts both
  ways; Opus dry streak resets to 0.

Recompiled clean (31 pp). Counter: 0 of K=3.

## PUBLISH EVENT — 2026-07-13 (user-directed)

Post-pass-12 snapshot published to GitHub
p01-indivisible-ghosts (the user's Holmstrom-send version): reorg
URL sweep applied (Code availability -> p01, counter-neutral per
the rule-3 reorg exception) + fix-propagation of the two
title-dash corrections from p4 pass 22 (Barandes hyphen, Pimenta
capitalization, %-comments added); recompiled; clean p1-only tree
assembled (19 scripts + make_figures, AUDIT.md, this ledger,
provenance records, convention README with honest gate status:
"audited through 12 passes, formal gate in progress"); notes.md
and 8 non-p1 scripts REMOVED from the public repo. GitHub hold
lifted FOR P01 ONLY. PASS 13 launching (Opus x3).

## Pass 13 — 2026-07-13 (Opus x3) — session close

- Bibliography: CLEAN (FTT optional-cite no-actioned, matching
  the Fable pass-9 precedent on the same item).
- Claims: 1 MINOR applied — S_M in the stability theorem is minus
  Prop bo's channel operator; clarifying clause added ("standard
  overall sign; deficiency indices invariant under A -> -A").
- Numerics: manuscript-CLEAN (~115 traced, 0 mismatches; 8/8
  figures byte-identical modulo metadata; independent
  perturbation probes at fresh (theta,s) pairs and n up to 8);
  2 script NITs applied: tail_certificate.py stale pre-correction
  "must pass/fail" calibration labels relabeled to the corrected
  closure-defect readings; interacting_pu.py runtime docstring
  updated to observed ~15-20 min.

Recompiled clean (31 pp). Counter: 0 of K=3. SESSION WIND-DOWN:
no pass 14 this session (account switch). The published p01
snapshot is being refreshed to this exact state.

## Pass 14 — 2026-07-13 (Opus x3)

- Bibliography: CLEAN (eighth consecutive all-49).
- Numerics: CLEAN (~95 traced, 0 mismatches; ALL 8 figures
  pixel-identical, mean|delta|=0; deterministic).
- Claims: 1 MINOR + 1 NIT. MINOR = the S_M clause I ADDED in
  pass 13 stated a FALSE general fact ("deficiency indices
  invariant under A->-A"); correct is that A->-A INTERCHANGES
  them (n+(-A)=n-(A)), and S_M being real (conjugation-commuting)
  gives n+=n- so the sign is immaterial. Conclusion (2M,2M)
  unchanged; reasoning corrected. [META: the gate caught the
  orchestrator's own pass-13 fix on the very next pass -- logged
  for the meta-paper as an orchestrator-error-caught event.]
  NIT = Cor 9.9 wrote the lambda<0 confining fiber's lower term
  as "+O(k^2)" (misleading remainder notation for an EXACT
  quadratic, inconsistent with the exact lambda>0 form); now
  "(plus exact lower-order quadratic terms, not a remainder)" --
  descriptive, no explicit coefficient asserted (avoids a
  new-coefficient error).

Recompiled clean. Counter: 0 of K=3. Published p01 refreshed to
this state. Opus dry streak resets to 0 (accepted findings).
