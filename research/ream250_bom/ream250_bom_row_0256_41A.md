---
row_identity:
  item: "41A"
  cad_file: "41A_belt_pulley_D12-575390"
  source_row_number: 256
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "AT5 toothed belt pulley for the reAM250 powder-inlet drivetrain, with a 12 mm H7 shaft bore, keyway/groove, and set-screw/threaded-hole retention feature."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.fecconsulting.dk/tandremskiver/tandremskiver-at5-for-udboring/rembredde-10mm-at5/tandremskive-21-at5-30.html"
    cited_fact_or_basis: "BOM row 256 identifies item 41A as quantity 1 of 41A_belt_pulley_D12-575390, described as a belt pulley with 12 mm H7 bore, groove, and threaded hole on the groove. The manifest keeps it in the 410_powder_inlet assembly. The row-matched 21 AT5 30-2 catalog page identifies the product as a 30-tooth AT5 timing pulley for 10 mm belt width and industrial power transmission/synchronization applications."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The BOM row's D12/H7 bore, groove, and threaded-hole wording is interpreted as a customized bore/keyway/set-screw version of the standard 21 AT5/30-2 pulley family."
  uncertainty_notes:
    - "The local CAD export is assembly_only for this row; the individual pulley was named in the raw STEP but not exposed as a separate FreeCAD object, so function is based on BOM identity plus catalog family rather than isolated pulley CAD inspection."
mass:
  value_kg: 0.075
  basis: "Per-unit mass for quantity 1. The matched 21 AT5 30-2 catalog page lists weight as 75.00 g, so mass.value_kg is 0.075 kg. The D12/H7 bore, groove, and threaded-hole customization may shift the final mass slightly, but the row quantity remains one physical pulley."
  source:
    url_or_path: "https://www.fecconsulting.dk/tandremskiver/tandremskiver-at5-for-udboring/rembredde-10mm-at5/tandremskive-21-at5-30.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/410_powder_inlet.step"
    cited_fact_or_basis: "The 21 AT5 30-2 catalog page lists Produktnummer AL-21-AT5-30-2, width 21.00 mm, weight 75.00 g, and selectable Ø12 mm/H7 boring. FreeCAD measured the retained parent assembly STEP as 91 solids with volume 7316733.187 mm^3 and bounding box 609.50 x 282.00 x 626.20 mm, confirming the CAD is not an isolated per-pulley mass source."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The catalog mass is used as the best per-unit mass proxy for the customized BOM row because the individual pulley STEP could not be isolated."
  uncertainty_notes:
    - "Catalog weight may be for the base pulley before exact bore/keyway/set-screw machining; the likely difference is small relative to BOM planning precision."
material:
  primary_material: "Aluminum 6082 T6 body with zinc-plated steel flanges"
  source:
    url_or_path: "https://www.fecconsulting.dk/tandremskiver/tandremskiver-at5-for-udboring/rembredde-10mm-at5/tandremskive-21-at5-30.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The 21 AT5 30-2 catalog page states Materiale: Aluminium 6082 T6 UNI 9006-4 and Flange Materiale: Zinc plated steel. Local assembly STEP material extraction for 41A_belt_pulley_D12-575390 returned only material 'Generic' with density 1000.0, which is placeholder metadata."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's zahriemen24.de/manufacturer reference and 575390 product clue are treated as pointing to the same standard 21 AT5/30-2 pulley family represented by the independently found catalog page."
  uncertainty_notes:
    - "The exact supplier page from zahriemen24.de was not available in the local BOM link fields, so the material is row-family matched rather than confirmed from the original BOM vendor route."
how_to_make:
  summary: "Procure as a standard 21 AT5/30-2 aluminum timing pulley and customize the bore/keyway/set-screw features, or locally machine it from aluminum round stock with installed steel flanges."
  manufacturing_steps:
    - "Start from Aluminum 6082 T6 round bar or a near-net timing-pulley blank sized for 30 AT5 teeth, 21 mm total width, and about 51 mm flange diameter."
    - "Turn the hub, faces, bore pilot, and outside diameters on a lathe."
    - "Generate the AT5 tooth profile around the pulley rim by hobbing, form milling, or equivalent indexing cutter operation."
    - "Bore and ream the shaft hole to 12 mm H7, then cut the keyway/groove."
    - "Drill and tap the hub for the set-screw/threaded-hole retention feature, install zinc-plated steel flanges if not integral, deburr, and inspect concentricity and belt fit."
  source:
    url_or_path: "https://www.fecconsulting.dk/tandremskiver/tandremskiver-at5-for-udboring/rembredde-10mm-at5/tandremskive-21-at5-30.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "The catalog page identifies 21 AT5 30-2 as a standard aluminum timing pulley for later boring, with selectable Ø12 mm/H7 bore, pinolskruer/set-screws, and notgang/keyway options; BOM row 256 specifically requires a 12 mm H7 bore with groove and threaded hole on the groove. targeted_web_search: tried 'zahriemen24 575390 D12 belt pulley 12 mm H7 bore groove threaded hole', '\"575390\" \"AT5/30-2\"', '\"21 AT5/30-2\" \"575390\"', and '\"Tandremskive 21 AT5 30-2\"'; searches found matching vendor/catalog family data but no row-specific manufacturing-process specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local route is inferred from common timing-pulley geometry and the catalog's selectable boring/keyway/set-screw customization options."
    - "For KB planning, procurement of the standard pulley blank plus local bore/keyway/set-screw customization is more realistic than fully manufacturing the tooth profile unless timing pulleys become a major dependency."
  uncertainty_notes:
    - "No source states the actual zahriemen24.de or upstream factory manufacturing process for this exact row; tooth profile tolerances, balancing requirements, and flange attachment method remain unresolved."
kb_implications:
  - "item_granularity: simple_part - Model as reusable AT5 timing-pulley hardware with configurable bore/keyway/set-screw features rather than as a reAM250-specific purchased module."
---

Research result for the leased reAM250 BOM row only.
