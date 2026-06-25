---
row_identity:
  item: "70"
  cad_file: "70_dummy_laser_beam_source"
  source_row_number: 276
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://static1.squarespace.com/static/628d22a4cced8544470496fe/t/654533e22ca7ac1dafd952e0/1699034082388/nLIGHT_AFX_Series_Product_Sheet_30AUG2023+version+1.pdf"
function:
  summary: "Programmable nLIGHT AFX-1000 fiber laser source for the reAM250 optical train, providing switchable single-mode/ring beam output for laser powder-bed fusion exposure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/70_dummy_laser_beam_source.step; https://static1.squarespace.com/static/67bc98f2403e741e30757770/t/67c7851c2162180ca00deaac/1741128989380/nLIGHT%2BAFX%2BSeries%2BProduct%2BSheet.pdf"
    cited_fact_or_basis: "BOM row 276 names item 70 as 70_dummy_laser_beam_source, product AFX - 1000 by nLight. The current nLIGHT AFX Series product sheet lists AFX-1000 as a CW/modulated fiber laser with programmable beam quality, 1070 nm wavelength, 200-240 VAC supply, RS-232/Ethernet control, and water cooling. CAD preview shows one rectangular enclosed module matching a rack/benchtop laser source placeholder. official_alternate_route_check: original BOM Squarespace PDF URL returned 404; the cited current Squarespace PDF is an nLIGHT AFX Series Product Sheet, same manufacturer and AFX-1000 product family, and resolves the same row product identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM's 'dummy' CAD label is treated as a simplified CAD representation of the real AFX-1000 laser source rather than a nonfunctional placeholder item."
  uncertainty_notes:
    - "The supplied CAD does not expose optical ports, fiber routing, or service features, so function is primarily resolved from the BOM product identity and nLIGHT product sheet."
mass:
  value_kg: 45.0
  basis: "Per unit for BOM quantity 1. FreeCAD measured the supplied CAD as 1 solid, volume 44,721,356.934 mm3, surface area 895,469.918 mm2, and bounding box 660.00 x 164.90 x 430.30 mm. The nLIGHT product sheet gives a similar module envelope of 480 x 677 x 177 mm but no weight. A planning mass of 45 kg uses the CAD volume as a simplified occupied module volume with an effective module density near 1000 kg/m3, appropriate only as a coarse subsystem estimate."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/70_dummy_laser_beam_source.step; https://static1.squarespace.com/static/67bc98f2403e741e30757770/t/67c7851c2162180ca00deaac/1741128989380/nLIGHT%2BAFX%2BSeries%2BProduct%2BSheet.pdf"
    cited_fact_or_basis: "FreeCAD measured the row STEP geometry; the nLIGHT product sheet states the AFX-1000 mechanical dimensions but does not state weight. targeted_web_search: queries tried: 'AFX-1000 Weight kg nLIGHT', 'nLIGHT AFX-1000 kg Weight', 'AFX-1000 Mass nLIGHT', and 'AFX-1000 480 x 677 x 177 weight'; no row-specific vendor mass was found, only dimensions and system-level AM machine weights."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The simplified CAD solid is used as an occupied-envelope proxy, not literal solid material."
    - "Effective module density of about 1000 kg/m3 is used for a mixed rackmount laser subsystem with enclosure, optics, electronics, cooling hardware, and internal voids."
  uncertainty_notes:
    - "True mass may differ substantially because vendor weight, internal packaging, pump diode count, power electronics mass, and cooling hardware allocation were not available."
material:
  primary_material: "multi-material laser subsystem with metal enclosure, optical fiber, power/control electronics, optical components, and water-cooling interfaces"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://static1.squarespace.com/static/67bc98f2403e741e30757770/t/67c7851c2162180ca00deaac/1741128989380/nLIGHT%2BAFX%2BSeries%2BProduct%2BSheet.pdf"
    cited_fact_or_basis: "Local STEP material extraction for 70_dummy_laser_beam_source returned only Generic with density 1000.0, which is non-resolving. The nLIGHT product sheet states a fiber laser with optical fiber, 200-240 VAC electrical supply, RS-232/Ethernet control, water cooling, and Class 4 laser output, but does not list construction materials. targeted_web_search: queries tried: 'nLIGHT AFX-1000 material datasheet', 'AFX-1000 laser source enclosure material', and 'nLIGHT AFX Series Product Sheet material'; no row-specific material breakdown was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Material is kept at subsystem/component-family level because no source states enclosure alloy, fiber composition, optics materials, circuit materials, or cooling wetted materials."
  uncertainty_notes:
    - "Do not model this row as a single homogeneous material; later KB work needs a sub-BOM or vendor teardown before assigning material masses."
how_to_make:
  summary: "Treat as a purchased/calibrated laser module for current KB planning; local self-manufacture would require a separate subsystem model for pump diodes, doped fiber, beam-shaping fiber architecture, electronics, cooling, enclosure, firmware, and optical calibration."
  manufacturing_steps:
    - "Procure or import the nLIGHT AFX-1000 laser source as a qualified vendor subsystem."
    - "Mount the enclosed module in the reAM250 frame, connect AC power, cooling water, control interfaces, safety interlocks, and the QBH/process fiber path."
    - "Perform OEM integration, beam-profile control setup, water-cooling checks, and laser safety validation before process use."
    - "For future local manufacturing research, decompose into optical fiber/pump laser, power electronics, cooling, enclosure, control, and calibration work packages."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://static1.squarespace.com/static/67bc98f2403e741e30757770/t/67c7851c2162180ca00deaac/1741128989380/nLIGHT%2BAFX%2BSeries%2BProduct%2BSheet.pdf"
    cited_fact_or_basis: "BOM row identifies a vendor nLight AFX-1000 item. The nLIGHT product sheet states the AFX fiber laser family, AFX-1000 model, 200-240 VAC supply, RS-232/Ethernet control, water cooling, optical fiber with QBH connector, and Class 4 laser product warning. targeted_web_search: queries tried: 'nLIGHT AFX-1000 manufacturing process', 'AFX-1000 fiber laser teardown', and 'nLIGHT AFX-1000 service manual'; no public sub-BOM or manufacturing route was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The immediate route is procurement/integration because the row is a calibrated commercial laser source and no public manufacturing recipe or sub-BOM was found."
  uncertainty_notes:
    - "Detailed local manufacture is unresolved beyond high-level subsystem decomposition and would require protected vendor design information or dedicated reverse engineering."
kb_implications:
  - "item_granularity: complex_module - model this row as a functional/calibrated laser subsystem for this pass; split into a sub-BOM only when laser-source replication becomes an explicit modeling target."
---
