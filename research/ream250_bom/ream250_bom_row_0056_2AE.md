---
row_identity:
  item: "2AE"
  cad_file: "2AE_glass_scale_slide"
  source_row_number: 56
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.kuc-maschinen.de/produkt/linear-glasmassstaebe/"
function:
  summary: "K+C S5 glass-scale reader-head slide/carriage for the 520 mm measuring-range linear optical position measuring system; it carries or guides the read head so scale and machine-slide misalignment can be tolerated."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.kuc-maschinen.de/products/linear-glass-scales/?lang=en; research/ream250_bom/ream250_bom_row_0056_2AE__views_2x2.png"
    cited_fact_or_basis: "BOM row 56 identifies item 2AE as a K+C 'measuring range 520 mm: slide S5/0500 K+C glass scale S5'. K+C describes the linear optical position measuring system as a glass scale scanned by a reading head, and lists a reader head slide with five-fold ball bearing and spring to compensate misalignments between scale and machine slide. The CAD preview shows a compact 20.00 x 80.00 x 17.00 mm slide-like component."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM word 'slide' is interpreted as the K+C reader-head slide/carriage, not the full 642 mm glass scale assembly or the separate track row 2AF1."
  uncertainty_notes: []
mass:
  value_kg: 0.069
  basis: "FreeCAD measured one solid with volume 25625.159 mm^3, equal to 2.5625159e-5 m^3. Using the local aluminum density 2700 kg/m^3 gives 0.0692 kg per slide/carriage body, rounded to 0.069 kg for BOM quantity 1. If the full CAD volume were steel-like at 7850 kg/m^3, the same envelope would be about 0.201 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AE_glass_scale_slide.step; kb/materials/properties.yaml; https://www.kuc-maschinen.de/products/linear-glass-scales/?lang=en; https://www.top-maschinen.de/k-c-glasmassstab-s5-500-mm-5-m-verfahrweg-520-mm-812251.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 25625.159 mm^3, area 7357.281 mm^2, and bounding box 20.00 x 80.00 x 17.00 mm. The local density table lists aluminum at 2700 kg/m^3 and steel at 7850 kg/m^3. K+C states the system uses a robust aluminium housing and a reader head slide with five-fold ball bearing and spring. A same-product vendor page for K+C S5 500 mm / 520 mm gives whole-system shipping weight 3.1 kg but not a separate slide mass. targeted_web_search: searched \"K+C S5/0500 glass scale slide material weight\", \"K+C Glasmaßstab S5 Lesekopf Schlitten 5-fach Kugellagerung Federaufhängung\", and \"K+C S5/0500 Glasmaßstab Gewicht Aluminiumgehäuse\"; results resolved product family and whole-system details but no row-specific slide mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is treated as the per-unit physical volume of the slide body represented by row 2AE."
    - "The nominal mass uses an aluminum-body scenario because the official product family identifies aluminium housing construction and the CAD shows a compact carriage/slide body."
  uncertainty_notes:
    - "The STEP package material extractor returned only placeholder Generic material at density 1000.0, so material-specific mass is not directly resolved."
    - "Small steel bearing/spring elements and any sensor internals are not separated in the single-solid CAD model; the mass could approach the steel scenario if the row represents a mostly steel carriage."
material:
  primary_material: "mixed metal reader-head slide/carriage material family: aluminum body class with steel ball-bearing and spring hardware"
  source:
    url_or_path: "https://www.kuc-maschinen.de/products/linear-glass-scales/?lang=en; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "K+C states the glass-scale system has a robust aluminium housing, double sealing lips, and a reader head slide with five-fold ball bearing and spring. BOM row 56 names the item as the K+C S5/0500 glass-scale slide. Local assembly STEP material extraction for 2AE_glass_scale_slide returned only Generic material and density 1000.0, which does not resolve material. targeted_web_search: searched \"K+C S5/0500 glass scale slide material weight\", \"K+C Glasmaßstab S5 Lesekopf Schlitten 5-fach Kugellagerung Federaufhängung\", and \"K+C S5/0500 Glasmaßstab Gewicht Aluminiumgehäuse\"; no row-specific slide material grade was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The body is grouped with the official aluminium-housing construction while the named ball bearing and spring features are modeled as steel-family hardware."
  uncertainty_notes:
    - "The exact aluminum alloy, bearing steel grade, spring grade, seal material, and whether the CAD row includes any read-head electronics are not specified."
how_to_make:
  summary: "Procure as the K+C S5 glass-scale reader-head slide within the linear measuring system for current modeling; a plausible local route would make the small carriage body by precision machining, add bearing/spring hardware, then assemble and calibrate it with the optical glass scale and read head."
  manufacturing_steps:
    - "Procure or model as part of the K+C S5 linear glass-scale system matched to the S5/0500, 520 mm measuring-range row."
    - "For a local approximation, machine or extrude the compact carriage/body profile to the 20 x 80 x 17 mm CAD envelope and finish the bearing/guide features."
    - "Install precision ball-bearing and spring elements that let the reader head slide accommodate scale-to-machine-slide misalignment."
    - "Assemble with the optical read head, glass scale, seals, cable, and housing, then calibrate and verify the position signal."
  source:
    url_or_path: "https://www.kuc-maschinen.de/products/linear-glass-scales/?lang=en; research/ream250_bom/ream250_bom_row_0056_2AE__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AE_glass_scale_slide.step"
    cited_fact_or_basis: "K+C identifies the S5 glass-scale product family, aluminium protected construction, and reader-head slide with five-fold ball bearing and spring; the rendered CAD contact sheet shows a compact grooved slide/carriage with two end holes and a 20.00 x 80.00 x 17.00 mm bounding box. The detailed local fabrication and calibration route is inferred from the product function and CAD geometry rather than stated by K+C. targeted_web_search: searched \"K+C S5/0500 glass scale slide material weight\", \"K+C Glasmaßstab S5 Lesekopf Schlitten 5-fach Kugellagerung Federaufhängung\", and \"K+C S5/0500 Glasmaßstab Gewicht Aluminiumgehäuse\"; found product-family features and dimensions but no factory manufacturing process for the slide."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row is best treated as part of a calibrated optical measuring subsystem, even though the CAD export for this row is one compact mechanical slide component."
    - "A self-manufactured replacement would require optical/electrical calibration steps beyond ordinary metal part fabrication."
  uncertainty_notes:
    - "No source provides tolerances, bearing preload, spring force, optical read-head interface, or production process details for the slide."
kb_implications:
  - "item_granularity: purchased_module - Treat 2AE as the reader-head slide/carriage portion of a calibrated K+C glass-scale measuring subsystem for near-term KB modeling; split into simple body, bearings, spring, seals, and read-head electronics only if the linear encoder becomes a detailed manufacturing target."
---

# reAM250 BOM Row 56 - 2AE

Research result for the leased reAM250 BOM row.
