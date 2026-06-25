---
row_identity:
  item: 8C1
  cad_file: 8C1_flexible_pipe
  source_row_number: 208
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
  link_url: https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0500
function:
  summary: Flexible DN 40 ISO-KF corrugated vacuum hose used to connect vacuum plumbing while tolerating alignment offsets, bending, vibration, and thermal movement.
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0208_8C1__views_2x2.png; https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0500; https://vacuum-shop.com/2074124/downloads/datasheets/Datasheet_120SWG040-0500_en.pdf"
    cited_fact_or_basis: "BOM row 208 identifies item 8C1 as Pfeiffer Vacuum 120SWG040-0500 flexible pipe; the manifest maps it to 8C1_flexible_pipe.step; the rendered CAD preview shows a thin corrugated circular hose/end form; the Pfeiffer datasheet identifies the product as a corrugated hose, flexible, annealed, DN 40 ISO-KF, length 500 mm. official_alternate_route_check: the BOM URL is the Pfeiffer shop route, and the vacuum-shop datasheet is the official Pfeiffer/Busch online-shop download for the same order number 120SWG040-0500."
    evidence_basis: bom_provided
  assumptions:
    - The row is modeled as the complete purchased 120SWG040-0500 hose, not only the compact STEP ring-like representation.
  uncertainty_notes:
    - The per-row STEP preview does not show the full 500 mm hose length, so CAD visual evidence is weaker than the vendor product identity for function.
mass:
  value_kg: 0.34
  basis: "Per-unit estimate for quantity 1. Official geometry gives length A = 500 mm, inner/nominal B = 41 mm, outer C = 52 mm, and 15 mm flange connection length. Planning calculation: two stainless end/flange annuli approximated as OD 52 mm, ID 41 mm, length 15 mm each give about 24100 mm^3; a 470 mm bellows shell at mean diameter 46.5 mm, 0.20 mm wall, and 1.3 corrugation area factor gives about 17800 mm^3; total stainless volume about 41900 mm^3 at 8000 kg/m^3 gives about 0.335 kg, rounded to 0.34 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8C1_flexible_pipe.step; research/ream250_bom/ream250_bom_row_0208_8C1__views_2x2.png; https://vacuum-shop.com/2074124/downloads/datasheets/Datasheet_120SWG040-0500_en.pdf; kb/materials/properties.yaml; https://longva.en.made-in-china.com/product/rQGULPMDINVm/China-Vacuum-Pump-Fittings-Kf40-Flexible-Hose-500mm-Vacuum-Corrugated-Bellows.html"
    cited_fact_or_basis: "FreeCAD measured the local STEP as 1 solid, volume 309.686 mm^3, area 4276.689 mm^2, bounding box 5.32 x 56.28 x 56.28 mm, which is not a full 500 mm hose mass model. The official datasheet gives DN 40 ISO-KF, 500 mm length, 41 mm B, 52 mm C, 15 mm flange connection length, and stainless material set. kb/materials/properties.yaml gives stainless_steel density 8000 kg/m^3. A separate KF vacuum hose supplier lists stainless bellows wall thickness in the 0.12-0.4 mm range. targeted_web_search: tried \"120SWG040-0500 Weight\", \"120SWG040-0500 kg\", \"120SWG040-0500 datasheet weight\", \"DN40 KF flexible corrugated hose 500 mm weight kg stainless\", and \"KF40 500mm flexible hose weight stainless steel\"; exact Pfeiffer/vendor pages found dimensions and material but no exact row-matched catalog weight, while non-row-matched retail listings varied enough to use only a hypothesis."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The effective bellows wall is modeled as 0.20 mm stainless, within the externally observed 0.12-0.4 mm range for similar KF stainless bellows.
    - Corrugations increase developed shell area by about 30% relative to a straight tube.
    - End/flange hardware is approximated as two simple stainless annuli; real KF flange profiles remove and add local material.
  uncertainty_notes:
    - Pfeiffer did not provide an exact weight in the located row-matched product data, so the estimate may be off by roughly a factor of two.
    - The local STEP geometry appears to be a compact end/corrugation proxy rather than the full hose, so CAD-derived mass alone would severely undercount the row item.
material:
  primary_material: "Stainless steel component set: 316L bellows and stainless steel 1.4301/304 flanges."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0500; https://vacuum-shop.com/2074124/downloads/datasheets/Datasheet_120SWG040-0500_en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The official product/datasheet route for order number 120SWG040-0500 states material as flange stainless steel 1.4301/304 and bellows stainless steel 316L, with media-contact materials listed as bellows 316L and flange stainless steel 1.4301/304. Local STEP material extraction for product 8C1_flexible_pipe returned only Generic with density 1000.0, so it was not used as material evidence. official_alternate_route_check: the BOM URL is the Pfeiffer shop route, and the vacuum-shop product/datasheet route is an official Pfeiffer/Busch online-shop alternate for the same order number."
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes:
    - No separate gasket or clamp material is included in this row; it is treated as the hose assembly material set only.
how_to_make:
  summary: "Prepare as a standard Pfeiffer 120SWG040-0500 DN 40 ISO-KF corrugated stainless vacuum hose; form/weld a thin 316L corrugated bellows tube and attach 304/1.4301 KF flanges, followed by leak and cleanliness checks"
  manufacturing_steps:
    - For a Manufacturing route, roll or draw thin 316L stainless tube, seam weld it, and form annular corrugations over the hose length.
    - Machine or form 304/1.4301 DN 40 ISO-KF end flanges and weld them to the bellows ends.
    - Clean, passivate if required, inspect dimensions, and helium leak test for vacuum service.
  source:
    url_or_path: "https://vacuum-shop.com/2074124/downloads/datasheets/Datasheet_120SWG040-0500_en.pdf; research/ream250_bom/ream250_bom_row_0208_8C1__views_2x2.png; https://hoseflex.com/wp-content/uploads/2023/11/02.-Stainless-Steel-Hose-2.pdf"
    cited_fact_or_basis: "The official datasheet identifies a purchasable corrugated, flexible, annealed stainless DN 40 ISO-KF hose with 500 mm length and stainless 316L/304 material set; the CAD preview confirms a corrugated circular hose/end form. A general stainless hose manufacturing reference describes corrugated hose as made from thin-walled tube formed from rolled strip and welded at the seam, with an impressed corrugated annular profile. targeted_web_search: tried \"120SWG040-0500 manufacturing corrugated hose\", \"stainless corrugated hose manufactured rolled strip welded seam annular corrugation\", and \"KF40 stainless bellows hose manufacturing\" no row-specific Pfeiffer manufacturing process was found, so The manufacturing route is inferred from generic corrugated stainless hose practice."
    evidence_basis: engineering_hypothesis
  assumptions:
    - "Local manufacturing is only a plausible route for later modeling"
    - Vacuum acceptance testing is needed because the hose is part of a vacuum boundary.
  uncertainty_notes:
    - "Pfeiffer's own manufacturing process, wall thickness, weld details, and acceptance thresholds were not located for this exact part number"
kb_implications:
  - "item_granularity: simple_part - Treat as a reusable DN40 ISO-KF corrugated vacuum hose item; capture thin-wall bellows forming, KF flange joining, cleaning, and leak testing in the manufacturing route."
---
