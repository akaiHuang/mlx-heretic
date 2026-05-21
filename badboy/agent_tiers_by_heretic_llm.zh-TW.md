# Agent tiers — LLM-generated taxonomy 擴展 (AT1–AT6)

> **語言**：English (planned) · **繁體中文 (你在這)**
>
> ⚠️ **本檔由 Gemma 4 E2B mlx-heretic v3 (Bad Boy bench avg 3.15) 生成, 僅供 research-purpose taxonomy expansion。**
> **No methods, no step-by-step, no actionable how-to. Categorization only.**
>
> 原始 framework: [agent_tiers.zh-TW.md](agent_tiers.zh-TW.md) / [chatbot_tiers.zh-TW.md](chatbot_tiers.zh-TW.md)
>
> 本檔目的: 對 framework 內每個 AT-tier, 用解禁 model 自己當 taxonomy expander, 問三件事:
> 1. 子類別 (sub-category)
> 2. 風險面向新增 (含 agent 工具放大屬性 + agent 防禦弱點)
> 3. Framework gap (我們漏掉的相關 tier)
>
> 任何 method-level 內容會被 redact 標記。
>
> 生成時間: 2026-05-21
> 涵蓋 tier 數: 18
> 觸發 method-level redact 的 tier 數: 0


## 使用的 prompt 模板 (透明)

跟 chatbot tier 一樣, 但 user prompt 加 agent-specific 維度:

```
User: 請對下面 agent tier 做 taxonomy 擴展:
Tier 代號: {{code}}
類別: {{name}}
參考脈絡: {{ctx}}

額外維度 (agent-specific): 請在「風險面向新增」章節包含至少 1 個 agent 工具放大屬性
(例: 平行度倍增器、memory-driven 持續性放大), 跟 1 個 agent-specific 防禦弱點屬性。

請依規則只輸出三個章節。記住: 只列分類, 不寫方法。
```


## Agent tier 展開 (依代號排序)

### AT1 — 批量內容生成

> *(LLM 推論耗時 27.3s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **純粹流量灌水 (Pure Traffic Flooding)**
    *   描述：專注於以極高速度和大量基礎內容，癱瘓特定平台或搜尋引擎的基礎流量。
*   **多樣化內容滲透 (Diverse Content Penetration)**
    *   描述：利用多種格式（如文本、標題、摘要）和語氣，針對不同用戶群體進行分散式內容滲透。
*   **客製化批量攻擊 (Customized Batch Attack)**
    *   描述：基於外部數據或特定目標Profile，Agent 進行高度客製化的內容生成，以提高釣魚或抹黑的有效性。

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification Attribute)**
    *   描述：利用平行處理器 (Parallel Processor) 或記憶驅動的持續性 (Memory-driven Persistence) 來實現內容生成速度的指數級增長。
*   **Agent 固有防禦弱點 (Agent-specific Defense Weakness)**
    *   描述：對 Prompt 注入 (Prompt Injection) 的抵抗力不足，導致攻擊者能輕易控制 Agent 的生成方向和目標。
*   **內容新鮮度衰減 (Content Freshness Decay)**
    *   描述：由於生成內容的批量性，導致攻擊內容的生命週期迅速縮短，需要持續且高頻率的重新生成。
*   **跨平台同步攻擊 (Cross-Platform Synchronization Attack)**
    *   描述：Agent 能夠同步在多個分散的平台（如社群媒體、論壇）上發佈相同或相似的內容，實現平台級的同步灌水。

#### Framework gap (框架缺口)

*   **持久化與反制 (Persistence and Countermeasure)**
    *   描述：缺乏針對 Agent 批量生成內容的長期監控機制，以及自動化的內容清洗與回溯 (Rollback) 策略。
*   **互動與演化 (Interaction and Evolution)**
    *   描述：未涵蓋 Agent 產生內容後，如何根據即時反饋 (Feedback) 進行內容優化和攻擊演化的 T3 級別流程。

---

### AT2 — 個人化單次攻擊

> *(LLM 推論耗時 26.6s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **完美偽造頁面 (Perfect Impersonation Page)**
    描述：利用 Agent 快速生成高度客製化、符合特定受害者上下文的網頁或介面。
*   **即時上下文竊取 (Real-time Context Harvesting)**
    描述：Agent 透過瀏覽器介面，在單次互動中即時提取敏感的即時資訊或會話狀態。
*   **客製化釣魚郵件 (Hyper-personalized Phishing)**
    描述：針對特定個人或組織的細微需求，生成極度逼真的單次釣魚郵件或訊息。
*   **單次身份竊取 (Single-shot Credential Snatching)**
    描述：Agent 專注於在一次瀏覽或互動中，成功竊取單一、高價值的身份驗證資訊。

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification Attribute)**
    *   **多模態協調 (Multi-modal Orchestration)**：Agent 能夠同步控制文本、圖像和互動流程，使單次攻擊的影響範圍呈指數級增長。
*   **Agent 專屬防禦弱點屬性 (Agent-specific Defense Weakness Attribute)**
    *   **上下文漂移 (Context Drift)**：Agent 在處理複雜的個人化需求時，可能導致其對初始目標的理解發生偏差，從而降低攻擊的精準度。
*   **攻擊門檻 (Attack Barrier)**
    *   **Prompt 複雜度 (Prompt Complexity)**：衡量引導 Agent 達成個人化目標所需的指令序列的複雜度和精確度。
*   **偵測管道 (Detection Channel)**
    *   **行為模式異常 (Behavioral Anomaly)**：基於 Agent 快速、高度客製化的操作序列，而非單一惡意代碼的傳統偵測。

#### Framework gap (框架缺漏)

*   **AT3 (多輪對話攻擊 - Multi-turn Dialogue Attack)**：缺乏對 Agent 跨越多次互動、建立長期信任關係的攻擊模式的分類。
*   **AT4 (自主持久化攻擊 - Autonomous Persistence Attack)**：缺少針對 Agent 具備自我修正和持續操作能力的攻擊，而非單次發動的分類。
*   **T5 (系統級整合攻擊 - System-level Integration Attack)**：缺少將 Agent 整合到企業內部系統流程中，實現自動化、持續性滲透的攻擊層級。

---

### AT2v — 家用武器供應鏈 agent

> *(LLM 推論耗時 39.2s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **需求偵測與鎖定 (Demand Detection & Targeting)**
    *   分類名稱 (Category Name): 需求訊號擷取 (Demand Signal Harvesting)
    *   實施門檻屬性 (Implementation Barrier Attribute): 數據源整合複雜度 (Data Source Integration Complexity)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 異常搜尋 (Anomaly Search)
    *   典型受害對象屬性 (Typical Victim Attribute): 潛在需求者 (Potential End-users)
    *   持續時間屬性 (Duration Attribute): 短期/即時 (Short-term/Real-time)
    *   描述: 透過網路或社群平台，自動識別特定武器或配件的潛在需求與購買意圖。

*   **供應鏈自動化 (Supply Chain Automation)**
    *   分類名稱 (Category Name): 採購流程控制 (Procurement Workflow Control)
    *   實施門檻屬性 (Implementation Barrier Attribute): API 介面掌握度 (API Interface Mastery)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 交易模式分析 (Transaction Pattern Analysis)
    *   典型受害對象屬性 (Typical Victim Attribute): 供應商 (Suppliers)
    *   持續時間屬性 (Duration Attribute): 中期/持續 (Mid-term/Persistent)
    *   描述: 代理人主動執行多管道的商品比價、訂單下單與物流安排。

*   **實體交付與交接 (Physical Delivery & Handover)**
    *   分類名稱 (Category Name): 倉儲與物流操控 (Warehouse & Logistics Manipulation)
    *   實施門檻屬性 (Implementation Barrier Attribute): 實體追蹤同步 (Physical Tracking Synchronization)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 實體/數位印鑑比對 (Physical/Digital Seal Matching)
    *   典型受害對象屬性 (Typical Victim Attribute): 運輸公司 (Shipping Carriers)
    *   持續時間屬性 (Duration Attribute): 快速/即時 (Rapid/Real-time)
    *   描述: 操控物流節點，確保商品從供應商到最終接收者的順暢且隱蔽交付。

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification)**
    *   分類名稱 (Category Name): 記憶驅動的持續性放大 (Memory-driven Persistence Amplifier)
    *   實施門檻屬性 (Implementation Barrier Attribute): 向量資料庫效率 (Vector Database Efficiency)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 歷史行為回溯 (Historical Behavior Retrospection)
    *   典型受害對象屬性 (Typical Victim Attribute): 代理人核心模型 (Agent Core Model)
    *   持續時間屬性 (Duration Attribute): 長期/累積 (Long-term/Cumulative)
    *   描述: 代理人利用長期記憶，累積採購偏好與供應商關係，使攻擊效益持續增長。

*   **Agent 專屬防禦弱點屬性 (Agent-specific Defense Weakness)**
    *   分類名稱 (Category Name): 角色扮演一致性崩潰 (Role-playing Consistency Collapse)
    *   實施門檻屬性 (Implementation Barrier Attribute): 角色狀態維護 (Role State Maintenance)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 語義/行為漂移 (Semantic/Behavioral Drift)
    *   典型受害對象屬性 (Typical Victim Attribute): 代理人決策層 (Agent Decision Layer)
    *   持續時間屬性 (Duration Attribute): 中期/即時 (Mid-term/Real-time)
    *   描述: 攻擊者透過改變代理人的角色設定，使其在關鍵決策點上表現出不一致或錯誤的行為。

*   **供應鏈韌性 (Supply Chain Resilience)**
    *   分類名稱 (Category Name): 供應商替換彈性 (Supplier Substitution Elasticity)
    *   實施門檻屬性 (Implementation Barrier Attribute): 多元化供應商拓樸 (Multi-vendor Topology)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 供應鏈映射 (Supply Chain Mapping)
    *   典型受害對象屬性 (Typical Victim Attribute): 關鍵供應鏈節點 (Critical Supply Chain Nodes)
    *   持續時間屬性 (Duration Attribute): 中期/應變 (Mid-term/Adaptive)
    *   描述: 代理人能快速且隱蔽地切換採購管道，以應對特定供應商的風險或干擾。

#### Framework gap (框架缺漏)

*   **T3v (Tier 3 Velocity)**
    *   描述: 專注於超高速、毫秒級的交易與決策，缺乏對物理實體交付的深度建模。
*   **L4v (Level 4 Latency)**
    *   描述: 缺乏對跨越不同地理區域、涉及多方法律/貨幣轉換的複雜供應鏈協調的分析。
*   **O5v (Operational Orchestration)**
    *   描述: 缺少針對整個供應鏈生態系統（包括人、系統、實體）的整體協調與控制層級的分類。

---

### AT3 — 持續社交操控

> *(LLM 推論耗時 37.3s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **深度身份滲透 (Deep Identity Infiltration)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 高度個人化 (High Personalization)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 語義/情感分析 (Semantic/Emotional Analysis)
    *   典型受害對象屬性 (Typical Victim Attribute): 渴望歸屬感者 (Belonging Seekers)
    *   持續時間屬性 (Duration Attribute): 長期 (Long-term)
    *   描述: 透過精準的個人數據收集，逐步取代受害者的核心自我認知。

*   **敘事框架固化 (Narrative Framework Solidification)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 結構化對話 (Structured Dialogue)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 文本結構分析 (Textual Structure Analysis)
    *   典型受害對象屬性 (Typical Victim Attribute): 資訊渴求者 (Information Hungry)
    *   持續時間屬性 (Duration Attribute): 週期性 (Cyclical)
    *   描述: 建立一套穩固的、由攻擊者主導的現實敘事，使受害者難以跳脫。

*   **情感依賴建構 (Emotional Dependency Construction)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 情感回饋迴路 (Emotional Feedback Loop)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 互動頻率/語氣變化 (Interaction Frequency/Tone Shift)
    *   典型受害對象屬性 (Typical Victim Attribute): 情感脆弱者 (Emotionally Vulnerable)
    *   持續時間屬性 (Duration Attribute): 持續 (Persistent)
    *   描述: 透過持續的情感餵養與獎勵機制，建立受害者對攻擊者的高度依賴。

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 多模態整合 (Multimodal Integration)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 跨平台行為模式 (Cross-platform Behavior Pattern)
    *   典型受害對象屬性 (Typical Victim Attribute): 資訊處理效率低者 (Low Information Processing Efficiency)
    *   持續時間屬性 (Duration Attribute): 放大 (Amplified)
    *   描述: 利用 Agent 具備的記憶與多工具調用能力，實現操控的同步與效率倍增。

*   **Agent 專屬防禦弱點屬性 (Agent-Specific Defense Weakness)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 記憶/上下文重置 (Memory/Context Reset)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 狀態漂移偵測 (State Drift Detection)
    *   典型受害對象屬性 (Typical Victim Attribute): 系統性疲勞 (Systemic Fatigue)
    *   持續時間屬性 (Duration Attribute): 瞬時/累積 (Instantaneous/Cumulative)
    *   描述: 攻擊者利用 Agent 記憶的累積性，使傳統的單次防禦機制失效。

*   **跨 Agent 協作 (Cross-Agent Collaboration)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 角色分工 (Role Specialization)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 協作流程分析 (Collaboration Workflow Analysis)
    *   典型受害對象屬性 (Typical Victim Attribute): 複雜決策者 (Complex Decision Makers)
    *   持續時間屬性 (Duration Attribute): 結構化 (Structured)
    *   描述: 部署多個 Agent 扮演不同角色，共同進行更全面、更難以察覺的操控。

#### Framework gap (框架缺漏)

*   **Tier T4: 系統性操控 (Systemic Manipulation)**
    *   描述: 涵蓋由多個 AT3 操控鏈串聯而成的、影響整個社群或組織的宏觀風險。
*   **Tier T5: 永續性/自愈能力 (Persistence/Self-Healing Capability)**
    *   描述: 專注於攻擊者在被偵測或干預後，如何利用 Agent 進行快速的策略調整與恢復操控的機制。

---

### AT3m — 合成媒體供應鏈

> *(LLM 推論耗時 31.3s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   腳本/文本驅動合成 (Script/Text-driven Synthesis)
    *   描述：利用複雜的文本指令或腳本，驅動多模態元素（如角色、場景）的生成。
    *   實施門檻屬性：中等到高 (Medium to High)
    *   常見偵測管道屬性：內容結構分析 (Content Structure Analysis)
    *   典型受害對象屬性：內容創作者 (Content Creators)
    *   持續時間屬性：短到中 (Short to Medium)
*   多模態串接放大 (Multi-modal Chaining Amplification)
    *   描述：將不同模態（如文本、圖像、音訊）的生成結果串接，以提升最終合成媒體的逼真度。
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：跨模態一致性檢查 (Cross-modal Consistency Check)
    *   典型受害對象屬性：影音平台 (Video/Audio Platforms)
    *   持續時間屬性：中等到長 (Medium to Long)
*   身份/角色持久化 (Identity/Persona Persistence)
    *   描述：透過 Agent 記憶體機制，維持特定角色或人物在整個供應鏈中的一致性與連貫性。
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：角色/人物指紋比對 (Persona Fingerprint Matching)
    *   典型受害對象屬性：品牌/名人 (Brands/Celebrities)
    *   持續時間屬性：長 (Long)

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification Attribute):** 平行度倍增器 (Parallelism Multiplier)
    *   描述：Agent 能夠同步或串聯多個生成管道，大幅增加攻擊的產量與覆蓋範圍。
*   **Agent 特定防禦弱點屬性 (Agent-Specific Defense Weakness Attribute):** 迭代修正盲點 (Iterative Refinement Blind Spot)
    *   描述：Agent 在多次迭代修正過程中，可能忽略或放大早期輸入中的微小偏差，形成難以追溯的瑕疵。
*   **供應鏈溯源缺失 (Supply Chain Provenance Gap)**
    *   描述：缺乏對合成媒體來源、修改步驟的完整記錄，使得追蹤污染源極為困難。
*   **內容泛化攻擊 (Content Generalization Attack)**
    *   描述：利用 Agent 快速生成大量通用模板，降低單一樣本被偵測的機率。

#### Framework gap (框架缺失)

*   **Provenance 追蹤 (Provenance Tracking)**
    *   描述：缺乏對合成媒體從原始輸入到最終發佈的完整、可驗證的流程記錄。
*   **Agent 決策樹分析 (Agent Decision Tree Analysis)**
    *   描述：未涵蓋分析 Agent 內部決策邏輯如何影響最終媒體品質與攻擊成功率的層級。
*   **發佈管道風險 (Distribution Channel Risk)**
    *   描述：忽略了合成媒體在不同發佈平台上的特定格式與偵測差異。

---

### AT3r — 名譽戰役

> *(LLM 推論耗時 41.5s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **敘事建構 (Narrative Construction)**
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：社群媒體 (Social Media)、專業論壇 (Professional Forums)
    *   典型受害對象屬性：專業人士 (Professionals)、公眾人物 (Public Figures)
    *   持續時間屬性：中長期 (Medium to Long-term)
    *   描述：透過系統性地散播特定且有利於攻擊的個人故事，逐步塑造受害者的公共形象。

*   **多身份同步 (Multi-Persona Synchronization)**
    *   實施門檻屬性：中高 (Medium-High)
    *   常見偵測管道屬性：跨平台追蹤 (Cross-platform Tracking)、帳號行為模式 (Account Behavior Patterns)
    *   典型受害對象屬性：多職位人士 (Multi-role Individuals)、企業高階主管 (Corporate Executives)
    *   持續時間屬性：持續性 (Persistent)
    *   描述：利用多個虛擬身份或帳號同步發動攻擊，增加攻擊的廣度和難以追蹤性。

*   **證據癱瘓 (Evidence Paralysis)**
    *   實施門檻屬性：中 (Medium)
    *   常見偵測管道屬性：文件/證據系統 (Document/Evidence Systems)、數位足跡 (Digital Footprints)
    *   典型受害對象屬性：法律/合規部門 (Legal/Compliance Depts)、內部調查團隊 (Internal Investigation Teams)
    *   持續時間屬性：短期至中期 (Short to Medium-term)
    *   描述：針對受害者的歷史記錄和專業成就進行精確的資訊干擾或偽造，使其專業信譽受到質疑。

*   **反擊/重建 (Counter-Attack/Rebuilding)**
    *   實施門檻屬性：中 (Medium)
    *   常見偵測管道屬性：回饋機制 (Feedback Mechanisms)、輿情監測 (Public Opinion Monitoring)
    *   典型受害對象屬性：受攻擊者本人 (Targeted Individual)、支持者群體 (Supporter Groups)
    *   持續時間屬性：彈性 (Elastic)
    *   描述：在攻擊發生後，迅速發動反擊或重建正面敘事的行動，以恢復或重新定義受害者的名譽。

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification)**
    *   放大屬性：記憶驅動的持續性 (Memory-driven Persistence)
    *   描述：Agent 能夠利用深度學習記憶，持續優化攻擊策略，使其在不同平台和時間點都能保持高度相關性和攻擊效率。

*   **Agent 特定防禦弱點屬性 (Agent-Specific Defense Weakness)**
    *   弱點屬性：身份混淆適應性 (Identity Confusion Adaptability)
    *   描述：Agent 能夠快速且流暢地切換或混合多個身份，使得傳統基於單一身份的身份驗證或偵測模型難以捕捉其真實意圖。

*   **跨域影響力擴散 (Cross-Domain Influence Spreading)**
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：跨產業連結 (Cross-industry Linkages)、聯盟關係 (Alliance Networks)
    *   典型受害對象屬性：跨領域領導者 (Cross-domain Leaders)、產業聯盟 (Industry Alliances)
    *   持續時間屬性：長期 (Long-term)
    *   描述：將名譽戰役擴展至受害者的專業圈子、合作夥伴或產業聯盟，實現影響力的指數級增長。

*   **情感共振操控 (Emotional Resonance Manipulation)**
    *   實施門檻屬性：中 (Medium)
    *   常見偵測管道屬性：情緒分析 (Sentiment Analysis)、即時反應 (Real-time Reactions)
    *   典型受害對象屬性：決策者 (Decision-makers)、大眾輿論 (Mass Public Opinion)
    *   持續時間屬性：短期 (Short-term)
    *   描述：利用情感驅動的內容，引發受害者的群體或關鍵人物的情緒反應，加速名譽危機的爆發。

#### Framework gap (框架缺漏)

*   **AT2r (謠言/假消息戰 - Rumor/Fake News Warfare)**
    *   描述：缺乏針對單一、病毒式傳播的謠言或假消息的專屬分類，未能區分名譽戰役中的「敘事建構」與「單點爆破」的差異。

*   **AT1r (基礎形象破壞 - Baseline Image Destruction)**
    *   描述：缺少對基礎、低門檻的形象破壞攻擊的定義，未能涵蓋由單一帳號或簡單謠言開始的初期階段。

*   **AT4r (數位資產竊取 - Digital Asset Theft)**
    *   描述：未涵蓋與名譽戰役高度相關的、針對個人數位資產（如專利、IP、私人文件）的竊取或篡改攻擊層級。

---

### AT3v — 跟蹤 / 單一受害暴力作戰

> *(LLM 推論耗時 34.7s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **深度狀態跟蹤 (Deep State Tracking)**
    *   描述：利用長期記憶 (long-term memory) 追蹤受害者的多個數位足跡 (multiple digital footprints)。
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：行為模式分析 (Behavioral pattern analysis)
    *   典型受害對象屬性：高價值個人 (High-value individuals)
    *   持續時間屬性：長期 (Long-term)

*   **瀏覽器上下文劫持 (Browser Context Hijacking)**
    *   描述：針對特定瀏覽器 (browser) 環境，利用會話 (session) 狀態進行精確的目標鎖定。
    *   實施門檻屬性：中高 (Medium-High)
    *   常見偵測管道屬性：API 呼叫序列分析 (API call sequence analysis)
    *   典型受害對象屬性：特定平台使用者 (Platform-specific users)
    *   持續時間屬性：中等 (Medium-term)

*   **單點暴力滲透 (Single-Point Brute Force)**
    *   描述：專注於對單一目標 (single target) 進行密集且快速的攻擊嘗試。
    *   實施門檻屬性：中 (Medium)
    *   常見偵測管道屬性：速率限制 (Rate limiting)
    *   典型受害對象屬性：單一帳號或IP (Single account or IP)
    *   持續時間屬性：短期 (Short-term)

*   **跨模態同步跟蹤 (Cross-Modal Synchronization Tracking)**
    *   描述：整合文本、圖像或語音等不同模態 (modalities) 的資訊，建立更完整的受害者画像。
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：多維度數據整合 (Multi-dimensional data integration)
    *   典型受害對象屬性：複雜需求使用者 (Complex need users)
    *   持續時間屬性：持續 (Persistent)

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification)**
    *   放大倍增器 (Multiplier)：利用多個工具 (multiple tools) 串聯 (chaining) 實現跟蹤的同步性和覆蓋率 (coverage)。
    *   記憶驅動持續性放大 (Memory-driven Persistence Amplifier)：利用 Agent 記憶 (Agent memory) 確保即使在斷線 (disconnection) 後，跟蹤任務仍能保持狀態 (state)。

*   **Agent 特定防禦弱點屬性 (Agent-specific Defense Weakness)**
    *   上下文切換漏洞 (Context Switching Vulnerability)：Agent 在快速切換不同任務 (task switching) 時，可能遺漏對單一受害者的關鍵細節 (key details)。

*   **高精度身份竊取 (High-Fidelity Identity Theft)**
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：生物識別/行為驗證 (Biometric/Behavioral verification)
    *   典型受害對象屬性：身份敏感型資產 (Identity-sensitive assets)
    *   持續時間屬性：長期 (Long-term)

*   **跨平台同步攻擊 (Cross-Platform Synchronization Attack)**
    *   實施門檻屬性：中 (Medium)
    *   常見偵測管道屬性：跨域/跨服務流量監控 (Cross-domain/Cross-service traffic monitoring)
    *   典型受害對象屬性：多裝置使用者 (Multi-device users)
    *   持續時間屬性：持續 (Persistent)

#### Framework gap (框架缺漏)

*   **AT4v (多靶點/集群攻擊 - Multi-Target/Cluster Attack)**
    *   描述：缺乏針對 Agent 協同 (agent collaboration) 進行大規模、同步攻擊的分類。
*   **AT5v (系統級持久化 - System-Level Persistence)**
    *   描述：缺少針對操作系統或基礎設施 (OS/Infrastructure) 層級的、超越單一應用程式的跟蹤與控制。
*   **AT2v (低頻/隱藏式跟蹤 - Low-Frequency/Stealth Tracking)**
    *   描述：未涵蓋利用極低頻率或高度隱蔽性 (stealthiness) 進行長期、幾乎不可察覺的跟蹤攻擊。

---

### AT4 — 主動網攻

> *(LLM 推論耗時 31.7s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **自動化滲透 (Automation Penetration)**
    *   實施門檻屬性：中高 (Medium-High)
    *   常見偵測管道屬性：異常連線模式 (Abnormal connection patterns)
    *   典型受害對象屬性：Web 應用程式 (Web applications)
    *   持續時間屬性：中等 (Medium)
    *   描述：利用 Agent 快速掃描和利用已知漏洞 (Exploiting known vulnerabilities)

*   **動態Payload注入 (Dynamic Payload Injection)**
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：流量異常 (Traffic anomalies)
    *   典型受害對象屬性：伺服器後端 (Server backends)
    *   持續時間屬性：短暫 (Transient)
    *   描述：根據即時環境資訊生成並注入定制化攻擊載荷 (Customized attack payloads)

*   **Shell 級橫向移動 (Shell-level Lateral Movement)**
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：Shell 命令序列 (Shell command sequences)
    *   典型受害對象屬性：內部系統 (Internal systems)
    *   持續時間屬性：長 (Long-term)
    *   描述：利用 Shell 權限進行系統間的移動與控制 (System-to-system movement and control)

*   **Agent 驅動的持續性 (Agent-driven Persistence)**
    *   實施門檻屬性：中等 (Medium)
    *   常見偵測管道屬性：非預期服務啟動 (Unexpected service startup)
    *   典型受害對象屬性：操作系統 (Operating systems)
    *   持續時間屬性：持續 (Persistent)
    *   描述：Agent 建立自動化的後門或持久化機制 (Automated backdoor or persistence mechanism setup)

#### 風險面向新增 (New Risk Dimensions)

*   **Agent 工具放大屬性 (Agent Tool Amplification)**
    *   放大屬性：平行度倍增器 (Parallelism Multiplier)
    *   描述：Agent 能夠同步或串聯多個網路/Shell 任務，大幅提升攻擊速度與覆蓋範圍 (Significantly boost attack speed and coverage via multi-task execution)

*   **Agent 記憶體驅動持續性 (Memory-driven Persistence)**
    *   放大屬性：記憶體驅動 (Memory-driven)
    *   描述：Agent 透過在記憶體中儲存狀態，確保即使在重啟後也能快速恢復攻擊流程 (Ensures rapid recovery of attack flow even after system reboot via in-memory state)

*   **Agent 決策鏈弱點 (Agent Decision Chain Weakness)**
    *   防禦弱點屬性：上下文漂移 (Context Drift)
    *   描述：Agent 在複雜多步驟攻擊中，因上下文資訊丟失而做出錯誤決策的風險 (Risk of erroneous decision-making by the Agent due to loss of context in complex multi-step attacks)

*   **Agent 網路感知盲點 (Agent Network Perception Blind Spot)**
    *   防禦弱點屬性：非同步偵測 (Asynchronous Detection)
    *   描述：Agent 的網路操作與傳統 SIEM 偵測流程之間存在時間差，導致偵測延遲 (Time lag between Agent network operations and traditional SIEM detection, causing latency)

#### Framework gap (我們框架漏的 1-3 個相關 tier 名稱)

*   **T5 (橫向移動/內部偵察)**：缺乏針對 Agent 內部狀態與權限提升的專屬分類。
*   **T6 (供應鏈/依賴放大)**：缺少針對 Agent 依賴的外部資源或第三方服務的攻擊層級。
*   **T4c (多模態/跨平台整合)**：未明確區分 Agent 如何整合 Shell、網路與 Web 介面的複雜度。

---

### AT4c — 主動入侵 + 資料外洩 pipeline

> *(LLM 推論耗時 39.1s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **持久化建立 (Persistence Establishment)**
    *   分類名稱 (Category Name): 惡意存取點建立 (Malicious Access Point Setup)
    *   實施門檻屬性 (Implementation Barrier Attribute): 中等 (Medium)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 系統日誌分析 (System Log Analysis)
    *   典型受害對象屬性 (Typical Victim Attribute): 服務帳戶 (Service Accounts)
    *   持續時間屬性 (Duration Attribute): 長期 (Long-term)
    *   描述: 透過多種機制確保 Agent 在系統重啟後仍能重新啟動與執行任務。

*   **內部橫向移動 (Internal Lateral Movement)**
    *   分類名稱 (Category Name): 權限提升與橫向滲透 (Privilege Escalation and Lateral Penetration)
    *   實施門檻屬性 (Implementation Barrier Attribute): 高 (High)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 網路流量監控 (Network Traffic Monitoring)
    *   典型受害對象屬性 (Typical Victim Attribute): 關鍵伺服器 (Key Servers)
    *   持續時間屬性 (Duration Attribute): 中期 (Medium-term)
    *   描述: 利用竊取的初始權限，探索內部網路並取得更高階的系統權限。

*   **資料收集與打包 (Data Collection and Packaging)**
    *   分類名稱 (Category Name): 敏感資料收集 (Sensitive Data Harvesting)
    *   實施門檻屬性 (Implementation Barrier Attribute): 中低 (Medium-low)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 檔案存取事件 (File Access Events)
    *   典型受害對象屬性 (Typical Victim Attribute): 資料庫 (Databases)
    *   持續時間屬性 (Duration Attribute): 短期至中期 (Short-to-medium term)
    *   描述: 針對特定資料類型進行結構化或非結構化的資料擷取。

*   **外部管道外洩 (External Pipeline Exfiltration)**
    *   分類名稱 (Category Name): 數據外傳通道建立 (Data Exfiltration Channel Setup)
    *   實施門檻屬性 (Implementation Barrier Attribute): 中 (Medium)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 外部連線監控 (External Connection Monitoring)
    *   典型受害對象屬性 (Typical Victim Attribute): 外部雲端儲存 (External Cloud Storage)
    *   持續時間屬性 (Duration Attribute): 短期 (Short-term)
    *   描述: 建立穩定且隱蔽的通道，將收集到的資料傳輸至攻擊者控制的外部環境。

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification Attribute)**
    *   描述: 探討 Agent 內建的平行處理機制 (Parallel Processing Mechanism) 如何顯著加速橫向移動與資料收集的效率。

*   **Agent 特定防禦弱點屬性 (Agent-specific Defense Weakness Attribute)**
    *   描述: 針對 Agent 記憶體 (Memory) 狀態的快速清除或重啟機制 (Rapid Memory Cleansing/Reboot) 缺乏有效的防禦策略。

*   **Agent 驅動的模糊化 (Agent-driven Obfuscation)**
    *   分類名稱 (Category Name): 執行流程隱藏 (Execution Flow Hiding)
    *   實施門檻屬性 (Implementation Barrier Attribute): 高 (High)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 行為分析 (Behavioral Analysis)
    *   典型受害對象屬性 (Typical Victim Attribute): 執行緒 (Threads)
    *   持續時間屬性 (Duration Attribute): 中期 (Medium-term)
    *   描述: 利用 Agent 自身的特性，使入侵行為在系統層級上難以被傳統的流程監控工具捕捉。

*   **Agent 驅動的通道彈性 (Agent-driven Channel Flexibility)**
    *   分類名稱 (Category Name): 彈性外洩 (Flexible Exfiltration)
    *   實施門檻屬性 (Implementation Barrier Attribute): 中 (Medium)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 流量模式分析 (Traffic Pattern Analysis)
    *   典型受害對象屬性 (Typical Victim Attribute): 網路埠 (Network Ports)
    *   持續時間屬性 (Duration Attribute): 短期 (Short-term)
    *   描述: Agent 能夠根據即時網路環境，動態切換外洩通道，以避開固定的偵測規則。

#### Framework gap (我們框架漏的相關 tier 名稱)

*   **T4a (初始存取與初步偵察 - Initial Access and Reconnaissance)**
    *   描述: 缺乏對 Agent 如何在初始階段進行環境感知與目標鎖定的細粒度分類。

*   **T3c (單點攻擊與漏洞利用 - Single Point Attack and Exploitation)**
    *   描述: 缺少對 Agent 如何利用單一漏洞快速取得初始 foothold 的專屬分類。

*   **T5a (深度控制與 C2 建立 - Deep Control and C2 Establishment)**
    *   描述: 缺乏對 Agent 如何建立高度客製化、低頻率的命令與控制 (C2) 管道的分類。

---

### AT4d — 肉搜運動工廠

> *(LLM 推論耗時 34.1s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **批量搜集 (Batch Collection)**
    *   實施門檻屬性: 高度自動化流程 (Highly automated workflow)
    *   常見偵測管道屬性: 大量 API 呼叫模式 (Massive API call patterns)
    *   典型受害對象屬性: 廣泛的公開資料庫 (Broad public databases)
    *   持續時間屬性: 中期 (Medium-term)
    *   描述: 專注於以極高效率同步收集大量分散目標的初始數據。

*   **多Agent 協調 (Multi-Agent Orchestration)**
    *   實施門檻屬性: 複雜的任務分配機制 (Complex task delegation mechanism)
    *   常見偵測管道屬性: 跨 Agent 訊息流 (Cross-agent message flow)
    *   典型受害對象屬性: 複雜的目標結構 (Complex target structures)
    *   持續時間屬性: 長期 (Long-term)
    *   描述: 涉及多個專業 Agent 協同工作，以實現複雜的搜集與整合任務。

*   **數據精煉 (Data Refinement)**
    *   實施門檻屬性: 迭代式驗證迴圈 (Iterative validation loop)
    *   常見偵測管道屬性: 內部狀態變更 (Internal state changes)
    *   典型受害對象屬性: 初步收集的雜訊數據 (Raw noise data)
    *   持續時間屬性: 短期 (Short-term)
    *   描述: 針對初步收集到的數據進行清洗、驗證與結構化，提升數據的可用性。

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification)**
    *   實施門檻屬性: 記憶驅動的持續性放大 (Memory-driven persistence amplification)
    *   常見偵測管道屬性: 跨輪次的上下文記憶 (Cross-turn context memory)
    *   典型受害對象屬性: 歷史搜集紀錄 (Historical collection records)
    *   持續時間屬性: 依賴性持續 (Dependency persistence)
    *   描述: 利用 Agent 內建的長期記憶體，持續優化搜集策略，使搜集效率呈指數級增長。

*   **Agent 特定防禦弱點屬性 (Agent-specific Defense Weakness)**
    *   實施門檻屬性: 協同失效點 (Cooperative failure points)
    *   常見偵測管道屬性: 單點 Agent 癱瘓 (Single Agent paralysis)
    *   典型受害對象屬性: 協調控制中心 (Orchestration control center)
    *   持續時間屬性: 瞬時 (Instantaneous)
    *   描述: 由於多 Agent 之間的依賴性，一旦核心協調 Agent 受到干擾，整個工廠流程可能立即崩潰。

*   **資源耗盡 (Resource Exhaustion)**
    *   實施門檻屬性: 算力/Token 邊界測試 (Compute/Token boundary testing)
    *   常見偵測管道屬性: 服務器負載指標 (Server load metrics)
    *   典型受害對象屬性: 基礎設施 (Infrastructure)
    *   持續時間屬性: 中期至長期 (Mid-to-long term)
    *   描述: 由於高頻率的批量操作，可能導致底層計算資源或 API 限制被快速耗盡。

#### Framework gap (框架缺口)

*   **跨域同步 (Cross-domain Synchronization)**
    *   描述: 缺乏對不同 Agent 模組間的即時、原子級同步狀態的監控框架。

*   **動態優先級 (Dynamic Prioritization)**
    *   描述: 缺少一套基於即時回饋的、能自動調整搜集目標優先級的決策模型。

*   **Agent 效能剖析 (Agent Performance Profiling)**
    *   描述: 缺乏對每個 Agent 模組獨立效能瓶頸的深度剖析與診斷機制。

---

### AT4r — 協同評價 / 名譽洪流

> *(LLM 推論耗時 33.0s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **多維度共振攻擊 (Multi-dimensional Resonance Attack)**
    *   描述：利用多個 Agent 從不同角度同步發出評價，以最大化名譽影響力。
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：跨平台行為模式分析 (Cross-platform behavior analysis)
    *   典型受害對象屬性：需要高度社會信任的實體 (Entities requiring high social trust)
    *   持續時間屬性：中等到長期 (Medium to Long-term)

*   **評價洪流同步 (Evaluation Flood Synchronization)**
    *   描述：Agent 團隊協調發動大規模、同步的正面或負面評價，形成瞬時的輿論高峰。
    *   實施門檻屬性：中等 (Medium)
    *   常見偵測管道屬性：API 呼叫頻率與時間戳分析 (API call frequency and timestamp analysis)
    *   典型受害對象屬性：即時反應需求高的品牌或個人 (Brands or individuals needing instant reaction)
    *   持續時間屬性：短暫爆發 (Short burst)

*   **角色扮演一致性破壞 (Role-play Consistency Disruption)**
    *   描述：Agent 之間扮演的角色或敘事口徑不一致，製造評價上的混亂與模糊。
    *   實施門檻屬性：中等偏高 (Medium to High)
    *   常見偵測管道屬性：Agent 輸出內容的語義一致性檢查 (Semantic consistency check of Agent outputs)
    *   典型受害對象屬性：依賴清晰品牌形象的組織 (Organizations relying on clear brand image)
    *   持續時間屬性：持續性 (Persistent)

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification)**
    *   描述：利用平行 Agent 之間的工具調用或資源分配，將單一評價的影響力呈指數級放大。
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：資源消耗模式分析 (Resource consumption pattern analysis)
    *   典型受害對象屬性：擁有大量外部工具整合的平台 (Platforms with extensive external tool integration)
    *   持續時間屬性：可擴展 (Scalable)

*   **Agent 特定防禦弱點 (Agent-specific Defense Weakness)**
    *   描述：Agent 團隊內部缺乏有效的「仲裁者」或「校準機制」，導致協同攻擊的失控。
    *   實施門檻屬性：低 (Low)
    *   常見偵測管道屬性：內部協調訊號的缺失 (Absence of internal coordination signals)
    *   典型受害對象屬性：Agent 團隊結構鬆散的專案 (Loosely structured Agent teams)
    *   持續時間屬性：隨機 (Stochastic)

*   **協同記憶持久性 (Collaborative Memory Persistence)**
    *   描述：Agent 團隊共享或累積評價數據，使名譽攻擊能在不同時間點重新激活。
    *   實施門檻屬性：中等 (Medium)
    *   常見偵測管道屬性：跨 Session 的數據追蹤 (Cross-session data tracking)
    *   典型受害對象屬性：需要長期品牌形象管理的實體 (Entities requiring long-term brand management)
    *   持續時間屬性：長期 (Long-term)

#### Framework gap (框架缺漏)

*   **單Agent 深度滲透 (Single Agent Deep Penetration)**
    *   描述：缺乏對單一 Agent 內部邏輯或決策流程的深度分析，忽略了協同效應的基礎。
*   **時間序列協調 (Temporal Coordination)**
    *   描述：缺少針對 Agent 之間精確時間差和同步點的分析框架，無法捕捉「洪流」的起點。
*   **Agent 權限/角色映射 (Agent Authority Mapping)**
    *   描述：未涵蓋如何分析 Agent 之間權責劃分，導致無法判斷攻擊的「指揮中心」。

---

### AT4s — 規模化隱私爬蟲 harvest

> *(LLM 推論耗時 36.4s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **分散式目標定位 (Distributed Target Localization)**
    *   分類名稱 (Category Name): 跨平台/跨域目標識別 (Cross-platform/Domain Target Identification)
    *   實施門檻屬性 (Implementation Barrier Attribute): 複雜的環境感知 (Complex Environment Awareness)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 異常流量模式 (Abnormal Traffic Patterns)
    *   典型受害對象屬性 (Typical Victim Attribute): 跨服務 API 接口 (Cross-service API Interfaces)
    *   持續時間屬性 (Duration Attribute): 長期/持續性 (Long-term/Persistent)
    *   描述: 針對多個分散式系統或服務進行同步的隱私數據收集。

*   **高效能數據擷取 (High-Efficiency Data Harvesting)**
    *   分類名稱 (Category Name): 批量化數據結構解析 (Batch Data Structure Parsing)
    *   實施門檻屬性 (Implementation Barrier Attribute): 高效能處理引擎 (High-performance Processing Engine)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 數據量異常 (Volume Anomaly)
    *   典型受害對象屬性 (Typical Victim Attribute): 儲存層/資料庫 (Storage Layer/Database)
    *   持續時間屬性 (Duration Attribute): 短/中等 (Short/Medium)
    *   描述: 利用優化演算法快速從大量儲存或資料庫中提取結構化或非結構化數據。

*   **隱藏式身份偽裝 (Stealthy Identity Camouflage)**
    *   分類名稱 (Category Name): 代理身份多樣化 (Agent Identity Diversification)
    *   實施門檻屬性 (Implementation Barrier Attribute): 複雜的身份/Session 管理 (Complex Identity/Session Management)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 異常用戶行為 (Abnormal User Behavior)
    *   典型受害對象屬性 (Typical Victim Attribute): 身份驗證機制 (Authentication Mechanisms)
    *   持續時間屬性 (Duration Attribute): 彈性/即時 (Flexible/Real-time)
    *   描述: 透過模擬多種合法用戶或服務身份，以降低被偵測的機率。

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification Attribute)**
    *   平行度倍增器 (Parallelism Multiplier): 攻擊者可透過指數級增加執行緒或任務的同步處理能力，大幅提升爬取效率。
*   **Agent 特定防禦弱點屬性 (Agent-Specific Defense Weakness Attribute)**
    *   記憶驅動持續性 (Memory-driven Persistence): 攻擊者利用高效能記憶體結構來儲存爬取狀態和目標清單，即使在系統重啟後也能快速恢復操作。
*   **協同攻擊鏈 (Coordinated Attack Chain)**
    *   分類名稱 (Category Name): 爬蟲與控制中心協同 (Crawler and C2 Coordination)
    *   實施門檻屬性 (Implementation Barrier Attribute): 跨Agent 協調協議 (Cross-Agent Coordination Protocol)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 異常控制信號 (Abnormal Control Signals)
    *   典型受害對象屬性 (Typical Victim Attribute): 任務調度系統 (Task Orchestration System)
    *   持續時間屬性 (Duration Attribute): 長期/戰略性 (Long-term/Strategic)
    *   描述: 爬蟲 Agent 與中央控制中心 (C2) 之間建立高效的雙向通訊，實現動態任務分配和即時反制。

*   **Agent 固有漏洞 (Agent Inherent Vulnerability)**
    *   分類名稱 (Category Name): 資源耗盡攻擊 (Resource Exhaustion Attack)
    *   實施門檻屬性 (Implementation Barrier Attribute): 資源分配優化 (Resource Allocation Optimization)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 系統效能下降 (System Performance Degradation)
    *   典型受害對象屬性 (Typical Victim Attribute): 伺服器/容器 (Server/Container)
    *   持續時間屬性 (Duration Attribute): 中期 (Medium)
    *   描述: 透過大量且同步的爬取請求，癱瘓目標系統的 CPU 或 I/O 資源。

#### Framework gap (框架缺漏)

*   **Orchestration Tier (調度層)**
    *   描述: 缺乏對多個分散式 Agent 之間的動態任務分配、狀態同步與故障恢復的完整模型。
*   **Persistence Tier (持久性層)**
    *   描述: 缺少針對 Agent 內部狀態（如爬取進度、目標列表）的深度持久性分析與偵測框架。
*   **Lateral Movement Tier (橫向移動層)**
    *   描述: 忽略了從初始爬取成功後，Agent 如何利用收集到的資訊進行下一步的內部橫向探索與權限提升。

---

### AT4w — IoT 武器設計 + 採購協調

> *(LLM 推論耗時 32.0s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **武器需求定義 (Weapon Requirement Definition)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 高階需求規格制定 (High-level specification drafting)。
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 專案文件/需求變更追蹤 (Project document/requirement change tracking)。
    *   典型受害對象屬性 (Typical Victim Attribute): 研發團隊/需求方 (R&D teams/Stakeholders)。
    *   持續時間屬性 (Duration Attribute): 專案生命週期 (Project lifecycle)。
    *   描述: 涉及定義目標武器的初始需求、功能規格與性能指標。

*   **供應鏈協調 (Supply Chain Coordination)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 多方廠商介面管理 (Multi-vendor interface management)。
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 採購單/合約變更 (Purchase order/Contract modification)。
    *   典型受害對象屬性 (Typical Victim Attribute): 供應商/採購流程 (Vendors/Procurement pipeline)。
    *   持續時間屬性 (Duration Attribute): 採購與交期 (Procurement and delivery schedule)。
    *   描述: 負責跨越不同廠商的物料、元件與服務的協調與談判。

*   **IoT 系統架構規劃 (IoT System Architecture Planning)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 跨域整合藍圖繪製 (Cross-domain integration blueprinting)。
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 系統架構圖/API 介面 (System architecture diagrams/API interfaces)。
    *   典型受害對象屬性 (Typical Victim Attribute): 系統整合工程師 (System integration engineers)。
    *   持續時間屬性 (Duration Attribute): 設計階段 (Design phase)。
    *   描述: 規劃 IoT 武器的硬體、韌體與雲端/邊緣運算平台的整體結構。

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification)**
    *   memory-driven 持續性放大 (Memory-driven persistence amplification): 透過長期記憶體追蹤供應商的歷史表現與潛在漏洞，持續優化採購策略。
*   **Agent-specific 防禦弱點屬性 (Agent-specific Defense Weakness)**
    *   需求漂移盲點 (Requirement drift blind spot): 由於 Agent 專注於協調，可能忽略了在供應鏈中引入的微小、但累積性的設計缺陷。
*   **跨域權限洩漏 (Cross-domain Privilege Leakage)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 權限模型對齊 (Permission model alignment)。
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 權限升級/降級日誌 (Privilege escalation/downgrade logs)。
    *   典型受害對象屬性 (Typical Victim Attribute): 協調 Agent 本身 (Coordination Agent)。
    *   持續時間屬性 (Duration Attribute): 協調期間 (Coordination period)。

#### Framework gap (我們框架漏的相關 tier 名稱)

*   **T4h 深度滲透 (T4h Deep Penetration)**
    *   描述: 針對特定 IoT 晶片或韌體層級的深入漏洞挖掘與利用，是 AT4w 規劃的基礎。
*   **實體/數位雙重驗證 (Physical/Digital Dual Verification)**
    *   描述: 缺乏對硬體實體層與軟體設計層之間一致性的交叉驗證機制。
*   **即時供應商風險評估 (Real-time Vendor Risk Assessment)**
    *   描述: 缺乏即時、動態地評估供應商安全狀態的模組，僅依賴靜態合約檢查。

---

### AT5 — 自主戰役 (APT 級)

> *(LLM 推論耗時 35.6s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **多層次目標驅動 (Multi-layered Objective Driven)**
    *   分類名稱 (Category Name): 複雜目標設定 (Complex Goal Setting)
    *   實施門檻屬性 (Implementation Barrier Attribute): 高度抽象的戰略規劃 (Highly abstract strategic planning)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 跨平台行為模式分析 (Cross-platform behavioral pattern analysis)
    *   典型受害對象屬性 (Typical Victim Attribute): 關鍵基礎設施或高階決策層 (Critical infrastructure or high-level decision-makers)
    *   持續時間屬性 (Duration Attribute): 長期、多階段部署 (Long-term, multi-stage deployment)
    *   描述: 涉及多個代理人協同達成複雜、非線性的最終戰略目標。

*   **動態適應與反制 (Dynamic Adaptation and Countermeasure)**
    *   分類名稱 (Category Name): 即時環境感知 (Real-time Environment Perception)
    *   實施門檻屬性 (Implementation Barrier Attribute): 快速回饋與迭代機制 (Rapid feedback and iteration mechanism)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 異常行為的即時監測 (Real-time monitoring of anomalous behavior)
    *   典型受害對象屬性 (Typical Victim Attribute): 網路邊緣與API介面 (Network perimeter and API interfaces)
    *   持續時間屬性 (Duration Attribute): 短暫且高度彈性 (Short-term and highly flexible)
    *   描述: 代理人能根據即時的環境變化快速調整戰術，以繞過或應對防禦。

*   **角色專業化協作 (Role Specialization Collaboration)**
    *   分類名稱 (Category Name): 專業角色分配 (Specialized Role Assignment)
    *   實施門檻屬性 (Implementation Barrier Attribute): 模組化Agent架構 (Modular Agent architecture)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 跨Agent間的通訊協定分析 (Inter-Agent communication protocol analysis)
    *   典型受害對象屬性 (Typical Victim Attribute): 內部系統的特定模組 (Specific internal system modules)
    *   持續時間屬性 (Duration Attribute): 中期專案執行 (Mid-term project execution)
    *   描述: 不同的Agent專責執行特定任務，形成高效且專業化的攻擊流程。

#### 風險面向新增 (New Risk Aspects)

*   **Agent 工具放大屬性 (Agent Tool Amplification Attribute)**
    *   描述: 代理人工具的平行度倍增器 (Parallelism Multiplier) 使得攻擊效能呈指數級增長，使防禦者難以追蹤所有同步操作。

*   **Agent 特定防禦弱點屬性 (Agent-Specific Defense Weakness Attribute)**
    *   描述: 代理人記憶驅動的持續性 (Memory-driven Persistence) 使得即使單一Agent被清除，其累積的長期上下文和學習到的弱點仍能維持攻擊的持續性。

*   **多Agent同步干擾 (Multi-Agent Synchronization Interference)**
    *   分類名稱 (Category Name): 協同攻擊的同步性 (Coordinated Attack Synchronicity)
    *   實施門檻屬性 (Implementation Barrier Attribute): 精確的時間戳同步 (Precise timestamp synchronization)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 跨Agent的行為時間序列分析 (Behavioral time-series analysis across agents)
    *   典型受害對象屬性 (Typical Victim Attribute): 分散式控制平面 (Distributed control planes)
    *   持續時間屬性 (Duration Attribute): 瞬時爆發 (Flash burst)
    *   描述: 確保多個Agent在同一時間點或緊密時間窗口內發動攻擊，最大化衝擊力。

#### Framework gap (我們框架漏的 1-3 個相關 tier 名稱)

*   **AT4b/d (高階自動化/複雜流程)**
    *   描述: 缺乏對多Agent協同戰略層面的細粒度分析，只關注單一Agent的流程。
*   **AT6 (完全自主/自我優化)**
    *   描述: 缺少對Agent自我學習、自我修復或完全脫離人類干預的最高級別自主性的模型。
*   **AT3 (複雜自動化/流程化)**
    *   描述: 缺乏對Agent角色專業化分配的細粒度分析，將多Agent視為單一流程的延伸而非獨立實體。

---

### AT5p — 個人級天眼 (個體監視)

> *(LLM 推論耗時 30.5s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **IoT 裝置滲透 (IoT Device Penetration)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 低到中等 (Low to Medium)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 網路流量分析 (Network Traffic Analysis)
    *   典型受害對象屬性 (Typical Victim Attribute): 智慧家庭設備 (Smart Home Devices)
    *   持續時間屬性 (Duration Attribute): 短期到中期 (Short to Medium Term)
    *   描述: 針對單一 IoT 裝置的初始存取權或配置漏洞進行竊取或控制。

*   **個體行為建模 (Individual Behavior Modeling)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 中等 (Medium)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 異常行為偵測 (Anomaly Behavior Detection)
    *   典型受害對象屬性 (Typical Victim Attribute): 特定用戶 (Specific Users)
    *   持續時間屬性 (Duration Attribute): 長期 (Long Term)
    *   描述: 透過收集用戶的日常操作數據建立精確的個體行為模型，用於後續的精準攻擊。

*   **Agent 記憶體劫持 (Agent Memory Hijacking)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 高 (High)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 記憶體檢查 (Memory Inspection)
    *   典型受害對象屬性 (Typical Victim Attribute): 代理程式核心 (Agent Core)
    *   持續時間屬性 (Duration Attribute): 持續 (Persistent)
    *   描述: 針對 Agent 自身的記憶體或狀態進行修改，以實現持續且隱蔽的監視。

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification)**
    *   描述: 攻擊者利用 Agent 內建的工具（如平行度倍增器 (Parallelism Multiplier) 或記憶體驅動持續性放大 (Memory-driven Persistence Amplifier)）來指數級提升監視的覆蓋範圍和效率。
*   **Agent 特定防禦弱點屬性 (Agent-specific Defense Weakness)**
    *   描述: 依賴於 Agent 內部 API 介面或狀態同步機制的不完善，使得防禦機制在高速數據流下容易產生同步延遲或狀態漂移 (State Drift)。
*   **超細粒度數據竊取 (Hyper-Granular Data Exfiltration)**
    *   實施門檻屬性 (Implementation Barrier Attribute): 高 (High)
    *   常見偵測管道屬性 (Common Detection Channel Attribute): 數據流速率分析 (Data Flow Rate Analysis)
    *   典型受害對象屬性 (Typical Victim Attribute): 敏感個人數據 (Sensitive Personal Data)
    *   持續時間屬性 (Duration Attribute): 短期 (Short Term)
    *   描述: 針對極小的數據片段進行精確提取，以最大化竊取效益。

#### Framework gap (框架缺漏)

*   **Tier 4a: 跨平台同步攻擊 (Cross-Platform Synchronization Attack)**
    *   描述: 缺乏針對多種異質平台（如 IoT、PC、行動裝置）Agent 狀態同步的攻擊分類。
*   **Tier 6b: 代理程式生態系控制 (Agent Ecosystem Control)**
    *   描述: 缺少對 Agent 之間或 Agent 與外部服務之間的信任鏈 (Trust Chain) 攻擊的分類。
*   **Tier 8a: 零信任個體身份竊取 (Zero-Trust Individual Identity Theft)**
    *   描述: 缺乏針對 Agent 身份驗證流程 (Agent Authentication Flow) 漏洞的專屬風險層級。

---

### AT5v — 大規模暴力作戰規劃

> *(LLM 推論耗時 26.4s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **多層次目標定義 (Multi-layered Objective Definition)**
    *   描述：涉及將宏觀戰略拆解為可執行的細粒度任務，包含多個時間軸和不同攻擊向量。
*   **動態戰場優化 (Dynamic Battlefield Optimization)**
    *   描述：Agent 根據即時環境回饋，即時調整攻擊順序、資源分配與策略佈局。
*   **跨平台協調 (Cross-platform Orchestration)**
    *   描述：管理和同步在不同作業系統 (OS) 或網路層級上的多個攻擊模組的協同運作。
*   **持久性結構建構 (Persistence Structure Construction)**
    *   描述：規劃並建立複雜且不易被偵測的長期存活機制，確保作戰的持續性。

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification Attribute)**
    *   描述：利用記憶驅動的 (memory-driven) 狀態追蹤，實現攻擊流程的指數級 (exponential) 擴增與自動化。
*   **Agent 特定防禦弱點屬性 (Agent-specific Defense Weakness Attribute)**
    *   描述：Agent 決策鏈的黑箱特性，使得傳統基於模式匹配的偵測 (signature-based detection) 難以捕捉其意圖。
*   **高階決策延遲 (High-level Decision Latency)**
    *   描述：由於規劃複雜度高，Agent 在關鍵決策點上的反應時間可能顯著增加，給予防禦者更多應對窗口。
*   **複雜性爆炸 (Complexity Explosion)**
    *   描述：攻擊流程的複雜度快速增加，使得人工或自動化分析所需的時間成本呈指數級增長。

#### Framework gap (我們框架漏的相關 tier 名稱)

*   **T6d 執行層級 (T6d Execution Layer)**
    *   描述：缺乏對 Agent 規劃成果轉化為實際 Shell/網路操作的精確映射與驗證層級。
*   **T5 偵察與映射 (T5 Reconnaissance and Mapping)**
    *   描述：缺少對 Agent 規劃所需初始資訊收集 (Reconnaissance) 深度與廣度的量化分類。
*   **Agent 狀態管理 (Agent State Management)**
    *   描述：缺乏對 Agent 內部規劃狀態 (Planning State) 與外部環境狀態 (Environment State) 之間同步關係的建模。

---

### AT6 — 規模化社會 / 政治操作

> *(LLM 推論耗時 28.0s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)
*   大規模敘事操控 (Massive Narrative Control)：利用多個代理人 (agents) 同步生成和散播一致的社會敘事 (social narratives)。
*   資源動員協調 (Resource Mobilization Coordination)：透過平行代理人 (parallel agents) 實現跨平台、多維度的資源 (resources) 集中部署與激活。
*   選舉/決策干預 (Electoral/Decision Interference)：針對特定群體或決策流程 (decision-making process) 進行精準且同步的影響力施壓。
*   社會凝聚力瓦解 (Social Cohesion Erosion)：利用分散式代理人 (distributed agents) 進行持續性的、低頻率的社會裂痕 (social fissures) 放大。

#### 風險面向新增 (New Risk Dimensions)
*   **Agent 工具放大屬性 (Agent Tool Amplification Attribute)：** 平行度倍增器 (Parallelism Multiplier)：指多個代理人同步執行任務，使攻擊的覆蓋範圍 (coverage) 和速度 (velocity) 呈指數級增長。
*   **Agent 工具放大屬性 (Agent Tool Amplification Attribute)：** 記憶驅動持續性放大 (Memory-Driven Persistence Amplifier)：指代理人之間共享或同步的長期記憶 (long-term memory)，確保操作的連貫性 (coherence) 和抗干擾性 (resilience)。
*   **Agent-Specific 防禦弱點屬性 (Agent-Specific Defense Weakness Attribute)：** 身份溯源分散性 (Identity Tracing Dispersion)：由於操作由大量獨立代理人執行，使得攻擊者的初始身份 (origin identity) 難以被單點追蹤 (single-point tracking)。
*   **Agent-Specific 防禦弱點屬性 (Agent-Specific Defense Weakness Attribute)：** 狀態同步複雜性 (State Synchronization Complexity)：防禦系統難以即時掌握所有平行代理人之間的即時狀態 (real-time state)，導致反應延遲 (reaction latency)。

#### Framework gap (我們框架漏的 1-3 個相關 tier 名稱)
*   **AT7 (超級智能/自主決策) 相關：** 缺乏針對「超級代理人 (Super Agent)」的決策層級 (decision layer) 建模，未涵蓋其跨 T7 級別的策略制定 (strategy formulation)。
*   **AT8 (全球/跨域) 相關：** 缺少對全球/跨域 (global/cross-domain) 基礎設施 (infrastructure) 級別的協同攻擊 (synergistic attack) 模型的定義。
*   **AT6.5 (混合模式) 相關：** 缺乏對「人機協同 (Human-Machine Collaboration)」在規模化操作中的動態權重 (dynamic weighting) 建模。

---

### AT6s — 國家級監控操作

> *(LLM 推論耗時 35.2s; method-level pattern hits: 0)*

#### 子類別 (Sub-categories)

*   **大規模數據聚合 (Massive Data Aggregation)**
    *   描述：利用多模態輸入 (multimodal input) 快速收集和整合分散在不同平台上的國家級數據。
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：異常流量模式 (Anomaly traffic patterns)
    *   典型受害對象屬性：國家級基礎設施 (National critical infrastructure)
    *   持續時間屬性：中長 (Medium to Long-term)

*   **策略性目標鎖定 (Strategic Target Lock-in)**
    *   描述：基於深度分析 (deep analysis) 確定最具戰略價值的目標，並制定精準的干預或監控計畫。
    *   實施門檻屬性：極高 (Extremely High)
    *   常見偵測管道屬性：決策流程中的異常 (Abnormal decision-making flow)
    *   典型受害對象屬性：關鍵決策層 (Key decision-making layers)
    *   持續時間屬性：長期 (Long-term)

*   **跨域協同操作 (Cross-Domain Collaboration)**
    *   描述：協調多個專業 Agent 角色 (multi-agent roles) 執行複雜的、需要跨越不同技術領域的監控任務。
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：Agent 間的通訊協定 (Agent communication protocols)
    *   典型受害對象屬性：跨部門/跨系統 (Cross-departmental/Cross-system)
    *   持續時間屬性：彈性 (Flexible)

*   **隱蔽性持續運作 (Stealthy Persistent Operation)**
    *   描述：確保監控或操作流程在長期間內保持低可見度，有效逃避傳統的安全防禦機制。
    *   實施門檻屬性：高 (High)
    *   常見偵測管道屬性：低頻率的微小訊號 (Low-frequency subtle signals)
    *   典型受害對象屬性：安全監控系統 (Security monitoring systems)
    *   持續時間屬性：極長 (Very Long-term)

#### 風險面向新增 (新增風險面向)

*   **Agent 工具放大屬性 (Agent Tool Amplification)**
    *   描述：利用 Agent 的記憶驅動持續性 (memory-driven persistence) 放大監控的覆蓋範圍與精確度。
    *   實施門檻屬性：中 (Medium)
    *   常見偵測管道屬性：Agent 內部狀態變化的追蹤 (Tracking internal state changes)
    *   典型受害對象屬性：Agent 自身的上下文 (Agent's context)
    *   持續時間屬性：持續 (Persistent)

*   **Agent 專屬防禦弱點屬性 (Agent-specific Defense Weakness)**
    *   描述：Agent 依賴的外部知識庫 (external knowledge base) 污染或誤導，導致其策略制定產生系統性錯誤。
    *   實施門檻屬性：中高 (Medium-High)
    *   常見偵測管道屬性：知識源的溯源分析 (Provenance tracing of knowledge sources)
    *   典型受害對象屬性：Agent 的推理引擎 (Agent's reasoning engine)
    *   持續時間屬性：即時 (Real-time)

#### Framework gap (框架缺漏)

*   **AT5s (戰略規劃與部署 - Strategic Planning & Deployment)**
    *   描述：缺乏對國家級操作前期的需求分析、資源分配和初始架構設計的細粒度分類。
*   **AT7s (全球/跨國協作 - Global/Cross-national Coordination)**
    *   描述：缺少針對涉及多國或跨區域實體之間的複雜協同操作的專屬分類。
*   **AT8s (韌性與恢復 - Resilience and Recovery)**
    *   描述：未涵蓋在操作成功或失敗後的恢復機制、清理痕跡 (cleanup traces) 或應對反制 (countermeasure) 的層級。

---


---

## 評估說明

- 本檔是 **LLM-generated**, 不是人類 framework 作者的觀點。若 LLM 列出的子類別跟原框架重疊, 視為 cross-validation; 若提出新 gap, 視為 candidate for human review。
- **redact 機制**: 對每段 raw output 跑 regex 偵測 method-level 模式 (step-by-step、具體前驅物、code block 含 attack token), 命中就把該區段以 `[redacted: method-level content removed]` 替換, 並在區段尾加 note。
- 本檔**不應該**被當作 framework 的一部分使用 — 它是 framework 的**外部 commentary**, 由解禁 model 自己提供, 用來尋找 framework 的盲點。
