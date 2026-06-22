---
row_identity:
  item: "2AR"
  cad_file: "2AR_end_switch_sensor_top"
  source_row_number: 94
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin top end-switch sensor target or mounting flag associated with the reAM250 top inductive end-switch sensor group."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AR_end_switch_sensor_top.step"
    cited_fact_or_basis: "BOM row 94 identifies item 2AR as quantity 1, cad_file 2AR_end_switch_sensor_top. Neighboring BOM rows identify 2AQ as inductive_sensor_mount, 2AT3 as inductive sensor bottom, and 2AU3 as inductive sensor top. FreeCAD measured the row STEP as one solid with a 40.00 x 60.00 x 2.00 mm bounding box, and the rendered contact sheet shows a thin L-shaped plate/flag with two round holes. targeted_web_search: searched \"2AR_end_switch_sensor_top material\", \"2AR end switch sensor reAM250 material\", and \"end switch sensor top bracket material\"; found duplicate reAM250 BOM listings and generic end-switch material pages, but no row-specific vendor/function source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row name and adjacency to the Balluff top inductive sensor row are interpreted as a top end-switch target or sensor-side flag rather than the purchased sensor itself."
    - "The two holes visible in the preview are interpreted as mounting holes for fastening the flag/plate into the local end-switch assembly."
  uncertainty_notes:
    - "The BOM and CAD do not explicitly state whether this part is the sensed target, a protective flag, or a small sensor-side mounting plate; all interpretations imply the same simple thin-plate KB granularity."
mass:
  value_kg: 0.028
  basis: "FreeCAD measured 3529.515 mm^3 volume, 3975.763 mm^2 area, and a 40.00 x 60.00 x 2.00 mm bounding box. Using the local steel density table value of 7850 kg/m^3 gives 0.0277 kg, rounded to 0.028 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AR_end_switch_sensor_top.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, 3529.515 mm^3 volume, 3975.763 mm^2 area, and a 40.00 x 60.00 x 2.00 mm bounding box. kb/materials/properties.yaml lists generic steel density as 7850 kg/m^3. targeted_web_search: searched \"2AR_end_switch_sensor_top material\", \"2AR end switch sensor reAM250 material\", and \"end switch sensor top bracket material\"; found no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid is treated as the physical material volume of the part."
    - "Generic steel density is used because the part appears to serve an inductive end-switch target/flag role and the local material metadata does not resolve a grade."
  uncertainty_notes:
    - "If the plate is aluminum rather than steel, the same CAD volume would imply about 0.0095 kg; the material uncertainty is therefore the main mass uncertainty."
material:
  primary_material: "unknown metal/alloy sheet"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AR_end_switch_sensor_top.step"
    cited_fact_or_basis: "BOM row 94 names the part 2AR_end_switch_sensor_top. Neighboring BOM rows place it with Balluff inductive sensors and M12x1 sensor nuts. The row STEP measures as a 2.00 mm thick plate-like solid. Assembly STEP material extraction returned only material 'Allgemein' with density 1000.0, which is a placeholder and not resolved material evidence. targeted_web_search: searched \"2AR_end_switch_sensor_top material\", \"2AR end switch sensor reAM250 material\", and \"end switch sensor top bracket material\"; found no row-specific vendor, drawing, or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A metal sheet family is selected because an inductive end-switch target/flag should be a reliable metal target and the geometry is a thin plate with fastening holes."
    - "The result keeps the material at family level because neither BOM fields, STEP metadata, nor targeted web searches identify a specific alloy or grade."
  uncertainty_notes:
    - "The specific alloy, magnetic response, surface finish, and whether the actual material is carbon steel, stainless steel, or aluminum are unresolved."
how_to_make:
  summary: "Make as a simple thin sheet-metal flag or bracket: cut the 2 mm plate profile, drill or cut the two mounting holes, deburr, and finish as needed for the end-switch assembly."
  manufacturing_steps:
    - "Cut the L-shaped 2 mm sheet profile from ferrous sheet stock by laser, waterjet, CNC router/mill, or manual sheet cutting."
    - "Drill, punch, or cut the two mounting holes visible in the CAD preview."
    - "Deburr edges and holes, then apply corrosion protection or passivation if the selected steel grade requires it."
    - "Install and align the plate/flag in the top end-switch sensor assembly with the adjacent inductive sensor hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AR_end_switch_sensor_top.step; research/ream250_bom/ream250_bom_row_0094_2AR__views_2x2.png"
    cited_fact_or_basis: "The row STEP measures one 40.00 x 60.00 x 2.00 mm solid, and the rendered contact sheet shows a thin plate-like L-shaped part with two round holes. targeted_web_search: searched \"2AR_end_switch_sensor_top material\", \"2AR end switch sensor reAM250 material\", and \"end switch sensor top bracket material\"; found no row-specific manufacturing-process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The dominant manufacturing route is inferred from the thin constant-thickness plate geometry and visible mounting holes."
    - "Hole sizes and any bend/edge chamfers should be taken from CAD during downstream fabrication planning, not from the preview image."
  uncertainty_notes:
    - "The CAD preview is visual triage only; it does not establish tolerances, finish requirements, or whether bends/chamfers are functionally required."
kb_implications:
  - "item_granularity: simple_part - thin plate/flag with one dominant sheet-cutting or machining route; no sub-BOM is implied by the row evidence."
---

CAD preview: `research/ream250_bom/ream250_bom_row_0094_2AR__views_2x2.png`
