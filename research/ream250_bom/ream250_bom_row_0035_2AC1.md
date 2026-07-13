---
row_identity:
  item: "2AC1"
  cad_file: "2AC1_part_1"
  source_row_number: 35
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Supported bearing unit for the lower axis/bottom ballscrew support, matching the SLA10 bearing-unit envelope used in the CAD context."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/2AC0_bottom_axis_bearing_SLA10.step; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127"
    cited_fact_or_basis: "BOM row 35 states item 2AC1, quantity 1, cad file 2AC1_part_1, description 'axis bearing bottom'. The CAD context is 2AC0_bottom_axis_bearing_SLA10 with bounding box 86.00 x 24.00 x 58.00 mm; the HIWIN SLA10 page lists type SLA10 and dimensions L 86 mm, B 24 mm, H 58 mm, with bearing type 6200.2RS."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The SLA10 string in the CAD parent assembly identifies the same supported bearing family as the HIWIN SLA10 product page."
  uncertainty_notes:
    - "The leased row's direct STEP product imports with zero solids, so function is inferred from the parent SLA10 bearing assembly and matching external SLA10 dimensions rather than a row-isolated solid."
mass:
  value_kg: 0.526
  basis: "Per-unit mass for quantity 1. FreeCAD measured the SLA10 context assembly volume as 67013.783 mm^3. Using the local generic steel density constant 7850 kg/m^3 gives 67013.783 mm^3 * 1e-9 m^3/mm^3 * 7850 kg/m^3 = 0.526 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/2AC0_bottom_axis_bearing_SLA10.step; kb/materials/properties.yaml; https://www.multiproject.ro/download/Hiwin_Compact.pdf"
    cited_fact_or_basis: "FreeCAD measured 6 solids, volume 67013.783 mm^3, area 20516.186 mm^2, and bounding box 86.00 x 24.00 x 58.00 mm for the retained SLA10 context assembly. The HIWIN compact catalog identifies SLA supported-bearing components as steel pillow block, bearing, and locknut. kb/materials/properties.yaml gives generic steel density as 7850 kg/m^3. targeted_web_search: queries tried: 'SLA10 axis bearing', 'SLA10 bearing bottom', 'SLA10 linear bearing aluminum housing'; result: HIWIN SLA10 pages/catalog matched the geometry and component identity but did not provide a catalog weight."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The retained parent SLA10 assembly volume is a reasonable proxy for this row because 2AC1_part_1 has no row-isolated solids."
    - "A single steel density is used for the complete unit; small seals/grease and bearing internal void details are ignored for planning-scale mass."
  uncertainty_notes:
    - "Mass may double-count or misallocate mass relative to sibling 2AC rows because the row-level CAD product is assembly-only; use as a coarse supported-bearing-unit mass until row-isolated geometry or vendor weight is available."
material:
  primary_material: "Predominantly steel bearing unit: steel pillow block, bearing, and locknut."
  source:
    url_or_path: "https://www.multiproject.ro/download/Hiwin_Compact.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The HIWIN compact catalog labels SLA supported-bearing components as '(1) steel pillow block, (2) bearing, (3) locknut'. Local STEP material extraction for 2AC1_part_1 returned only Generic with density 1000.0, which is placeholder metadata and not treated as resolving material."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The bearing and locknut are treated as steel-family components consistent with standard bearing-unit construction."
  uncertainty_notes:
    - "No row-specific grade, heat treatment, bearing steel grade, seal material, or coating was resolved from the BOM-side STEP metadata."
how_to_make:
  summary: "Locally model as a precision steel pillow-block/bearing assembly"
  manufacturing_steps:
    - "Machine or grind the steel pillow-block housing to the SLA10 mounting envelope and bearing seat geometry."
    - "Manufacture a 6200.2RS deep-groove ball bearing and matching locknut/circlip hardware"
    - "Press the bearing into the pillow block, install the retaining hardware, and inspect shaft height/alignment against the ballscrew support axis."
  source:
    url_or_path: "https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127; https://www.multiproject.ro/download/Hiwin_Compact.pdf; research/ream250_bom/ream250_bom_row_0035_2AC1__views_2x2.png"
    cited_fact_or_basis: "HIWIN identifies SLA10 as a supported bearing with bearing type 6200.2RS and dimensions matching the CAD context. The HIWIN compact catalog states the SLA unit includes a steel pillow block, bearing, and locknut, and notes the pillow block can be fixed from top and bottom with a stop edge for alignment. The CAD preview shows a pillow-block-like bracket with central bearing bore and mounting holes. targeted_web_search: queries tried: 'SLA10 axis bearing', 'SLA10 bearing bottom', 'SLA10 linear bearing aluminum housing'; result: found row-matching SLA10 supported-bearing references but no source that directly states the manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Detailed follow common bearing-unit practice: precision machining/grinding for the housing, separately manufactured bearing elements, then press-fit assembly and inspection"
  uncertainty_notes:
    - "The proposed manufacturing route is inferred from geometry and standard bearing-unit construction; the cited vendor sources support product identity and components, not the full manufacturing process."
kb_implications:
  - "item_granularity: complex_module - Treat as a standard supported bearing unit for this pass; later KB work can split the pillow block, 6200.2RS bearing, locknut, and retaining hardware if row-isolated geometry or a sub-BOM is needed."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0035_2AC1.md
source_research_sha256: "0ddf197c38f28027c5d0d85f261c9824d2e84ba6b42de58631ebc5f769da74cc"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read function, coarse assembly mass basis, steel material evidence, supported-bearing construction route, kb implications, and preview showing a pillow-block bearing unit."
decomposition:
  decision: decompose_into_parts
  rationale: "The row is a supported bearing unit containing a machined pillow block, sealed bearing, locknut, retaining hardware, grease, and alignment requirements. These dependencies should be exposed before merge review."
  proposed_subparts:
    - steel_pillow_block_housing
    - sealed_6200_bearing
    - locknut_and_retaining_hardware
    - grease_and_seal_materials
process_abstraction:
  original_process_family: precision_bearing_unit_machining_and_assembly
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - decomposition_required
    - precision_machining
    - heat_treatment
    - grinding_lapping
    - assembly
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: bearing_manufacturing_small_v0
      fit: partial
      reason: "Closest anchor for precision bearing races, balls, grease, and tight tolerances."
    - process_id: assembly_process_bearing_v0
      fit: supporting
      reason: "Covers assembling bearing rings, balls, cage, seals, and grease into a sealed bearing."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Relevant for the pillow-block housing, though bearing seats require precision guardrails."
    - process_id: precision_grinding_and_scraping_v0
      fit: supporting
      reason: "Relevant to bearing seat and alignment surface finishing."
  abstraction_decision: needs_human
  rationale: "The source item is a catalog supported bearing unit, not just a block. It should remain in precision import/decompose-later until the KB decides whether to localize bearing production."
  process_guardrails:
    tolerance: high_precision_review
    surface_finish: bearing_seat_review
    sealing_quality: sealed_bearing_review
    alignment_accuracy: shaft_axis_alignment_review
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: supported bearing unit for ballscrew shaft support
  material: steel_bearing_unit_with_seals_and_grease
  scale_or_capacity:
    mass_kg: 0.526
    bom_quantity: 1
    row_total_mass_kg: 0.526
    scale_class: small
  geometry_form: sla10_pillow_block_bearing_unit
merge_pool:
  eligible: false
  functional_purpose_key: rotary_support
  precision_guardrails:
    - bearing_seat_tolerance
    - shaft_height_alignment
    - sealed_bearing
    - catalog_unit_identity
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Bearing steel grade, heat treatment, grinding, seal material, grease, and alignment inspection are unresolved."
    - "Row-isolated CAD solids are missing, so mass allocation across sibling rows is uncertain."
  post_merge_decision_notes: "Final import/local decision is deferred until decomposition separates pillow block, sealed bearing, locknut, hardware, and lubricant dependencies."
kb_staging:
  proposed_item_id: null
  notes: "Do not assign a final closure item ID during row conversion; review with other supported bearing units first."
assumptions:
  - "BOM quantity is 1, so row total mass equals the 0.526 kg coarse assembly estimate."
  - "The SLA10 parent assembly and vendor dimensions are sufficient to identify the supported bearing unit despite missing row-isolated solids."
  - "A single steel-family material approximation is acceptable only for row conversion."
unresolved:
  - "Exact bearing steel grade, housing grade, heat treatment, seal material, coating, and grease."
  - "Whether sibling 2AC rows split the same bearing unit into separate CAD pieces."
  - "Shaft-height tolerance, bearing-seat tolerance, and preload/fit requirement."
```
