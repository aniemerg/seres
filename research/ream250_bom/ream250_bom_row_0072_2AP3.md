---
row_identity:
  item: "2AP3"
  cad_file: "2AP3_heating_plate"
  source_row_number: 72
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom square heating/distribution plate in the 2AP build-platform stack, providing a broad heated interface near the lifting platform, seals, pressing plate, build platform, and PT100 temperature sensor rows."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0072_2AP3__views_2x2.png"
    cited_fact_or_basis: "BOM row 72 names item 2AP3 as 2AP3_heating_plate with quantity 1; neighboring rows 70-88 contain spring/assembly plates, fasteners, seals, lifting_platform, temperature_sensor, pressing_plate, felt_seal, and build_platform; CAD preview shows one thin square plate-like part."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD/BOM name is interpreted literally as a heating plate rather than an unrelated structural cover."
  uncertainty_notes:
    - "The package does not show the full 2AP assembly hierarchy in this result, so exact stack position and heat-transfer direction remain approximate."
mass:
  value_kg: 1.63
  basis: "FreeCAD measured one solid with volume 601865.420 mm^3, area 153803.114 mm^2, and bounding box 250.00 x 15.00 x 250.00 mm. Per-unit mass estimate uses volume 0.000601865 m^3 times the local aluminum density constant 2700 kg/m^3 from kb/materials/properties.yaml, giving 1.625 kg, rounded to 1.63 kg for one row item; BOM quantity is 1, so row total is also about 1.63 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP3_heating_plate.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD geometry command measured volume and 250.00 x 15.00 x 250.00 mm bounding box; kb/materials/properties.yaml lists aluminum density 2700 kg/m^3. targeted_web_search: queries tried: \"2AP3 heating_plate reAM250\", \"2AP3 heating plate reAM250\", \"reAM250 heating plate 2AP3\", and \"reAM250 2AP3\"; result: only the reAM250 BOM row or generic hot-plate pages were found, with no row-specific mass or material specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Aluminum-family density is used as the planning mass case because a heating/distribution plate benefits from high thermal conductivity and low moving-stack mass."
  uncertainty_notes:
    - "Assembly STEP material extraction returned only placeholder material Generic with density 1000.0, so it does not resolve mass; if the plate is generic steel at 7850 kg/m^3, the same CAD volume would imply about 4.72 kg."
material:
  primary_material: "unknown thermally conductive metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row name is 2AP3_heating_plate, but the material-family and specific-grade columns are empty; assembly STEP material extraction for product 2AP3_heating_plate returned Generic with density 1000.0. targeted_web_search: queries tried: \"2AP3 heating_plate reAM250 material\", \"2AP3 heating plate reAM250 aluminum\", and \"reAM250 2AP3 material\"; result: no row-specific material or grade was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Treat as a metal/alloy plate for later KB planning because the CAD is a rigid machined plate and the row's function is heating rather than sealing or insulation."
  uncertainty_notes:
    - "Do not encode aluminum or steel as sourced material for this row; the current evidence only supports a broad conductive-metal family."
how_to_make:
  summary: "Manufacture as a custom flat metal plate: prepare conductive plate stock, CNC mill the pocketed/ribbed geometry and perimeter features from the CAD, deburr, flatten/finish contact faces, clean, and assemble into the 2AP platform stack with the adjacent fasteners, seals, sensor, and platform hardware"
  manufacturing_steps:
    - "Cut a square blank from metal plate stock sized for the 250 mm square by 15 mm envelope."
    - "CNC mill the recessed/ribbed plate geometry and any edge or fastener-interface features indicated by the STEP model."
    - "Deburr and finish the broad contact faces for stable thermal contact."
    - "Clean and install with the neighboring 2AP fasteners, seals, pressing/build-platform parts, and temperature sensor."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP3_heating_plate.step; research/ream250_bom/ream250_bom_row_0072_2AP3__views_2x2.png"
    cited_fact_or_basis: "CAD geometry and preview show a single thin square machined plate-like part with a 250.00 x 15.00 x 250.00 mm envelope and pocketed/ribbed faces. targeted_web_search: queries tried: \"2AP3 heating_plate reAM250 manufacturing\", \"2AP3 heating plate reAM250 drawing\", and \"reAM250 2AP3 heating plate\" result: no row-specific drawing, vendor process, or manufacturing note was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "CNC machining from plate stock is chosen as the plausible route for a one-off custom reAM250 mechanical plate with broad flat faces and machined recesses."
  uncertainty_notes:
    - "The STEP preview is visual triage only; exact tolerances, surface finish, heat-treatment, coating, embedded heater attachment, and interface datums are not specified in the BOM row."
kb_implications:
  - "item_granularity: simple_part - Model as one custom machined conductive plate rather than a purchased module; keep heater electronics or sensors as separate rows/items."
---
## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0072_2AP3.md
source_research_sha256: "4ddc84f4cfa43544970b6ac28dd110e9d013187a9e7a8cec975c34010a163d45"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed function in the 2AP build-platform stack, aluminum-density planning mass, unresolved conductive-metal material evidence, CNC plate manufacturing route, and CAD preview showing a square pocketed plate."
decomposition:
  decision: simple_part
  rationale: "The row is one custom conductive plate; heater electronics, seals, sensor, and fasteners are separate neighboring rows rather than subparts of this plate."
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_machined_conductive_plate
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - deburring
    - surface_finishing
    - cleaning
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_process_milling_v0
      fit: partial
      reason: "Covers milling pockets, ribs, perimeter features, and interface faces from conductive plate stock."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant if platform flatness, sensor contact, and stack alignment require tighter datum control."
    - process_id: surface_finishing_basic_v0
      fit: supporting
      reason: "Covers face finishing needed for stable thermal contact and clean assembly."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers checks of plate thickness, flatness, pocket geometry, and fastener interfaces."
  abstraction_decision: keep_original_family
  rationale: "The original route is already a custom machined plate from stock; the lunar closure abstraction can reuse a general subtractive machining bucket while preserving thermal-contact guardrails."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: heated distribution interface in the build-platform stack
  material: thermally_conductive_metal
  scale_or_capacity:
    mass_kg: 1.63
    bom_quantity: 1
    row_total_mass_kg: 1.63
    scale_class: medium
  geometry_form: square_machined_plate_with_pockets_and_broad_contact_faces
merge_pool:
  eligible: true
  functional_purpose_key: heat_distribution
  precision_guardrails:
    - flatness
    - thermal_contact_surface_finish
    - stack_alignment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Material is unresolved; conductive metal choice affects thermal performance and final mass."
    - "Broad contact face flatness may require precision machining and inspection beyond rough plate cutting."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups thermal plates and resolves material plus precision requirements."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; candidate for a reusable thermal distribution plate closure item if material and face-quality requirements converge."
assumptions:
  - "Aluminum-density mass is retained as a planning estimate, while identity material remains broad conductive metal due missing source grade."
  - "The plate does not include embedded heaters; adjacent heating, sensing, sealing, and fastening rows remain separate closure items."
unresolved:
  - "Exact alloy, coating, heat treatment, and working temperature are not specified."
  - "Flatness, surface finish, and datum tolerances for thermal contact in the 2AP stack remain unknown."
```
