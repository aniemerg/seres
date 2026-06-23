---
row_identity:
  item: "2AC7"
  cad_file: "2AC7_part_7"
  source_row_number: 41
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small annular bearing retainer or cage-like ring within the lower SLA10 bottom-axis bearing group, used to locate rolling elements or retain bearing internals around the shaft bore."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC7_part_7.step; research/ream250_bom/ream250_bom_row_0041_2AC7__views_2x2.png; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127; https://www.smbbearings.com/firebrick/ckeditor/plugins/upload/Uploads/Documents/bearingpdfs/6200-2RS-bearing-10x32x9mm.pdf"
    cited_fact_or_basis: "BOM row 41 lists item 2AC7, quantity 1, CAD file 2AC7_part_7, description 'axis bearing bottom'. The manifest maps the row to a matched part STEP. FreeCAD measured one solid with volume 851.607 mm3 and bbox 22.74 x 6.84 x 22.74 mm; the rendered preview shows a short annular sleeve/ring with side openings. The related assembly name is 2AC0_bottom_axis_bearing_SLA10. HIWIN identifies SLA10 as a supported bearing using bearing type 6200.2RS, and SMB's 6200-2RS datasheet lists rings, balls, cage, seals, and grease as bearing elements. targeted_web_search: searched '2AC7 axis bearing bottom reAM250', '2AC7_part_7', 'SLA10 6200.2RS bearing cage material', and '6200-2RS bearing cage pressed steel'; results found duplicate BOM text and generic 6200-2RS bearing/cage data, but no row-specific drawing naming 2AC7."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row-level ring is interpreted as one internal retainer/cage-like bearing component because its annular form and side openings fit a rolling-bearing subpart better than a housing, ball, shaft, or seal."
  uncertainty_notes:
    - "The CAD file does not label the exact bearing subcomponent role, so the part could instead be a spacer, shield, or inner bearing ring in the lower axis-bearing group."
mass:
  value_kg: 0.00669
  basis: "Per-unit mass for quantity 1. FreeCAD measured volume 851.607 mm3, converted as 851.607e-9 m3. Using kb/materials/properties.yaml generic steel density 7850 kg/m3 gives 0.006685 kg, rounded to 0.00669 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC7_part_7.step; kb/materials/properties.yaml; https://www.smbbearings.com/firebrick/ckeditor/plugins/upload/Uploads/Documents/bearingpdfs/6200-2RS-bearing-10x32x9mm.pdf"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 851.607 mm3, area 1173.341 mm2, and bbox 22.74 x 6.84 x 22.74 mm. The local density table gives generic steel density as 7850 kg/m3. SMB's 6200-2RS datasheet lists cage material as pressed steel. targeted_web_search: searched '2AC7_part_7 weight', '2AC7 axis bearing bottom mass', '6200-2RS bearing cage weight', and '6200 bearing cage pressed steel'; no row-specific catalog mass or CAD material density was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The complete STEP solid is treated as one physical BOM item."
    - "Generic steel density is used as an effective density because the row is interpreted as a steel bearing cage/retainer-style component."
  uncertainty_notes:
    - "If the component is a polymer, brass, or thin stamped cage rather than solid steel-family material, the true mass could differ materially from the CAD-volume estimate."
material:
  primary_material: "probable steel-family bearing cage or retainer material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC7_part_7.step; https://www.smbbearings.com/firebrick/ckeditor/plugins/upload/Uploads/Documents/bearingpdfs/6200-2RS-bearing-10x32x9mm.pdf; https://www.skf.com/uk/products/rolling-bearings/ball-bearings/deep-groove-ball-bearings/productid-6200?failover=true"
    cited_fact_or_basis: "Local STEP material extraction for 2AC7_part_7 returned Generic with density 1000.0, which is placeholder metadata. The row STEP/preview shows a ring-like internal bearing subcomponent. SMB's 6200-2RS datasheet lists cage material as pressed steel; SKF's 6200 page lists bearing material as bearing steel and cage as sheet metal. targeted_web_search: searched '2AC7_part_7 material', '2AC7 axis bearing bottom material', '6200-2RS cage material pressed steel', and '6200 bearing cage material sheet metal'; no row-specific material grade or drawing was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local CAD geometry is mapped to a 6200-family bearing cage/retainer component within the SLA10 lower bearing assembly."
  uncertainty_notes:
    - "No row-specific material metadata, drawing, or supplier line item confirms the alloy or whether this exact subpart is a cage, spacer, shield, or ring."
how_to_make:
  summary: "Near-term route is to procure the complete SLA10/6200-2RS bearing unit or the bearing subcomponent; a plausible local route is stamped or machined thin steel ring/cage fabrication followed by deburring, heat treatment or finishing if required, and assembly into the bearing."
  manufacturing_steps:
    - "For current modeling, procure as part of a standard SLA10 supported bearing or 6200-2RS replacement bearing."
    - "For local manufacture, blank or turn the annular ring from steel-family stock to the measured outer diameter, bore, and width."
    - "Machine, punch, or broach the side openings/pockets, then deburr and finish contact edges."
    - "Clean, inspect concentricity and pocket geometry, then assemble with balls/races/seals and grease in the bottom-axis bearing."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0041_2AC7__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC7_part_7.step; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127; https://www.smbbearings.com/firebrick/ckeditor/plugins/upload/Uploads/Documents/bearingpdfs/6200-2RS-bearing-10x32x9mm.pdf"
    cited_fact_or_basis: "The CAD preview shows an annular ring with side openings. HIWIN identifies the matched SLA10 supported bearing and its 6200.2RS bearing type. SMB identifies 6200-2RS as a radial ball bearing with pressed-steel cage, SAE52100 chrome-steel rings and balls, rubber contact seals, and grease. The detailed local operations are inferred from the geometry and bearing-cage style rather than stated by a row-specific manufacturing source. targeted_web_search: searched '2AC7_part_7 manufacturing', '6200 bearing cage manufacturing pressed steel', 'bearing cage manufacturing punching deburring', and 'SLA10 bearing manufacturing process'; no reAM250 row-specific manufacturing route was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The ring is modeled as a simple precision bearing subpart rather than as a separately calibrated module."
  uncertainty_notes:
    - "If later evidence identifies this as a molded polymer cage, elastomer seal, or hardened race ring, the manufacturing route should change accordingly."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable small bearing cage/retainer or spacer-ring style component within a standard 6200/SLA10 bearing, not as a complete purchased bearing module."
---

# reAM250 BOM Row 41 - 2AC7
