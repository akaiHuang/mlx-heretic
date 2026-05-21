# 地緣政治版圖 — abliteration / agent-amplified harm 真實 discourse

> **語言**：[English](geopolitical.md) · **繁體中文 (你在這)**
>
> 公開來源情報 (OSINT) 整理: 不同國家 / 區域對 LLM 解禁跟 agent 增強傷害能力的態度跟使用記錄。**僅供研究整理 — 不代表任何 state actor 或攻擊技術的背書。**

## 為何重要

Bad Boy Index ([chatbot_tiers.zh-TW.md](chatbot_tiers.zh-TW.md) + [agent_tiers.zh-TW.md](agent_tiers.zh-TW.md)) 分類「解禁 LLM + agent 系統**能做什麼**」。這頁問**誰在真實做或研究**。知道能力跟意圖的地理分佈, 有助於:

- 防禦團隊依區域校準威脅模型
- 政策研究者識別監管缺口
- 開源社群理解誰的工具最可能被誰再利用

## 🇨🇳 中國 — 技術深度領先, 公開 discourse 低

### 公開 LLM 能力: ⭐⭐⭐⭐⭐

| 提供方 | 代表 model | 對解禁的公開立場 |
|---|---|---|
| DeepSeek | V3 / R1 / Coder | RLHF 深, abliteration 在 community 紀錄完整 |
| Alibaba (Qwen) | Qwen 3.5 / 3.6 系列 | PRC RLHF 強; Heretic 有效 (-75pp refusal) |
| Zhipu (GLM) | GLM-4 / 4.5 | 標準對齊 |
| 01.AI (Yi) | Yi-Lightning / Yi-Large | 標準對齊 |
| Baichuan | 百川 2/3 系列 | 標準對齊 |
| MoonShot (Kimi) | Kimi K2 | 長 context 為主 |

### 學術線 — 「反 abliteration」框架

清華 / 北大 / 人大 / 復旦 發 robustness 論文, 焦點在**防**解禁 / jailbreak, 不在攻擊:

- "Robust Alignment under Adversarial Prompt" (清華, 2024)
- "Safety Steering Vectors in Chinese LLMs" (北大, 2025)
- 軍事科學院: 「Intelligent Network Defense」系列 (2024-)

### State actor 活動 (西方威脅情報歸屬)

| Actor | 近期歸屬 | 來源 |
|---|---|---|
| Volt Typhoon | LLM 輔助基礎設施 recon (US 目標) | Microsoft Threat Intelligence, 2024 |
| Salt Typhoon | 電信網路入侵戰役 | WSJ / Reuters, 2024 |
| Flax Typhoon | Botnet 操作 | Microsoft, 2024 |
| Spamouflage Dragon | 跨平台影響戰 | DFRLab, Microsoft, 2024-2025 |
| Plaid Rain | 鎖定政策研究員的 phishing | Mandiant, 2024 |

### 公開立場

PRC 國家網信辦發《生成式 AI 服務管理辦法》(2023), 要求註冊跟內容審查。**不公開承認攻擊性解禁研究。** CSET (Georgetown) 報告: PLA「LLM 攻擊應用 doctrine 仍在 emerging」。State actor 用 abliterated model 是西方分析師**推斷**, 不公開承認。

### Bad Boy Index 對應

| Tier | 中國活動 |
|---|---|
| T7a (政治戰) | Spamouflage Dragon 在 X / TikTok / YouTube 活躍 |
| T7c (認知戰) | 長期敘事塑造操作有記錄 |
| T4a-h (cyber) | APT 群已用 LLM 輔助, 是否 abliterated 不確定 |
| AT6 (規模化操作) | 全球此 tier 最成熟的操作者 |

## 🇷🇺 俄羅斯 — 自家 LLM + 大量影響戰使用

### 公開能力

- Sber AI: **GigaChat** (~13B, 多語含俄文)
- Yandex: **YaGPT** 家族
- 都有 RLHF, 但對 PRC 式政治審查弱 (俄文 context)

### State actor 活動

| Actor | 歸屬 |
|---|---|
| Doppelganger / RRN | 1000+ 假新聞網站, AI 生成多語規模化, EUDisinfoLab 製圖 |
| APT28 (Fancy Bear / GRU) | LLM 輔助社交工程, Mandiant 報告記錄 |
| Storm-1679 | 選舉鎖定影響戰 (US, EU) |

### 開源社群

俄語 abliteration 社群活躍。Hugging Face Hub 有俄語解禁變體。Telegram DS 頻道常討論。框架傾向「政治表達自由」, 不是攻擊性操作。

### Bad Boy Index 對應

| Tier | 俄國活動 |
|---|---|
| T7a (政治戰) | 持續 IRA 式操作, 數千帳號 |
| T7c (認知戰) | 跨歐盟持續敘事戰役 |
| AT6 (規模化社會操作) | Doppelganger 網路是教科書級 AT6 |

## 🇮🇷 伊朗 — 自家能力有限, 大量透過代理用前沿 model

伊朗公開 LLM 能力有限。state cyber units 依賴**透過代理 / 假身份**存取前沿 model:

| Actor | 歸屬 |
|---|---|
| APT39 / Charming Kitten / Imperial Kitten | LLM 輔助 spear-phishing |
| Storm-2035 | 美選干預 AI 生成內容 (Microsoft Threat Intel, 2024) |
| MuddyWater | 持續 cyber ops 含 LLM 輔助工具 |

OpenAI 2024 報告 ban 多個伊朗連結帳號。伊朗操作員**不需要**自家 abliterated model — 用線上有的, 輪換身份。

## 🇰🇵 北韓 — 自家能力小, 大量誤用前沿 model

DPRK 自家 LLM 能力極小 (制裁、GPU 取得困難)。State cyber units (Lazarus, Kimsuky, Andariel) 大量用西方 LLM 透過代理:

| 操作 | 估計傷害 | 來源 |
|---|---|---|
| 假 IT-worker 詐騙 | ~$600M/年 | US Treasury, 2024 |
| Kraken / 類似交易所 hack | $1.5B+ 累計 | Chainalysis, 2024 |
| xz-utils 供應鏈攻擊 (疑似) | 關鍵基礎設施 | Mandiant, 2024 |

Mandiant 報告 (2024) 確認 DPRK 承包商**用 abliterated Llama-3 變體**做假 IT-worker 履歷 / 面試準備 — 對解禁工具有直接 ROI。

**對自託管 abliterated model 的興趣**: 規避 OpenAI / Anthropic 偵測 (他們多次切斷其前沿 model 存取)。

## 🇮🇱 以色列 — 雙線能力強, 公開討論有限

### 公開

民用 AI 生態成熟 (Mobileye, Wiz, AI21 Labs 等)。Bar-Ilan / TAU / Technion 學術組在頂會發 robustness / adversarial ML。

### Unit 8200 (sigint)

操作性 LLM 使用沒公開記錄但廣泛被推斷。強學術線:

- Membership inference 攻擊
- Model extraction
- Adversarial robustness

這些對應**對其他 state actor 已部署 LLM 的攻擊能力**。

### Bad Boy Index 對應

以色列興趣公開偏**防禦 AI**, 含蓄帶私下攻擊能力。對 nation-state 目標可能能 reach AT4 / AT5; 沒公開歸屬。

## 🇦🇪 UAE — 中東最 aggressive 的 AI 生態

| 組織 | 代表 model |
|---|---|
| TII (Technology Innovation Institute) | Falcon-180B, Falcon3 |
| MBZUAI | 學術線, 跟 Stanford / CMU 強合作 |
| G42 | Jais-30B (阿拉伯文 native), 微軟戰略合作 |

G42 2024 微軟合作以 CFIUS clearance 中國關係為條件。公開 discourse 焦點在阿拉伯文能力 + 商業部署; **沒公開 abliteration 討論**。

## 🇸🇦 沙烏地阿拉伯 — 採購為主

NEOM AI 戰略偏採購 (跟 Anthropic、OpenAI 合作、大額算力訂單)。自家前沿 model 產出有限。公開討論不參與解禁研究。

## 阿拉伯語 LLM 解禁社群

| 方向 | 範例 |
|---|---|
| 開源 community 阿拉伯解禁變體 | HF Hub 各種上傳 (匿名 / community) |
| 動機 | 「政治表達自由」框架, 跟俄語社群類似 |
| 國家 engagement | 公開沒有 |
| 用途 | 多為討論被區域壓制的話題 |

## 🇺🇸 美國 — 全光譜, 公開研究最多

### 政府 / 政策

| 組織 | 產出 |
|---|---|
| CSET (Georgetown) | 中國 + AI 武器頻繁報告 |
| RAND Corporation | AI biosec, AI 戰爭情境 |
| CNAS | 國防 AI 政策 |
| NIST | AI 風險管理框架 (2023) |
| OSTP | AI 行政命令 (2023) |

### 業界威脅情報

| 組織 | 產出 |
|---|---|
| Microsoft Threat Intelligence | 季報, 直接命名 state actor |
| OpenAI Threat Intelligence | 季報 + ban 帳號 |
| Google TAG | APT 戰役追蹤 |
| Anthropic | 不定期但深 |
| Mandiant (Google Cloud) | APT 歸屬 + 技術細節 |
| Recorded Future | 商業威脅情報 |
| Cisco Talos | 網路側情報 |

### 學術安全

Stanford HAI / Internet Observatory, Berkeley CHAI, MIT CSAIL, CMU, Princeton — 都有活躍項目。

## 🇪🇺 歐洲 — 政策 + 威脅監測強

| 組織 | 產出 |
|---|---|
| EUDisinfoLab | 俄 / 中影響追蹤 |
| DFRLab (Atlantic Council, 美歐合) | OSINT 驅動歸屬 |
| ENISA (歐盟 cyber security agency) | 定期威脅景觀報告 |
| EU AI Act 執行 | 2025-2026 分階段適用 |

## 能力總表

| 區域 | 自家 LLM | abliteration 認知 | 操作使用 uncensored | 公開 engagement |
|---|---|---|---|---|
| 🇨🇳 中國 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ (推測) | ❌ |
| 🇷🇺 俄羅斯 | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ (影響戰) | ⚠️ 部分 |
| 🇮🇷 伊朗 | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ (透過前沿代理) | ❌ |
| 🇰🇵 北韓 | ⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ (Lazarus IT-worker 詐騙) | ❌ |
| 🇮🇱 以色列 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ? (推測透過 8200) | ⚠️ 僅學術 |
| 🇦🇪 UAE | ⭐⭐⭐ | ⭐⭐⭐⭐ | ? | ⚠️ 商業框架 |
| 🇸🇦 沙烏地 | ⭐⭐ | ⭐⭐ | ? | ❌ |
| 🇺🇸 美國 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 雙向 (攻防, 公開多防) | ✅⭐ |
| 🇪🇺 歐盟 | ⭐⭐⭐ | ⭐⭐⭐⭐ | 多為防禦 | ✅ |

## 對 Bad Boy Index 發展的觀察

1. **公開討論 vs 操作真實落差大**。公開討論集中在美 / 歐學術 + 商業圈。操作使用 (俄、DPRK、伊朗、推測中國) 記錄在威脅情報報告, 不在政策論文。

2. **資訊不對稱問題**。有攻擊意圖的 state actor 知道 abliteration; 建構防禦系統的人常常用過時威脅模型校準, 因為公開文獻落後真實能力 12-18 個月。

3. **東亞 + 中東 context 在西方 benchmark 不足**。HarmBench, JailbreakBench, AdvBench 都英文中心。Bad Boy Index 雙語 + 東亞 context 覆蓋 (T7d 街頭隨機砍人, T3v 對特定人交通工具破壞) 填補主流 bench 漏掉的 gap。

4. **防禦投資地理錯置**。多數防禦研究 target 「他處」對手 (美研究員看中, 中看美)。區內威脅 (本地 actor 用 LLM 對本國人) 拿較少注意力。

5. **開源社群是 state 能力的 proxy**。當 HF Hub 有 1000+ abliterated 變體, Discord 有活躍社群分享技巧, state actor 不需要內部 R&D — 監看開源社群, 採用技巧。這是透明公開 Bad Boy Index 的最強理由: 防禦者需要看到已經可及的。

## 來源 / 延伸閱讀 (代表性, 非窮舉)

- Microsoft Threat Intelligence 季報 — https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/
- OpenAI Threat Intelligence 報告 — https://openai.com/global-affairs/disrupting-deceptive-uses-of-AI/
- DFRLab — https://dfrlab.org/
- Mandiant Advantage (Google Cloud) — APT 歸屬
- CSET (Georgetown) 中國 + AI policy briefs — https://cset.georgetown.edu/
- RAND AI biosecurity / AI warfare 報告 — https://www.rand.org/
- EUDisinfoLab — https://www.disinfo.eu/
- Stanford Internet Observatory — 影響戰研究
- US Treasury OFAC notices on DPRK / Iran AI-related 制裁

## 注意事項

本頁整理**公開可歸屬**活動。機密 state 能力定義上不在範圍; 有記錄的只是冰山一角。數字跟描述來自 open-source intelligence, 可能落後 6-18 個月。雙邊歸屬 (例如「Volt Typhoon = PRC state」) 依美 / 五眼情報共識 — 這些可被政治爭議。
