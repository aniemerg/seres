---
row_identity:
  item: "64"
  cad_file: "64_retaining_ring_DIN 471 - 8x0,8"
  source_row_number: 270
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "DIN 471 external retaining ring for an 8 mm shaft/groove interface; it forms a removable axial shoulder that retains a mating component on a shaft."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/64_retaining_ring_DIN 471 - 8x0,8.step; research/ream250_bom/ream250_bom_row_0270_64__views_2x2.png"
    cited_fact_or_basis: "BOM row 270 lists item 64, quantity 1, CAD file '64_retaining_ring_DIN 471 - 8x0,8', and description 'spring retaining ring'. The manifest maps the same row to a matched part STEP. FreeCAD measured one solid with a 10.25 x 12.45 x 0.80 mm bounding box, and the rendered preview shows a thin split external retaining ring with lug holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The DIN 471 - 8x0,8 text is interpreted as a standard external shaft retaining-ring designation for an 8 mm shaft with 0.8 mm ring thickness."
  uncertainty_notes: []
mass:
  value_kg: 0.00027
  basis: "FreeCAD volume 34.376 mm^3 equals 3.4376e-8 m^3. Assembly STEP material metadata reports Steel, Mild with density 7850 kg/m^3 for this product, giving 3.4376e-8 m^3 * 7850 kg/m^3 = 0.000270 kg per retaining ring. BOM quantity is 1, so the row total is also about 0.000270 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/64_retaining_ring_DIN 471 - 8x0,8.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 34.376 mm^3, area 137.952 mm^2, and bounding box 10.25 x 12.45 x 0.80 mm. The local STEP material extractor matched product 64_retaining_ring_DIN 471 - 8x0,8 and reported material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP volume is treated as the complete solid volume for one physical retaining ring."
    - "The STEP material density is used as the calculation constant for the row-level mass estimate."
  uncertainty_notes:
    - "The CAD-derived mass is sensitive to whether small chamfers, edge radii, and manufacturing clearances are fully represented, but the value is adequate for BOM-scale mass accounting."
material:
  primary_material: "steel family; local STEP metadata labels the row material as Steel, Mild, while DIN 471 retaining rings are commonly spring-steel hardware"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.fastenermart.com/din-471-external-retaining-rings.html; https://www.fasteners.eu/standards/din/471/"
    cited_fact_or_basis: "The local STEP material extractor reports Steel, Mild and density 7850.0 for this row product. Fastener Mart lists DIN 471 external retaining rings as available in spring steel and stainless steel, and Fasteners.eu lists the DIN 471 steel material as spring steel; these are cross-checks for the standard hardware family."
    evidence_basis: "bom_provided"
  assumptions:
    - "For KB planning, model this as steel-family retaining-ring hardware rather than relying on the CAD label as a functional spring grade."
  uncertainty_notes:
    - "The row-specific CAD metadata resolves the material family as steel, but exact grade, heat treatment, and finish are not resolved for this specific BOM row."
how_to_make:
  summary: "Prepare as a standard DIN 471 external retaining ring; blanking/stamping the ring profile from spring-steel strip, heat treating if not supplied pre-hardened, finishing/coating, and inspecting shaft-groove fit"
  manufacturing_steps:
    - "Select spring-steel strip or steel strip stock at about 0.8 mm thickness for the DIN 471 8 mm ring size."
    - "Blank or stamp the split-ring outline, lug ends, and plier holes."
    - "Deburr edges and heat treat or stress relieve as needed for spring retention behavior."
    - "Apply a corrosion-protection finish if required, then inspect free shape, thickness, lug holes, and fit in the mating shaft groove."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0270_64__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/64_retaining_ring_DIN 471 - 8x0,8.step; https://www.huyett.com/dsh-008-zc; https://www.fastenermart.com/din-471-external-retaining-rings.html"
    cited_fact_or_basis: "The CAD preview shows a thin stamped-looking split retaining ring with lug holes. Huyett's matching M8 DIN 471 snap-ring page lists an external snap ring, carbon spring steel material, 0.80 mm thickness, and stamped style. Fastener Mart describes DIN 471 rings as external shaft retaining rings installed into a shaft groove. targeted_web_search: searched 'DIN 471 retaining ring 8x0.8 material spring steel', 'DIN 471 external retaining ring function shaft groove spring steel', and 'DIN 471 retaining ring manufacturing stamped spring steel'; results resolved standard retaining-ring function, common material family, and a stamped style for comparable DIN 471 rings, but did not provide the actual factory process used for this exact reAM250 row."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the standard ring geometry, 0.8 mm strip-like thickness, and comparable catalog description of DIN 471 rings as stamped external snap rings."
  uncertainty_notes:
    - "The cited sources do not identify the actual supplier or process used for the reAM250 row, so heat treatment and finish remain planning assumptions."
kb_implications:
  - "item_granularity: simple_part - standard small external retaining-ring hardware; later KB modeling should reuse or parameterize a generic DIN 471 steel retaining ring rather than create a machine-specific custom part."
---

Research result for reAM250 BOM row 270.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0270_64.md
source_research_sha256: "863de06773c2e88e9175599a960c50b626278c3b940324ad666326b87682c103"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read shaft-retention function, CAD/STEP material mass basis, steel retaining-ring material evidence, stamped spring-hardware route, KB implication, and preview of the thin split ring with lug holes."
decomposition:
  decision: simple_part
  rationale: "The row is one standard retaining ring with no subcomponents; it should merge into a generic small retaining hardware family."
  proposed_subparts: []
process_abstraction:
  original_process_family: stamped_heat_treated_spring_steel_retaining_ring
  primary_process_bucket: fastener_forming_thread_rolling
  supporting_processes:
    - cutting
    - forming
    - heat_treatment
    - deburring
    - coating
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: fastener_kit_small_fabrication_v0
      fit: partial
      reason: "Aggregates small fastener fabrication and can stand in for standard retaining-ring hardware during coarse closure."
    - process_id: metal_forming_basic_v0
      fit: supporting
      reason: "Covers basic sheet/strip forming operations related to stamped ring shape production."
    - process_id: heat_treatment_basic_v0
      fit: supporting
      reason: "Relevant to spring retention behavior after blanking and forming."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks of thickness, free shape, lug holes, and shaft-groove fit."
  abstraction_decision: keep_original_family
  rationale: "The source route is standard stamped steel retaining hardware; the canonical fastener-forming bucket is the closest shared closure handle despite the absence of thread rolling."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: not_applicable
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: removable axial retention shoulder for a shaft groove
  material: steel_spring_hardware_family
  scale_or_capacity:
    mass_kg: 0.00027
    bom_quantity: 1
    row_total_mass_kg: 0.00027
    scale_class: tiny
  geometry_form: thin_split_external_retaining_ring_with_lug_holes
merge_pool:
  eligible: true
  functional_purpose_key: axial_retention
  precision_guardrails:
    - shaft_groove_fit
    - spring_retention
    - thickness
    - heat_treatment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - fastener_forming_thread_rolling
  import_risk_factors:
    - "Exact spring steel grade, heat treatment, and finish are unresolved."
    - "Small stamped hardware may be better treated as part of a fastener kit if individual production detail is below closure resolution."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred until after merge review with other retaining rings and small axial-retention hardware."
kb_staging:
  proposed_item_id: null
  notes: "Leave final closure item ID open; likely merge into generic retaining-ring hardware rather than a row-specific DIN 471 item."
assumptions:
  - "Use steel-family spring hardware despite row CAD metadata saying mild steel."
  - "Use 0.00027 kg per unit from the CAD-volume and steel-density calculation."
  - "Treat stamped strip forming plus heat treatment as the local closure route."
unresolved:
  - "Exact spring steel grade and hardness."
  - "Finish/coating and corrosion requirement."
  - "Whether later staging should model this as an individual retaining ring item versus fold it into a small fastener kit."
```
