---
row_identity:
  item: "6A"
  cad_file: "6A_conveyor_belt"
  source_row_number: 167
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Closed conveyor or timing-belt style loop for subsystem 6, providing a flexible moving belt span over pulleys or guides."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6A_conveyor_belt.step; research/ream250_bom/ream250_bom_row_0167_6A__views_2x2.png"
    cited_fact_or_basis: "BOM row 167 identifies item 6A as 6A_conveyor_belt from zahriemen24.de with quantity 1. The manifest maps the row to one matched_existing vendor_component STEP file. FreeCAD measured one solid with bbox about 104.18 x 138.06 x 268.00 mm, and the rendered contact sheet shows a closed flexible belt loop with a narrow raised/rounded edge."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name and closed-loop CAD form indicate a conveyor or synchronous belt element rather than a rigid pulley, bracket, or frame part."
  uncertainty_notes:
    - "The BOM row does not state the transported material, tooth profile, pulley layout, or whether the belt is primarily used for conveying or synchronized motion."
mass:
  value_kg: 0.15
  basis: "FreeCAD volume 114921.335 mm^3 = 0.000114921 m^3. Using an engineering effective density of 1300 kg/m^3 for a mostly polyurethane belt with embedded steel or aramid tension members gives 0.149 kg, rounded to 0.15 kg per unit. BOM quantity is 1, so the row total is also about 0.15 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6A_conveyor_belt.step; https://www.z24.de/zahnriemen/pu-zahnriemen"
    cited_fact_or_basis: "FreeCAD measured one row STEP solid with volume 114921.335 mm^3. Z24 describes PU timing belts as polyurethane belts reinforced with high-strength tension members, generally steel tension cords, with Kevlar cords available for many meterware profiles. targeted_web_search: queries tried: 'zahriemen24.de conveyor belt material polyurethane timing belt weight', 'Zahriemen24 Polyurethan Zahnriemen Stahlzugtraeger Gewicht', and '6A_conveyor_belt zahriemen24'; result: found row-family material facts but no row-specific supplier mass, belt profile, or cord volume fraction."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid volume is treated as the physical volume of one belt represented by the BOM row."
    - "An effective density of 1300 kg/m^3 is used as a coarse mixed-material estimate for a mostly polyurethane belt with a smaller tension-cord contribution."
  uncertainty_notes:
    - "Mass depends on whether the CAD body includes all teeth, coatings, backing layers, and internal cords as modeled volume."
    - "No row-specific catalog weight or material split was found, so this is an order-of-magnitude planning estimate."
material:
  primary_material: "polyurethane belt body with high-strength tension members, probably steel cords for a standard PU timing-belt family or Kevlar/aramid cords if specified for the exact profile"
  source:
    url_or_path: "https://www.z24.de/zahnriemen/pu-zahnriemen; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 167 lists manufacturer zahriemen24.de. Z24 states that PU timing belts use polyurethane and high-strength tension members, generally steel tension cords, with Kevlar tension strands available for many polyurethane meterware profiles. Local assembly STEP material extraction for 6A_conveyor_belt returned only Generic with density 1000.0, which is placeholder metadata."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The manufacturer's PU timing-belt product-family construction applies because the BOM source is zahriemen24.de and the CAD/row name match a closed belt item."
  uncertainty_notes:
    - "The exact profile, polyurethane formulation, coating, and cord material are not specified in the BOM row or STEP metadata."
how_to_make:
  summary: "Procure as a catalog or custom PU conveyor/timing belt from a belt supplier; a local route would manufacture PU belt stock around tension cords, close or form it as an endless loop, cut it to final width, and verify fit on the matching pulleys or guides."
  manufacturing_steps:
    - "Select belt width, loop length, profile, backing or transport surface, and tension-cord option to match the CAD loop and machine pulleys."
    - "For open or welded stock, extrude polyurethane around the tension cords, cool the belt, cut it to length, and weld or otherwise close the belt ends."
    - "For a truly endless flex belt, wind the tension cord on forming wheels or a mold and extrude or mold polyurethane around the cord before final width cutting."
    - "Inspect belt width, loop length, profile engagement, tracking, and installed tension."
  source:
    url_or_path: "https://www.z24.de/zahnriemen/pu-zahnriemen; https://www.alphabelt.de/en/Timing-Belts/"
    cited_fact_or_basis: "Z24 lists PU timing-belt variants including closed manufactured belts, open meterware, welded meterware, flex belts, and double-sided belts. Alphabelt describes open-end timing belts as polyurethane continuously extruded onto tension cords, then cooled and rolled; it describes welded belts cut and welded from stock and flex belts made by winding tension cord on forming wheels before polyurethane is extruded around the cords. targeted_web_search: queries tried: 'PU timing belt welded manufacturing extruded tension cords', 'polyurethane timing belt flex belt manufacturing tension cord forming wheels', and 'zahriemen24 PU Zahnriemen Meterware verschweisst'; result: found product-family manufacturing routes but no route specific to this exact 6A belt."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The later KB route should preserve the closed-loop belt geometry and pulley interface rather than substitute generic flat belt stock."
  uncertainty_notes:
    - "The BOM row does not specify whether this exact belt is closed manufactured, welded meterware, or flex-manufactured."
kb_implications:
  - "item_granularity: simple_part - Model as one replaceable conveyor/timing belt wear component, with PU body and tension-cord construction captured in notes rather than separate subparts unless belt manufacture becomes a priority."
---
