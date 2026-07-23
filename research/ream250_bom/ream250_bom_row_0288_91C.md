---
row_identity:
  item: "91C"
  cad_file: "91C_angle_profile_DIN_59370_50x5_200"
  source_row_number: 288
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Short 200 mm length of sharp-edged equal steel L-angle profile, likely used as a small structural bracket, spacer, stiffener, or mounting rail in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91C_angle_profile_DIN_59370_50x5_200.step; research/ream250_bom/ream250_bom_row_0288_91C__views_2x2.png"
    cited_fact_or_basis: "BOM row 288 names item 91C as quantity 3, cad file 91C_angle_profile_DIN_59370_50x5_200, description sharp-edged L-profile. CAD geometry is one solid with 50.00 x 50.00 x 200.00 mm bounding box; preview shows an L-shaped angle section."
    evidence_basis: "bom_provided"
  assumptions:
    - "Function is inferred from the row name and angle-section geometry because the BOM row does not name the parent mounting location."
  uncertainty_notes:
    - "Exact installation location and load case are not identified from this row alone."
mass:
  value_kg: 0.746
  basis: "Per-unit mass for one 200 mm angle profile: FreeCAD volume 95042.920 mm^3 = 9.504292e-5 m^3, multiplied by row-specific STEP density 7850 kg/m^3 gives 0.746 kg. BOM quantity is 3, so row total is about 2.24 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91C_angle_profile_DIN_59370_50x5_200.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 95042.920 mm^3, surface area 40864.588 mm^2, and 50.00 x 50.00 x 200.00 mm bounding box. Assembly STEP material extraction for this product returned Steel, Mild with density 7850.0; local material properties list generic steel density as 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The single exported CAD solid represents one physical BOM-row item."
    - "The STEP density is interpreted as kg/m^3, consistent with the extractor note for this reAM250 export."
  uncertainty_notes:
    - "CAD volume is used directly; any unmodeled small chamfers, burrs, or cut-end finish are below the precision needed for this BOM estimate."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Assembly STEP material extraction matched product 91C_angle_profile_DIN_59370_50x5_200 to material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The export does not specify a more exact steel grade such as S235JR, so the material should remain mild steel unless later vendor or drawing evidence narrows it."
how_to_make:
  summary: "Locally make as a DIN 59370-style bright square-edge equal steel angle, 50 x 50 x 5 mm nominal section, then cut to 200 mm length and deburr the cut ends"
  manufacturing_steps:
    - "Start from mild-steel flat/strip or commercial bright square-edge equal angle stock."
    - "Form the sharp-edged L profile by rolling, press-brake forming, or equivalent profile-forming operation suitable for 5 mm steel."
    - "Cut the profile to 200 mm length."
    - "Deburr and inspect length, leg dimensions, and squareness before assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://webstore.ansi.org/standards/din/din593701978"
    cited_fact_or_basis: "BOM row identifies a sharp-edged L-profile with CAD filename DIN_59370_50x5_200. ANSI's DIN 59370 listing identifies the standard as steel sections, bright square-edge equal angles, covering dimensions, permissible deviations, and weights. targeted_web_search: searched 'DIN 59370 sharp edged L profile angle steel 50x5 material manufacturing hot rolled' and 'DIN 59370 L profile sharp-edged angle profile steel'; results confirmed standard/profile identity but did not provide a row-specific manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The 50x5_200 filename is interpreted as 50 x 50 x 5 mm equal angle cut to 200 mm, consistent with the CAD bounding box and measured volume."
    - "The inferred from common steel angle/profile production and cut-to-length practice, not from a row-specific process drawing."
  uncertainty_notes:
    - "The exact original supply route, surface finish, and forming process are not specified by the BOM row."
kb_implications:
  - "item_granularity: simple_part - Treat this as reusable cut-to-length steel angle stock/profile rather than a machine-specific assembly; later KB modeling can represent standard angle stock plus a cutting operation."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0288_91C.md
source_research_sha256: "5b67da278a0b3a469ebdc52e519e7ca062e2e724f336d0604740faf0819b027c"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read function, quantity, CAD-derived mass, mild-steel material evidence, profile forming/cutting route, kb implications, and preview showing a 200 mm equal L-angle profile."
decomposition:
  decision: simple_part
  rationale: "The row is a single cut length of steel angle profile with no subparts. Profile cross-section and length define its merge guardrails."
  proposed_subparts: []
process_abstraction:
  original_process_family: steel_angle_profile_forming_and_cut_to_length
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - forming
    - cutting
    - deburring
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: metal_forming_basic_v0
      fit: partial
      reason: "Covers forming steel profiles at coarse closure level."
    - process_id: cutting_basic_v0
      fit: supporting
      reason: "Covers cutting profile stock to 200 mm length."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Relevant for length, leg dimensions, squareness, and cut-end checks."
    - process_id: rolling_basic_shop_v0
      fit: supporting
      reason: "Relevant if local production rolls steel profile stock before cutting."
  abstraction_decision: keep_original_family
  rationale: "The original route is standard structural profile stock formed and cut to length. This should merge with other cut steel structural profiles when dimensions and material are compatible."
  process_guardrails:
    tolerance: standard_profile_review
    surface_finish: cut_end_finish_review
    sealing_quality: not_applicable
    alignment_accuracy: squareness_review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: small structural rail bracket spacer stiffener and mounting member
  material: mild_steel
  scale_or_capacity:
    mass_kg: 0.746
    bom_quantity: 3
    row_total_mass_kg: 2.24
    scale_class: small
  geometry_form: 50x50x5mm_equal_l_angle_profile_200mm_length
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_member
  precision_guardrails:
    - angle_profile_cross_section
    - cut_length
    - squareness
    - mild_steel
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
  import_risk_factors:
    - "Exact steel grade and surface finish are unresolved."
    - "DIN profile tolerances may matter if the part aligns precision hardware."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares cut structural profiles and decides standard stock reuse."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review before assigning an item ID; likely candidate family is a small mild-steel structural angle profile."
assumptions:
  - "BOM quantity is 3, so row total mass is about 2.24 kg from the 0.746 kg per-unit estimate."
  - "The filename and CAD box support 50 x 50 x 5 mm equal angle cut to 200 mm."
  - "Profile stock plus cutting is sufficient for row-conversion closure abstraction."
unresolved:
  - "Exact steel grade and finish."
  - "Installation location, load case, and alignment tolerance."
```
