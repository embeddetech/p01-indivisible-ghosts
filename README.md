# indivisible-ghosts

*Paper 1 of the [Ghosts program](https://github.com/embeddetech/ghosts-program).*

![indivisible-ghosts](indivisible-ghosts.png)

**Indivisible stochastic processes for non-Hermitian and higher-derivative
quantum systems: detailed balance, broken PT symmetry, and the explosion
of ghosts** — J. Torkelson (2026). The paper:
[`indivisible-ghosts-paper.pdf`](indivisible-ghosts-paper.pdf), source in
[`paper/`](paper/).

This manuscript is an experiment in AI-conducted research as much as a
physics paper: the research program, theorems and proofs, numerical
experiments, literature search, and text were produced by the large
language model Claude Fable 5 (Anthropic), directed and reviewed by the
author. Nothing here should be taken on trust — every theorem is stated
with a full proof, and every numerical claim is reproducible from the
scripts in this repository.

## Verification

This paper is audited under the program's release gate: repeated
adversarial audit passes by fresh AI agents — cross-model (Claude Opus
and Claude Fable), three independent lanes per pass — each re-deriving
every proof from scratch, re-running every script and tracing every
quoted number to its output, and verifying every reference against
primary records (Crossref, arXiv, publisher pages). Circulation
requires three consecutive passes with zero findings.

- The audit process: [`AUDIT.md`](AUDIT.md)
- This paper's complete pass-by-pass referee trail — every finding,
  every fix, every counter state:
  [`histories/paper1-gate-history.md`](histories/paper1-gate-history.md)

Status of this snapshot: audited through 12 full passes (36 independent
referee lanes); every finding raised has been fixed and re-verified;
the formal three-consecutive-clean gate is in progress.

## Reproducing the results

All results reproduce from the 19 standalone Python scripts in
[`scripts/`](scripts/) (NumPy/SciPy; the paper's Code availability
section maps scripts to sections) and the figure generator
[`paper/make_figures.py`](paper/make_figures.py). Most scripts run in
seconds to minutes; `interacting_pu.py` and `completion_candidates.py`
take tens of minutes.

## Provenance

The originating conversation
([`Conversation_Conformal_Gravity_PT_Barandes.pdf`](Conversation_Conformal_Gravity_PT_Barandes.pdf))
and the project briefing
([`PT_stochastic_handoff.md`](PT_stochastic_handoff.md)) that seeded
this paper are preserved here. The program-wide research notebook,
registries, and full audit ledgers live in the
[program hub](https://github.com/embeddetech/ghosts-program).

## License

MIT — see [`LICENSE`](LICENSE).
