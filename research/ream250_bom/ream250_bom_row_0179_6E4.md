---
row_identity:
  item: "6E4"
  cad_file: "6E4_plate_back"
  source_row_number: 179
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin rear/back plate for the 6E powder-handling subassembly area; the CAD shows a flat, irregular stainless plate likely used as a cover, side boundary, or support plate behind adjacent 6E-series parts."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6E4_plate_back.step; research/ream250_bom/ream250_bom_row_0179_6E4__views_2x2.png"
    cited_fact_or_basis: "BOM row 179 lists item 6E4, quantity 1, CAD file 6E4_plate_back. FreeCAD measured one solid with a 35.75 x 118.50 x 1.00 mm bounding box. The rendered preview shows a very thin irregular plate form."
    evidence_basis: "bom_provided"
  assumptions:
    - "The filename suffix plate_back and neighboring 6E-series plate rows are interpreted as rear/back placement within the local assembly."
  uncertainty_notes:
    - "The row does not identify exact mating faces or fastener interfaces, so the specific assembly function is broad rather than a fully constrained mechanical role."
mass:
  value_kg: 0.0264
  basis: "FreeCAD volume 3298.009 mm^3 converted to 3.298009e-6 m^3 and multiplied by stainless steel density 8000 kg/m^3, giving 0.026384 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6E4_plate_back.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 3298.009 mm^3, area 6918.824 mm^2, and bounding box 35.75 x 118.50 x 1.00 mm. The assembly STEP material extractor matched 6E4_plate_back to Stainless Steel with density 8000.0. The local density table lists stainless_steel density_kg_per_m3: 8000."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished physical volume of the part."
    - "The assembly STEP stainless steel density is used directly for mass conversion."
  uncertainty_notes: []
material:
  primary_material: "stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product 6E4_plate_back to material Stainless Steel with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local material metadata gives a stainless steel family but not a specific alloy grade."
how_to_make:
  summary: "Make as a simple stainless sheet-metal plate: cut the 1 mm thick outline from stainless sheet, add any CAD-defined edge/slot geometry, deburr, and clean/passivate if needed for powder-contact service."
  manufacturing_steps:
    - "Start from approximately 1 mm stainless steel sheet stock."
    - "Cut the irregular plate profile by laser cutting, waterjet cutting, or CNC routing/shearing followed by profile finishing."
    - "Deburr and smooth cut edges; verify outline and thickness against the CAD profile."
    - "Clean, passivate, or otherwise finish the stainless surface if the installed location contacts metal powder or process atmosphere."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6E4_plate_back.step; research/ream250_bom/ream250_bom_row_0179_6E4__views_2x2.png"
    cited_fact_or_basis: "The STEP geometry measures 1.00 mm thick with an irregular flat plate outline; the CAD preview shows a thin plate with no visible multi-part assembly features. targeted_web_search: searched \"6E4_plate_back reAM250 material manufacturing\", \"6E4 6E4_plate_back\", and \"reAM250 plate_back stainless steel\" found duplicate BOM text but no row-specific fabrication drawing or vendor manufacturing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A flat 1 mm stainless plate is best treated as a sheet-cut part rather than a machined block or external calibrated module"
    - "Deburring and cleaning are included because thin stainless powder-system plates commonly need edge cleanup and surface cleanliness."
  uncertainty_notes:
    - "No row-specific fabrication drawing was found, so cut method, edge tolerance, and finish requirements remain inferred from geometry."
kb_implications:
  - "item_granularity: simple_part - one thin stainless sheet-metal plate with a dominant sheet-cutting/deburring manufacturing route."
---

Research result for reAM250 BOM row 179.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0179_6E4.md
source_research_sha256: "59697cc7694688a12785a9ab0a7caa47cdeef5964204a137cb1a31956ec325d0"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed powder-handling back-plate function, 1 mm stainless sheet geometry, CAD-derived mass, material metadata, sheet-cutting route, and simple-part KB implication."
decomposition:
  decision: simple_part
  rationale: "The row is a single thin stainless sheet plate. Its closure-relevant features are outline cutting, edge cleanup, cleanliness, and fit in the 6E powder-handling area."
  proposed_subparts: []
process_abstraction:
  original_process_family: stainless_sheet_cutting_deburring_cleaning
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
    - cutting
    - deburring
    - surface_finishing
    - cleaning
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: sheet_metal_cutting_v0
      fit: direct
      reason: "Directly covers cutting a thin stainless sheet profile to the irregular CAD outline."
    - process_id: finishing_deburring_v0
      fit: supporting
      reason: "Relevant to edge cleanup on the 1 mm stainless profile before installation near powder-handling hardware."
    - process_id: cleaning_basic_v0
      fit: supporting
      reason: "Relevant to cleanliness for a stainless plate installed near powder-contact mechanisms."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers outline, thickness, and fit checks against neighboring 6E-series parts."
  abstraction_decision: keep_original_family
  rationale: "The source manufacturing route is already thin stainless sheet cutting, deburring, cleaning, and inspection, matching the sheet/plate cutting bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: low
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: rear boundary and support plate for powder-handling area hardware
  material: stainless_steel
  scale_or_capacity:
    mass_kg: 0.0264
    bom_quantity: 1
    row_total_mass_kg: 0.0264
    scale_class: small
  geometry_form: thin_irregular_flat_sheet_plate
merge_pool:
  eligible: true
  functional_purpose_key: powder_containment
  precision_guardrails:
    - powder_area_cleanliness
    - edge_burr_control
    - outline_fit
    - stainless_material_family
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Powder-contact cleanliness and burr control may need stricter finishing than ordinary sheet covers."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this powder-handling back plate with nearby stainless powder containment and guide plates."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable as a small stainless powder-containment sheet plate with row-specific outline notes."
assumptions:
  - "The assembly STEP stainless steel material assignment is reliable enough for row conversion."
  - "The 6E powder-handling context makes powder containment a better merge key than generic enclosure barrier."
unresolved:
  - "Specific stainless grade, edge tolerance, and surface passivation requirements are not resolved."
  - "Exact mating interfaces and fastener pattern are not specified by the row evidence."
```
