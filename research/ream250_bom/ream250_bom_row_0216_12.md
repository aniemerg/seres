---
row_identity:
  item: "12"
  cad_file: "12_flat_seal_back"
  source_row_number: 216
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
function:
  summary: "Applied rear flat seal bead/gasket for the reAM250 assembly, made from Liqui Moly 6185 black silicone sealant and forming a long rectangular perimeter seal."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/12_flat_seal_back.step; research/ream250_bom/ream250_bom_row_0216_12__views_2x2.png; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
    cited_fact_or_basis: "BOM row 216 identifies item 12, quantity 1, CAD file 12_flat_seal_back, product 6185 black silicone sealant, manufacturer Liqui Moly, and a Liqui Moly product URL. The manifest maps the row to one matched vendor-component STEP. FreeCAD measured one solid with bounding box 840.00 x 3.00 x 400.00 mm, and the contact sheet shows a thin rectangular perimeter seal. The Liqui Moly page describes 6185 as a silicone-based sealing compound for sealing assemblies."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file represents the cured or applied seal geometry for the single physical BOM row item, not the full 200 ml retail container."
  uncertainty_notes:
    - "The row evidence identifies this as the back flat seal but does not show the mating faces or compression condition in the final machine assembly."
mass:
  value_kg: 0.0869
  basis: "Per-unit estimate for quantity 1. FreeCAD measured volume 72427.433 mm^3 = 0.000072427433 m^3 for the applied seal geometry. Using the local silicone_rubber density constant of 1200 kg/m^3 gives 0.086913 kg, rounded to 0.0869 kg. The row total is the same because the BOM quantity is 1."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/12_flat_seal_back.step; kb/materials/properties.yaml; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 72427.433 mm^3, area 62770.442 mm^2, and bounding box 840.00 x 3.00 x 400.00 mm. The Liqui Moly page identifies product 6185 as a silicone-based sealing compound. kb/materials/properties.yaml lists silicone_rubber density_kg_per_m3: 1200."
    evidence_basis: "bom_provided"
  assumptions:
    - "The cured/applied seal density is approximated by the local silicone_rubber density constant."
    - "The CAD volume is treated as the physical volume of one applied back seal bead/gasket."
  uncertainty_notes:
    - "Actual cured sealant density and final compressed volume may differ from the local representative silicone-rubber constant and the uncompressed CAD export."
material:
  primary_material: "black silicone-based sealing compound / cured silicone elastomer"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
    cited_fact_or_basis: "BOM row 216 names product 6185 as black silicone sealant from Liqui Moly. The Liqui Moly product page describes it as a silicone-based sealing compound and lists article 6185 as a 200 ml aerosol can variant."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The product page resolves the material family but not the exact cured formulation, filler package, pigment composition, or durometer."
how_to_make:
  summary: "Prepare Liqui Moly 6185 black silicone sealant, clean and dry the mating surfaces, dispense the sealant uniformly along the CAD-defined rear perimeter, then assemble the parts immediately so the bead cures as the back flat seal"
  manufacturing_steps:
    - "Prepare Liqui Moly 6185 black silicone sealant or a functionally equivalent silicone sealing compound"
    - "Clean the rear sealing surfaces so they are dry and free of oil and grease."
    - "Apply the sealant uniformly along the back perimeter matching the 12_flat_seal_back CAD path."
    - "Join the mating parts immediately after application and allow the sealant to cure in place."
    - "Inspect for continuous coverage and absence of gaps, smears into functional openings, or obvious underfilled sections."
  source:
    url_or_path: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/12_flat_seal_back.step; research/ream250_bom/ream250_bom_row_0216_12__views_2x2.png"
    cited_fact_or_basis: "The Liqui Moly page states that 6185 is supplied in an automatic cartridge/aerosol can, identifies article 6185 as 200 ml, and instructs users to clean/dry/degrease sealing surfaces, apply material evenly, and assemble parts immediately. The STEP/contact sheet provides the rear rectangular perimeter path and 3 mm thickness for this row's applied seal geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "Inspection is modeled as a basic assembly-quality check because the cited product page gives application guidance but not reAM250-specific quality-control criteria."
  uncertainty_notes:
    - "Machine's assembly conditions, or acceptance test for leak tightness"
kb_implications:
  - "item_granularity: simple_part - Model as an applied silicone sealant/gasket replaceable or applied part tied to a CAD-defined bead path, not as a reusable machine part or purchased module."
---

Research result for the leased reAM250 BOM row only.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0216_12.md
source_research_sha256: 2382409166eb2f9c1203e9fdfd1f6a2229096c2554ab0b94b878b2a3bd2a6c1c
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Read the function, CAD-derived mass basis, silicone sealant material evidence, in-place dispensing and cure route,
    KB implications, and CAD preview showing a thin rectangular rear perimeter bead before conversion.
decomposition:
  decision: simple_part
  rationale: The row represents one applied silicone sealant bead/gasket with no hidden subassembly, electronics, mechanism,
    and no vendor module requiring decomposition.
  proposed_subparts: []
process_abstraction:
  original_process_family: sealant_surface_preparation_dispensing_cure
  primary_process_bucket: polymer_elastomer_forming_dispensing
  supporting_processes:
  - elastomer_forming
  - curing
  - cleaning
  - assembly
  - dimensional_inspection
  - leak_testing
  candidate_existing_processes:
  - process_id: elastomer_molding_basic_v0
    fit: partial
    reason: Covers basic elastomer forming when the row becomes a local seal element.
  - process_id: potting_and_sealing_v0
    fit: partial
    reason: Covers dispensed sealing material and encapsulation style work.
  - process_id: drying_and_curing_v0
    fit: supporting
    reason: Covers curing after polymer and elastomer placement.
  - process_id: seal_installation_v0
    fit: supporting
    reason: Covers installation when the row is treated as a seal in an assembly.
  - process_id: leak_testing_v0
    fit: supporting
    reason: Relevant when sealing and fluid integrity matter.
  abstraction_decision: keep_original_family
  rationale: 'The source route already belongs to the shared polymer dispensing bucket: clean mating surfaces, dispense a
    continuous bead, assemble, cure, and inspect.'
  process_guardrails:
    tolerance: review bead path, bead volume, and compression gap
    surface_finish: review cleanliness and mating-face condition
    sealing_quality: review
    alignment_accuracy: not_applicable
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: elastic perimeter seal between rear mating machine panels and housings
  material: black_silicone_elastomer_sealant
  scale_or_capacity:
    mass_kg: 0.0869
    bom_quantity: 1
    row_total_mass_kg: 0.0869
    scale_class: small
  geometry_form: thin_rectangular_dispensed_perimeter_bead_840x400x3mm
merge_pool:
  eligible: true
  functional_purpose_key: perimeter_panel_barrier
  precision_guardrails:
  - bead_continuity
  - compression_set
  - mating_surface_cleanliness
  - leak_contamination_limit
  - thermal_and_powder_compatibility
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - polymer_elastomer_forming_dispensing
  import_risk_factors:
  - exact cured silicone formulation, additives, pigment, and durometer are unresolved
  - local silicone polymer and sealant-compounding supply chain may be outside near-term closure scope
  - service temperature, powder exposure, outgassing, and leak-tightness requirements are not specified
  post_merge_decision_notes: Final import/local manufacture decision is deferred until merge review compares similar perimeter
    seals and later staging resolves local chemistry, import treatment, and generic elastomer gasket substitution.
kb_staging:
  proposed_item_id: null
  notes: Wait for merge review before assigning a closure item ID; likely compare with other applied silicone perimeter seals
    such as the top/bottom flat seal row.
assumptions:
- The CAD solid is treated as the installed and cured sealant bead volume for one rear seal.
- A generic black silicone elastomer sealant is an acceptable closure abstraction for Liqui Moly 6185 unless service evidence
  requires a specific commercial formulation.
- A general labor bot and simple dispensing tool can apply and inspect the bead if surface cleanliness and bead continuity
  requirements are met.
unresolved:
- Exact cured formulation, filler package, pigment, hardness, and compression-set behavior are not identified.
- The row does not specify sealed medium, pressure level, leak criterion, thermal exposure, powder contamination exposure,
  and cure acceptance test.
- Whether later lunarized design should retain dispensed sealant, substitute a cut/molded elastomer gasket, and adjust mating
  geometry remains a merge and staging decision.
```
