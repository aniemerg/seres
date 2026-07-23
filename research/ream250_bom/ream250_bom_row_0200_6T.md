---
row_identity:
  item: "6T"
  cad_file: "6T_motor_Nema_23"
  source_row_number: 200
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.reichelt.de/de/de/schrittmotor-nema-23-1-8-1-0-a-6-5-v-nema23-05-p335326.html?PROVID=2789&msclkid=b4bbcdd3d6b414c32dd1ab210a71467d&utm_source=bing&utm_medium=cpc&utm_campaign=(DE%3A%20All%20Products)%20Marge%201-10&utm_term=4575755099603094&utm_content=Ad%20group%20%231&&r=1"
function:
  summary: "NEMA 23 bipolar stepper motor for driving a GT2 belt pulley in the reAM250 recoater motion assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.reichelt.com/de/en/shop/product/stepper_motor_nema_23_1_8_1_0_a_6_5_v_-335326; research/ream250_bom/ream250_bom_row_0200_6T__views_2x2.png"
    cited_fact_or_basis: "BOM row 200 identifies item 6T, quantity 1, cad_file 6T_motor_Nema_23, manufacturer reichelt elektronik, and row text linking it to 6U_belt_pulley_motor_GT2_Bore6p35_20. The manifest maps the same row to gold_export/parts/6T_motor_Nema_23.step as a matched_existing vendor_component with one CAD instance. Reichelt identifies product NEMA23-05 as a NEMA 23 bipolar stepper motor with 1.8 degree step angle, 132 Ncm holding torque, 6.35 mm shaft, and 1 A / 6.5 V rating. The rendered CAD contact sheet shows a square-frame motor body with a protruding shaft and lead/cable feature. official_alternate_route_check: the original BOM URL is a reichelt.de German route for product p335326; the cited reichelt.com/de/en page is Reichelt's English canonical/shop route for the same product number 335326 and row-matched product NEMA23-05."
    evidence_basis: "bom_provided"
  assumptions:
    - "The nearby BOM row text naming the GT2 bore-6.35 pulley is used as row-local context for the motor's drive role."
  uncertainty_notes:
    - "The BOM row does not state which recoater axis this motor drives, only that it is paired with the GT2 pulley motor context."
mass:
  value_kg: 1.082
  basis: "Use 1.082 kg per physical motor from the BOM-provided Reichelt product route. BOM quantity is 1, so the row total is also 1.082 kg. FreeCAD measured one CAD solid with volume about 220,718.436 mm3, surface area about 23,436.225 mm2, and bounding box about 56.40 x 73.20 x 96.60 mm; vendor mass supersedes a CAD-density estimate for this multi-material motor."
  source:
    url_or_path: "https://www.reichelt.com/de/en/shop/product/stepper_motor_nema_23_1_8_1_0_a_6_5_v_-335326; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6T_motor_Nema_23.step"
    cited_fact_or_basis: "Reichelt lists product NEMA23-05 / EAN 4250236821764 with manufacturer ID NEMA23-05 and weight 1.082 kg. FreeCAD measured the supplied row STEP as one solid, volume about 220,718.436 mm3, area about 23,436.225 mm2, and bounding box about 56.40 x 73.20 x 96.60 mm. official_alternate_route_check: the original BOM URL is a reichelt.de German route for product p335326; the cited reichelt.com/de/en page is Reichelt's English canonical/shop route for the same product number 335326 and row-matched product NEMA23-05."
    evidence_basis: "bom_provided"
  assumptions:
    - "The Reichelt catalog weight is treated as the per-unit physical motor mass for this BOM row."
  uncertainty_notes:
    - "The CAD file is a single vendor-component solid and does not separate housing, rotor, stator, windings, bearings, magnets, shaft, cable, or insulation into material-specific volumes."
material:
  primary_material: "Multi-material electromechanical stepper motor assembly: ferrous/stainless metal body and shaft, copper windings, magnetic rotor/stator materials, electrical insulation, bearings, and polymer cable insulation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.reichelt.com/de/en/shop/product/stepper_motor_nema_23_1_8_1_0_a_6_5_v_-335326; https://joy-it.net/en/products/NEMA23-05; https://www.linengineering.com/news/choosing-the-right-stepper-motor%3A-pm-stepper-or-hybrid-stepper"
    cited_fact_or_basis: "Local assembly STEP material extraction for 6T_motor_Nema_23 returned Stainless Steel with density 8000.0 kg/m3-like units. Reichelt and Joy-IT identify the row item as a NEMA23-05 bipolar stepper motor with 4 connecting cables, 6.35 mm shaft, and high-torque NEMA 23 frame. Lin Engineering describes stepper motors as having stator coils and a permanent-magnet rotor. targeted_web_search: queries tried included 'NEMA23-05 material stainless steel copper winding magnet material datasheet' and 'hybrid stepper motor construction stator windings permanent magnet rotor laminated steel'; results found row function, dimensions, weight, wiring, and generic stepper construction but no row-specific material bill or exact alloy breakdown."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP Stainless Steel tag is treated as useful evidence that the CAD exporter assigned a ferrous/stainless material, but not as a complete material bill for the whole electromechanical motor."
    - "Copper windings, magnetic rotor/stator materials, insulation, bearings, and polymer cable materials are inferred from standard stepper-motor construction."
  uncertainty_notes:
    - "Exact winding mass, magnet type, bearing type, insulation class material, and body/shaft alloy grades are unresolved and would need a manufacturer drawing, teardown, or detailed datasheet."
how_to_make:
  summary: "Manufacturing route would split it into motor housing/shaft, laminated magnetic core parts, rotor magnets, copper winding, bearings, cable/insulation, assembly, and electrical/torque testing"
  manufacturing_steps:
    - "Install it at the recoater pulley location, mount the NEMA 23 face, fit the 6.35 mm bore GT2 pulley to the shaft flat, route the four motor leads, and connect it to the stepper driver."
    - "For future local manufacture, Make the metal frame/end caps/shaft, laminated stator and rotor pole pieces, permanent magnet rotor, copper windings, bearings, cable and insulation parts, then assemble, align, and test step angle, winding resistance, insulation, holding torque, and runout"
  source:
    url_or_path: "https://www.reichelt.com/de/en/shop/product/stepper_motor_nema_23_1_8_1_0_a_6_5_v_-335326; https://joy-it.net/en/products/NEMA23-05; research/ream250_bom/ream250_bom_row_0200_6T__views_2x2.png"
    cited_fact_or_basis: "Reichelt identifies the row-matched product as a NEMA23-05 bipolar NEMA 23 stepper motor with 1.8 degree step angle, 132 Ncm holding torque, 6.35 mm shaft, and 1 A / 6.5 V rating. Joy-IT identifies NEMA23-05 as shipped as a stepper motor with 4 connecting cables and 6.35 x 20 mm shaft. The CAD contact sheet shows a finished motor body with protruding shaft and lead/cable feature. targeted_web_search: queries tried included 'NEMA23-05 manufacturing route', 'NEMA23-05 datasheet material winding shaft bearing', and 'hybrid stepper motor manufacturing laminated stator rotor winding'; results resolved product identity and generic motor construction but no row-specific factory process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local-manufacture decomposition is a planning hypothesis based on the row-matched motor type, CAD shape, and common stepper motor architecture."
  uncertainty_notes:
    - "A concrete self-manufacturing recipe would need lamination geometry, magnet specification, winding turns and wire gauge, bearing and shaft tolerances, insulation system, balancing/runout requirements, torque test method, and driver compatibility tests."
kb_implications:
  - "item_granularity: complex_module - Model as one reusable NEMA 23 stepper motor complex module for this pass; split into frame/shaft, laminations, rotor magnet, windings, bearings, cable, insulation, and acceptance testing only if motor self-manufacture becomes a priority."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0200_6T.md
source_research_sha256: 0c4125e117c5662ca358eeb799d9ad1a29ed3aaa7f880aa71df6e1065cce065a
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Reviewed the NEMA 23 stepper motor drive function, vendor mass, multi-material motor construction evidence,
    inferred motor decomposition route, KB implication, and preview showing a finished motor body with shaft and lead.
decomposition:
  decision: decompose_into_parts
  rationale: The row is a finished electromechanical motor module. Frame, shaft, laminations, windings, rotor magnet,
    bearings, cable, insulation, alignment, and electrical/torque testing are closure-relevant before merge and KB staging.
  proposed_subparts:
  - motor_frame_and_end_caps
  - motor_shaft
  - laminated_stator_stack
  - rotor_magnet_and_pole_pieces
  - copper_windings
  - bearing_set
  - cable_and_insulation
process_abstraction:
  original_process_family: vendor_stepper_motor_assembly_test
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
  - decomposition_required
  - import_assumption
  - precision_machining
  - assembly
  - calibration
  - dimensional_inspection
  candidate_existing_processes:
  - process_id: motor_assembly_standard_fabrication_v0
    fit: partial
    reason: Covers a generic motor assembly route, but the row still needs explicit stepper laminations, windings, magnets,
      bearings, cable, and acceptance tests.
  - process_id: coil_winding_motor_v0
    fit: supporting
    reason: Relevant to producing the motor windings after decomposition defines wire gauge and turn count.
  - process_id: motor_final_assembly_v0
    fit: supporting
    reason: Relevant to assembling the motor once decomposed subparts exist.
  - process_id: bearing_set_fabrication_v0_v0
    fit: supporting
    reason: Relevant because bearing closure is separate from the motor housing and windings.
  - process_id: cable_harness_assembly_v0
    fit: supporting
    reason: Relevant to the lead/cable feature visible in the row preview.
  - process_id: electrical_testing_and_calibration_v0
    fit: supporting
    reason: Relevant to winding resistance, insulation, step behavior, torque, and driver compatibility tests.
  abstraction_decision: substitute_process_family
  rationale: The row evidence describes a purchased NEMA 23 stepper motor with multiple material families and performance
    requirements. Treat it as precision import/decompose-later until the magnetic, winding, bearing, cable, and test workflows
    are modeled.
  process_guardrails:
    tolerance: blocked_until_decomposed
    surface_finish: shaft, bearing seats, and laminations need review after decomposition
    sealing_quality: not_applicable
    alignment_accuracy: shaft runout, bearing alignment, and rotor/stator gap are function-critical
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: provide controlled rotary actuation for a belt pulley in the recoater motion assembly
  material: multi_material_electromechanical_motor
  scale_or_capacity:
    mass_kg: 1.082
    bom_quantity: 1
    row_total_mass_kg: 1.082
    scale_class: medium
    frame_size: NEMA23
    holding_torque_Ncm: 132
    step_angle_deg: 1.8
    shaft_diameter_mm: 6.35
  geometry_form: square_frame_stepper_motor_with_shaft_and_leads
merge_pool:
  eligible: false
  functional_purpose_key: rotary_actuation
  precision_guardrails:
  - holding_torque
  - step_angle
  - shaft_runout
  - winding_resistance
  - insulation_quality
  - bearing_alignment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - precision_component_import_decompose_later
  import_risk_factors:
  - Exact winding mass, magnet type, bearing type, insulation system, and material grades are unresolved.
  - Magnetic laminations, permanent magnet production, winding control, bearing precision, and acceptance tests are major
    closure dependencies.
  - Driver compatibility and torque verification are required before local substitution.
  post_merge_decision_notes: Final import/local decision is deferred. Decompose this motor before merge review, then evaluate
    housing, shaft, laminations, windings, bearings, cable, magnets, assembly, and testing separately.
kb_staging:
  proposed_item_id: null
  notes: Do not assign a final closure item ID during row conversion; stage as a reusable stepper motor module needing
    decomposition before KB promotion.
assumptions:
- The Reichelt catalog mass is the best per-unit mass evidence for this multi-material module.
- The motor is represented as a complex module at row level until a focused self-manufacture pass exists.
- The GT2 pulley context is retained as use evidence, not as part of the motor item identity.
unresolved:
- Exact motor sub-BOM, magnet composition, lamination geometry, winding turns, wire gauge, bearing specification, and insulation
  system are unknown.
- Torque test method, runout requirement, and driver integration tests are not specified by the row evidence.
```
