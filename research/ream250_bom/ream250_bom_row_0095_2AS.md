---
row_identity:
  item: "2AS"
  cad_file: "2AS_end_switch_sensor_bottom"
  source_row_number: 95
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin bottom end-switch sensor target or mounting flag associated with the reAM250 bottom inductive end-switch sensor group."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AS_end_switch_sensor_bottom.step"
    cited_fact_or_basis: "BOM row 95 identifies item 2AS as quantity 1, cad_file 2AS_end_switch_sensor_bottom. Neighboring BOM rows identify 2AQ as inductive_sensor_mount, 2AT3 as a Balluff inductive sensor bottom, and 2AU3 as a Balluff inductive sensor top. FreeCAD measured the row STEP as one solid with a 50.00 x 65.00 x 2.00 mm bounding box, and the rendered contact sheet shows a thin L-shaped plate/flag with a visible round hole. targeted_web_search: searched \"2AS_end_switch_sensor_bottom material\", \"2AS end switch sensor reAM250 material\", \"reAM250 2AS end switch sensor\", and \"end switch sensor bottom 2AS material\"; found duplicate reAM250 BOM listings and generic end-switch pages, but no row-specific vendor/function source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row name and adjacency to the Balluff bottom inductive sensor row are interpreted as a bottom end-switch target or sensor-side flag rather than the purchased sensor itself."
    - "The round feature visible in the preview is interpreted as a mounting or clearance hole for fastening or aligning the flag/plate in the local end-switch assembly."
  uncertainty_notes:
    - "The BOM and CAD do not explicitly state whether this part is the sensed target, a protective flag, or a small sensor-side mounting plate; all interpretations imply the same simple thin-plate KB granularity."
mass:
  value_kg: 0.029
  basis: "FreeCAD measured 3729.515 mm^3 volume, 4235.763 mm^2 area, and a 50.00 x 65.00 x 2.00 mm bounding box. Using the local steel density table value of 7850 kg/m^3 gives 0.0293 kg, rounded to 0.029 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AS_end_switch_sensor_bottom.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, 3729.515 mm^3 volume, 4235.763 mm^2 area, and a 50.00 x 65.00 x 2.00 mm bounding box. kb/materials/properties.yaml lists generic steel density as 7850 kg/m^3. targeted_web_search: searched \"2AS_end_switch_sensor_bottom material\", \"2AS end switch sensor reAM250 material\", \"reAM250 2AS end switch sensor\", and \"end switch sensor bottom 2AS material\"; found no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid is treated as the physical material volume of the part."
    - "Generic steel density is used because the part appears to serve an inductive end-switch target/flag role and the local material metadata does not resolve a grade."
  uncertainty_notes:
    - "If the plate is aluminum rather than steel, the same CAD volume would imply about 0.010 kg; the material uncertainty is therefore the main mass uncertainty."
material:
  primary_material: "unknown metal/alloy sheet"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AS_end_switch_sensor_bottom.step"
    cited_fact_or_basis: "BOM row 95 names the part 2AS_end_switch_sensor_bottom. Neighboring BOM rows place it with Balluff inductive sensors and M12x1 sensor nuts. The row STEP measures as a 2.00 mm thick plate-like solid. Assembly STEP material extraction returned only material 'Allgemein' with density 1000.0, which is a placeholder and not resolved material evidence. targeted_web_search: searched \"2AS_end_switch_sensor_bottom material\", \"2AS end switch sensor reAM250 material\", \"reAM250 2AS end switch sensor\", and \"end switch sensor bottom 2AS material\"; found no row-specific vendor, drawing, or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A metal sheet family is selected because an inductive end-switch target/flag should be a reliable metal target and the geometry is a thin plate with a fastening or clearance feature."
    - "The result keeps the material at family level because neither BOM fields, STEP metadata, nor targeted web searches identify a specific alloy or grade."
  uncertainty_notes:
    - "The specific alloy, magnetic response, surface finish, and whether the actual material is carbon steel, stainless steel, or aluminum are unresolved."
how_to_make:
  summary: "Make as a simple thin sheet-metal flag or bracket: cut the 2 mm plate profile, drill or cut the visible hole/clearance feature, deburr, and finish as needed for the end-switch assembly."
  manufacturing_steps:
    - "Cut the L-shaped 2 mm sheet profile from ferrous sheet stock by laser, waterjet, CNC router/mill, or manual sheet cutting."
    - "Drill, punch, or cut the visible round mounting or clearance hole from the CAD-defined position."
    - "Deburr edges and holes, then apply corrosion protection or passivation if the selected steel grade requires it."
    - "Install and align the plate/flag in the bottom end-switch sensor assembly with the adjacent inductive sensor hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AS_end_switch_sensor_bottom.step; research/ream250_bom/ream250_bom_row_0095_2AS__views_2x2.png"
    cited_fact_or_basis: "The row STEP measures one 50.00 x 65.00 x 2.00 mm solid, and the rendered contact sheet shows a thin plate-like L-shaped part with a visible round hole. targeted_web_search: searched \"2AS_end_switch_sensor_bottom material\", \"2AS end switch sensor reAM250 material\", \"reAM250 2AS end switch sensor\", and \"end switch sensor bottom 2AS material\"; found no row-specific manufacturing-process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The dominant manufacturing route is inferred from the thin constant-thickness plate geometry and visible plate feature."
    - "Hole size, exact contour, and any edge chamfers should be taken from CAD during downstream fabrication planning, not from the preview image."
  uncertainty_notes:
    - "The CAD preview is visual triage only; it does not establish tolerances, finish requirements, or whether small chamfers or bends are functionally required."
kb_implications:
  - "item_granularity: simple_part - thin plate/flag with one dominant sheet-cutting or machining route; no sub-BOM is implied by the row evidence."
---

CAD preview: `research/ream250_bom/ream250_bom_row_0095_2AS__views_2x2.png`
