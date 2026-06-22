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
  summary: "Treat as a purchased Pfeiffer Vacuum SAS 40 DN 40 ISO-KF dust separator module for current KB planning; a local build would require a vacuum-tight DN 40 ISO-KF housing, cover/clasp and seals, and a replaceable polyester filter insert."
  manufacturing_steps:
    - "Procure one Pfeiffer Vacuum PK Z60 510 / SAS 40 dust separator, DN 40 ISO-KF, matching the BOM product route and CAD geometry."
    - "Verify DN 40 ISO-KF inlet and outlet interfaces, filter insert condition, and cover/seal/clasp integrity before installation."
    - "Install in the vacuum line or pump inlet path with compatible ISO-KF centering rings, seals, and clamps from neighboring BOM rows."
    - "For a future local-manufacturing model, decompose into housing/flange fabrication, cover/clasp hardware, elastomer seals, and polyester filter insert production or procurement."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/PK_Z60_510; https://www.ajvs.com/library/Pfeiffer%20SAS%2016-160%20Dust%20Separators%20Operation%20Manual.pdf; https://www.ajvs.com/library/Pfeiffer%20SAS%2040%20Dust%20Separator%20Data%20Sheet%20PKZ60510.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/85_filter_ISO_KF_DN40_CSL-357y2-KF.step; research/ream250_bom/ream250_bom_row_0281_85__views_2x2.png"
    cited_fact_or_basis: "The BOM supplies a Pfeiffer product route and product number PK Z60 510. The SAS documentation identifies PK Z60 510 as a SAS 40 dust separator with DN 40 ISO-KF interfaces and shows removable filter-insert maintenance steps, including removing the cover, removing/cleaning the insert, cleaning seals and sealing surfaces, and reinstalling the insert. The rendered CAD preview shows a complete canister-style filter module with ports and cover/clasp features. official_alternate_route_check: the original BOM URL is the Pfeiffer shop route for PK_Z60_510; because the official shop page returned only an anti-bot wrapper, the same manufacturer/order-number identity was checked against Pfeiffer-branded SAS 40 documentation mirrored externally."
    evidence_basis: "bom_provided"
  assumptions:
    - "Current KB planning should model the row as a purchased functional vacuum accessory unless later work intentionally decomposes the dust separator into housing, filter media, seals, and fastening hardware."
  uncertainty_notes:
    - "The documentation supports procurement and maintenance/insert replacement, but not a detailed local manufacturing drawing, tolerances, seal profile, filter-media pleat construction, or housing alloy."
kb_implications:
  - "item_granularity: purchased_module - row 85 is a standard Pfeiffer SAS 40 DN 40 ISO-KF dust separator/filter module; model as a purchased vacuum accessory unless later work decomposes the housing, filter insert, seals, and cover/clasp hardware."
---

Research result for reAM250 BOM row 281.
