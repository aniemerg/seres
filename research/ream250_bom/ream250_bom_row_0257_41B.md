---
row_identity:
  item: "41B"
  cad_file: "41B_timing_belt_340x10"
  source_row_number: 257
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Endless AT5 synchronous timing belt for positive, non-slip power transmission or shaft synchronization in the powder supply/inlet mechanism."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/41B_timing_belt_340x10.step; https://www.tyma.eu/products/10-at5-340-gen-iii-conti-synchroflex/"
    cited_fact_or_basis: "BOM row 257 identifies item 41B as 10-AT5-340 from zahriemen24.de; the STEP preview shows an endless toothed belt; the TYMA exact 10 AT5-340 listing describes the item as an AT5 timing belt for power transmission."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The BOM product identifier 10-AT5-340 is treated as the same AT5, 10 mm wide, 340 mm pitch-length belt family represented by the exact catalog designation 10 AT5-340."
  uncertainty_notes:
    - "The source row does not state the driven pulleys or exact reAM250 axis, so the function is limited to the belt-level drive role rather than a named machine motion axis."
mass:
  value_kg: 0.014
  basis: "Per physical belt. Quantity is 1, so row total is also about 0.014 kg. TYMA lists 0.014 kg for 10 AT5-340. FreeCAD measured the row STEP as one solid with volume 8451.406 mm^3 and bounding box 142.16 x 56.21 x 10.00 mm; multiplying that CAD volume by the local assembly STEP material density of 930 kg/m^3 gives about 0.00786 kg, used as a lower supporting check rather than the selected estimate."
  source:
    url_or_path: "https://www.tyma.eu/products/10-at5-340-gen-iii-conti-synchroflex/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/41B_timing_belt_340x10.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "TYMA lists weight 0.014 kg for 10 AT5-340; FreeCAD measured CAD volume 8451.406 mm^3; local STEP material extraction for 41B_timing_belt_340x10 reports Rubber at density 930 kg/m^3."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The catalog 10 AT5-340 mass is used as the best per-unit estimate because it captures belt construction that the simplified CAD volume may not fully represent."
  uncertainty_notes:
    - "Catalog and CAD-derived masses differ by about 1.8x, likely from simplified CAD geometry, material-density simplification, or reinforced-cord construction not represented as separate CAD material regions."
material:
  primary_material: "polyurethane timing belt body/teeth/backing with steel tensile cord reinforcement"
  source:
    url_or_path: "https://www.tyma.eu/products/10-at5-340-gen-iii-conti-synchroflex/; https://maedlernorthamerica.com/partshop/polyurethane-timing-belt-at5-width-10mm-lw-340mm-68-teeth-10-at5-340-pn-16660600/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "TYMA describes 10 AT5-340 as polyurethane with steel tensile fiber and construction of polyurethane teeth, steel cord tension member, and polyurethane backing. Maedler's exact 10 AT5/340 page states cast polyurethane with steel tensile member. Local STEP material extraction reports Rubber, which supports an elastomeric belt body but is less specific."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Polyurethane with steel tensile cord is selected over the broad local STEP material label Rubber because two exact-designation catalog sources resolve the belt construction more specifically."
  uncertainty_notes:
    - "The exact belt vendor in the BOM is zahriemen24.de, while the material construction comes from equivalent exact-designation AT5 catalog listings rather than a row-provided product URL."
how_to_make:
  summary: "Local manufacture, model it as a molded or cast polyurethane synchronous belt with embedded steel tensile cords"
  manufacturing_steps:
    - "Specify AT5 profile, 340 mm pitch length, 68 teeth, and 10 mm width."
    - "Inspect belt width, tooth count/pitch, and fit on matching AT5 pulleys before installation."
    - "If modeled locally later, use a dedicated timing-belt molding/casting route with continuous tensile cord placement and tooth-form tooling."
  source:
    url_or_path: "https://www.tyma.eu/products/10-at5-340-gen-iii-conti-synchroflex/; https://megadynegroup.com/files/resources/attachments/md_manu_en_megapower_web.pdf"
    cited_fact_or_basis: "TYMA provides the exact standard purchasable designation and dimensions. Megadyne's timing-belt catalog describes polyurethane timing belts as manufactured by a molding process with helically wound cords inside the belt body."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The generalized from polyurethane timing-belt manufacturing literature, not from a reAM250-specific production plan."
  uncertainty_notes:
    - "Targeted_web_search: searched 'site:zahriemen24.de \"10-AT5-340\"', '\"10-AT5-340\" \"zahriemen24\"', and '\"10 AT5 340\" \"zahriemen24\"'; no row-specific zahriemen24 product page was found, so The manufacturing route remains a general timing-belt hypothesis."
kb_implications:
  - "item_granularity: simple_part - Treat as a replaceable standard timing belt/wear item, not as a custom machine assembly; later KB work should reuse a generic AT5 timing belt family with length/width parameters where possible."
---

