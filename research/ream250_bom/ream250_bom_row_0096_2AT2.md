---
row_identity:
  item: "2AT2"
  cad_file: "2AT2_nut_M12x1"
  source_row_number: 96
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Hex mounting/locking nut for an M12x1 Balluff BES 516-356-S4-C inductive proximity sensor, used to clamp the threaded cylindrical sensor body in position."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0096_2AT2__views_2x2.png; https://www.balluff.com/en-us/products/BES01H6"
    cited_fact_or_basis: "BOM row 96 names 'Nut M12 x 1 BALLUFF BES 516-356-S4-C_1:' with quantity 2; CAD preview shows a thin hex nut with internal thread opening; Balluff BES01H6 page identifies BES 516-356-S4-C as an M12x1 threaded cylindrical inductive proximity sensor."
    evidence_basis: "bom_provided"
  assumptions:
    - "The nut is associated with the named M12x1 sensor rather than being a separate functional module."
  uncertainty_notes: []
mass:
  value_kg: 0.005
  basis: "Per-unit estimate for one nut. FreeCAD measured one solid with volume 609.594 mm^3 and bounding box about 4.00 x 19.63 x 19.63 mm; using 8030 kg/m^3 for stainless steel 304/1.4301 gives 0.00490 kg, while 8500 kg/m^3 for brass gives 0.00518 kg. BOM quantity is 2, so row total is about 0.010 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AT2_nut_M12x1.step; kb/materials/properties.yaml; https://balluff-ua.com/pdf/KT_Nuts_EN.pdf"
    cited_fact_or_basis: "FreeCAD CAD measurement: 1 solid, volume 609.594 mm^3, area 648.760 mm^2, bounding box 4.00 x 19.63 x 19.63 mm. Local density table gives stainless_steel_304/1_4301 as 8030 kg/m^3 and brass as 8500 kg/m^3. Balluff nut table lists M12x1 metal and stainless nut variants with 17 mm wrench size and 4 mm height, matching the CAD scale. targeted_web_search: searched 'Balluff BES 516-356-S4-C M12x1 nut material', 'Balluff M12x1 nut proximity sensor stainless steel', and 'site:balluff.com M12x1 nut Balluff stainless steel proximity sensor'; results found matching Balluff nut variants but not a row-specific nut part number."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid volume is the physical nut volume, and thread-detail simplification does not materially change the estimate at this scale."
    - "A 0.005 kg planning value covers the plausible stainless steel and nickel-plated brass M12x1 Balluff nut variants."
  uncertainty_notes:
    - "Assembly STEP material metadata for this product was only 'Generic' with density 1000.0, so it was not used as material evidence."
    - "The BOM row does not state Balluff accessory part number 500462 or 636981, so the exact alloy variant remains unidentified."
material:
  primary_material: "metal sensor mounting nut: Balluff M12x1 family includes nickel-plated brass and stainless steel 1.4305 variants"
  source:
    url_or_path: "https://balluff-ua.com/pdf/KT_Nuts_EN.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Balluff accessory table lists M12x1 nut variants: metal nut part 500462 with material 'Ms nickel plated' and stainless steel nut part 636981 with material 1.4305. Local STEP material extraction for 2AT2_nut_M12x1 returned only Generic at density 1000.0. targeted_web_search: searched 'Balluff BES 516-356-S4-C M12x1 nut material', 'Balluff M12x1 nut proximity sensor stainless steel', and 'site:balluff.com M12x1 nut Balluff stainless steel proximity sensor'; no source tied row 96 to one exact nut part number."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Treat as a metal M12x1 sensor mounting nut for KB planning, with the exact Balluff variant deferred."
  uncertainty_notes:
    - "The row description names the sensor model, not a nut accessory order code, so material should not be narrowed to one grade without additional BOM evidence."
how_to_make:
  summary: "Prepare as a standard Balluff M12x1 sensor mounting nut; use small metal hex stock or a cold-formed blank, drilled/tapped M12x1, faced to about 4 mm thickness, deburred, and optionally nickel plated if using the brass variant"
  manufacturing_steps:
    - "Select stainless steel or brass hex stock/blank sized for a 17 mm wrench M12x1 nut."
    - "Cut or face blank to about 4 mm thickness."
    - "Drill, tap M12x1 internal thread, and deburr edges and thread starts."
    - "Apply nickel plating only for the brass/nickel-plated variant; otherwise clean/passivate stainless as appropriate."
    - "Inspect thread fit on an M12x1 sensor body and verify wrench flats."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0096_2AT2__views_2x2.png; https://balluff-ua.com/pdf/KT_Nuts_EN.pdf"
    cited_fact_or_basis: "CAD preview shows a thin hex internally threaded nut; Balluff accessory table gives M12x1 nuts with 17 mm wrench size and 4 mm height in metal/stainless variants. targeted_web_search: searched the Balluff sensor and M12x1 nut terms above; sources identify standard nut variants but do not state a detailed manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Machining/tapping route is a plausible low-volume local manufacturing path for KB closure; production hardware could also be cold formed and tapped."
  uncertainty_notes:
    - "No cited source specified Balluff's actual factory process for this nut."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable M12x1 metal sensor mounting nut/locknut rather than as part of the sensor module; keep material variant notes on the BOM or recipe if exact accessory part number is later recovered."
---

