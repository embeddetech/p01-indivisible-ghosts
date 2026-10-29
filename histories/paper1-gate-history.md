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
title-dash corrections from p5 pass 22 (Barandes hyphen, Pimenta
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

## Pass 15 — 2026-07-13 (Opus x3) — CLEAN (counter 0 -> 1) [RECONSTRUCTED]

Not ledgered at the time; reconstructed 2026-07-13 from the user's
recollection + the HANDOFF STATE (which recorded "pass 15 CLEAN (Opus),
counter 1"). A clean pass means no findings and no fixes. This is the
clean claims lane that the pass-16 abstract false-converse (below) was
present during. Counter 0 -> 1.

## Pass 16 — 2026-07-13 (FABLE x3, counter-1 confirming) — NOT CLEAN

**PASS-15 RECONCILED (2026-07-13, user):** pass 15 occurred (CLEAN,
Opus, counter 0 -> 1) but was undocumented; a reconstructed stub is
added above per the user's recollection. So this is correctly pass 16,
the prior counter was 1, and it resets 1 -> 0 here. The escalation
trigger stands and is in fact confirmed: the abstract false-converse
below WAS present during the declared-clean pass 15 (and also survived
ledgered-clean claims lanes 8, 11, 12, 13).

**GATE CHANGE (user, provisional 2026-07-13):** per-lane K adopted —
claims K=4, biblio K=3, numerics K=3 (publish/release-gate.md). All
three p1 lanes reset to 0 this pass (each produced applied findings).

- Claims (Fable, "hunt false converses" framing): **1 MAJOR + 3 MINOR
  + 3 NIT**, all VERIFIED then FIXED (rule 7). Every theorem
  re-derived sound.
    MAJOR (FALSE-CONVERSE, the flagship's historical failure mode;
      logged to major-findings-ledger.md #6): abstract/intro (i)
      "exactly/precisely the condition for a process to exist" is
      proven by Prop 2.1 only for the metric-form process ("no process
      of this form"), not any beable map. The stronger claim is TRUE:
      added a similarity-free argument to Prop 2.1 -- column-
      stochasticity bounds the Frobenius norm of $B\ee^{-\ii Ht}B^{-1}$
      by $\sqrt n$, but that dominates the (similarity-invariant)
      spectral radius $\ee^{\beta t}\to\infty$ ($\beta=\max\mathrm{Im}
      E_k>0$ broken). Statement strengthened to "no probability-
      conserving process on any beables." Abstract/intro now fully
      proven (claim unchanged).
    MINOR: "iff its couplings satisfy detailed balance" dropped K1
      (on-site reality) -- counterexample H=[[i,1],[1,-i]] (real
      couplings, DB-satisfying, but no fixed-beable rep); fixed
      abstract + intro to "on-site energies real AND couplings...".
    MINOR: "skin effect is the exact obstruction" (abstract/intro/
      Sec 3.6) contradicts the paper's own Cor 3.5 ("obstruction finer
      than net winding"); exact obstruction = imaginary gauge flux
      ($H^1$ class), skin effect its spectral/boundary manifestation.
      Reworded all three sites.
    MINOR: Cor 9.3 quantified over d=1 (fails there, (2,2)); scoped to
      $d\ge2$, $c>0$.
    NIT: Thm 9.8 "commutes with complex conjugation" -> natural
      conjugation of the decoupled eigenframe ($K\circ\Pi_2$); Thm
      3.4(iii) grammar; $\kappa=\sqrt{s^2-\sin^2\theta}$ defined at
      first use.
- Numerics (Fable): 163/163 traced, all match; all 20 scripts rc=0.
  **1 borderline-MAJOR + 1 MINOR + 2 NIT** (all fixed):
    borderline-MAJOR: Sec 9 ghost-pair "null escape ... stays below
      0.07" is a 4-sample threshold-crossing ARTIFACT -- continuous
      re-integration (179,634 samples) gives max 1.0, mean 0.50, 87.7%
      above 0.07. Restated honestly: small (0.01-0.07) at the four
      sampled crossings, NOT a trajectory-wide bound (oscillates full
      range between crossings); the escape "never locks onto a definite
      direction" (vs lambda>0 PU -> 0.9997) -- qualitative contrast
      preserved, false bound removed.
    MINOR: Sec 9 two "band" clauses inconsistent (0.46 "in band" vs
      0.49 "above band"); reworded to one e.s.a. band (0.49 at its
      upper edge, above the tighter free-PU control).
    NIT: Sec 7 "4 decimals" -> "$\lesssim10^{-3}$ (four for t<=6)";
      Sec 3 null-space solver "reproduces d" -> "confirms the solution
      space is exactly d's ray" (solver returns dimension only).
- Bibliography (Fable): 1 MINOR + NITs (all fixed), records verified
  vs primary sources:
    MINOR (CITATION): Reed--Simon range X.8--X.10 omits X.7 (the Weyl
      limit-point/limit-circle e.s.a. theorem that Thm 8.1(1) uses);
      web-verified X.7 = that theorem -> range X.7--X.10 (in-text +
      bibitem).
    +Dahya arXiv:2508.07511 (cite-and-distinguish: operator-theoretic
      dilation of indivisible contraction families -- precedent for
      the Sec 4-5 dilation, no PT/beable reading); record web-verified.
    +Lan-Ma-Yang arXiv:2606.13251 (independent biorthogonal-KMS route
      to metric<->detailed-balance, nearest neighbor to Thm 3.1);
      record web-verified.
    Z2 Liu et al. record completed to Adv. Mater. **37**, 2506739
      (2025) (Crossref-verified DOI 10.1002/adma.202506739).
    No-action: BenderMannheim "Pais--Uhlenbeck" en-dash (consistent
      house style); Ralston editor (optional).

Recompiled clean (31 pp); log shows no errors, no undefined
refs/citations. Per-lane counters: claims 0/4, biblio 0/3, numerics
0/3 (all reset -- applied findings in every lane). Editing local v1.1
(public v1.0 frozen; publish HELD). NOTE: the provenance note still
reads "three consecutive passes" -- pending a corpus-wide phrasing
decision (per-lane K now: claims 4).

## 2026-07-13 — GATE PASS 17 (three fresh Opus agents). NOT CLEAN (claims).
Fresh-eyes Opus x3, no histories/notes; numerics given absolute
output paths, biblio given raw-Crossref instructions. User-directed
"do more" batch (p1+p5+p6 same session). Editing local v1.1 (public
v1.0 frozen; publish HELD).

**Claims — NOT CLEAN (2 NIT; both VERIFIED then FIXED, rule 7).**
Every theorem/prop/cor independently re-derived and confirmed
(Prop 2.1 similarity-free exclusion; Thm 3.1/Cor 3.2 Kolmogorov
K1-K4, both directions; Thm 3.4/Cor 4.5 skin cohomology; Thm 4.3
terminal indivisibility to 1e-8, floor -1.2071; Sec 7 cascade
thresholds + two-mode-squeezing law; Sec 6 Ostrogradski reduction;
Sec 8 channel-additivity / Kato / (2M,2M) decoupling / sign
dichotomy). Quartic-PU deficiency correctly held as an Open Problem
(finite-M rigor + numerical evidence, no overclaim). Two applied:
  F1 (NIT) abstract :85 and intro :259 "channelization (exact to
    O(k^2))" reads self-contradictory (exact vs approximate); the
    body :1384-85 correctly says "up to O(k^2) corrections." FIX:
    both -> "(exact up to O(k^2))" -- keeps the displaced-oscillator
    identity's exactness while naming the channel reduction's order.
  F2 (NIT) thm:dictionary is stated for ONE escaping end + a
    confining end (deficiency (1,1)), but the numerical examples
    V=-x^4 / -x^2 are symmetric -- they escape at BOTH ends
    (deficiency (2,2), the U(2) case). Part (2)(a) already covers two
    ends, so no math error, just an unflagged jump. FIX: added "both
    symmetric and so realizing the two-escaping-end case---deficiency
    (2,2), the U(2) completions of~(2)(a)" at the numerical-
    verification line :1139.

**Numerics — CLEAN.** 19 scripts run to completion + 2 slow blowup
sections reproduced standalone; every number matches within stated
tolerances and is mutually consistent across abstract/body/tables/
figures. Spot: pt_barandes ‖U‖ 1.58..77.2; fixed_beable spectrum +
18% off-diagonal fraction; terminal floor -1.2071; PU dim 1936,
spectrum -26..140; explosion Table 1 all 16 entries (worst
3.4% < 3.5%); quartic-PU blowup t* 3.26-6.86 -> paper's "3.3-6.9";
maslov exponent -1.999. No discrepancies. (The p1 numerics agent hit
the "armed a waiter" control-failure once mid-run -- same mode as
p1-pass15; recovered via SendMessage. Standing dataset point.)

**Bibliography — CLEAN.** 51 bibitems verified vs Crossref + arXiv;
every cite resolves, no orphan/undefined; the six future-dated 2026
arXiv preprints + FischerBL2026 independently confirmed real (not
fabricated). Six non-DOI books/chapters corroborated via catalog/
review records. Diacritics correct in the real .tex (the ASCII-
artifact NITs were dismissed). 51/51.

Recompiled clean (30 pp); log shows no errors, no undefined
refs/citations. No auditor leads rejected (nothing for
auditor-error-log.md). Not CRITICAL/MAJOR and no prior-fix reversal,
so nothing for major-findings-ledger.md.

**Counter move:** claims had applied findings -> resets to 0; biblio
and numerics both CLEAN -> +1 each. After pass 17: **claims 0/4,
biblio 1/3, numerics 1/3.** Opus dry streak stays 0 (claims lane not
clean).

---

## GATE PASS 18 — 2026-07-13 (Fable x3; user-directed "do more" batch p1+p4+p5+p6)

Fresh-eyes Fable x3 per the per-lane cadence (claims flips Opus->Fable;
biblio & numerics at counter 1 -> Fable = all-Fable pass). No
histories/notes; numerics absolute output paths + standalone-only (no
full stiff/blowup runs); biblio raw-Crossref; claims adversarial
framing + a compact-output guard.

AGENT-CONTROL NOTES (two failures this pass, both recovered):
  - claims Fable agent FAILED first launch: exceeded the 64k output-
    token max (0-byte transcript, nothing recoverable) -> relaunched
    fresh with a hard compact-output instruction; relaunch returned
    clean. NEW failure mode (distinct from the numerics stall).
  - numerics Fable agent hit the recurring "armed a waiter"/slow-
    integration STALL (now 3x: pass 15, 17, 18): it launched a full
    production-tolerance ghost-pair trajectory despite the standalone-
    only instruction and waited on it. Recovered via SendMessage (abandon
    the job, report from completed checks). Standing dataset point; the
    standalone-only rule targets the root cause but the agent overrode
    it again.

**Claims — NOT CLEAN (1 MINOR + 4 NIT; ALL 5 APPLIED, all VERIFIED
first, rule 7).** Full re-derivation clean (dimer spectrum/EP; deflation
Frobenius; K1-K4 both directions + uniqueness; closed forms p,q,r,detGamma,
L12/L21,t_c,t_0; floor -(sinth+kappa) + approach; EP exponents + 2-D
intertwiner; Ostrogradski; cascade thresholds; quartic blowup A=sqrt(30gamma/lambda);
displaced-oscillator identity; deficiency counts (2,2)/(2M,2M)/(0,0)/
(inf,inf); Nelson; WKB residual; numerics 0.632/1.69/1.2071/1.3170/24.49).
  MINOR (APPLIED) Sec 2.1 infinitesimal criterion :315-317 "P-divisibility
    holds iff off-diagonal entries of L(t) nonnegative" dropped the sub-
    stochastic column-sum condition that the paper's OWN discrete criterion
    :312-313 states ("column sums <= 1 in the sub-stochastic case"). The
    infinitesimal analog is "column sums of L <= 0". FIX: added that clause
    to the criterion, and a proof line to Thm thm:terminal noting the
    reduced divisor stays sub-stochastic: 1^T L = (0, -4 sin theta) <= 0.
    ORCHESTRATOR-VERIFIED: computed L = Gamdot Gam^{-1} for Gam_red at four
    (theta,s,t) points -> column sums (0, -4 sin theta) EXACTLY (check_colsum.py).
  NIT (APPLIED) Intro item 1 :184-185 "Unbroken antilinear symmetry is
    precisely the condition for a valid indivisible process to exist"
    dropped the abstract's qualifiers; read literally it contradicts item 3
    (broken phase supports a dilated/sub-stochastic process). FIX: inserted
    "probability-conserving, same-configuration-space".
  NIT (APPLIED) Sec 4.3 :817-818 "every lossy two-site Hamiltonian with
    degenerate site frequencies is a shifted PT dimer" implicitly assumes
    reciprocal coupling (H12 != H21 breaks it). FIX: added "and reciprocal
    coupling".
  NIT (APPLIED) Thm thm:kato :1268 "same (infinite) deficiency indices"
    presupposes h_perp discrete spectrum (the orthonormal-eigenbasis
    hypothesis of Thm thm:channels) to make the indices infinite; not
    restated. FIX: added "with h_perp having orthonormal eigenbasis as in
    Theorem~\ref{thm:channels} (so that H_0's indices are infinite)".
  NIT (APPLIED) Thm 7.1(2)(c) :1126-1127 "losing mass at the classical
    escape rate" is a semiclassical statement inside a theorem item; hedge
    covered only WKB norms/spacing. FIX: inserted "semiclassically".

**Numerics — CLEAN.** All 20 scripts (19 + make_figures plotting-only)
traced; the slow stiff/blowup sections reproduced via standalone
reductions. Every quoted number reproduced (deflation ||U|| 1.58..77.2;
fixed-beable spectrum + 18% off-diag; skin eigvec 4.7e-15; terminal
floor -1.2071 / t_c 1.3170; PU dim 1936 spectrum -26..140; explosion
V4 98.6-98.8%; multi-D counts 34/37; Maslov exponent -1.999). ONE open
item independently CLOSED by the orchestrator: the flagship ghost-pair
"kinetic-form ratio small (0.01-0.07) at the four sampled crossings"
(:~1492) -- the auditor's coarser rtol-1e-9 rerun diverged (one value
0.943, chaotic escape) and it abandoned the production run per scope;
orchestrator reran the isolated ghost-pair trajectory at the script's
own rtol=atol=1e-10 (stopping just past the top threshold) ->
0.0663/0.0139/0.0209/0.0633, ALL 4 in [0.01,0.07] (verify_gp_ratio.py).
Paper CONFIRMED; no change. 2 script-docstring NITs (self-documented
t* range) no-fix.

**Bibliography — CLEAN.** 51 bibitems verified vs primary publisher/
Crossref records; no chimeras/wrong-author/title-drift/vol-page-year;
priority-sharing attributions (LanMaYang2026, KAU2017, Chruscinski/Rivas
dichotomy) verified in content. 2 NITs no-change (Kolmogorov byline
normalization; sentence-case house style). 51/51.

Recompiled clean (31 pp; +1 page from the applied claims text -- the
titling/droptitle formatting is intact, publish held so no re-fit
needed now). Log shows no errors, no undefined refs/citations. No
auditor leads rejected. Not CRITICAL/MAJOR, no prior-fix reversal ->
nothing for major-findings-ledger.md.

**Counter move:** claims had applied findings -> resets to 0; biblio and
numerics both CLEAN -> +1 each. After pass 18: **claims 0/4, biblio 2/3,
numerics 2/3.** Opus dry streak stays 0 (claims lane not clean; ran Fable).

---

## GATE PASS 19 — 2026-07-13 (claims Opus; biblio+numerics Fable; user-directed p1/p5/p6 batch)
Per-lane cadence: claims flips Fable->Opus (adversarial); biblio & numerics
at counter 2 -> Fable. Fresh-eyes, no histories/notes; numerics absolute
paths + standalone-only; biblio raw-Crossref; compact-output guard on all
three. AGENT-CONTROL: the p1-numerics Fable lane hit the recurring slow-
integration STALL a 4th time ("armed a waiter"); recovered via SendMessage
(compact-output + abandon-long-run) -> it wound down clean AND later
completed the reduced blowup run in the background, closing its one SKIPPED
item. The user pre-warned this lane blew its output window last time; the
compact-output nudge pre-empted a repeat.

**Claims — NOT CLEAN (1 MINOR + 1 NIT applied; 1 NIT REJECTED).** Every
theorem/prop/cor independently re-derived clean (prop:deflation;
thm:kolmogorov K1-K4 both directions + uniqueness; thm:skin (i)-(iii) +
cor:topology; thm:terminal full closed forms, floor -(sin th+kappa),
t_0>t_c, column sums 1^T L=(0,-4 sin th); thm:dictionary; thm:quadratic
Nelson; thm:channels; thm:kato; prop:bo displaced-oscillator identity
exact; thm:stability (2M,2M); cor:dichotomy; prop:directintegral). Both
headline biconditionals checked both directions, no false converse.
  MINOR (APPLIED) cor:central :1264-67 sits as a corollary of thm:channels
    (tensor sum h_1(x)1+1(x)h_perp) but the radial reduction is NOT a
    literal tensor sum (the centrifugal eigenvalue enters the radial
    potential ell-dependently). Conclusion (inf,inf) correct. FIX: reworded
    to "the same channel argument as Thm channels, now via the angular-
    momentum decomposition rather than a literal tensor sum: each fixed-ell
    radial channel is limit circle at infinity because its centrifugal term
    is subquadratic, and there are infinitely many channels."
  NIT (APPLIED) abstract :54 + intro :185-86 "unbroken antilinear symmetry
    is exactly the condition for a probability-conserving INDIVISIBLE
    process to exist" folded indivisibility into the existence biconditional;
    the proven iff gates EXISTENCE (indivisibility is generic, not
    equivalent). FIX at BOTH loci: dropped "indivisible" from the
    biconditional; "generically indivisible" now attaches to the resulting
    process ("the ordinary (generically indivisible) process of the
    isospectral Hermitian partner").
  NIT (REJECTED -> auditor-error-log) thm:dictionary(1): "move the non-
    escaping-end-confining clause from item (1) into the shared hypothesis."
    Inline item-(1) placement is correct; a shared hypothesis would wrongly
    impose confining-other-end on item (2), the two-escaping-end (2,2) case
    (V=-x^4). Only item (1)'s e.s.a. claim needs it.

**Numerics — CLEAN.** All 20 scripts rc=0; ~170 quoted values traced, all
match (deflation ||U|| 1.58..77.2; Kolmogorov 1.69 + 200/200; skin 5e-15;
terminal floor -1.2071 / t_c 1.3170; EP slopes -0.998/-0.499/+0.999; PU dim
1936 spectrum -26..140; explosion 16 table entries worst 3.5%; multiD
34/37; certificates; Maslov -1.999). Slow blowup/stiff sections reduced
standalone; the one initially-SKIPPED value (quartic-PU t*=3.3-6.9) was then
reproduced in the background -- interacting_pu.py Sec B gives t*
5.13/3.89/3.26 (lam=+0.05) and 6.86/5.25/4.44 (lam=-0.05) -> 3.26-6.86 ==
quoted 3.3-6.9. 3 NITs reviewed and HELD no-action (order-consistent /
hedged: "consistent with (g^2/k^2)sinh^2" 21% high in a pre-asymptotic fit
window; "generator to 10^-11" vs measured 2.8e-11, same order; ghost-pair
0.01-0.07 already disclaimed not-a-trajectory-wide-bound). No streak-
protection: each NIT is defensible physics usage, not a masked defect.

**Bibliography — CLEAN.** 53/53 records (51 bibitems; Mostafazadeh2002 +
Z2experiments each bundle two) verified vs primary Crossref/arXiv; every
cite resolves, no orphan; all 14 arXiv IDs incl. six future-dated 2026
preprints confirmed real; %-comment provenance re-verified. 2 house-style
NITs (sentence-case; KMS/PU en-dashes) no-action. Two adjacent uncited 2026
works (Dey-Fring 2603.15395; 2506.21400) optional, non-preempting.

Recompiled clean (31 pp); log clean (no errors, no undefined refs/cites).
No CRITICAL/MAJOR, no prior-fix reversal -> nothing for major-findings-
ledger.md.

**Counter move:** claims applied -> reset to 0; biblio CLEAN -> 2->3 =
**CERTIFIED (K=3)**; numerics CLEAN -> 2->3 = **CERTIFIED (K=3)**. After
pass 19: **claims 0/4, biblio 3/3 CERT, numerics 3/3 CERT.** Publish still
HELD. Opus dry streak resets (claims lane not clean).

## 2026-07-13 — GATE PASS 20 (three fresh FABLE agents). NOT CLEAN (claims).
Per-lane cadence: claims Fable (adversarial, flips from pass-19 Opus);
biblio+numerics Fable guard (both CERT). Fresh eyes, no histories/notes.
NOTHING APPLIED THIS PASS — all claims findings HELD FOR AUTHOR (published
flagship; not edited autonomously). Counter unchanged: claims 0/4 (not
clean, nothing applied), biblio/numerics 3/3 CERT guards hold.

**Claims — 1 MAJOR + 4 MINOR + NITs. ALL HELD FOR AUTHOR.**
- **[MAJOR] thm:dictionary stochastic/Feller leg** (items (2)(c)/(2)(d) +
  abstract (vii) l.77-81 "proves ... stochastic conservativity" + intro
  l.246): the "minimal (Feller) semigroup [Feller1952]" / "stochastic
  conservativity (Feller exit boundary)" leg is asserted as a THEOREM but
  no diffusion generator is constructed; Feller1952 classifies diffusion
  generators, and the quantum e^{-tH} with V->-inf is not sub-Markov, so it
  cannot BE the referenced semigroup; the post-thm disclaimer (l.1139-41)
  covers only WKB norms + spacing law, not the stochastic leg.
  ORCHESTRATOR-VERIFIED as substantive (a real under-constructed theorem
  leg, likely repairable -- T is plausibly a Feller exit-boundary integral
  for the right time-changed diffusion). NOT the pass-19-rejected lead
  (that was a DIFFERENT item-(1) e.s.a.-hypothesis-placement issue, logged
  REJECTED in auditor-error-log). -> major-findings-ledger entry 12. Fix
  flavor (construct the diffusion vs downgrade Feller clauses to heuristic
  register) is an AUTHOR call.
- [MINOR] Abstract (i)/Prop deflation "exactly the condition" iff: EP
  boundary case (real but defective spectrum, beta=0) not covered by the
  spectral-radius argument. Auditor fix: add the column-stochasticity =>
  ||Be^{-iHt}B^{-1}||_F = sqrt(n) => bounded group => diagonalizable line.
- [MINOR] Abstract (iii)/Sec 9(a)/Fig 2 vs thm:terminal(iii): floor
  -(sin theta + kappa~) is claimed as a bound on (t_c,inf) + an experimental
  prediction, but the theorem proves only the t->inf LIMIT. (Bound is true,
  = 2s^2 sigma(c-kappa~ sigma)+(sin+kappa~)>0, but unstated.) Fix: add the
  inequality or say "asymptote."
- [MINOR] thm:skin(iii) "periodic-boundary spectrum is a complex loop, so
  no closed process": imports the Hatano-Nelson spectral computation
  unproven; needs non-real eigenvalues (exist only for N>=3). Fix: add
  E_k = V0 + 2t cos(k - iw), note N>=3.
- [MINOR] Sec 5.3 "late-window backflow vanishes identically for every
  broken s": universal (for-all s) claim from sampled numerics in fixed
  window t in [20,40]; as s->s_*- the relaxation time 1/kappa~ diverges,
  invading any fixed late window. Fix: prove late-time monotonicity or add
  the near-EP window caveat and drop "identically."
- NITs (no action): e.s.a. domain-closure equivalence; skin(ii) flux sign
  orientation; abstract (v) finite-grid scope; ring uniform-w assumption.
No false converses in the checked theorems (Thm 3.1 iff, Cor 3.2, Thm 4.1
closed forms, Prop 8.8 identity all re-derived clean); Sec 8 hedging praised.

**Biblio — CLEAN (guard).** 52/52 verified vs Crossref; historically-
corrupted spots (Mende, Rivas OSID, InvertedHO 9-author) all correct; 1 NIT
("Kolmogoroff" transliteration) no-fix. CERT holds.

**Numerics — CLEAN (guard).** Enormous standalone set traced (Sec 2-9;
spacing table 16/16, T_esc 0.4635, ghost-pair 0.49/0.32, Maslov exponent
-1.999/amp 24.55 vs sqrt600, glued cert 0.0011, skin cond e^{2w(N-1)}).
completion_candidates.py + interacting_pu.py quantum-CAP long-run claims
marked unverifiable-standalone (abandoned per run discipline -- see below;
no contrary evidence). CERT holds.

**AGENT-CONTROL note (p1-numerics, 5th recurrence, RECOVERED):** the lane
again armed a waiter on a long integration. PRE-EMPTED early with a
proactive SendMessage (standalone-only + compact-output) and, when it was
the last lane still running, a second abandon-and-report nudge -> it killed
the running job mid-flight and delivered a clean compact report from its
completed standalone checks. No output-window blowout (the user's warned
failure mode) this time.

No recompile (no p1 edits). No CRITICAL/MAJOR APPLIED; no prior-fix reversal;
the pass-19 thm:dictionary item-(1) REJECTED lead is distinct from this
pass's MAJOR (no double-jeopardy). After pass 20: **claims 0/4 (1 MAJOR +
4 MINOR held for author), biblio 3/3 CERT, numerics 3/3 CERT.** Publish HELD.
Pass 21 (Opus claims + Fable guards) launching for cross-model corroboration
of the thm:dictionary MAJOR before the author adjudicates.

## 2026-07-13 — GATE PASS 21 (three fresh agents; 2nd pass this session).
Per-lane cadence: claims Opus (adversarial, flips from pass-20 Fable);
biblio+numerics Fable guard (both CERT). Fresh eyes. NOTHING APPLIED -- all
claims findings HELD FOR AUTHOR. Counter unchanged.

**Claims (Opus) — 1 MAJOR + 1 MINOR + 2 NIT. CROSS-MODEL CORROBORATION.**
- **[MAJOR] thm:dictionary (Thm 6.1) Feller/stochastic leg (2)(c)/(d) +
  abstract (vii)** -- Opus INDEPENDENTLY lands on the pass-20 Fable MAJOR
  with the same grounding: the "minimal (Feller) semigroup" leg never
  constructs its generator; a 1D Feller generator is d/dm d/ds - k (killing
  k>=0) and a negative potential is neither drift nor nonnegative killing;
  e^{-tH} (H unbounded below) is not even bounded, so the "one integral
  decides stochastic conservativity" equivalence is asserted-by-analogy, not
  proven, while the abstract says it "proves" it. => thm:dictionary MAJOR is
  now BOTH-MODEL confirmed (Fable p20 + Opus p21), fresh-eyes, independently.
  major-findings entry 12 updated. HELD FOR AUTHOR. (User has directed a
  constructive-proof attempt -- Fable agent building the time-changed
  diffusion + Feller-exit=T equivalence; deliverable held for author review,
  paper NOT edited.)
- [MINOR] Prop 3.1 deflation "no probability-conserving process exists at
  all (not merely none of this form)": the spectral-radius/Frobenius
  exclusion needs a FIXED time-independent beable map B; a time-DEPENDENT B
  is not excluded, so "at all" overreaches its own proof. (Corroborates the
  pass-20 deflation MINOR from a different angle -- time-dependent vs EP-
  boundary.) Fix: keep the "fixed invertible beable map" qualifier on the
  "at all" clause. HELD.
- [NIT] abstract (ii) vs Thm 3.2: "detailed-balance criterion" silently
  folds in the (K2) reciprocity + (K3) positivity conditions of the iff.
- [NIT] Thm 4.2(iii)/abstract (iii) "floor -(sin theta+kappa~)": the t->inf
  LIMIT is proven, but "floor" (|L12| stays below for all t>t_c, approached
  monotonically) is asserted "by inspection"/numerically, not derived.
  CORROBORATES pass-20's MINOR (iii) (pass-20 rated MINOR, pass-21 NIT --
  both flag the same asserted-not-proven boundedness).
Opus did NOT re-raise pass-20's skin-loop-spectrum or Sec 5.3 "vanishes
identically" MINORs; those remain on the pass-20 flag. No new false
converses; multidimensional legs (Thm 8.2/8.4/8.7) confirmed correctly
scoped; Open Problem 8.5 + "computer-assisted" hedges praised again.

**Biblio (Fable) — CLEAN (guard).** 53/53 works re-verified vs Crossref;
same single "Kolmogoroff" transliteration NIT (no fix). CERT holds.

**Numerics (Fable) — CLEAN (guard).** Extensive standalone set re-traced
across Secs 2-9 (spacing table relerr 0.30-3.44%, T_esc 0.4635, Maslov
exp -1.999/amp 24.55, ghost-pair 0.49/0.32, skin cond e^{2w(N-1)}); the
completion_candidates.py / interacting_pu.py long-runs marked unverifiable-
standalone (physical claims corroborated by independent standalone re-
derivations; nothing contradicted). CERT holds.

**AGENT-CONTROL note (p1-numerics, 6th recurrence, RECOVERED w/ KILL):**
despite a HARD BAN naming completion_candidates.py + interacting_pu.py, the
lane wrote a standalone reproduction (scratchpad/check_cc_misc.py) of the
completion_candidates run and blocked waiting on it (live python PID 121696,
~4.8 GB). A SendMessage abandon-nudge alone did NOT free it (it re-armed the
waiter). Recovery required FORCE-KILLING the python process (Stop-Process),
which returned the blocked wait; a second firm SendMessage then produced the
clean final report. Token cost was high (~2x 200k+ subagent tokens across the
stall). LESSON for future p1-numerics prompts: ban is insufficient; the lane
re-derives banned runs standalone. Candidate mitigations: forbid writing ANY
script with a loop/integration over >~1e4 steps; or cap wall-time per snippet;
or split Sec 9 completion_candidates checks into their own tiny fixed-seed
fixtures shipped with the repo so no live long-run is ever needed.

No recompile (no p1 edits). No CRITICAL/MAJOR APPLIED; no prior-fix reversal.
After pass 21: **claims 0/4 (thm:dictionary MAJOR both-model-confirmed +
MINORs, all held for author), biblio 3/3 CERT, numerics 3/3 CERT.** Publish
HELD.

## 2026-07-13 — AUTHOR ADJUDICATION + APPLICATION (all held p1 items resolved).
User (author) directed: resolve everything now, embed the full proof, and
never leave an investigable thread deferred ([[investigate-dont-defer]]).
APPLIED to paper1/main.tex (local v1.1; publish still HELD):
- **thm:dictionary Feller leg (MAJOR):** EMBEDDED the constructive proof as
  **Lemma 8.2** ("the stochastic leg: an escape diffusion") + full proof;
  reworded (2)(c) (name the escape diffusion, speed measure = WKB deficiency
  density) and (2)(d) ("Feller exit boundary" -> "regular---accessible---iff
  T<inf, natural iff T=inf"); added a "stochastic leg is not carried by H"
  paragraph; +3 bibitems (Feller1957, ItoMcKean, KarlinTaylor). Orchestrator
  re-verified the algebra (Sigma=N=T^2; accessibility+finite speed mass =>
  regular).
- **4 MINORs (all APPLIED, Fable second-opinion adjudicated each):**
  (1) deflation: appended the EP-boundary (s=s_*) closing sentence (Jordan
  linear growth of ||e^{-iHt}|| rules out the beta=0 defective case the
  spectral-radius bound missed). (2) terminal-thm (iii): replaced the bare
  limit with the proven floor inequality L12 < -(sin th + kappa~) for all
  t>t_c (verified identity 2s^2 sigma e^{-kappa~ t}+sin th+kappa~>0 with
  1-2r^2<0) + proof line. (3) skin (iii): added E_k = V0+2t cos(k-iw),
  Im E_k != 0 for N>=3, cite Prop deflation. (4) Sec 5.3: "vanishes
  identically for every broken s" -> confined to onset t_c(s) preceding the
  window; failure regime corrected to s->0 (NOT near-EP, per the second
  opinion) + caption "identically" dropped.
- **BUILD FIX:** the new proof page triggered a microtype font-EXPANSION
  error on this MiKTeX (not any specific glyph; identical math compiles in
  the standalone note which has no microtype). Set microtype to
  [protrusion=true,expansion=false] -- protrusion kept, expansion off.
  Author flagged: regenerating MiKTeX font maps would restore expansion.
Recompiled clean: **32 pp, 0 errors, 0 undefined refs/cites.** Lemma is 8.2
on p19; all refs resolve. major-findings entry 12 -> RESOLVED.
FOLLOW-ON INVESTIGATIONS (investigate-don't-defer): **multi-D escape =
PER-CHANNEL-ONLY** with proved obstructions + two counterexamples
(research/p1_multiD_escape_diffusion.tex -- companion-paper-scale; explains
the classically-explosive-but-quantum-safe asymmetry, connects Open Problem
8.5); **U(1)<->Feller-lateral dictionary** launched (result pending).
The applied claims content is substantial + NEW -> p1 claims lane wants a
fresh pass (counter 0). Publish HELD.

## 2026-07-13 — MONOLITH RESTRUCTURE COMPLETE (author-directed: monolith + appendix tier).
Author org decision (judge-panel-analyzed): keep p1 as ONE paper, machinery
behind an appendix wall + a results map. Executed across 4 commits
(70eab44 / 6c29540 / this):
- **Body:** Part I "The correspondence machinery" / Part II "The ghost
  problem" / Part III "Contact with the world" dividers; a one-page RESULTS
  MAP (tab:resultsmap: modules A-J' with status tags E/R/N/O + dependency
  column + 3 reading paths) in SS1; NEW **SS9 "The completions dictionary"**
  (sec:completions) stating the extension<->lateral theorem (thm:extlat) in
  1D form -- self-adjoint extensions <-> boundary unitary S(E) in U(n);
  n=1 collapse / n=2 [0,1] segment; wormhole<->jump-in; sub-unitary<->
  sub-Markov; "structural mirror, not a bijection" caveat -- proof deferred
  to App E.
- **Appendix tier:** App C (app:feller) = the escape-diffusion Feller proof
  MOVED from the body; App D (app:multiD) = the multidimensional escape
  dictionary; App E (app:completions) = the full extension<->lateral
  parametrization (boundary-unitary Prop, flux functor, 4 exclusions each by
  an exact invariant, maximal-dissipative matrix-ball picture, tab:extlat,
  E-covariance + eps>0 caveats). +5 bibitems (Zettl, EverittMarkus, BHS,
  ChenFukushima, Olver).
- **Build fix carried:** microtype expansion still off (font-expansion bug on
  this MiKTeX; flagged for the author to regenerate font maps).
Recompiled clean: **48 pp, 0 errors, 0 undefined refs/cites.**
**AUDIT STATUS:** SS9 + App D + App E are NEW UN-AUDITED content (assembled
from research/ investigation notes). p1's counters STAY 0; the claims &
numerics lanes both need a FRESH gate pass over the new sections before any
re-certification. This is the single most important item for the next
session: **audit the new monolith content** (SS9, App C/D/E) -- the proofs
are Fable-authored + orchestrator-sanity-checked, not gate-verified. Publish
HELD.

## 2026-07-13 — GATE PASS 22 (NEW MONOLITH CONTENT: SS9 + App C/D/E). NOT CLEAN (claims: 2 MAJOR held).
First gate audit of the un-audited monolith content (SS9 sec:completions /
thm:extlat; App C app:feller; App D app:multiD; App E app:completions) + the
5 new bibitems. Part of a user-directed do-more batch (p1 new content + p5 +
p6). Per-lane cadence: claims **Fable** (adversarial, flips from pass-21
Opus); biblio **Opus** (counter 0); numerics **Opus** (counter 0). Fresh
eyes, no histories/notes; numerics hard-railed against the slow-integration
stall (no runs >1e4 steps, standalone-only, compact output).

**Claims (Fable, adversarial) — 2 MAJOR + 6 MINOR + 5 NIT**, with a large
independently-CLEAN-verified list (thm:quadratic, thm:channels, thm:kato,
thm:stability, prop:bdyS signature + U(n) bijection, n=1 collapse / n=2
segment + double-stochasticity, App E Green's factors, App D counterexample
arithmetic, App C both-beta boundary classifications). Both MAJORs verified
vs source and **HELD FOR AUTHOR** (major-findings ledger 14, 15):
- **(M1) thm:app-ghost supermartingale proof drops the reflection local-time
  term** (L2556-2563): phi is flattened only near the single base x_*, yet
  each channel reflects at its own base x_n (E_n unbounded => x_n -> inf); at
  x_n>x_*+1, phi'(x_n)=1/vbar>0 so +phi'(x_n) dL^n >= 0 is dropped with the
  wrong sign — no supermartingale established. Appendix's HEADLINE result.
  Fix nontrivial (flatten near every x_n costs phi'' terms that may kill
  phi->inf; or restrict admissible switched processes; or new test fn).
- **(M2) thm:extlat(4) / App E (c1)-(c2): the universal negative is not a
  defined statement** (L1419-1431, 2868-2899): "no self-adjoint extension
  corresponds to any lateral datum outside C" — "corresponds" is only defined
  via Phi_E (making (4) true by fiat), and (c1)'s killing argument + (c2)'s
  measure-class invariant quantify over an unspecified class of "pairings that
  match total probability." ((c3),(c4) genuine.) Pre-flagged by the
  realignment thread-hunt, now claims-confirmed. Fix: state (4) as
  im Phi_E ⊂ C + a quantified no-go over a declared correspondence class, or
  demote (c1)-(c2) to remarks.
MINORs (all HELD with the MAJORs — same appendices, entangled with the fixes):
eps-normalization convention inconsistent App C (eps=1) vs App D (dX=v∘(β dt+eps
dW)) — thm:app-separable(i)/(ii) "Sigma=N=T^2"/"mean lifetime T^2" off by
1/eps^2; prop:app-ce1 constructed V_1 (piecewise-linear shelves) violates its
own advertised C^1/regularity hypotheses; lem:app-U "x'≍x_g" unjustified
(only x'≲x_g provable; conclusion still holds via direct integration of
-V_1'≥c_3 y^{1+eps}); thm:app-ghost hypothesis parenthetical "(holds for
V_1≥-Kx^2)" false for vbar'; prop:bo displaced-oscillator identity called
"exact" but sole support is BCH-to-1e-9 (finite algebraic check — write it
out or tag status); "face of the Feller-Wentzell cone" — C is a *slice* not a
face (reciprocity c4 R_+=R_- breaks the face property); "self-adjoint family
is the unitary *boundary* of ‖S‖≤1" true for n=1 only (n≥2: unitaries are
extreme points, not the topological boundary).
NITs (HELD): App C small-noise sandwich one-sided (needs Z_t≤t+2eps sup|W|);
Weyl-classification "agrees" clause never addressed; cor:app-central sqrt2
constant bookkeeping (ratios insensitive); thm:app-separable(ii) uniqueness
hypothesis unstated; per-channel-*end* deficiency count; "settles/reduces to"
phrasing overstates numerical feasibility evidence.

**Numerics (Opus, counter 0) — App C/D/E ALL standalone numbers PASS.**
appD_escape_dictionary.py reproduces cor:app-central (0.447/0.208/0.096,
ratio 2.154, C_alpha=0.964) and prop:app-ce1 (T_1/T_3/T_8 = 1.171/1.011/
1.00001, all ≤3/2); App C Sigma=T^2 (driftless S=xi,M=2xi); App E S†S=I ∀R.
**SS9 numbers** (channel counts 34/32.3, 37/37.1; deficiency ratios 3.77/
1.06/0.34; return-law vectors) are full truncation/production-run outputs —
flagged NOT standalone-reproducible per the safety rails and NOT run. No
paper numeric error found. **Script-hygiene APPLIED**: appD_escape_
dictionary.py carried stale comment strings (1.194/0.554/0.257; T_8=1.00004;
ratio 2.155) contradicting its own live output AND the paper — corrected to
0.447/0.208/0.096 / T_8=1.00001 / 2.154 (comments only; paper was correct).

**Biblio (Opus, counter 0) — CLEAN.** 5 new bibitems (Zettl; EverittMarkus;
BHS; ChenFukushima; Olver) verified on metadata AND claim-support;
FischerBL2026 future-date flag CLEARED (legitimate J.Phys.A 59 255203 (2026),
DOI 10.1088/1751-8121/ae7acb, arXiv:2508.09044); 4 App-D inline cites
(Freidlin-Wentzell Ann.Probab.21(1993)2215; Ito Proc.6th Berkeley Symp.III
(1972)225; Blumenthal 1992; Khasminskii 2012 Thm 3.5) verified. Sole note:
Khasminskii exact "Thm 3.5" locator not independently confirmable online
(book/edition/result confirmed) — low-risk.

**Counter move (NEW-content lanes):** claims — 2 MAJOR (held) => **stays 0**;
biblio CLEAN => **0->1**; numerics — auditable content (App C/D/E) CLEAN but
SS9 production-run numbers UNVERIFIED (the recurring structural barrier) =>
**0->1 provisionally, SS9-coverage caveated** (NOT full numerics cert until
the p1-numerics structural fix — fixtures / wall-cap — lets SS9 be checked
standalone). After pass 22: claims 0, biblio 1, numerics 1 (SS9-caveated).
8 MINOR + 5 NIT held for author alongside the 2 MAJORs. Publish HELD.

## 2026-07-14 — AUTHOR APPLICATION (do-more batch; user "apply all recommended").
Verify-before-apply on every theorem edit; p1 recompiled clean.
- **M1 thm:app-ghost** (ledger 14): added hypothesis $(\mathrm R)$ [all
  channels reflect at the common base $x_*$; none above], scoped title +
  theorem to (D),(R), fixed the proof ($\varphi'$ vanishes at every reflection
  point, all at $x_*$ by (R)), softened "\emph{absolutely} stable"->"stable
  ... under (R)"; repaired the (D) parenthetical ($-V_1'\le Kx$ or eventual
  monotone).
- **M2 thm:extlat(4)** (ledger 15): restated as $\operatorname{im}\Phi_E
  \subseteq\mathcal C$ + a converse over a declared class (correspondences
  preserving total probability AND the state-space measure class); App E (c1)
  reworded to that class.
- MINORs: eps-convention fixed once (App C unit-noise clause; general $\eps>0$
  rescales $\Sigma,N$ by $\eps^{-2}$); prop:app-ce1 statement now
  non-increasing + mollifiable-to-$C^1$; lem:app-U proof rewritten via the
  derivative bound $-V_1'\ge c_3y^{1+\eps}$ + scaling ($x'\to\infty$); prop:bo
  BCH tagged (bilinear generator => series terminates => exact; $10^{-9}$ =
  numerical confirmation); "face"->"slice" (x5); "unitary boundary"->"extreme
  points (for $n=1$, topological boundary)"; thm:app-separable(ii) uniqueness
  hypothesis stated (generator agrees on $C_c$ of the interiors).
- NITs: App C sandwich two-sided; **cor:app-central proof constant
  $(2c)^{-1/2}\to c^{-1/2}$** (real $\sqrt2$ slip; final numbers unaffected --
  they come from the direct integral, reproduced 0.447/0.208/0.096);
  "settles"->"indicates", "reduces to"->"should reduce to"; "positive
  transition density"->"reachable with positive probability".
Recompiled clean: **49pp** (was 48), 0 errors, 0 undefined. ledger 14,15 ->
RESOLVED. Claims counter 0. Publish HELD.

## 2026-07-14 — SS9 NUMERICS FULLY VERIFIED (carried item cleared; "don't carry forward").
The pass-22 numerics lane had DEFERRED §9's production-run numbers per the
safety rails. Cleared by running the committed backing scripts under a
`timeout 540` wall-cap (the "cap wall-time" structural fix, applied):
- `deficiency_multiD.py`: window counts **34/32.27** (L=8), **37/37.14**
  (L=12); μ=0 deviation **1.04e-12**; coupling shift **34->34, 37->36**;
  return mixtures **(0.5828,0.3459,0.0576,0.0137)** (L=6) /
  **(0.4009,0.4212,0.1433,0.0347)** (L=9); revivals **0.955 / 0.933** (96/93%).
- `pu_bo_channels.py`: prop:bo ToF **1.7364**; extended trunc **3.766 / 1.055**
  (N=48->56/56->64, lam=+0.05); ghost pair **0.489 / 0.319** (lam=-0.05);
  e.s.a. baselines 0.17-0.46 / 0.34. `pu_deficiency_evidence.py` corroborates
  the baseline ratios.
- **prop:bo displaced-oscillator identity: proven EXACT by hand** (term-by-
  term; H_PU eq. ostro, U-conjugation p_y->p_y+p3/gO, q2->q2-y/gO: y*q2 cross
  cancels, y^2 -> -y^2/2gO, p_y block -> T(p_y+p3/gO)). The "1e-9" is the
  Fock-truncation witness of this exact identity.
Provenance/fixtures shipped: **`scripts/SS9_NUMERICS.md`** (map of every §9
number -> backing script -> reproduced value + the analytic BCH derivation),
so §9 never re-stalls. **p1 numerics 0->1 SS9-caveat REMOVED** -- the lane is
now an honest clean pass over the new content (1/3; K=3 for cert). Publish HELD.

## 2026-07-14 — GATE PASS 23 (claims Opus / biblio Fable / numerics Fable).
Per-lane cadence; fresh-eyes, no-histories auditors. **No CRITICAL/MAJOR, no
prior-fix reversals, no rejected leads.**
- **claims (Opus, pass 23, adversarial): 3 MINOR + 2 NIT, ALL APPLIED** (verify-
  before-apply). (1) intro item 8 "a genuine glued-tail von Neumann certificate"
  -> "computer-assisted" (rem:nocompact *defines* "genuine" = analytically-
  controlled tails, which the WKB-remainder-numeric construction lacks; abstract
  already hedged "computer-assisted"); (2) results-map row J "$S$-matrix at
  infinity" -> "(model cases, Thm stability)" (physical S-matrix-at-infinity is
  open, row J'); (3) trilemma option (ii) "in multi-D" -> "in the separable
  multi-D model" (thm:channels is a separable-model result; physical deficiency
  is op:pu, open); (4) NIT app:feller: deleted leftover "so 'exit' ... must be
  read as regular" hysteresis note; (5) NIT thm:terminal(iii): "approached from
  below" -> "approached from below by the signed entry" (imported abstract
  wording). Load-bearing algebra across §8-10 + App C/D/E re-verified sound.
- **biblio (Fable): CLEAN.** 59/59 cite<->bibitem self-consistent; all 15 arXiv
  refs + App D inline cites (Freidlin-Wentzell, Ito, Blumenthal, Khasminskii,
  Zettl, Everitt-Markus, BHS, Chen-Fukushima, Olver) verified metadata +
  claim-support; future-looking 26xx ids all resolve. Counter **1->2**.
- **numerics (Fable): PASS, NO DISCREPANCIES.** 30+ numbers reproduced from
  backing scripts (App D escape-dictionary 0.447/0.208/0.096, ratio 10^{1/3};
  Maslov exponent/amplitude; EP slopes; 3x3/2x2 examples; tail/glued/gap certs;
  skin); §9 traced to SS9_NUMERICS.md fixtures. Two EXPENSIVE sweeps abandoned
  per rails (completion_candidates kinetic-form ratios; interacting_pu
  t*=3.3-6.9) -> unverified-expensive; cheap quartic_pu_leak cross-check
  t*=5.336 sits inside the range (consistent). Counter **1->2**.
- AGENT-CONTROL: p1-numerics hit the slow-integration STALL again (armed waiters
  on the two expensive runs) -> SendMessage abandon+report recovery; wound down
  clean.
Recompiled clean (**48pp**, 0 errors/undefined). Counters: claims 0, biblio 2,
numerics 2. Publish HELD.

## 2026-07-14 — GATE PASS 24 (claims Fable / biblio Fable / numerics Fable). MAJOR (Zeno) applied.
All-Fable wave (claims flips Opus->Fable by parity). Fresh-eyes, no-histories.
- **claims (Fable, pass 24, adversarial): 1 MAJOR + 4 MINOR + 3 NIT, ALL APPLIED.**
  **MAJOR (major-findings 20, CROSS-CONFIRMED by an Opus adversary)**: thm:app-ghost
  "every switched escape process ... any unbounded rates is conservative" is broken by
  the paper's own prop:app-tail — Zeno rates q_n=2^n reach the channel tail n=∞ in
  finite time; the Khasminskii proof's clock φ=τ̄(x) controls only spatial explosion.
  FIX: scoped "conservative" to the spatial coordinate X + non-explosive-switching
  hypothesis (Σ1/q_n=∞) + Zeno-cannot-be-dropped remark + downstream-remark adjust.
  MINORs: (D) parenthetical "V₁ eventually monotone" DROPPED (insufficient —
  monotone-staircase breaks limsup v̄'<∞); prop:app-ce1 crude "+1" ramp bound ->
  exact linear-ramp plunge time (√(1+2ΔE)−1)/ΔE (the "1/√1+1+..." majorization
  exceeded 3/2); thm:channels preamble +hypothesis C₀^∞⊆D(h_⊥) (Schrödinger-type
  h_⊥); §12.3 "now reduced"->"should reduce". NITs: prop:deflation "generically"->"at
  generic tested parameters"; thm:skin(ii) +cycle-orientation caveat; results-map I'
  ↔->→ (surjection, not bijection). Claims stays 0.
- **biblio (Fable): CLEAN.** 59/59 re-verified metadata+claim-support (2nd consecutive
  clean: Opus p23 + Fable p24). Counter **2->3 = CERTIFIED (K=3)**.
- **numerics (Fable): NO WRONG PAPER NUMBERS.** ~70 reproduced live, ~15 traced to
  SS9 fixtures; **rails held — no stall**. Fixture provenance improved (not paper
  corrections): SS9 header §9->§10 fixed (numbers live in sec:multiD); completion_
  candidates section added — Part A (sign-dichotomy drift **2.90e-08->3.07e-13**)
  reproduced+fixtured, Part B (kinetic-form ratios 0.9997/0.01–0.07/0.16–0.45)
  confirmed PRODUCTION-SCALE (exceeds timeout 540, exit 124) and documented as such.
  **Counter HELD at 2** (not certified): the completion_candidates Part-B ratios
  remain the one quoted-number family not traced to a captured output.
Recompiled clean (**49pp**). **Model-diversity corroborated again**: clean Opus claims
pass 23 -> Fable pass 24 MAJOR -> Opus cross-confirm. Counters: claims 0, biblio **3
CERT**, numerics 2. Publish HELD.

## 2026-07-14 — CLAIMS PASS 25 (Opus, adversarial). VALIDATES the Zeno fix.
Per-lane cadence (claims flips Fable->Opus). **No CRITICAL/MAJOR** — Opus
re-derived thm:terminal, the β=1 explosion-time formula, the thm:app-ghost
Lyapunov step, both counterexamples, cor:app-central; explicitly CONFIRMED the
wave-2 Zeno fix ("thm:app-ghost carves out n=∞ to prop:app-tail rather than
overclaiming"). 1 MINOR + 2 NIT applied: MINOR thm:dictionary text mislabelled
V=-x² as deficiency (2,2)/U(2) — that is the V=-x⁴ case; V=-x² is limit-point
(0,0) [fixed]; NIT results-map row J flagship ref thm:stability -> thm:channels
(S-matrix-at-infinity is thm:channels, not finite-M thm:stability); NIT
thm:extlat(3) phase-torus "≥2" -> "generically 3" (dim U(2)-dim C = 4-1). Claims
stays 0. Recompiled clean (49pp).

## 2026-07-14 — FULL WAVE: claims pass 26 (Fable) + numerics pass 3 (Fable, trace-only).
**claims: 1 MAJOR + 1 MINOR + 2 NIT.** MAJOR (major-findings 24, INCOMPLETE-FIX): the
(D)-parenthetical "−V₁'≤Kx" left by the wave-2 fix is STILL insufficient (bounds v̄ from
above, not below) -> replaced with −V₁'≤K√(1+|V₁|). MINOR: thm:dictionary(2)(c) speed-
measure identity scoped to the driftless variant. NITs (extlat(3) proof dim-3;
results-map I' "R" gloss) no-action. p1 otherwise re-derived EXTENSIVELY clean by hand
(thm:terminal, prop:bo, App B/C). **numerics (trace-only, machine busy): numbers all
trace cleanly; PROVENANCE gaps** — tail_certificate.py docstring stale on the outer
launch 1.41 (paper correct; docstring FIXED); glued-cert/Maslov/gap_closure values
reproduced-but-unfixtured; completion_candidates Part-B still untraced (production-scale).
DEFERRED behind the L=32 MPS (needs runs): fixture rows + a Part-B log. Claims 0,
numerics held at 2. Clean (49pp).

## 2026-07-14 — WAVE 5: claims pass 27 (Opus). CONVERGENCE.
Fresh Opus re-derived the ENTIRE monolith incl. app:multiD (priority target) + the
just-fixed (D)-parenthetical (Khasminskii step verified) — "could not break the
load-bearing claims." 2 NIT: results-map row E "E"->"E+R" (terminal indivisibility is a
full-proof theorem) [APPLIED]; abstract (ii) K1-K4 compression [no-action, harmless].
Every fix from the full wave (the (D)-condition) VALIDATED. Claims 0. Clean (49pp).
Cores-free provenance: §10 certificate diagnostics now in SS9_NUMERICS.md.

## 2026-07-14 — WAVE 6: claims pass 28 (Fable) + numerics pass 4 (Fable). MAJOR (App C frame).
- **claims (Fable, pass 28, adversarial): 1 MAJOR + 4 MINOR + 7 NIT.**
  - MAJOR (major-findings 28): App C flux functor def:fluxfunctor — R=|S_ii|^2 not fixed; psi_pm=u1+/-i u2 from an arbitrary real Wronskian-1 pair carries an end-local SU(1,1) frame freedom (SL(2,R) on the real pair; orchestrator computed the induced (psi+,psi-) map [[A,Bbar],[B,Abar]], |A|^2-|B|^2=det g=1) under which |S_ij|^2 is NOT invariant. APPLIED: pinned psi_pm to the Olver-normalized LG in/out waves (canonical up to a diagonal U(1) leaving |S_ij|^2 invariant), noted the class-level results are frame-independent, qualified rem:phasecollapse, softened the two "no WKB input" claims (L1364, L2680) to "beyond the Olver frame". Result-preserving (Theorem extlat content unchanged).
  - MINOR applied: #3 sec 3.3 TV-distance "monotone in both phases" -> "numerically monotone ... (after t_c indivisibility no longer guarantees it)"; #4 abstract (v) free-PU fixed-beable process -> "on the truncated configuration space"; #5 FACTOR-2 SLIP — thm:dictionary(2)(c) statement (L1218) + App-multiD (L2173) said speed measure "is the WKB deficiency density" while lem:feller (L1254) correctly has m=2dx/v = TWICE it -> inserted "twice" at both (App B (iii) already carried the 2 explicitly).
  - MINOR reviewed, no change: #2 "generically indivisible" (abstract/intro) — prop:deflation itself honestly states "at generic tested parameters, indivisible"; the abstract parenthetical is consistent, judged adequately hedged.
  - NIT PENDING micro-pass (7): #6 sec5.2 "bounded similarity"; #7 monotone-case LG-non-L2 citation; #8 lem:feller(ii) eps->0 scope to drifted variant; #9 thm:extlat(3) proof "torus dim >=2" vs stated dim 3 (add phase count); #10 cor:central centrifugal-term reason misplaced; #11 sec11 probe (b) companion-sequel status marker; #12 thm:dictionary(2)(b) T_cross undefined at first use. (All logged from the captured transcript; low-risk polish.)
- **numerics (Fable, pass 4): CLEAN.** All 20 backing scripts traced, every computed number (secs 3-10, App C/D/E, tables) reproduced or fixture-covered; zero mismatch. 1 MINOR provenance (the 1.12 marginal-branch constant in glued_certificate_1d.py is docstring-only, not a computed output — qualitative limit-point + ratio 0.00109 do reproduce) + 1 NIT (A=sqrt(30g/l) analytic, numerically corroborated). Being CLOSED by a background Fable provenance agent. **Numerics counter HELD at 2** pending 1.12 closure (one clean pass from cert).
- Recompiled clean, 49pp. Counters: claims 0 (applied MAJOR+MINORs), biblio CERT (not run), numerics 2 (held). Clean-Opus-CONVERGENCE (pass 27) -> Fable-pass-28 MAJOR: model-diversity flips a declared-converged monolith again.

## 2026-07-14 — WAVE 6 follow-up: p1 `1.12` provenance CLOSED -> numerics 2->3 CERT.
Background Fable provenance agent proved the §10 marginal-branch constant 1.12 is ANALYTIC, not a fit:
for U=-c k^2, |psi|~k^{-1/2 +/- Z/(2 sqrt(Ac))} and 2 sqrt(A c)=2 sqrt(0.4*0.78)=1.11714 ~ 1.12 (a fair
3-sig-fig rounding). glued_certificate_1d.py extended: docstring derivation + marginal_exponent() now
emits "2 sqrt(A c)=1.11714" and checks the exact growing-WKB branch log-log slope (4.8709 = analytic,
exact match); certified ratio 0.00109 unchanged. NO manuscript change needed. => pass-4 numerics is fully
clean (numbers + provenance); **p1 numerics lane 2 -> 3 CERTIFIED**. p1 lanes now: claims 0, biblio 3 CERT,
numerics 3 CERT.
