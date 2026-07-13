---
row_identity:
  item: "6B1"
  cad_file: "6B1_gliding_surface"
  source_row_number: 168
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Long, narrow stainless gliding surface or wear rail used to provide a smooth sliding/contact face in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B1_gliding_surface.step; research/ream250_bom/ream250_bom_row_0168_6B1__views_2x2.png"
    cited_fact_or_basis: "BOM row 168 names item 6B1 with quantity 1 and CAD file 6B1_gliding_surface; manifest row 168 maps it to one matched part STEP. FreeCAD measured one solid with bounding box 50.00 x 10.00 x 274.00 mm, and the rendered preview shows a long thin rail-like contact member."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM/CAD name 'gliding_surface' is interpreted as the functional role rather than a decorative cover."
  uncertainty_notes:
    - "The mating component and exact sliding load direction are not identified by the isolated part export."
mass:
  value_kg: 0.864
  basis: "Per-unit mass for quantity 1. FreeCAD volume is 107985.102 mm^3 = 0.000107985 m^3; assembly STEP metadata reports Stainless Steel with density 8000 kg/m^3, giving 0.863881 kg, rounded to 0.864 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B1_gliding_surface.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 107985.102 mm^3. Local STEP material extraction for product 6B1_gliding_surface found material 'Stainless Steel' and density 8000.0 in the full assembly. The local material properties table lists stainless_steel density as 8000 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported single-solid STEP volume represents one physical 6B1 part."
    - "The stainless steel density applies uniformly to the whole modeled solid."
  uncertainty_notes:
    - "CAD mass excludes any separate coatings, lubricants, or fasteners not present in the isolated gliding-surface solid."
material:
  primary_material: "stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 6B1_gliding_surface returned material 'Stainless Steel' with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata does not specify a stainless grade or surface finish."
how_to_make:
  summary: "Plausible route: cut stainless bar or plate stock to length, machine the profiled ends and contact geometry, deburr, and finish or polish the sliding/contact face before inspection."
  manufacturing_steps:
    - "Prepare stainless steel rectangular bar or plate stock sized for the 50 x 10 x 274 mm envelope"
    - "Saw or abrasive-cut the blank to length."
    - "Mill the end profiles and any relieved rail features visible in the CAD preview."
    - "Deburr edges and polish or grind the gliding contact face to the required sliding finish."
    - "Inspect length, thickness, straightness, and contact-surface finish against the CAD model."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B1_gliding_surface.step; research/ream250_bom/ream250_bom_row_0168_6B1__views_2x2.png; https://pbclinear.com/pages/gliding-surface-technology-catalog; https://www.pobcoplastics.com/product-categories/wear-strips-guide-rails/"
    cited_fact_or_basis: "CAD shows a single stainless rail-like solid with a 50.00 x 10.00 x 274.00 mm envelope and profiled ends. Web sanity check found gliding-surface linear guides and wear-strip/guide-rail product families, but no row-specific manufacturing route. targeted_web_search: queries tried 'stainless steel gliding surface wear strip manufacturing machined ground guide rail', 'stainless steel wear strip gliding surface guide rail', and 'stainless steel sliding surface guide rail ground finish manufacturing'; results supported the guide/wear-surface interpretation but did not identify a reAM250-specific process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because the part is a simple monolithic stainless rail, subtractive machining from bar or plate stock is more plausible than casting or a vendor module route at this modeling resolution."
    - "A smoother sliding face is required by the 'gliding_surface' role, so a final deburr and finish operation is included."
  uncertainty_notes:
    - "The actual production drawing may require a specific roughness, hardening, passivation, or coating not visible in the STEP export."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable stainless machined wear rail/gliding surface rather than a purchased module; no sub-BOM is implied by the single-solid CAD and BOM row."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0168_6B1.md
source_research_sha256: 155361f1a130a0fa6760a754bf793e167851572dae63569c2d09d47f603a36bb
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Read the function, CAD-derived stainless mass, material evidence, machining-and-finishing route, KB implications,
    and preview image showing a long profiled rail before conversion.
decomposition:
  decision: simple_part
  rationale: The row is a single-solid stainless gliding and wear rail with no internal subassembly. Closure should model
    it as one reusable monolithic part whose important requirements are material, straightness, contact-face finish, and end/profile
    geometry.
  proposed_subparts: []
process_abstraction:
  original_process_family: subtractive_machining_from_bar_plate
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
  - stock_preparation
  - cutting
  - precision_machining
  - deburring
  - surface_finishing
  - dimensional_inspection
  - grinding_lapping
  - coating
  candidate_existing_processes:
  - process_id: machining_basic_v0
    fit: partial
    reason: Covers basic stock removal; row-specific precision features remain guardrails.
  - process_id: machining_precision_v0
    fit: supporting
    reason: Relevant when bore, sliding, concentricity, and finish control matter.
  - process_id: inspection_basic_v0
    fit: supporting
    reason: Covers dimensional checks before staging selects the final recipe.
  - process_id: precision_grinding_basic_v0
    fit: supporting
    reason: Relevant when rolling, sliding, and raceway surfaces need precision finishing.
  - process_id: surface_treatment_basic_v0
    fit: supporting
    reason: Relevant when the row needs protective surface treatment.
  abstraction_decision: add_post_processing
  rationale: The wear rail should use the shared subtractive machining bucket, with surface finishing called out for the sliding
    contact face. Metal additive manufacturing is less suitable for straightness and finish.
  process_guardrails:
    tolerance: required - length, thickness, straightness, and profile geometry control sliding fit
    surface_finish: required - gliding/contact face likely needs grinding, polishing, and equivalent finishing
    sealing_quality: not_applicable - no evidence this is a pressure and service seal
    alignment_accuracy: required - rail must register with adjacent recoater/gliding components
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: provide a smooth sliding contact face for recoater and adjacent machine elements
  material: stainless_steel
  scale_or_capacity:
    mass_kg: 0.864
    bom_quantity: 1
    row_total_mass_kg: 0.864
    scale_class: small
  geometry_form: long_narrow_profiled_wear_rail
merge_pool:
  eligible: true
  functional_purpose_key: sliding_contact_guidance
  precision_guardrails:
  - straightness
  - contact_surface_finish
  - wear_resistance
  - profile_accuracy
  - alignment_registration
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - general_subtractive_machining
  import_risk_factors:
  - stainless grade is unspecified
  - required surface roughness, hardening, passivation, and coating is unknown
  - wear life and mating surface requirements are not identified
  post_merge_decision_notes: Final import/local decision is deferred until merge review compares other sliding-contact and
    wear-rail rows and decides the condition that one generalized closure item can cover them.
kb_staging:
  proposed_item_id: null
  notes: Wait for merge review before assigning an item ID; likely candidate for a generalized stainless sliding contact and
    wear rail if precision requirements align.
assumptions:
- The STEP single solid represents one physical gliding-surface part for BOM quantity 1.
- The stainless steel density from assembly metadata applies to the whole rail.
- A shared machining plus surface-finishing process can meet the closure-level requirements if detailed tolerances are not
  unusually tight.
unresolved:
- Exact stainless alloy, hardness, finish roughness, coating/passivation, and wear specification are not provided.
- The mating component and sliding load direction are not visible from the isolated part export.
- Merge review must check the condition that this is functionally compatible with other guide, rail, and wear-surface rows
  despite geometry differences.
```
