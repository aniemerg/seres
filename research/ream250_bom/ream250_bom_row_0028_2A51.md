---
row_identity:
  item: "2A51"
  cad_file: "2A51_linear_guide_HGL15CA2R600Z0H"
  source_row_number: 28
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.hiwin.de/de/Produkte/Profilschienenf%C3%BChrungen/Auswahl-%C3%BCber-Profilschiene/HGR/HGR-R/HGR15R4000H/p/5-001920"
function:
  summary: "HIWIN HGR15R profile rail used with the adjacent HGL15 linear-guide carriages to provide the fixed precision raceway for low-friction linear motion on the reAM250 axis."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A51_linear_guide_HGL15CA2R600Z0H.step; research/ream250_bom/ream250_bom_row_0028_2A51__views_2x2.png; https://www.hiwin.de/en/Products/Linear-guideways/Profile-rails/Ball-guides/Series-HGR/HGR-R/HGR15R4000H/p/5-001920"
    cited_fact_or_basis: "BOM row 28 identifies item 2A51 as quantity 2, CAD file 2A51_linear_guide_HGL15CA2R600Z0H, description linear guide rail, manufacturer HIWIN, and the HGR15R4000H product route. The manifest maps the row to a matched existing vendor-component STEP. The HIWIN product page identifies type HGR15R4000H, article number 5-001920, under Linear guideways / Profile rails / Ball guides / Series HGR / HGR-R, and states that linear guideways use balls or rolls between rail and block for precise linear movement. FreeCAD measured one solid with bounding box 15.00 x 600.00 x 15.00 mm, and the contact sheet shows a long narrow rail profile. official_alternate_route_check: original BOM URL is the German hiwin.de route; the cited English hiwin.de page is the same official domain and same product/article route, matching HGR15R4000H and 5-001920."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted as the rail, not the carriage, because the BOM description, product URL, and CAD geometry identify the HGR rail while adjacent rows 2A3 and 2A4 cover HGL15CA carriages."
  uncertainty_notes:
    - "The BOM URL product code is for a 4000 mm production-length rail, while the supplied row STEP is a 600 mm rail segment; the row-specific CAD length is used for installed-part mass and function."
mass:
  value_kg: 0.87
  basis: "Per-unit mass for one 600 mm rail segment. HIWIN lists HGR15R weight as 1.45 kg/m; FreeCAD measured the row STEP length as 600.00 mm, so 1.45 kg/m * 0.600 m = 0.870 kg per rail. BOM quantity is 2, so the row total is about 1.74 kg. FreeCAD measured volume 110239.319 mm^3, area 40247.204 mm^2, and bounding box 15.00 x 600.00 x 15.00 mm; using the local generic steel density 7850 kg/m^3 gives about 0.865 kg, a close sanity check."
  source:
    url_or_path: "https://www.hiwin.de/en/Products/Linear-guideways/Profile-rails/Ball-guides/Series-HGR/HGR-R/HGR15R4000H/p/5-001920; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A51_linear_guide_HGL15CA2R600Z0H.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "The HIWIN HGR15R4000H product page lists rail width 15 mm, rail height 15 mm, hole pitch 60 mm, weight 1.45 kg/m, and 4000 mm production length. FreeCAD measured the row STEP as 1 solid, volume 110239.319 mm^3, area 40247.204 mm^2, and bounding box 15.00 x 600.00 x 15.00 mm. The local material properties table lists generic steel density 7850 kg/m^3. official_alternate_route_check: original BOM URL is the German hiwin.de product route; the cited English hiwin.de page is the same official product/article route and resolves the rail weight per meter."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD-exported 600 mm segment represents one physical rail in the BOM row, so the official kg/m value is scaled by the measured row length."
    - "The steel-density calculation is used only as a sanity check, not as the primary mass source."
  uncertainty_notes:
    - "End-distance and cut-length tolerance details from the original rail order are not fully recoverable from the BOM row, but they do not materially change the 0.87 kg planning mass."
material:
  primary_material: "carbon steel precision linear-guide rail, with optional HIWIN rail coatings depending on ordered finish"
  source:
    url_or_path: "https://www.hiwin.com/wp-content/uploads/HG-Info.pdf; https://www.hiwin.de/en/Products/Linear-guideways/Profile-rails/Ball-guides/Series-HGR/HGR-R/HGR15R4000H/p/5-001920; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "HIWIN HG-series material convention states that no material symbol means carbon steel and M means stainless steel. The row product code HGR15R4000H has no M material suffix, and the HIWIN product page confirms the HGR15R4000H identity. The same product page describes optional HICOAT CZS zinc coating and HICOAT CTS thin chrome coating for linear-guide rails. Local assembly STEP material extraction for 2A51_linear_guide_HGL15CA2R600Z0H returned only placeholder material Generic with density 1000.0, so STEP metadata does not resolve material. standard_part_convention: parameters present are series HG, rail type R, size 15, fastening from above, 4000 mm production length, accuracy H, and no M material suffix; this is sufficient for broad carbon-steel versus stainless family, but not exact alloy grade, heat treatment, or ordered coating."
    evidence_basis: "standard_part_convention"
  assumptions: []
  uncertainty_notes:
    - "The exact steel grade, heat treatment, surface hardness, and whether this specific row used an optional coating are not specified by the row evidence."
how_to_make:
  summary: "Locally produce a 600 mm carbon-steel precision linear-guide rail with HGR15-class envelope, counterbored top-mounting holes, hardened/ground raceways, datum faces, corrosion/wear protection as needed, and inspection against the mating HGL/HG15 carriage geometry."
  manufacturing_steps:
    - "Prepare carbon-steel rail stock or a near-net rail blank long enough for the 600 mm finished part plus workholding allowance."
    - "Machine the rectangular rail envelope, bottom datum, side datums, and HGR15-class raceway profile along the full length."
    - "Drill and counterbore the top-mounting holes at the row-matched pitch and end offsets needed by the 600 mm CAD geometry."
    - "Heat treat the rail for guideway service, then precision grind the raceways, mounting face, and side datums to the straightness, parallelism, surface finish, and accuracy required by the mating carriage."
    - "Deburr or chamfer ends and hole edges, apply any selected corrosion/wear coating, clean and protect the rail, then inspect hole pattern, length, raceway geometry, hardness, straightness, and carriage fit."
  source:
    url_or_path: "https://www.hiwin.de/en/Products/Linear-guideways/Profile-rails/Ball-guides/Series-HGR/HGR-R/HGR15R4000H/p/5-001920; https://www.hiwin.com/wp-content/uploads/HG-Info.pdf; research/ream250_bom/ream250_bom_row_0028_2A51__views_2x2.png"
    cited_fact_or_basis: "The HIWIN product page identifies HGR15R4000H as an HGR-R profile rail, gives 15 mm rail width and height, top-mounting hole dimensions, 60 mm pitch, weight per meter, production length details, and notes mechanical or manual chamfering videos for linear guideways. The HG-series convention identifies the no-M material option as carbon steel. The rendered contact sheet shows a long straight rail profile. The detailed local fabrication route is inferred from the sourced geometry, material convention, and precision-rail function rather than stated as HIWIN's factory process. targeted_web_search: checked the BOM-provided HIWIN route and searched 'HGR15R4000H Hiwin mass material', 'HIWIN HGR15R rail material carbon steel M stainless steel', 'HIWIN HG rail manufacturing grinding heat treatment', and 'HIWIN linear guideway HGR15R dimensions pitch weight'; results found row-matched product, dimensions, mass, material-code convention, and generic chamfering information, but no row-specific manufacturing-process sheet."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "This simple-part route models the rail as locally produced precision guideway hardware, using the vendor evidence only to constrain geometry, material family, hole pattern, and functional interface."
    - "The manufacturing route describes a plausible closure path, not a sourced factory process specification."
  uncertainty_notes:
    - "The exact alloy grade, heat treatment cycle, raceway grinding sequence, coating choice, inspection tolerance stack, and end-offset tolerances are not provided by the row evidence."
kb_implications:
  - "item_granularity: simple_part - Treat as a reusable single precision linear-guide rail compatible with HGL/HG15 carriages; capture heat treatment, grinding, hole machining, coating, and inspection in the manufacturing route rather than modeling it as a complex module."
---

Research result for the leased reAM250 BOM row only.
