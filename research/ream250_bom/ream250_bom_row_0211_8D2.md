---
row_identity:
  item: "8D2"
  cad_file: "8D2_flexible_pipe_part_2"
  source_row_number: 211
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250"
function:
  summary: "Thin annular stainless end/flange subpart of the Pfeiffer 120SWG040-0250 DN 40 ISO-KF flexible corrugated vacuum hose, used as part of the vacuum line connection."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2072984/iso-kf-corrugated-hose-flexible-annealed.html"
    cited_fact_or_basis: "The Pfeiffer webshop page lists ISO-KF Corrugated Hose, Flexible, Annealed; order number 120SWG040-0250; DN 40 ISO-KF; A 250 mm; B 41 mm; C 52 mm; bending radius 59 mm. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250; alternate URL https://vacuum-shop.com/shop/en_US/category/2072984/iso-kf-corrugated-hose-flexible-annealed.html is a Pfeiffer Vacuum online shop page with Pfeiffer Vacuum Components & Solutions GmbH contact/copyright and the row-matched order number 120SWG040-0250."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name 'part 2' and the CAD ring geometry identify this as a subpart of the BOM-matched flexible pipe rather than the complete 250 mm hose."
  uncertainty_notes:
    - "The BOM row does not name which hose subcomponent 'part 2' is; the function is assigned from the catalog hose identity plus the local annular CAD shape."
mass:
  value_kg: 0.00249
  basis: "FreeCAD measured one solid with volume 309.686 mm^3 and bounding box 5.319 x 56.284 x 56.284 mm. Using local stainless_steel_304 density 8030 kg/m^3 gives 0.0024868 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8D2_flexible_pipe_part_2.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2072984/iso-kf-corrugated-hose-flexible-annealed.html"
    cited_fact_or_basis: "FreeCAD measured volume 309.686 mm^3 and one solid for the row STEP file; the Pfeiffer webshop page states flange material stainless steel 1.4301/304 for the matched 120SWG040-0250 hose family; kb/materials/properties.yaml lists stainless_steel_304 density 8030 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250; alternate URL https://vacuum-shop.com/shop/en_US/category/2072984/iso-kf-corrugated-hose-flexible-annealed.html is a Pfeiffer Vacuum online shop page with Pfeiffer Vacuum Components & Solutions GmbH contact/copyright and the row-matched order number 120SWG040-0250."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row CAD solid is treated as the full physical volume of this BOM row component."
    - "The row part is treated as stainless steel 1.4301/304 because its ring/flange geometry matches the catalog flange material rather than the bellows tube."
  uncertainty_notes:
    - "If this CAD row is an extracted surface/detail rather than the complete metal subpart, the CAD-derived mass will understate the physical row mass."
material:
  primary_material: "stainless steel 1.4301/304"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2072984/iso-kf-corrugated-hose-flexible-annealed.html"
    cited_fact_or_basis: "The Pfeiffer webshop page states the hose family has flange material stainless steel 1.4301/304 and bellows material stainless steel 316L. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250; alternate URL https://vacuum-shop.com/shop/en_US/category/2072984/iso-kf-corrugated-hose-flexible-annealed.html is a Pfeiffer Vacuum online shop page with Pfeiffer Vacuum Components & Solutions GmbH contact/copyright and the row-matched order number 120SWG040-0250."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD row's thin annular ring/end geometry is assigned to the catalog flange material, not the corrugated bellows material."
  uncertainty_notes:
    - "The local assembly STEP material metadata for this product is only the placeholder 'Generic', so the specific subpart material assignment depends on matching the CAD geometry to the catalog's flange-vs-bellows material split."
how_to_make:
  summary: "Model later as a external flexible vacuum hose subcomponent; Manufacturing requires forming a thin stainless ISO-KF annular/flange ring and integrating it with the corrugated hose assembly"
  manufacturing_steps:
    - "Start from stainless 304 sheet/tube or near-net annular blank sized for the DN 40 ISO-KF hose end."
    - "Cut or deep-draw/roll-form the annular profile, then trim and deburr the vacuum sealing/contact edges."
    - "Clean and inspect the part for vacuum compatibility before joining it into the flexible hose end assembly."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0211_8D2__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8D2_flexible_pipe_part_2.step; https://vacuum-shop.com/shop/en_US/category/2072984/iso-kf-corrugated-hose-flexible-annealed.html"
    cited_fact_or_basis: "The CAD preview shows a thin annular/corrugated ring-like part; FreeCAD measured a 5.319 x 56.284 x 56.284 mm bounding box; the Pfeiffer webshop page identifies the matched product as an ISO-KF flexible corrugated hose with stainless 1.4301/304 flanges and stainless 316L bellows. targeted_web_search: searched \"Pfeiffer Vacuum 120SWG040_0250 flexible pipe material\", \"120SWG040-0250 Pfeiffer flexible pipe\", and \"site:pfeiffer-vacuum.com 120SWG040_0250\" found row-matched catalog material and dimensions but no row-specific manufacturing route for this extracted CAD subpart. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250; alternate URL https://vacuum-shop.com/shop/en_US/category/2072984/iso-kf-corrugated-hose-flexible-annealed.html is a Pfeiffer Vacuum online shop page with Pfeiffer Vacuum Components & Solutions GmbH contact/copyright and the row-matched order number 120SWG040-0250."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The visible annular subpart can be approximated as a formed or machined stainless ring/end feature for KB planning."
    - "The complete Pfeiffer flexible hose should remain a module unless the KB later models corrugated bellows forming, welding/brazing, and vacuum leak testing"
  uncertainty_notes:
    - "The CAD row does not expose the production method, joining details, or tolerances needed for a reliable local manufacturing recipe."
kb_implications:
  - "item_granularity: simple_part - Treat as the annular stainless end/flange subpart of a DN40 ISO-KF flexible hose; rerun if the row needs a concrete local fabrication route rather than only whole-hose procurement."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0211_8D2.md
source_research_sha256: 3fb33ace95af103c18bdbf987b1a8904db086fe7eaf79c8b88f05f75fa6bb498
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Read the catalog-linked function, CAD-derived mass, stainless 304 material evidence, inferred forming/machining route,
    KB implications, and preview image showing a thin annular hose-end ring before conversion.
decomposition:
  decision: simple_part
  rationale: This row is one annular stainless end/flange subpart extracted from a larger flexible service hose assembly.
    The row itself has no internal subparts, but later closure work should still consider the complete hose as a module with
    bellows, end fittings, joining, cleaning, and leak testing.
  proposed_subparts: []
process_abstraction:
  original_process_family: stainless_ring_forming_finishing
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
  - stock_preparation
  - forming
  - precision_machining
  - joining
  - cleaning
  - leak_testing
  - dimensional_inspection
  candidate_existing_processes:
  - process_id: fitting_assembly_basic_v0
    fit: partial
    reason: Covers generic fitting and connector assembly work.
  - process_id: plumbing_and_pneumatics_v0
    fit: partial
    reason: Covers fluid and gas handling connector work at the system level.
  - process_id: leak_testing_v0
    fit: supporting
    reason: Covers leak checks when sealing function matters.
  - process_id: cleaning_basic_v0
    fit: supporting
    reason: Covers cleaning before connector assembly and test.
  - process_id: leak_testing_v0
    fit: supporting
    reason: Relevant when sealing and fluid integrity matter.
  - process_id: welding_basic_v0
    fit: supporting
    reason: Relevant when the row needs permanent joining.
  abstraction_decision: substitute_process_family
  rationale: The thin annular hose end is a plumbing connection interface. Use the shared plumbing connector bucket with forming,
    light machining, cleaning, and integration checks.
  process_guardrails:
    tolerance: required - DN 40 ISO-KF fit and mating geometry must be controlled
    surface_finish: required - contact edges must be clean, deburred, and compatible with plumbing hardware
    sealing_quality: required - the complete hose end participates in a plumbing line connection
    alignment_accuracy: review - ring concentricity and integration with bellows/end assembly may matter
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: provide a plumbing line connection interface at the end of a flexible hose
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 0.00249
    bom_quantity: 1
    row_total_mass_kg: 0.00249
    scale_class: tiny
  geometry_form: thin_annular_hose_end_ring
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
  - mating_fit
  - leak_tightness
  - surface_cleanliness
  - concentricity
  - hose_integration_method
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - plumbing_connector_fabrication_testing
  import_risk_factors:
  - complete flexible service hose manufacturing may require corrugated bellows forming and qualified joining
  - service leak testing and cleanliness requirements are not specified at row level
  - local route depends on the condition that the hose is modeled as a purchased module and decomposed assembly
  post_merge_decision_notes: Final import/local decision is deferred until merge review and later hose-level staging decide
    the condition that this ring is merged with other plumbing connection interfaces and remains part of a decomposed flexible
    hose module.
kb_staging:
  proposed_item_id: null
  notes: Wait for merge review before assigning an item ID; likely candidate for a generalized plumbing line connection interface
    only if material, nominal size, and sealing guardrails align.
assumptions:
- The row CAD solid represents the physical annular subpart for BOM quantity 1.
- The stainless 304 catalog flange material applies to this ring rather than the bellows material.
- A general forming plus machining route is adequate at closure level if cleaning and inspection are included.
unresolved:
- The exact hose-end subcomponent role, joining process, tolerance stack, and leak-test requirements are not exposed by the
  row CAD.
- The row may understate physical mass if the CAD export is only a surface/detail rather than the complete metal subpart.
- Later staging must decide the condition that to model the complete flexible hose as an import, decompose it, and replace
  it with another plumbing line abstraction.
```
