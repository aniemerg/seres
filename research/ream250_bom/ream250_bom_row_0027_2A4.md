---
row_identity:
  item: "2A4"
  cad_file: "2A4_slide_HGL15CA2R600Z0H_part_2"
  source_row_number: 27
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.hiwin.de/de/Produkte/Profilschienenf%C3%BChrungen/Auswahl-%C3%BCber-Laufwagen/Baureihe-HG-QH/HGL/HGL15CAZ0H/p/5-001374"
function:
  summary: "Hiwin HGL15CAZ0H low square linear guideway block/carriage for HG/QH ball-guide rails, providing precise low-friction linear motion on the reAM250 axis guide rail."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.hiwin.de/en/Products/Linear-guideways/Blocks/Ball-guides/Series-HG-QH/HGL/HGL15CAZ0H/p/5-001374; research/ream250_bom/ream250_bom_row_0027_2A4__views_2x2.png"
    cited_fact_or_basis: "BOM row 27 and the manifest identify item 2A4 as quantity 3 of 2A4_slide_HGL15CA2R600Z0H_part_2, described as a Hiwin linear guide slide. The Hiwin product page identifies type HGL15CAZ0H, article number 5-001374, in Linear guideways / Blocks / Ball guides / Series HG/QH / HGL, and states that linear guideways use balls or rolls between rail and block for precise linear movement. The CAD contact sheet shows a compact guide block/carriage form. official_alternate_route_check: original BOM URL is the German hiwin.de product page; the cited English hiwin.de page is the same official domain and same product/article route, matching HGL15CAZ0H and 5-001374."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM word 'slide' is treated as the linear guideway block/carriage, not the rail; the adjacent BOM row 2A51 separately covers the HGR15 rail."
  uncertainty_notes: []
mass:
  value_kg: 0.14
  basis: "Per-unit catalog mass for one HGL15CAZ0H block. BOM quantity is 3, so the row total is about 0.42 kg. FreeCAD measured the row STEP as one solid with volume 32117.282 mm^3 and bounding box about 34.00 x 69.56 x 19.70 mm; the CAD-derived steel-volume sanity check is not used as the final mass because the row-matched Hiwin page gives a direct catalog mass."
  source:
    url_or_path: "https://www.hiwin.de/en/Products/Linear-guideways/Blocks/Ball-guides/Series-HG-QH/HGL/HGL15CAZ0H/p/5-001374; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A4_slide_HGL15CA2R600Z0H_part_2.step"
    cited_fact_or_basis: "The Hiwin HGL15CAZ0H product page lists mass 0.14 kg, plus dimensions H 24 mm, W 34 mm, and block length L 61.4 mm. FreeCAD measured 1 solid, volume 32117.282 mm^3, area 9939.172 mm^2, and bounding box about 34.00 x 69.56 x 19.70 mm. official_alternate_route_check: original BOM URL is the German hiwin.de page for HGL15CAZ0H / 5-001374; the cited English hiwin.de page is the same official product route and resolves the row's mass."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The supplied STEP length is slightly longer than the catalog block length, likely because it includes end features or CAD envelope details; the direct catalog mass is preferred for planning."
material:
  primary_material: "carbon steel linear-guide block/carriage with recirculating steel balls, seals/end components, and grease/lubrication features"
  source:
    url_or_path: "https://www.hiwin.com/wp-content/uploads/Linear_Guideway-E-1.pdf; https://www.hiwin.de/en/Products/Linear-guideways/Blocks/Ball-guides/Series-HG-QH/HGL/HGL15CAZ0H/p/5-001374; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Hiwin HG-series order-code material convention states that no material symbol means carbon steel and M means stainless steel; the row product code HGL15CAZ0H contains no M material marker. The Hiwin product page confirms HGL15CAZ0H and 5-001374. Assembly STEP material extraction for 2A4_slide_HGL15CA2R600Z0H_part_2 returned only placeholder 'Generic' with density 1000.0, so STEP metadata does not resolve material. standard_part_convention: parameters present are series HG, block type L, size 15, load type C, mounting A, preload Z0, accuracy H, and no M material suffix; this is sufficient for the broad carbon-steel versus stainless material family, but not for exact alloy grade, ball grade, seal elastomer, or grease."
    evidence_basis: "standard_part_convention"
  assumptions:
    - "Small non-steel components such as seals, end caps, and lubricant are grouped under the purchased guide block material set rather than modeled as separate materials at this stage."
  uncertainty_notes:
    - "The exact steel grade, heat treatment, coating, seal polymer, and lubricant are not specified by the row evidence."
how_to_make:
  summary: "Manufacturing requires precision-machined and hardened steel raceway bodies, recirculating balls, end-return/seal components, lubrication hardware, grinding/lapping, assembly, preload control, and inspection"
  manufacturing_steps:
    - "Start from bearing-quality carbon steel stock for the block body and rolling elements."
    - "Machine the low square guide-block body, mounting faces, M4 mounting holes, and internal recirculation/raceway features."
    - "Heat treat and precision grind or lap the raceways and datum faces to match HG15 rail geometry."
    - "Manufacture precision steel balls, end-return pieces, seals, grease nipple or lubrication interface parts, and retainers as needed"
    - "Assemble with lubricant, set the Z0 light preload class, and inspect smooth travel, dimensions, accuracy class H interfaces, and load-bearing surfaces."
  source:
    url_or_path: "https://www.hiwin.de/en/Products/Linear-guideways/Blocks/Ball-guides/Series-HG-QH/HGL/HGL15CAZ0H/p/5-001374; https://www.hiwin.com/wp-content/uploads/Linear_Guideway-E-1.pdf; research/ream250_bom/ream250_bom_row_0027_2A4__views_2x2.png"
    cited_fact_or_basis: "The Hiwin product page identifies the row as HGL15CAZ0H, gives block dimensions, load ratings, preload Z0, accuracy H, mass, and linear-guideway operating principle. The HG catalog/order-code convention identifies HGL as a low square block and the no-M material convention as carbon steel. The CAD preview shows a compact carriage/block with railway features. targeted_web_search: checked the BOM-provided Hiwin URL, searched 'site:hiwin.de HGL15CAZ0H 5-001374 Hiwin', 'HIWIN linear guideway HGL block material steel balls rail block material', 'HIWIN linear guideways catalogue HGL15CA material steel block', 'No symbol: Carbon Steel HGL HIWIN', and 'HGL15CAZ0H Carbon Steel'; found row-matched product, material-code, dimension, and mass evidence, but no source stating Hiwin's exact factory manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the product identity, precision linear-guide function, carbon-steel convention, CAD geometry, and common bearing/linear-guide construction."
    - "For KB planning, this should remain a external precision motion component unless linear-guide production becomes a high-priority closure target"
  uncertainty_notes:
    - "The actual Hiwin process, alloy, heat treatment, grinding sequence, preload-setting method, and seal/lubricant specifications are not provided by the row evidence."
kb_implications:
  - "item_granularity: complex_module - Treat as a standard complex precision linear-guide block/carriage shared with similar HGL15 rows; decompose only if the KB later models precision guideway manufacturing."
---

Research result for the leased reAM250 BOM row only.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0027_2A4.md
source_research_sha256: "c6b71a878bc44c9629a0850e49154839736cc7659bf6b1cc6e2c5a4f3ec3e647"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read function, quantity, catalog mass, material convention evidence, precision guideway manufacturing route, kb implications, and preview showing a compact guide block/carriage."
decomposition:
  decision: decompose_into_parts
  rationale: "The row is a complex precision linear guide carriage containing a hardened body, raceways, recirculating balls, end-return parts, seals, lubricant, and preload/accuracy controls. Those internal dependencies matter before local closure."
  proposed_subparts:
    - hardened_carriage_body
    - precision_steel_balls
    - recirculation_end_return_parts
    - seal_and_lubrication_parts
    - preload_and_inspection_requirements
process_abstraction:
  original_process_family: precision_linear_guide_block_manufacturing_and_assembly
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - decomposition_required
    - precision_machining
    - heat_treatment
    - grinding_lapping
    - assembly
    - calibration
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: precision_grinding_and_scraping_v0
      fit: supporting
      reason: "Relevant to finishing guide surfaces and datum faces, though recirculating raceway geometry is more specialized."
    - process_id: bearing_manufacturing_small_v0
      fit: partial
      reason: "Closest anchor for precision races, balls, grease, and tight tolerances, but it models bearings rather than linear guide carriages."
    - process_id: ball_bearing_machining_v0
      fit: supporting
      reason: "Weak anchor for rolling-element finishing only."
    - process_id: heat_treatment_basic_v0
      fit: supporting
      reason: "Relevant to hardening and tempering the steel raceway body."
  abstraction_decision: needs_human
  rationale: "The source item is a catalog precision motion component with preload class and accuracy class. Row conversion should keep it in precision import/decompose-later until the KB explicitly models linear guideway production."
  process_guardrails:
    tolerance: high_precision_review
    surface_finish: raceway_grinding_review
    sealing_quality: seal_and_lubrication_review
    alignment_accuracy: high_precision_review
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: precision low-friction carriage for linear axis motion
  material: carbon_steel_with_rolling_elements_seals_and_lubricant
  scale_or_capacity:
    mass_kg: 0.14
    bom_quantity: 3
    row_total_mass_kg: 0.42
    scale_class: small
  geometry_form: compact_hgl15_linear_guide_carriage
merge_pool:
  eligible: false
  functional_purpose_key: linear_guidance
  precision_guardrails:
    - preload_class_z0
    - accuracy_class_h
    - raceway_surface_finish
    - ball_recirculation
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Precision raceway grinding, heat treatment, ball manufacture, preload setting, seals, lubricant, and inspection are unresolved."
    - "Catalog guideway block is likely an import candidate until precision linear guidance becomes a modeled manufacturing target."
  post_merge_decision_notes: "Final import/local decision is deferred until decomposition separates carriage body, rolling elements, seals, lubricant, and inspection requirements."
kb_staging:
  proposed_item_id: null
  notes: "Do not assign a final closure item ID during row conversion; review with other HGL15 linear guidance rows first."
assumptions:
  - "BOM quantity is 3, so row total mass is about 0.42 kg from the 0.14 kg catalog mass."
  - "Carbon steel material family follows the Hiwin order-code convention; exact alloy and heat treatment remain unresolved."
  - "Small seals, end-return parts, and lubricant are retained as decomposition notes rather than separate row-conversion items."
unresolved:
  - "Exact steel grade, heat treatment, raceway grinding sequence, and preload-setting method."
  - "Seal polymer, lubricant, end-return material, and inspection acceptance criteria."
  - "Whether later KB staging imports a generic linear guide block set instead of modeling individual carriage components."
```
