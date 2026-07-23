---
row_identity:
  item: "2AO2"
  cad_file: "2AO2_guidance"
  source_row_number: 69
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Open rectangular guidance housing in the build-platform guidance area, likely acting as a guide/shroud around the moving build-platform mount stack rather than as a calibrated vendor module."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0069_2AO2__views_2x2.png"
    cited_fact_or_basis: "BOM row 69 identifies item 2AO2 as CAD file 2AO2_guidance with quantity 1; the assembly STEP product list places it under 2AO0_build_platform_guidance near 2AO1_flange and 2AP0_build_platform_mount; the rendered CAD preview shows an open-top rectangular guide-like shell."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD filename term guidance and parent assembly context are interpreted as the functional role."
  uncertainty_notes:
    - "No mating-position analysis was performed, so the exact guided component or clearance function remains unresolved."
mass:
  value_kg: 10.6
  basis: "FreeCAD measured one solid with volume 1346447.193 mm^3 and bounding box 264.00 x 264.00 x 328.00 mm. Using generic steel density 7850 kg/m^3 from kb/materials/properties.yaml gives 0.001346447 m^3 * 7850 = 10.57 kg, rounded to 10.6 kg per unit. BOM quantity is 1, so row total is also about 10.6 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AO2_guidance.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured volume 1346447.193 mm^3 from the row STEP; local density table lists generic steel at 7850 kg/m^3. targeted_web_search: queries tried were \"2AO2_guidance reAM250\", \"2AO0_build_platform_guidance\", \"2AO2 guidance reAM250\", and \"2AO2_guidance material\"; results only duplicated the BOM row and did not provide row-specific material or mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The single CAD solid volume is treated as the per-unit physical volume for this BOM row."
    - "Generic steel is used as the planning-density assumption because the part is a large structural guide adjacent to the build-platform/heating-plate assembly; if it is aluminum instead, the same CAD volume would imply about 3.6 kg."
  uncertainty_notes:
    - "The STEP material extractor returned only Generic with density 1000.0, so material is not resolved; mass may vary by roughly a factor of three if the part is aluminum rather than steel."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AO2_guidance.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The row STEP geometry is a thin-walled rectangular structural guide; assembly material extraction for product 2AO2_guidance returned only Generic with density 1000.0. targeted_web_search: queries tried were \"2AO2_guidance reAM250\", \"2AO0_build_platform_guidance\", \"2AO2 guidance reAM250\", and \"2AO2_guidance material\"; results only duplicated the BOM row and did not provide row-specific material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A metal construction is inferred from the machine context, size, and structural guide role."
  uncertainty_notes:
    - "No source states a grade or family; downstream KB work should keep this broad until a drawing, CAD material assignment, or physical BOM note is found."
how_to_make:
  summary: "Fabricate locally as a simple structural guide shell from cut and bent/welded sheet or plate stock, then deburr and inspect the rectangular profile and mating clearances."
  manufacturing_steps:
    - "Cut four side panels or a foldable sheet blank to the CAD envelope."
    - "Bend or fixture the walls into the rectangular guide shape."
    - "Weld or fasten the corner seams if the design is not made from one bent blank."
    - "Deburr, finish, and inspect squareness, height, and fit against the build-platform guidance assembly."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0069_2AO2__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AO2_guidance.step"
    cited_fact_or_basis: "CAD preview and measured bounding box show a simple open rectangular shell without visible precision bearing features. targeted_web_search: queries tried were \"2AO2_guidance manufacturing\", \"2AO0_build_platform_guidance\", and \"2AO2_guidance material\" results did not provide a row-specific manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The shell can be represented as sheet/plate fabrication for KB planning rather than as a vendor module."
  uncertainty_notes:
    - "The CAD preview does not prove whether the production part was bent sheet, welded plate, machined from billet, or additively manufactured."
kb_implications:
  - "item_granularity: simple_part - Treat as one reusable structural guide/shell part with uncertain metal material, not as a purchased module or multi-part assembly."
---

Research result for reAM250 BOM row 69.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0069_2AO2.md
source_research_sha256: ff1ccad7fe472f24ea89993e4d7721c9e5b02bba79e5ee1e22130cedfead9409
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Reviewed the build-platform guidance function, steel-basis CAD mass, unresolved metal evidence, sheet/plate shell
    fabrication route, KB implication, and CAD preview showing an open rectangular guide shell.
decomposition:
  decision: simple_part
  rationale: The row is one large thin-walled guide shell with no vendor module, moving mechanism, bearing set, and control
    subsystem to expose during row conversion.
  proposed_subparts: []
process_abstraction:
  original_process_family: sheet_plate_fabrication
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
  - stock_preparation
  - cutting
  - forming
  - joining
  - deburring
  - surface_finishing
  - dimensional_inspection
  candidate_existing_processes:
  - process_id: sheet_metal_cutting_v0
    fit: direct
    reason: Covers cutting sheet and plate blanks for the rectangular guide walls.
  - process_id: sheet_metal_forming_v0
    fit: supporting
    reason: Relevant if the shell is made from bent sheet instead of separate plates.
  - process_id: welding_and_fabrication_v0
    fit: supporting
    reason: Relevant if the corners need welded seams after cutting and forming.
  - process_id: finishing_deburring_v0
    fit: supporting
    reason: Covers edge cleanup before the guide is installed around moving hardware.
  - process_id: inspection_basic_v0
    fit: supporting
    reason: Covers checks for squareness, height, and fit against the build-platform guidance stack.
  abstraction_decision: keep_original_family
  rationale: The original route is sheet/plate cutting, bending, possible seam joining, and inspection. The shared sheet/plate
    bucket captures the primary closure work without inventing a dedicated guide-shell process.
  process_guardrails:
    tolerance: review squareness, height, wall spacing, and clearance around the guided build-platform hardware
    surface_finish: deburr and smooth edges that could contact nearby moving parts
    sealing_quality: not_applicable
    alignment_accuracy: shell geometry should preserve guidance clearances, but no precision bearing interface is visible
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: guide and shroud the build-platform mount stack with an open rectangular shell
  material: unknown_metal_alloy
  scale_or_capacity:
    mass_kg: 10.6
    bom_quantity: 1
    row_total_mass_kg: 10.6
    scale_class: large
  geometry_form: open_rectangular_sheet_plate_guide_shell
merge_pool:
  eligible: true
  functional_purpose_key: structural_guidance_shell
  precision_guardrails:
  - squareness
  - wall_spacing
  - moving_clearance
  - seam_integrity
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - sheet_plate_cutting_drilling
  import_risk_factors:
  - Exact metal family is unresolved; steel and aluminum assumptions change mass substantially.
  - Production construction method is inferred from CAD shape and could involve bent sheet, welded plate, machined stock,
    and additive fabrication.
  post_merge_decision_notes: Final import/local decision is deferred until merge review compares this with other guide shells,
    enclosure-like barriers, and build-platform structural members.
kb_staging:
  proposed_item_id: null
  notes: Leave final item ID open for merge review; this may converge with other large structural guidance shells if geometry,
    material, and clearance guardrails are compatible.
assumptions:
- The CAD solid is the complete per-unit shell and not a hidden multi-part vendor module.
- Generic steel is used only for planning mass; material identity remains broad pending drawings.
- Sheet/plate fabrication is a conservative closure abstraction for a thin-walled open guide shell.
unresolved:
- Exact metal grade, production route, wall thickness strategy, and surface treatment are unknown.
- The guided component, clearance envelope, and fit tolerance are not resolved by the row evidence.
```
