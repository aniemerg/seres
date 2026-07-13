---
row_identity:
  item: "3O2"
  cad_file: "3O2_curvature_320SWN063"
  source_row_number: 128
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130"
function:
  summary: "Curved/corrugated annular bellows feature from the Pfeiffer Vacuum 320SFK063-130 DN 63 ISO-K spring bellows/flexible vacuum connector, providing compliant vacuum piping geometry in the reAM250 gas/vacuum line."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0128_3O2__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073107/iso-k-spring-bellows.html"
    cited_fact_or_basis: "BOM row 128 and the manifest identify item 3O2 as quantity 1, CAD file 3O2_curvature_320SWN063, description 320SFK063: curvature, manufacturer Pfeiffer Vacuum. The rendered contact sheet shows a thin corrugated circular/annular component about 9.73 x 81.83 x 80.59 mm. The Pfeiffer Vacuum Online Shop page lists 320SFK063-130 under ISO-K Spring Bellows. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130 is a Pfeiffer product route; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists the same 320SFK063-130 order number/global number, and matches the row manufacturer and product family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name 'curvature' and the circular corrugated CAD geometry identify this as a bellows curvature/corrugation element of the 320SFK063-130 connector, not the complete flexible connector assembly."
  uncertainty_notes:
    - "The BOM row decomposes the vendor connector into CAD subfeatures; the exact mating position of this curvature within the full spring-bellows assembly is not named beyond the row label and geometry."
mass:
  value_kg: 0.013
  basis: "Per-unit estimate for BOM quantity 1. FreeCAD measured CAD volume 1618.858 mm^3 = 1.618858e-6 m^3. Using stainless_steel density 8000 kg/m^3 from kb/materials/properties.yaml gives 0.01295 kg, rounded to 0.013 kg per physical item; row total is also about 0.013 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3O2_curvature_320SWN063.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073107/iso-k-spring-bellows.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 1618.858 mm^3, area 16677.041 mm^2, and bounding box 10.06 x 88.44 x 87.18 mm. The Pfeiffer Vacuum Online Shop page states stainless steel construction for 320SFK063-130 spring bellows, with DN 63 bellows in 316L. kb/materials/properties.yaml lists stainless_steel density 8000 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130 is a Pfeiffer product route; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches product 320SFK063-130."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied STEP solid volume is treated as the physical solid volume of one row item."
    - "The local stainless_steel density constant is used for the vendor-stated 316L bellows stainless family."
  uncertainty_notes:
    - "This mass is for the CAD row item only, not the full 320SFK063-130 spring bellows assembly with flanges/end pieces."
material:
  primary_material: "stainless steel bellows material, DN 63 bellows 316L; associated spring-bellows product flanges are stainless steel 304"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073107/iso-k-spring-bellows.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Pfeiffer Vacuum Online Shop technical data states spring bellows material as stainless steel, with flanges 304 and DN 63 to DN 100 bellows 316L. Local assembly STEP material extraction for product 3O2_curvature_320SWN063 returned only placeholder material 'Generic' with density 1000.0, so the vendor route resolves the material. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130 is a Pfeiffer product route; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches product 320SFK063-130."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because the row is named 'curvature' and the CAD preview is a corrugated annular bellows feature, the DN 63 bellows material applies more directly than the flange material."
  uncertainty_notes:
    - "The vendor material statement is for the 320SFK063-130 spring-bellows product family; the row-level CAD subfeature does not carry non-placeholder material metadata."
how_to_make:
  summary: "Form thin 316L stainless bellows corrugations, trim to the required annular geometry, weld or integrate with matching ISO-K end pieces, clean for vacuum service, and leak-test the completed connector"
  manufacturing_steps:
    - "Start from thin 316L stainless tube or sheet stock sized for a DN 63 ISO-K bellows element."
    - "Form the corrugated bellows curvature visible in the CAD preview by bellows forming or hydroforming."
    - "Trim and fixture the corrugated element for integration with the matching end-piece/flange components in the connector assembly."
    - "Weld or otherwise join the bellows element to the adjacent stainless end pieces."
    - "Clean and helium leak-test the vacuum connector for high-vacuum service."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0128_3O2__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3O2_curvature_320SWN063.step; https://vacuum-shop.com/shop/en_US/category/2073107/iso-k-spring-bellows.html"
    cited_fact_or_basis: "The CAD preview shows a thin corrugated annular feature; FreeCAD measured a thin single solid with about 10.06 mm depth and 88.44 x 87.18 mm outer span. The Pfeiffer Vacuum Online Shop page identifies the row-matched product family as ISO-K spring bellows and states stainless steel bellows/flange materials and pressure/temperature service. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130 is a Pfeiffer product route; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches product 320SFK063-130. targeted_web_search: checked the BOM-provided Pfeiffer URL route and searched 'Pfeiffer Vacuum 320SFK063 130 flexible pipe ISO-K DN 63 material weight', '320SFK063 Pfeiffer Vacuum DN 63 flexible pipe datasheet', and 'site:pfeiffer-vacuum.com 320SFK063'; found row-matched product/material/service facts, but no row-specific manufacturing-process specification for the curvature subfeature."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the stainless corrugated bellows geometry and standard vacuum bellows construction practice, not from a Pfeiffer production-process disclosure."
    - "Vacuum service requires clean, welded/integrated stainless joints and leak testing after assembly."
  uncertainty_notes: []
kb_implications:
  - "item_granularity: simple_part - Treat this row as a one-piece stainless corrugated bellows curvature subfeature within a larger purchased spring-bellows connector, not as the complete connector module."
---

# reAM250 BOM Row 128 - 3O2

Research result for the leased reAM250 BOM row only.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0128_3O2.md
source_research_sha256: "0a66500b99871a7c85cb4ae3b2a249f738701268cbbca2bc5d44c43954a6fdec"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the corrugated bellows function, CAD-derived row mass, Pfeiffer stainless bellows material evidence, inferred forming and connector-integration route, and preview showing a thin annular corrugated feature."
decomposition:
  decision: simple_part
  rationale: "The row is one bellows curvature subfeature from a larger spring-bellows connector; the row itself has no internal subparts, while connector-level assembly belongs to related rows."
  proposed_subparts: []
process_abstraction:
  original_process_family: stainless_bellows_forming_and_leak_test
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - forming
    - cutting
    - joining
    - cleaning
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: metal_forming_basic_v0
      fit: partial
      reason: "Covers general forming of metal stock, but not the specialized thin-wall bellows corrugation operation."
    - process_id: tube_forming_process_v0
      fit: partial
      reason: "Relevant to tube-based starting stock for the bellows element, with corrugation details missing."
    - process_id: welding_tig_basic_v0
      fit: supporting
      reason: "Relevant to joining the stainless bellows element to adjacent end pieces in the connector."
    - process_id: plumbing_and_pneumatics_v0
      fit: partial
      reason: "Covers fitting and gas-handling context, but not bellows manufacture."
    - process_id: leak_testing_v0
      fit: direct
      reason: "Matches the vacuum connector leak-test requirement after bellows integration."
    - process_id: cleaning_basic_v0
      fit: supporting
      reason: "Supports vacuum-service cleaning of formed stainless bellows surfaces."
  abstraction_decision: substitute_process_family
  rationale: "The source row is a vendor bellows subfeature; closure analysis should group it under plumbing connector fabrication/testing with specialized forming as a guardrail."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: high
    alignment_accuracy: standard
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: compliant corrugated bellows element for flexible vacuum/gas connector
  material: stainless_steel_316l
  scale_or_capacity:
    mass_kg: 0.013
    bom_quantity: 1
    row_total_mass_kg: 0.013
    scale_class: small
  geometry_form: thin_corrugated_annular_bellows_curvature
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
    - corrugation_flexibility
    - leak_tightness
    - weld_integration
    - vacuum_cleanliness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "Thin-wall stainless bellows corrugation requires specialized forming control."
    - "Vacuum leak-tight welded integration may be harder than ordinary pipe fabrication."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares bellows, flexible connector, and plumbing rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; this row may merge into a flexible plumbing connector abstraction rather than remain a separate closure item."
assumptions:
  - "The row represents the DN 63 316L bellows curvature rather than the complete connector assembly."
  - "Local closure would form and test the bellows as part of a connector fabrication route."
unresolved:
  - "Exact corrugation forming process, wall thickness, cycle-life requirement, and leak-rate requirement are not specified."
  - "Connector-level relationship to adjacent Pfeiffer spring-bellows rows needs group review."
```
