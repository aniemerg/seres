---
row_identity:
  item: "15"
  cad_file: "15_seal_door"
  source_row_number: 219
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.lisema.eu/Moosgummiprofile_Halbrund"
function:
  summary: "Compressible rectangular door seal for the reAM250 enclosure or chamber door; CAD shows one continuous rectangular gasket loop made from a narrow half-round/bulb sponge-rubber profile."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/15_seal_door.step; research/ream250_bom/ream250_bom_row_0219_15__views_2x2.png; https://lisema.eu/Moosgummiprofile_Halbrund"
    cited_fact_or_basis: "BOM row 219 states item 15, quantity 1, CAD file 15_seal_door, manufacturer Lisema, and the Lisema half-round sponge-profile URL. The manifest maps the row to gold_export/parts/15_seal_door.step as a matched vendor-component export. FreeCAD measured 1 solid with bounding box about 844.94 x 20.00 x 404.94 mm; the rendered contact sheet shows a thin rectangular gasket loop. The Lisema page is for NEOSOFT EPDM sponge half-round and hollow chamber standard profiles and lists 20 x 20 mm black half-round-profile stock matching the CAD profile thickness."
    evidence_basis: "bom_provided"
  assumptions:
    - "The filename seal_door and rectangular compressible-loop geometry are interpreted as a door perimeter seal rather than a structural frame."
  uncertainty_notes:
    - "The CAD/BOM evidence identifies the seal role and approximate envelope, but not the exact mating groove, compression percentage, adhesive layout, or required leak-rate specification."
mass:
  value_kg: 0.23
  basis: "FreeCAD volume 453695.042 mm^3 equals 453.695 cm^3 or 0.000453695 m^3 for one seal. Using a representative apparent density of 0.5 g/cm^3 (500 kg/m^3) for EPDM sponge rubber profiles gives 0.000453695 m^3 * 500 kg/m^3 = 0.2268 kg, rounded to 0.23 kg per unit. BOM quantity is 1, so the row total is also about 0.23 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/15_seal_door.step; https://lisema.eu/Moosgummiprofile_Halbrund; https://kremer-tec.de/en/products/rubber-profiles/epdm-profiles.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 453695.042 mm^3, area 133536.424 mm^2, and bounding box about 844.94 x 20.00 x 404.94 mm. The Lisema BOM route identifies the material family as EPDM sponge profile but does not state mass or density. Independent web search found Kremer's EPDM profile page, which states that EPDM sponge rubber cords and sponge rubber profiles commonly have density about 0.5 g/cm^3, lower than solid EPDM profiles due to cellular structure. bom_url_route_check: the BOM-provided Lisema URL was checked first and resolved material/profile dimensions but not row-specific density or weight, so the different-domain Kremer profile source was used only for the density constant."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The STEP solid volume is used as the apparent-volume proxy for one physical gasket loop."
    - "The independent EPDM sponge-profile density is treated as representative for the Lisema NEOSOFT EPDM sponge profile because Lisema does not publish row-specific density or weight on the BOM-provided page."
  uncertainty_notes:
    - "The mass is sensitive to foam density and profile hollowness; lower-density closed-cell EPDM sponge grades could make the real mass materially lower, while denser sponge grades could make it higher."
material:
  primary_material: "black EPDM sponge rubber profile with mixed open/closed cellular structure and closed outer skin"
  source:
    url_or_path: "https://lisema.eu/Moosgummiprofile_Halbrund; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Lisema BOM-provided route identifies NEOSOFT sponge-rubber half-round and hollow-chamber standard profiles made from black EPDM. The same page describes mixed cells with both closed and open pores and a protective closed outer skin, and gives hardness about 15-20 Shore A. The local assembly STEP material extractor matched 15_seal_door but returned only Generic material and density 1000.0, so STEP metadata did not resolve material."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Lisema identifies the material family and hardness range, but not the exact EPDM compound, filler package, density, adhesive backing, or batch-specific datasheet."
how_to_make:
  summary: "Procure or locally fabricate as a cut-to-length EPDM sponge half-round profile formed into a rectangular frame seal, with corners joined by adhesive bonding or vulcanized joining and the finished loop fitted to the door perimeter."
  manufacturing_steps:
    - "Select black EPDM sponge half-round or hollow-chamber profile stock matching the CAD cross section, approximately 20 mm profile thickness."
    - "Cut four profile lengths to the door perimeter dimensions with mitered or square ends as required by the corner-joint design."
    - "Join the corners by suitable rubber-profile adhesive bonding or vulcanized corner joining, then allow the joint to cure."
    - "Trim flash or excess adhesive and inspect continuity, corner alignment, and compression surface quality."
    - "Install on the door or mating groove with the specified adhesive or mechanical retention and verify uniform compression around the rectangular loop."
  source:
    url_or_path: "https://lisema.eu/Moosgummiprofile_Halbrund; https://kremer-tec.de/en/products/rubber-profiles/epdm-profiles.html; research/ream250_bom/ream250_bom_row_0219_15__views_2x2.png"
    cited_fact_or_basis: "Lisema identifies the BOM route as EPDM sponge half-round/hollow-chamber profiles and states bonding guidance for these profiles. Independent web search found Kremer's EPDM profile page, which states EPDM profiles can be supplied by the metre, as profile sections, bonded or impact-vulcanized rings, and corner-vulcanized frame seals. The CAD contact sheet shows the row-specific part as a rectangular loop seal. bom_url_route_check: the BOM-provided Lisema URL was checked first and resolved the product family and bonding note, but did not state whether this row was supplied as a cut profile, bonded loop, or vulcanized frame, so the different-domain Kremer source was used for the frame-seal delivery/manufacturing route."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The reAM250 row is treated as a finished gasket loop made from profile stock rather than a raw 5 m vendor coil, because the CAD export is a closed rectangular loop sized to the machine door."
    - "Local fabrication would reuse general rubber-profile cutting, bonding, and inspection tooling rather than requiring a dedicated special-purpose machine."
  uncertainty_notes:
    - "The sources support the profile and frame-seal route, but the row does not state whether Lisema supplied this exact seal as a bonded loop, a loose profile length cut during assembly, or a corner-vulcanized custom frame."
kb_implications:
  - "item_granularity: simple_part - door gasket/seal should later map to a reusable elastomer seal/profile replaceable or applied part rather than a machine-specific structural part; model size and material as variants of generic EPDM sponge seal stock where possible."
---

Research result for reAM250 BOM row 219.
