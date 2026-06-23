---
row_identity:
  item: "1B41"
  cad_file: "1B41_glas"
  source_row_number: 12
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Flat laser-protective viewing glass/window panel for the reAM250 door or optical access assembly; it provides a transparent barrier while preserving laser safety around the process chamber."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B41_glas.step; https://www.uvex-group.com/en/brands/laservision/"
    cited_fact_or_basis: "BOM row 12 identifies item 1B41 as quantity 1, CAD file 1B41_glas, manufacturer Laservision. CAD measures a single flat 210.00 x 297.00 x 3.20 mm panel. Laservision/uvex describes laservision as a maker of laser safety eyewear, filters, windows, and large-area protection systems."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The German/CSV term 'glas' and the Laservision manufacturer assignment indicate a protective glass window/filter rather than an ordinary structural cover plate."
    - "Adjacent BOM items 1B42_seal and 1B43_frame imply this glass is installed as a sealed framed window."
  uncertainty_notes:
    - "The BOM row has no product ID or link URL, so the exact Laservision filter family and certified wavelength/OD rating were not resolved."
    - "targeted_web_search: searched 'Laservision 1B41 glass 210 297 3.2', '1B41 Laservision', '1B41 laser safety Laservision', and '1B41_glas'; no row-specific catalog page was found."
mass:
  value_kg: 0.499
  basis: "Per-unit mass for quantity 1. FreeCAD volume is 199584.000 mm^3 = 0.000199584 m^3. Using the local kb/materials/properties.yaml generic glass density of 2500 kg/m^3 gives 0.49896 kg, rounded to 0.499 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B41_glas.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 199584.000 mm^3, area 127984.800 mm^2, bounding box 210.00 x 297.00 x 3.20 mm. Local density table lists generic glass at 2500 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid represents the full physical glass panel with no omitted frame, coating, adhesive, or film mass."
    - "Generic glass density is close enough for planning because the exact Laservision filter glass composition is unknown."
  uncertainty_notes:
    - "Assembly STEP material extraction returned only placeholder material 'Generic' with density 1000.0, so it was not used."
    - "If this is a laminated or coated laser safety filter, true mass may differ from the monolithic generic-glass estimate."
material:
  primary_material: "laser-protective mineral/safety glass panel; exact filter grade and coating/lamination stack unknown"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://lasersafety.com/eyewear/glass/; https://www.uvex-group.com/en/brands/laservision/"
    cited_fact_or_basis: "BOM row name is 1B41_glas and manufacturer is Laservision. Laservision USA describes absorbing glass laser safety filters made from large uncut sheets polished to required thickness, with tempered-glass splinter protection. uvex/Laservision describes laser safety windows using glass, PMMA, or PC and mentions glass composite manufacturing."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Because the row explicitly says 'glas', model the primary material as glass rather than PMMA or polycarbonate."
    - "Treat any protective coating, absorber chemistry, or lamination as part of the purchased/specialty glass panel until a row-specific product number is available."
  uncertainty_notes:
    - "No row-specific Laservision filter code, OD rating, wavelength band, glass chemistry, or lamination stack was present in the BOM, CAD metadata, or targeted web search."
    - "targeted_web_search: searched 'Laservision 1B41 glass material', '1B41 Laservision filter', and 'Laservision 1B41_glas'; results only confirmed the BOM row or general Laservision glass-filter product family."
how_to_make:
  summary: "Procure as a certified Laservision laser-safety glass/window filter cut to the CAD envelope, or manufacture later by producing a specialty absorbing/laminated safety glass sheet, polishing it to thickness, cutting to approximately A4 size, edging it, adding any required splinter-protection or coatings, and certifying optical density for the machine laser wavelengths."
  manufacturing_steps:
    - "Select the required laser wavelength and OD rating from the machine hazard analysis."
    - "Procure or make the appropriate absorbing laser-safety glass/filter blank."
    - "Polish or grind to the required 3.20 mm thickness if not supplied at final thickness."
    - "Cut/waterjet/CNC edge the rectangular 210.00 x 297.00 mm panel and deburr or polish edges."
    - "Apply any required splinter-protection, lamination, or coating stack and verify optical transmission and OD rating before installation."
  source:
    url_or_path: "https://lasersafety.com/eyewear/glass/; https://www.uvex-group.com/en/brands/laservision/"
    cited_fact_or_basis: "Laservision USA says absorbing glass filters start as large uncut/unpolished sheets that are polished to required thickness and edged; uvex/Laservision describes glass-composite manufacturing, waterjet cutting, CNC milling, and automatic bonding for laser safety windows."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "For near-term KB modeling, procurement is the realistic route because certified laser OD performance is a safety-critical specialty property."
    - "A future local route would need optical glass/filter chemistry and certification steps, not only generic glass cutting."
  uncertainty_notes:
    - "The BOM row does not state the laser wavelength or OD rating, so the manufacturing route cannot specify the absorber composition or certification target."
kb_implications:
  - "item_granularity: purchased_module - Model 1B41 as one purchased/certified laser-safety glass window panel rather than generic glass stock, because safety certification and wavelength-specific optical density dominate substitutability."
---
