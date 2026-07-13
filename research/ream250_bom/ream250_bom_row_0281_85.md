---
row_identity:
  item: "85"
  cad_file: "85_filter_ISO_KF_DN40_CSL-357y2-KF"
  source_row_number: 281
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/PK_Z60_510"
function:
  summary: "Pfeiffer Vacuum SAS 40 dust separator / inlet particle filter for a DN 40 ISO-KF vacuum line, used to protect a vacuum pump from process particles while preserving DN 40 ISO-KF inlet and outlet connectivity."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/85_filter_ISO_KF_DN40_CSL-357y2-KF.step; research/ream250_bom/ream250_bom_row_0281_85__views_2x2.png; https://www.pfeiffer-vacuum.com/global/de/shop/products/PK_Z60_510; https://www.ajvs.com/library/Pfeiffer%20SAS%2016-160%20Dust%20Separators%20Operation%20Manual.pdf; https://www.ajvs.com/library/Pfeiffer%20SAS%2040%20Dust%20Separator%20Data%20Sheet%20PKZ60510.pdf"
    cited_fact_or_basis: "BOM row 281 states item 85, quantity 1, CAD file 85_filter_ISO_KF_DN40_CSL-357y2-KF, description/product ID PK Z60 510, manufacturer Pfeiffer Vacuum, and a Pfeiffer product URL. The manifest maps the row to gold_export/parts/85_filter_ISO_KF_DN40_CSL-357y2-KF.step as a matched_existing vendor_component. The row-matched Pfeiffer SAS documentation identifies PK Z60 510 as SAS 40, dust separator, DN 40 ISO-KF, with DN 40 ISO-KF inlet/outlet connections, 5 um separable grain size, and 99.7% degree of separation; it describes the part as protecting the pump against particles from the process. FreeCAD measured one solid and the contact sheet shows a cylindrical filter canister with DN 40 ISO-KF ports and filter/cover features. official_alternate_route_check: the original BOM URL is the Pfeiffer product route for PK_Z60_510; direct curl of the official shop route returned only an anti-bot wrapper, so row identity was resolved through the same order number and manufacturer in Pfeiffer-branded SAS 40 documentation mirrored by a vacuum distributor."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents the complete SAS 40 dust separator/filter module rather than only a replaceable insert, because the BOM row quantity, product number, CAD geometry, and documentation all point to the full DN 40 ISO-KF dust separator."
  uncertainty_notes:
    - "The exact location in the reAM250 vacuum train is not identified by this row alone."
mass:
  value_kg: 2.1
  basis: "Use the row-matched catalog weight as the per-unit mass for one physical SAS 40 dust separator. BOM quantity is 1, so row total is also about 2.1 kg. FreeCAD measured one solid with volume 3228021.000 mm^3, area 150931.267 mm^2, and a bounding box about 202.07 x 189.02 x 223.73 mm; this geometry supports a large filter module but is not used for density-derived mass because catalog mass is available."
  source:
    url_or_path: "https://www.ajvs.com/library/Pfeiffer%20SAS%2016-160%20Dust%20Separators%20Operation%20Manual.pdf; https://www.ajvs.com/library/Pfeiffer%20SAS%2040%20Dust%20Separator%20Data%20Sheet%20PKZ60510.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/85_filter_ISO_KF_DN40_CSL-357y2-KF.step"
    cited_fact_or_basis: "The SAS 16-160 operating manual table for polyester filter inserts lists SAS 40, part number PK Z60 510, weight 2.1 kg. The row-matched SAS 40 data sheet lists weight 2.1 kg / 4.63 lb and also shows 2.06 kg in the same technical-data block. FreeCAD measured the supplied row STEP as one solid with volume 3228021.000 mm^3 and approximately 202.07 x 189.02 x 223.73 mm bounding box. official_alternate_route_check: the original BOM URL is the Pfeiffer shop route for PK_Z60_510; direct access returned only an anti-bot wrapper, so the same Pfeiffer Vacuum manufacturer, exact order number PK Z60 510, SAS 40 product designation, and DN 40 ISO-KF interface were checked in Pfeiffer-branded SAS documentation mirrored by AJVS."
    evidence_basis: "bom_provided"
  assumptions:
    - "Use 2.1 kg rather than 2.06 kg because the operating manual and one data-sheet line agree on 2.1 kg, while both values are within normal catalog rounding for the same row-matched part."
  uncertainty_notes:
    - "The catalog mass does not break out housing, filter insert, seals, or clasp subcomponents."
material:
  primary_material: "polyester filter insert; housing/flange hardware and seals are present but exact material grades are not specified by the row-matched evidence"
  source:
    url_or_path: "https://www.ajvs.com/library/Pfeiffer%20SAS%2016-160%20Dust%20Separators%20Operation%20Manual.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0281_85__views_2x2.png"
    cited_fact_or_basis: "The SAS operating manual identifies SAS spare parts and states the standard filter insert is polyester, with paper as an optional filter insert. The technical-data tables for SAS 40 are for polyester filter inserts. The assembly STEP material extractor matched the CAD product name but returned material Generic and density 1000.0, which is placeholder metadata under the task criteria and is not used as material evidence. The contact sheet shows the filter module body, ports, cover/clasp features, and filter element geometry but does not identify material grade. official_alternate_route_check: the original BOM URL is the Pfeiffer shop route for PK_Z60_510; direct access returned only an anti-bot wrapper, so the same Pfeiffer Vacuum manufacturer, exact order number PK Z60 510, SAS 40 product designation, and DN 40 ISO-KF interface were checked in Pfeiffer-branded SAS documentation mirrored by AJVS."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The sourced material only resolves the standard filter insert. The housing/flange metal family, seal elastomer, clasp/fastener material, and any surface treatment remain unresolved for detailed local manufacturing."
how_to_make:
  summary: "Treat as a external Pfeiffer Vacuum SAS 40 DN 40 ISO-KF dust separator module for current KB planning; a local build would require a vacuum-tight DN 40 ISO-KF housing, cover/clasp and seals, and a replaceable polyester filter insert"
  manufacturing_steps:
    - "Verify DN 40 ISO-KF inlet and outlet interfaces, filter insert condition, and cover/seal/clasp integrity before installation."
    - "Install in the vacuum line or pump inlet path with compatible ISO-KF centering rings, seals, and clamps from neighboring BOM rows."
    - "For a future local-manufacturing model, decompose into housing/flange fabrication, cover/clasp hardware, elastomer seals, and polyester filter insert production"
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/PK_Z60_510; https://www.ajvs.com/library/Pfeiffer%20SAS%2016-160%20Dust%20Separators%20Operation%20Manual.pdf; https://www.ajvs.com/library/Pfeiffer%20SAS%2040%20Dust%20Separator%20Data%20Sheet%20PKZ60510.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/85_filter_ISO_KF_DN40_CSL-357y2-KF.step; research/ream250_bom/ream250_bom_row_0281_85__views_2x2.png"
    cited_fact_or_basis: "The BOM supplies a Pfeiffer product route and product number PK Z60 510. The SAS documentation identifies PK Z60 510 as a SAS 40 dust separator with DN 40 ISO-KF interfaces and shows removable filter-insert maintenance steps, including removing the cover, removing/cleaning the insert, cleaning seals and sealing surfaces, and reinstalling the insert. The rendered CAD preview shows a complete canister-style filter module with ports and cover/clasp features. official_alternate_route_check: the original BOM URL is the Pfeiffer shop route for PK_Z60_510; because the official shop page returned only an anti-bot wrapper, the same manufacturer/order-number identity was checked against Pfeiffer-branded SAS 40 documentation mirrored externally."
    evidence_basis: "bom_provided"
  assumptions:
    - "Current KB planning should model the row as a external functional vacuum accessory unless later work intentionally decomposes the dust separator into housing, filter media, seals, and fastening hardware"
  uncertainty_notes:
    - "Local manufacturing drawing, tolerances, seal profile, filter-media pleat construction, or housing alloy"
kb_implications:
  - "item_granularity: complex_module - row 85 is a standard Pfeiffer SAS 40 DN 40 ISO-KF dust separator/filter module; model as a complex vacuum accessory unless later work decomposes the housing, filter insert, seals, and cover/clasp hardware."
---

Research result for reAM250 BOM row 281.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0281_85.md
source_research_sha256: "9e12581e32d10e43d55548a57e92410916e26f7bf7f3c420a4886e2256425139"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read function, catalog mass, material notes for polyester insert plus unresolved housing/seals, module-level route, kb implications, and preview showing a canister filter with DN40 ports and cover/clasp features."
decomposition:
  decision: decompose_into_parts
  rationale: "The row is a complete dust separator/filter module with housing, ports, cover/clasp hardware, seals, and replaceable filter media. Those closure dependencies need decomposition before item merging."
  proposed_subparts:
    - vacuum_tight_filter_housing_with_dn40_ports
    - polyester_filter_insert
    - seal_set
    - cover_clasp_and_fastener_hardware
process_abstraction:
  original_process_family: vendor_vacuum_dust_separator_module_with_replaceable_filter_insert
  primary_process_bucket: precision_component_import_decompose_later
  supporting_processes:
    - decomposition_required
    - assembly
    - cleaning
    - leak_testing
    - pressure_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: filtration_basic_v0
      fit: supporting
      reason: "Anchors the functional filtration operation, but does not manufacture the SAS 40 hardware module."
    - process_id: sealing_and_assembly_basic_v0
      fit: supporting
      reason: "Relevant to installing seals, cover, and filter insert during module assembly."
    - process_id: pressure_test_basic_v0
      fit: supporting
      reason: "Relevant to checking housing and port integrity; vacuum leak testing may be stricter."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Relevant for port dimensions, cover fit, and filter insert inspection."
  abstraction_decision: needs_human
  rationale: "The source item is a catalog vacuum accessory with filter media, housing, seals, and serviceable cover hardware. Row conversion should not collapse it into a single simple fabrication process."
  process_guardrails:
    tolerance: review
    surface_finish: sealing_surface_review
    sealing_quality: vacuum_leak_tight_review
    alignment_accuracy: port_alignment_review
    blocked_by_precision: true
identity_for_merge:
  functional_purpose: particulate separation from a gas line to protect downstream equipment
  material: mixed_polyester_filter_media_metal_housing_and_seals
  scale_or_capacity:
    mass_kg: 2.1
    bom_quantity: 1
    row_total_mass_kg: 2.1
    scale_class: small
  geometry_form: dn40_canister_dust_separator_filter_module
merge_pool:
  eligible: false
  functional_purpose_key: particulate_separator
  precision_guardrails:
    - dn40_interface_geometry
    - filter_media_grade
    - leak_tightness
    - serviceable_cover_hardware
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - precision_component_import_decompose_later
  import_risk_factors:
    - "Housing alloy, seal elastomer, filter-media pleat construction, leak acceptance, and cover/clasp details are unresolved."
    - "Catalog module may remain imported until filter media and vacuum housing fabrication are explicitly modeled."
  post_merge_decision_notes: "Final import/local decision is deferred until decomposition separates housing, ports, filter insert, seals, and cover hardware."
kb_staging:
  proposed_item_id: null
  notes: "Do not assign a final closure item ID during row conversion; review with other particulate separator and vacuum filter rows first."
assumptions:
  - "BOM quantity is 1, so row total mass equals the 2.1 kg catalog mass."
  - "The row represents the full SAS 40 module rather than only the polyester insert."
  - "DN40 ISO-KF interface and serviceable filter insert should be preserved in later decomposition."
unresolved:
  - "Housing/flange material, seal elastomer, filter insert construction, and clasp hardware material."
  - "Leak-rate, pressure rating, filter replacement interval, and cleaning specification."
  - "Whether the later KB should stage a generic DN40 dust separator module as an import boundary."
```
