---
row_identity:
  item: "1A1"
  cad_file: "1A1_back_plate"
  source_row_number: 2
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Large custom back plate or rear structural frame for the reAM250 1A-side monitoring/chamber interface, providing a tall stiffened mounting plate with apertures or bosses for adjacent optical and sealing hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A1_back_plate.step; research/ream250_bom/ream250_bom_row_0002_1A1__views_2x2.png"
    cited_fact_or_basis: "BOM row 2 identifies item 1A1, quantity 1, CAD file 1A1_back_plate. The manifest maps row 2 to gold_export/parts/1A1_back_plate.step as a matched part export. FreeCAD measured one solid with a 460.00 x 96.13 x 900.00 mm bounding box; the rendered contact sheet shows a tall rectangular perimeter plate/frame with diagonal bracing or lightening ribs and circular interface features. Neighboring 1A rows include schlieren-imaging flanges, a flow-rectifier mounting plate, seals, and a cover."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name back_plate is interpreted literally as a rear plate/frame in the same 1A optical or chamber-interface group."
    - "The visible ribs and perimeter structure are interpreted as stiffness and lightening features rather than separate subparts."
  uncertainty_notes:
    - "The local BOM/CAD evidence identifies the part's structural interface role, but not the exact mating assemblies, sealing load case, or optical alignment requirements."
mass:
  value_kg: 41.21
  basis: "FreeCAD volume 15,261,919.417 mm^3 equals 0.015261919 m^3. Using an aluminum-alloy density of 2700 kg/m^3 from kb/materials/properties.yaml gives 0.015261919 m^3 * 2700 kg/m^3 = 41.21 kg per unit. BOM quantity is 1, so the row total is also about 41.21 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A1_back_plate.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; web_search"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 15,261,919.417 mm^3, area 996,027.013 mm^2, and bounding box 460.00 x 96.13 x 900.00 mm. Local assembly STEP material extraction for product 1A1_back_plate returned only material Generic with density 1000.0, which is placeholder metadata under the task criteria. kb/materials/properties.yaml lists aluminum density as 2700 kg/m^3. targeted_web_search: queries tried \"1A1_back_plate\" reAM250 material, \"reAM250\" \"1A1\" \"back_plate\", \"1A1_back_plate\", and \"reAM250\" \"back plate\"; results found duplicate reAM250 BOM listings and general reAM250 paper context, but no row-specific mass, material, or drawing for 1A1_back_plate."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The isolated STEP solid volume is used as the complete per-unit geometry for one physical back plate."
    - "Aluminum alloy is used as the mass basis because adjacent large custom reAM250 plate rows use aluminum metadata and the CAD shape resembles a machined structural plate/frame; this is not row-specific material evidence."
  uncertainty_notes:
    - "Mass is most sensitive to the unresolved material: using generic steel density would make the same CAD volume about 119.8 kg instead of 41.21 kg."
    - "The rendered preview reports a 460.00 x 40.00 x 900.00 mm visual bounding box while the raw FreeCAD read reports 96.13 mm in one axis; the mass estimate uses measured solid volume rather than display thickness."
material:
  primary_material: "aluminum alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAM250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0002_1A1__views_2x2.png; web_search"
    cited_fact_or_basis: "BOM row 2 has blank material fields. Local assembly STEP material extraction for product 1A1_back_plate returned material Generic with density 1000.0, which is placeholder metadata under the task criteria. The contact sheet shows a large custom plate/frame geometry. targeted_web_search: queries tried \"1A1_back_plate\" reAM250 material, \"reAM250\" \"1A1\" \"back_plate\", \"1A1_back_plate\", and \"reAM250\" \"back plate\"; results found duplicate reAM250 BOM listings and general reAM250 paper context, but no row-specific alloy, material callout, or vendor drawing."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A broad aluminum-alloy family is chosen from geometry and neighboring reAM250 machined plate precedent, not from row-specific metadata."
  uncertainty_notes:
    - "The exact alloy, temper, coating, and surface-treatment requirements remain unresolved for this row."
how_to_make:
  summary: "Fabricate as a custom machined aluminum-alloy back plate/frame from thick plate or billet stock, with CNC-machined perimeter, rib/lightening geometry, mounting holes, circular interface features, and finished mating faces."
  manufacturing_steps:
    - "Procure aluminum-alloy plate or billet stock large enough for the approximately 460 x 900 mm finished envelope and local thickness/features."
    - "Rough-cut the rectangular blank, leaving machining allowance on the perimeter and faces."
    - "CNC mill the perimeter, pockets or rib reliefs, diagonal web geometry, and circular interface features shown in the CAD."
    - "Drill, tap, counterbore, or countersink mounting patterns needed for neighboring schlieren-imaging, seal, cover, and flow-rectifier interface hardware."
    - "Deburr, clean, and inspect flatness, hole locations, aperture locations, and mating faces against the CAD model."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A1_back_plate.step; research/ream250_bom/ream250_bom_row_0002_1A1__views_2x2.png; web_search"
    cited_fact_or_basis: "The row-specific STEP and contact sheet show one large plate/frame-like solid with a 460.00 x 96.13 x 900.00 mm FreeCAD bounding box, perimeter members, diagonal rib/lightening geometry, and circular interface features. targeted_web_search: queries tried \"1A1_back_plate\" reAM250 manufacturing, \"reAM250\" \"1A1_back_plate\" drawing, and \"reAM250\" \"back plate\" material; results found duplicate BOM listings and general reAM250 context but no row-specific process plan, drawing, tolerance note, or vendor route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Subtractive CNC machining is selected because the part appears to be a one-piece custom plate/frame with planar faces, relieved/ribbed geometry, and precise mounting/interface features."
    - "No welding, casting, additive build, coating, or heat-treatment step is specified because the row evidence does not state those requirements."
  uncertainty_notes:
    - "This is a plausible KB manufacturing route, not a shop traveler; tolerances, datum scheme, sealing flatness, surface finish, and actual stock form are not provided by the row evidence."
kb_implications:
  - "item_granularity: simple_part - model later as one custom machined aluminum-alloy back plate/frame; keep neighboring optical flanges, seals, cover, and flow-rectifier mounting plate as separate BOM items."
---

Research result for reAM250 BOM row 2.
