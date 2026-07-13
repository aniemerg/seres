---
row_identity:
  item: "91F1"
  cad_file: "91F1_square_profile_DIN_EN_10219-2_80x80x5_150"
  source_row_number: 291
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Short 80 x 80 x 5 mm square hollow structural section, 150 mm long, used as a compact frame/spacer member in the reAM250 mechanical structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0291_91F1__views_2x2.png"
    cited_fact_or_basis: "BOM row 291 identifies item 91F1 as quantity 1, CAD file 91F1_square_profile_DIN_EN_10219-2_80x80x5_150, description square hollow section; the manifest maps the same row to a matched part STEP; the preview shows an open-ended square tube with rounded corners and no added holes or brackets."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted as a structural spacer/frame member because the BOM description and CAD geometry are a square hollow section, but the exact mounting location is not named in the row."
  uncertainty_notes:
    - "No parent assembly name or installation notes were provided, so the exact load path or mating parts remain unresolved."
mass:
  value_kg: 1.690
  basis: "FreeCAD measured one solid with volume 215342.917 mm^3 and bounding box 80.00 x 80.00 x 150.00 mm. The assembly STEP material metadata reports Steel, Mild with density 7850 kg/m^3. Per-unit mass = 215342.917 mm^3 * 1e-9 m^3/mm^3 * 7850 kg/m^3 = 1.690 kg. BOM quantity is 1, so row total is also about 1.690 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91F1_square_profile_DIN_EN_10219-2_80x80x5_150.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 215342.917 mm^3, area 89008.406 mm^2, and bounding box 80.00 x 80.00 x 150.00 mm; local assembly STEP material extraction for 91F1_square_profile_DIN_EN_10219-2_80x80x5_150 reports material Steel, Mild and density 7850.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP part volume is treated as the physical volume of one BOM-row item."
    - "The assembly STEP density is interpreted as kg/m^3, consistent with the reAM250 material extractor note."
  uncertainty_notes:
    - "The CAD volume includes modeled corner radii and any STEP simplifications; it should be preferred over a sharp-corner tube hand calculation for this row, but remains CAD-derived rather than weighed."
material:
  primary_material: "mild steel structural square hollow section"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://knowledge.bsigroup.com/products/cold-formed-welded-steel-structural-hollow-sections-tolerances-dimensions-and-sectional-properties"
    cited_fact_or_basis: "Local assembly STEP material extraction for this product reports Steel, Mild with density 7850.0; BSI describes BS EN 10219-2 as covering cold-formed welded steel structural hollow sections, including square sections."
    evidence_basis: "bom_provided"
  assumptions:
    - "The DIN EN 10219-2 designation is used as corroboration that this row is a steel structural hollow section, while the row-specific STEP metadata resolves the material family as mild steel."
  uncertainty_notes:
    - "The exact EN steel grade, such as S235 or S355, is not specified by the BOM row, filename, or extracted STEP metadata."
how_to_make:
  summary: "Produce EN 10219-2-compatible mild-steel square hollow section stock and cut it to the 150 mm finished length; form steel strip into a square tube, longitudinally weld it, size it to 80 x 80 x 5 mm, then saw/cut and deburr the short section"
  manufacturing_steps:
    - "Start from mild-steel strip/coil or structural tube stock suitable for square hollow sections."
    - "For local tube production, cold-form the strip into an 80 x 80 mm square hollow profile and longitudinally weld the seam."
    - "Size/calibrate the profile to the required 5 mm wall and square-section tolerance class."
    - "Cut one 150 mm length from the tube stock."
    - "Deburr and inspect length, squareness, and open-end condition before assembly."
  source:
    url_or_path: "https://knowledge.bsigroup.com/products/cold-formed-welded-steel-structural-hollow-sections-tolerances-dimensions-and-sectional-properties; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91F1_square_profile_DIN_EN_10219-2_80x80x5_150.step"
    cited_fact_or_basis: "BSI identifies EN 10219-2 as a standard for cold-formed welded steel structural hollow sections and says it covers square sections and dimensions/tolerances; the row CAD measures an 80.00 x 80.00 x 150.00 mm open square tube. targeted_web_search: searched \"EN 10219-2 square hollow section cold formed welded structural steel tubes standard title\" and \"DIN EN 10219-2 square hollow section 80x80x5 steel tube\" found standard/catalog evidence for the stock family but no row-specific factory routing for item 91F1."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Cutting from standard EN 10219-2 square hollow section stock is the most plausible route for this simple structural row."
    - "The cold-forming and welding steps describe local tube-stock production"
  uncertainty_notes:
    - "Cut, cut in-house, or fabricated from strip"
kb_implications:
  - "item_granularity: simple_part - model as a reusable mild-steel square hollow structural section/cut tube length rather than a machine-specific assembly."
---

Research result for reAM250 BOM row 291.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0291_91F1.md
source_research_sha256: "d9dc183e500c9aefb4a35df35c5f401c82cafd924dd48f79fe82f380b34ed2f1"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the row research, CAD preview, CAD-derived mass basis, mild steel material metadata, EN 10219-2 stock evidence, and cut square-tube manufacturing route before conversion."
decomposition:
  decision: simple_part
  rationale: "This is a single short square hollow section with no added holes, brackets, electronics, moving elements, sealing interfaces, and calibration features. Treat it as reusable structural stock cut to length."
  proposed_subparts: []
process_abstraction:
  original_process_family: cold_formed_welded_structural_tube_cut_to_length
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - stock_preparation
    - forming
    - joining
    - cutting
    - deburring
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: cutting_basic_v0
      fit: direct
      reason: "Covers sawing/cutting stock into the required 150 mm length, followed by rough edge cleanup."
    - process_id: metal_forming_basic_shop_v0
      fit: partial
      reason: "Represents local forming of metal stock when tube stock must be produced from strip; lacks the dedicated welded tube sizing details."
    - process_id: welding_and_fabrication_v0
      fit: partial
      reason: "Covers combined structural steel cutting, forming, seam welding, fitting, and cleanup for locally made tube stock."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers length, squareness, wall condition, open-end condition, and basic dimensional checks before use in the frame."
  abstraction_decision: keep_original_family
  rationale: "The source route already belongs to structural hollow profile production followed by cut-to-length finishing. The lunarized closure handle should keep that profile-stock family without expanding this simple row into a machine-specific frame item."
  process_guardrails:
    tolerance: basic
    surface_finish: basic
    sealing_quality: not_applicable
    alignment_accuracy: basic
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: compact structural frame and spacer member
  material: mild_steel
  scale_or_capacity:
    mass_kg: 1.69
    bom_quantity: 1
    row_total_mass_kg: 1.69
    scale_class: small
  geometry_form: square_hollow_structural_tube_cut_length
merge_pool:
  eligible: true
  functional_purpose_key: structural_spacer
  precision_guardrails:
    - length
    - squareness
    - wall_thickness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
    - cutting_basic_v0
    - welding_and_fabrication_v0
  import_risk_factors:
    - "Exact EN steel grade is unresolved; closure can likely use generic mild steel unless later load review requires a named grade."
    - "If local tube-stock production is selected, seam welding and sizing capability must be represented upstream."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred until merge review compares this with other small structural spacers and profile-stock members."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a generic mild-steel square hollow structural spacer/profile item."
assumptions:
  - "BOM quantity is 1 and CAD-derived row mass is 1.690 kg."
  - "Mild steel is adequate for closure identity because the exact EN grade was not present in the source evidence."
  - "Cutting from structural tube stock is the Phase 1 abstraction; full welded tube production can be modeled upstream only when needed."
unresolved:
  - "Exact parent assembly, load path, and named EN steel grade remain unknown."
  - "Merge review must decide whether 80 x 80 x 5 mm geometry stays distinct from other small structural profile spacers."
```
