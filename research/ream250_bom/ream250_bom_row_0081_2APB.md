---
row_identity:
  item: "2APB"
  cad_file: "2APB_spring_block_back"
  source_row_number: 81
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Back spring block for the reAM250 build-platform/heating-plate area; model as a long narrow mechanical support or preload block paired with the front, right, and left spring blocks."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APB_spring_block_back.step; research/ream250_bom/ream250_bom_row_0081_2APB__views_2x2.png"
    cited_fact_or_basis: "BOM row 81 lists item 2APB, quantity 1, CAD file '2APB_spring_block_back'. Nearby BOM rows 79-82 list matching front, right, back, and left spring blocks. The manifest maps row 81 to a matched_existing part STEP. FreeCAD measured one solid with a bounding box about 22.00 x 205.00 x 15.00 mm; the rendered preview shows a long narrow block with planar faces, a lengthwise relieved or tapered feature, and small end features."
    evidence_basis: "bom_provided"
  assumptions:
    - "The four named spring blocks form a set around the adjacent spring plate, assembly plate, heating plate, and build-platform rows."
  uncertainty_notes:
    - "The exact load path or spring interface is not named in the BOM, so the function is limited to mechanical support/preload-block level."
mass:
  value_kg: 0.422
  basis: "FreeCAD measured volume 53766.281 mm^3, which is 0.0000537663 m^3. Using generic steel density 7850 kg/m^3 from the local density table gives 0.422 kg per unit. Quantity is 1, so the row total is also about 0.422 kg. If later material evidence shows aluminum instead, the same CAD volume would be about 0.145 kg using 2700 kg/m^3."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APB_spring_block_back.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, 53766.281 mm^3 volume, 16102.915 mm^2 area, and about 22.00 x 205.00 x 15.00 mm bounding box. The local density table lists steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. targeted_web_search: searched '2APB_spring_block_back material', '2APB spring_block_back reAM250', 'reAM250 spring_block_back', and '2APB_spring_block_back manufacturing'; results repeated the public BOM identity but did not provide row-specific mass or material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is a usable per-unit physical volume for this custom machined block."
    - "A steel-like density is the best planning assumption for a spring/preload block when no row-specific material is provided."
  uncertainty_notes:
    - "Mass is material-sensitive; if the block is aluminum rather than steel, the per-unit mass would be roughly one third of the stated value."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0081_2APB__views_2x2.png"
    cited_fact_or_basis: "BOM row 81 names the part '2APB_spring_block_back' but provides no manufacturer, product ID, material family, or grade. Assembly STEP material extraction for product '2APB_spring_block_back' returned material 'Generic' with density 1000.0, which is placeholder metadata. The rendered preview shows a simple block-like solid. targeted_web_search: searched '2APB_spring_block_back material', '2APB spring_block_back reAM250', 'reAM250 spring_block_back', and 'spring block reAM250 material'; no row-specific material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A load-bearing spring block in this location is treated as metal stock unless later evidence identifies a polymer or ceramic."
  uncertainty_notes:
    - "The exact alloy and grade remain unresolved; downstream KB modeling should avoid a grade-specific material until a drawing or native CAD material source is found."
how_to_make:
  summary: "Machine the spring block from rectangular metal bar or plate stock, creating the long block profile, end features, and lengthwise relieved or tapered face, then deburr and inspect fit against the spring-block assembly."
  manufacturing_steps:
    - "Cut rectangular metal stock slightly oversize for a finished block about 22.00 x 205.00 x 15.00 mm."
    - "Mill the long faces, end features, and lengthwise relieved or tapered geometry visible in the STEP model."
    - "Deburr edges and inspect length, width, thickness, flatness, and fit with the adjacent spring block or spring plate interfaces."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APB_spring_block_back.step; research/ream250_bom/ream250_bom_row_0081_2APB__views_2x2.png"
    cited_fact_or_basis: "The STEP file contains one solid with a long 22.00 x 205.00 x 15.00 mm bounding box; the rendered preview shows a simple elongated block with planar faces, small end features, and a lengthwise relieved or tapered feature. targeted_web_search: searched '2APB_spring_block_back material', '2APB spring_block_back reAM250', 'reAM250 spring_block_back', and '2APB_spring_block_back manufacturing'; no row-specific vendor or manufacturing route was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is custom fabricated rather than external as a catalog module because the BOM provides no vendor or standard designation and the CAD is a simple single-solid block"
  uncertainty_notes:
    - "The exact tolerances, heat treatment, and surface finish are not available from the BOM-side evidence."
kb_implications:
  - "item_granularity: simple_part - Treat as a custom machined metal block; consolidate with the other spring-block rows if later KB modeling can represent orientation variants with one reusable spring_block part."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0081_2APB.md
source_research_sha256: "ca22c34df6e2f5f48fb82bfd21c902aacfacbf267c3e342fd7ba10aaf2c3bc7e"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the spring-block support function, CAD-derived steel-assumption mass, unresolved metal material evidence, machining route, and long narrow block geometry before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one custom block solid with no internal parts, fasteners, springs, electronics, nor module evidence."
  proposed_subparts: []
process_abstraction:
  original_process_family: machined_metal_spring_block
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - deburring
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: metal_cutting_basic_v0
      fit: supporting
      reason: "Covers cutting bar and plate stock to rough block length."
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers general machining of the long block, end features, and relieved face."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant if spring preload faces require tighter flatness and parallelism."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers length, width, thickness, flatness, and fit checks."
  abstraction_decision: keep_original_family
  rationale: "The source route is machining from rectangular metal stock, which directly matches the general subtractive machining bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: mechanical support and preload block for spring plate assembly
  material: structural_metal_unknown_steel_assumed_for_mass
  scale_or_capacity:
    mass_kg: 0.422
    bom_quantity: 1
    row_total_mass_kg: 0.422
    scale_class: small
  geometry_form: long_narrow_machined_block_with_relief_feature
merge_pool:
  eligible: true
  functional_purpose_key: preload_support
  precision_guardrails:
    - material_family
    - length
    - flatness
    - preload_face_geometry
    - orientation_variant
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Material uncertainty changes mass and may affect spring preload stiffness."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review; compare with front, right, and left spring-block rows before choosing a shared closure item."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with the spring-block set before assigning a closure item ID."
assumptions:
  - "The block is load-bearing metal stock."
  - "Steel density is a conservative planning assumption until material evidence improves."
  - "Back, front, right, and left spring blocks may be orientation variants of one closure item."
unresolved:
  - "Exact alloy, heat treatment, finish, and preload tolerance are not specified."
  - "The load path within the spring plate and heating plate assembly needs group-level review."
```
