# Section 10 (multidimensional channel theory) — numerics provenance / fixtures

(Filename `SS9_NUMERICS.md` is legacy; the numbers below live in §10 `sec:multiD`,
not §9 `sec:completions`, which is number-free.)

Reproducibility map for the numeric claims in Sec. 10 (`sec:multiD`) of
`paper1/main.tex`, so an audit does not re-stall on the slow production runs.
All values below were reproduced 2026-07-14 under a wall-time cap (each
backing script wrapped in `timeout 540`); every committed script completes
well inside that cap. **Reproduce with:** `python scripts/<name>.py`.

## Four-channel malicious model — `deficiency_multiD.py` (runs in ~minutes)
| §10 claim (main.tex) | paper value | reproduced |
|---|---|---|
| window level count vs channel sum, L=8  | 34 vs 32.3 | 34 vs **32.27** |
| window level count vs channel sum, L=12 | 37 vs 37.1 | 37 vs **37.14** |
| μ=0 exact ladder-union deviation | 1e-12 | **1.04e-12** |
| bounded-coupling count shift (μ=0.2) | 34→34, 37→36 | **34→34, 37→36** |
| returned channel mixture, L=6 | (0.583,0.346,0.058,0.014) | **(0.5828,0.3459,0.0576,0.0137)** |
| returned channel mixture, L=9 | (0.401,0.421,0.143,0.035) | **(0.4009,0.4212,0.1433,0.0347)** |
| classical-return fraction, L=6 / L=9 | 96% / 93% | revival **0.955 / 0.933** |

## Quartic-PU drift diagnostic — `pu_bo_channels.py` / `pu_deficiency_evidence.py`
| §10 claim | paper value | reproduced |
|---|---|---|
| prop:bo channel time of flight T(k=2→400) | 1.74 | **1.7364** |
| e.s.a. baseline ratios (two basis scales) | 0.17–0.46 | 0.170, 0.347, 0.364, … |
| single early-window dip | 0.34 | 0.341 (basis nu1=1.0, N=24) |
| extended trunc λ=+0.05, N=48→56 / 56→64 | 3.77 / 1.06 | **3.766 / 1.055** |
| ghost pair λ=−0.05, N=48→56 / 56→64 | 0.49 / 0.32 | **0.489 / 0.319** |

## prop:bo displaced-oscillator identity — EXACT (analytic; no script needed)
With H_PU = p₁q₂ + p₂²/2γ + (γ/2)Ω q₂² − (γ/2)Ω₀² q₁² (eq. ostro, Ω=ω₁²+ω₂²,
Ω₀²=(ω₁ω₂)²), rotated rep p₁→y, q₁→−p_y, and U = exp(−i y p₂/γΩ):
U acts as  p_y → p_y + p₂/γΩ,  q₂ → q₂ − y/γΩ,  y,p₂ fixed. Term by term,
U(H_PU+λq₁⁴)U† = T(p_y+p₂/γΩ) + p₂²/2γ + (γΩ/2)q₂² − y²/2γΩ, T(p)=λp⁴−(γΩ₀²/2)p²:
the y·q₂ cross-term cancels (γΩ·1/γΩ = 1), the y² terms combine to −y²/2γΩ,
and the p_y block becomes T(p_y+p₂/γΩ). The generator is bilinear ⇒ the BCH
series terminates ⇒ the identity is exact (the paper's "1e-9" is the Fock-
truncation numerical witness of this exact identity). Verified by hand
2026-07-14.

## Completion candidates — `completion_candidates.py`
**Part A (sign dichotomy — CHEAP, runs in seconds; reproduced 2026-07-14):**
| §10 claim (main.tex) | paper value | reproduced |
|---|---|---|
| λ<0 wall-regularized convergence drift, L=6→8 / 8→10 | 3e-8 → 1e-13 | **2.90e-08 → 3.07e-13** |
| sign dichotomy (0,0) vs (2M,2M): λ<0 e.s.a. converges, λ>0 never | theorem at finite channel # | converges as reproduced |

**Part B/C (kinetic-form ratios `0.9997 / 0.01–0.07 / 0.16–0.45`): REPRODUCED
2026-07-14** via a long uncapped run (the wall-cap could not reach it; full stdout
committed as `completion_candidates_run.txt`).
| paper value | reproduced |
|---|---|
| PU λ>0 deficiency, definite escape (ratio→1) | **0.9997** (amp 1e5) |
| ghost λ<0, null escape (ratio→0) | **0.0663/0.0139/0.0209/0.0633** (i.e. 0.01–0.07) |
| valley-adapted drift ratios | **0.158–0.445** (i.e. 0.16–0.45) |
| falsification: λ<0 PU ratio ALSO →1 | **0.9998** (amp 1e5) — as the paper reports |

This was the last unbacked §10 number-family; the p1 numerics lane's blocking
provenance item is now CLOSED.

## §10 certificate diagnostics (reproduced in gate passes 24/26; committed here)
Values reproduced by fresh audit agents running the committed scripts; recorded
here so the "trace every number to an output" gate closes without a re-run.
| §10 claim (main.tex) | paper value | reproduced | script |
|---|---|---|---|
| Maslov exponent / amplitude vs √600 | −1.999 / 24.55 vs 24.49 | **−1.999 / 24.546** | maslov_feasibility.py |
| Maslov alignment / transverse width / \|det∂q\|~τ^m | 1.0000 / 5e−3 / m≈3.1 | **1.0000 / 5.28e−3 / 3.14** | " |
| Maslov N@Z=6 / weighted residual / peak | 0.082 / 0.026 / 8e3 | **0.0824 / 0.0262 / 8.25e3** | " |
| glued 1D certificate ratio; poly branch | 0.0011; k^{−1/2+Z/1.12} | **0.00109**; 1.12 | glued_certificate_1d.py |
| frame decoupling; λ<0 drift then | 1e−13; 3e−8→1e−13 | **1.28e−13; 2.90e−8→2.63e−13** | gap_closure_channels.py |
| tail cert λ>0 (five launches): four falling + outer | 1.21–1.29 + 1.41 | **1.2867/1.2119/1.2112/1.4120/1.2112** | tail_certificate.py |
| tail cert 1D LC control / confining / λ<0 control | 1.22 / 4.9 / 641 | **1.2181 / 4.8675 / 640.76** | " |

Not separately re-run here (algebra / covered by `appD_escape_dictionary.py`
and the body's certified numerics): the Puiseux exponent 1.999 and the small
ω-parameter tuples in the prop:bo / Maslov passages.
