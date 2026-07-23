---
row_identity:
  item: "2AC4"
  cad_file: "2AC4_part_4"
  source_row_number: 38
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Loose spherical rolling element for the bottom axis bearing stack; it provides point rolling contact between bearing races or seats so the bottom axis can rotate with lower friction."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC4_part_4.step; research/ream250_bom/ream250_bom_row_0038_2AC4__views_2x2.png"
    cited_fact_or_basis: "BOM row 38 names item 2AC4 / 2AC4_part_4 as 'axis bearing bottom'; FreeCAD measured one solid with a 5.40 mm by 5.40 mm by 5.40 mm bounding box, and the rendered contact sheet shows a smooth sphere."
    evidence_basis: "bom_provided"
  assumptions:
    - "The repeated neighboring 2AC rows with the same 'axis bearing bottom' description are separate rolling elements in the same bottom bearing assembly."
  uncertainty_notes: []
mass:
  value_kg: 0.000647
  basis: "Per-unit mass for one 5.4 mm diameter sphere. FreeCAD measured volume 82.448 mm^3; using the local generic steel density 7850 kg/m^3 gives 82.448e-9 m^3 * 7850 kg/m^3 = 0.000647 kg, about 0.647 g. BOM quantity is 1, so the row total is also about 0.000647 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC4_part_4.step; kb/materials/properties.yaml; https://www.redhillballs.com/product/bearing-steel-balls/bearing-chrome-steel-balls/"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 82.448 mm^3. The local material table gives generic steel density as 7850 kg/m^3. The independent bearing-ball vendor page describes chrome steel bearing balls as AISI 52100 high-carbon chromium alloy steel used for precision bearings."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD solid represents one physical bearing ball and has no hidden internal voids."
    - "Generic steel density is a close calculation constant for chrome bearing steel at this modeling precision."
  uncertainty_notes:
    - "The row STEP material metadata is only 'Generic' with density 1000 kg/m^3, so the steel material used for mass is independently inferred from bearing-ball practice rather than supplied by the BOM package."
material:
  primary_material: "chrome bearing steel / high-carbon chromium bearing steel"
  source:
    url_or_path: "https://www.redhillballs.com/product/bearing-steel-balls/bearing-chrome-steel-balls/"
    cited_fact_or_basis: "Targeted search for '5.4 mm bearing ball material chrome steel' found an independent bearing-ball supplier describing bearing chrome steel balls as AISI 52100 high-carbon chromium alloy steel for precision bearing applications."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's spherical CAD geometry and 'axis bearing bottom' BOM description identify this as a loose bearing ball, so common bearing-ball material practice is applicable."
  uncertainty_notes:
    - "No row-specific non-placeholder STEP material or BOM vendor link resolves the exact grade; stainless or ceramic bearing balls are possible alternatives, but the BOM package gives no evidence for those variants."
how_to_make:
  summary: "Treat as a standard precision loose bearing ball: a Manufacturing route would form a steel blank, harden it, then grind, lap, polish, and inspect to bearing-ball roundness and surface-finish requirements"
  manufacturing_steps:
    - "Start from bearing-steel wire or rod sized for a roughly 5.4 mm ball blank."
    - "Cold-head or cut and upset the blank into a near-spherical ball, then remove flash."
    - "Through-harden and temper the ball for bearing service."
    - "Rough grind, lap, polish, clean, and grade-sort for diameter, roundness, and surface finish."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC4_part_4.step; https://hartfordtechnologies.com/precision-balls/chrome-steel-balls/"
    cited_fact_or_basis: "The row CAD is a smooth 5.4 mm sphere. The independent precision-ball supplier page describes chrome steel as bearing-grade alloy steel with high hardness, wear resistance, through-hardening, and precision surface characteristics. targeted_web_search: tried '5.4 mm bearing ball material chrome steel' and 'bearing balls chrome steel material 5.4 mm'; results found general bearing-ball material/spec pages but no row-specific manufacturing process for 2AC4."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Detailed forming, grinding, lapping, and inspection steps are inferred from common precision-ball manufacturing practice, because the BOM and supplier pages identify the item class but do not specify the actual production route for this row."
  uncertainty_notes:
    - "Manufacturing requires precision finishing and metrology capability"
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable loose precision bearing ball or small bearing-ball part, not as raw stock or a purchased functional module."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0038_2AC4.md
source_research_sha256: e3dce70f34f62088c587cb908ba8166bf1672bbe74678b7dd65056036c62cc63
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Reviewed the source function, 5.4 mm spherical CAD/image evidence, steel mass estimate, bearing-steel material inference,
    precision-ball manufacturing route, and KB implication before conversion.
decomposition:
  decision: simple_part
  rationale: The item is one loose spherical rolling element with no separable subparts and module-level internal dependencies.
    Its closure difficulty comes from precision bearing-ball manufacture, not part decomposition.
  proposed_subparts: []
process_abstraction:
  original_process_family: precision_bearing_ball_forming_heat_treating_grinding_lapping_polishing_inspection
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
  - decomposition_required
  - import_assumption
  - precision_machining
  - grinding_lapping
  - heat_treatment
  - dimensional_inspection
  - calibration
  candidate_existing_processes:
  - process_id: assembly_basic_v0
    fit: poor_fit
    reason: Only covers generic assembly; internal precision manufacturing needs decomposition.
  - process_id: inspection_basic_v0
    fit: supporting
    reason: Covers basic checks while detailed metrology remains unresolved.
  - process_id: calibration_and_test_basic_v0
    fit: supporting
    reason: Covers generic calibration and test after decomposition defines the item.
  - process_id: precision_grinding_basic_v0
    fit: supporting
    reason: Relevant when rolling, sliding, and raceway surfaces need precision finishing.
  abstraction_decision: substitute_process_family
  rationale: The original route requires bearing-steel forming, through-hardening, precision grinding/lapping, polishing,
    cleaning, and grade sorting. Ordinary additive, sheet, profile, and general subtractive buckets do not preserve the required
    roundness, hardness, and surface finish, so this row should enter the precision component bucket until a local precision-ball
    process is explicitly modeled.
  process_guardrails:
    tolerance: required
    surface_finish: required
    sealing_quality: not_applicable
    alignment_accuracy: required
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: Provide low-friction point rolling contact between bearing races and seats in a rotating axis bearing
    stack.
  material: chrome_bearing_steel
  scale_or_capacity:
    mass_kg: 0.000647
    bom_quantity: 1
    row_total_mass_kg: 0.000647
    nominal_diameter_mm: 5.4
    scale_class: tiny
  geometry_form: precision_sphere
merge_pool:
  eligible: true
  functional_purpose_key: rolling_contact
  precision_guardrails:
  - roundness
  - diameter_tolerance
  - surface_finish
  - hardness
  - wear_resistance
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - precision_component_import_decompose_later
  import_risk_factors:
  - Bearing-grade roundness, surface finish, hardness, and metrology requirements are likely outside generic lunar metalworking
    buckets.
  - Exact material grade is inferred from bearing-ball practice rather than row-specific material metadata.
  - Multiple neighboring axis-bearing rows may need consolidation before deciding the condition that to model loose balls
    and an assembled bearing set.
  post_merge_decision_notes: Final import/local decision is deferred until merge review groups this with other rolling elements
    and bearing-stack rows.
kb_staging:
  proposed_item_id: null
  notes: Wait for merge review; likely merge candidate with other small loose bearing balls and a reusable precision rolling-element
    class.
assumptions:
- The row represents one loose bearing ball rather than a complete bearing assembly.
- Chrome bearing steel is the best closure material assumption from geometry and bearing-ball practice despite absent row-specific
  material metadata.
- The 5.4 mm diameter is scale evidence for merge review, not part of the functional merge key.
unresolved:
- Determine the condition that neighboring 2AC rows are identical rolling elements that should merge into one bearing-ball
  closure item with aggregated quantity.
- Decide later the condition that the KB should model loose bearing balls separately and abstract them into a bearing set
  for this axis stack.
- Confirm the condition that local precision-ball manufacture is in scope and this remains an import during KB staging.
```
