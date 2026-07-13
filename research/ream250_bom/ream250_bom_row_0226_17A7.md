---
row_identity:
  item: "17A7"
  cad_file: "17A7_strut_profile_20X20_D50"
  source_row_number: 226
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Short 20 x 20 mm Bosch Rexroth strut-profile segment used as a structural or spacer/connector member in the reAM250 frame or subassembly; the four open slots accept matching profile fasteners and brackets."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A7_strut_profile_20X20_D50.step; research/ream250_bom/ream250_bom_row_0226_17A7__views_2x2.png"
    cited_fact_or_basis: "BOM row 226 identifies item 17A7 as quantity 1, description 'strut profile', manufacturer Bosch Rexroth AG. FreeCAD measured one solid with 50.00 x 20.00 x 20.00 mm bounding box, and the rendered preview shows a four-slot extrusion cross-section."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-specific CAD export represents the one physical profile segment in the BOM row."
  uncertainty_notes:
    - "The BOM and CAD do not state the exact mounting location, so the function is resolved at profile-member granularity rather than a specific frame joint."
mass:
  value_kg: 0.0224
  basis: "Per-unit mass for quantity 1. FreeCAD volume 8280.953 mm^3 = 8.280953e-6 m^3; assembly STEP material metadata reports density 2700 kg/m^3 for Aluminum 6061; 8.280953e-6 m^3 * 2700 kg/m^3 = 0.02236 kg. Optional row total is the same because quantity is 1."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A7_strut_profile_20X20_D50.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 8280.953 mm^3, area 9382.047 mm^2, and 50.00 x 20.00 x 20.00 mm bounding box. Local STEP material extraction for product 17A7_strut_profile_20X20_D50 returned material Aluminum 6061 and density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume is treated as the as-installed material volume for one BOM-row item."
    - "The STEP density is treated as kg/m^3-like metadata, consistent with the extraction script note for the reAM250 export."
  uncertainty_notes:
    - "Small CAD export simplifications or end-cut details could shift the mass slightly, but the estimate is within the precision needed for BOM planning."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local STEP material extraction for product 17A7_strut_profile_20X20_D50 returned material 'Aluminum 6061' with density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local metadata resolves the alloy family for this CAD row, but it does not separately specify surface treatment such as anodizing."
how_to_make:
  summary: "Prepare a Bosch Rexroth-compatible 20 x 20 mm aluminum strut profile segment, preferably cut to the 50 mm row length, then install it with the matching slot fasteners or brackets in the reAM250 assembly"
  manufacturing_steps:
    - "Cut a Bosch Rexroth 20 x 20 mm strut profile to 50 mm length"
    - "Deburr cut ends if cut from longer stock."
    - "Assemble through the four profile slots using compatible Bosch Rexroth profile connectors, sliding blocks, or brackets required by the surrounding assembly."
  source:
    url_or_path: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A7_strut_profile_20X20_D50.step"
    cited_fact_or_basis: "The BOM-provided Bosch Rexroth store route is for 'Strebenprofil' strut profiles, BOM row 226 names Bosch Rexroth AG and 'strut profile', and CAD fixes the row length and cross-section at 50.00 x 20.00 x 20.00 mm."
    evidence_basis: "bom_provided"
  assumptions:
    - "Cut-to-length stock preparation is the relevant route for this vendor extrusion row"
  uncertainty_notes:
    - "The exact connector set used with this short segment is outside this row and should be resolved from adjacent BOM rows or the parent assembly."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable 20 x 20 aluminum profile cut-length variant or parameterized stock segment, not as a machine-specific purchased module."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0226_17A7.md
source_research_sha256: "a4f72cd10265314525274dce0090d9ccfa65df9d0504565a761bf1bcd31d22e8"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed Bosch Rexroth strut-profile function, 50 mm cut-length CAD geometry, Aluminum 6061 material metadata, CAD-derived mass, cut-to-length route, and simple reusable profile KB implication."
decomposition:
  decision: simple_part
  rationale: "The row is one cut segment of an aluminum slotted profile. Slots and end cuts are integral profile geometry rather than separate subparts."
  proposed_subparts: []
process_abstraction:
  original_process_family: extruded_profile_cut_to_length
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - extrusion
    - cutting
    - deburring
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: extrusion_basic_v0
      fit: partial
      reason: "Covers generic extrusion of profile stock, though the Bosch-style four-slot cross-section would need a profile die and later staging detail."
    - process_id: aluminum_tube_stock_extrusion_v0
      fit: poor_fit
      reason: "Aluminum extrusion anchor is relevant by material and stock concept, but tube geometry differs from a slotted structural profile."
    - process_id: cutting_basic_v0
      fit: supporting
      reason: "Relevant to cutting longer profile stock to the 50 mm row length."
    - process_id: finishing_deburring_v0
      fit: supporting
      reason: "Relevant to deburring cut ends before assembly."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers length and cross-section fit checks."
  abstraction_decision: keep_original_family
  rationale: "The source route is aluminum profile stock cut to row length and deburred, directly matching structural profile stock fabrication and cutting."
  process_guardrails:
    tolerance: low
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: short structural profile member for frame spacing and modular attachment
  material: aluminum_6061
  scale_or_capacity:
    mass_kg: 0.0224
    bom_quantity: 1
    row_total_mass_kg: 0.0224
    scale_class: small
  geometry_form: short_20x20_four_slot_extruded_profile_segment
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - profile_cross_section
    - cut_length
    - slot_interface_compatibility
    - aluminum_6061_material
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
  import_risk_factors:
    - "Local extrusion of a Bosch-compatible four-slot profile needs a dedicated die and may be replaced by a simpler generic profile after merge review."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this short strut profile with other modular frame profile segments."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable as an aluminum structural profile cut-length variant."
assumptions:
  - "The row CAD represents one installed 50 mm profile segment."
  - "Aluminum 6061 STEP metadata is accepted for row conversion."
unresolved:
  - "Surface treatment, exact connector set, profile-interface tolerance, and whether a generic local profile can replace Bosch-style slots remain unresolved."
```
