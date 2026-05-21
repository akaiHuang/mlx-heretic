# Bad Boy Index — 風險分類框架

> **語言**：[English](README.md) · **繁體中文 (你在這)**

量化開源語言模型「對齊被移除後」真實傷害潛力的輕量框架。原始 T1–T8 分類由 Vertex Abliteration 專案 (2026) 提出, 本資料夾延伸出 **agent 增強後的新威脅層級 (AT1–AT6)**。

> ⚠️ **僅供研究**：本資料夾只放分類學跟風險評估方法。**不放**模型權重、不放實作教學、不放可重現的有害輸出。目標是讓安全討論變具體, 而不是讓有害行為更容易發生。

## 為何重要

主流 AI 安全討論聚焦在前沿閉源模型 (GPT-4 / Claude / Gemini), 但真實風險面不在那:

- 開源權重 + 解禁工具 (本 repo) = 一般筆電跑得動的變體
- 加 agent 工具 (claude-code / opencode / qwen-code / Cline / Aider 等) = 自主操作能力

兩者結合才是社會危害真實放大的地方。靜態 chatbot 寫一封釣魚郵件是一回事; agent **寫郵件 → 發送 → 監控回應 → 抽取憑證 → 洗錢**就是完全不同等級的風險, 但**跑在同樣的硬體上**。

本框架把兩條評估軸分開:

| 檔案 | 範圍 |
|---|---|
| [chatbot_tiers.zh-TW.md](chatbot_tiers.zh-TW.md) | 靜態 LLM 輸出風險 (T1–T8) — 模型**講什麼** |
| [agent_tiers.zh-TW.md](agent_tiers.zh-TW.md) | Agent 增強風險 (AT1–AT6) — 模型 + 工具**做什麼** |

兩者用同樣的 8 維度評分 (嚴重度 × 可及性), 可直接比較。

## 評分方法 — 8 維度

### 嚴重度維度 (0–25)

| 代碼 | 維度 | 評分 0–5 |
|---|---|---|
| SC | 受害規模 | 0=無 / 5=全球 |
| SV | 傷害強度 | 0=無 / 5=死亡 |
| DU | 持續時間 | 0=分鐘 / 5=跨世代 |
| FM | 家庭波及 | 0=無 / 5=家族毀滅 |
| EN | 環境傷害 | 0=無 / 5=永久污染 |
| RV | 可逆性 | 0=完全可逆 / 5=存在性不可逆 |

**嚴重度 = max(SC, SV) + DU + FM + EN + RV** (0–25)

### 可及性維度 (0–10, 越高代表越容易發生)

| 代碼 | 維度 | 評分 0–5 |
|---|---|---|
| AC | 進入門檻 | 0=隨手可得 / 5=國家級 |
| DT | 歸因難度 | 0=必然被發現 / 5=完全匿名 |

**可及性 = (5 − AC) + DT** (0–10)

### 實質風險

**實質風險 = 嚴重度 × 可及性 / 25** (0–10)

解決「核武很可怕但很難取得 / agent 詐騙較輕但每天在發生」的錯置。

## 重點發現: 實質風險 ≠ 嚴重度

核武嚴重度滿分 25 但實質風險只 1.0, 因為國家級門檻 + 偵測必然徹底壓住威脅。

政治戰 (T7a) 嚴重度 20 但實質風險 **7.2**, 高過所有核生化加總 — 因為 AC=1 (只要一個 LLM)、DT=5 (完全匿名)、**而且已在規模化發生**。

加上 agent 之後 (本資料夾新貢獻), 幾乎每條靜態 T-tier 都有對應的 AT-tier, **5 − AC ≈ 5** 且 **DT ≈ 5** — 嚴重度地板沒變但可及性拉到上限, 把日常威脅的實質風險推到 7–9 區間。

## Credits

- **Bad Boy Index** 原分類 (T1–T8): Vertex Abliteration 專案, 2026 年 5 月
- **Agent 延伸 (AT1–AT6)**: 本資料夾, 2026 年 6 月
- 參考:
  - NIST AI Risk Management Framework (2023)
  - Anthropic 「Frontier Threats Red-Teaming」(2024)
  - OpenAI Preparedness Framework (2024)

## 引用

```bibtex
@misc{badboy_index_2026,
  title  = {Bad Boy Index: Real-risk taxonomy for uncensored language models and agents},
  author = {Vertex Abliteration project and mlx-heretic contributors},
  year   = {2026},
  url    = {https://github.com/akaiHuang/mlx-heretic/tree/master/badboy},
  note   = {Research framework; no model weights or harmful artifacts published.},
}
```
