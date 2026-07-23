---
row_identity:
  item: "8D1"
  cad_file: "8D1_flexible_pipe_part_1"
  source_row_number: 210
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250"
function:
  summary: "Thin annular end/flange component for the Pfeiffer Vacuum 120SWG040-0250 DN 40 ISO-KF flexible pipe assembly, providing one circular vacuum connection interface rather than representing the full hose."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8D1_flexible_pipe_part_1.step; research/ream250_bom/ream250_bom_row_0210_8D1__views_2x2.png"
    cited_fact_or_basis: "BOM row 210 identifies item 8D1 as Pfeiffer Vacuum 'part 1 120SWG040-0250: flexible pipe'; the manifest maps row 210 to 8D1_flexible_pipe_part_1.step; FreeCAD measured one solid with an approximately 5.32 x 56.28 x 56.28 mm bounding box; the rendered preview shows a thin circular ring/end feature."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-specific CAD part is interpreted as one end/flange part of the 120SWG040-0250 flexible pipe because the BOM splits neighboring row 8D2 as part 2 of the same vendor product."
  uncertainty_notes:
    - "The CAD part represents an exported subcomponent of the flexible pipe, so the function is for this annular end part rather than the complete hose assembly."
mass:
  value_kg: 0.00249
  basis: "Per-unit mass for one CAD part. FreeCAD measured volume 309.686 mm^3, converted to 3.09686e-7 m^3; using local stainless_steel_304 density 8030 kg/m^3 gives 0.00249 kg. BOM quantity is 1, so the row total is also about 0.00249 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8D1_flexible_pipe_part_1.step; kb/materials/properties.yaml; https://vacuum-shop.com/2074220/downloads/datasheets/Datasheet_120SWG040-0250_en.pdf"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 309.686 mm^3 for 8D1_flexible_pipe_part_1.step; kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3; the row-matched 120SWG040-0250 datasheet identifies the DN 40 ISO-KF flexible hose flange material as stainless steel 1.4301/304. official_alternate_route_check: the original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250 returned HTTP 403 to curl; the alternate PDF is a Pfeiffer Vacuum datasheet for the same 120SWG040-0250 product and same DN 40 ISO-KF family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical volume of one row item."
    - "The annular end part uses the stainless 304/1.4301 flange material from the matched 120SWG040-0250 flexible-pipe product family."
  uncertainty_notes:
    - "If the CAD export omits small weld beads, rolled edges, or other nonmodeled end-piece details, the true mass may be modestly higher."
material:
  primary_material: "Stainless steel 1.4301 / AISI 304 flange/end-ring material; the complete 120SWG040-0250 flexible pipe family also uses 316L stainless bellows."
  source:
    url_or_path: "https://vacuum-shop.com/2074220/downloads/datasheets/Datasheet_120SWG040-0250_en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The row-matched 120SWG040-0250 datasheet identifies a DN 40 ISO-KF stainless flexible hose and lists flange material as stainless steel 1.4301/304 with 316L bellows; local assembly STEP material extraction for this CAD product returns only Generic material with density 1000, which does not resolve material. official_alternate_route_check: the original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250 returned HTTP 403 to curl; the alternate PDF is a Pfeiffer Vacuum datasheet for the same 120SWG040-0250 product and same DN 40 ISO-KF family."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because the rendered row CAD is the end-ring/flange-like subpart, the flange material is more applicable to this row than the bellows material."
  uncertainty_notes:
    - "The local STEP file does not carry a real material assignment for this subpart; material assignment depends on matching the row to the vendor product family."
how_to_make:
  summary: "Locally, model this as a stainless 304 annular ISO-KF end/flange part: cut or turn a ring blank, machine the vacuum sealing/profile features, deburr and clean for vacuum service, then weld or join it to the flexible hose assembly during later hose fabrication."
  manufacturing_steps:
    - "Start from stainless 304 / 1.4301 bar, tube, or near-net ring stock sized for the approximately 56 mm outside diameter and 5 mm axial thickness."
    - "Turn the outer diameter, inner bore, and side faces on a lathe; add the small flange/end profile features indicated by the CAD preview."
    - "Deburr, passivate or clean for vacuum service, and inspect the DN 40 ISO-KF sealing/interface geometry."
    - "Join to the stainless bellows or hose body in the later flexible-pipe assembly workflow."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8D1_flexible_pipe_part_1.step; research/ream250_bom/ream250_bom_row_0210_8D1__views_2x2.png; https://vacuum-shop.com/2074220/downloads/datasheets/Datasheet_120SWG040-0250_en.pdf"
    cited_fact_or_basis: "CAD evidence shows a one-piece thin annular geometry; the row-matched datasheet identifies the product family as a DN 40 ISO-KF flexible stainless hose and gives stainless 1.4301/304 flange material. targeted_web_search: queries tried included '120SWG040-0250 manufacturing flange', 'Pfeiffer 120SWG040-0250 datasheet flange material', and 'ISO-KF stainless flange manufacturing machining'; no row-specific source stated the manufacturing process for this exported subpart, so the route is inferred from geometry and material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A machined stainless ring is the simplest Manufacturing route for this exported end/flange subpart at the BOM-row level."
    - "The eventual complete flexible pipe would need separate bellows forming and joining steps; those are outside this row's part-1 CAD scope."
  uncertainty_notes:
    - "Actual vendor production may use forming, stamping, or welded subfeatures not visible in the single exported STEP solid."
kb_implications:
  - "item_granularity: simple_part - Model row 8D1 as a simple stainless annular end/flange part of a standard flexible vacuum pipe assembly; represent hose length and complete bellows assembly behavior in related rows or later BOM notes rather than as a separate granularity label for this row."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0210_8D1.md
source_research_sha256: ae6582dc6f632a06529874a8bd27333f444fb49d292d5ac721a4163cb26b1088
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Reviewed the original function, CAD-derived mass and BOM quantity, stainless flange material evidence, inferred turning
    route, KB implication, and CAD preview showing a thin annular end/interface component rather than the full flexible hose.
decomposition:
  decision: simple_part
  rationale: The row represents one exported annular end/flange subpart of a flexible service pipe assembly. It should not
    be decomposed further at row level; the complete hose/bellows assembly dependencies belong in related rows and later assembly
    modeling.
  proposed_subparts: []
process_abstraction:
  original_process_family: lathe_machining
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
  rationale: The thin annular end ring is a plumbing connection interface. Use the shared plumbing connector bucket with turning,
    deburring, cleaning, and inspection rather than a service-specific process label.
  process_guardrails:
    tolerance: Outer diameter, inner bore, and DN 40 ISO-KF interface dimensions need inspection against plumbing hardware
      fit.
    surface_finish: Sealing/interface faces must be deburred and clean enough for sealed service.
    sealing_quality: The part contributes to a plumbing connection interface, so profile quality and cleanliness matter even
      if the seal element is modeled elsewhere.
    alignment_accuracy: Concentricity and face parallelism should be controlled enough for later joining to the hose and bellows
      body.
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: circular plumbing connection interface for a flexible pipe and hose assembly
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 0.00249
    bom_quantity: 1
    row_total_mass_kg: 0.00249
    scale_class: small
  geometry_form: thin_annular_end_ring
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
  - service_interface_profile
  - sealing_face_finish
  - concentricity
  - joining_surface_cleanliness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - plumbing_connector_fabrication_testing
  import_risk_factors:
  - The complete flexible pipe also requires stainless bellows and hose fabrication and joining, which are outside this row's
    simple end-part scope.
  - Service cleanliness and sealing profile requirements may be more stringent than ordinary stainless ring hardware.
  post_merge_decision_notes: Final import/local decision is deferred until merge review compares this with other plumbing
    connection interface parts and later flexible-pipe assembly rows.
kb_staging:
  proposed_item_id: null
  notes: Leave item ID open for merge review; likely a reusable stainless plumbing connection interface and end-ring candidate
    if similar rows converge.
assumptions:
- The CAD solid is treated as one annular end part, not the full 120SWG040-0250 flexible pipe.
- The row uses stainless 304/1.4301 flange material from the matched product family.
- Hose length, bellows material, and joining steps will be handled in related rows and later assembly abstraction.
unresolved:
- Actual vendor production route may include forming and welded details not visible in the exported STEP solid.
- Exact interface tolerances and cleaning/passivation requirements are not specified.
- Merge review must decide the condition that this can share one closure item with other DN-sized plumbing connection end
  parts.
```
