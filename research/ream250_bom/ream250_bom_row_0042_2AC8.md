---
row_identity:
  item: "2AC8"
  cad_file: "2AC8_part_8"
  source_row_number: 42
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Sealed 6200.2RS deep-groove ball bearing used in the lower axis bearing support; it carries a 10 mm shaft while fitting a 30 mm outside-diameter, 9 mm wide bearing pocket in the bottom-axis-bearing assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC8_part_8.step; research/ream250_bom/ream250_bom_row_0042_2AC8__views_2x2.png; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127"
    cited_fact_or_basis: "BOM row 42 lists item 2AC8, quantity 1, CAD file 2AC8_part_8, description 'axis bearing bottom'. Manifest row 42 maps it to a matched part STEP. FreeCAD measured one solid with volume 3541.624 mm^3 and a 32.47 x 9.00 x 32.47 mm bounding box; the rendered preview shows a sealed bearing-like ring. The local manifest names the related assembly as 2AC0_bottom_axis_bearing_SLA10. HIWIN's SLA10 page lists bearing type 6200.2RS and dimensions D 30 mm, b 9 mm."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row part is interpreted as one of the 6200.2RS bearings inside the lower SLA10 axis bearing support because the CAD ring envelope and 9 mm width match the HIWIN SLA10 bearing specification."
  uncertainty_notes:
    - "The row-level STEP does not expose the shaft bore as a separate measured catalog field; the 10 mm bore comes from the SLA10 vendor specification for the matched bearing type."
mass:
  value_kg: 0.0318
  basis: "Per unit. BOM quantity is 1, so row total is also about 0.0318 kg. A vendor listing for 6200-2RS gives weight 0.07 lb, converted as 0.07 * 0.45359237 = 0.03175 kg and rounded to 0.0318 kg. CAD volume 3541.624 mm^3 and a bearing-steel density sanity check gives about 0.0278 kg before seals/cage/void fidelity, consistent with a roughly 0.03 kg catalog bearing."
  source:
    url_or_path: "https://usarollerchain.com/products/2278-brg-6200-2rs; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC8_part_8.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "USA Roller Chain lists 6200-2RS bearing dimensions d 10 mm, D 30 mm, B 9 mm, and weight 0.07 lb. FreeCAD measured one solid, volume 3541.624 mm^3, area 3831.294 mm^2, and bounding box 32.47 x 9.00 x 32.47 mm. The local material density table lists steel density_kg_per_m3: 7850."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The 0.07 lb catalog weight for a standard 6200-2RS bearing is used as the best per-unit mass proxy for this row."
    - "The CAD-derived steel-density calculation is used only as a sanity check because the simplified STEP ring does not resolve balls, cage, seals, grease, and internal voids."
  uncertainty_notes:
    - "Different 6200-2RS manufacturers may vary slightly in cage, seal, grease, and clearance design, so the exact mass may differ by a few grams."
material:
  primary_material: "52100 chrome/bearing steel rings and balls with pressed steel cage, rubber contact seals, and grease lubrication."
  source:
    url_or_path: "https://www.smbbearings.com/firebrick/ckeditor/plugins/upload/Uploads/Documents/bearingpdfs/6200-2RS-bearing-10x32x9mm.pdf; https://pgnbearings.com/products/6200-2rs"
    cited_fact_or_basis: "SMB Bearings' 6200-2RS datasheet lists rings and balls as SAE52100 chrome steel, cage as pressed steel, closures as rubber contact seals, and lubrication as grease. PGN's 6200-2RS product page lists material as 100% Chrome Steel (AISI 52100)."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Material data from standard 6200-2RS bearing vendors is applied to this row because the BOM/CAD identity resolves to a standard 6200.2RS sealed bearing."
  uncertainty_notes:
    - "The local assembly STEP material extractor returned only placeholder Generic density 1000 for this product, so it does not confirm the exact vendor, cage variant, seal elastomer, or grease type used in the reAM250 assembly."
how_to_make:
  summary: "Manufacture by bearing-grade steel ring turning/grinding, ball and raceway finishing, cage forming, rubber seal production, lubrication, assembly, and precision inspection"
  manufacturing_steps:
    - "Manufacturing route: make inner and outer bearing rings from SAE 52100 or equivalent bearing steel, then harden, grind raceways, and finish bearing seats."
    - "Produce"
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0042_2AC8__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC8_part_8.step; https://www.smbbearings.com/firebrick/ckeditor/plugins/upload/Uploads/Documents/bearingpdfs/6200-2RS-bearing-10x32x9mm.pdf; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127"
    cited_fact_or_basis: "The CAD preview shows a compact sealed-bearing ring, and HIWIN's SLA10 page identifies the matched bearing as 6200.2RS. The SMB datasheet identifies material stack and closures/lubrication for a 6200-2RS bearing. The detailed inferred from the standard bearing geometry and material stack rather than directly stated by those sources. targeted_web_search: searched '2AC8 axis bearing bottom reAM250', '2AC8_part_8', 'axis bearing bottom SLA10 bearing', '6200.2RS bearing dimensions 10 30 9 mass material', and '6200-2RS bearing weight 10x30x9 material bearing steel'; results resolved the row's standard bearing identity, material, dimensions, and mass but did not provide a row-specific manufacturing process for the reAM250 bearing."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A self-manufacturing route would model this as a bearing subsystem only after the KB has processes for bearing steel heat treatment, precision race grinding, ball production, seal production, and clean assembly."
  uncertainty_notes:
    - "No row-specific drawing, fit tolerance, bearing clearance class, seal compound, grease specification, or original bearing manufacturer was found."
kb_implications:
  - "item_granularity: simple_part - Treat as a standard replaceable 6200-2RS sealed ball bearing wear item, not a machine-specific custom part; defer sub-BOM modeling until precision bearing manufacture is in scope."
---

# reAM250 BOM Row 42 - 2AC8

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0042_2AC8.md
source_research_sha256: "977e9e0251805ddc958e9afb1809bb17b9032f48a8e4fa1658491a5b13b159b2"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the SLA10 lower axis bearing context, 6200-2RS identity, vendor mass proxy, bearing steel and rubber seal material stack, CAD bearing-ring preview, and KB implication to treat it as a standard replaceable precision bearing."
decomposition:
  decision: decompose_into_parts
  rationale: "The row is a standard replaceable sealed ball bearing at BOM granularity, but local manufacture would require precision rings, balls, heat treatment, race grinding, seals, grease, and clean assembly. That internal chain should be decomposed when precision bearing manufacture is in scope."
  proposed_subparts:
    - inner_and_outer_bearing_rings
    - precision_bearing_balls
    - pressed_steel_cage
    - rubber_contact_seals
    - bearing_grease
process_abstraction:
  original_process_family: precision_sealed_ball_bearing_manufacture
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - import_assumption
    - decomposition_required
    - precision_machining
    - grinding_lapping
    - heat_treatment
    - elastomer_forming
    - assembly
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: bearing_set_fabrication_v0
      fit: partial
      reason: "Closest bearing fabrication anchor, but this row needs a sealed 6200-2RS bearing with race grinding, seals, grease, and precision quality control."
    - process_id: bearing_ball_precision_fabrication_v0
      fit: supporting
      reason: "Relevant to the precision ball subpart if the bearing is decomposed later."
    - process_id: grinding_process_precision_v0
      fit: supporting
      reason: "Relevant to raceway and bearing-seat finishing requirements."
    - process_id: elastomer_molding_basic_v0
      fit: supporting
      reason: "Relevant to rubber contact seals after decomposition."
    - process_id: assembly_process_bearing_v0
      fit: supporting
      reason: "Relevant to clean bearing assembly after rings, balls, cage, seals, and grease are available."
  abstraction_decision: substitute_process_family
  rationale: "The source row resolves to a commercial sealed bearing. A direct local recipe would overstate current closure maturity, so Phase 1 should stage it as a precision component pending bearing-specific decomposition."
  process_guardrails:
    tolerance: high
    surface_finish: high
    sealing_quality: high
    alignment_accuracy: high
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: sealed radial ball bearing for supporting a 10 mm shaft in an axis bearing pocket
  material: bearing_steel_with_pressed_steel_cage_rubber_seals_and_grease
  scale_or_capacity:
    mass_kg: 0.0318
    bom_quantity: 1
    row_total_mass_kg: 0.0318
    scale_class: small
  geometry_form: sealed_deep_groove_ball_bearing_10mm_bore_30mm_outer_diameter_9mm_width
merge_pool:
  eligible: true
  functional_purpose_key: rotary_bearing
  precision_guardrails:
    - bearing_clearance_class
    - raceway_surface_finish
    - seal_material
    - lubrication_specification
    - shaft_and_pocket_dimensions
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Precision race grinding, bearing steel heat treatment, ball production, rubber seals, grease, and clean assembly are unresolved closure dependencies."
    - "Bearing clearance class, seal compound, grease type, and original manufacturer are unknown."
  post_merge_decision_notes: "Final import/local decision is deferred until bearing merge review groups similar rotary bearings and decides whether sealed bearing manufacture is in scope."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a reusable small sealed radial bearing closure item rather than a row-specific axis-bearing part."
assumptions:
  - "Standard 6200-2RS vendor material and mass data are acceptable proxies because the row identity resolves to that bearing type."
  - "The CAD ring is a simplified representation and not a full material-volume basis for balls, cage, seals, grease, and voids."
unresolved:
  - "Original bearing manufacturer, clearance class, seal elastomer, grease specification, and reAM250 fit tolerance remain unresolved."
```
