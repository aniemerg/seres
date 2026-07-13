---
row_identity:
  item: "1B61"
  cad_file: "1B61_seal"
  source_row_number: 17
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.lisema.eu/"
function:
  summary: "Replaceable elastomer seal/gasket for the schlieren imaging door area, providing compression sealing around the optical-door/cover interface."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/1B50_schlieren_imaging_door.step; research/ream250_bom/ream250_bom_row_0017_1B61__views_2x2.png"
    cited_fact_or_basis: "BOM row 17 names item 1B61 as 1B61_seal from Lisema; manifest maps the row to the 1B50_schlieren_imaging_door assembly; FreeCAD/rendered preview shows a small annular gasket-like body with approximately 55.88 x 39.87 x 45.80 mm bounding box."
    evidence_basis: "bom_provided"
  assumptions:
    - "Interpreted as a compression seal because the BOM row name is seal, the supplier is a gasket vendor, and the rendered geometry is annular/gasket-like."
  uncertainty_notes:
    - "CAD export status is assembly_only; the raw STEP does not contain a 1B61 product label, so exact placement within the door assembly is not independently resolved."
mass:
  value_kg: 0.0028
  basis: "Per unit for quantity 1. FreeCAD measured 2573.818 mm^3 for the canonical STEP shape; using the local kb/materials/properties.yaml nitrile_rubber density constant of 1100 kg/m^3 gives 2573.818e-9 m^3 * 1100 kg/m^3 = 0.00283 kg, rounded to 0.0028 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/1B50_schlieren_imaging_door.step; kb/materials/properties.yaml; https://lisema.eu/Moosgummiprofile-Hohlkammer"
    cited_fact_or_basis: "FreeCAD measured one solid, 2573.817841 mm^3 volume, 3560.408063 mm^2 area, and 55.88 x 39.87 x 45.80 mm bounding box; local properties list nitrile_rubber density as 1100 kg/m^3; LiSEMA's seal-profile pages show EPDM/NBR/CR sponge-rubber seal families. targeted_web_search: tried 'site:lisema.eu Dichtung Lisema Moosgummiprofile Halbrund EPDM seal' and 'lisema.eu Moosgummiprofile Halbrund material EPDM'; found Lisema seal-family material pages but no 1B61-specific catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid volume is treated as the best available row-scale volume, despite the assembly_only export limitation."
    - "NBR density is used as a solid elastomer proxy because local density data covers NBR/nitrile rubber and the Lisema evidence supports NBR as one plausible family."
  uncertainty_notes:
    - "If the actual Lisema part is sponge rubber/foam rather than solid elastomer, real mass may be lower than the solid-density estimate."
    - "No 1B61-specific vendor mass or material grade was found."
material:
  primary_material: "elastomer sealing material in LiSEMA EPDM/NBR/CR sponge-rubber or rubber-profile families"
  source:
    url_or_path: "https://www.lisema.eu/; https://lisema.eu/Moosgummiprofile-Hohlkammer; https://lisema.eu/EPDM-Flachdichtungen"
    cited_fact_or_basis: "The BOM row identifies Lisema as the manufacturer and links to Lisema; Lisema lists NEOSOFT moosgummi profiles in EPDM, NBR, and CR families, and its flat-gasket page lists custom gasket materials including silicone, silicone foam, EPDM, NBR, CR, cellular rubber, sponge rubber, and FKM/Viton."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because row 1B61 has no product ID or grade, the material is kept at the supplier-supported family level instead of selecting a specific elastomer grade."
  uncertainty_notes:
    - "STEP material extraction from the full assembly returned no matches for 1B61_seal."
    - "The exact grade, hardness, adhesive backing, and foam/open-cell versus solid construction remain unresolved."
how_to_make:
  summary: "Prepare as a cut-to-size Lisema gasket/profile where practical; cut or join elastomer gasket/profile stock to the CAD outline and install it as a replaceable compression seal"
  manufacturing_steps:
    - "Select compatible elastomer gasket/profile stock from EPDM, NBR, CR, silicone, or FKM family based on temperature, chemical, and compression requirements."
    - "Cut the profile or sheet to the annular/door-seal outline, with scarfed or bonded joint if made from linear profile."
    - "Apply adhesive backing or compatible gasket adhesive if the installation requires retention."
    - "Install in the door/cover interface and compression-check for continuous contact."
  source:
    url_or_path: "https://www.lisema.eu/; https://lisema.eu/Moosgummiprofile-Hohlkammer; https://lisema.eu/EPDM-Flachdichtungen; research/ream250_bom/ream250_bom_row_0017_1B61__views_2x2.png"
    cited_fact_or_basis: "Lisema is the BOM-listed seal supplier and offers standard/profile and custom drawing-based gasket routes; the CAD preview shows a compact ring/gasket form. targeted_web_search: tried 'Lisema 1B61 seal', '1B61_seal Lisema', and 'Lisema custom gasket drawing EPDM NBR'; no row-specific 1B61 manufacturing note was found, only supplier-family procurement routes."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Detailed cutting/joining steps are inferred from common gasket/profile manufacturing practice and the CAD shape, not directly stated for this BOM row."
  uncertainty_notes:
    - "A production BOM should preserve this as a external or cut consumable unless later evidence identifies an exact Lisema catalog/profile number"
kb_implications:
  - "item_granularity: simple_part - Model as a replaceable elastomer seal/gasket replaceable or applied part, not as a multi-part assembly or precision machine component."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0017_1B61.md
source_research_sha256: "5d496a6de45a2990d440cc250ba2311e37b638aa6ce4f516ba3c495e32f1b167"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the schlieren door compression-seal function, 0.0028 kg mass estimate, Lisema elastomer-family evidence, cut gasket/profile route, KB implication, and CAD preview showing a compact annular gasket form."
decomposition:
  decision: simple_part
  rationale: "The row is a single replaceable elastomer seal/gasket and has no internal closure dependencies beyond material stock, cutting, joining, adhesive retention, and installation."
  proposed_subparts: []
process_abstraction:
  original_process_family: elastomer_gasket_cutting_profile_joining
  primary_process_bucket: polymer_elastomer_forming_dispensing
  supporting_processes:
    - elastomer_forming
    - cutting
    - joining
    - curing
    - cleaning
    - dimensional_inspection
    - leak_testing
    - assembly
  candidate_existing_processes:
    - process_id: elastomer_molding_basic_v0
      fit: partial
      reason: "Covers generic elastomer forming but does not identify the row-specific Lisema profile family."
    - process_id: gasket_sheet_cut_to_part_v0
      fit: supporting
      reason: "Anchors gasket cutting from stock when the final design uses sheet gasket material."
    - process_id: seal_installation_v0
      fit: supporting
      reason: "Covers installing the finished seal at the door/cover interface."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Relevant if the optical-door interface requires verified environmental sealing."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers visual, dimensional, and compression-contact checks."
  abstraction_decision: substitute_process_family
  rationale: "The source route is a supplier gasket/profile family, but closure can use the shared elastomer forming, cutting, joining, inspection, and installation bucket without creating a row-specific purchased part."
  process_guardrails:
    tolerance: low_to_moderate
    surface_finish: compression_surface_review
    sealing_quality: review
    alignment_accuracy: low
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "replaceable compression seal for an optical door cover interface"
  material: unresolved_elastomer_seal_family
  scale_or_capacity:
    mass_kg: 0.0028
    bom_quantity: 1
    row_total_mass_kg: 0.0028
    scale_class: small
  geometry_form: compact_annular_elastomer_gasket
merge_pool:
  eligible: true
  functional_purpose_key: environment_barrier
  precision_guardrails:
    - sealing_quality
    - compression_set
    - elastomer_family
    - gasket_cross_section
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - polymer_elastomer_forming_dispensing
  import_risk_factors:
    - "Exact elastomer family, hardness, adhesive backing, cellular construction, and compression-set performance are unresolved."
    - "Assembly-only CAD export leaves exact door placement and mating groove uncertain."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this with other door, cover, and optical-interface seal rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a generic small elastomer compression gasket if material and sealing requirements converge."
assumptions:
  - "BOM quantity is 1 and row total mass is treated as 0.0028 kg from the available CAD-volume estimate."
  - "The row is modeled as supplier-family elastomer seal stock cut to a compact annular shape."
  - "Leak testing is only a supporting guardrail because the row does not state a leak-rate requirement."
unresolved:
  - "Exact Lisema material grade, density, hardness, foam state, adhesive retention, and mating groove geometry are unknown."
  - "Whether this seal should merge with larger door seals depends on material and compression requirements."
```
