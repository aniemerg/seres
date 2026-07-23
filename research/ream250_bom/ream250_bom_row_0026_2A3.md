---
row_identity:
  item: "2A3"
  cad_file: "2A3_slide_HGL15CA2R600Z0H_part_1"
  source_row_number: 26
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.hiwin.de/de/Produkte/Profilschienenf%C3%BChrungen/Auswahl-%C3%BCber-Laufwagen/Baureihe-HG-QH/HGL/HGL15CAZ0H/p/5-001374"
function:
  summary: "HIWIN HGL15CAZ0H low square linear-guide carriage/slide block for the reAM250 2A axis. It rides on an HGR15 profile rail and provides high-stiffness, low-friction guided linear motion for the moving structure attached to the carriage."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A3_slide_HGL15CA2R600Z0H_part_1.step; research/ream250_bom/ream250_bom_row_0026_2A3__views_2x2.png; https://www.hiwin.de/en/Products/Linear-guideways/Blocks/Ball-guides/Series-HG-QH/HGL/HGL15CAZ0H/p/5-001374"
    cited_fact_or_basis: "BOM row 26 identifies item 2A3 as quantity 1, linear guide slide, manufacturer HIWIN, CAD file 2A3_slide_HGL15CA2R600Z0H_part_1, and links to the HIWIN HGL15CAZ0H product route. The manifest maps that row to the matched existing vendor component STEP. The same-domain HIWIN product route identifies HGL15CAZ0H under HGL ball-guide blocks in Series HG/QH linear guideways. CAD measurement found one solid with bounding box 34.00 x 69.56 x 19.70 mm, and the rendered contact sheet shows a compact carriage block form."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM label slide is interpreted as the carriage/block rather than the rail because the row's product URL and CAD filename identify the HGL15CAZ0H block; adjacent row 2A51 covers the matching linear guide rail."
  uncertainty_notes:
    - "The exact reAM250 axis load path and fastener interface are not specified by the BOM row, so the section describes the standard carriage function rather than the full installed-axis function."
mass:
  value_kg: 0.14
  basis: "Per-unit mass is 0.14 kg for one HGL15CA block/carriage. Quantity is 1, so the row total is also about 0.14 kg. FreeCAD measured CAD volume 32117.287 mm^3 and bounding box 34.00 x 69.56 x 19.70 mm; the catalog mass is preferred because the carriage is a multi-material bearing assembly and the STEP material is placeholder Generic."
  source:
    url_or_path: "https://www.reiman.pt/pub/media/technical_data/hiwin/datasheets/hgl15caz0h.pdf; https://www.tuli-shop.com/us/hiwin-linear-block-hgl-15-ca-z0-h; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A3_slide_HGL15CA2R600Z0H_part_1.step"
    cited_fact_or_basis: "HIWIN datasheet table for HGL15CA lists weight m = 0.14 kg with dimensions W 34 mm and L 61.4 mm. The Tuli product page for HGL 15 CA Z0 H also lists Weight [kg] 0.1400. FreeCAD measured the row STEP as 1 solid, volume 32117.287 mm^3, area 9939.172 mm^2, and bounding box 34.00 x 69.56 x 19.70 mm. bom_url_route_check: the BOM-provided HIWIN URL identifies the same HGL15CAZ0H product route; the directly parsed official datasheet and distributor page were used for the mass value because the BOM product page route did not expose the weight in the captured page text."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "Catalog mass is used over CAD-density calculation because the STEP volume does not expose separate volumes for steel body, balls, retainer, seals, grease nipple, lubricant, or end-cap components."
material:
  primary_material: "chrome/bearing steel linear-guide carriage with steel balls and non-metal seal/retainer/end-cap components"
  source:
    url_or_path: "https://www.alibaba.com/product-detail/hiwin-linear-guide-HGL15-HGL15CA_1600369376261.html; https://www.lm76.com/HG-Series-Catalog_opt.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "An independent HGL15CA product listing states material Chrome steel, model number HGL15CA, brand HIWIN, and core components Bearing. The HIWIN HG-series catalog construction diagram names block, rail, end cap, retainer, bottom seal, ball, grease nipple, and piping joint as guideway components. Local assembly STEP material extraction for this row returned only Generic with density 1000.0, which is placeholder material evidence rather than a material callout. bom_url_route_check: the BOM-provided HIWIN HGL15CAZ0H route and HIWIN datasheet resolve the product identity and configuration but did not expose a specific material grade in the captured text, so the material family uses a row-matched independent product listing plus HIWIN construction context."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Chrome steel is treated as the main load-bearing steel family for the carriage body/raceway and rolling elements; small seals, retainer, end-cap, and lubricant details are kept broad because no row-specific material split was found."
  uncertainty_notes:
    - "The exact steel grade, heat treatment, coating, seal polymer, and retainer/end-cap polymer are not identified by the available row-matched evidence."
how_to_make:
  summary: "Do not model a row-level manufacturing route for this pass. Treat the HGL15CAZ0H linear-guide carriage as a complex precision motion module that must be decomposed in later KB work before any local manufacturing process is claimed."
  manufacturing_steps:
    - "Defer detailed manufacturing until a separate linear-guide-carriage sub-BOM is created."
    - "Future decomposition should resolve at least the carriage body/raceways, recirculating balls, end caps, retainer, seals, grease nipple or lubrication interface, lubricant, heat treatment, precision grinding/lapping, cleaning, assembly, preload control, and accuracy inspection."
  source:
    url_or_path: "https://www.reiman.pt/pub/media/technical_data/hiwin/datasheets/hgl15caz0h.pdf; https://www.hiwin.de/en/Products/Linear-guideways/Blocks/Ball-guides/Series-HG-QH/HGL/HGL15CAZ0H/p/5-001374; https://www.lm76.com/HG-Series-Catalog_opt.pdf; research/ream250_bom/ream250_bom_row_0026_2A3__views_2x2.png"
    cited_fact_or_basis: "The HIWIN datasheet identifies the order specification HGL15CAZ0H, block preserved, HGL15CAZ0H (1 pcs.), and grease nipple straight loose; it also gives M4 mounting and the configuration attributes. The HIWIN product route matches the same product family and model. The HG-series catalog describes the guideway construction as block, rail, end cap, retainer, bottom seal, ball, grease nipple, and related lubrication components. The rendered contact sheet confirms the row CAD is a compact carriage-like module, not raw stock or a simple machined block. targeted_web_search: searched \"Hiwin HGL15CAZ0H datasheet\", \"HGL15CAZ0H material\", \"HGL15CAZ0H weight\", and \"HGL15CA chrome steel\" no row-matched source found a complete manufacturing process, heat treatment, tolerance stack, or component-level sub-BOM for local production."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because this is a precision recirculating linear-guide carriage, row-level manufacturing is intentionally not specified until the module is decomposed."
  uncertainty_notes:
    - "The exact component sub-BOM, steel grades, heat treatment, grinding/lapping process, seal materials, lubrication details, tolerances, and inspection sequence are unresolved."
kb_implications:
  - "item_granularity: complex_module - model as a reusable complex precision linear-guide carriage for this pass; only split into steel body, balls, seals, retainer/end caps, lubricant, and inspection processes if linear-guide imports become a priority."
---

Research result for reAM250 BOM row 26.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0026_2A3.md
source_research_sha256: "cbb7d4ea474e8a76b775b0cc9dc0695d438c29b7695d2365a4766c5809eabe66"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the HIWIN linear-guide carriage function, 0.14 kg catalog mass with BOM quantity 1, chrome/bearing-steel plus nonmetal component evidence, deferred manufacturing route, KB implication, and CAD preview showing a compact recirculating carriage module."
decomposition:
  decision: complex_module
  rationale: "The carriage contains precision raceways, rolling balls, seals, end caps, retainer features, lubricant, preload control, and inspection dependencies; these internals matter for closure if local manufacture is attempted."
  proposed_subparts:
    - carriage_body_raceway
    - recirculating_balls
    - end_caps
    - retainer_elements
    - seals
    - grease_nipple
    - lubricant_charge
process_abstraction:
  original_process_family: vendor_precision_linear_guide_carriage
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - decomposition_required
    - import_assumption
    - precision_machining
    - grinding_lapping
    - heat_treatment
    - assembly
    - calibration
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_precision_v0
      fit: partial
      reason: "Relevant to carriage body and rail-interface features, but does not cover recirculating ball guideway manufacturing."
    - process_id: precision_grinding_basic_v0
      fit: supporting
      reason: "Relevant to hardened raceway surfaces and preload-critical sliding accuracy."
    - process_id: heat_treatment_hardening_v0
      fit: supporting
      reason: "Relevant to bearing steel raceway and rolling element hardness."
    - process_id: bearing_set_heavy_production_v0
      fit: partial
      reason: "Covers some rolling-bearing manufacturing concepts, but linear carriage ball recirculation and preload are not represented directly."
    - process_id: assembly_basic_v0
      fit: supporting
      reason: "Relevant to final placement of balls, seals, end caps, lubricant, and grease fitting after precision parts exist."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Basic QA anchor; later staging needs accuracy, preload, smoothness, and dimensional inspection beyond the generic process."
  abstraction_decision: needs_human
  rationale: "A precision linear-guide carriage should not be reduced to a simple machined block. It should remain an import/decompose-later precision component until the KB has a deliberate linear-guidance manufacturing model."
  process_guardrails:
    tolerance: high
    surface_finish: high
    sealing_quality: review
    alignment_accuracy: high
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: "low friction precision linear motion carriage for a guided machine axis"
  material: chrome_bearing_steel_with_polymer_seals_and_lubricant
  scale_or_capacity:
    mass_kg: 0.14
    bom_quantity: 1
    row_total_mass_kg: 0.14
    scale_class: small
  geometry_form: compact_square_linear_guide_carriage_block
merge_pool:
  eligible: false
  functional_purpose_key: linear_guidance
  precision_guardrails:
    - preload
    - raceway_surface_finish
    - rolling_element_quality
    - alignment_accuracy
    - seal_materials
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Precision raceways, rolling balls, preload control, seals, lubricant, and accuracy inspection create a high closure burden."
    - "Component-level sub-BOM, steel grades, heat treatment, and grinding/lapping process are unresolved."
  post_merge_decision_notes: "Final import/local decision is deferred; compare with other guideway blocks and rails before deciding whether to keep a generic linear-guidance import candidate."
kb_staging:
  proposed_item_id: null
  notes: "Do not assign a simple closure item ID at row conversion; decomposition and merge review should decide the linear-guide carriage abstraction."
assumptions:
  - "BOM quantity is 1 and row total mass is the catalog carriage mass of 0.14 kg."
  - "Chrome/bearing steel is treated as the main load-bearing material, with nonmetal seals and lubricant kept as unresolved secondary materials."
  - "The CAD preview confirms carriage form but does not expose internal ball path, preload, seal, and grease features."
unresolved:
  - "Exact steel grade, heat treatment, ball grade, seal polymer, grease type, preload class, and inspection sequence remain unresolved."
  - "Whether linear-guide carriages are imported as modules, decomposed locally, and merged across sizes is deferred."
```
