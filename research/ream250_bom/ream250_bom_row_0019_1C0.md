---
row_identity:
  item: "1C0"
  cad_file: "1C0_clamp_GN 820_2-230-MFC"
  source_row_number: 19
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.ganternorm.com/de/produkte/2.4-Spannen-mit-Spannmechanik/Schnellspanner/GN-853-Edelstahl-Verschlussspanner-mit-Verriegelung#Gr%C3%B6%C3%9Fe%3Di(160)%3BForm%3Du(bec5acdb-2fc0-4cf4-9459-a053043062c1)%3BWerkstoff%3Du(4ffaa763-f739-4917-9edb-5c7ca96d4057)"
function:
  summary: "Ganter/Elesa+Ganter GN 820.2-230-MFC horizontal acting toggle clamp with side/vertical mounting base, forked clamping arm, two flanged washers, and GN 708.1 spindle assembly; BOM quantity is 2."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1C0_clamp_GN 820_2-230-MFC.step; https://www.ganternorm.com/en/products/2.4-Tensioning-with-clamping-mechanisms/Toggle-clamps/GN-820.2-Stainless-Steel-Toggle-clamps-operating-lever-horizontal-with-side-mounting"
    cited_fact_or_basis: "BOM row 19 names item 1C0, quantity 2, CAD file 1C0_clamp_GN 820_2-230-MFC, manufacturer GanterNorm, and description 'flanged washers and GN spindle assembly'. Manifest row 19 maps the row to a matched vendor-component STEP. FreeCAD measured 7 solids with bounding box 196.59 x 121.00 x 43.00 mm, matching the GN 820.2 size-230 envelope; the contact sheet shows a toggle clamp with side mounting base, forked arm, handle, and clamping screw. Ganter describes GN 820.2 as a horizontal acting toggle clamp, says type MFC includes two flanged washers and clamping screw GN 708.1, and lists size 230 with holding capacity 1700 N. official_alternate_route_check: the original BOM Link URL was checked, but it points to Ganter GN 853 rather than the row's GN 820.2 CAD/product identity; the row-matched Ganter GN 820.2 page on the same official manufacturer domain was used instead because it matches the BOM/CAD product family and filename."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The original BOM Link URL appears to be a row-linking error because it identifies GN 853 while the BOM text, CAD filename, manifest, and geometry identify GN 820.2-230-MFC."
mass:
  value_kg: 0.42
  basis: "Per unit. BOM quantity is 2, so the row total is about 0.84 kg. D&D Barry's Elesa+Ganter GN 820.2 table lists the exact steel SKU GN 820.2-230-MFC with weight 420 g. Local CAD volume is 72479.263 mm^3 and bounding box is 196.59 x 121.00 x 43.00 mm; this supports size/shape identity but is not used for density-derived mass because the row is a multi-solid, multi-material assembly."
  source:
    url_or_path: "https://www.ddbarry.com.au/product/gn-820-2/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1C0_clamp_GN 820_2-230-MFC.step"
    cited_fact_or_basis: "D&D Barry's GN 820.2 listing includes SKU GN 820.2-230-MFC with dimensions matching size 230 and weight 420 g. FreeCAD measured the row STEP as 7 solids, volume 72479.263 mm^3, area 37940.166 mm^2, and bounding box 196.59 x 121.00 x 43.00 mm. bom_url_route_check: the original BOM Link URL points to GN 853 and did not resolve the exact GN 820.2-230-MFC mass; the row-matched Elesa+Ganter distributor table was used for mass."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's CAD filename omits the NI stainless suffix, so the non-NI steel GN 820.2-230-MFC catalog row is treated as the BOM item."
  uncertainty_notes:
    - "The Ganter page reached from the row-matched search exposes a selected-part weight field, but browser state did not reliably prove that field was configured to GN 820.2-230-MFC; the exact SKU table weight is therefore preferred."
    - "The assembly STEP material extractor found the product but no material or density metadata for this row."
material:
  primary_material: "case-hardened steel C10 clamp body with zinc-plated blue-passivated finish, tempered bearing pins, lubricated moving parts, oil-resistant red plastic hand grip, and GN 708.1 spindle assembly with steel or stainless spindle and rubber tip"
  source:
    url_or_path: "https://static.globalindustrial.com/products/pdf/45554-jw-winco-inc/B2958413.pdf; https://www.ganternorm.com/en/products/2.4-Tensioning-with-clamping-mechanisms/Toggle-clamps/GN-820.2-Stainless-Steel-Toggle-clamps-operating-lever-horizontal-with-side-mounting"
    cited_fact_or_basis: "The JW Winco/Ganter GN 820.2 standard sheet states the steel toggle clamp material as case-hardened steel C10 with zinc-plated blue-passivated finish, tempered bearing pins, moving parts lubricated with special grease, oil-resistant red plastic hand grip, and GN 708.1 spindle assembly with rubber tip. The Ganter GN 820.2 page identifies type MFC as the forked clamping arm with two flanged washers and clamping screw GN 708.1. agent-initiated independent search route: searched exact row product 'GN 820.2-230-MFC' after finding the original BOM Link URL pointed to GN 853; the row-matched GN 820.2 catalog/source facts were used for material."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Because the BOM/CAD row names GN 820.2-230-MFC without the NI suffix, the steel material option is used rather than the stainless GN 820.2-230-MFC-NI option."
  uncertainty_notes:
    - "If the BOM Link URL was intended to indicate a stainless replacement despite the CAD filename, the material would shift toward AISI 304 stainless components; the current row identity evidence favors the non-NI steel SKU."
how_to_make:
  summary: "Manufacturing route would be a small mechanical assembly made from stamped or machined steel clamp links/base, bearing pins/rivets, a formed or molded plastic handle, and a threaded clamping spindle with rubber thrust pad"
  manufacturing_steps:
    - "Manufacturing route: cut, form, or machine C10 steel sheet/plate pieces for the side mounting base, forked clamping arm, and linkage plates, then zinc plate or otherwise protect the steel surfaces."
    - "Make or source pins/rivets, flanged washers, the GN 708.1-style threaded spindle, plastic handle, and rubber tip; lubricate moving joints."
    - "Assemble the linkage and spindle, then inspect clamp travel, over-center locking action, mounting-hole geometry, and approximate holding-capacity suitability."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0019_1C0__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1C0_clamp_GN 820_2-230-MFC.step; https://www.ganternorm.com/en/products/2.4-Tensioning-with-clamping-mechanisms/Toggle-clamps/GN-820.2-Stainless-Steel-Toggle-clamps-operating-lever-horizontal-with-side-mounting; https://static.globalindustrial.com/products/pdf/45554-jw-winco-inc/B2958413.pdf"
    cited_fact_or_basis: "The CAD preview shows a multi-link toggle clamp assembly with base, forked arm, pins, handle, and threaded clamping screw. FreeCAD measured a 196.59 x 121.00 x 43.00 mm envelope. The Ganter page identifies the GN 820.2 toggle-clamp function and MFC clamping screw; the JW Winco/Ganter sheet identifies steel, pins, plastic handle, lubrication, and spindle/rubber tip component materials. The detailed fabrication sequence is inferred from component geometry and material stack rather than stated by the cited sources. targeted_web_search: queries tried included 'GN 820.2-230-MFC manufacturing process', 'GN 820.2 toggle clamp material C10 pins handle', and 'GN 820.2-230-MFC weight material'; results resolved row-matched product, material, dimensions, and mass but did not provide a row-specific manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The clamp is best represented initially as a external standard module because it combines several small precision linkage, handle, spindle, and rubber-pad parts"
    - "The manufacturing route assumes conventional sheet/plate forming or machining plus pin/rivet assembly, consistent with standard toggle clamp construction."
  uncertainty_notes:
    - "No row-specific drawing was found for tolerances, pin fits, heat treatment depth, plating specification, lubrication type, or production tooling."
kb_implications:
  - "item_granularity: simple_part - Treat as a reusable standard toggle-clamp hardware item for near-term KB modeling; split into steel links/base, pins, handle, spindle, washers, and rubber pad only if clamp manufacturing becomes a detailed target."
---

# reAM250 BOM Row 19 - 1C0

Research result for the leased reAM250 BOM row.
