---
row_identity:
  item: "2AJ1"
  cad_file: "2AJ1_axis"
  source_row_number: 61
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.karl-hipp.de/produkte/praezisionskugelgewindetriebe/nenndurchmesser-16mm/16-04/item/kgt-f1-16-04"
function:
  summary: "Ball screw spindle or axis member for the reAM250 Z-axis drive, converting rotary input through the mating ball nut into precise linear motion."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AJ1_axis.step; https://www.karl-hipp.de/produkte/praezisionskugelgewindetriebe/nenndurchmesser-16mm/16-04/item/kgt-f1-16-04"
    cited_fact_or_basis: "BOM row 61 identifies item 2AJ1 as 2AJ1_axis from Karl Hipp GmbH with description including axis and the KGT-F1-16-04 product route; FreeCAD measured a long 490.00 x 16.00 x 16.00 mm single solid; Karl Hipp states ball screws convert rotary motion to linear motion and the product route is for nominal diameter 16 mm, lead 4 mm precision ball screws."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name axis and long cylindrical CAD geometry identify this row as the spindle/axis portion of the ball screw set rather than the flanged nut shown on the shared product-family page."
  uncertainty_notes:
    - "The row-specific STEP file contains the spindle geometry but not thread detail or assembly context for the mating nut."
mass:
  value_kg: 0.679
  basis: "Per-unit estimate for quantity 1. FreeCAD volume is 86444.075 mm^3, converted to 0.000086444075 m^3 and multiplied by 7850 kg/m^3 generic steel density from kb/materials/properties.yaml, giving 0.6786 kg per spindle."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AJ1_axis.step; kb/materials/properties.yaml; https://www.schneeberger.com/fileadmin/images/landingpages/Vis_a_billes_HIPP/ProduktkatalogEN.pdf"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 86444.075 mm^3 and bounding box 490.00 x 16.00 x 16.00 mm. kb/materials/properties.yaml lists generic steel density as 7850 kg/m^3. The Hipp product catalogue identifies the standard ballscrew spindle material as Cf53 with the ball track hardened to 60 +/-2 HRC. bom_url_route_check: the BOM Link URL on karl-hipp.de and its one-page KGT-F1-16-04 datasheet route were checked first; they resolved the product family and dimensions but not material, so the hosted Hipp catalogue PDF was used for the spindle material fact."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The STEP solid volume is treated as the per-unit physical volume for one BOM row item."
    - "Cf53 spindle steel is approximated with the local generic steel density because the local density table does not include a Cf53-specific entry."
  uncertainty_notes:
    - "Mass omits any balls, nut, bearing supports, or coupling hardware from adjacent BOM rows."
material:
  primary_material: "Cf53 steel ball screw spindle, ball track hardened to 60 +/-2 HRC"
  source:
    url_or_path: "https://www.schneeberger.com/fileadmin/images/landingpages/Vis_a_billes_HIPP/ProduktkatalogEN.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Hipp product catalogue materials section states the standard ballscrew spindle material is Cf53 with ball track hardened to 60 +/-2 HRC. The local assembly STEP material extractor returned only placeholder material Generic with density 1000.0 for 2AJ1_axis, which does not resolve material. bom_url_route_check: the BOM Link URL on karl-hipp.de and the row's downloadable KGT-F1-16-04 datasheet route were checked first and did not expose a row-specific material grade."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The standard spindle material applies to this non-stainless row because neither the BOM text nor CAD metadata indicates a stainless variant."
  uncertainty_notes:
    - "The row does not include a complete Karl Hipp order code tolerance/material suffix, so stainless or special-order variants cannot be excluded from BOM-side evidence alone."
how_to_make:
  summary: "Prepare as a Karl Hipp precision-ground 16 mm lead-4 ball screw spindle, or manufacture locally by preparing Cf53 steel bar, machining end features, heat treating the ball track, precision grinding the screw profile, and inspecting lead accuracy"
  manufacturing_steps:
    - "Start from Cf53 steel round bar sized for a 16 mm nominal ball screw spindle and cut to the required overall length."
    - "Turn bearing journals, threaded or coupling ends, and shoulders to the required drawing dimensions."
    - "Heat treat the ball track region to the catalogue hardness target."
    - "Precision grind the ball screw thread/profile after heat treatment and finish-grind bearing seats."
    - "Inspect straightness, lead, runout, surface finish, and fit with the matching ball nut."
  source:
    url_or_path: "https://www.schneeberger.com/fileadmin/images/landingpages/Vis_a_billes_HIPP/ProduktkatalogEN.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AJ1_axis.step"
    cited_fact_or_basis: "The Hipp catalogue says ball screw profiles are ground after heat treatment and identifies standard spindle material/hardness; the CAD file shows a slender 490 mm long axis/spindle form. targeted_web_search: queries tried: 'Karl Hipp KGT-F1-16-04 ball screw material axis', 'Karl Hipp ballscrew spindle Cf53 hardened ground after heat treatment', and 'KGT-F1-16-04 datasheet material'; results found product-family and catalogue evidence but no row-specific manufacturing routing sheet."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The listed manufacturing route extrapolates normal precision ball screw production steps from the catalogue facts and CAD geometry."
  uncertainty_notes:
    - "A full local process model would need the exact thread grinding geometry, heat treatment specification, end-machining drawing, and inspection tolerances."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable precision ball screw spindle/axis part rather than raw bar stock; the mating nut, supports, and couplings should remain separate BOM rows or subcomponents."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0061_2AJ1.md
source_research_sha256: "576911d038eeeda3e0fd081ab0a26fbd45628d94037ebc4e473b8c3f5cc54b05"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the ball-screw spindle function, steel-density mass basis, Cf53 hardened material evidence, precision manufacturing route, KB implications, and CAD preview before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one precision ball-screw spindle/axis member, not the full linear actuator assembly. It stays a simple item, but precision manufacturing capability is a major guardrail."
  proposed_subparts: []
process_abstraction:
  original_process_family: precision_ground_hardened_ball_screw_spindle
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - heat_treatment
    - grinding_lapping
    - surface_finishing
    - dimensional_inspection
    - calibration
    - import_assumption
  candidate_existing_processes:
    - process_id: machining_process_turning_v0
      fit: supporting
      reason: "Relevant to turning journals, shoulders, and end features before heat treatment and grinding."
    - process_id: machining_precision_v0
      fit: partial
      reason: "Covers precision machining concepts but lacks ball-screw thread grinding, lead accuracy, and hardened race detail."
    - process_id: precision_grinding_and_scraping_v0
      fit: supporting
      reason: "Closest existing anchor for precision finishing, though ball-screw thread grinding needs more specific capability."
    - process_id: calibration_basic_v0
      fit: supporting
      reason: "Relevant to lead accuracy and axis-fit verification after manufacture."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers straightness, runout, surface, and fit checks at coarse KB level."
  abstraction_decision: needs_human
  rationale: "The part requires hardened race geometry, precision ground screw profile, lead accuracy, and runout control beyond generic machining. It should remain a precision component until a local ball-screw process is explicitly modeled."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: convert rotary drive input into precise linear axis motion
  material: cf53_hardened_steel
  scale_or_capacity:
    mass_kg: 0.679
    bom_quantity: 1
    row_total_mass_kg: 0.679
    scale_class: small
    nominal_diameter_mm: 16
    lead_mm: 4
    length_mm: 490
  geometry_form: long_precision_ball_screw_spindle_with_end_features
merge_pool:
  eligible: true
  functional_purpose_key: linear_guidance
  precision_guardrails:
    - lead_accuracy
    - thread_profile
    - hardness
    - straightness
    - runout
    - nut_compatibility
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Precision ball-screw manufacture requires hardened Cf53 steel, ground race profile, lead accuracy, runout control, and matched nut compatibility."
    - "Current generic machining processes do not fully capture ball-screw grinding and inspection requirements."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this row with other linear-guidance and ball-screw rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable precision ball-screw spindle abstraction with diameter, lead, and length guardrails."
assumptions:
  - "The standard Karl Hipp spindle material and hardness apply to this row."
  - "The CAD solid represents the spindle only, excluding mating nut, balls, supports, and couplings."
  - "Generic steel density is sufficient for mass grouping despite Cf53-specific material identity."
unresolved:
  - "Exact end-machining drawing, tolerance class, lead accuracy, thread profile, heat treatment specification, surface finish, and matched nut details are not resolved by row evidence."
```
