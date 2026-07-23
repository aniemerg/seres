---
row_identity:
  item: "22"
  cad_file: "22_seal_bottom"
  source_row_number: 245
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
function:
  summary: "Bottom perimeter seal formed from Liqui Moly 6185 black silicone sealant; it seals a roughly 355 mm square interface as a thin cured bead or gasket."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0245_22__views_2x2.png; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html"
    cited_fact_or_basis: "The BOM row identifies item 22 as 22_seal_bottom, quantity 1, description 6185 black silicone sealant, manufacturer Liqui Moly; the CAD preview shows a thin square perimeter seal; the BOM-provided product page identifies article 6185 as black silicone sealing compound for sealing joined surfaces."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD perimeter body represents the cured sealant bead applied to the bottom interface, not a separately stocked molded gasket."
  uncertainty_notes: []
mass:
  value_kg: 0.049
  basis: "FreeCAD measured one solid with volume 40498.672 mm^3, surface area 35098.849 mm^2, and bounding box about 355.00 x 355.00 x 3.00 mm. Using the local silicone_rubber density constant of 1200 kg/m^3 gives 0.0486 kg for the cured sealant represented by the CAD solid."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/22_seal_bottom.step; kb/materials/properties.yaml; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html"
    cited_fact_or_basis: "FreeCAD measured volume 40498.672 mm^3 and bounding box 355.00 x 355.00 x 3.00 mm; the BOM-provided Liqui Moly page identifies article 6185 as silicone-based sealing compound; kb/materials/properties.yaml lists silicone_rubber density as 1200 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD volume is treated as cured silicone-rubber volume after application."
    - "The local silicone_rubber density is used as a representative calculation constant for cured silicone sealant."
  uncertainty_notes:
    - "Sealant cure shrinkage, bead compression, and any excess squeeze-out are not represented separately, so the mass is best treated as a CAD-derived installed-seal estimate."
material:
  primary_material: "black silicone sealant / cured silicone rubber"
  source:
    url_or_path: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The BOM row specifies 6185 black silicone sealant from Liqui Moly; the BOM-provided Liqui Moly product page describes the product as silicone-based sealing compound; the assembly STEP material extractor for 22_seal_bottom returned only Generic material with density 1000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "For KB material modeling, the installed bead is represented as cured silicone rubber rather than uncured aerosol/can contents."
  uncertainty_notes:
    - "The exact silicone formulation and fillers are not specified by the BOM row or product page, so the material should remain a broad silicone-sealant family rather than a precise compound."
how_to_make:
  summary: "Model as an applied consumable sealant: dispense black silicone sealant along the bottom perimeter, assemble the mating surfaces immediately, and let it cure into the thin square gasket-like bead."
  manufacturing_steps:
    - "Clean and dry the mating surfaces so they are free of oil and grease."
    - "Dispense Liqui Moly 6185 or equivalent black silicone sealant along the roughly 355 mm square perimeter path."
    - "Join the parts promptly so the bead compresses to the approximately 3 mm CAD thickness."
    - "Allow the sealant to cure, then inspect the perimeter for continuity, adhesion, and excess squeeze-out."
  source:
    url_or_path: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html; research/ream250_bom/ream250_bom_row_0245_22__views_2x2.png"
    cited_fact_or_basis: "The BOM-provided Liqui Moly page states that the surfaces to be sealed should be clean, oil-free, grease-free, and dry, and that material is applied evenly before parts are joined immediately; the CAD preview shows a thin square perimeter bead."
    evidence_basis: "bom_provided"
  assumptions:
    - "The local manufacturing action is application and curing of a external sealant, not synthesis of silicone chemistry"
    - "The CAD preview is used only for the applied path and approximate installed shape."
  uncertainty_notes:
    - "The BOM evidence does not state the actual dispensing nozzle size, cure schedule, or compression target used in the reAM250 assembly."
kb_implications:
  - "item_granularity: simple_part - installed black silicone sealant bead; model as a replaceable or applied part/applied material rather than a reusable part or separate molded gasket."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0245_22.md
source_research_sha256: 26546a33058566570da002c980336dcc0008bff9ab2e1f75d50d554887906afc
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Reviewed the bottom perimeter sealing function, CAD-derived cured bead mass, Liqui Moly silicone sealant evidence,
    dispensing and curing route, KB implication, and preview showing a thin square perimeter seal.
decomposition:
  decision: simple_part
  rationale: The row is one installed sealant bead at an interface. It has no internal assembly dependencies, although the
    source consumable chemistry can stay an upstream material concern for later staging.
  proposed_subparts: []
process_abstraction:
  original_process_family: sealant_dispensing_and_curing
  primary_process_bucket: polymer_elastomer_forming_dispensing
  supporting_processes:
  - cleaning
  - elastomer_forming
  - curing
  - assembly
  - leak_testing
  - dimensional_inspection
  candidate_existing_processes:
  - process_id: seal_installation_v0
    fit: partial
    reason: Covers installing seals and gaskets with general tools, but this row is a dispensed bead instead of a preformed
      seal.
  - process_id: potting_and_sealing_v0
    fit: partial
    reason: Covers compound application and curing for sealing work, though its default scope is electronics potting.
  - process_id: drying_and_curing_v0
    fit: supporting
    reason: Covers the curing portion after the silicone bead is applied and compressed.
  - process_id: cleaning_basic_v0
    fit: supporting
    reason: Surface cleaning is required before applying the silicone sealant.
  - process_id: leak_testing_v0
    fit: supporting
    reason: Relevant when the sealed interface must be checked for continuity and leakage.
  - process_id: inspection_basic_v0
    fit: supporting
    reason: Covers visual and dimensional checks of bead continuity, compression, and excess squeeze-out.
  abstraction_decision: keep_original_family
  rationale: The original route is already sealant dispensing, mating-surface assembly, and curing, so the polymer/elastomer
    forming and dispensing bucket is the direct closure handle.
  process_guardrails:
    tolerance: bead path and compressed thickness should match the roughly square interface geometry
    surface_finish: mating surfaces need cleaning; cut-edge finish is not_applicable
    sealing_quality: continuity, adhesion, cure state, and compression are function-critical
    alignment_accuracy: perimeter path alignment matters, but precision machine alignment is not indicated
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: seal a square bottom machine interface with an applied cured silicone bead
  material: silicone_sealant_cured_silicone_rubber
  scale_or_capacity:
    mass_kg: 0.049
    bom_quantity: 1
    row_total_mass_kg: 0.049
    scale_class: small
  geometry_form: thin_square_perimeter_sealant_bead
merge_pool:
  eligible: true
  functional_purpose_key: interface_sealing
  precision_guardrails:
  - seal_path_geometry
  - compressed_bead_thickness
  - adhesion
  - cure_state
  - leak_integrity
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - polymer_elastomer_forming_dispensing
  import_risk_factors:
  - Exact silicone formulation, fillers, and cure schedule are not specified by the row evidence.
  - Local closure may need a silicone precursor path plus dispensing and curing capability.
  post_merge_decision_notes: Final import/local decision is deferred until merge review compares this with other applied
    sealant beads and gasket-like interface seals.
kb_staging:
  proposed_item_id: null
  notes: Leave final item ID open for merge review; this may merge with other applied silicone interface seals if service
    conditions and bead scale are compatible.
assumptions:
- The CAD body represents the installed cured bead after compression, not the full purchased tube of sealant.
- Silicone rubber density is an acceptable planning constant for the cured bead mass.
- The source product is represented as broad silicone sealant chemistry rather than a vendor-specific SKU.
unresolved:
- Exact compound formulation, cure time, compression target, and service temperature limits are unknown.
- The sealed interface pressure, leakage requirement, and replacement interval are not stated.
```
