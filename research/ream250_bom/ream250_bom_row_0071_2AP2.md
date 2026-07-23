---
row_identity:
  item: "2AP2"
  cad_file: "2AP2_assembly_plate"
  source_row_number: 71
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin square frame-like assembly plate in the 2AP0 build platform mount, apparently serving as an intermediate mounting, spacing, or retaining plate around the central build-platform/heating-plate stack."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP2_assembly_plate.step; research/ream250_bom/ream250_bom_row_0071_2AP2__views_2x2.png"
    cited_fact_or_basis: "BOM row 71 identifies item 2AP2, quantity 1, CAD file 2AP2_assembly_plate. The manifest maps it to one matched_existing part STEP. The assembly STEP places it under product 2AP0_build_platform_mount next to 2AP1_spring_plate, 2AP3_heating_plate, spring blocks, seals, pressing plate, and 2API_build_platform. FreeCAD measured one solid with bounding box 252.00 x 252.00 x 2.00 mm; the rendered contact sheet shows a thin square frame/plate with a central square opening and four small corner holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file represents the single physical item for this BOM row."
    - "The term assembly_plate and its position in the 2AP0_build_platform_mount subassembly are interpreted as a mounting/spacing/retaining role rather than as the heated or build-contact surface itself."
  uncertainty_notes:
    - "The BOM and assembly labels do not state the exact mating faces or whether this plate primarily spaces, clamps, locates, or shields neighboring build-platform components."
mass:
  value_kg: 0.677
  basis: "Per-unit planning estimate for quantity 1. FreeCAD volume is 86277.858 mm^3, equal to 8.6277858e-5 m^3. Using the local generic steel density constant of 7850 kg/m^3 gives 0.677 kg; if the same CAD volume were aluminum at 2700 kg/m^3, it would be about 0.233 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP2_assembly_plate.step; kb/materials/properties.yaml; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 86277.858 mm^3, area 89978.358 mm^2, and bounding box 252.00 x 252.00 x 2.00 mm. kb/materials/properties.yaml lists steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. Assembly STEP material extraction for product 2AP2_assembly_plate returned only placeholder material 'Generic' with density 1000.0. targeted_web_search: tried '2AP2_assembly_plate reAM250 material', '2AP2 assembly plate reAM250', 'reAM250 2AP2 assembly_plate', and 'reAM250 assembly plate material'; results duplicated the BOM identity or general reAM250 context and did not provide row-specific material or mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A steel-like density is used as the conservative single-value planning estimate because the part is a thin rigid build-platform-mount plate in a metal PBF machine and no row-specific material is provided."
  uncertainty_notes:
    - "Actual mass could be closer to 0.233 kg if the plate is aluminum; no catalog weight, drawing material, or non-placeholder STEP material metadata resolves the steel-versus-aluminum range."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0071_2AP2__views_2x2.png"
    cited_fact_or_basis: "BOM row 71 gives no manufacturer, product ID, material hint, or link URL. Assembly STEP material extraction for product 2AP2_assembly_plate returned material 'Generic' with density 1000.0, which is placeholder metadata. The CAD preview shows a thin rigid plate/frame in the build-platform-mount stack. targeted_web_search: tried '2AP2_assembly_plate reAM250 material', '2AP2 assembly plate reAM250', 'reAM250 2AP2 assembly_plate', and 'reAM250 assembly plate material'; no row-specific usable material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The plate is modeled as a metal/alloy part because the geometry is a thin structural frame in the build-platform/heating-plate area, not a seal, cable, sensor, or polymer consumable."
  uncertainty_notes:
    - "Material family is intentionally broad; downstream KB modeling should not select steel, stainless, or aluminum grade-specific process routes without a drawing, supplier note, or direct design source."
how_to_make:
  summary: "Fabricate as a thin one-piece metal plate/frame from sheet or plate stock"
  manufacturing_steps:
    - "Cut a 2 mm metal sheet or plate blank to the 252 mm square outside profile and central square opening."
    - "Machine, laser-cut, waterjet-cut, or punch the four small corner holes and frame profile."
    - "Deburr all cut edges and hole edges."
    - "Flatten or lightly finish the plate as needed for stack-up fit against the spring/heating/build-platform mount components."
    - "Clean and inspect hole location, outer dimensions, central opening, and flatness before assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP2_assembly_plate.step; research/ream250_bom/ream250_bom_row_0071_2AP2__views_2x2.png"
    cited_fact_or_basis: "FreeCAD measured a 252.00 x 252.00 x 2.00 mm one-solid plate/frame, and the contact sheet shows a flat square frame with central opening and corner holes. targeted_web_search: tried '2AP2_assembly_plate manufacturing reAM250', '2AP2 assembly plate reAM250 material', 'reAM250 build platform mount assembly plate', and 'reAM250 2AP2 assembly_plate'; no source stated the manufacturing route for this row."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Sheet/plate cutting is the most plausible Manufacturing route for a flat 2 mm one-piece frame with through features."
    - "The CAD preview is used for route triage only; exact cutting tolerances and finish are not available."
  uncertainty_notes:
    - "The row evidence does not specify whether the actual part was laser cut, waterjet cut, machined from plate, stamped, or otherwise produced."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable one-piece custom metal plate/frame in the build-platform-mount stack, with material left broad until a design source resolves the alloy."
---

Research result for the leased reAM250 BOM row only.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0071_2AP2.md
source_research_sha256: 4d6845c35bdd1302feaa2608bfad8d5301997899d608d0831589b9e67164c598
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Reviewed the build-platform mount stack function, steel-basis CAD mass, unresolved metal material evidence, sheet/plate
    cutting route, KB implication, and preview showing a thin square frame plate with central opening and corner holes.
decomposition:
  decision: simple_part
  rationale: The row is one flat plate/frame with through features and no hidden module, sensor, actuator, and assembled
    mechanism to expose during row conversion.
  proposed_subparts: []
process_abstraction:
  original_process_family: sheet_plate_cutting_drilling
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
  - stock_preparation
  - cutting
  - drilling
  - deburring
  - surface_finishing
  - cleaning
  - dimensional_inspection
  candidate_existing_processes:
  - process_id: sheet_metal_cutting_v0
    fit: direct
    reason: Covers cutting the flat outside profile and central opening from thin sheet/plate stock.
  - process_id: drilling_basic_v0
    fit: supporting
    reason: Covers the corner hole pattern if not made during the primary cutting pass.
  - process_id: finishing_deburring_v0
    fit: supporting
    reason: Covers edge cleanup on the central opening, outside profile, and holes.
  - process_id: surface_finishing_v0
    fit: supporting
    reason: Relevant if the build-platform stack needs light finishing after cutting.
  - process_id: inspection_basic_v0
    fit: supporting
    reason: Covers checks of flatness, hole location, outer size, and central opening geometry.
  abstraction_decision: keep_original_family
  rationale: The original route is flat sheet/plate cutting, hole making, deburring, and inspection. The sheet/plate cutting
    bucket directly captures the closure path for this thin frame plate.
  process_guardrails:
    tolerance: review hole pattern, central opening, outer dimensions, and stack-up fit
    surface_finish: deburr and lightly finish edges that contact the spring, heating, and build-platform mount stack
    sealing_quality: not_applicable
    alignment_accuracy: flatness and hole locations affect stack alignment
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: provide a mounting, spacing, and retaining plate in the build-platform mount stack
  material: unknown_metal_alloy
  scale_or_capacity:
    mass_kg: 0.677
    bom_quantity: 1
    row_total_mass_kg: 0.677
    scale_class: medium
  geometry_form: thin_square_frame_plate_with_central_opening_and_corner_holes
merge_pool:
  eligible: true
  functional_purpose_key: mounting_spacing
  precision_guardrails:
  - flatness
  - hole_pattern
  - central_opening_geometry
  - stack_up_fit
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - sheet_plate_cutting_drilling
  import_risk_factors:
  - Exact metal family is unresolved, and steel plus aluminum assumptions differ substantially in mass and thermal behavior.
  - Build-platform and heater-adjacent service may impose flatness, cleanliness, and thermal constraints beyond row evidence.
  post_merge_decision_notes: Final import/local decision is deferred until merge review compares this with other mounting,
    spacing, retaining, and frame-like plates in the build-platform stack.
kb_staging:
  proposed_item_id: null
  notes: Leave final item ID open for merge review; this may converge with other thin mounting and spacing plates if material,
    scale, and stack-up guardrails are compatible.
assumptions:
- The STEP solid is the complete per-unit row item, with fasteners and seals modeled in adjacent rows.
- Steel-equivalent mass is a conservative planning value, while material identity remains broad.
- Sheet/plate cutting is sufficient for closure abstraction unless later evidence requires precision grinding.
unresolved:
- Exact alloy, material grade, surface treatment, flatness requirement, and cutting process are unknown.
- The plate role within the stack could be spacing, retaining, locating, shielding, and clamping; source evidence does not
  distinguish these functions.
```
