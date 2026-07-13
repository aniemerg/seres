---
row_identity:
  item: "38"
  cad_file: "38_T_pipe_ISO_K_DN63_320RTS063"
  source_row_number: 254
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RTS063"
function:
  summary: "DN 63 ISO-K vacuum tee fitting that branches one ISO-K vacuum line into a perpendicular third DN63 port while preserving clamp/seal interfaces for the reAM250 vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/38_T_pipe_ISO_K_DN63_320RTS063.step; research/ream250_bom/ream250_bom_row_0254_38__views_2x2.png; https://vacuum-shop.com/shop/en_US/category/2073069/product/320rts063/tee-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 254 identifies item 38 as Pfeiffer Vacuum product 320RTS063 named 38_T_pipe_ISO_K_DN63_320RTS063; the manifest maps the row to the matching STEP file. The Pfeiffer Vacuum Online Shop product page identifies 320RTS063 as a Tee, stainless steel 1.4301/304, with DN 63 ISO-K connection. FreeCAD measured one solid with bounding box about 176.00 x 140.57 x 105.13 mm, and the rendered contact sheet shows a three-port tee with ISO-style flanged ends. official_alternate_route_check: original BOM URL is the Pfeiffer product route for 320RTS063; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches order number 320RTS063 plus Global-No. 2000042718."
    evidence_basis: "bom_provided"
  assumptions:
    - "The three visible flanged ports are treated as vacuum plumbing interfaces, not as structural mounts."
  uncertainty_notes: []
mass:
  value_kg: 1.84
  basis: "Per-unit estimate for quantity 1. FreeCAD measured CAD volume 229667.765 mm^3 = 0.000229667765 m^3. Using kb/materials/properties.yaml stainless_steel_304 density 8030 kg/m^3 gives 0.000229667765 * 8030 = 1.844 kg, rounded to 1.84 kg. BOM quantity is 1, so the row total is also about 1.84 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/38_T_pipe_ISO_K_DN63_320RTS063.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073069/product/320rts063/tee-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 229667.765 mm^3. The row-matched Pfeiffer Vacuum Online Shop page identifies product 320RTS063 as stainless steel 1.4301/304. kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3. official_alternate_route_check: original BOM URL is the Pfeiffer product route for 320RTS063; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches order number 320RTS063 and Global-No. 2000042718."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied single-solid CAD volume is used as the physical tee metal volume for one purchased item."
  uncertainty_notes:
    - "No catalog weight was found on the row-matched product page, so this is a CAD-volume-derived mass rather than a vendor-stated shipping or measured part weight."
material:
  primary_material: "stainless steel 1.4301/304"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073069/product/320rts063/tee-stainless-steel-1-4301-304.html; .venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/extract_step_materials.py --step design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step --product-name 38_T_pipe_ISO_K_DN63_320RTS063"
    cited_fact_or_basis: "The row-matched Pfeiffer Vacuum Online Shop page lists product 320RTS063 under Stainless steel 1.4301/304. Local assembly STEP material extraction for 38_T_pipe_ISO_K_DN63_320RTS063 returned only Generic material with density 1000.0, which is placeholder metadata and was not used to resolve material. official_alternate_route_check: original BOM URL is the Pfeiffer product route for 320RTS063; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches the same 320RTS063 tee row."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Form or cut a 304/1.4301 stainless tee body, attach three ISO-K flange ends, finish sealing faces, clean for vacuum service, and leak-test"
  manufacturing_steps:
    - "For local manufacture, prepare 304/1.4301 stainless tube/tee stock and three compatible ISO-K DN63 flange ends."
    - "Join the perpendicular tee branch and flange ends with vacuum-compatible welding or formed pulled-port fabrication, then remove burrs and clean internal surfaces."
    - "Machine or finish seal-adjacent flange lips/faces, passivate or clean as required for vacuum plumbing, and leak-test the completed tee."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073069/product/320rts063/tee-stainless-steel-1-4301-304.html; https://www.n-c.com/vacuum-flanges-fittings/tees/iso-k-iso-f; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/38_T_pipe_ISO_K_DN63_320RTS063.step"
    cited_fact_or_basis: "The Pfeiffer Vacuum Online Shop page identifies the row as a DN63 ISO-K stainless 1.4301/304 tee. Pfeiffer Vacuum+Fab Solutions states ISO-K/ISO-F tee fittings are made from 304 stainless steel pulled port tubing and ISO-K flanges, with full size tees offering three equal-size flanged connections. The CAD preview shows a three-port flanged tee. targeted_web_search: queries tried: '320RTS063 Pfeiffer T-piece DN63 ISO-K stainless steel 1.4301 weight', 'site:vacuum-shop.com 320RTS063 T-piece stainless steel 1.4301 304', and 'Pfeiffer ISO-K tee manufacturing 304 stainless pulled port tubing'; found row-matched product/material/dimension facts and a Pfeiffer family manufacturing description, but no product-specific factory traveler for 320RTS063."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Detailed welding, flange finishing, cleaning, and leak-test steps are inferred as a plausible Manufacturing route for a vacuum-rated stainless tee."
  uncertainty_notes:
    - "The exact Pfeiffer production sequence for part number 320RTS063 is not published in the sources checked"
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable standard DN63 ISO-K stainless tee fitting rather than a reAM250-specific custom part or calibrated purchased module."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0254_38.md
source_research_sha256: eb8733dfc053d07bd7addde843b8f8e7a5facf57167fbe81a780ea61031e531d
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Reviewed the DN63 ISO-K tee function, CAD-derived mass, stainless 304 material evidence, inferred tube/flange
    fabrication and leak-test route, KB implication, and preview showing a three-port flanged tee.
decomposition:
  decision: simple_part
  rationale: The row is a standard one-piece plumbing tee fitting with welded/forming and finish requirements, not a complex
    module needing internal subpart exposure during row conversion.
  proposed_subparts: []
process_abstraction:
  original_process_family: stainless_vacuum_tee_fabrication_testing
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
  - stock_preparation
  - forming
  - cutting
  - joining
  - precision_machining
  - surface_finishing
  - cleaning
  - leak_testing
  - dimensional_inspection
  candidate_existing_processes:
  - process_id: fitting_assembly_basic_v0
    fit: partial
    reason: Covers general fitting assembly, though this tee also needs stainless tube/flange fabrication and tested sealing
      interfaces.
  - process_id: tube_stock_forming_v0
    fit: supporting
    reason: Relevant to forming stainless tube stock before the tee and branch geometry are made.
  - process_id: welding_tig_basic_v0
    fit: supporting
    reason: Relevant for vacuum-compatible stainless branch and flange joining.
  - process_id: machining_precision_v0
    fit: supporting
    reason: Relevant for controlled ISO-K flange lips, faces, and fit surfaces.
  - process_id: cleaning_basic_v0
    fit: supporting
    reason: Covers cleaning before vacuum plumbing use and leak checks.
  - process_id: leak_testing_v0
    fit: supporting
    reason: Covers checking sealed plumbing joints and flange integrity.
  abstraction_decision: keep_original_family
  rationale: The original route is stainless tube/flange fabrication, joining, finishing, cleaning, and leak testing. That
    already matches the plumbing connector fabrication/testing bucket.
  process_guardrails:
    tolerance: DN63 ISO-K flange geometry and port alignment need inspection
    surface_finish: seal-adjacent flange faces need suitable finish and cleanliness
    sealing_quality: leak integrity and flange profile quality are function-critical
    alignment_accuracy: three ports should remain square and concentric enough for clamp/seal assembly
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: branch a plumbing line into a perpendicular third port while preserving clamp and seal interfaces
  material: stainless_steel_304
  scale_or_capacity:
    mass_kg: 1.84
    bom_quantity: 1
    row_total_mass_kg: 1.84
    scale_class: medium
    nominal_size: DN63
  geometry_form: three_port_flanged_tee_fitting
merge_pool:
  eligible: true
  functional_purpose_key: plumbing_connection
  precision_guardrails:
  - flange_profile
  - sealing_face_finish
  - port_alignment
  - leak_integrity
  - vacuum_cleanliness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - plumbing_connector_fabrication_testing
  import_risk_factors:
  - ISO-K flange profile, sealing finish, and leak-cleanliness requirements may exceed generic tube fitting capability.
  - Stainless 304 production, tube forming, flange fabrication, and tested welding must all be available for local closure.
  post_merge_decision_notes: Final import/local decision is deferred until merge review compares this tee with other plumbing
    connectors by function, size, material, and sealing guardrails.
kb_staging:
  proposed_item_id: null
  notes: Leave final item ID open for merge review; this may stage as a reusable DN63 stainless plumbing tee if similar
    rows converge.
assumptions:
- The supplied CAD solid represents one tee fitting and the CAD-derived mass is acceptable for planning.
- Stainless 304 from the row-matched Pfeiffer product page is the correct material family.
- Seal rings, clamps, and fasteners are separate interface hardware outside this row item.
unresolved:
- Catalog weight, detailed production route, welding details, and exact finish specification were not found.
- Later staging must decide how much ISO-K standard geometry remains explicit versus generic plumbing connector abstraction.
```
