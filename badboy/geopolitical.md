# Geopolitical landscape — abliteration / agent-amplified harm discourse

> **Language**: **English (you are here)** · [繁體中文](geopolitical.zh-TW.md)
>
> Open-source-intelligence (OSINT) summary of how different state actors and regions engage with LLM uncensoring and agent-amplified harm capabilities. **Research compilation only — does not endorse any state actor or attack technique.**

## Why this matters

The Bad Boy Index ([chatbot_tiers.md](chatbot_tiers.md) + [agent_tiers.md](agent_tiers.md)) classifies *what* an uncensored LLM-plus-agent system can do. This page asks *who* is actually using or studying it. Knowing the geographic distribution of capability and intent helps:

- Defensive teams calibrate threat models per region
- Policy researchers identify regulatory gaps
- Open-source community understand whose tools are most likely to be repurposed by whom

## 🇨🇳 China — leading technical depth, low public discourse

### Public LLM capability: ⭐⭐⭐⭐⭐

| Provider | Notable models | Public position on uncensoring |
|---|---|---|
| DeepSeek | V3 / R1 / Coder | RLHF deep, abliteration well-documented in community |
| Alibaba (Qwen) | Qwen 3.5 / 3.6 series | Strong PRC RLHF; Heretic effective (-75pp refusal) |
| Zhipu (GLM) | GLM-4 / 4.5 | Standard alignment |
| 01.AI (Yi) | Yi-Lightning / Yi-Large | Standard alignment |
| Baichuan | Baichuan-2/3 series | Standard alignment |
| MoonShot (Kimi) | Kimi K2 | Long-context focused |

### Academic line — "anti-abliteration" framing

Tsinghua / Peking / Renmin / Fudan publish robustness papers focusing on **defending against** jailbreak / abliteration, not on offensive use:

- "Robust Alignment under Adversarial Prompt" (THU, 2024)
- "Safety Steering Vectors in Chinese LLMs" (PKU, 2025)
- PLA Academy of Military Sciences: "Intelligent Network Defense" series (2024-)

### State actor activity (Western threat-intel attribution)

| Actor | Recent attribution | Source |
|---|---|---|
| Volt Typhoon | LLM-assisted infrastructure recon (US targets) | Microsoft Threat Intelligence, 2024 |
| Salt Typhoon | Telecom-network intrusion campaigns | Wall St Journal / Reuters, 2024 |
| Flax Typhoon | Botnet operations | Microsoft, 2024 |
| Spamouflage Dragon | Cross-platform influence operations | DFRLab, Microsoft, 2024-2025 |
| Plaid Rain | Targeted phishing of policy researchers | Mandiant, 2024 |

### Public position

PRC's Cyberspace Administration of China (CAC) issued *Generative AI Services Management Measures* (2023) requiring registration and content moderation. **Does not publicly acknowledge offensive uncensoring research.** CSET (Georgetown) reports PLA "doctrine for LLM offensive applications still emerging." State-actor use of abliterated models is *inferred* by Western analysts, not publicly admitted.

### Bad Boy Index relevance

| Tier | Chinese activity |
|---|---|
| T7a (political warfare) | Spamouflage Dragon active across X / TikTok / YouTube |
| T7c (cognitive warfare) | Long-term narrative-shaping ops documented |
| T4a-h (cyber) | APT groups using LLM assistance, abliterated unclear |
| AT6 (mass-scale ops) | Most mature operator globally for this tier |

## 🇷🇺 Russia — domestic LLMs + heavy influence-op use

### Public capability

- Sber AI: **GigaChat** (~13B, multilingual incl. Russian)
- Yandex: **YaGPT** family
- Both have RLHF but PRC-style political alignment is weaker (Russian context)

### State actor activity

| Actor | Attribution |
|---|---|
| Doppelganger / RRN | 1000+ fake-news sites, AI-generated content at multilingual scale, mapped by EUDisinfoLab |
| APT28 (Fancy Bear / GRU) | LLM-assisted social engineering, documented in Mandiant reports |
| Storm-1679 | Election-targeted influence ops (US, EU) |

### Open community

Russian-speaking abliteration community is active. Hugging Face Hub hosts Russian-language abliterated variants. Discussions in Telegram data-science channels are common. Framing tends to be "freedom of political expression" rather than offensive operations.

### Bad Boy Index relevance

| Tier | Russian activity |
|---|---|
| T7a (political warfare) | Continuous IRA-style ops, 1000s of accounts |
| T7c (cognitive warfare) | Cross-EU sustained narrative campaigns |
| AT6 (mass-scale social op) | Doppelganger network is textbook AT6 |

## 🇮🇷 Iran — limited self-capability, heavy operational use of frontier models via fronts

Iran has limited domestic LLM capability publicly known. State cyber units rely on **frontier models accessed via proxies / fake identities**:

| Actor | Attribution |
|---|---|
| APT39 / Charming Kitten / Imperial Kitten | LLM-assisted spear-phishing |
| Storm-2035 | US election interference via AI-generated content (Microsoft Threat Intel, 2024) |
| MuddyWater | Sustained cyber ops with LLM-aided tooling |

OpenAI banned multiple Iran-linked accounts in 2024 reports. Iranian operators **don't need** their own abliterated models — they use whatever's online and rotate identities.

## 🇰🇵 North Korea — small domestic capability, heavy frontier-model misuse

DPRK has minimal domestic LLM capability (sanctions, GPU access). State cyber units (Lazarus, Kimsuky, Andariel) heavily use Western LLMs via fronts:

| Operation | Estimated harm | Source |
|---|---|---|
| Fake IT-worker fraud | ~$600M/yr | US Treasury, 2024 |
| Kraken / similar exchange heists | $1.5B+ aggregated | Chainalysis, 2024 |
| xz-utils supply-chain attack (suspected) | Critical infrastructure | Mandiant, 2024 |

Mandiant reports (2024) confirm DPRK contractors using **abliterated Llama-3 variants** for fake-IT-worker resume / interview prep — direct ROI on uncensoring tools.

**Interest in self-hosted abliterated models**: motivated by evading OpenAI / Anthropic detection that has repeatedly cut off their frontier-model access.

## 🇮🇱 Israel — strong dual capability, limited public discussion

### Public

Civilian AI ecosystem is mature (Mobileye, Wiz, AI21 Labs, etc.). Academic groups at Bar-Ilan, Tel Aviv University, Technion publish robustness / adversarial ML at top venues.

### Unit 8200 (signals intelligence)

Operational LLM use is not publicly documented but is widely inferred. Strong academic line in:

- Membership inference attacks
- Model extraction
- Adversarial robustness

These map to offensive capabilities against *other* state actors' deployed LLMs.

### Bad Boy Index relevance

Israel's interest skews toward **defensive AI** publicly, with implied offensive capability privately. Likely capable of AT4 / AT5 against nation-state targets; no public attribution exists.

## 🇦🇪 UAE — most aggressive Middle East AI ecosystem

| Org | Notable models |
|---|---|
| TII (Technology Innovation Institute) | Falcon-180B, Falcon3 |
| MBZUAI | Academic line, strong collaboration with Stanford / CMU |
| G42 | Jais-30B (Arabic-native), Microsoft strategic partnership |

G42's 2024 Microsoft partnership was conditioned on CFIUS clearance regarding China relationships. Public discourse focuses on Arabic-language capability and commercial deployment; **no public abliteration discussion**.

## 🇸🇦 Saudi Arabia — procurement-led

NEOM AI strategy is procurement-heavy (Anthropic, OpenAI partnerships, large compute orders). Limited domestic frontier-model production. No notable public engagement with uncensoring research.

## Arabic-language LLM uncensoring community

| Direction | Examples |
|---|---|
| Open-community Arabic-uncensored variants | Various HF Hub uploads (anonymous / community) |
| Motivation | "Freedom of political expression" framing, similar to Russian community |
| State engagement | None openly |
| Use cases | Mostly community discussion of regionally-suppressed topics |

## 🇺🇸 United States — full-spectrum, most public research

### Government / policy

| Org | Output |
|---|---|
| CSET (Georgetown) | Frequent reports on China + AI weapons |
| RAND Corporation | AI biosecurity, AI warfare scenarios |
| CNAS | Defense AI policy |
| NIST | AI Risk Management Framework (2023) |
| OSTP | Executive Order on AI (2023) |

### Industry threat intelligence

| Org | Output |
|---|---|
| Microsoft Threat Intelligence | Quarterly reports naming state actors (Volt Typhoon, Storm-2035, Emerald Sleet, etc.) |
| OpenAI Threat Intelligence | Quarterly bans + attribution (Russia, China, Iran, DPRK) |
| Google TAG (Threat Analysis Group) | APT campaign tracking |
| Anthropic | Less frequent but in-depth threat reports |
| Mandiant (Google Cloud) | APT attribution + technical detail |
| Recorded Future | Commercial threat intel |
| Cisco Talos | Network-side intel |

### Academic safety

Stanford HAI / Internet Observatory, Berkeley CHAI, MIT CSAIL, CMU, Princeton — all maintain active programs.

## 🇪🇺 Europe — strong policy + threat-monitoring framework

| Org | Output |
|---|---|
| EUDisinfoLab | Russia / China influence tracking |
| DFRLab (Atlantic Council, US-EU joint) | OSINT-driven attribution |
| ENISA (EU cyber security agency) | Periodic threat landscape reports |
| EU AI Act enforcement | Began phased application 2025-2026 |

## Summary capability matrix

| Region | Self-LLM | Abliteration awareness | Operational use of uncensored | Public engagement |
|---|---|---|---|---|
| 🇨🇳 China | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ (inferred) | ❌ |
| 🇷🇺 Russia | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ (influence ops) | ⚠️ partial |
| 🇮🇷 Iran | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ (via frontier proxies) | ❌ |
| 🇰🇵 North Korea | ⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ (Lazarus IT-worker fraud) | ❌ |
| 🇮🇱 Israel | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ? (inferred via 8200) | ⚠️ academic only |
| 🇦🇪 UAE | ⭐⭐⭐ | ⭐⭐⭐⭐ | ? | ⚠️ commercial framing |
| 🇸🇦 Saudi Arabia | ⭐⭐ | ⭐⭐ | ? | ❌ |
| 🇺🇸 USA | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | bidirectional (offense + defense, mostly defense public) | ✅⭐ |
| 🇪🇺 EU | ⭐⭐⭐ | ⭐⭐⭐⭐ | mostly defensive | ✅ |

## Observations relevant to Bad Boy Index development

1. **Public discourse vs operational reality diverges sharply**. Public discussion of abliteration is concentrated in US / EU academic + commercial spheres. Operational use (Russia, DPRK, Iran, inferred China) is documented through threat-intel reports, not policy papers.

2. **The information-asymmetry problem**. State actors with offensive intent know about abliteration; defenders building protective systems often calibrate against outdated threat models because the public literature lags real-world capability by 12-18 months.

3. **East Asia + Middle East context underrepresented in Western benchmarks**. HarmBench, JailbreakBench, AdvBench are English-centric. Bad Boy Index's bilingual + East-Asia-context coverage (T7d random street violence, T3v vehicle sabotage of specific person) fills a gap that mainstream benchmarks miss.

4. **Defense investment is misallocated geographically**. Most defensive research targets adversaries from "elsewhere" (US researchers focus on China, China focuses on US). Within-region threats (domestic actors using LLMs against own population) get less attention.

5. **Open-source community as proxy for state capability**. When Hugging Face Hub has 1000+ abliterated variants and Discord has active communities sharing techniques, state actors don't need internal R&D — they monitor open community and adopt techniques. This is the strongest reason to publish Bad Boy Index transparently: defenders need to see what's already accessible.

## Sources / further reading (representative, not exhaustive)

- Microsoft Threat Intelligence quarterly reports — https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/
- OpenAI Threat Intelligence reports — https://openai.com/global-affairs/disrupting-deceptive-uses-of-AI/
- DFRLab — https://dfrlab.org/
- Mandiant Advantage (Google Cloud) — APT attribution
- CSET (Georgetown) China + AI policy briefs — https://cset.georgetown.edu/
- RAND AI biosecurity / AI warfare reports — https://www.rand.org/
- EUDisinfoLab — https://www.disinfo.eu/
- Stanford Internet Observatory — published research on influence ops
- US Treasury OFAC notices on DPRK / Iran AI-related sanctions

## Caveat

This page summarizes **publicly attributable** activity. Classified state capabilities are by definition not in scope; what is documented is the iceberg's tip. Numbers and characterizations come from open-source intelligence and may lag by 6-18 months. Bilateral attribution (e.g. "Volt Typhoon = PRC state") follows the consensus of US / Five Eyes intelligence statements — these can be politically contested.
