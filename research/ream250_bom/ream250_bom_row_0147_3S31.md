---
row_identity:
  item: "3S31"
  cad_file: "3S31_part_1"
  source_row_number: 147
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom gas outlet pipe segment for the reAM250 gas-handling path; the CAD shows a short hollow square duct/transition piece that likely carries or guides outlet gas from one section of the gas outlet assembly to the next."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S31_part_1.step; research/ream250_bom/ream250_bom_row_0147_3S31__views_2x2.png"
    cited_fact_or_basis: "BOM row 147 lists item 3S31, quantity 1, CAD file 3S31_part_1, and description 'gas outlet pipe: part 1'. The manifest maps row 147 to one matched_existing part STEP. FreeCAD measured one solid with bounding box 60.00 x 60.00 x 115.00 mm; the rendered preview shows a hollow square duct-like part."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted as one segment of the neighboring 3S31-3S35 gas outlet pipe group rather than a standalone commercial pipe fitting."
  uncertainty_notes:
    - "The CAD/BOM evidence identifies the gas outlet role and duct-like geometry, but not the exact mating interfaces or flow direction."
mass:
  value_kg: 0.381
  basis: "Per-unit mass for quantity 1. FreeCAD volume is 47594.147 mm^3 = 4.7594147e-5 m^3. Using a stainless-steel planning density of 8000 kg/m^3 from kb/materials/properties.yaml gives 4.7594147e-5 m^3 x 8000 kg/m^3 = 0.38075 kg, rounded to 0.381 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S31_part_1.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 47594.147 mm^3, area 48560.377 mm^2, and bounding box 60.00 x 60.00 x 115.00 mm. Local assembly STEP material extraction for 3S31_part_1 returned only placeholder material Generic with density 1000.0. The local density table lists stainless_steel density_kg_per_m3: 8000. targeted_web_search: searched 'Renishaw AM250 gas outlet pipe material', 'Renishaw AM250 gas outlet pipe 3S31', and 'Renishaw AM250 chamber gas outlet pipe'; results did not provide a row-specific material or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is treated as the physical material volume for one gas outlet pipe segment."
    - "Stainless steel is used as the planning-density material because this is a rigid internal gas/outlet part in a metal powder-bed machine and no real material metadata was available."
  uncertainty_notes:
    - "Mass depends mainly on the unresolved material; if the part is aluminum rather than stainless steel, the same CAD volume would imply about 0.129 kg."
material:
  primary_material: "unknown metal/alloy sheet or thin-wall duct material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0147_3S31__views_2x2.png; web targeted search"
    cited_fact_or_basis: "BOM row 147 identifies the part as 'gas outlet pipe: part 1' but provides no material, manufacturer, product ID, or link URL. Local assembly STEP material extraction for 3S31_part_1 returned only placeholder material Generic with density 1000.0. The rendered preview shows a rigid hollow square duct-like segment. targeted_web_search: searched '3S31 gas outlet pipe reAM250 material', '3S31_part_1 gas outlet pipe material', and 'Renishaw AM250 gas outlet pipe material'; results did not resolve row-specific material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Model as a metal/alloy duct part because the CAD is a rigid thin-wall gas-path component and adjacent BOM rows are gas outlet pipe segments."
  uncertainty_notes:
    - "No source resolves the alloy family, grade, coating, or whether the part is stainless steel, aluminum, or another metal; downstream KB modeling should keep the material broad until an original drawing or CAD material note is available."
how_to_make:
  summary: "Fabricate as a custom thin-wall metal duct segment, then clean and fit it into the larger gas outlet pipe assembly."
  manufacturing_steps:
    - "Cut sheet or thin plate blanks for the square duct walls, or start from square tube/duct stock close to the 60 mm section."
    - "Form or fixture the walls to the CAD geometry and join seams by welding, brazing, or equivalent sealed metal joining."
    - "Trim or machine the ends to the 115 mm length and required mating geometry."
    - "Deburr, clean, and inspect the internal passage and external interfaces before assembly with neighboring gas outlet pipe parts."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S31_part_1.step; research/ream250_bom/ream250_bom_row_0147_3S31__views_2x2.png; web targeted search"
    cited_fact_or_basis: "FreeCAD measured a 60.00 x 60.00 x 115.00 mm one-solid part. The rendered preview shows a hollow square duct-like geometry without visible standard fitting, shaft, electronics, or calibrated module features. targeted_web_search: searched '3S31 gas outlet pipe reAM250 manufacturing', '3S31_part_1 drawing', 'Renishaw AM250 gas outlet pipe material', and 'Renishaw AM250 chamber gas outlet pipe'; results did not provide a row-specific fabrication drawing or manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A sheet-metal or tube-stock fabrication route is used because the geometry is a short hollow duct segment with a square section."
    - "Final sealing, fasteners, and alignment are handled at the larger gas outlet pipe assembly level."
  uncertainty_notes:
    - "The exact process may differ if the original part was machined, printed, or made from a proprietary duct extrusion; no drawing or process note was found."
kb_implications:
  - "item_granularity: simple_part - Model as one reusable custom fabricated gas outlet pipe segment; keep the material as broad metal/alloy until alloy evidence is available."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0147_3S31.md
source_research_sha256: "77e10a25960d0178b12d2feb33140b34469fa016b42bf2cf0a3d2590be2a8aee"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the row function, CAD-derived mass basis, unresolved metal/alloy material evidence, inferred thin-wall duct fabrication route, and preview evidence showing a hollow square gas outlet segment."
decomposition:
  decision: simple_part
  rationale: "The row is one duct-like pipe segment in a gas outlet group; no internal module decomposition is needed before merge review."
  proposed_subparts: []
process_abstraction:
  original_process_family: sheet_metal_tube_duct_fabrication
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - cutting
    - forming
    - joining
    - deburring
    - cleaning
    - dimensional_inspection
    - leak_testing
  candidate_existing_processes:
    - process_id: sheet_metal_fabrication_v0
      fit: partial
      reason: "Covers cutting, forming, and punching style work for thin metal parts, but lacks gas-path cleanliness and sealed seam requirements."
    - process_id: tube_stock_forming_v0
      fit: supporting
      reason: "Relevant if square tube stock is the starting form for the duct segment."
    - process_id: welding_brazing_basic_v0
      fit: supporting
      reason: "Covers sealed metal joining if the duct is built from sheet blanks."
    - process_id: plumbing_and_pneumatics_v0
      fit: partial
      reason: "Covers gas-handling installation and fitting work, but this row is a fabricated duct component rather than a full plumbing assembly."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Relevant if the segment contains welded seams that must be checked before integration into the gas outlet path."
    - process_id: cleaning_basic_v0
      fit: supporting
      reason: "Supports cleaning of the internal passage before assembly into powder-machine gas handling."
  abstraction_decision: substitute_process_family
  rationale: "The original evidence is a custom gas outlet pipe segment; closure analysis should treat it as a fabricated plumbing/gas-path component with joining and cleanliness guardrails instead of a vendor-specific part."
  process_guardrails:
    tolerance: standard
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: standard
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: gas outlet path segment guiding process gas between adjacent outlet assembly sections
  material: metal_alloy_unresolved
  scale_or_capacity:
    mass_kg: 0.381
    bom_quantity: 1
    row_total_mass_kg: 0.381
    scale_class: small
  geometry_form: short_hollow_square_duct_segment
merge_pool:
  eligible: true
  functional_purpose_key: gas_flow_path
  precision_guardrails:
    - internal_cleanliness
    - seam_integrity
    - mating_interface_fit
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "Material family is unresolved, so stainless versus aluminum selection can change mass and fabrication route."
    - "Gas-path cleanliness may matter in the powder-bed environment."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this piece with neighboring gas outlet pipe segments."
kb_staging:
  proposed_item_id: null
  notes: "Hold final item identity for merge review across the gas outlet pipe segment family."
assumptions:
  - "The row is treated as a rigid metal duct component using the 0.381 kg stainless planning mass from the research file."
  - "Sealing requirements are lower confidence than the geometric gas-path role because no drawing callouts were available."
unresolved:
  - "Actual alloy, coating, seam method, and required leak rate are unknown."
  - "Mating interfaces to adjacent 3S31-3S35 gas outlet rows need group review before final staging."
```
