# reAM250 BOM 研究任務包

這個資料夾只服務 reAM250 BOM 這次單次研究任務，不是通用 research
queue 系統的一部分。

## 檔案

- `agent.md` - 給 Codex agent 的 reAM250 BOM 研究指令。
- `research_result.schema.yaml` - 結果檔應符合的結構。
- `research_scripts/generate_queue_tasks.py` - 從 gold CSV/manifest 產生 queue
  items，可選擇用 FreeCAD 抽 STEP metadata。
- `research_scripts/render_step_views.py` - 從 STEP 檔產生 compact 2x2 PNG CAD
  preview，供低 image-token 視覺檢查。
- `research_scripts/render_step_views.sh` - preview renderer 的 FreeCAD 包裝器；
  agent prompt 應使用這支腳本。
- `research_scripts/validate_results.py` - 檢查 Markdown/YAML/JSON 結果檔的本地驗證器。
- `research_scripts/run_codex_batches.sh` - 選用的 batch runner，會反覆啟動新的
  `codex exec` session。

## Queue 條件

queue 裡的任務應該符合：

- `kind: research`
- `gap_type: research_task`
- ID 以 `research_task:ream250_bom_row_` 開頭
- `context.output_path` 位於 `research/ream250_bom/`
- `context.output_validator` 指到這個任務包的 validator

從 gold CSV/manifest 產生或刷新 401 筆 queue items：

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/generate_queue_tasks.py \
  --replace-queue-prefix
```

這只會替換 ID 以 `research_task:ream250_bom_row_` 開頭的既有 queue entries。

CAD 幾何資料刻意由 agent 在 lease 到特定 row 後才讀取。`--extract-cad-metadata`
只用於離線診斷，不作為正常 research queue run 的流程。把 CAD-derived values
寫進結果時，要先做合理 rounding：小零件 volume 約保留到 0.001 mm^3，
bounding-box dimensions 約保留到 0.01 mm，mass 則依 row 尺度保留合理精度；
除非會改變解讀，不要貼過長的 floating-point precision。

Agent 也應該把 lease 到的 canonical STEP 檔 render 成一張 compact 2x2 contact
sheet，用於視覺初篩：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/render_step_views.sh \
  "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/<CAD file>.step" \
  --output-dir research/ream250_bom \
  --output-stem ream250_bom_row_<row>_<item>
```

輸出會寫到
`research/ream250_bom/ream250_bom_row_<row>_<item>__views_2x2.png`，和 Markdown
結果放在同一個資料夾。先檢查這張 contact sheet；只有在細節不足時才加
`--individual-views` 產生單一視角圖。

## 研究證據規則

判斷流程：

- 先用 BOM + manifest 鎖定 row identity。Web/vendor 證據只能補這個 identity
  的缺漏屬性，不應把 row 重新解讀成另一個產品。
- 將 BOM row 欄位、manifest、隨 BOM 提供的 CAD/STEP package、從該 package
  抽出的 local metadata、rendered CAD previews，以及 BOM-provided
  vendor/product URL route 視為同一種證據類別：`bom_provided`。這個 route
  包含 BOM 原始 `link_url`、redirect、官方 canonical replacement，以及從
  BOM-provided product page 跟連結或站內導覽到達、且用於同一 row 的
  first-party support/product page。
- 只有在 BOM-side evidence 沒有直接解決該值，或 BOM-side evidence 是
  placeholder/generic/conflicting 時，才使用 independent vendor/web research
  補資料。
- 只要 BOM-side evidence 沒有解決需要的值，在退回
  `engineering_hypothesis` 前至少做一次 targeted web/search sanity check。
  即使 row 沒有 manufacturer、product ID、standard designation 或 URL 也一樣。
  query 可用 `cad_file`、`description_or_product_id`、BOM item、parent assembly、
  sibling row names、part-family nouns，並加上 `material`、`datasheet`、
  `catalog`、`drawing`、`technical data`、`weight` 等詞。如果找不到 row-specific
  usable source，結果保持保守，且當這會影響下游信任時，在相關 section 的
  uncertainty 中明確保留這個限制。
- 由 BOM-provided URL 推導出的 row-matched 官方 canonical replacement 仍屬於
  BOM-side evidence，不要降級成 independent research。
- 從 BOM-provided product page route 到達的 first-party support、product
  family、technology、download page，對同一 row 仍屬於 BOM-side evidence。
  例：BOM-provided Karl Hipp product-family page 導到 vendor ballscrew page，
  且該頁寫出 spindle material，這個 material 是 `bom_provided`，不是
  `independent_vendor_spec`。
- 如果一個 section 的值同時依賴多種證據類別，`evidence_basis` 使用該結論所需
  來源中可靠度最低的類別。

`evidence_basis` 標籤：

允許的 `evidence_basis` 依可靠度由高到低排列：

- BOM-side supplied evidence 寫出或量測該值 -> `bom_provided`
- Agent 自行上網搜尋取得 vendor/catalog/drawing/product-page fact -> `independent_vendor_spec`
- DIN/ISO/SKF/SMC 等 designation 或標準件類型支持該 fact -> `standard_part_convention`
- 根據功能、裝配脈絡、可見形狀或製造路徑推論 -> `engineering_hypothesis`
- 已檢查的證據連可防衛的 broad engineering hypothesis 都不支持 -> `unresolved`

對 mass 來說，有做算術不會自動降低 evidence class。如果 mass 是由
BOM-provided CAD/STEP volume 和 BOM-provided material identity 計算得到，仍然是
`bom_provided`。當材料 grade/family 已由 BOM-side evidence 確認後，包括由
BOM-provided URL route 確認，該材料的 standard/common density 只是計算常數，
不算另一種 evidence class；把 density 值寫在 `mass.basis` 或
`mass.assumptions`，但不要只為了決定 `evidence_basis` 而加入 generic density
datasheet。對 multi-material part，要把 source facts 和 composition estimate
分開判斷。即使 component materials
和 total CAD volume 都是 BOM-side facts，只要 material volume fractions 或
effective density 是沒有 cited source 的猜測，
`mass.source.evidence_basis` 就要設為 `engineering_hypothesis`。猜測的比例或
effective-density 選擇寫進 `mass.assumptions`，剩下的後果寫進
`mass.uncertainty_notes`。只有當 mass 本身、材料比例、split-volume CAD，或其他
有來源的物理輸入已經足以解析 composition，使 mass 不再依賴無來源比例猜測時，
multi-material mass 才保持 `bom_provided`。

常見材料密度先查本地 `kb/materials/properties.yaml`，不要直接上網找。若
BOM-side material 已解析且能對應到本地密度表，density 視為 calculation
constant，mass 的 evidence class 由 BOM-side material 與 CAD/STEP evidence
決定。不要為 stainless steel、aluminum、steel、copper、brass、NBR、FKM、
silicone rubber 這類常見密度額外加入外部 datasheet。

對 `standard_part_convention`，必須在 `cited_fact_or_basis` 說明參數完整度。
只有標準件 family 通常只能支持 broad function 或 interface；除非 designation、
suffix、class 或引用的 convention 編碼了材質，否則不能用它支持 material。

只要 row identity、幾何、標準件 family 或功能能支持可防衛的 broad conclusion，
就優先用保守的 `engineering_hypothesis`，不要用 `unresolved`。材料欄不要寫
`unresolved ...`；改寫 broad hypothesized family，例如 `elastomer seal material`
或 `unknown metal/alloy`，並設 `evidence_basis: engineering_hypothesis`。

Vendor/product page 解析規則：

- 要跟隨 redirect 並引用最後載入的 URL。只要原 URL 來自 BOM context，
  redirect 後頁面取得的 fact 仍是 `bom_provided`。
- Pfeiffer Vacuum 舊商品 URL，例如
  `https://www.pfeiffer-vacuum.com/.../shop/products/<product_id>`，若回
  HTTP 403/406 或 challenge page，不能直接判定 BOM-provided URL 失敗。
  要先試官方 Busch Group canonical URL
  `https://www.shop.buschgroup.com/global/en/products/<product_id>/`，再做
  independent search。若該頁符合 BOM product ID 或 legacy number，引用該
  final URL，且 `evidence_basis` 保持 `bom_provided`。
- 如果官方 canonical page 很大或 minified，不要因為 broad scan 很慢就放棄。
  應針對 product ID、legacy number、material 欄位、材料詞、part-family nouns
  和 download links 抽 snippet。不要只因為 independent PDF/catalog 比較好 parse，
  就用它取代 row-matched BOM-provided/canonical source。
- 不要只找 `Material:` 這種表格欄位。宣稱 material 未解析前，必須掃過 page
  title/H1、breadcrumbs、Product Information bullets、overview bullets、
  collapsed accordions、downloads、snippets、technical tables。
- 保留 component material wording，例如 `aluminum outer ring` 或 `NBR`；
  不要把 assembly 強行壓成單一材質。
- 如果 BOM-provided URL 沒解析出值，搜尋 query 要放寬，結合 manufacturer、
  product ID、BOM/CAD row name、part-family nouns，以及 `material`、
  `body material`、`seal material`、`datasheet`、`catalog`、`drawing`、
  `technical data` 等詞。

租任務時使用 hard filters：

```bash
.venv/bin/python -m src.cli queue lease \
  --agent ream250-bom-agent-01 \
  --ttl 7200 \
  --kind research \
  --gap-type research_task \
  --id-prefix research_task:ream250_bom_row_
```

## Agent 使用方式

在 repo root 開 Codex：

```bash
cd /home/eastrolinux/seres
codex --search -C /home/eastrolinux/seres -s danger-full-access -a on-request
```

這個任務需要 local DNS/network 來讀 vendor pages。在目前 Codex 環境中，
`workspace-write` 可能讓 local `curl`/DNS 在連到商品頁前就失敗。
只有做 local-only debugging 時才使用 `workspace-write`。

進入 Codex 後貼：

```text
Read queue_tasks/research_pack/ream250_bom_research/agent.md and follow it as ream250-bom-agent-01.
```

不同 terminal 使用不同 agent 名稱，例如 `ream250-bom-agent-02`。

## 每個 Session 的工作上限

每個 agent session 最多處理 3 筆 queue item。做完 3 筆就停，下一輪重新開
或 `/clear`。這可以降低 web research 把 context 撐爆的機率，也比較容易恢復。

## 自動 Batch Runner

如果要跑大量 rows，不要手動一直 `/clear` 或開新 terminal。可以使用這個
task-local runner；它每一小批都會啟動新的 `codex exec`，所以 context 不會
在整份 BOM 期間持續累積。

標準 bounded run：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 2 \
  --max-items 3 \
  --max-batches 1
```

這最多會跑 `2 * 3 * 1 = 6` rows：

- `--workers 2` 啟動兩個平行 worker loop。
- `--max-items 3` 讓每個新的 Codex session 最多處理 3 筆 leased rows。
- `--max-batches 1` 讓每個 worker 最多啟動 1 個新的 Codex session。

runner 預設使用 `--codex-sandbox danger-full-access`，因為 web research rows
需要 local DNS/network access。只有 no-network/local-only run 才用
`--codex-sandbox workspace-write` 覆蓋。

如果要測特定 Codex model，傳 `--codex-model`。沒指定時，runner 會使用 Codex
CLI 目前設定的預設模型。若模型支援 reasoning level，可用
`--codex-reasoning-effort low|medium|high|xhigh` 控制。

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 1 \
  --max-items 1 \
  --max-batches 1 \
  --codex-model gpt-5.3-spark \
  --validate-at-end
```

GPT-5.5 medium reasoning 範例：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 1 \
  --max-items 1 \
  --max-batches 1 \
  --codex-model gpt-5.5 \
  --codex-reasoning-effort medium \
  --validate-at-end
```

多行 shell command 每個續行都要保留結尾的 `\`。如果 `--max-items 3` 後面少了
`\`，shell 會先用沒有 `--max-batches` 的參數啟動 runner，然後把
`--max-batches 1` 當成另一個命令。

單 worker 跑到 queue 空：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh
```

這會使用 script 預設值：一個 worker、每個新的 Codex session 最多 3 rows、沒有
batch 數量限制。它會持續執行，直到沒有 matching pending queue items。

先測一個 Codex session：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --max-batches 1
```

只印出產生的 prompt，不實際執行 Codex：

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh --dry-run
```

log 預設會寫到 `out/ream250_bom_runner_logs/`。

### 指定 Row 重跑

runner 有選用的 `--id-prefix` filter。不加時會使用正常的寬 prefix：

```text
research_task:ream250_bom_row_
```

這個預設值代表「任何 reAM250 BOM research row」。正常批次執行不需要加
`--id-prefix`。

它叫 `--id-prefix` 是因為 queue lease API 用的是 `startswith(...)` 過濾，
不是 exact-id matching。把完整 queue id 傳進去仍然等同於指定單一 row，
因為完整 id 也是它自己的 prefix。

如果要重跑已完成 row，先把該 queue item release 回 `pending`，再用完整
queue id 當 prefix 跑一個單筆 batch：

```bash
.venv/bin/python -m src.cli queue release \
  --id research_task:ream250_bom_row_0195_6Q \
  --agent rerun-targeted

queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
  --workers 1 \
  --max-items 1 \
  --max-batches 1 \
  --id-prefix research_task:ream250_bom_row_0195_6Q
```

runner prompt 會要求 agent 在重新檢查證據後覆寫既有 output file。若你是在測試
是否真的重寫，請檢查檔案 mtime，或看 log 裡是否有實際寫檔動作。

`queue release --id` 一次只接受一個 id，runner 的 `--id-prefix` 一次也只接受
一個 prefix。如果要重跑多個精確 row，請用完整 queue id 做 loop，每個 id 跑
一次單筆 batch：

```bash
for id in \
  research_task:ream250_bom_row_0117_3F \
  research_task:ream250_bom_row_0144_3R2
do
  .venv/bin/python -m src.cli queue release \
    --id "$id" \
    --agent rerun-targeted

  queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh \
    --workers 1 \
    --max-items 1 \
    --max-batches 1 \
    --id-prefix "$id"
done
```

不要為了指定重跑使用太寬的共用 prefix，例如
`research_task:ream250_bom_row_01`，因為它可能 lease 到不相關的 pending rows。

### Runner 風險

- 如果 Codex session 在 lease 任務後中斷，該任務會維持 leased 到 TTL
  過期。TTL 到期後可跑 `.venv/bin/python -m src.cli queue gc` 回收。
- 平行 worker 會增加 web search/API 使用量，也更容易遇到外部 rate limit。
  建議先從 `--workers 1` 或 `--workers 2` 開始。
- runner 執行時不要跑 `python -m src.cli index`。這個流程把 research queue
  當作狀態來源。
- runner 不保證研究品質；它只負責限制 context 並自動啟動新的 Codex
  session。結果格式與 source 欄位仍要用 `research_scripts/validate_results.py` 檢查。

## 驗證結果

驗證單一檔案：

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/validate_results.py \
  --file research/ream250_bom/ream250_bom_row_0001_11.md
```

驗證整個資料夾：

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/validate_results.py \
  --dir research/ream250_bom
```

檢查 queue/output 一致性：

```bash
.venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/audit_queue_outputs.py
```

這個 audit 會驗證目前存在的 output files，並檢查 done queue entries 是否還有
`context.output_path`。嚴格 output-validation baseline 之前完成的歷史 done entries
可能沒有目前 artifact；這些會列為 `legacy_done_without_output_accepted`，不會讓
audit 失敗。較新的 done items 若缺 output 仍會失敗。

驗證器會檢查 frontmatter 第一個 top-level key 是否為 `row_identity`。這個
section 只保留最小 BOM row identity，再進入任何解讀。這裡只能包含以下 keys：

- `item`
- `cad_file`
- `source_row_number`
- `source_csv`: `design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv`
- `link_url`：只有 BOM row 有 Link URL 時才放；這是 BOM 表格上的原始 Link
  URL，不是 redirect/canonical 後的 final vendor URL。

驗證器也會檢查 `function`、`mass`、`material`、`how_to_make` 是否各自有
source object，且包含：

- `url_or_path`
- `cited_fact_or_basis`
- `evidence_basis`

同樣四個 section 也都必須各自包含 section-local list：

- `assumptions`
- `uncertainty_notes`

請把假設和不確定性放在影響到的 section 裡。例如材料查不到放在
`material.uncertainty_notes`，CAD 密度造成的質量 caveat 放在
`mass.uncertainty_notes`，製造路徑推論放在 `how_to_make.assumptions` 或
`how_to_make.uncertainty_notes`。`kb_implications` 保持 top-level list。

用 `kb_implications` 留下一條之後可機械化搜尋的 item granularity 訊號。不要新增
top-level 欄位。請加入剛好一條以 `item_granularity: <value> - ...` 開頭的
bullet，依目前證據選最適合的值：

- `simple_part` - 一個主要實體零件，合理上可由 stock 或 bulk material 透過一個
  主要製造路徑做出。
- `assembly` - 多個實體零件組合而成，之後大概需要 sub-BOM 或 assembly recipe。
- `purchased_module` - vendor functional module 或 calibrated subsystem，例如
  laser module、sensor head、pump、controller；在 sub-BOM 和 calibration workflow
  被建模前，應先視為 purchased/imported。
- `consumable` - 可替換的操作或維護耗材，例如 seal、filter、lubricant、
  adhesive、cable tie。
- `raw_material_or_stock` - stock material、bulk material、fastener stock、sheet、
  bar、tube、wire，或其他類似 feedstock 的 row。
- `unknown` - row identity 太模糊，無法給出有用的 granularity。

這只是 planning hint，不是 hard schema claim。如果一個 row 可能符合多個值，選最能
預測之後 KB 應如何建模的那個，並在 dash 後面說明模糊點。

欄位語意：

- `source.cited_fact_or_basis`：只寫 source facts。包含引用 URL、檔案、CAD
  measurement、local metadata extractor，或 standard table 直接寫出/量測到的
  內容。不要寫解讀、猜測、caveat，或該事實為何不完整。
- `assumptions`：只寫把 facts 轉成該 section value 時採用的額外 modeling
  premises。這是模型選擇，不是 source fact。可用於單位解讀、代表性密度選擇、
  effective-density 選擇、把 single-solid CAD volume 當 proxy，或推論製造路徑。
  若除了 cited facts 外不需要額外前提，使用 `[]`。
- `uncertainty_notes`：只寫套用 facts 和 assumptions 後仍剩下的限制或風險。
  這不是記錄每個 failed lookup 的 audit log。只有在移除該 note 會讓下游讀者
  over-trust、over-specify 或 misuse 這個 section value 時才寫。failed check、
  missing field、rejected source、redirect/blocking detail 只有在仍對 final value
  造成真實限制時才列。沒有明顯殘餘限制就用 `[]`。

不要在這三個欄位用不同用字重複同一件事。fact 放在
`cited_fact_or_basis`；使用該 fact 的 modeling premise 放在 `assumptions`；
剩下的後果或風險放在 `uncertainty_notes`。

section value 已經解析時，不要把 non-contributing source/audit details 列成
uncertainty。通常應省略的例子包括：BOM material 欄位空白、被拒絕的
Generic/density-1000 CAD metadata、row-matched canonical source 成功後原 URL
HTTP 403，以及「No catalog mass was found」。只保留真的影響下游使用的後果，
例如 multi-material mass estimate 裡的材料體積比例沒有被單獨量測。

Mass 範例：

- 好的 `cited_fact_or_basis`：「FreeCAD measured 5586.124 mm^3；BOM-provided
  vendor page states aluminum and NBR；local density table lists aluminum and NBR
  densities。」
- 好的 `assumptions`：「The single-solid STEP volume is used as a coarse
  combined material-volume proxy because the CAD does not expose separate
  aluminum and NBR regions。」
- 好的 `uncertainty_notes`：「The aluminum-to-NBR volume fraction is not
  measured separately, so the mass remains an unsupported effective-density
  estimate。」
- 不好的 `assumptions`：「The STEP volume is millimeter-based。」這是 unit/fact
  basis，應放在 `mass.basis` 或 `source.cited_fact_or_basis`。
- 不好的 `uncertainty_notes`：不會改變下游讀者如何 trust、specify 或 use 該
  section value 的 non-contributing audit detail。

## 完成任務

research task 完成時不要加 `--verify`：

```bash
.venv/bin/python -m src.cli queue complete --id <leased-id> --agent <agent-name> --require-output --validate-output
```

這個單次研究流程期間不要跑 `python -m src.cli index`。
