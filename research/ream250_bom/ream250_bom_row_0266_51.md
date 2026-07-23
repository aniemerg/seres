---
row_identity:
  item: "51"
  cad_file: "51_dummy_scanner"
  source_row_number: 266
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.raylase.de/_Resources/Persistent/4/9/b/7/49b7182a146725d34457ce6b213a228d737e26a8/RAYLASE_AM-MODUL NEXT GEN_en.pdf"
function:
  summary: "Raylase AM-MODULE NEXT GEN fiber-laser scan module for additive manufacturing; it provides fast beam deflection, digitally controlled scan positioning, variable spot size through a zoom axis, and process-monitoring optical outputs for cameras, pyrometers, or photodiodes."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/51_dummy_scanner.step; research/ream250_bom/ream250_bom_row_0266_51__views_2x2.png; https://www.raylase.de/_Resources/Persistent/4/9/b/7/49b7182a146725d34457ce6b213a228d737e26a8/RAYLASE_AM-MODUL NEXT GEN_en.pdf"
    cited_fact_or_basis: "BOM row 266 names item 51, quantity 1, CAD file 51_dummy_scanner, description AM-Module Next Gen, manufacturer Raylase, and the Raylase AM-MODULE NEXT GEN PDF route. Manifest row 266 maps the row to a matched vendor-component STEP. FreeCAD measured 1 solid with volume 34111966.482 mm^3, area 787778.761 mm^2, and bounding box 407.50 x 589.00 x 270.00 mm; the contact sheet shows a large scanner/module envelope with protruding mounting or optical-interface features. The Raylase PDF describes the AM-MODULE NEXT GEN as an additive-manufacturing module for fiber-coupled lasers with beam deflection, flexible spot diameter, digital control, process-control sensor connections, and multi-module operation over one build field."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local CAD filename says dummy_scanner, so CAD shape is used for envelope/function consistency rather than for exact internal scanner layout."
mass:
  value_kg: 15.0
  basis: "Per unit. BOM quantity is 1, so the row total is about 15 kg if the row is the base module alone. The Raylase PDF gives approximate weights of 15 kg for the BASE-Module and 5 kg for the optional RAYSPECTOR monitoring unit; if this row includes RAYSPECTOR, planning mass would be about 20 kg. CAD volume 34111966.482 mm^3 is not converted by density because the vendor module is a hollow, multi-material calibrated assembly and local STEP material metadata only reports Generic at density 1000."
  source:
    url_or_path: "https://www.raylase.de/_Resources/Persistent/4/9/b/7/49b7182a146725d34457ce6b213a228d737e26a8/RAYLASE_AM-MODUL NEXT GEN_en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/51_dummy_scanner.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Raylase mechanical data gives approximate weights for the BASE-Module and optional RAYSPECTOR. FreeCAD measured the row STEP as 1 solid, volume 34111966.482 mm^3, area 787778.761 mm^2, and bounding box 407.50 x 589.00 x 270.00 mm. The local assembly STEP material extractor matched 51_dummy_scanner but returned material Generic and density 1000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM row description AM-Module Next Gen is treated as the base scanner module, not the optional RAYSPECTOR add-on, because the row does not explicitly name RAYSPECTOR."
  uncertainty_notes:
    - "Mass may be approximately 20 kg instead of 15 kg if the row's CAD/assembly intent includes the optional RAYSPECTOR monitoring unit."
material:
  primary_material: "multi-material optomechatronic module: aluminum cooling-contact parts, silicon-carbide deflection mirrors with coating for 1060-1090 nm fiber lasers, galvanometer scanner/electronics, optical sets, lens/fiber interfaces, water/air-cooling connections, electrical/data connectors, and process-monitoring sensor interfaces"
  source:
    url_or_path: "https://www.raylase.de/_Resources/Persistent/4/9/b/7/49b7182a146725d34457ce6b213a228d737e26a8/RAYLASE_AM-MODUL NEXT GEN_en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Raylase describes aluminum parts that require cooling-water corrosion protection, silicon-carbide mirror substrate for the 1060-1090 nm laser range, mirror variations, electronic components, galvanometer scanner, deflection mirrors, optical sets for fiber coupling, laser fiber socket, water connection, power/data connection, C-mount camera connection, and process-light outputs. Local assembly STEP material extraction matched the product but returned only Generic material and density 1000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The PDF identifies material families and key optical/electronic components, but it does not provide a full sub-BOM, exact alloy grades, coatings beyond the mirror notation, or material fractions."
how_to_make:
  summary: "Machine integration with the laser fiber, power and RL3-100 data connection, water/air cooling services, and process-monitoring sensor paths. Local self-manufacture should be deferred until a detailed scanner/optics/electronics sub-BOM and calibration process are modeled"
  manufacturing_steps:
    - "Integrate the module mechanically using the CAD envelope and mounting/interface protrusions as layout constraints."
    - "Connect QBH laser fiber, +48 V power, RL3-100 data, water temperature control or air cooling as configured, and process-monitoring camera/pyrometer/photodiode paths."
    - "Commission the module through Raylase-style field setup, software adjustment, focus tracking, and process-monitoring calibration before production use."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0266_51__views_2x2.png; https://www.raylase.de/_Resources/Persistent/4/9/b/7/49b7182a146725d34457ce6b213a228d737e26a8/RAYLASE_AM-MODUL NEXT GEN_en.pdf"
    cited_fact_or_basis: "BOM row 266 identifies the row as a Raylase AM-Module Next Gen. The Raylase PDF states that Raylase develops, manufactures, and tests its products in-house, and it describes the relevant fiber, power/data, water/air cooling, process-monitoring, setup, and software-adjustment interfaces. The contact sheet shows a simplified module envelope suitable for integration planning, not a local manufacturing sub-BOM."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "A future local-manufacturing model would need scanner motor, mirror, optical coating, electronics, cooling, alignment, and calibration details that are not exposed by the BOM row or PDF."
kb_implications:
  - "item_granularity: complex_module - Treat as a calibrated Raylase laser scan/monitoring subsystem for near-term KB modeling; split into galvo scanner, zoom/focus optics, mirrors, electronics, cooling hardware, and sensor paths only if a detailed optomechatronic scanner manufacturing workflow becomes a target."
---

# reAM250 BOM Row 266 - 51

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0266_51.md
source_research_sha256: "75689ff76cfce0acdf8604d00c6def8693301f26c7de0454b4317da19a828db6"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read laser scan-module function, Raylase mass basis, multi-material optomechatronic evidence, integration/calibration route, KB implication, and preview of the large scanner-module envelope."
decomposition:
  decision: complex_module
  rationale: "The row is a calibrated laser scan subsystem with internal scanner mechanics, precision mirrors, optics, electronics, cooling services, and monitoring interfaces; closure cannot model it as a simple housing."
  proposed_subparts:
    - scanner_housing_and_mounting_frame
    - galvanometer_scanner_set
    - coated_silicon_carbide_mirrors
    - zoom_focus_optics
    - fiber_laser_interface
    - control_and_drive_electronics
    - cooling_connections
    - process_monitoring_sensor_interfaces
process_abstraction:
  original_process_family: calibrated_laser_scan_module_integration
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - precision_machining
    - coating
    - assembly
    - cleaning
    - calibration
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: optical_sensor_alignment_assembly_v0
      fit: partial
      reason: "Anchors optical alignment assembly concepts, but this module needs higher power laser scanning and calibrated motion control."
    - process_id: electronic_component_assembly_v0
      fit: supporting
      reason: "Relevant to controller, scanner-driver, sensor-interface, and power electronics subassemblies."
    - process_id: cooling_loop_basic_fabrication_v0
      fit: supporting
      reason: "Relevant to water/air cooling service interfaces, not the precision optical core."
    - process_id: sensor_calibration_v0
      fit: supporting
      reason: "Covers calibration concept for monitoring sensors, though scan-field calibration is more specialized."
    - process_id: calibration_basic_v0
      fit: supporting
      reason: "Generic anchor for measurement-system calibration and adjustment."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant to the mounting frame and optical interface surfaces after decomposition."
  abstraction_decision: substitute_process_family
  rationale: "The source item is a vendor-calibrated optomechatronic module; row conversion should defer local manufacture until scanner, optics, electronics, cooling, and calibration submodels exist."
  process_guardrails:
    tolerance: high
    surface_finish: high
    sealing_quality: review
    alignment_accuracy: high
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: laser beam scanning and focus control for additive manufacturing
  material: multi_material_optomechatronic_module_with_aluminum_sic_mirrors_optics_electronics_cooling_and_sensor_interfaces
  scale_or_capacity:
    mass_kg: 15.0
    bom_quantity: 1
    row_total_mass_kg: 15.0
    scale_class: large
  geometry_form: large_box_like_scanner_module_envelope_with_optical_and_service_interfaces
merge_pool:
  eligible: false
  functional_purpose_key: laser_beam_steering
  precision_guardrails:
    - optical_alignment
    - mirror_coating
    - scan_field_calibration
    - thermal_control
    - control_electronics
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Galvanometer scanner motors, coated mirrors, zoom/focus optics, and control electronics are specialized dependencies."
    - "Scan-field calibration and process-monitoring alignment require metrology beyond ordinary assembly."
    - "Mass may be 15 kg for the base module and higher if monitoring hardware is included."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred; decompose the optomechatronic scanner subsystem before any merge review."
kb_staging:
  proposed_item_id: null
  notes: "Do not assign a simple enclosure item ID; keep as precision module pending scanner/optics/electronics decomposition."
assumptions:
  - "Treat the row as the base AM-MODULE NEXT GEN unless later evidence confirms the optional monitoring unit is included."
  - "Use 15 kg as the planning mass and preserve the 20 kg possibility as an import risk."
  - "Treat the CAD as an envelope for integration, not a source for material closure."
unresolved:
  - "Whether RAYSPECTOR monitoring hardware is part of this row."
  - "Detailed mirror coating, galvo scanner, lens, electronics, and cooling sub-BOM."
  - "Calibration procedure, scan-field accuracy, and service requirements."
```
