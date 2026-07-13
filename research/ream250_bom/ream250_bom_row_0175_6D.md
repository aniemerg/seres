---
row_identity:
  item: "6D"
  cad_file: "6D_rod_sleeve"
  source_row_number: 175
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small stainless rod sleeve or bushing, likely used as a spacer, guide, or wear sleeve around a rod in the reAM250 mechanism."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6D_rod_sleeve.step; research/ream250_bom/ream250_bom_row_0175_6D__views_2x2.png"
    cited_fact_or_basis: "BOM row 175 names item 6D as 6D_rod_sleeve with quantity 1; FreeCAD measured one solid with about 815.309 mm^3 volume and a 10.91 x 12.00 x 14.00 mm bounding box; rendered views show a short cylindrical sleeve-like part with a larger collar/head. targeted_web_search: queries 'stainless steel rod sleeve bushing function manufacturing' and 'rod sleeve bushing stainless steel sleeve bearing function' found generic sleeve/bushing descriptions, not a row-specific source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD part name is interpreted literally: rod_sleeve is treated as a sleeve/bushing associated with a rod, not as an unrelated cover or cap."
  uncertainty_notes:
    - "The parent assembly context was not provided in the leased row, so the exact interface and load case remain uncertain."
mass:
  value_kg: 0.00652
  basis: "Per-unit mass for quantity 1. CAD volume 815.308552 mm^3 = 8.15308552e-7 m^3; assembly STEP material metadata gives Stainless Steel density 8000 kg/m^3, yielding 0.006522 kg per sleeve."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6D_rod_sleeve.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD shape read measured one solid, volume 815.309 mm^3, area 670.633 mm^2, and bounding box 10.91 x 12.00 x 14.00 mm; local assembly STEP material extraction matched product 6D_rod_sleeve to Stainless Steel with density 8000.0 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The matched CAD solid represents one physical item for BOM quantity 1."
    - "The STEP material density is applied uniformly to the measured CAD volume."
  uncertainty_notes:
    - "Mass does not include any separate coating, lubricant, or press-fit allowance that may exist outside the exported part solid."
material:
  primary_material: "Stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 6D_rod_sleeve returned material Stainless Steel and density 8000.0 in the reAM250 export's kg/m^3-like density convention."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata does not identify a stainless grade such as 304, 316, or hardened stainless."
how_to_make:
  summary: "Make as a small precision-machined stainless sleeve from bar stock"
  manufacturing_steps:
    - "Cut stainless bar or rod stock slightly oversize."
    - "Turn the outside diameter, collar/head, and end faces on a lathe."
    - "Drill and bore or ream the internal passage if the sleeve is hollow in the mating assembly."
    - "Add flats/chamfers or head features visible in CAD, deburr, clean, and inspect critical diameters."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6D_rod_sleeve.step; https://gjl8888.en.made-in-china.com/product/IXBxfvSKbiYm/China-Custom-Made-CNC-Turning-Stainless-Steel-Shaft-Sleeve-Bushing.html"
    cited_fact_or_basis: "CAD evidence shows a small sleeve-like stainless component with turned cylindrical features; the searched vendor example shows custom stainless shaft sleeve bushings are commonly made with CNC turning. targeted_web_search: query 'stainless steel rod sleeve bushing function manufacturing' found generic custom CNC-turned stainless sleeve/bushing routes, but no row-specific manufacturing drawing."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Lathe turning is the most plausible route because the part is mostly rotationally symmetric and only about 14 mm tall."
    - "Secondary machining is allowed for the non-axisymmetric flats or local features visible in the rendered preview."
  uncertainty_notes:
    - "No tolerances, surface finish, heat treatment, or internal bore specification were available in the BOM row or CAD evidence."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable small stainless machined sleeve/bushing rather than a machine-specific assembly or purchased module."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0175_6D.md
source_research_sha256: "99f48c436a123681df06a5461bc9cad5b00c52ca2440905f06757b8c66d05951"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed rod-sleeve function, small cylindrical CAD geometry with collar, stainless material metadata, CAD-derived mass, turning-based manufacturing route, and reusable sleeve/bushing KB implication."
decomposition:
  decision: simple_part
  rationale: "The row is one small stainless sleeve/bushing. Collar, bore, flats, chamfers, and end faces are integral machined features."
  proposed_subparts: []
process_abstraction:
  original_process_family: precision_turned_stainless_sleeve
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - deburring
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_process_turning_v0
      fit: direct
      reason: "Directly covers turning the small cylindrical sleeve, collar, and end faces from bar stock."
    - process_id: machining_process_boring_v0
      fit: supporting
      reason: "Relevant if the sleeve has an internal rod passage with controlled bore size."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant to bore fit, outside diameter, and wear-contact surfaces."
    - process_id: cutting_basic_v0
      fit: supporting
      reason: "Relevant to cutting stainless rod stock before turning."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers diameter, length, bore, and fit checks."
  abstraction_decision: keep_original_family
  rationale: "The source route is a lathe-turned stainless sleeve from bar stock with secondary feature cleanup, directly matching general subtractive machining."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: rod guidance and spacing sleeve for a machine mechanism
  material: stainless_steel
  scale_or_capacity:
    mass_kg: 0.00652
    bom_quantity: 1
    row_total_mass_kg: 0.00652
    scale_class: small
  geometry_form: short_turned_cylindrical_sleeve_with_collar
merge_pool:
  eligible: true
  functional_purpose_key: linear_guidance
  precision_guardrails:
    - bore_diameter
    - outside_diameter
    - wear_surface_finish
    - stainless_grade
    - rod_interface_fit
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Stainless grade, bore tolerance, and wear surface finish are unresolved."
    - "If the sleeve is a precision bearing surface, it may need stricter machining than an ordinary spacer."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this sleeve with other small rod guides, bushings, and spacers."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable as a small stainless machined sleeve/bushing closure item."
assumptions:
  - "The CAD name and geometry are sufficient to treat the row as a rod sleeve/bushing."
  - "Uniform stainless density from STEP metadata is acceptable for mass planning."
unresolved:
  - "Exact stainless grade, bore specification, load case, wear requirement, surface finish, heat treatment, and parent assembly interface remain unresolved."
```
