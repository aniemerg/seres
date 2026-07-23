---
row_identity:
  item: "2APD"
  cad_file: "2APD_temperature_sensor"
  source_row_number: 83
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.sensorshop24.de/temperaturfuehler-passiv/einschraubfuehler/einschraubtemperaturfuehler-mit-m6-gewinde-und-17mm-einbaulaenge?gclid=CjwKCAiA3pugBhAwEiwAWFzwdQBx2F7Mx5fSqYqBRL3cTjxoc6K1ZIkG89zC_WzhvPEmSCOVUAO9XRoCgmwQAvD_BwE"
function:
  summary: "Sensorshop24 EF9 screw-in passive temperature sensor for measuring the build-platform or heating-plate temperature through an M6x1 threaded probe with a PT100 sensing element and 5 m lead."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.sensorshop24.de/temperaturfuehler-passiv/einschraubtemperaturfuehler-mit-m6-gewinde-und-17mm-einbaulaenge; research/ream250_bom/ream250_bom_row_0083_2APD__views_2x2.png"
    cited_fact_or_basis: "BOM row 83 identifies item 2APD as 2APD_temperature_sensor, product EF9-EF9G-PT100-2L-5.0 from Sensorshop 24. The Sensorshop24 EF9 product page names an Einschraubtemperaturfuehler with M6x1 thread and 17 mm insertion length, and exposes selectable PT100 sensors, 2/3/4-wire wiring, cable lengths including 5 m, and IP54/IP67 protection. The CAD preview shows a slim probe/lead body with a small threaded/hex sensor end."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-specific product code PT100-2L-5.0 is interpreted as the selected PT100, two-wire, 5 m configuration from the Sensorshop24 EF9 option set."
  uncertainty_notes: []
mass:
  value_kg: 0.11
  basis: "Best planning estimate is 0.11 kg per sensor for BOM quantity 1. FreeCAD measured the simplified row STEP as one solid with volume 1596.288 mm^3 and bounding box 131.00 x 10.00 x 11.55 mm; if treated as stainless-steel-equivalent probe body volume using kb/materials/properties.yaml stainless_steel density 8000 kg/m^3, that visible CAD body contributes about 0.0128 kg. The remaining estimate is dominated by the product-code 5 m two-wire lead, modeled as about 0.019 kg/m for a small insulated sensor cable, or about 0.095 kg, giving about 0.108 kg total rounded to 0.11 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APD_temperature_sensor.step; kb/materials/properties.yaml; https://www.sensorshop24.de/temperaturfuehler-passiv/einschraubtemperaturfuehler-mit-m6-gewinde-und-17mm-einbaulaenge"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 1596.288 mm^3, area 1683.396 mm^2, and bounding box 131.00 x 10.00 x 11.55 mm. The Sensorshop24 EF9 page provides cable-length options including 5 m and the row product code includes PT100-2L-5.0. The local density table lists stainless_steel density 8000 kg/m^3. targeted_web_search: searched \"EF9-EF9G-PT100-2L-5.0\", \"EF9G PT100 2L 5.0 Sensorshop24 weight\", \"Sensorshop24 EF9G PT100 Glasseide 5m weight\", and \"Einschraubtemperaturfuehler M6x1 17mm PT100 5m weight\"; results resolved the product family and row identity but no row-specific catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The visible CAD solid represents the metal probe/fitting envelope, not the full physical length of the 5 m cable."
    - "A small two-wire insulated temperature-sensor lead is modeled at about 0.019 kg/m for planning mass, so cable mass dominates the total."
  uncertainty_notes:
    - "No row-matched catalog weight was found; actual mass could vary substantially with cable jacket material, conductor gauge, strain relief, and connector or bare-lead termination details."
material:
  primary_material: "metal screw-in probe/fitting, PT100 resistance sensor element, copper conductors, and high-temperature cable insulation"
  source:
    url_or_path: "https://www.sensorshop24.de/temperaturfuehler-passiv/einschraubtemperaturfuehler-mit-m6-gewinde-und-17mm-einbaulaenge; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Sensorshop24 EF9 page identifies selectable lead materials PVC, Silikon, PFA, and Glasseide; selectable sensors including PT100; and selectable 2/3/4-wire wiring. BOM product code EF9-EF9G-PT100-2L-5.0 preserves EF9G, PT100, 2L, and 5.0 tokens. The local assembly STEP material extractor matched 2APD_temperature_sensor but returned Generic material and density 1000.0, which is placeholder metadata. targeted_web_search: searched \"EF9G Sensorshop24 PT100 Glasseide\", \"EF9G-PT100-2L-5.0\", \"EF9 EF9G PT100 2L\", and \"Sensorshop24 EF9G Glasseide\"; results found Sensorshop24 EF9G product-family pages but no row-specific material breakdown or metal grade."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "EF9G is treated as the Glasseide/high-temperature lead variant within the EF9 option family, but the result keeps material broad because the page does not expose a complete row-specific bill of materials."
    - "The screw-in probe/fitting is modeled as metal-compatible sensor hardware without assigning a specific alloy grade."
  uncertainty_notes:
    - "Exact probe alloy, PT100 element packaging, conductor gauge, insulation construction, and termination hardware remain unspecified."
how_to_make:
  summary: "Assemble a machined/threaded metal probe body, PT100 element, insulated conductors, cable jacket, strain relief, and final resistance/insulation test"
  manufacturing_steps:
    - "Use the EF9 M6x1, 17 mm insertion-length PT100, two-wire, 5 m configuration as the reference geometry and electrical specification for the local sensor build"
    - "Manufacturing route: machine or source the small M6x1 threaded metal probe/fitting and prepare the sensor cavity."
    - "Install and pot or crimp a PT100 resistance element with two insulated copper leads into the probe tip."
    - "Attach the 5 m high-temperature cable, add strain relief or termination hardware as required, then perform resistance, insulation, and temperature calibration checks."
  source:
    url_or_path: "https://www.sensorshop24.de/temperaturfuehler-passiv/einschraubtemperaturfuehler-mit-m6-gewinde-und-17mm-einbaulaenge; research/ream250_bom/ream250_bom_row_0083_2APD__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APD_temperature_sensor.step"
    cited_fact_or_basis: "The Sensorshop24 page identifies the EF9 product as a configurable screw-in temperature sensor with M6x1 thread, 17 mm insertion length, PT100 option, wiring options, cable-material options, cable lengths, and made-to-order support. The CAD contact sheet shows a slim sensor/probe lead with a small threaded/hex feature. targeted_web_search: searched \"EF9-EF9G-PT100-2L-5.0 manufacturing\", \"Sensorshop24 EF9 PT100 screw-in temperature sensor datasheet\", and \"M6x1 PT100 screw-in temperature sensor construction\" results resolved product configuration but not a row-specific manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The detailed Manufacturing route is inferred from the sourced product type, PT100 configuration, and visible probe geometry."
    - "Calibration and insulation testing are required for a usable replacement sensor even though the BOM row does not state test requirements."
  uncertainty_notes:
    - "Vendor evidence does not provide the exact internal construction, potting compound, cable gauge, or calibration class selected beyond the visible PT100/two-wire/5 m row code."
kb_implications:
  - "item_granularity: complex_module - treat as a configured calibrated temperature-sensor assembly for near-term KB modeling; defer splitting into probe body, RTD element, cable, insulation, and calibration workflow until sensor manufacturing is modeled."
---

# reAM250 BOM Row 83 - 2APD

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0083_2APD.md
source_research_sha256: "f0313f1b9b3a931c01d3eedeb9b95a940d7023e54e7d445e0a99cd016d49e472"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed screw-in PT100 temperature-sensor function, planning mass including 5 m lead, mixed material evidence, inferred probe/cable/calibration route, and CAD preview showing a slim threaded probe form."
decomposition:
  decision: decompose_into_parts
  rationale: "The row is a calibrated sensor assembly with probe body, RTD element, long cable, insulation, strain relief, and test dependencies that matter for closure."
  proposed_subparts:
    - threaded_metal_probe_body
    - pt100_resistance_temperature_element
    - insulated_copper_sensor_lead
    - cable_insulation_and_strain_relief
    - termination_hardware
process_abstraction:
  original_process_family: configured_rtd_temperature_sensor_assembly
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - decomposition_required
    - import_assumption
    - precision_machining
    - assembly
    - calibration
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: import_receiving_basic_v0
      fit: direct
      reason: "Appropriate near-term closure handle if the configured calibrated sensor remains imported."
    - process_id: electrical_wiring_assembly_v0
      fit: partial
      reason: "Covers wired sensor assembly patterns, but lacks PT100 element construction, probe potting, and calibration class controls."
    - process_id: insulated_wire_formation_v0
      fit: supporting
      reason: "Relevant for the long insulated copper lead if decomposed for local manufacture."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for making the small M6 threaded metal probe body."
    - process_id: calibration_and_test_basic_v0
      fit: partial
      reason: "Covers basic calibration and functional testing, but row-specific temperature accuracy and insulation checks need explicit procedures."
  abstraction_decision: substitute_process_family
  rationale: "The source route is a configured sensor build, not a single low-risk fabricated part; the closure model should defer local manufacture until the probe, RTD element, lead, and calibration steps are separated."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: low
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: screw-in temperature measurement for heated machine surfaces
  material: mixed_metal_pt100_copper_high_temperature_insulation
  scale_or_capacity:
    mass_kg: 0.11
    bom_quantity: 1
    row_total_mass_kg: 0.11
    scale_class: small
  geometry_form: m6_threaded_probe_with_5m_sensor_lead
merge_pool:
  eligible: false
  functional_purpose_key: temperature_measurement
  precision_guardrails:
    - calibration_accuracy
    - insulation_resistance
    - cable_temperature_rating
    - probe_thread_interface
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "PT100 element construction, potting, cable material, and calibration class are unresolved."
    - "The 5 m high-temperature lead dominates mass and depends on insulation materials not specified by the row."
    - "Usable replacement requires resistance, insulation, and temperature calibration checks."
  post_merge_decision_notes: "Final import/local decision is deferred; perform decomposition review before merging with generic sensor items."
kb_staging:
  proposed_item_id: null
  notes: "Do not assign a final closure item during row conversion; stage as a precision sensor assembly pending decomposition."
assumptions:
  - "Planning mass of 0.11 kg is retained because visible CAD excludes most of the 5 m cable."
  - "The product code is interpreted as PT100, two-wire, 5 m configuration."
  - "The sensor can remain a functional module in this pass while subparts are listed for later closure analysis."
unresolved:
  - "Probe alloy, RTD element package, conductor gauge, insulation construction, termination hardware, and calibration class are not fully specified."
  - "Exact installation target and environmental rating selected from the product options remain unclear."
```
