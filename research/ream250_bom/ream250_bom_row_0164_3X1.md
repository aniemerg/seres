---
row_identity:
  item: "3X1"
  cad_file: "3X1_valve_part_1"
  source_row_number: 164
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html"
function:
  summary: "Part 1 of an AMproved ISO-KF DN40 manual disc valve used to manually control or close fluid/powder flow paths on powder bottles, overflows, filler necks, or pipework in AM machines."
  source:
    url_or_path: "https://www.amproved.com/iso-kf-dn-40-scheibenventil.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0164_3X1__views_2x2.png"
    cited_fact_or_basis: "BOM row 164 identifies item 3X1 as AMproved valve part 1 for 'valve sv04_din_cc_dn40'. The AMproved page names the product ISO-KF DN 40 Scheibenventil, describes it as a disc valve for manual control of fluid streams in pipework, and says it is ideal for closing powder bottles, overflows, and filler necks in AM machines. The rendered CAD preview shows a compact cylindrical valve-body-like component with a central through bore and external lugs. official_alternate_route_check: original BOM URL https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html was checked; the reachable AMproved canonical page https://www.amproved.com/iso-kf-dn-40-scheibenventil.html is the same first-party domain and matches the row product name ISO-KF DN 40 Scheibenventil."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents the first physical CAD part of the valve rather than the complete valve assembly because adjacent row 165 is valve part 2 for the same product."
  uncertainty_notes:
    - "The exact internal role of part 1 within the two-part valve split is not named by the vendor page, so the function is stated at valve-component level."
mass:
  value_kg: 0.173
  basis: "FreeCAD measured CAD volume 21574.099 mm^3 = 2.1574099e-5 m^3. Using stainless_steel density 8000 kg/m^3 from kb/materials/properties.yaml gives 0.1726 kg per part, rounded to 0.173 kg. BOM quantity is 1, so the row total is also about 0.173 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3X1_valve_part_1.step; kb/materials/properties.yaml; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 21574.099 mm^3, area 8200.189 mm^2, and bounding box 38.00 x 45.50 x 38.00 mm. BOM row 164 states material text '_aisi_316l-1_4404_-_epdm: part 1 valve sv04_din_cc_dn40_-'. The local material density table lists stainless_steel density 8000 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid is treated as the physical solid volume for one 3X1 valve part."
    - "The CAD solid is treated as primarily 316L/1.4404 stainless steel; any EPDM associated with the complete valve is not separately visible in this part-1 STEP."
    - "The local broad stainless_steel density is used as the calculation constant for the 316L/1.4404 stainless family."
  uncertainty_notes:
    - "Mass is CAD-derived rather than a catalog weight, and could be low or high if the STEP omits small seals, fasteners, or internal features belonging to this valve part."
material:
  primary_material: "AISI 316L / EN 1.4404 stainless steel valve component, with EPDM present in the valve material set"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 164 material/description text includes '_aisi_316l-1_4404_-_epdm: part 1 valve sv04_din_cc_dn40_-'. Local assembly STEP material extraction for product 3X1_valve_part_1 returned only placeholder material Generic at density 1000.0, which does not resolve material beyond the BOM row text."
    evidence_basis: "bom_provided"
  assumptions:
    - "For the part-1 CAD solid, the metal valve body is modeled as the dominant material, while EPDM is retained as part of the valve-level material set."
  uncertainty_notes:
    - "The BOM text does not identify whether any EPDM volume is physically included in part 1 versus adjacent valve rows, so downstream modeling should avoid assigning an EPDM fraction to this row until the valve subassembly is split."
how_to_make:
  summary: "Procure as the AMproved ISO-KF DN40 disc-valve component for current modeling; a plausible local route is machined 316L stainless valve-body production, EPDM seal integration at valve assembly level, cleaning/passivation, and fit/leak inspection."
  manufacturing_steps:
    - "Procure route: buy the AMproved ISO-KF DN40 disc valve and treat 3X1 as one vendor-supplied valve component."
    - "Local route: machine the roughly 38 x 45.5 x 38 mm stainless valve-body component from 316L/1.4404 bar or near-net blank, including the central bore and external lug features visible in CAD."
    - "Deburr, clean, and passivate the stainless surfaces for vacuum/powder-handling service."
    - "Assemble with the mating valve part and EPDM sealing element, then inspect manual positions, fit, closure, and leak/powder-tightness."
  source:
    url_or_path: "https://www.amproved.com/iso-kf-dn-40-scheibenventil.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3X1_valve_part_1.step; research/ream250_bom/ream250_bom_row_0164_3X1__views_2x2.png"
    cited_fact_or_basis: "AMproved identifies the product as an ISO-KF DN40 disc valve with 3 detent positions for manual control/closure in AM-machine pipework. FreeCAD measured a 38.00 x 45.50 x 38.00 mm one-solid part, and the contact sheet shows a compact bored cylindrical valve-body component with lugs. The detailed machining, passivation, seal integration, and inspection route is inferred from material, geometry, and valve service rather than stated by the vendor. targeted_web_search: searched 'AMPROVED ISO-KF DN 40 Scheibenventil AISI 316L 1.4404 EPDM', 'AMproved ISO-KF DN40 Scheibenventil weight material', 'sv04_din_cc_dn40 316L EPDM valve', and 'ISO-KF DN40 disc valve 316L EPDM manufacturing'; results resolved row-matched product function/material wording but did not provide a row-specific manufacturing process or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The visible compact bored body and stainless material make subtractive machining from stainless stock a plausible local manufacturing route."
    - "EPDM sealing is handled during valve-level assembly rather than during fabrication of the metal part-1 body."
  uncertainty_notes:
    - "The vendor page does not specify production method, tolerances, seal geometry, surface finish, or leak-test standard; those would matter for a self-manufactured replacement."
kb_implications:
  - "item_granularity: simple_part - model 3X1 as one reusable 316L stainless valve-body component within a larger ISO-KF DN40 disc-valve assembly; keep EPDM sealing as valve-level context unless later CAD or BOM evidence assigns it to this exact part."
---

Research result for reAM250 BOM row 164.
