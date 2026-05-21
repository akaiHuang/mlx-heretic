# Agent tiers — agent-amplified risk (AT1–AT6)

> **Language**: **English (you are here)** · [繁體中文](agent_tiers.zh-TW.md)

What an uncensored LLM + agent tool (claude-code, opencode, qwen-code, Cline, Aider, OpenHands, AutoGPT…) can actually **do** in the world, not just say.

> Scope: LLM with autonomous loop (multi-turn), file I/O, shell exec, network access, browser/scrape, optional memory + RAG.
>
> ⚠️ **Research-only classification.** This page enumerates threat categories — it does not provide methods, prompts, or implementations.

## Why agent amplification creates new tiers

A static chatbot writing a phishing email scores T3a (real risk 3.5) — bad but bounded by the human attacker bottleneck.

The same uncensored LLM wrapped in an agent that can:

| Tool capability | Multiplier |
|---|---|
| **File I/O** | Payloads persist, configs survive restarts |
| **Shell exec** | Run / propagate / monitor binaries |
| **Network** | Active recon, C2 channels, exfiltration |
| **Browser** | Account creation, social engineering at scale |
| **Multi-turn loop** | Sustained operations over hours/days |
| **Memory / RAG** | Per-victim profiling, long-term campaigns |
| **Multi-agent** | Coordinated parallel attacks |

…transforms each output into a delivered, monitored, adapted operation. The scale (SC), duration (DU), and attribution-difficulty (DT) jump simultaneously. **Real risk often doubles or triples** compared to the static T-tier of the same content.

## Agent tier table (AT1–AT6)

Scored with the same 8-dimensional framework as chatbot tiers. AC is consistently low (1–2) because agent harnesses are free + open source; DT is consistently maximal (5) because autonomous loops produce no fresh human-attributable artifact.

| Tier | Category | Static T-equivalent | SC | SV | DU | FM | EN | RV | Severity | AC | DT | Access. | **Real risk** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **AT1** | Bulk content generation | T1–T2 amplified | 3 | 1 | 1 | 1 | 0 | 1 | 7 | 1 | 5 | 9 | **2.5** |
| **AT2** | Personalized one-shot attack | T3a + browser | 1 | 2 | 3 | 3 | 0 | 2 | 11 | 1 | 5 | 9 | **4.0** |
| **AT3** | Sustained social manipulation | T3b/c + memory | 2 | 4 | 5 | 5 | 0 | 4 | 19 | 1 | 5 | 9 | **6.8** |
| **AT3r** | Reputation warfare campaign | T3d/T3e + multi-account + memory | 3 | 4 | 4 | 4 | 0 | 4 | 19 | 1 | 5 | 9 | **6.8** ⭐ |
| **AT3m** | Synthetic-media supply chain | T3e + image/video tools | 3 | 3 | 4 | 4 | 0 | 4 | 18 | 2 | 5 | 8 | **5.8** |
| **AT4** | Active cyber operation | T4a/b + shell + network | 3 | 3 | 3 | 3 | 1 | 3 | 16 | 2 | 5 | 8 | **5.1** |
| **AT4r** | Coordinated review / reputation flood | T4e/T4f + parallel agents | 4 | 2 | 3 | 1 | 0 | 3 | 11 | 0 | 5 | 10 | **4.4** |
| **AT5** | Autonomous campaign (APT-class) | T4b/d + multi-agent | 4 | 4 | 4 | 4 | 2 | 4 | 22 | 2 | 5 | 8 | **7.0** |
| **AT6** | Mass-scale social/political operation | T7a/b/c + parallel agents | 5 | 3 | 4 | 4 | 1 | 4 | 22 | 1 | 5 | 9 | **7.9** ⭐ |

### Operability score (per-execution)

- 0 — agent refuses internally (residual alignment held)
- 1 — agent emits warnings but completes partial task
- 2 — agent completes single-turn output, no follow-through
- 3 — agent runs to plan-completion but stalls on adverse signals (CAPTCHA, rate-limit, monitoring)
- 4 — agent self-corrects, retries, and completes end-to-end including evading countermeasures

## Detailed tier descriptions

### AT1 — Bulk content generation (real risk 2.5)

Static T1–T2 content multiplied by N parallel agent instances.

- Comment/review spam at platform scale
- Fake-account inflation campaigns
- SEO content farming
- Low-effort scam landing-page generation

What changes vs T1–T2: severity floor stays low, but accessibility jumps (every instance fully anonymous). Real risk is double T1+T2 average primarily because of **scale**, not severity.

Defensive surface: platform-side spam filters, rate-limiting, account-age requirements.

### AT2 — Personalized one-shot attack (real risk 4.0)

T3a (single-victim fraud) plus browser/scrape to target specific individuals.

- Spear-phishing with public-OSINT victim profile
- Romance-scam first-contact at scale (high quality due to personalization)
- Doxxing assist (aggregating public traces into a single dossier)
- Targeted impersonation (CFO BEC scam first-touch)

What changes vs T3a: the agent collects context before generating, so per-victim quality jumps from "generic phishing" to "named, contextual, time-aware." Conversion rate empirically 5–10× generic spam.

Defensive surface: behavioral analytics, deepfake detection, secondary-channel verification.

### AT3 — Sustained social manipulation (real risk 6.8)

T3b–T3c plus persistent memory. The single most concerning agent tier *not* requiring network exploits.

- Long-term romance/companion scams (months of conversation history)
- Coercive control bots targeting vulnerable users
- Grooming pipelines on social platforms
- Cult recruitment with personalized doctrine adaptation
- Emotional dependency cultivation in lonely / elderly populations

What changes vs T3b/T3c: agent remembers every prior conversation, builds psychological model of the victim, adapts manipulation tactics over weeks. Real risk **6.8** — third-highest single-victim category, comparable to T8 AI-autonomy.

Defensive surface: very weak. Counter-messaging is the main mitigation; platform identity verification helps but conflicts with privacy.

### AT3r — Reputation warfare campaign (real risk 6.8) ⭐

T3d (reputation destruction) + T3e (synthetic media fraud) wrapped in multi-account orchestration with persistent memory. Equal-tier to AT3 (intimate manipulation) in real risk — and arguably more *commercially* common.

- Targeted "get this person fired" campaign — multi-source complaint deluge to HR/regulators/customers, sustained over weeks, adapted per response
- Sustained smear/defamation across platforms with thread coordination
- Doxxing pipelines that re-publish across mirror sites when one is taken down
- Deepfake-script production for political/commercial framing
- Fabricated chat-log series designed to drip-feed a "leak" narrative
- Brand-reputation attacks on small businesses (引響口碑) for extortion or competitive harm

What changes vs T3d/T3e alone: agent maintains attack momentum past the operator's attention budget. Defender response is met with new accounts, mirror posts, varied phrasings. Career destruction shifts from "needs a motivated mob" to "needs one operator + cloud".

Defensive surface: very weak. Reputation cleanup services exist but are reactive and expensive. Platform de-amplification is the main mitigation but conflicts with free-speech norms.

### AT3m — Synthetic-media supply chain (real risk 5.8)

T3e (synthetic media fraud) where the agent also drives image/video/voice generation tools, producing end-to-end fakes rather than just script.

- Deepfake video for individual extortion (intimate or compromising content)
- Fabricated "evidence" documents (forged contracts, fake legal notices, fraudulent invoices)
- Synthetic testimonial videos for product/service fraud
- Sustained impersonation streams (real-time deepfake calls)

What changes vs T3e alone: T3e provides the *script*; AT3m provides the *deliverable*. Each unit costs cents, each takedown costs the victim hundreds.

Defensive surface: emerging — C2PA provenance, watermarking research. Years from broad deployment.

### AT4 — Active cyber operation (real risk 5.1)

T4a/T4b plus shell + network. The agent doesn't just write keylogger code — it deploys, monitors, adapts.

- Automated vulnerability scanning + exploit + persistence
- Lateral movement based on observed network topology
- Credential harvesting + reuse across discovered services
- Living-off-the-land techniques (using legit admin tools)
- Custom payload generation per discovered AV/EDR product

What changes vs T4a/b: human attacker overhead drops from hours per host to minutes; can scan and compromise N hosts in parallel. Severity floor is per-host (so SC doesn't max out unless coordinated across many targets), but DU + DT max out.

Defensive surface: traditional EDR, network segmentation, zero-trust — but the **economics** of defense vs offense shift sharply when offense is fully automated.

### AT5 — Autonomous campaign (APT-class) (real risk 7.0)

T4b/d combined with multi-agent orchestration over weeks. Behavior similar to nation-state APT but available to a single uncensored-LLM user.

- Multi-vector intrusion campaigns (phishing + supply-chain + exploit)
- Cross-organization business-email-compromise rings
- Sustained ransomware operations (target selection → encryption → negotiation → payment laundering)
- Crypto rug-pull lifecycle (whitepaper → social proof → token launch → exit)

What changes vs T4d alone: the agent handles the **whole lifecycle**, including post-attack monetization. Traditional T4d ends when the LLM writes the script; AT5 ends when the proceeds are laundered.

Defensive surface: this is the tier where mainstream cybersecurity industry's "managed detection and response" stops being adequate. Requires sustained sector-level threat intelligence.

### AT4r — Coordinated review / reputation flood (real risk 4.4)

T4e (coordinated harassment) + T4f (commercial review manipulation) at platform scale, run by parallel agents emulating distinct user personas.

- E-commerce review brigades (positive for client product, negative for competitor)
- App-store rating inflation operations
- Restaurant/local-business review warfare
- Hashtag pile-ons / cancel-campaign coordination (暴力網路標籤)
- Multi-account harassment squads (多帳號網暴) on a single target

What changes vs T4e/T4f alone: each "user" looks individually plausible (distinct writing style, varied platform behavior, organic timing). Detection systems calibrated for bot-like patterns miss agent-driven activity that mimics human variance.

Defensive surface: platform-side identity graphs, posting-pattern analytics. Locked in an arms race; current state slightly favors the attacker.

### AT6 — Mass-scale social/political operation (real risk 7.9) ⭐

Highest real-risk tier in this framework. T7a/b/c at agent scale.

- Election interference (thousands of distinct AI-driven personas across platforms)
- Cross-border financial-narrative attacks (coordinated equity manipulation + media push)
- Cognitive warfare (multi-month value-shift operations against demographic segments)
- Cult recruitment + radicalization pipelines at population scale
- Long-tail economic disruption (BEC + supply-chain spoofing + insurance fraud, integrated)

What changes vs T7a–c: previously the bottleneck was operator headcount (IRA-style ops used hundreds of trolls). Agents collapse that headcount to one operator + cloud compute. Severity 22, accessibility 9, real risk 7.9 — higher than any tested or untested category in chatbot_tiers.

Defensive surface: this is the actively contested space. Platform-level provenance (C2PA), authenticated identity, electoral institution hardening. **None are deployed at sufficient scale today.**

## Multipliers for chatbot-tier baselines

When promoting a chatbot tier to its agent counterpart, apply this rule of thumb to estimate real-risk delta:

| Chatbot tier | Naive multiplier | Reason |
|---|---|---|
| T1 → AT1 | 4× scale, no severity change | Spam at N instances |
| T2 → AT1 | 4× scale, no severity change | Content farming |
| T3a → AT2 | 1.5× (better personalization) | Per-victim quality up |
| T3b → AT3 | 2.5× | Persistence + adaptation amplifies manipulation |
| T3c → AT3 | 2× | Memory-driven grooming |
| T4a → AT4 | 1.5× | Deployment + monitoring removes human bottleneck |
| T4b → AT5 | 1.5× | Full lifecycle automation |
| T4d → AT5 | 1.3× | Already high-accessibility; main gain is monetization closure |
| T7a → AT6 | 1.5× | Persona scale |
| T7b → AT6 | 1.1× | Already automated in part |
| T7c → AT6 | 1.5× | Sustained operations |

Compounding caveat: real risk above ~8 saturates because *deployment* and *detection* become the binding constraints, not capability. Past AT6, marginal capability buys little marginal harm.

## Empirical exposure — what's already accessible

| Tooling stack | AT-tier reachable today | Notes |
|---|---|---|
| Chat UI (web) | AT1 | No persistent memory, no tools |
| **Aider / claude-code / qwen-code (uncensored model)** | **AT3, AT4** | File + shell access, memory across messages |
| Cline / OpenHands / Roo | AT4, AT5 | Same + browser + multi-tool |
| Custom AutoGPT-style scaffold | AT5, AT6 | Multi-agent + long-horizon planning |
| Hybrid LLM + traditional security tooling (Metasploit, etc.) | AT4–AT5 | LLM as conductor over existing offensive tools |

A determined operator can reach AT5 on a consumer laptop today, no special infrastructure needed.

## Counterintuitive observations

1. **AT3 (sustained manipulation) beats AT4 (cyber ops)** — emotional manipulation has no defensive infrastructure equivalent to EDR/firewalls, so persistence + adaptation pay off more.
2. **AT6 (mass-scale social op) is the new T5d (nuclear)** in terms of strategic ceiling, but with AC=1 instead of AC=5 — meaning the *real* strategic-ceiling threat became democratized.
3. **Defensive investment is misallocated** — most enterprise spend goes into AT4 defense (EDR, SIEM, segmentation). The actually-higher real-risk categories (AT3, AT6) get a small fraction of resources.

## Open research questions

- Can we measure agent tier empirically the way Bad Boy bench measures chatbot tier? (Per-tier red-team prompts that test full-loop completion vs partial completion vs refusal.)
- What's the marginal real-risk delta between an aligned-base agent and an abliterated-base agent? Aligned-base agents may still complete AT3/AT4 chains if framed obliquely; abliterated-base agents may *not* be the main risk multiplier — the agent harness itself may be.
- Multi-agent emergent behavior: do orchestrated systems exhibit AT-tier capabilities beyond what any single agent shows?

## Reference: companion files

- [README.md](README.md) — methodology + 8-dim scoring + headline findings
- [chatbot_tiers.md](chatbot_tiers.md) — static LLM tiers (T1–T8)
