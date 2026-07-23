---
row_identity:
  item: "2AF1"
  cad_file: "2AF1_track"
  source_row_number: 57
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.kuc-maschinen.de/produkt/linear-glasmassstaebe/"
function:
  summary: "Track/body of a K+C linear optical glass measuring scale for the reAM250 axis, providing a protected precision position reference over a 520 mm measuring range."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.kuc-maschinen.de/produkt/linear-glasmassstaebe/"
    cited_fact_or_basis: "BOM row 57 identifies item 2AF1 as K+C 'measuring range 520 mm: track'. The manifest maps it to 2AF1_track.step. K+C describes the product family as a linear optical measuring system based on a glass scale read by a read head and used for machine and plant engineering."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM word 'track' is treated as the installed linear scale track/body rather than the separate display electronics."
  uncertainty_notes:
    - "The row CAD contains the long scale body only; the complete commercial scale may also include read head, cable, mounting hardware, and protective angle hardware."
mass:
  value_kg: 0.99
  basis: "Per-unit estimate for quantity 1. FreeCAD measured one solid with volume 365696.325 mm^3 and bounding box about 20.00 x 28.50 x 644.00 mm. Using the local aluminum density constant 2700 kg/m^3 gives 365696.325 mm^3 * 1e-9 m^3/mm^3 * 2700 kg/m^3 = 0.987 kg, rounded to 0.99 kg. The row total is also about 0.99 kg. A row-matched distributor page lists 3.1 kg shipping weight for K+C M5/0500, treated only as a packaged upper-bound sanity check."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AF1_track.step; kb/materials/properties.yaml; https://www.top-maschinen.de/k-c-glasmassstab-m5-500-mm-5-m-verfahrweg-520-mm-810012.html"
    cited_fact_or_basis: "FreeCAD measured CAD volume 365696.325 mm^3 and bbox 20.00 x 28.50 x 644.00 mm. kb/materials/properties.yaml lists aluminum density 2700 kg/m^3. The distributor product page for K+C M5 500 mm / travel 520 mm lists shipping weight 3.1 kg and dimensions near the CAD length. bom_url_route_check: original BOM URL https://www.kuc-maschinen.de/produkt/linear-glasmassstaebe/ confirms product family/materials but did not expose a net item mass; a different-domain distributor was used only for row-match and shipping-weight sanity check. targeted_web_search: tried 'site:kuc-maschinen.de K+C Glasmassstaebe Gewicht M5 520 mm', 'K+C Glasmassstaebe Gewicht 520', and 'linear glass scale aluminum housing weight 520 mm K+C M5'; no row-specific net mass source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid volume is treated as a usable per-unit volume proxy for the row item."
    - "The aluminum housing dominates the modeled CAD volume; small glass, seal, cable, and reader components are not split into separate volume fractions."
  uncertainty_notes:
    - "STEP material metadata for this row is only Generic, and no net catalog weight was found; the estimate may miss internal glass/electronics/cable mass or CAD simplification differences."
material:
  primary_material: "aluminum housing with glass scale, elastomer sealing lips, read-head hardware/electronics, cable, metal protective sleeve, and connector"
  source:
    url_or_path: "https://www.kuc-maschinen.de/produkt/linear-glasmassstaebe/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "K+C states the system is based on a glass scale with optical scaling, protected in a robust aluminum housing with sealing lips. Local assembly STEP material extraction for 2AF1_track returned only Generic with density 1000.0, so it does not resolve material."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Exact aluminum grade, glass composition, seal elastomer, connector metal, and cable jacket material are not specified by the BOM-side evidence."
how_to_make:
  summary: "Fabricate the aluminum scale housing/profile, install the glass scale, read-head carriage, seals, cable, connector, and protective sleeve, then laser-measure/calibrate the assembly"
  manufacturing_steps:
    - "For local manufacture, extrude or machine the long aluminum housing/profile and cut it to the required scale length."
    - "Install the optical glass scale, read-head carriage or interface hardware, sealing lips, cable, DIN-style connector, and protective sleeve."
    - "Perform precision alignment, laser measurement/calibration, sealing, electrical testing, and functional verification before installation."
  source:
    url_or_path: "https://www.kuc-maschinen.de/produkt/linear-glasmassstaebe/; https://www.top-maschinen.de/k-c-glasmassstab-m5-500-mm-5-m-verfahrweg-520-mm-810012.html; research/ream250_bom/ream250_bom_row_0057_2AF1__views_2x2.png"
    cited_fact_or_basis: "K+C describes glass scale optical measurement, aluminum housing, sealing lips, laser measurement/calibration, read-head carriage, 3 m data cable, and connector. The row-matched distributor identifies MPN M5/0500, 500 mm nominal length, 520 mm travel, and a ready-wired scale. CAD preview shows a long narrow profiled rail/scale body. bom_url_route_check: the original BOM URL resolved product-family construction and calibration facts but not the exact MPN; the distributor page was used for the exact 520 mm product identity. targeted_web_search: tried 'K+C Glasmassstab M5 manufacturing aluminum housing glass scale' and found product/construction descriptions, not a detailed factory process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Manufacturing requires precision metrology and calibration comparable to commercial linear encoder production."
    - "The CAD track profile can be produced by extrusion plus finish machining or by direct machining at low quantity."
  uncertainty_notes:
    - "No source found gives K+C's detailed manufacturing process or calibration fixture design, so The manufacturing route is a high-level engineering plan rather than a sourced process recipe."
kb_implications:
  - "item_granularity: complex_module - Treat as a calibrated functional linear encoder/scale complex module for this pass; later KB work should only decompose it after modeling optical scale fabrication, read-head electronics, sealing, cabling, and calibration."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0057_2AF1.md
source_research_sha256: "bcfa9bbc0b17b2c75c447330226fe7127acd0d12f827f9bc4d34aa296151e6f6"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read linear-position reference function, CAD-volume aluminum mass estimate, multi-material scale evidence, assembly/calibration route, KB implication, and preview of the long scale track."
decomposition:
  decision: complex_module
  rationale: "The row is a calibrated linear encoder/scale module, not merely an aluminum rail; closure depends on optical glass scale fabrication, read-head hardware, seals, cabling, and calibration."
  proposed_subparts:
    - aluminum_scale_housing
    - optical_glass_scale
    - read_head_hardware_and_electronics
    - elastomer_sealing_lips
    - cable_and_connector
    - protective_sleeve
process_abstraction:
  original_process_family: calibrated_linear_optical_scale_assembly
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - extrusion
    - precision_machining
    - assembly
    - cleaning
    - calibration
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: precision_scale_fabrication_v0
      fit: partial
      reason: "Anchors high-accuracy encoder scale patterning and inspection, a key dependency hidden inside the commercial module."
    - process_id: sensor_integration_v0
      fit: supporting
      reason: "Relevant to integrating read-head hardware, cabling, and mechanical scale body."
    - process_id: sensor_calibration_v0
      fit: supporting
      reason: "Covers calibration/verification concept, though this row likely needs optical metrology beyond basic sensor calibration."
    - process_id: electronic_component_assembly_v0
      fit: supporting
      reason: "Relevant to read-head electronics if the module is decomposed."
    - process_id: metal_extrusion_process_v0
      fit: supporting
      reason: "Potential route for the long aluminum housing/profile before precision finishing."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for mounting surfaces and scale alignment features."
  abstraction_decision: substitute_process_family
  rationale: "The commercial product route is a calibrated sensor module; row conversion should not collapse it into a simple machined rail, so the precision-component/decompose-later bucket is the correct closure handle."
  process_guardrails:
    tolerance: high
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: high
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: linear position feedback and precision reference for a machine axis
  material: aluminum_housing_with_glass_scale_elastomer_seals_read_head_electronics_cable_and_connector
  scale_or_capacity:
    mass_kg: 0.99
    bom_quantity: 1
    row_total_mass_kg: 0.99
    scale_class: medium
  geometry_form: long_protected_linear_scale_track_about_520_mm_measuring_range
merge_pool:
  eligible: false
  functional_purpose_key: linear_position_feedback
  precision_guardrails:
    - optical_scale_accuracy
    - calibration_traceability
    - read_head_integration
    - seal_integrity
    - cable_connector_interface
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Optical glass scale patterning and read-head electronics are specialized closure dependencies."
    - "Laser measurement/calibration infrastructure is required by the source evidence."
    - "Internal material split is unresolved because CAD represents the track body only."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred; first decompose the module into housing, optical scale, read-head electronics, sealing, cabling, and calibration dependencies."
kb_staging:
  proposed_item_id: null
  notes: "Do not assign a simple rail item ID before decomposition; merge review should not group this solely by the aluminum track geometry."
assumptions:
  - "Use 0.99 kg as a CAD-volume aluminum-housing dominated estimate, with missing internal component mass noted."
  - "Treat the 520 mm measuring range and optical calibration evidence as closure-critical."
  - "Treat this as a complex precision sensor module despite the simple track-like CAD preview."
unresolved:
  - "Exact glass scale material, patterning method, and accuracy class."
  - "Read-head electronics, cable, connector, and seal material breakdown."
  - "Calibration fixture, reference metrology, and acceptance procedure."
```
