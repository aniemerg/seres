---
row_identity:
  item: "81"
  cad_file: "81_vacuum_pump_Duo35"
  source_row_number: 277
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/PK_D45_602_E"
function:
  summary: "Pfeiffer Vacuum Duo 35 oil-sealed, two-stage rotary vane vacuum pump module with 3-phase motor, used to generate low to medium vacuum for the reAM250 vacuum subsystem."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/81_vacuum_pump_Duo35.step; https://www.idealvac.com/en-us/Pfeiffer-DUO-35-Dual-Stage-Rotary-Vane-Vacuum-Pump-440-480-VAC-3-Phase-PN%3A-PK-D45-602/pp/P107998; https://res.cloudinary.com/iwh/image/upload/q_auto%2Cg_center/assets/1/26/PfeifferDuo_35_Manual.pdf"
    cited_fact_or_basis: "BOM row 277 identifies item 81 as 81_vacuum_pump_Duo35, quantity 1, product PK D45 602 E, manufacturer Pfeiffer Vacuum. FreeCAD measured one CAD solid with volume about 29,602,320.000 mm3 and bounding box about 241.88 x 823.69 x 368.70 mm; the rendered contact sheet shows a motor-driven pump on base rails with pump body, cylindrical motor, and vacuum-port features. Ideal Vacuum identifies PN PK D45 602 as a Pfeiffer DUO35 two-stage rotary vane vacuum pump for low to medium vacuum. The operating manual table lists order number PK D45 602 as Duo 35, 3-phase motor, 3TF, 230/400 V 50 Hz and 265/460 V 60 Hz. bom_url_route_check: the BOM-provided Pfeiffer URL was checked first but the current Pfeiffer shop page returned a product-not-loaded page, so row-matched distributor/manual evidence was used for function."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The BOM suffix PK D45 602 E is treated as the same Duo 35 order-number family as PK D45 602 in the manual and distributor sources."
  uncertainty_notes:
    - "The current Pfeiffer shop URL no longer exposes the product detail directly, so the function relies on row-matched secondary vendor/manual evidence plus the local CAD export."
mass:
  value_kg: 68.0
  basis: "Use 68 kg per physical pump as the BOM planning mass. BOM quantity is 1, so the row total is also about 68 kg. FreeCAD measured CAD volume about 29,602,320.000 mm3, area about 1,173,155.010 mm2, and a bounding box about 241.88 x 823.69 x 368.70 mm; vendor/manual mass supersedes CAD-density estimation for this multi-material pump-and-motor module."
  source:
    url_or_path: "https://res.cloudinary.com/iwh/image/upload/q_auto%2Cg_center/assets/1/26/PfeifferDuo_35_Manual.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/81_vacuum_pump_Duo35.step"
    cited_fact_or_basis: "The operating manual technical-data table for Duo 35 lists order number PK D45 602 and weight with motor 68 kg. FreeCAD measured one solid, volume about 29,602,320.000 mm3, area about 1,173,155.010 mm2, and bounding box about 241.88 x 823.69 x 368.70 mm. bom_url_route_check: the BOM-provided Pfeiffer product URL was checked first but did not load product specifications, so the row-matched operating manual table was used for the mass value."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The manual's weight with motor is the relevant installed purchased-module mass for the BOM row."
    - "The E suffix in the BOM part number does not materially change the listed Duo 35 PK D45 602 pump mass for KB planning."
  uncertainty_notes:
    - "The CAD export is one vendor-component solid and does not split pump body, motor, oil fill, guards, fasteners, bearings, seals, or electrical hardware into separate masses."
material:
  primary_material: "Unknown multi-material electromechanical vacuum pump module: metal pump housing/rotor/stator/base hardware, electric motor steel/copper/insulation materials, P3 mineral operating oil, and elastomer or polymer seals, gaskets, cable insulation, and protective parts."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://res.cloudinary.com/iwh/image/upload/q_auto%2Cg_center/assets/1/26/PfeifferDuo_35_Manual.pdf"
    cited_fact_or_basis: "Local assembly STEP material extraction for 81_vacuum_pump_Duo35 returned only Generic with density 1000.0, which is placeholder metadata and was not used to resolve material. The operating manual identifies a motorized Duo 35 rotary vane pump and lists P3 operating fluid for PK D45 602. targeted_web_search: queries tried included 'PK D45 602 E material Duo 35 housing', 'Pfeiffer Duo 35 material housing rotor vane', and 'Pfeiffer Duo 35 datasheet material weight'; results resolved function, mass, oil type, and dimensions but no authoritative row-specific material breakdown."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Material families are inferred only at broad electromechanical pump-module level because no row-matched source found a full material bill or exact housing/rotor grades."
  uncertainty_notes:
    - "Do not treat the broad material set as a sourced Pfeiffer sub-BOM; local manufacturing would require a teardown, parts list, or manufacturer drawing."
how_to_make:
  summary: "Decompose it into precision rotary-vane pump internals, housing, motor, seals, valves, oil system, base hardware, assembly, and acceptance testing"
  manufacturing_steps:
    - "Install the pump on its base rails or machine mounting points, connect DN/KF vacuum plumbing and exhaust, fill/verify P3 operating oil, and wire the 3-phase motor according to the required supply."
    - "For future local manufacture, split the module into cast or machined pump housing, rotor, vanes, stator surfaces, bearings, motor, safety/gas-ballast valve parts, seals, base hardware, oil fill/drain hardware, final assembly, leak/performance testing, and electrical safety testing."
  source:
    url_or_path: "https://www.idealvac.com/en-us/Pfeiffer-DUO-35-Dual-Stage-Rotary-Vane-Vacuum-Pump-440-480-VAC-3-Phase-PN%3A-PK-D45-602/pp/P107998; https://res.cloudinary.com/iwh/image/upload/q_auto%2Cg_center/assets/1/26/PfeifferDuo_35_Manual.pdf; research/ream250_bom/ream250_bom_row_0277_81__views_2x2.png"
    cited_fact_or_basis: "Ideal Vacuum identifies PN PK D45 602 as a Pfeiffer DUO35 two-stage rotary vane pump with 3-phase motor for low to medium vacuum. The operating manual gives Duo 35 order-number, motor, operating-fluid, performance, and weight data. The CAD contact sheet shows the row as one complete pump-and-motor module. targeted_web_search: 'PK D45 602 E manufacturing route', 'Pfeiffer Duo 35 pump manufacturing', and 'Pfeiffer Duo 35 material housing rotor vane' found product/manual data but no row-specific factory manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local-manufacture decomposition is a planning hypothesis based on the rotary-vane pump function, CAD shape, and common electromechanical pump architecture."
  uncertainty_notes:
    - "A concrete self-manufacturing recipe would need rotor/stator tolerances, vane material, bearing and seal specifications, motor design, valve details, oil compatibility, balancing, leak-rate, ultimate-pressure, and run-test requirements."
kb_implications:
  - "item_granularity: complex_module - Model as one Pfeiffer Duo 35 vacuum pump complex module for this pass; split into pump body/internals, motor, seals, valves, oil system, base hardware, and calibration/testing workflow only if vacuum-pump manufacturing becomes a priority."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0277_81.md
source_research_sha256: "beb0a831f1e63c210be6944923ef07dfaac8a3481d1be2502795e8466def5397"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the pump function, manual-derived installed mass, multi-material module evidence, decomposition-oriented manufacturing notes, KB implications, and CAD preview before conversion."
decomposition:
  decision: decompose_into_parts
  rationale: "The row is a complete oil-sealed rotary-vane pump and motor module. It contains precision pump internals, motor materials, seals, valves, oil system, base hardware, assembly, and performance-test dependencies that should be exposed before any local-manufacture decision."
  proposed_subparts:
    - pump_housing_and_stator_surfaces
    - rotor_and_vane_set
    - shaft_bearings_and_seals
    - electric_motor_module
    - valve_and_gas_ballast_hardware
    - operating_oil_system
    - base_rails_and_mounting_hardware
    - electrical_connection_hardware
process_abstraction:
  original_process_family: vendor_oil_sealed_rotary_vane_pump_module
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - decomposition_required
    - import_assumption
    - assembly
    - leak_testing
    - pressure_testing
    - calibration
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: hydraulic_pump_unit_assembly_v0
      fit: poor_fit
      reason: "Only a rough pump-module assembly analogy; it does not cover rotary-vane low-pressure pump tolerances and oil-sealed gas handling."
    - process_id: pump_housing_machining_v0
      fit: supporting
      reason: "Relevant to precision housing and stator-surface machining if the pump body is decomposed later."
    - process_id: motor_assembly_standard_fabrication_v0
      fit: supporting
      reason: "Relevant to the attached 3-phase motor portion of the module."
    - process_id: vacuum_testing_v0
      fit: supporting
      reason: "Covers pumpdown/performance testing context after assembly."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Covers seal and joint leak checks in the pump and connected gas path."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers interface, mounting, and incoming module checks."
  abstraction_decision: needs_human
  rationale: "This is a heavy calibrated pump module with precision internals and motor integration. Phase 1 should preserve it as a decomposition target and likely import-risk item rather than map it to a simple fabrication bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: pump gas from the machine chamber to maintain low-pressure operation
  material: mixed_electromechanical_fluidic
  scale_or_capacity:
    mass_kg: 68.0
    bom_quantity: 1
    row_total_mass_kg: 68.0
    scale_class: large
  geometry_form: rotary_vane_pump_module_with_motor_base_and_ports
merge_pool:
  eligible: true
  functional_purpose_key: gas_pumping
  precision_guardrails:
    - pumping_speed
    - ultimate_pressure
    - oil_compatibility
    - motor_voltage
    - leak_rate
    - vibration
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Rotary-vane pump manufacture requires precision rotor/stator geometry, vane material, bearings, seals, oil compatibility, motor integration, balancing, and performance testing."
    - "Vendor manual mass and performance imply a purchased industrial module beyond the current simple fabrication scope."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups comparable gas-pumping modules and a later decomposition pass defines pump internals."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review and decomposition; do not create a row-specific Pfeiffer item unless no reusable gas-pumping abstraction fits."
assumptions:
  - "The 68 kg manual value with motor is the installed module mass for closure grouping."
  - "The BOM suffix is treated as part of the same Duo 35 order-number family for planning."
  - "P3 operating oil and performance tests are part of the module closure problem."
unresolved:
  - "Rotor/stator tolerances, vane material, bearing and seal specifications, motor sub-BOM, valve details, oil fill amount, balancing, leak-rate target, ultimate pressure, and run-test requirements are not resolved by row evidence."
```
