---
row_identity:
  item: "1B52"
  cad_file: "1B52_flange_schlieren_imaging"
  source_row_number: 16
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Flange associated with the reAM250 schlieren-imaging door, likely serving as a mounting, spacing, or retaining ring for the optical/imaging opening."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/1B50_schlieren_imaging_door.step; research/ream250_bom/ream250_bom_row_0016_1B52__views_2x2.png"
    cited_fact_or_basis: "BOM row 16 names item 1B52 as quantity 1, '1B52_flange_schlieren_imaging'. Manifest row 16 maps it to the 1B50_schlieren_imaging_door assembly with status assembly_only. The rendered canonical STEP preview shows a small annular/oval ring form."
    evidence_basis: "bom_provided"
  assumptions:
    - "The 'flange_schlieren_imaging' name is interpreted mechanically as an optical-port mounting or retaining flange rather than as an optical element."
  uncertainty_notes:
    - "The CAD export did not isolate a 1B52-prefixed product, so the visible canonical shape may represent the enclosing 1B50 door assembly proxy rather than the exact standalone flange."
mass:
  value_kg: 0.0202
  basis: "Per-unit estimate for quantity 1. FreeCAD measured the canonical assembly-only STEP as 1 solid, volume 2573.818 mm^3, area 3560.408 mm^2, bounding box about 55.88 x 39.87 x 45.80 mm. Using the local generic steel density constant 7850 kg/m^3 gives 2573.818e-9 m^3 * 7850 kg/m^3 = 0.0202 kg per item."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/1B50_schlieren_imaging_door.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured the canonical STEP volume as 2573.818 mm^3. kb/materials/properties.yaml lists generic steel density as 7850 kg/m^3. targeted_web_search: queries tried: 'EOS M290 reAM250 schlieren imaging flange material', 'reAM250 schlieren imaging door flange 1B52', and 'EOS additive manufacturing schlieren imaging process monitoring window flange'; no row-specific usable mass or material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Generic steel density is used as a conservative metal-flange planning proxy because no row-specific material metadata was available."
    - "The measured assembly-only canonical STEP volume is treated as the best available per-unit geometry proxy for this row."
  uncertainty_notes:
    - "If the missing isolated 1B52 flange corresponds instead to larger sibling schlieren-imaging flange geometry, the true mass could be much higher than this assembly-proxy estimate."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The BOM and manifest identify the row as a schlieren-imaging flange but do not state material. Assembly STEP material extraction for product '1B52_flange_schlieren_imaging' returned no matches; extraction for '1B50_schlieren_imaging_door' returned a product match with no material or density property. targeted_web_search: queries tried: 'EOS M290 reAM250 schlieren imaging flange material', 'reAM250 schlieren imaging door flange 1B52', and 'EOS additive manufacturing schlieren imaging process monitoring window flange'; no row-specific usable material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A flange in this machine location is modeled as metallic because the BOM name and CAD shape indicate a structural retaining/mounting part."
  uncertainty_notes:
    - "Specific alloy and grade remain unresolved; downstream KB work should avoid assigning aluminum, carbon steel, or stainless steel without better row evidence."
how_to_make:
  summary: "Manufacture as a simple custom metal flange matched to the schlieren-imaging door interface"
  manufacturing_steps:
    - "Start from metal plate, tube, or near-net ring stock sized for the optical-door opening."
    - "Machine or cut the annular/oval profile and mating faces to fit the schlieren-imaging door."
    - "Deburr, clean, and inspect fit against the door, seal, and cover interfaces before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/1B50_schlieren_imaging_door.step; research/ream250_bom/ream250_bom_row_0016_1B52__views_2x2.png"
    cited_fact_or_basis: "BOM row name identifies a flange for schlieren imaging; the rendered canonical CAD preview shows an annular/oval ring. targeted_web_search: queries tried: 'EOS M290 reAM250 schlieren imaging flange material', 'reAM250 schlieren imaging door flange 1B52', and 'EOS additive manufacturing schlieren imaging process monitoring window flange'; no row-specific usable manufacturing drawing or vendor route was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Machining or profile cutting from metal stock is the simplest plausible route for a one-piece custom flange with this CAD shape."
  uncertainty_notes:
    - "No source states the actual fabrication method, tolerances, finish, or whether this row was external or made in-house"
kb_implications:
  - "item_granularity: simple_part - Treat as a one-piece custom flange/ring unless later evidence shows it is a calibrated vendor module or a multi-part optical assembly."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0016_1B52.md
source_research_sha256: a61e5870e1e61ad07192597720799480eb151c331fa3f133a34a8a9bfb3e7358
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Read function, proxy mass basis, unknown-metal material evidence, machining/cutting route, KB implication, and CAD
    preview showing a small annular/oval flange before conversion.
decomposition:
  decision: simple_part
  rationale: The row is best treated as a one-piece flange and retaining ring for the schlieren-imaging door interface; no
    internal closure-relevant subassemblies are evidenced.
  proposed_subparts: []
process_abstraction:
  original_process_family: custom_metal_profile_cutting_machining
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
  - stock_preparation
  - cutting
  - precision_machining
  - deburring
  - surface_finishing
  - dimensional_inspection
  - leak_testing
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
  - process_id: leak_testing_v0
    fit: supporting
    reason: Relevant when sealing and fluid integrity matter.
  abstraction_decision: keep_original_family
  rationale: The source route already points to machining and cutting a simple metal flange from stock. General subtractive
    machining best preserves the optical-door mating faces and ring profile without introducing a special flange process.
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: mounting spacing and retaining flange for an optical imaging door opening
  material: unknown_metal_alloy
  scale_or_capacity:
    mass_kg: 0.0202
    bom_quantity: 1
    row_total_mass_kg: 0.0202
    scale_class: small
  geometry_form: annular_oval_flange_ring
merge_pool:
  eligible: true
  functional_purpose_key: optical_port_mounting_retention
  precision_guardrails:
  - optical_port_alignment
  - mating_face_flatness
  - seal_interface_fit
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - general_subtractive_machining
  import_risk_factors:
  - Specific alloy and grade are unresolved.
  - The isolated 1B52 geometry was not found; the mass and shape use the best available assembly-only proxy.
  - Optical-door alignment, surface finish, and any sealing requirement may impose tighter tolerances than a generic flange.
  post_merge_decision_notes: Final import/local decision is deferred until after merge review; compare with other optical-port
    flanges and small interface rings before assigning an item ID.
kb_staging:
  proposed_item_id: null
  notes: Wait for merge review because this may merge with other small optical-port and interface-retaining flanges if material
    and precision guardrails are compatible.
assumptions:
- The row is a metallic mechanical flange rather than an optical element and calibrated vendor module.
- The BOM quantity is one and the row total mass equals the proxy per-unit mass.
- General subtractive machining can satisfy the required profile and mating faces if tolerances are reviewed later.
unresolved:
- Exact alloy, grade, finish, coating, and sealing role are unknown.
- The true standalone 1B52 geometry may differ from the assembly-only proxy used in the research row.
- Merge review must decide the condition that optical-port guardrails require this flange to stay separate from generic interface
  flanges.
```
