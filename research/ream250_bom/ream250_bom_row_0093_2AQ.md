---
row_identity:
  item: "2AQ"
  cad_file: "2AQ_inductive_sensor_mount"
  source_row_number: 93
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Compact L-shaped mount for positioning the reAM250 inductive end-switch sensors near their top and bottom sensing targets."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AQ_inductive_sensor_mount.step; research/ream250_bom/ream250_bom_row_0093_2AQ__views_2x2.png"
    cited_fact_or_basis: "BOM row 93 identifies item 2AQ as quantity 2, cad_file 2AQ_inductive_sensor_mount. Neighboring BOM rows identify 2AR as end_switch_sensor_top, 2AS as end_switch_sensor_bottom, and 2AT3/2AU3 as Balluff inductive sensors. FreeCAD measured the row STEP as one solid with a 30.00 x 30.00 x 25.00 mm bounding box, and the rendered contact sheet shows an L-shaped bracket with two vertical mounting slots and a rounded slot/opening. targeted_web_search: searched \"2AQ_inductive_sensor_mount material\", \"2AQ inductive_sensor_mount reAM250\", and \"inductive sensor mount material bracket\"; found duplicate reAM250 BOM listings and generic M12 inductive-sensor mount examples, but no row-specific vendor/function source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row name and adjacency to the Balluff top and bottom inductive sensor rows are interpreted as a shared custom mount used twice in the end-switch sensor assembly."
    - "The two vertical slots are interpreted as sensor or fastener adjustment slots for aligning the inductive sensor position."
  uncertainty_notes:
    - "The BOM and CAD do not explicitly state the installed orientation or whether each quantity serves the top and bottom sensor positions, but the local row grouping strongly supports an inductive-sensor mounting role."
mass:
  value_kg: 0.031
  basis: "FreeCAD measured 3952.142 mm^3 volume, 3202.814 mm^2 area, and a 30.00 x 30.00 x 25.00 mm bounding box. Using the local generic steel density table value of 7850 kg/m^3 gives 0.0310 kg per mount, rounded to 0.031 kg. The BOM quantity is 2, so the optional row total would be about 0.062 kg under the same density assumption."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AQ_inductive_sensor_mount.step; kb/materials/properties.yaml; https://www.damencnc.com/en/m12-inductive-sensor-mount-2-detection-plates/a3555"
    cited_fact_or_basis: "FreeCAD measured one solid, 3952.142 mm^3 volume, 3202.814 mm^2 area, and a 30.00 x 30.00 x 25.00 mm bounding box. kb/materials/properties.yaml lists generic steel density as 7850 kg/m^3. A generic DamenCNC M12 inductive sensor mount listing says a similar mount set is made from steel, but it is not row-specific to 2AQ. targeted_web_search: searched \"2AQ_inductive_sensor_mount material\", \"2AQ inductive_sensor_mount reAM250\", and \"inductive sensor mount material bracket\"; found no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid is treated as the physical material volume of one 2AQ mount."
    - "Generic steel density is used because the part is a compact machine sensor bracket, similar M12 inductive-sensor mounts are commonly steel, and the local STEP material metadata does not resolve a real material."
  uncertainty_notes:
    - "If the mount is aluminum rather than steel, the same CAD volume would imply about 0.011 kg per unit; material uncertainty is therefore the main mass uncertainty."
material:
  primary_material: "unknown metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AQ_inductive_sensor_mount.step; https://www.damencnc.com/en/m12-inductive-sensor-mount-2-detection-plates/a3555"
    cited_fact_or_basis: "BOM row 93 names the part 2AQ_inductive_sensor_mount. Neighboring BOM rows place it with Balluff inductive sensors and M12x1 sensor nuts. The rendered preview shows a compact slotted bracket. Assembly STEP material extraction returned only material 'Allgemein' with density 1000.0, which is placeholder material evidence. A generic M12 inductive sensor mount vendor example uses steel, but it is not a row-specific 2AQ source. targeted_web_search: searched \"2AQ_inductive_sensor_mount material\", \"2AQ inductive_sensor_mount reAM250\", and \"inductive sensor mount material bracket\"; found no row-specific vendor, drawing, or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A metal/alloy family is selected because the part is a structural sensor bracket in a machine axis assembly and the CAD geometry shows a slotted mount rather than a printed sensor clip."
    - "The result stays at family level because neither BOM fields, STEP metadata, nor targeted web searches identify a specific alloy, grade, coating, or magnetic requirement."
  uncertainty_notes:
    - "The specific alloy, surface finish, and whether the actual material is carbon steel, stainless steel, aluminum, or another machinable metal are unresolved."
how_to_make:
  summary: "Make as a small custom metal bracket: machine or cut the L-shaped profile with the CAD-defined slots, deburr, finish, and install two copies for the inductive sensor positions."
  manufacturing_steps:
    - "Start from small metal bar, plate, or angle stock sized for the 30.00 x 30.00 x 25.00 mm bracket envelope."
    - "CNC mill, drill, slot, or waterjet/laser-cut and bend the bracket geometry to match the CAD-defined L shape and elongated mounting slots."
    - "Deburr the slots and external edges, then apply corrosion protection, passivation, or coating if required by the selected alloy and machine environment."
    - "Install two mounts in the end-switch assembly and align them with the neighboring Balluff M12 inductive sensors and sensor nuts."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AQ_inductive_sensor_mount.step; research/ream250_bom/ream250_bom_row_0093_2AQ__views_2x2.png; https://www.damencnc.com/en/m12-inductive-sensor-mount-2-detection-plates/a3555"
    cited_fact_or_basis: "The row STEP measures one 30.00 x 30.00 x 25.00 mm solid, and the rendered contact sheet shows an L-shaped bracket with two vertical slots and a rounded slot/opening. A generic M12 inductive sensor mount vendor page describes a steel mount set used for mounting cylindrical M12 sensors, but it is not row-specific to 2AQ. targeted_web_search: searched \"2AQ_inductive_sensor_mount material\", \"2AQ inductive_sensor_mount reAM250\", and \"inductive sensor mount material bracket\"; found no row-specific manufacturing-process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from the compact bracket envelope, slotted mounting features, and simple one-solid CAD geometry."
    - "Final fabrication should use the STEP/CAD file for exact slot dimensions, bend radii or corner relief, and tolerances; the preview is visual triage only."
  uncertainty_notes:
    - "The CAD preview does not establish whether the original was machined from solid, bent from sheet, cast, or 3D printed; machining/cut-and-bend are plausible low-volume routes for later KB modeling."
kb_implications:
  - "item_granularity: simple_part - compact custom sensor bracket with one dominant fabrication route and no row evidence for a sub-BOM."
---

CAD preview: `research/ream250_bom/ream250_bom_row_0093_2AQ__views_2x2.png`
