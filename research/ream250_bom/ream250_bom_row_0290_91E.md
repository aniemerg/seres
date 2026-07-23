---
row_identity:
  item: "91E"
  cad_file: "91E_angle_profile_closed_DIN_59370_50x5"
  source_row_number: 290
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Closed rectangular structural frame made from sharp-edged DIN 59370 L-angle profile, likely serving as a stiff mounting or perimeter support frame within the reAM250 mechanical structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91E_angle_profile_closed_DIN_59370_50x5.step; research/ream250_bom/ream250_bom_row_0290_91E__views_2x2.png"
    cited_fact_or_basis: "BOM row 290 identifies item 91E, quantity 1, description 'sharp-edged L-profile', and CAD file 91E_angle_profile_closed_DIN_59370_50x5. The manifest maps row 290 to a matched_existing part STEP. FreeCAD measured one solid with bounding box 50.00 x 900.00 x 1670.00 mm, and the rendered contact sheet shows a closed rectangular frame from angle-section stock."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP solid represents the physical item for this BOM row."
    - "Because the BOM row and CAD filename do not name the parent subsystem, the frame is interpreted by geometry as a structural support or mounting frame rather than a process-active module."
  uncertainty_notes:
    - "The exact mating parts and load path are not identified by the BOM row, so the frame's precise location in the machine remains unresolved."
mass:
  value_kg: 18.9
  basis: "Per-unit estimate for BOM quantity 1. FreeCAD volume is 2356023.354 mm^3, equal to 0.002356023 m^3. Using the local stainless_steel_304 / EN 1.4301 density constant of 8030 kg/m^3 gives 18.918 kg, rounded to 18.9 kg. As a sanity check, the CAD outer perimeter is about 2 * (0.900 + 1.670) = 5.14 m; a vendor DIN 59370 L 50 x 50 x 5 angle stock listing gives about 3.8 kg/m, implying about 19.5 kg before miter/closure details."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91E_angle_profile_closed_DIN_59370_50x5.step; kb/materials/properties.yaml; https://www.montanstahl.com/downloads/pdf/Equal-Angles-Cold-Drawn-Datasheet.pdf"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 2356023.354 mm^3, area 991166.823 mm^2, and bounding box 50.00 x 900.00 x 1670.00 mm. kb/materials/properties.yaml lists stainless_steel_304 / stainless_steel_1_4301 density as 8030 kg/m^3. Montanstahl's cold-drawn equal-angle data sheet lists L 50 x 50 x 5 at 3.8 kg/m and states dimensions/tolerances according to DIN 59370."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD solid volume is treated as the complete solid volume of one closed frame."
    - "Stainless 304 / EN 1.4301 density is used as the calculation constant because DIN 59370 sharp-edged angle vendor examples are stainless steel angle stock, but the exact grade is not row-stated."
  uncertainty_notes:
    - "The estimate depends on the inferred stainless family; using generic carbon steel density would change the value only slightly, while aluminum would be a substantially lower-mass alternative not supported by the DIN 59370 stainless angle sources checked."
material:
  primary_material: "stainless steel sharp-edged DIN 59370 L-angle stock family"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.montanstahl.com/downloads/pdf/Equal-Angles-Cold-Drawn-Datasheet.pdf; https://www.edelstahl-lechner.de/edelstahl-profil-ipe-winkel-rohr/edelstahlwinkel-scharfkantig/va-winkel-scharfkantig-gezogen.html"
    cited_fact_or_basis: "BOM row 290 and the CAD filename identify a DIN 59370 50x5 sharp-edged L-profile but give no manufacturer, material hint, or link URL. Assembly STEP material extraction for product 91E_angle_profile_closed_DIN_59370_50x5 returned placeholder material 'Generic' with density 1000.0. Montanstahl's data sheet covers cold-drawn equal angles with dimensions/tolerances according to DIN 59370 and grade according to EN 10088-3. Edelstahl Lechner lists sharp-edged stainless steel angles in 1.4301 and 1.4571 and includes a 50x50x5 DIN 59370 product image."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's DIN 59370 sharp-edged L-profile designation is interpreted as the same stainless angle-stock product family described by the vendor sources."
  uncertainty_notes:
    - "No row-specific material metadata resolves the exact grade; downstream KB modeling should keep the material at stainless-steel family level unless another assembly drawing or procurement record identifies 1.4301, 1.4571, or a different alloy."
how_to_make:
  summary: "Fabricate as a welded or otherwise joined closed rectangular frame from DIN 59370 50x50x5 sharp-edged stainless L-angle stock"
  manufacturing_steps:
    - "Make stainless DIN 59370 50x50x5 sharp-edged L-angle stock"
    - "Cut four angle-stock segments to the frame lengths and miter or notch the corners to match the CAD geometry."
    - "Fixture the segments square to the roughly 900 x 1670 mm frame envelope."
    - "Weld, braze, or mechanically join the corners into the closed frame, then grind/deburr exposed edges."
    - "Inspect flatness, corner squareness, and mounting-interface dimensions before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91E_angle_profile_closed_DIN_59370_50x5.step; research/ream250_bom/ream250_bom_row_0290_91E__views_2x2.png; https://www.montanstahl.com/downloads/pdf/Equal-Angles-Cold-Drawn-Datasheet.pdf"
    cited_fact_or_basis: "The CAD preview shows a closed rectangular frame made from angle-section stock, and FreeCAD measured a 50.00 x 900.00 x 1670.00 mm bounding box. Montanstahl's data sheet identifies 50x50x5 cold-drawn equal angle stock made to DIN 59370 dimensions/tolerances. targeted_web_search: tried 'DIN 59370 angle profile 50x5 sharp edged L profile material', 'DIN 59370 steel angle profile 50 x 5 weight kg m', and 'DIN 59370 Winkelprofil 50x5 scharfkantig Edelstahl'; results resolved the angle-stock family and weight/material examples but did not provide a row-specific manufacturing route for the closed reAM250 frame."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The closed frame is made from cut lengths of the standard angle stock rather than machined from one monolithic plate."
    - "Joining and finishing operations are inferred from the closed-frame geometry; the source data does not state the original manufacturing route."
  uncertainty_notes:
    - "The CAD preview is sufficient for route triage but not for weld type, corner detail, tolerance class, or final surface-finish requirements."
kb_implications:
  - "item_granularity: simple_part - Treat as one fabricated structural frame from reusable stainless DIN 59370 angle stock, not as a calibrated purchased module; later KB work can model the stock profile and frame fabrication route separately if this row becomes mass-critical."
---

Research result for the leased reAM250 BOM row only.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0290_91E.md
source_research_sha256: "e22247d6edfc05332ee7ba7fafdf6650095c96ea51d6f368e8a7f73fdf49c82d"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the structural perimeter frame function, 18.9 kg mass estimate, stainless DIN 59370 angle-stock evidence, cut-and-join frame fabrication route, KB implication, and CAD preview showing a large closed rectangular angle frame."
decomposition:
  decision: simple_part
  rationale: "The row is one fabricated structural frame made from repeated profile stock segments; it can remain one closure item while the stock and joining route are handled in process modeling."
  proposed_subparts: []
process_abstraction:
  original_process_family: cut_joined_structural_angle_stock_frame
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - stock_preparation
    - cutting
    - joining
    - deburring
    - grinding_lapping
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: metal_cutting_basic_v0
      fit: partial
      reason: "Covers cutting profile stock to length before frame joining."
    - process_id: welding_and_fabrication_v0
      fit: partial
      reason: "Covers fitting, joining, cleanup, and general frame fabrication from stock."
    - process_id: welding_structural_v0
      fit: supporting
      reason: "Relevant if the closed frame uses welded corners and needs structural joint control."
    - process_id: finishing_deburring_v0
      fit: supporting
      reason: "Covers deburring and grinding exposed cut and joined edges."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers frame squareness, flatness, and mounting-interface checks."
  abstraction_decision: keep_original_family
  rationale: "The source route is already profile stock cut to frame lengths and joined into a rectangular structure, matching the structural profile stock fabrication bucket."
  process_guardrails:
    tolerance: moderate
    surface_finish: low_to_moderate
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "stiff structural perimeter frame and mounting support"
  material: stainless_steel_angle_stock_family
  scale_or_capacity:
    mass_kg: 18.9
    bom_quantity: 1
    row_total_mass_kg: 18.9
    scale_class: large
  geometry_form: closed_rectangular_l_angle_profile_frame
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - frame_squareness
    - flatness
    - profile_cross_section
    - stainless_material_family
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
  import_risk_factors:
    - "DIN 59370 sharp-edged profile stock availability and stainless grade remain unresolved at row-specific level."
    - "Large frame squareness and flatness may require welding fixtures and post-join inspection."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this with other structural frames and profile-stock members."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a generic large stainless structural frame made from angle profile stock."
assumptions:
  - "BOM quantity is 1 and row total mass is treated as 18.9 kg from the stainless angle-stock estimate."
  - "The frame is modeled as cut and joined profile stock rather than a monolithic machined plate."
  - "DIN 59370 50x50x5 profile geometry is important to merge identity because it drives stock form and mass."
unresolved:
  - "Exact stainless grade, corner joint type, weld detail, fixture requirements, and final flatness tolerance are unknown."
  - "The parent subsystem and precise load path are not resolved from the row evidence."
```
