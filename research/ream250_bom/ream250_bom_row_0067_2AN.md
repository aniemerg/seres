---
row_identity:
  item: "2AN"
  cad_file: "2AN_motor_mount"
  source_row_number: 67
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom motor-mount bracket or adapter plate in the 2A motion/mechanical group, providing a circular motor/gearbox clearance or register opening plus four small mounting holes for fastening and alignment."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AN_motor_mount.step; research/ream250_bom/ream250_bom_row_0067_2AN__views_2x2.png"
    cited_fact_or_basis: "BOM row 67 lists item 2AN, quantity 1, CAD file 2AN_motor_mount. Manifest row 67 maps it to gold_export/parts/2AN_motor_mount.step as a matched_existing part. FreeCAD measured one solid with a 27.00 x 67.00 x 86.00 mm bounding box; the rendered contact sheet shows a rectangular mount with a large circular central opening and four small corner-region holes. Neighboring rows 63-66 identify the adjacent gearbox, motor, and coupling parts."
    evidence_basis: "bom_provided"
  assumptions:
    - "The 'motor_mount' CAD name and neighboring motor/gearbox/coupling rows are interpreted as the installed functional context."
    - "The large circular opening is interpreted as motor/shaft/coupling clearance or a locating register, and the four small holes as mounting or fastening features."
  uncertainty_notes:
    - "The per-part STEP does not include the mating motor, gearbox, fasteners, or assembly constraints, so exact installed orientation and load path remain inferred from row context and visible geometry."
mass:
  value_kg: 0.915
  basis: "FreeCAD volume 116550.846 mm^3 = 1.16550846e-4 m^3. Using the local generic steel density of 7850 kg/m^3 gives 0.9149 kg, rounded to 0.915 kg per motor mount. BOM quantity is 1, so the row total is also about 0.915 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AN_motor_mount.step; kb/materials/properties.yaml; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 116550.846 mm^3, surface area 23470.452 mm^2, and bounding box 27.00 x 67.00 x 86.00 mm. The local density table lists steel at 7850 kg/m^3 and aluminum at 2700 kg/m^3. targeted_web_search: searched \"2AN_motor_mount reAM250\", \"2AN motor_mount reAM250\", \"reAM250 2AN_motor_mount material\", and \"2AN_motor_mount motor mount material\"; results found duplicate BOM text but no row-specific material or catalog mass source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is treated as the physical material volume for one 2AN motor mount."
    - "Generic steel is used as the planning density because the part is a compact structural motor mount with fastener features in a machine motion group, and no row-specific material source was available."
  uncertainty_notes:
    - "Material is not directly specified; if the part is aluminum, the same CAD volume would imply about 0.315 kg using the local aluminum density."
    - "The estimate excludes separate screws, dowels, motor hardware, or coupling parts represented by neighboring BOM rows."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; web targeted search"
    cited_fact_or_basis: "BOM row 67 identifies the part only as 2AN_motor_mount and provides no material, manufacturer, product ID, or link URL. Local assembly STEP material extraction for product 2AN_motor_mount returned only placeholder material 'Generic' with density 1000.0. targeted_web_search: searched \"2AN_motor_mount reAM250 material\", \"2AN motor mount reAM250 material\", \"reAM250 2AN_motor_mount\", and \"2AN_motor_mount\"; found duplicate BOM listings but no row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is modeled as metal structural hardware because the CAD shows a rigid one-piece motor mount with a central register/clearance hole and small fastener holes."
  uncertainty_notes:
    - "The evidence supports only a broad metal/alloy family; exact grade, heat treatment, coating, and whether steel or aluminum is used remain unresolved."
how_to_make:
  summary: "Fabricate as a custom machined metal motor-mount bracket from plate or billet stock, then deburr and inspect mounting geometry."
  manufacturing_steps:
    - "Cut a metal plate or billet blank large enough for the 27.00 x 67.00 x 86.00 mm envelope."
    - "CNC mill the rectangular outer profile, the diagonal/lightened face geometry if functionally required, and flat mounting/reference faces."
    - "Bore or interpolate the large circular central opening and drill, ream, tap, countersink, or counterbore the four small mounting holes as required by the mating motor/gearbox hardware."
    - "Deburr, clean, apply any required protective finish, and inspect hole spacing, face flatness, and motor/shaft clearance before assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AN_motor_mount.step; research/ream250_bom/ream250_bom_row_0067_2AN__views_2x2.png; web targeted search"
    cited_fact_or_basis: "The STEP is one solid with a 27.00 x 67.00 x 86.00 mm bounding box. The rendered contact sheet shows a one-piece rectangular motor mount with a large central circular opening, four small holes, and planar/ribbed faces. targeted_web_search: searched \"2AN_motor_mount reAM250 manufacturing\", \"2AN motor mount drawing reAM250\", \"reAM250 2AN_motor_mount\", and \"2AN_motor_mount\" results found duplicate BOM text but no row-specific fabrication drawing or process specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Subtractive machining is chosen because the row is a one-piece prismatic bracket with accurate-looking motor register/clearance and fastener features."
    - "Plate or billet stock is assumed over casting because this is a low-count custom machine part and no casting or vendor route is identified."
  uncertainty_notes:
    - "A full drawing could add tolerance, thread, surface-finish, coating, or datum requirements not visible in the simplified STEP/contact-sheet evidence."
kb_implications:
  - "item_granularity: simple_part - Model as one reusable custom machined metal motor-mount bracket; keep the motor, gearbox, coupling, and fasteners as separate BOM items."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0067_2AN.md
source_research_sha256: "583455d87e2a4adc6102bc3bbbcbe2f78a2445223aabfccfc0869075a3587374"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the motor-mount function, CAD-derived steel-assumption mass, unresolved metal material evidence, machining route, and central-register geometry before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one custom mount body; motor, gearbox, coupling, fasteners, dowels, and adjacent motion components are separate BOM rows."
  proposed_subparts: []
process_abstraction:
  original_process_family: machined_metal_motor_mount
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - drilling
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers machining the mount body from metal stock."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant to central register geometry, face flatness, and motor/shaft alignment."
    - process_id: drilling_basic_v0
      fit: supporting
      reason: "Covers the four mounting-hole features before any final reaming, tapping, countersinking, and counterboring."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers hole spacing, face flatness, and clearance checks before assembly."
  abstraction_decision: keep_original_family
  rationale: "The source route is a custom machined metal mount, and the central opening plus fastener pattern make subtractive machining the clearest closure handle."
  process_guardrails:
    tolerance: high
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: high
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: motor and gearbox mounting interface for motion assembly
  material: structural_metal_unknown_steel_assumed_for_mass
  scale_or_capacity:
    mass_kg: 0.915
    bom_quantity: 1
    row_total_mass_kg: 0.915
    scale_class: small
  geometry_form: compact_machined_mount_with_large_circular_register_and_four_holes
merge_pool:
  eligible: true
  functional_purpose_key: motor_mounting
  precision_guardrails:
    - material_family
    - register_diameter
    - hole_spacing
    - face_flatness
    - shaft_alignment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Material uncertainty changes mass and stiffness."
    - "Motor and gearbox alignment may require precision machining and inspection."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review; compare with other motor mount and adapter rows before assigning closure identity."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review before deciding whether this can share a generic motor mounting interface item."
assumptions:
  - "The large circular feature is a motor/shaft clearance feature and locating register."
  - "Steel density is a conservative planning assumption until material evidence improves."
  - "Fasteners and dowels are not included in this row."
unresolved:
  - "Exact material, hole callouts, thread state, datum scheme, and surface finish are not specified."
  - "Mating motor and gearbox alignment requirements need review with neighboring motion rows."
```
