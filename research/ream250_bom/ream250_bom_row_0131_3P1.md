---
row_identity:
  item: "3P1"
  cad_file: "3P1_cyclone_separator"
  source_row_number: 131
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Cyclone separator vessel for removing entrained particulate or powder from a gas/process stream by tangential vortex flow; the CAD shows a tall conical cyclone body with side inlet, top outlet, and lower discharge."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0131_3P1__views_2x2.png; https://unitedstatessystems.com/cyclone-separator/"
    cited_fact_or_basis: "The BOM and manifest identify row 131 item 3P1 as quantity 1 of 3P1_cyclone_separator. The rendered CAD contact sheet shows a cyclone-like conical body with tangential side inlet, vertical top outlet, and bottom discharge. US Systems describes mechanical dust collector cyclones as using cyclonic airflow to separate particulates from an air stream, with particles moving to the walls and falling to a hopper while air exits upward."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row name and cyclone geometry indicate this separator handles powder/particulate carried in gas or vacuum flow in the reAM250 system."
  uncertainty_notes:
    - "The row evidence does not identify the exact particle size range, pressure drop, or capture efficiency."
mass:
  value_kg: 12.6
  basis: "FreeCAD measured CAD volume 1576521.047 mm^3 for one solid. Using the row-specific STEP material density 8000 kg/m^3 gives 1576521.047 mm^3 * 1e-9 m^3/mm^3 * 8000 kg/m^3 = 12.612 kg, rounded to 12.6 kg per unit. BOM quantity is 1, so the row total is also about 12.6 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P1_cyclone_separator.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 1576521.047 mm^3, area 652239.626 mm^2, and bounding box 320.13 x 183.08 x 788.00 mm. Local STEP material extraction for product 3P1_cyclone_separator found material Stainless Steel with density 8000.0. The local material density table lists stainless_steel density 8000 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported STEP solid volume is treated as the physical stainless steel volume of one cyclone separator."
    - "The STEP density value and the local stainless_steel density table are equivalent for this calculation."
  uncertainty_notes:
    - "The estimate depends on the supplied CAD solid including the relevant wall thickness and fittings; any omitted internal vanes, seals, clamps, or weld hardware would add mass."
material:
  primary_material: "stainless steel cyclone separator body"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 3P1_cyclone_separator returned row-specific material Stainless Steel with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata resolves the material family but not a specific stainless grade such as 304, 316, or 316L."
how_to_make:
  summary: "Model as a welded stainless cyclone vessel: prepare as a custom stainless cyclone separator, or locally fabricate from rolled/conical stainless sheet and tube with welded inlet, outlet, and discharge fittings, followed by cleaning and leak/fit inspection"
  manufacturing_steps:
    - "Cut stainless sheet blanks for the cylindrical upper body and tapered cone; cut tube or formed duct stock for the tangential inlet, top outlet, and lower discharge."
    - "Roll/form the cylindrical and conical shell sections to match the CAD envelope."
    - "Fit and weld the tangential inlet, top outlet tube, bottom discharge stub, and any mounting tabs or flanges visible in the CAD."
    - "Grind/deburr internal flow edges, clean the stainless surfaces, and passivate or otherwise finish as needed for powder/vacuum service."
    - "Inspect critical connection dimensions, weld integrity, and leak tightness before installation."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0131_3P1__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P1_cyclone_separator.step; https://unitedstatessystems.com/cyclone-separator/"
    cited_fact_or_basis: "The rendered CAD contact sheet shows a tall conical cyclone shell with tangential inlet, vertical outlet, bottom discharge, and small mounting/connection features. FreeCAD measured a bounding box of 320.13 x 183.08 x 788.00 mm. US Systems states that it manufactures standard cyclone separators and custom-engineers cyclones from stainless steel, aluminum, or painted carbon steel."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the stainless material, cyclone shell geometry, and common welded vessel/sheet-metal practice."
    - "Vacuum or powder handling service requires smooth cleaned internal surfaces and leak-tight welded joints."
  uncertainty_notes:
    - "The row evidence does not state the actual supplier's production process, weld procedure, wall thickness tolerance, pressure rating, or surface finish."
    - "Targeted_web_search: searched `cyclone separator stainless steel conical body tangential inlet manufacturing fabrication welding`; found general cyclone function/material/vendor manufacturing evidence but no row-specific 3P1 production specification."
kb_implications:
  - "item_granularity: simple_part - one custom stainless cyclone vessel/body with welded fittings; later KB modeling should treat it as a fabricated stainless separator body rather than a calibrated purchased module unless a vendor subsystem spec is found."
---

# reAM250 BOM Row 131 - 3P1

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0131_3P1.md
source_research_sha256: "4c9e364a03fd67a70c7aed944d1ccebd7c4f0e7c3b032dba1362d0f01574a052"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read function, mass basis, stainless material evidence, welded fabrication route, kb implications, and CAD preview showing a conical cyclone body with side inlet, top outlet, and lower discharge."
decomposition:
  decision: simple_part
  rationale: "The row is one fabricated cyclone separator body with welded fittings. It may later assemble with seals and ducting, but row evidence does not show a vendor control module, motor, sensor package, and internal mechanism requiring decomposition."
  proposed_subparts: []
process_abstraction:
  original_process_family: welded_stainless_sheet_and_tube_vessel_fabrication
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
    - stock_preparation
    - cutting
    - forming
    - joining
    - deburring
    - surface_finishing
    - cleaning
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: sheet_metal_fabrication_v0
      fit: partial
      reason: "Covers cutting and forming sheet stock into vessel sections, though the conical cyclone body also needs tube fittings and weld sequencing."
    - process_id: welded_fabrication_basic_v0
      fit: supporting
      reason: "Covers fit-up and welding of stainless sections and fittings into a single separator body."
    - process_id: pressure_testing_v0
      fit: supporting
      reason: "Relevant for leak and pressure checks before installation in a gas/powder flow path."
    - process_id: cleaning_basic_v0
      fit: supporting
      reason: "Relevant for removing fabrication residue before powder-contact service."
  abstraction_decision: substitute_process_family
  rationale: "The evidence describes a welded stainless cyclone vessel. For closure, the dominant path is sheet and tube fabrication with forming, welding, cleaning, and leak inspection rather than a unique separator-specific machine."
  process_guardrails:
    tolerance: review
    surface_finish: internal_flow_surface_review
    sealing_quality: leak_tight_review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: cyclone separation of particulate from a gas process stream
  material: stainless_steel_unspecified_grade
  scale_or_capacity:
    mass_kg: 12.6
    bom_quantity: 1
    row_total_mass_kg: 12.6
    scale_class: medium
  geometry_form: welded_conical_cyclone_vessel_with_tangential_inlet
merge_pool:
  eligible: true
  functional_purpose_key: particulate_separator
  precision_guardrails:
    - cyclone_geometry
    - internal_surface_finish
    - leak_tightness
    - connection_dimensions
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Capture efficiency, particle size range, wall thickness, pressure rating, and weld acceptance criteria are unresolved."
    - "If separation performance is calibrated tightly, later review may need vendor design data."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares separator bodies and decides whether a generic fabricated cyclone vessel is acceptable."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review before assigning an item ID; likely candidate family is a medium stainless particulate separator vessel."
assumptions:
  - "BOM quantity is 1, so row total mass equals the 12.6 kg per-unit estimate."
  - "The STEP density and preview justify treating the item as a stainless welded body rather than an electronics module."
  - "Powder-contact and gas-flow service require cleaned internal surfaces and leak checks."
unresolved:
  - "Specific stainless grade and wall thickness."
  - "Particle size range, pressure drop, and separation efficiency."
  - "Whether pressure/vacuum service requires stricter leak testing than basic pressure checks."
```
