---
row_identity:
  item: "17A4"
  cad_file: "17A4_strut_profile_20X20_463"
  source_row_number: 223
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Cut length of Bosch Rexroth 20 mm strut/profile extrusion used as a lightweight structural rail or frame member in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A4_strut_profile_20X20_463.step; research/ream250_bom/ream250_bom_row_0223_17A4__views_2x2.png; https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
    cited_fact_or_basis: "BOM row 223 identifies item 17A4 as quantity 2, CAD file 17A4_strut_profile_20X20_463, description 'strut profile', manufacturer Bosch Rexroth AG. FreeCAD measured a 463.7 x 20.0 x 20.0 mm single solid, and the rendered preview shows a long square slotted extrusion profile."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents one cut-to-length strut profile per physical item; the BOM quantity of 2 means two identical profiles."
  uncertainty_notes:
    - "The BOM URL is a product-family route rather than a row-specific configured length page, so exact catalog article number is not locked beyond the CAD length and BOM identity."
mass:
  value_kg: 0.207
  basis: "Per unit: FreeCAD volume 76,797.555 mm^3 = 0.000076797555 m^3; assembly STEP metadata density for this product is 2700 kg/m^3; mass = 0.207353 kg, rounded to 0.207 kg. BOM quantity is 2, so row total is about 0.415 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A4_strut_profile_20X20_463.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD shape read reported 1 solid, volume 76,797.555 mm^3, area 84,268.444 mm^2, and bounding box 463.7 x 20.0 x 20.0 mm. Local assembly STEP material extraction for product 17A4_strut_profile_20X20_463 returned material Aluminum 6061 with density 2700.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported CAD solid volume is treated as the volume of one physical BOM-row profile."
    - "The STEP material density is treated as kg/m^3-like, consistent with the extractor note for the reAM250 export."
  uncertainty_notes:
    - "Small CAD export or tessellation differences could shift the mass slightly, but the result is within the precision needed for BOM planning."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 17A4_strut_profile_20X20_463 returned material Aluminum 6061 and density 2700.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row uses the material metadata attached to the full assembly product definition rather than any generic material placeholder in the standalone STEP."
  uncertainty_notes:
    - "The Bosch strut-profile family is commonly sold as anodized aluminum, but the row-specific local metadata does not separately specify anodized surface finish or temper."
how_to_make:
  summary: "Prepare as a Bosch Rexroth modular aluminum strut profile cut to the CAD length, or locally make by extruding a 20 x 20 mm slotted aluminum profile, cutting to about 463.7 mm, deburring, and applying a protective/anodized finish if needed"
  manufacturing_steps:
    - "Extrude Aluminum 6061 billet through a die matching the 20 x 20 mm slotted profile cross-section."
    - "Cut the extrusion to the CAD length of about 463.7 mm."
    - "Deburr cut ends and inspect slot geometry, straightness, and length."
    - "Apply anodized or equivalent corrosion-resistant finish if the installed environment requires the standard Bosch-style finish."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17A4_strut_profile_20X20_463.step; research/ream250_bom/ream250_bom_row_0223_17A4__views_2x2.png; https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
    cited_fact_or_basis: "BOM row identifies a Bosch Rexroth AG strut profile; CAD and preview show a long 20 x 20 mm slotted extrusion. targeted_web_search: tried 'Bosch Rexroth strut profile 20x20 aluminum 6061 profile'; usable results matched the Bosch Rexroth 20x20 anodized aluminum strut-profile product family, but did not state a row-specific manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A slotted constant-cross-section aluminum profile is best produced as an extrusion and then cut to length."
  uncertainty_notes:
    - "The detailed die design, alloy temper, and finish specification are not provided by the row evidence."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable cut-to-length aluminum structural profile, with length captured in BOM/recipe notes rather than as a calibrated purchased module."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0223_17A4.md
source_research_sha256: "f19848c508f48ef336e4827f88ddba1797839ba9585e4825d8d563f246352b90"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed strut-profile function, per-unit and row-total mass basis, Aluminum 6061 material metadata, extrusion/cut-to-length route, and CAD preview showing a long 20x20 slotted profile."
decomposition:
  decision: simple_part
  rationale: "The row is two identical cut aluminum profile segments with no internal module structure."
  proposed_subparts: []
process_abstraction:
  original_process_family: aluminum_extrusion_cut_to_length
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - extrusion
    - cutting
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: metal_extrusion_process_v0
      fit: partial
      reason: "Represents aluminum extrusion from ingot to profile stock, but current bindings are heat-sink-specific rather than generic strut stock."
    - process_id: metal_cutting_basic_v0
      fit: supporting
      reason: "Covers cutting metal stock to the required profile length."
    - process_id: surface_treatment_anodizing_v0
      fit: supporting
      reason: "Relevant if merge review preserves anodized aluminum finish as a functional requirement."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers length, straightness, and slot-geometry checks before frame assembly."
  abstraction_decision: keep_original_family
  rationale: "The source route is already a structural aluminum extrusion workflow; the closure abstraction keeps that family and defers exact profile consolidation to merge review."
  process_guardrails:
    tolerance: low
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: low
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: light structural rail member for modular fastening in the frame
  material: aluminum_alloy_6061
  scale_or_capacity:
    mass_kg: 0.207
    bom_quantity: 2
    row_total_mass_kg: 0.415
    scale_class: small
  geometry_form: cut_20x20_slotted_t_slot_extrusion_profile_464mm
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - slot_geometry
    - cut_length
    - straightness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
  import_risk_factors:
    - "Requires an extrusion die and reusable profile-forming capability for the 20x20 slotted section."
  post_merge_decision_notes: "Final import/local decision is deferred until after merge review; compare with other small aluminum profile rows before assigning a closure item."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely merge candidate with other 20x20 aluminum slotted profile lengths."
assumptions:
  - "Aluminum 6061 metadata is sufficient for row conversion despite unresolved temper and finish."
  - "The two BOM units can share one closure item with quantity two."
  - "Length variation should remain a BOM/recipe parameter unless merge review finds a precision reason for separate items."
unresolved:
  - "Exact Bosch article number, alloy temper, surface finish, and installed load path are not specified."
```
