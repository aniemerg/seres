---
row_identity:
  item: "2APK3"
  cad_file: "2APK3_left_right"
  source_row_number: 92
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Pair of thin left/right side plates in the reAM250 build-platform mount area, likely forming side walls or retainers around the 2APK build-platform/seal-guide subassembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APK3_left_right.step; research/ream250_bom/ream250_bom_row_0092_2APK3__views_2x2.png"
    cited_fact_or_basis: "BOM row 92 lists item 2APK3, quantity 2, CAD file 2APK3_left_right. Neighboring BOM rows name 2API_build_platform, 2APJ_inner_seal_guide, 2APK1_bottom, and 2APK2_front_back. Manifest row 92 maps this row to a matched part STEP. FreeCAD measured one solid with bounding box 4.00 x 46.00 x 76.00 mm, and the rendered contact sheet shows a thin rectangular side plate with four corner fastener holes and formed or relieved faces."
    evidence_basis: "bom_provided"
  assumptions:
    - "The name left_right means the same physical part is used on both left and right sides of the subassembly."
    - "The side-wall/retainer function is inferred from the row name, neighboring build-platform/seal-guide rows, and plate-like CAD geometry."
  uncertainty_notes:
    - "The CAD/BOM evidence does not expose mating constraints, so the exact interface with the bottom/front/back plates and seal guide remains unresolved."
mass:
  value_kg: 0.106
  basis: "Per-unit planning estimate for one 2APK3 plate; BOM quantity is 2, so row total is about 0.212 kg. FreeCAD volume is 13501.051 mm^3, equal to 1.3501051e-5 m^3. Using the local generic steel density constant of 7850 kg/m^3 gives 0.10598 kg, rounded to 0.106 kg. If the same CAD volume were aluminum at 2700 kg/m^3, one plate would be about 0.0365 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APK3_left_right.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 13501.051 mm^3, area 7858.637 mm^2, and bounding box 4.00 x 46.00 x 76.00 mm. kb/materials/properties.yaml lists steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. targeted_web_search: tried '\"2APK3_left_right\"', '\"2APK3\" \"reAM250\"', and '\"2APK3\" \"left_right\" CAD'; results found duplicate BOM text but no row-specific catalog mass or material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The supplied STEP solid volume is treated as the finished physical volume for one plate."
    - "A steel-like density is used as the conservative single-value planning estimate for this small structural plate because no row-specific material is provided."
  uncertainty_notes:
    - "Actual mass could be closer to 0.0365 kg per plate if this side piece is aluminum rather than steel; no catalog weight or material-specific STEP metadata resolves the material-dependent range."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0092_2APK3__views_2x2.png"
    cited_fact_or_basis: "BOM row 92 gives no manufacturer, product ID, material hint, or link URL. Assembly STEP material extraction for product 2APK3_left_right returned material 'Generic' with density 1000.0, which is placeholder metadata. CAD preview shows a rigid thin plate with fastener holes. targeted_web_search: tried '\"2APK3_left_right\"', '\"2APK3\" \"reAM250\"', and '\"2APK3\" \"left_right\" CAD'; no row-specific usable material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The thin rigid plate geometry and build-platform mount context indicate a metal plate rather than a polymer seal, felt element, sensor, or consumable."
  uncertainty_notes:
    - "Material family is broad only; downstream KB modeling should not choose a specific alloy or grade without a drawing, designer note, or better assembly metadata."
how_to_make:
  summary: "Fabricate as a small custom side plate from sheet or plate stock, then deburr, drill or finish the fastener holes, and inspect fit in the build-platform mount/seal-guide subassembly."
  manufacturing_steps:
    - "Cut a 4 mm thick metal blank to the 46 x 76 mm side-plate profile from sheet or plate stock."
    - "Machine, punch, laser-cut, or waterjet the four corner mounting holes and outside profile."
    - "Form or machine the visible relieved/faceted faces if they are functional rather than cosmetic CAD simplification."
    - "Deburr edges and holes, clean the part, and verify fit against the 2APK bottom/front/back pieces and neighboring seal-guide/build-platform parts."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APK3_left_right.step; research/ream250_bom/ream250_bom_row_0092_2APK3__views_2x2.png"
    cited_fact_or_basis: "CAD preview shows a one-piece thin plate with four fastener holes; FreeCAD reports one solid and a 4.00 x 46.00 x 76.00 mm bounding box. targeted_web_search: tried '\"2APK3_left_right\"', '\"2APK3\" \"reAM250\"', and '\"2APK3\" \"left_right\" CAD'; no row-specific manufacturing drawing, vendor route, or material specification was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Sheet/plate cutting plus hole finishing is the most plausible route for a small one-piece custom plate with the observed geometry."
    - "Any local self-manufacturing process would need the surrounding assembly or drawing to set hole tolerances and surface finish."
  uncertainty_notes:
    - "The CAD preview is enough for manufacturing-route triage but not for bend radius, hole tolerance, surface finish, or whether the faceted faces are exact production geometry."
kb_implications:
  - "item_granularity: simple_part - Model later as one reusable custom metal side plate used twice in the build-platform mount/seal-guide area, not as a purchased module."
---

Research result for the leased reAM250 BOM row only.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0092_2APK3.md
source_research_sha256: "4e767039b421cf0d1f88c857fa68b278d4595ecce1792c370a4d2223e873b9af"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed build-platform side-plate function, conservative steel-density mass basis with quantity 2, unresolved metal material evidence, sheet/plate cutting route, and preview showing a thin holed plate."
decomposition:
  decision: simple_part
  rationale: "The row is a one-piece side plate used twice; bottom, front/back, seal-guide, and build-platform neighbors remain separate rows."
  proposed_subparts: []
process_abstraction:
  original_process_family: sheet_plate_cutting_with_hole_finishing
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
    - stock_preparation
    - cutting
    - drilling
    - precision_machining
    - deburring
    - cleaning
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: sheet_metal_cutting_v0
      fit: partial
      reason: "Covers cutting the small side-plate outline from 4 mm metal sheet stock."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Covers producing the four fastener holes if not cut in the same operation."
    - process_id: machining_finish_basic_v0
      fit: supporting
      reason: "Relevant for local relieved faces and hole finishing after rough cutting."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers hole location, thickness, and fit checks against the build-platform mount stack."
  abstraction_decision: keep_original_family
  rationale: "The source route is already small sheet/plate fabrication with holes and local finishing, matching the canonical sheet/plate bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: side retention and location support in a build-platform mount subassembly
  material: unresolved_metal
  scale_or_capacity:
    mass_kg: 0.106
    bom_quantity: 2
    row_total_mass_kg: 0.212
    scale_class: small
  geometry_form: thin_rectangular_side_plate_with_four_corner_holes
merge_pool:
  eligible: true
  functional_purpose_key: subassembly_retention
  precision_guardrails:
    - hole_pattern
    - mating_fit
    - side_alignment
    - sealing_interface_if_applicable
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Material is unresolved; steel and aluminum alternatives materially change mass and local supply path."
    - "Fit against nearby seal-guide and platform parts may impose tighter hole-location tolerances."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups similar side retainers and resolves metal family."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; candidate for a reusable small side-retainer plate closure item if function and hole-pattern guardrails converge."
assumptions:
  - "The left/right name is treated as two instances of the same physical closure item."
  - "Steel-density mass is retained as a conservative planning value, while material identity remains unresolved metal."
unresolved:
  - "Exact material, alloy, surface finish, hole tolerance, and mating constraints are not specified."
  - "The functional importance of the relieved faces is unknown."
```
