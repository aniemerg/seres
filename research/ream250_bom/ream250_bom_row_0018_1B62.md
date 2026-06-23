---
row_identity:
  item: "1B62"
  cad_file: "1B62_cover"
  source_row_number: 18
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "BOM text identifies this row as a GN 820.2 Type MFC horizontal side-mount toggle clamp used to hold or latch a cover/door element; the local row CAD export is not a row-specific clamp model."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.elesa-ganter.com/en/www/Toggle-power-and-hook-clamps--Horizontal-acting-toggle-clamps--GN8202"
    cited_fact_or_basis: "BOM row 18 text says GN 820.2 toggle clamps, Type MFC. The full assembly STEP contains product metadata for GN 820.2-230-MFC with the same Type MFC description. The Elesa+Ganter page states GN 820.2 clamps use a toggle principle with opposite lever/clamping-bar motion, horizontal lever in the clamped position, and side mounting."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Treat the GN 820.2 Type MFC product text as the intended row component despite the 1B62_cover CAD filename."
  uncertainty_notes:
    - "The manifest marks the row as assembly_only and says no 1B62-prefixed product was found in the raw STEP; the rendered preview from 1B50_schlieren_imaging_door.step shows a thin ring, not a toggle clamp."
mass:
  value_kg: 0.42
  basis: "Per-unit mass for one clamp. The official Elesa+Ganter SKU data for GN 820.2-230-MFC lists logoweight 420 g; quantity is 1, so the row total is also about 0.42 kg."
  source:
    url_or_path: "https://www.elesa-ganter.com/static/products/ganter/skus/GN%20820.2.en.js?dc=202606180906444; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The SKU data row for GN 820.2-230-MFC lists Size 230, Type MFC, and weight 420 g. The full assembly STEP metadata contains GN 820.2-230-MFC as the exact clamp designation. FreeCAD measured only the collapsed parent assembly/ring geometry: 1 solid, volume 2573.818 mm^3, area 3560.408 mm^2, bbox 55.88 x 39.87 x 45.80 mm."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Use the vendor weight directly instead of CAD-derived volume because the available CAD for this leased row is not a row-specific clamp solid."
  uncertainty_notes:
    - "The BOM row itself omits the size suffix; the size 230 suffix is taken from same-product metadata in the full assembly STEP, not from the row 18 CSV fields alone."
material:
  primary_material: "Case-hardened C10 steel with zinc-plated/blue-passivated finish; tempered steel bearing pins; zinc-plated steel GN 708.1 clamping screw with 85 Shore A rubber thrust pad; oil-resistant plastic handle; special grease on moving parts."
  source:
    url_or_path: "https://www.elesa-ganter.com/en/www/Toggle-power-and-hook-clamps--Horizontal-acting-toggle-clamps--GN8202; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The GN 820.2 steel specification lists case-hardened C10 steel with zinc-plated blue-passivated finish, tempered bearing pins, grease on moving parts, oil-resistant plastic handle, and a GN 708.1 Type A steel clamping screw with 85 Shore A rubber tip. The local exact designation lacks the NI stainless suffix."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Use the steel version because GN 820.2-230-MFC in the local STEP metadata has no NI stainless suffix."
  uncertainty_notes:
    - "No row-specific STEP material metadata matched 1B62_cover; the assembly material extractor returned no matches for this row CAD filename."
how_to_make:
  summary: "Procure as a standard GN 820.2-230-MFC toggle clamp, then install it on the door or cover mounting interface with the supplied clamping screw adjusted to the required reach."
  manufacturing_steps:
    - "Order or stock the configured GN 820.2-230-MFC steel Type MFC clamp."
    - "Inspect the clamp, spindle, rubber tip, and lever action before installation."
    - "Fasten the side-mount base to the local door/cover structure and set the GN 708.1 clamping screw contact position."
  source:
    url_or_path: "https://www.elesa-ganter.com/en/www/Toggle-power-and-hook-clamps--Horizontal-acting-toggle-clamps--GN8202; https://www.zoro.com/jw-winco-gn8202-230-mfc-horizontal-toggle-clamp-8202-230-mfc/i/G4707144/"
    cited_fact_or_basis: "Elesa+Ganter defines Type MFC as the U-bar version with two flanged washers and GN 708.1 spindle assembly. Zoro lists Mfr # 820.2-230-MFC as a JW Winco horizontal toggle clamp, confirming a purchasable configured standard part."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Use procurement plus installation as the practical route for this BOM row rather than modeling the clamp's internal stamped links, pivots, handle, spindle, and rubber pad as separate manufactured parts."
  uncertainty_notes:
    - "A local self-manufacturing route would require a sub-BOM and process plan for the linkage, pivots, handle, spindle, rubber pad, lubrication, plating, and assembly that are not present in the row evidence."
kb_implications:
  - "item_granularity: assembly - Model later as a reusable standard mechanical clamp assembly, not as a calibrated purchased module and not as the misleading 1B62_cover CAD ring."
---

