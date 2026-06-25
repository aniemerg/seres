---
row_identity:
  item: "2AD4"
  cad_file: "2AD4_part_4"
  source_row_number: 47
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Loose spherical rolling/contact element for the top side of an axis bearing group; likely one ball in the axis bearing stack rather than a complete bearing cartridge."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD4_part_4.step; research/ream250_bom/ream250_bom_row_0047_2AD4__views_2x2.png"
    cited_fact_or_basis: "BOM row 47 names the item 'axis bearing top' with quantity 1 and CAD file 2AD4_part_4. FreeCAD measured one solid, volume 63.506 mm^3, area 76.977 mm^2, and bounding box 4.95 x 4.95 x 4.95 mm. The rendered contact sheet shows a near-spherical part."
    evidence_basis: "bom_provided"
  assumptions:
    - "The spherical CAD geometry is interpreted as a bearing ball or point-contact rolling element within the axis bearing top group."
  uncertainty_notes:
    - "The row name does not identify the mating race, preload hardware, or whether this top-bearing row is one of several duplicate balls in a larger bearing arrangement."
mass:
  value_kg: 0.0005
  basis: "Per-unit mass for one BOM row item. CAD volume 63.506 mm^3 = 6.3506e-8 m^3. Using representative steel density 7850 kg/m^3 from kb/materials/properties.yaml gives 0.000499 kg, rounded to 0.0005 kg. BOM quantity is 1, so the row total is also about 0.0005 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD4_part_4.step; kb/materials/properties.yaml; https://www.thomasnet.com/articles/metals-metal-products/52100-steel/"
    cited_fact_or_basis: "FreeCAD measured the row CAD volume as 63.506 mm^3. The local material table gives generic steel density as 7850 kg/m^3. Thomasnet describes 52100 steel as a high-carbon chromium alloy primarily known for rolling element bearings. targeted_web_search: queries tried: 'axis bearing top 2AD4 reAM250', '2AD4_part_4', '5 mm bearing ball material chrome steel AISI 52100 stainless steel'; result: only duplicate BOM listings were found for the row identity, while generic bearing-ball sources support steel/chrome-steel as the likely material family."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid volume is treated as the physical volume of one ball."
    - "The part is modeled as a hardened steel bearing ball; exact alloy is not row-specified."
  uncertainty_notes:
    - "Mass would shift materially if the ball is ceramic or stainless rather than generic/chrome bearing steel, but the CAD volume is small enough that the absolute row-mass impact remains low."
material:
  primary_material: "hardened bearing steel family"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD4_part_4.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.abbottball.com/materials/chrome-steel-balls/"
    cited_fact_or_basis: "The per-part CAD is a 4.95 mm near-sphere and the BOM description is 'axis bearing top'. Assembly STEP material extraction for 2AD4_part_4 returned only Generic with density 1000.0, which does not resolve material. Abbott Ball states AISI Type 52100 chrome steel balls are used in the ball and roller bearing industry and lists size availability beginning at 0.80 mm. targeted_web_search: queries tried: 'axis bearing top 2AD4 reAM250', '2AD4_part_4', '5 mm bearing ball material chrome steel AISI 52100 stainless steel'; result: no row-specific material source was found, but generic bearing-ball sources match the CAD shape and bearing function."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A small bearing ball in this axis-bearing context is more likely hardened steel/chrome steel than polymer or soft metal."
  uncertainty_notes:
    - "Exact grade, corrosion class, hardness grade, and whether the design used chrome steel such as AISI 52100/100Cr6, stainless steel, or ceramic balls are not specified by BOM-side evidence."
how_to_make:
  summary: "Start from bearing-steel wire or slugs, cold-head or form the blank, flash-remove/rough-grind, heat treat, finish-grind/lap/polish, and inspect roundness and surface finish"
  manufacturing_steps:
    - "For local manufacturing, cut or cold-head bearing-steel blanks near 5 mm diameter."
    - "Remove flash and rough-grind to spherical form."
    - "Harden and temper for bearing wear resistance."
    - "Finish grind, lap, polish, clean, and inspect for diameter, roundness, and surface finish."
  source:
    url_or_path: "https://insights.globalspec.com/article/12349/how-are-bearing-balls-made; https://resources.hartfordtechnologies.com/blog/high-quality-precision-ball-manufacturing-a-process-overview; research/ream250_bom/ream250_bom_row_0047_2AD4__views_2x2.png"
    cited_fact_or_basis: "GlobalSpec describes bearing-ball manufacture as converting an unhardened steel slug to a hardened, ground, and polished round ball. Hartford Technologies describes lapping as a final process for high-precision or super-precision ball grades. The CAD preview shows this row item is a small sphere. targeted_web_search: queries tried: 'bearing balls manufacturing process forged ground lapped steel balls', 'how are bearing balls made', '5 mm bearing ball material chrome steel AISI 52100 stainless steel'; result: generic manufacturing sources support the route, but no row-specific manufacturing drawing was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from standard precision steel ball practice, not from a row-specific drawing."
  uncertainty_notes:
    - "A fully Manufacturing route would require precision grinding/lapping and metrology capabilities; without a required ball grade, the tolerance and inspection burden are unresolved."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable small precision bearing ball/rolling element, not as a purchased module or full bearing assembly."
---
