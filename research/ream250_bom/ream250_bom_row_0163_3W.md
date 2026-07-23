---
row_identity:
  item: "3W"
  cad_file: "3W_dummy_oxygen_sensor_FCX-TR"
  source_row_number: 163
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://sensorsandpower.angst-pfister.com/de/produkte/gassensoren/produkt/fcx-tr0025-amperometric-oxygen-o2-gas-transmitter/"
function:
  summary: "Angst+Pfister FCX-TR0025 oxygen transmitter module for measuring 0-25% oxygen concentration and converting the zirconia sensor signal to a 4-20 mA industrial output."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3W_dummy_oxygen_sensor_FCX-TR.step; https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/FCX-TR_1620-21914-0029-E-0821.pdf"
    cited_fact_or_basis: "BOM row 163 identifies item 3W as 3W_dummy_oxygen_sensor_FCX-TR, manufacturer Angst + Pfister, description oxygen (O2) gas transmitter. Manifest row 163 maps the same item to the per-part STEP. FreeCAD measured one solid with volume about 60172.791 mm3, area about 11084.770 mm2, and bounding box about 34.50 x 114.00 x 34.50 mm; the rendered contact sheet shows a cylindrical threaded transmitter body with connector/end features. The FCX-TR manual says the FCX-TR0025 range is 0...25% O2, the sensor and measurement electronics are integrated in a stainless steel transmitter housing, and the electronics outputs 4-20 mA."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The BOM wording includes 'valve sv04_din_cc_dn40_-' after the oxygen-transmitter description, but the CAD filename, manufacturer, URL, dimensions, and manual all match the FCX-TR oxygen transmitter rather than a separate valve."
mass:
  value_kg: 0.25
  basis: "Use the official FCX-TR manual weight of 250 g, or 0.25 kg, per transmitter. BOM quantity is 1, so the row total is also about 0.25 kg. FreeCAD measured volume about 60172.791 mm3 and bounding box about 34.50 x 114.00 x 34.50 mm; the vendor weight is preferred over CAD-density calculation for this mixed stainless-housing, sensor, connector, and electronics module."
  source:
    url_or_path: "https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/FCX-TR_1620-21914-0029-E-0821.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3W_dummy_oxygen_sensor_FCX-TR.step"
    cited_fact_or_basis: "The FCX-TR manual specifications list dimensions length/diameter 114 mm / Ø34.5 mm and weight 250 g. FreeCAD measured one STEP solid, volume about 60172.791 mm3, area about 11084.770 mm2, and bounding box about 34.50 x 114.00 x 34.50 mm."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local STEP assembly material extractor returned only Generic with density 1000.0, which is placeholder metadata and was not used for mass."
material:
  primary_material: "Stainless steel transmitter housing with zirconium oxide oxygen sensor, integrated control/amplifier electronics, M8 4-pole electrical connector, and a small PA6.6 plastic protection screw."
  source:
    url_or_path: "https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/FCX-TR_1620-21914-0029-E-0821.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The FCX-TR manual states the zirconia oxygen sensor is built into a stainless steel transmitter housing, with control electronics integrated into the housing; it also identifies a male M8 4-pole electrical connection and an M3x6 PA6.6 plastic screw protecting the potentiometer. Local assembly STEP material extraction for 3W_dummy_oxygen_sensor_FCX-TR returned only Generic with density 1000.0, so CAD metadata was treated as placeholder."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The source does not provide a full material breakdown for electrodes, connector contacts, PCB, potting, seals, or internal fasteners; treat those as unresolved submaterials inside the purchased transmitter module."
how_to_make:
  summary: "A future Manufacturing route would decompose it into precision stainless housing fabrication, zirconia sensor production, electronics assembly, connector installation, calibration, and functional testing"
  manufacturing_steps:
    - "Integration route: screw-mount the transmitter by its G1/2 process connection, connect the M8 4-pole electrical interface or matching cable, supply 10-28 VDC, and verify output/calibration in dry air or calibration gas per the manual."
    - "Manufacturing route: machine or otherwise fabricate the stainless transmitter housing and process adapter, make or source the zirconium-oxide oxygen sensing element, assemble heater/control/amplifier electronics and connector hardware, install protection screw and seals as required, then calibrate and verify 4-20 mA output response."
  source:
    url_or_path: "https://sensorsandpower.angst-pfister.com/fileadmin/products/datasheets/272/FCX-TR_1620-21914-0029-E-0821.pdf; research/ream250_bom/ream250_bom_row_0163_3W__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3W_dummy_oxygen_sensor_FCX-TR.step"
    cited_fact_or_basis: "The FCX-TR manual establishes product identity, sensor range, stainless housing, zirconia sensor, 4-20 mA output, G1/2 process connection, M8 4-pole electrical connection, dimensions, weight, and factory calibration behavior. CAD geometry and preview confirm the compact threaded cylindrical transmitter form. targeted_web_search: queries tried included 'FCX-TR0025 amperometric oxygen O2 gas transmitter Angst Pfister datasheet weight material', 'FCX-TR0025 amperometric oxygen O2 gas transmitter Angst+Pfister', and 'FCX-TR oxygen gas transmitter datasheet FCX-TR0025'; results found official/product/manual data but no row-specific factory manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Near-term KB modeling should treat this as a calibrated external sensor/transmitter module, because zirconia oxygen sensor fabrication and calibration are specialized precision-electronics work"
    - "The a planning decomposition inferred from the sourced product architecture and CAD shape, not a disclosed Angst+Pfister factory route."
  uncertainty_notes:
    - "A concrete self-manufacturing recipe would need sensor ceramic/electrode details, heater design, PCB schematic, connector and seal specifications, calibration procedure limits, and acceptance-test requirements."
kb_implications:
  - "item_granularity: complex_module - Model this row as one calibrated FCX-TR oxygen-transmitter complex module for this pass; split later only if oxygen-sensor/electronics manufacturing becomes a priority."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0163_3W.md
source_research_sha256: "7b243156d780162ef9ef47dc6cbb14c6cb9d269d8c2550d6af9a1d73987e1a39"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed oxygen transmitter function, vendor mass and dimensions, mixed stainless/zirconia/electronics material evidence, integration and manufacturing route notes, and CAD preview showing a compact threaded cylindrical transmitter."
decomposition:
  decision: decompose_into_parts
  rationale: "The row is a calibrated sensor transmitter module with housing, zirconia sensing element, electronics, connector, seals, and calibration dependencies that matter for closure."
  proposed_subparts:
    - stainless_threaded_transmitter_housing
    - zirconia_oxygen_sensing_element
    - control_amplifier_electronics
    - m8_electrical_connector
    - seals_and_protection_hardware
process_abstraction:
  original_process_family: calibrated_zirconia_sensor_transmitter_manufacture
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - decomposition_required
    - import_assumption
    - precision_machining
    - ceramic_sintering
    - assembly
    - calibration
  candidate_existing_processes:
    - process_id: import_receiving_basic_v0
      fit: direct
      reason: "Appropriate near-term closure handle if the calibrated transmitter remains an imported precision module."
    - process_id: electronic_assembly_v0
      fit: partial
      reason: "Covers PCB/enclosure assembly patterns, but lacks the zirconia sensing element, heater controls, connector details, and calibration gas response."
    - process_id: calibration_and_test_basic_v0
      fit: partial
      reason: "Covers basic calibration and functional testing, but row-specific oxygen range and 4-20 mA verification need explicit procedures."
    - process_id: ceramic_sintering_high_temp_v0
      fit: poor_fit
      reason: "Only a coarse ceramic process anchor for the zirconia element; sensor electrodes, heater structure, and gas-response behavior are missing."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for the stainless threaded transmitter housing and process adapter if decomposed for local manufacture."
  abstraction_decision: substitute_process_family
  rationale: "The source item is not a simple machined housing; the closure abstraction should defer local manufacture until the sensor, electronics, connector, and calibration dependencies are separated."
  process_guardrails:
    tolerance: high
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: oxygen concentration transmitter with industrial current output
  material: mixed_stainless_steel_zirconia_electronics_polymer
  scale_or_capacity:
    mass_kg: 0.25
    bom_quantity: 1
    row_total_mass_kg: 0.25
    scale_class: small
  geometry_form: threaded_cylindrical_sensor_transmitter_module
merge_pool:
  eligible: false
  functional_purpose_key: oxygen_concentration_measurement
  precision_guardrails:
    - sensing_element_materials
    - calibration_accuracy
    - electronics_functionality
    - connector_interface
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Zirconia oxygen sensing element fabrication is specialized."
    - "Integrated heater, amplifier electronics, connector hardware, and factory calibration are unresolved."
    - "Acceptance testing requires controlled oxygen calibration gas and 4-20 mA verification."
  post_merge_decision_notes: "Final import/local decision is deferred; perform decomposition review before merging with generic sensor suites."
kb_staging:
  proposed_item_id: null
  notes: "Do not assign a final closure item in row conversion; stage as a precision sensor module pending decomposition."
assumptions:
  - "Vendor weight of 0.25 kg is the authoritative planning mass for the assembled transmitter."
  - "The row should remain one functional sensor module in this pass, while subparts are listed for later closure analysis."
  - "The stray BOM wording mentioning a valve is treated as row metadata noise because the CAD, URL, manufacturer, and manual all identify the oxygen transmitter."
unresolved:
  - "Full material breakdown for electrodes, PCB, connector contacts, seals, potting, and internal fasteners is unavailable."
  - "Sensor fabrication route, heater design, calibration procedure limits, and acceptance-test thresholds need future research."
```
