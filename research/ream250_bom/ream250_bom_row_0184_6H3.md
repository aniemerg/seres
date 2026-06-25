---
row_identity:
  item: 6H3
  cad_file: 6H3_brush_seal_bottom
  source_row_number: 184
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
  link_url: https://mink-buersten.com/konfigurator/?id_artikelkategorie=275
function:
  summary: Cut-to-length flexible brush seal installed along the lower edge of a reAM250 opening or interface to provide compliant sealing, wiping, or guidance while tolerating relative motion and contour variation.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6H3_brush_seal_bottom.step; research/ream250_bom/ream250_bom_row_0184_6H3__views_2x2.png; https://mink-buersten.com/en/products/strip-brushes/flex-system/
    cited_fact_or_basis: "BOM row 184 names item 6H3 as 6H3_brush_seal_bottom from Mink Bursten. FreeCAD measured a single 270.00 x 30.00 x 39.75 mm part, and the rendered preview shows a long flexible strip/brush profile. Mink's Flex-System page describes flexible strip brushes for sealing, wiping, and guiding, with a flexible body that can follow axial or radial contours. official_alternate_route_check: original BOM URL is the Mink configurator category URL; the official Mink Flex-System product page on the same domain matches the row manufacturer and the assembly STEP product context FBL3002-Mink Flex-System."
    evidence_basis: bom_provided
  assumptions:
    - The row name suffix "bottom" means this is the lower member of a paired brush-seal set rather than a standalone top seal.
  uncertainty_notes:
    - The exact mating surface and whether the seal primarily controls powder, air leakage, or contact wiping is not identified by the row-level CAD file.
mass:
  value_kg: 0.0541
  basis: "Per unit. Quantity in BOM row is 1, so row total is also about 0.0541 kg. FreeCAD volume is 58210.975 mm^3 = 5.8210975e-5 m^3; assembly STEP material metadata reports Rubber with density 930 kg/m^3; computed mass is 5.8210975e-5 m^3 x 930 kg/m^3 = 0.05414 kg."
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6H3_brush_seal_bottom.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step
    cited_fact_or_basis: "FreeCAD measured one solid, volume 58210.975 mm^3, area 43711.302 mm^2, bounding box 270.00 x 30.00 x 39.75 mm. Local assembly material extractor matched 6H3_brush_seal_bottom to material Rubber with density 930 kg/m^3."
    evidence_basis: bom_provided
  assumptions:
    - The STEP solid volume represents one physical brush-seal segment for this BOM row.
    - The assembly STEP density is interpreted as kg/m^3, consistent with the extractor note for reAM250 material densities.
  uncertainty_notes:
    - The vendor family normally includes both flexible body and bristles, so the single-material STEP density may be an effective CAD material rather than a complete materials declaration.
material:
  primary_material: Thermoplastic rubber or similar flexible rubber body, with possible polyamide bristles for the Mink Flex-System brush profile.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://wechat.partcommunity.com/3d-cad-models/fbl3002-mink-flex-system-mink-b%C3%BCrsten?info=mink%2Fstrip_brushes%2Fflex_system%2Ffbl3002.prj
    cited_fact_or_basis: "Local STEP material extraction for product 6H3_brush_seal_bottom reports material Rubber and density 930 kg/m^3. The FBL3002 CADENAS/Partcommunity catalog entry for Mink Flex-System lists body material Thermoplastic rubber / TPE/TPV and bristle material Polyamide 6 for an FBL3002 configuration. bom_url_route_check: the BOM-provided Mink configurator route and the official Mink Flex-System page identify the product family and application but do not expose row-specific FBL3002 material fields in the browsable page, so the material set uses the CADENAS/Partcommunity catalog entry matching FBL3002."
    evidence_basis: independent_vendor_spec
  assumptions:
    - The assembly STEP product context FBL3002-Mink Flex-System means the row belongs to the FBL3002 product family represented by the catalog entry.
  uncertainty_notes:
    - The row-specific STEP file does not expose the exact Mink order variant, bristle height, or polymer grade; treat TPE/TPV plus PA6 as the best family-level material set, not a certified material grade.
how_to_make:
  summary: "Prepare as a Mink Flex-System/FBL3002 flexible strip brush seal and cut to the 270 mm CAD length for installation; extrude or mold the rubber/TPE profile and add polymer bristles, then trim and inspect the segment"
  manufacturing_steps:
    - Select the Mink Flex-System profile matching the reAM250 groove/interface, using the FBL3002 family indicated by the assembly STEP context.
    - Cut the flexible strip brush from supplied roll/length stock to the 270 mm row length shown by CAD.
    - Inspect the cut end, profile fit, and bristle/seal orientation, then install on the lower interface as the bottom brush seal.
  source:
    url_or_path: https://mink-buersten.com/wp-content/uploads/FBL_D_GB_F.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6H3_brush_seal_bottom.step
    cited_fact_or_basis: "Mink's Flex-System brochure says the product is supplied in rolls up to several hundred metres, can be cut to the required length, and can be fitted/replaced with low tool effort by gluing, pushing onto an edge, or inserting into a groove. CAD evidence gives the required row length as 270.00 mm."
    evidence_basis: bom_provided
  assumptions:
    - "Cut-to-length installation is the preferred route because the row is a vendor component from Mink Bursten"
    - "This manufacturing route is lower confidence because the catalog does not provide a full sub-BOM or bristle-insertion manufacturing workflow"
  uncertainty_notes:
    - "Exact machine drawing or Mink configuration is needed before replacing the component"
kb_implications:
  - "item_granularity: simple_part - Model as a replaceable cut-to-length flexible brush seal, not as raw stock or a calibrated module; later KB work can reuse a generic brush-seal replaceable or applied part with row-specific length."
---
