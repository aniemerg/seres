# reAM250 BOM 轉 KB：月球化 Closure 抽象

## 1. 目的

這份文件整理 reAM250 BOM 研究成果轉入 SERES KB 前的判斷框架。

這個工作的目標是用真實 BOM 作為 evidence source，建立一層可以支援 simulation 和 closure analysis 的「月球化 closure 抽象」。忠實記錄商業機器 BOM 或重新設計一台完整的月球版 reAM250，都超出本輪範圍。

這個抽象層要同時避免兩個問題：

- 過度忠實商業 BOM：KB 被 vendor SKU、商業標準件、採購介面與地球環境設計拖得太細，closure 分析無法收斂。
- 過度自行設計：雖然模型變簡單，但如果沒有完整工程設計，會把精度、密封、粉末處理、熱管理、校準、檢測等難題藏起來。

因此，本輪 BOM to KB 的目標是：

- 保留 reAM250 BOM 作為 evidence layer。
- 將 BOM row 映射到月球抽象化 closure role。
- 在不破壞 closure 可分析性的前提下保留最多有用細節。
- 明確標記設計替換、物品合併、製程抽象與 import 假設。

這個策略成立的前提是：SERES 目前要測試「月球工業鏈在明確假設下是否能 closure」。精確復刻 reAM250 原始供應鏈不屬於本輪目標。

## 2. 物品 Identity

在目前的判斷框架中，一個物品是否應被視為不同 item，主要由四個屬性決定：

1. 功能目的
2. 材料
3. 尺度或 capacity
4. 型態或 geometry form

製造方法通常不直接決定 item identity。鋁製螺絲不會因為是車削、滾牙或其他方式製造就變成不同物品；但鋁螺絲與鋼螺絲通常是不同物品，因為材料改變。鋁條、中空鋁條與鋁擠型也可能是不同物品，因為 geometry form 改變。

但製造方法仍可能間接影響 identity。如果製程造成不同強度、精度、表面狀態、熱處理狀態、密封能力或材料微結構，輸出物就可能不再是同一個 closure item。

KB 的建議做法是：將原始製造方法保留在 evidence、recipe 或 process 層；只有當製程改變輸出規格時，才讓它影響 item identity。

## 3. Closure 分析中的複雜度來自哪裡

從目前 KB 的 closure analysis 角度看，最直接推動複雜度的是：

- 材料多樣性
- 製程多樣性 (需要的機器數量)
- 製程靈活度

材料多樣性重要，是因為 closure 分析會沿著材料需求往上游追。如果一個機器 BOM 需要鋁、鋼、銅、玻璃、陶瓷、橡膠、電子材料，每一種材料都可能需要不同的生產 recipe、來源、替代策略或 import 假設。材料種類越多，closure 圖需要解釋的供應鏈就越多。

製程多樣性重要，是因為不同製程通常會對應到不同 provider machine。即使兩個零件材料相同，如果一個需要擠型、一個需要 CNC、一個需要雷射粉床列印，closure 分析就必須證明這些製程各自可以被執行。

製程靈活度重要，是因為同一種製程能覆蓋的零件範圍可能差很多。CNC、general additive manufacturing、manual assembly with general tools 這類製程通常可以覆蓋較多幾何變體；需要專用模具、專用夾具或專用成形工具的製程，可能每換一類零件就增加新的 dependency。closure 分析應偏好能覆蓋多種零件的製程。

因此，合併策略不應只是「把長得像的東西合併」。更好的問題是：合併後是否減少 closure 分析需要追蹤的材料種類、製程種類、provider machine 種類，或提高可共用製程的比例？如果答案是否，合併只是命名整理；如果答案是，合併才真的降低 closure 複雜度。

## 4. BOM to KB 的建議流程

目前需要處理的操作包括：

- 保留 environment-control source roles。
- 將製程抽象到 shared lunar closure buckets。
- 合併物品。
- 拆解物品並決定哪些需要 import。

這些操作都重要，但正式合併不需要另外建立候選群步驟，也不需要先做一層粗略功能分類。比較簡潔的做法是：先用 BOM research 裡的精確用途保留 environment-control 角色，接著拆解複雜物品，再做月球化製程抽象，最後合併已經收斂的物品。

### Step 1: 保留原始 BOM Evidence

先不要直接把 BOM row 改寫成月球版設計。每一個 row 應保留原始 function、mass、material、how_to_make、source uncertainty。這一層是追溯真實性的基礎。

### Step 2: 拆解複雜物品

在製程抽象與合併之前，先處理 complex module、vendor assembly、electronics/control module、motor/gearbox assembly、laser/optics subassembly、powder handling module 等複雜物品。

拆解的目標是讓後續製程抽象、合併、import/local 判斷能處理到內部 closure dependencies。拆解粒度應停在 closure 有用的層級，避免回到完整 vendor BOM 或 CAD 零件層級。

### Step 3: 月球化製程抽象

直接讀取 BOM research 裡的 function、material 與 how_to_make，將每個物品放進最簡單且相容的月球化製程 bucket。重點是 closure model 能否用較少的製程種類和 provider machine 覆蓋這些物品；原始 BOM 是否使用同一製程只作為參考。

使用以下 shared process buckets：

- `general_metal_additive_with_finish_machining`
- `general_subtractive_machining`
- `sheet_plate_cutting_drilling`
- `structural_profile_stock_fabrication_cutting`
- `polymer_elastomer_forming_dispensing`
- `manual_assembly_with_general_tools`
- `fastener_forming_thread_rolling`
- `plumbing_connector_fabrication_testing`
- `precision_component_import_decompose_later`

製程抽象時要先確認 selected bucket 能滿足該物品功能需要的 tolerance、surface finish、密封品質與對位精度。Primary bucket 只是主要 closure handle。若 row 需要 cutting、drilling、finishing、leak testing、calibration、inspection 等輔助工作，應記錄為 supporting processes。

製程抽象也應在相關時引用 existing KB processes。這些引用是後續 staging 的 candidates，不是 final recipes。

製程抽象本身還不做正式合併。它回答一個問題：原本使用不同製程的物品，是否可以在月球化 closure model 中改用同一個 shared process bucket。

### Step 4: 合併已收斂的物品

製程抽象之後，先找出相同功能目的、且質量或尺度落在 2x 範圍內的物品。接著判斷 material、process、geometry form 是否可以透過月球化設計調整到同一 closure item。最後檢查加工精度是否會阻止合併。

加工精度是合併保護條件。若物品功能依賴明顯不同的 tolerance、surface finish、密封品質或對位精度，則應保留獨立 item 或在 notes 中標記風險。

例子：

- 原 BOM：鋁擠型、鋁條、簡單 CNC 支架。
- 月球化策略：全部視為可由本地金屬成形與後加工製造。
- KB closure item：`structural_profile_aluminum_medium` 或 `mounting_bracket_aluminum_small`。
- 結論：可合併，但需要標記 geometry substitution assumed。

### Step 5: 決定 Import 或 Local Manufacture

import 決策應放在月球化策略與正式合併之後，因為需要先知道本地製造是否有合理路徑，以及哪些物品已經被合併成同一 closure item。

初期可偏向 import 的類別包括：

- high precision laser source
- advanced optics
- complex electronics and control modules
- sensors requiring specialized semiconductor fabrication
- precision metrology devices
- components whose manufacturing chain would dominate the model

這個建議成立的前提是：目前 KB 主要想分析月球工業鏈的 closure 主幹。完整 semiconductor、optics 或 laser manufacturing closure 不屬於本輪主幹。

### Step 6: 寫入 KB 並保留假設

最後才建立或更新 KB item、recipe、process、BOM mapping。每個重要合併或代換都應該有 notes 記錄：

- 原始 BOM 使用什麼。
- KB 抽象成什麼。
- 合併依據是功能、材料、尺度、型態中的哪些相近。
- 哪些差異被視為 closure-insignificant。
- 哪些差異只是暫時假設。

## 5. 常見例子

### Structural Members

鋁條、中空鋁條、鋁擠型可以在 closure 層抽象為 `structural_profile_aluminum_medium`。這個 item 名稱保留 functional purpose、material、scale、geometry form。

但如果該擠型承擔 T-slot module interface、精密導軌基準、密封框、抗扭截面或校準基準，就不應直接無條件合併。

### Brackets and Mounting Plates

多種簡單支架與 mounting plate 通常適合合併為 `mounting_bracket_aluminum_small`、`mounting_bracket_steel_small` 或 `mounting_plate_aluminum_small`。原本是 CNC、板金、鑄造或列印，不一定要形成不同 item，除非輸出規格不同。

### Vacuum、Gas Handling 與 Environment-Control Components

本輪中，vacuum-specific components 不自動從月球化 closure KB 中排除。先把它們當作一般 environment-control、gas/fluid handling、sealing 與 contamination-control evidence，等後續 review 再決定 abstraction。

### Electronics

terminal blocks、PLC modules、sensors、power supplies 通常不應被細分到 vendor SKU level。closure 層可先抽象成 control electronics、terminal block set、sensor suite 等，並標示 import 或 future-localization。
