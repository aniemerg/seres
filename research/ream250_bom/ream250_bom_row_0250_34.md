---
row_identity:
  item: "34"
  cad_file: "34_flexible_pipe_ISO_KF_DN50_170SFK050-060"
  source_row_number: 250
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/170SFK050_060"
function:
  summary: "Pfeiffer Vacuum 170SFK050-060 DN 50 ISO-KF stainless spring bellows used as a short flexible vacuum connector in the reAM250 gas/vacuum plumbing; the BOM row quantity is 2."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://vacuum-shop.com/shop/en_US/category/2072993/product/170sfk050060/bellows-stainless-steel-flange-1-4301-304-bellows-316l.html; https://vacuum-shop.com/2074314/downloads/datasheets/Datasheet_170SFK050-060_en.pdf"
    cited_fact_or_basis: "BOM row 250 identifies item 34 as quantity 2 of Pfeiffer Vacuum product 170SFK050-060. The Pfeiffer Vacuum Online Shop and data sheet identify 170SFK050-060 as a DN 50 ISO-KF spring bellows with length 60 mm, axial stroke +/-6.5 mm, tightness 1e-11 Pa m3/s, and pressure range 1e-8 hPa to 5e2 hPa over pressure. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/170SFK050_060 corresponds to the row product; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, provides the same order number 170SFK050-060 and Global-No. 2000044741, and links the row-matched English data sheet and STEP file."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.3
  basis: "Per-unit planning estimate for one spring bellows; BOM quantity is 2, so row total is about 0.60 kg. FreeCAD measured the supplied row STEP as one ring-like solid with volume 16479.747 mm^3 and bounding box about 15.00 x 81.18 x 81.18 mm; using stainless_steel_304 density 8030 kg/m^3 gives 0.132 kg for that represented flange/ring volume. The estimate doubles that measured end volume for two flanged ends, then adds about 0.035 kg for the thin 316L corrugated bellows between them."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/34_flexible_pipe_ISO_KF_DN50_170SFK050-060.step; research/ream250_bom/ream250_bom_row_0250_34__views_2x2.png; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2072993/product/170sfk050060/bellows-stainless-steel-flange-1-4301-304-bellows-316l.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 16479.747 mm^3, area 9960.873 mm^2, and bounding box 15.00 x 81.18 x 81.18 mm. The contact sheet shows a short annular ISO-KF flange/bellows-end geometry, not a full 60 mm long connector body. The vendor page identifies the row product as DN 50 ISO-KF, length 60 mm, flange stainless steel 1.4301/304 and bellows stainless steel 316L. kb/materials/properties.yaml lists stainless_steel_304 density 8030 kg/m^3 and stainless_steel density 8000 kg/m^3. targeted_web_search: tried '170SFK050-060 weight kg', '2000044741 kg', '170SFK050-060 datasheet pdf', and the BOM-provided Pfeiffer/vacuum-shop product route; found exact dimensions/materials but no row-specific catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row STEP appears to capture one flanged end or simplified end geometry rather than the complete 60 mm spring bellows, so the mass estimate treats the measured 0.132 kg stainless volume as one end and mirrors it for the second end."
    - "The thin corrugated bellows contribution is modeled as a small additional 316L stainless shell mass of about 0.035 kg."
  uncertainty_notes:
    - "No catalog weight was found for the exact order number; the estimate is suitable for coarse BOM planning but could shift if the STEP omits more of the flanges, uses simplified wall thickness, or the bellows shell is heavier than estimated."
material:
  primary_material: "flange: stainless steel 1.4301/304; bellows: stainless steel 316L"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2072993/product/170sfk050060/bellows-stainless-steel-flange-1-4301-304-bellows-316l.html; https://vacuum-shop.com/2074314/downloads/datasheets/Datasheet_170SFK050-060_en.pdf"
    cited_fact_or_basis: "The Pfeiffer Vacuum Online Shop page and row-matched English data sheet state the material as flange stainless steel 1.4301/304 and bellows stainless steel 316L. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/170SFK050_060 corresponds to the row product; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, provides the same order number 170SFK050-060 and Global-No. 2000044741, and links the same row-matched data sheet and STEP file."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Treat as a vendor vacuum spring-bellows connector for current KB planning; form or hydroform a thin 316L corrugated bellows tube, machine or form two 304/1.4301 ISO-KF flange ends, TIG weld/braze the bellows to the flanges, then clean and helium leak-test the assembly for vacuum service."
  manufacturing_steps:
    - "For local fabrication, make two DN 50 ISO-KF stainless 304/1.4301 flange ends with the 15 mm connection length and sealing geometry."
    - "Form the thin 316L stainless bellows section to the 60 mm overall connector length and required axial compliance."
    - "Join bellows to flanges with vacuum-compatible welding or brazing, then deburr and clean all wetted stainless surfaces."
    - "Inspect dimensions and perform leak testing against the vendor tightness class before installation."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2072993/product/170sfk050060/bellows-stainless-steel-flange-1-4301-304-bellows-316l.html; https://vacuum-shop.com/2074314/downloads/datasheets/Datasheet_170SFK050-060_en.pdf; research/ream250_bom/ream250_bom_row_0250_34__views_2x2.png"
    cited_fact_or_basis: "The row-matched vendor page and data sheet state product identity, length 60 mm, DN 50 ISO-KF connection, flange connection length 15 mm, material split between 304/1.4301 flanges and 316L bellows, pressure range, tightness, and service life. The CAD preview shows an annular ISO-KF end geometry. targeted_web_search: checked the BOM-provided Pfeiffer/vacuum-shop route plus '170SFK050-060 manufacturing', '170SFK050-060 weld bellows', and 'Pfeiffer 170SFK050-060 datasheet'; found product and material data but no source stating Pfeiffer's actual manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the vendor-stated materials, ISO-KF spring-bellows construction, and common vacuum bellows fabrication practice."
    - "Vacuum service requires cleaned stainless parts and leak testing comparable to the vendor-stated tightness."
  uncertainty_notes:
    - "The evidence resolves the external product and performance class, but not Pfeiffer's actual forming, welding, heat treatment, cleaning, or inspection process details"
kb_implications:
  - "item_granularity: simple_part - Treat as a reusable DN50 ISO-KF stainless spring-bellows connector; capture bellows forming, flange joining, cleaning, and leak testing as manufacturing requirements."
---

# reAM250 BOM Row 250 - 34

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0250_34.md
source_research_sha256: "3f7ea10bab57161e8ce7b445458f8b6d6490bfd34ecddbea6dcaa3247711b51c"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the function, quantity, mass basis, stainless material split, inferred bellows/flange manufacturing route, KB implication, and CAD preview showing an annular ISO-KF end geometry."
decomposition:
  decision: simple_part
  rationale: "Although fabricated from flanges and a corrugated bellows, the closure role is a reusable DN50 flexible vacuum plumbing connector; subpart expansion can be deferred unless bellows forming becomes a bottleneck."
  proposed_subparts: []
process_abstraction:
  original_process_family: vacuum_bellows_fabrication
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - forming
    - precision_machining
    - joining
    - cleaning
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: plumbing_and_pneumatics_v0
      fit: partial
      reason: "Covers installation and pressure/leak testing of plumbing assemblies, but not fabrication of a welded stainless bellows connector."
    - process_id: metal_forming_basic_v0
      fit: supporting
      reason: "Relevant to forming the thin corrugated bellows section, though the row may need specialized bellows tooling beyond basic forming."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Applies to ISO-KF flange sealing and mating geometry where dimensional control matters."
    - process_id: welding_tig_basic_v0
      fit: supporting
      reason: "Covers precision stainless welding for leak-tight bellows-to-flange joints."
    - process_id: leak_test_v0
      fit: supporting
      reason: "Directly supports the vacuum tightness check required by the vendor performance class."
  abstraction_decision: substitute_process_family
  rationale: "The vendor route is generalized into a reusable plumbing connector fabrication and test bucket because the closure concern is stainless fluid/vacuum connection capability, not the exact Pfeiffer supply chain."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: high
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: flexible short plumbing connector for DN50 gas and vacuum line compliance
  material: stainless_steel_304_and_316l
  scale_or_capacity:
    mass_kg: 0.3
    bom_quantity: 2
    row_total_mass_kg: 0.6
    scale_class: small
  geometry_form: short_corrugated_bellows_with_iso_kf_dn50_flange_ends
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
    - leak_tightness
    - flange_sealing_geometry
    - axial_compliance
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "Thin corrugated stainless bellows forming and vacuum-grade welded joints may require specialized tooling and inspection."
    - "Vendor tightness target is much stricter than ordinary pressure plumbing and must remain a staging guardrail."
  post_merge_decision_notes: "Final import/local decision is deferred until after merge review compares other DN50 plumbing connectors and leak-tight flexible sections."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a generic stainless DN50 flexible plumbing connector rather than a Pfeiffer-specific item."
assumptions:
  - "The STEP preview appears to show one simplified flange/end feature, so the conversion uses the source research mass estimate rather than CAD volume alone."
  - "Vacuum service is recorded as sealing and leak-test guardrails, not as a separate merge key."
unresolved:
  - "No exact catalog mass was found for the row order number."
  - "Actual bellows forming, weld qualification, cleaning, and helium leak-test procedure remain unspecified."
```
