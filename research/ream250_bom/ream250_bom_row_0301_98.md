---
row_identity:
  item: "98"
  cad_file: "98_plate"
  source_row_number: 301
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Large plain structural plate or panel used with the page-10 frame/profile group; BOM quantity is 4."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/98_plate.step; research/ream250_bom/ream250_bom_row_0301_98__views_2x2.png"
    cited_fact_or_basis: "BOM row 301 lists item 98, quantity 4, CAD file 98_plate. Neighboring page-10 BOM rows include Bosch Rexroth 60x60 strut profiles and bottom/top square-profile frame items. The manifest maps row 301 to gold_export/parts/98_plate.step as a matched existing part. FreeCAD measured one solid with a 900.00 x 10.00 x 960.00 mm bounding box, and the rendered preview shows a large flat rectangular plate."
    evidence_basis: "bom_provided"
  assumptions:
    - "The generic filename 98_plate and the adjacent frame-profile rows are interpreted as a structural frame plate or panel rather than a calibrated purchased module."
  uncertainty_notes:
    - "The CAD preview shows the plate envelope but no holes, slots, mounting faces, or explicit assembly mates, so the exact interface and placement in the frame remain unresolved."
mass:
  value_kg: 22.766
  basis: "FreeCAD volume 8432000.000 mm^3 = 0.008432 m^3. Using the local aluminum density of 2700 kg/m^3 gives 22.766 kg per plate. The BOM quantity is 4, so the row total under this assumption is about 91.1 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/98_plate.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; web targeted search"
    cited_fact_or_basis: "FreeCAD measured 1 solid, 8432000.000 mm^3 volume, 1723600.000 mm^2 area, and a 900.00 x 10.00 x 960.00 mm bounding box. The local assembly STEP material extractor matched 98_plate only to placeholder material Generic with density 1000.0. The local density table lists aluminum density_kg_per_m3: 2700. targeted_web_search: searched \"98_plate reAM250 material\", \"reAM250 98_plate material\", \"reAM250 900 960 10 plate\", and \"reAM250 98 4 98_plate\"; results found duplicate BOM listings but no row-specific mass, material callout, drawing, or vendor source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP volume is treated as the physical solid volume for one plate."
    - "Aluminum density is used as the planning estimate because this row is adjacent to Bosch Rexroth aluminum strut-profile frame rows and the plate is a very large 10 mm frame/panel component."
  uncertainty_notes:
    - "Material is not directly specified for row 98. If the plate is generic steel instead of aluminum, the same CAD volume would be about 66.2 kg per plate using the local steel density of 7850 kg/m^3."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; web targeted search"
    cited_fact_or_basis: "BOM row 301 provides no material family or grade for 98_plate. Local assembly STEP material extraction for 98_plate returned only placeholder material Generic with density 1000.0. targeted_web_search: searched \"98_plate reAM250 material\", \"reAM250 98_plate material\", \"reAM250 900 960 10 plate\", and \"reAM250 98 4 98_plate\"; results found duplicate BOM listings but no row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Treat as a structural metal plate for KB planning because the CAD is a 10 mm thick load-bearing-size plate in a machine-frame context."
    - "Aluminum is plausible from neighboring Bosch Rexroth frame-profile rows, but the result keeps the material family broad because no row-specific material evidence was found."
  uncertainty_notes:
    - "Do not use this result to distinguish aluminum tooling plate, carbon steel, stainless steel, or coated sheet/plate without a later drawing or material callout."
how_to_make:
  summary: "Make as a simple large metal plate from 10 mm stock: cut the rectangular blank to the CAD envelope, square and deburr the edges, finish surfaces as required, and install as a frame plate or panel."
  manufacturing_steps:
    - "Start from approximately 10 mm aluminum or steel plate stock large enough for a 900 x 960 mm finished envelope."
    - "Cut the rectangular blank by waterjet, laser, plasma, saw, or CNC router/mill workflow selected for the final material."
    - "Machine or finish the perimeter to the CAD dimensions if tighter squareness or fit-up is required."
    - "Deburr, clean, and apply any required surface finish or corrosion protection before frame assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/98_plate.step; research/ream250_bom/ream250_bom_row_0301_98__views_2x2.png; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid with a 900.00 x 10.00 x 960.00 mm bounding box. The rendered preview shows a plain flat rectangular plate with no visible holes, pockets, threads, or multi-part features. targeted_web_search: searched \"98_plate reAM250 material\", \"reAM250 98_plate material\", \"reAM250 900 960 10 plate\", and \"reAM250 98 4 98_plate\" found duplicate BOM listings but no row-specific fabrication drawing or manufacturing instructions."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Plate cutting and edge finishing are selected as the plausible route because the CAD is a simple prismatic 10 mm plate."
    - "No drilling or pocketing step is listed because no such features are visible in the supplied STEP preview."
  uncertainty_notes:
    - "The final attachment method is unresolved; downstream modeling should keep installation generic until the assembly drawing shows whether the plate is clamped, bolted, welded, or captured in profiles."
kb_implications:
  - "item_granularity: simple_part - model as one reusable large cut structural plate/panel, with BOM quantity carrying the count, rather than as four separate item definitions or a purchased module."
---

Research result for reAM250 BOM row 301.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0301_98.md
source_research_sha256: "8142feceb6dfc3e98fabfbabc5f89d23f76fd9943f192bee67ee3252fabd0b56"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the frame plate function, CAD-derived mass, unresolved material evidence, simple plate-cutting route, and plain rectangular CAD preview before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is four instances of one large plain plate geometry; no embedded hardware, electronics, seals, nor multi-part structure is present in the row evidence."
  proposed_subparts: []
process_abstraction:
  original_process_family: large_plate_cutting_and_edge_finishing
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
    - stock_preparation
    - cutting
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: sheet_metal_cutting_v0
      fit: direct
      reason: "Covers cutting sheet and plate stock into large rectangular blanks for panels and frame plates."
    - process_id: metal_cutting_basic_v0
      fit: supporting
      reason: "Covers saw-style stock cutting to length when the stock is treated as thick metal plate."
    - process_id: surface_finishing_v0
      fit: supporting
      reason: "Covers edge cleanup, surface conditioning, and fit-up finishing when required by assembly."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers checks of length, width, thickness, squareness, and flatness."
  abstraction_decision: keep_original_family
  rationale: "The source evidence already describes a plain large plate made from stock by cutting and edge finishing, which fits the selected sheet and plate cutting bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: structural plate and panel for machine frame group
  material: structural_metal_unknown_aluminum_assumed_for_mass
  scale_or_capacity:
    mass_kg: 22.766
    bom_quantity: 4
    row_total_mass_kg: 91.064
    scale_class: large
  geometry_form: large_plain_rectangular_plate_900x960x10mm
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - material_family
    - flatness
    - edge_squareness
    - attachment_method
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Material uncertainty is high; steel would roughly triple the per-unit mass compared with the aluminum planning estimate."
    - "Row total mass is significant, so material resolution can materially affect closure accounting."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review; this row should merge only after material family and attachment role are checked against related frame rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with other large structural plates and panels before assigning a closure item ID."
assumptions:
  - "The four BOM units share the same geometry and role."
  - "The plate is structural metal stock rather than a calibrated module."
  - "No hidden holes, pockets, inserts, nor coatings are modeled until stronger evidence appears."
unresolved:
  - "Material family remains unresolved; aluminum is only the mass-planning assumption."
  - "Final attachment method and frame location are not identified by the row evidence."
```
