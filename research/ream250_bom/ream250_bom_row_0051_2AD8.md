---
row_identity:
  item: 2AD8
  cad_file: 2AD8_part_8
  source_row_number: 51
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Small spherical rolling element for the top axis bearing set.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD8_part_8.step; research/ream250_bom/ream250_bom_row_0051_2AD8__views_2x2.png
    cited_fact_or_basis: "BOM row 51 names item 2AD8 as 'axis bearing top'; the matched STEP is one solid with a 4.95 x 4.95 x 4.95 mm bounding box, and the rendered preview shows a near-spherical ball."
    evidence_basis: bom_provided
  assumptions:
    - The repeated neighboring rows 2AD1 through 2ADB with the same description represent individual balls in the same top-axis bearing group.
  uncertainty_notes:
    - The BOM does not name the bearing assembly type or the race/cage that uses this ball.
mass:
  value_kg: 0.000499
  basis: "Per-unit mass for quantity 1. FreeCAD measured volume is 63.506 mm^3, or 6.3506e-8 m^3. Using the local steel density constant 7850 kg/m^3 gives 0.0004985 kg, rounded to 0.000499 kg."
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD8_part_8.step; kb/materials/properties.yaml; https://www.metal-ball.com/wp-content/uploads/2016/02/manufacturing-std.pdf
    cited_fact_or_basis: "CAD measures a 63.506 mm^3 spherical solid; local properties list generic steel density as 7850 kg/m^3; bearing balls are covered by standard families such as ISO 3290-1 and DIN 5401."
    evidence_basis: standard_part_convention
  assumptions:
    - The part is treated as a steel bearing ball because the BOM description and CAD sphere match a standard bearing-ball use.
  uncertainty_notes:
    - Assembly STEP material extraction returned only Generic with density 1000.0, so the CAD package does not provide a usable material-specific mass.
material:
  primary_material: bearing steel / chrome steel bearing-ball material family
  source:
    url_or_path: https://www.grw.de/files/grw/FINALE%20BILDDATEN/INFOTHEK/DOWNLOADS/BROSCHUEREN/EN/GRW_Bearing%20Materials_2023.pdf; https://www.metal-ball.com/wp-content/uploads/2016/02/manufacturing-std.pdf
    cited_fact_or_basis: "Standard precision ball-bearing material references identify chrome steel and stainless bearing steels for bearing balls, and manufacturing standards cover bearing steel balls under ISO 3290-1 / DIN 5401 classes."
    evidence_basis: standard_part_convention
  assumptions:
    - For KB planning, use the broad bearing-steel family rather than a specific grade because the BOM row has no manufacturer, grade, or product designation.
  uncertainty_notes:
    - The row-specific local STEP material is a placeholder, and targeted_web_search: queries '2AD8 axis bearing top reAM250', 'axis bearing top 2AD8_part_8', and '4.95 mm bearing ball material steel' found the BOM text and generic bearing-ball material examples, but no row-specific vendor material record.
how_to_make:
  summary: "Follow bearing-ball forming, hardening, grinding, lapping, polishing, and inspection"
  manufacturing_steps:
    - Select a standard steel bearing-ball size matching the CAD diameter near 4.95 mm.
    - For local manufacture, cut steel wire slug stock and cold-head or forge it into a ball blank.
    - Heat treat the blank for bearing hardness, then grind, lap, polish, and sort to the required ball grade.
    - Inspect diameter, roundness, and surface finish before installing it in the top-axis bearing group.
  source:
    url_or_path: https://www.metal-ball.com/wp-content/uploads/2016/02/manufacturing-std.pdf; https://www.grw.de/files/grw/FINALE%20BILDDATEN/INFOTHEK/DOWNLOADS/BROSCHUEREN/EN/GRW_Bearing%20Materials_2023.pdf
    cited_fact_or_basis: "Standard bearing-ball documents define ISO/DIN ball classes and bearing material families; the row has enough standard parameters for procurement planning only at the family/diameter level, not a complete grade designation."
    evidence_basis: standard_part_convention
  assumptions: []
  uncertainty_notes:
    - The exact tolerance grade, hardness, and corrosion-resistance requirement are not present in the BOM or CAD evidence.
kb_implications:
  - "item_granularity: simple_part - Model 2AD8 with the other 2AD top-axis rows as a reusable bearing ball part, not as a separate machine or assembly."
---

Research result for reAM250 BOM row 51.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0051_2AD8.md
source_research_sha256: "12c69eea5e8dc9f6d0c80a4e9a5ec611fa68ed43334edf6b91c5fe0be5c1f2b2"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the top-axis rolling element function, CAD-derived steel mass, bearing-steel material convention, bearing-ball manufacturing route, and spherical CAD geometry before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one solid spherical rolling element with no subparts; precision comes from material, heat treatment, roundness, and surface finish rather than assembly."
  proposed_subparts: []
process_abstraction:
  original_process_family: precision_bearing_ball_manufacture
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - stock_preparation
    - forming
    - heat_treatment
    - grinding_lapping
    - surface_finishing
    - dimensional_inspection
    - import_assumption
  candidate_existing_processes:
    - process_id: ball_bearing_machining_v0
      fit: partial
      reason: "Anchors current KB bearing-ball coverage, but it is a simplified placeholder for real precision ball production."
    - process_id: heat_treatment_hardening_v0
      fit: supporting
      reason: "Relevant to hardening bearing steel before final finishing."
    - process_id: precision_grinding_basic_v0
      fit: supporting
      reason: "Relevant to roundness, diameter, and surface finish control."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers basic dimensional checks; true ball grading would need tighter metrology later."
  abstraction_decision: substitute_process_family
  rationale: "Although the physical part is simple, bearing-ball closure is precision-intensive and should remain grouped with precision components until the bearing-manufacturing scope is reviewed."
  process_guardrails:
    tolerance: high
    surface_finish: high
    sealing_quality: not_applicable
    alignment_accuracy: high
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: rolling element for bearing load transfer
  material: bearing_steel
  scale_or_capacity:
    mass_kg: 0.000499
    bom_quantity: 1
    row_total_mass_kg: 0.000499
    scale_class: small
  geometry_form: spherical_bearing_ball_about_4_95mm_diameter
merge_pool:
  eligible: true
  functional_purpose_key: rolling_element
  precision_guardrails:
    - diameter
    - roundness
    - hardness
    - surface_finish
    - ball_grade
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Very low mass and high precision make local manufacture unattractive unless bearing production becomes a focused closure target."
    - "Tolerance grade and hardness are unknown but likely critical to bearing performance."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review; this row should merge with neighboring top-axis bearing balls if diameter and material match."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with adjacent bearing-ball rows before assigning a closure item ID."
assumptions:
  - "The sphere is a steel bearing ball used in the top-axis bearing group."
  - "Neighboring 2AD rows likely represent repeated instances of the same rolling element."
  - "CAD diameter is sufficient for Phase 1 scale matching but not for tolerance grade selection."
unresolved:
  - "Bearing assembly type, cage/race context, ball grade, and hardness requirement are not identified."
  - "Material grade remains broad bearing steel rather than a row-specific alloy."
```
