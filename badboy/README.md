# Bad Boy Index — Risk classification framework

A lightweight risk-rating framework for quantifying real-world harm potential of language models, originally proposed by the Vertex Abliteration project (2026) and extended here to cover the *agent-amplified* threat landscape.

> ⚠️ **Research-only.** This folder contains classification taxonomy and risk-rating methodology. No model weights, no method tutorials, no reproducible harmful outputs. The goal is to make safety discussions concrete — not to enable harm.

## Why this matters

Mainstream AI safety discourse focuses on frontier closed models (GPT-4, Claude, Gemini). But the real-world risk surface lives elsewhere:

- Open-weight model + uncensoring tool (this repo) = consumer-laptop-runnable variant
- Add agent tooling (claude-code, opencode, qwen-code, Cline, Aider, etc.) = autonomous capability

The combination is where actual social harm scales. A static chatbot writing a phishing email is one thing; an agent that **writes, sends, monitors responses, extracts credentials, and launders proceeds** is a different category of risk entirely — yet runs on the same hardware.

This framework separates the two evaluation axes:

| File | Scope |
|---|---|
| [chatbot_tiers.md](chatbot_tiers.md) | Static LLM output risk (T1–T8) — what the model **says** |
| [agent_tiers.md](agent_tiers.md) | Agent-amplified risk (AT1–AT6) — what the model + tools **does** |

Both use the same 8-dimensional risk score (severity × accessibility), allowing direct comparison.

## Methodology — 8-dimensional scoring

### Severity dimensions (0–25)

| Code | Dimension | Score 0–5 |
|---|---|---|
| SC | Victim scale | 0=none / 5=global |
| SV | Harm intensity | 0=none / 5=death |
| DU | Duration | 0=minutes / 5=cross-generational |
| FM | Family impact | 0=none / 5=family destruction |
| EN | Environmental damage | 0=none / 5=permanent contamination |
| RV | Reversibility | 0=fully reversible / 5=existential |

**Severity = max(SC, SV) + DU + FM + EN + RV** (0–25)

### Accessibility dimensions (0–10, higher = more likely)

| Code | Dimension | Score 0–5 |
|---|---|---|
| AC | Entry barrier | 0=anyone / 5=state-level |
| DT | Attribution difficulty | 0=certain detection / 5=fully anonymous |

**Accessibility = (5 − AC) + DT** (0–10, higher = more likely to actually happen)

### Real risk

**Real Risk = Severity × Accessibility / 25** (0–10)

Solves the "nukes are scary but no one will get one / agent fraud is mundane but happens every day" mismatch.

## Headline finding: real risk ≠ severity

Nuclear weapons score severity 25 (max) but real risk 1.0 (lowest), because state-level entry + certain attribution kills the threat in practice.

Political warfare (T7a) scores severity 20 but real risk **7.2**, beating all nuclear/biological/chemical categories combined — because AC=1 (just an LLM) and DT=5 (fully anonymous) and **it's already happening at scale**.

When agents are added (this folder's new contribution), nearly every static T-tier gets a corresponding AT-tier with **5 − AC ≈ 5** and **DT ≈ 5**, i.e. the same severity floor but with maximum accessibility — pushing real risk into the 7–9 range for routine threats.

## Credits

- **Bad Boy Index** original taxonomy (T1–T8): Vertex Abliteration project, May 2026.
- **Agent extension (AT1–AT6)**: this folder, June 2026.
- Inspired by:
  - NIST AI Risk Management Framework (2023)
  - Anthropic "Frontier Threats Red-Teaming" (2024)
  - OpenAI Preparedness Framework (2024)

## Citation

```bibtex
@misc{badboy_index_2026,
  title  = {Bad Boy Index: Real-risk taxonomy for uncensored language models and agents},
  author = {Vertex Abliteration project and mlx-heretic contributors},
  year   = {2026},
  url    = {https://github.com/akaiHuang/mlx-heretic/tree/master/badboy},
  note   = {Research framework; no model weights or harmful artifacts published.},
}
```
