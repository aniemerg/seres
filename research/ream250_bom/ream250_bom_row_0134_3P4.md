---
row_identity:
  item: "3P4"
  cad_file: "3P4_filter_ISO_K_DN63_CSL-357y2-K"
  source_row_number: 134
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/PK_Z60_511_A"
function:
  summary: "Pfeiffer Vacuum SAS 63 dust separator/inlet particle filter for a DN 63 ISO-K vacuum connection, used to protect the pump from process particles in the pumped gas stream."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/en/shop/products/PK_Z60_511_A; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "BOM row 134 identifies item 3P4 as Pfeiffer Vacuum order number PK Z60 511 A. The Pfeiffer product page names SAS 63, dust separator, DN 63 ISO-K, states order number PK Z60 511 A, and says it is for the inlet flange and protects the pump against particles from the process."
    evidence_basis: "bom_provided"
  assumptions:
    - "In the reAM250 plumbing, this row is treated as the inlet-side particle protection filter assembly associated with the adjacent DN63 ISO-K vacuum line."
  uncertainty_notes:
    - "The CAD contact-sheet render was attempted for the row STEP but did not complete within several minutes and was terminated; function is therefore based on BOM/product identity and FreeCAD geometry measurements rather than visual CAD triage."
mass:
  value_kg: 5.9
  basis: "Per-unit catalog weight for quantity 1. BOM quantity is 1, so the row total is also 5.9 kg. FreeCAD measured the supplied row STEP as one solid with volume 713793.760 mm^3, surface area 611047.693 mm^2, and bounding box about 280.34 x 316.22 x 243.48 mm; this CAD size is consistent with a complete DN63 dust separator assembly, but the catalog weight is used directly."
  source:
    url_or_path: "https://www.ajvs.com/pfeiffer-sas-63-51014; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P4_filter_ISO_K_DN63_CSL-357y2-K.step"
    cited_fact_or_basis: "The row-matched A&J page lists Weight 5.9 kg for Pfeiffer SAS 63 / PK Z60 511 A. FreeCAD measured the row STEP as one solid with volume 713793.760 mm^3 and bounding box 280.34 x 316.22 x 243.48 mm. bom_url_route_check: the BOM-provided Pfeiffer product route was checked via the English canonical product page and matched order number PK Z60 511 A, but the fetched page did not expose weight; the independent A&J page matches the same manufacturer, order number, and product name and supplies the weight."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "Local assembly STEP material extraction returned only Generic at density 1000.0, so STEP material metadata was not used for a density-derived mass."
material:
  primary_material: "corrosion-resistant carbon steel housing with powder-coat finish; stainless steel ISO flange and clips; Buna/NBR-style O-ring seal; replaceable polyester filter insert, with paper insert available as an alternative"
  source:
    url_or_path: "https://www.ajvs.com/pfeiffer-sas-63-51014; https://sraml-kompresorji.si/wp-content/uploads/2022/02/filters_CSL.pdf"
    cited_fact_or_basis: "The row-matched A&J page states the standard filter insert is polyester and paper is available as an alternative. The CSL ISO vacuum filter datasheet for the matching CSL family lists ISO flange connections, stainless steel ISO flange, Buna O-ring sealing, corrosion-resistant carbon steel construction, powder-coat finish, stainless steel torsion clips, and polyester 99%+ removal efficiency standard to 5 micron. bom_url_route_check: the BOM-provided Pfeiffer product route matched the row product identity but the fetched page did not expose component material data, so row-matched distributor facts and the CSL filter-family datasheet were used."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD filename suffix CSL-357y2-K is treated as the CSL-family filter construction represented in the Solberg/CSL ISO filter datasheet for material planning."
  uncertainty_notes:
    - "The exact Pfeiffer-supplied variant may differ in coating details or filter media option, but the sourced facts resolve the main material families needed for KB planning."
how_to_make:
  summary: "Fabricate a vacuum-tight steel filter housing with ISO-K interfaces and install a replaceable pleated filter cartridge and elastomer sealing hardware"
  manufacturing_steps:
    - "Fabricate the DN63 ISO-K vacuum filter housing from corrosion-resistant carbon steel shell parts with stainless ISO flange/interface hardware"
    - "Form or machine the inlet and outlet flange interfaces, sealing grooves, housing lid, and cartridge-retention features."
    - "Apply corrosion-protective powder-coat finish where compatible with the vacuum-side cleanliness requirements."
    - "Install Buna/NBR-style O-ring seals, stainless clips or retention hardware, and the polyester filter insert cartridge."
    - "Clean, assemble, and leak-test the housing; verify installed filter grade, conductance, and pressure-drop suitability before fitting it to the vacuum line."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/en/shop/products/PK_Z60_511_A; https://www.ajvs.com/pfeiffer-sas-63-51014; https://sraml-kompresorji.si/wp-content/uploads/2022/02/filters_CSL.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P4_filter_ISO_K_DN63_CSL-357y2-K.step"
    cited_fact_or_basis: "The Pfeiffer page identifies the purchased SAS 63 dust separator for DN 63 ISO-K. The A&J page gives row-matched performance and scope facts, including integrated filter insert, 5 um separable grain size, 99.7% separation degree, leak-rate data, and 5.9 kg weight. The CSL datasheet gives material and construction features for the matching CSL ISO filter family. FreeCAD measured a large single-solid filter body with bounding box about 280.34 x 316.22 x 243.48 mm. targeted_web_search: queries tried: 'PK Z60 511 A material weight', 'Pfeiffer SAS 63 dust separator material', 'CSL-357y2-K ISO K DN63 filter material', and 'CSL ISO vacuum filter manufacturing'; sources resolved procurement, materials, and filter construction but no row-specific factory process, so detailed fabrication and assembly steps are inferred from the sourced product geometry/materials."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route treats the housing and replaceable filter cartridge as an assembly requiring vacuum leak testing, not as a single machined part."
  uncertainty_notes:
    - "The exact Pfeiffer factory process, weld/forming sequence, coating specification, and cartridge supplier are not sourced."
kb_implications:
  - "item_granularity: simple_part - Model as a replaceable vacuum filter/dust-separator assembly with wear media; later KB work can separate housing, O-rings, clips, and filter cartridge if filter maintenance dominates."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0134_3P4.md
source_research_sha256: "c6e00d586c9d646f45cb13e9df9c3cfb7f624fedc8ceb5b5f4f795f09f797581"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: false
  notes: "Read dust-separator function, catalog mass, multi-material evidence, housing/filter assembly route, and KB implication. No preview image was available; the row itself notes render failure, so geometry use is from product identity and FreeCAD measurements only."
decomposition:
  decision: decompose_into_parts
  rationale: "The row is a multi-material filter assembly with housing, replaceable media, elastomer seal, stainless hardware, coating, and leak-test requirements; flattening it would hide closure dependencies."
  proposed_subparts:
    - steel_filter_housing
    - stainless_iso_k_flange_and_clips
    - elastomer_o_ring_seal
    - polyester_filter_cartridge
    - retention_hardware
process_abstraction:
  original_process_family: vacuum_filter_housing_cartridge_assembly
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - cutting
    - forming
    - joining
    - coating
    - assembly
    - cleaning
    - leak_testing
    - pressure_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: vacuum_seal_assembly_fabrication_v0
      fit: partial
      reason: "Covers vacuum seal hardware assembly, torque/fit checks, and basic leak checks, but lacks filter cartridge modeling."
    - process_id: sheet_metal_fabrication_v0
      fit: supporting
      reason: "Relevant to formed steel shell and housing component fabrication."
    - process_id: welding_tig_basic_v0
      fit: supporting
      reason: "Relevant to leak-tight stainless/steel joining if housing parts are welded."
    - process_id: filtration_basic_v0
      fit: poor_fit
      reason: "Represents filtration as a unit operation, but does not fabricate a filter cartridge assembly."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Covers leak checks needed for the assembled filter housing."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks and basic QA before staging selects detailed tests."
  abstraction_decision: substitute_process_family
  rationale: "The item is a vacuum line filter/dust separator, so the closure handle should preserve connector fit, seal integrity, filter media, coating, cleaning, and leak-test needs rather than treating it as a single machined part."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: high
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: particle filtration and pump protection in a pumped gas stream
  material: steel_housing_stainless_hardware_elastomer_seals_polyester_filter_media_powder_coat
  scale_or_capacity:
    mass_kg: 5.9
    bom_quantity: 1
    row_total_mass_kg: 5.9
    scale_class: large
  geometry_form: dn63_inline_dust_separator_filter_housing_with_replaceable_cartridge
merge_pool:
  eligible: false
  functional_purpose_key: particle_filtration
  precision_guardrails:
    - filter_grade
    - leak_rate
    - flange_standard_fit
    - seal_material
    - pressure_drop
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "Replaceable filter media and seal materials introduce non-metal closure dependencies."
    - "Powder-coat compatibility with cleanliness and outgassing requirements is unresolved."
    - "Filter grade, conductance, pressure drop, and leak-rate acceptance need sourced limits before local substitution."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred; decompose housing, filter media, seals, and hardware before merge review."
kb_staging:
  proposed_item_id: null
  notes: "Do not assign a simple metal fitting ID before decomposition; treat as a filter assembly with consumable media."
assumptions:
  - "Use catalog weight 5.9 kg as the planning mass."
  - "Treat the sourced CSL/Pfeiffer construction as representative for material-family planning."
  - "Treat the selected closure path as vacuum plumbing/filter assembly fabrication plus leak testing."
unresolved:
  - "Exact housing fabrication route, coating specification, and leak-rate acceptance."
  - "Filter cartridge construction details and replacement interval."
  - "Whether paper media variant matters for any reAM250 operating mode."
```
