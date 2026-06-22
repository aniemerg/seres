---
row_identity:
  item: "41D"
  cad_file: "41D_belt_pulley_D7-575457"
  source_row_number: 259
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small flanged AT5 toothed timing-belt pulley for the reAM250 powder-inlet drivetrain, finish-bored 7 mm H7 so it can mount to a shaft and transmit synchronous belt motion without slip."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.lenze-selection.com/en-at/products/belt-drives; https://www.optibelt.com/fileadmin/pdf/produkte/scheiben/optibelt-timing-belt-pulleys.pdf"
    cited_fact_or_basis: "BOM row 259 identifies item 41D as quantity 2, CAD file 41D_belt_pulley_D7-575457, manufacturer zahriemen24.de, and description 'Toothed belt pulley 21 AT5/18-2 with 7 mm H7 bore'. The manifest maps the row to the 410_powder_inlet assembly context with cad_export_status assembly_only. Lenze describes toothed belt drives as synchronous, slip-free power transmission, and the Optibelt timing-pulley table lists the exact 21 AT5 / 18-2 pulley designation."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row belongs to the powder-inlet drivetrain because the manifest retained it in the 410_powder_inlet assembly context."
    - "The 7 mm H7 bore is interpreted as the shaft interface for one physical pulley."
  uncertainty_notes:
    - "The row-level STEP export is assembly_only, so the exact mating shaft, belt path, and installed orientation are inferred from the BOM identity and parent assembly rather than isolated part geometry."
mass:
  value_kg: 0.031
  basis: "Per-unit estimate for one pulley. The exact standard catalog line 21 AT5 / 18-2 is listed at about 0.031 kg. BOM quantity is 2, so the row total is about 0.062 kg before any small mass change from the 7 mm H7 finished bore. Parent assembly FreeCAD geometry is not used for mass because it measured the whole 410_powder_inlet assembly context: 91 solids, volume 7316733.187 mm^3, area 2248637.223 mm^2, bounding box 609.50 x 282.00 x 626.20 mm."
  source:
    url_or_path: "https://www.optibelt.com/fileadmin/pdf/produkte/scheiben/optibelt-timing-belt-pulleys.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/410_powder_inlet.step"
    cited_fact_or_basis: "Optibelt's metric timing-belt-pulley table lists 21 AT5 / 18-2 with material AL, 18 teeth, type 6F, pitch diameter 28.65 mm, outside diameter 27.40 mm, flange diameter 32 mm, F 15 mm, L 21 mm, Dm 20 mm, maximum finished bore 12 mm, and weight about 0.031 kg. FreeCAD measured only the parent assembly because the row export status is assembly_only."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The Optibelt 21 AT5 / 18-2 catalog mass is used as the closest supported per-unit mass for the same standard pulley designation."
    - "The custom 7 mm H7 bore is within the catalog's 12 mm maximum finished bore and is treated as a small machining change that does not materially change the catalog mass at this precision."
  uncertainty_notes:
    - "The exact Zahriemen24 part number 575457 was not resolved to a live row-specific datasheet, and the local CAD export does not isolate the pulley volume."
material:
  primary_material: "aluminum timing-pulley body, exact alloy not specified"
  source:
    url_or_path: "https://www.optibelt.com/fileadmin/pdf/produkte/scheiben/optibelt-timing-belt-pulleys.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Optibelt's exact 21 AT5 / 18-2 standard pulley line lists material 'AL'. The local assembly STEP material extractor matched 41D_belt_pulley_D7-575457 but returned only material Generic and density 1000.0, which the task acceptance criteria treats as placeholder rather than resolved material evidence."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The catalog abbreviation AL is interpreted as aluminum/aluminum alloy for the pulley body."
    - "The row-specific 7 mm H7 bore does not imply a different body material from the standard 21 AT5 / 18-2 pulley."
  uncertainty_notes:
    - "No source identified the exact aluminum alloy, surface treatment, or whether the supplied pulley includes any separate steel retaining hardware."
how_to_make:
  summary: "Procure or manufacture as a standard 21 AT5/18-2 aluminum timing pulley, then finish-bore or verify the 7 mm H7 bore for the reAM250 shaft interface."
  manufacturing_steps:
    - "Start from an aluminum AT5 pulley blank or standard 21 AT5/18-2 pulley body with two flanges."
    - "Generate or finish the AT5 tooth profile and flange geometry by pulley hobbing/form cutting or equivalent CNC turning and milling operations."
    - "Finish-bore the hub to 7 mm H7 while keeping the bore concentric with the tooth pitch diameter."
    - "Deburr, clean, and inspect bore tolerance, runout, tooth profile, and belt fit before installation."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.lenze-selection.com/en-at/products/belt-drives/toothed-belt-pulleys-and-clamping-plates-and-taper-bushes; https://www.optibelt.com/fileadmin/pdf/produkte/scheiben/optibelt-timing-belt-pulleys.pdf"
    cited_fact_or_basis: "BOM row 259 states the custom 7 mm H7 bore requirement. Lenze states that belt pulleys can be made according to drawing with special drilled holes, special tolerances, different surface treatments, different materials, and single-piece or large-series production. Optibelt gives the base 21 AT5 / 18-2 pulley geometry, aluminum material, maximum finished bore, and catalog mass. targeted_web_search: searched 'zahriemen24 21 AT5/18-2 toothed belt pulley 7 mm H7 575457', 'site:zahriemen24.de 575457', 'site:zahriemen24.de 21 AT5/18-2', and '21 AT5/18-2 7 mm H7'; found duplicate BOM text and standard pulley catalog matches, but no row-specific manufacturing drawing for the exact Zahriemen24 575457 modification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A purchased standard pulley plus secondary bore finishing or vendor-supplied bore customization is the most plausible route because the BOM names a standard pulley designation plus a custom H7 bore."
    - "If manufactured locally from stock instead of procured, the same operations can be modeled as aluminum blank turning, tooth/flange machining, bore finishing, deburring, and inspection."
  uncertainty_notes:
    - "The exact surface finish, balance grade, tooth-tolerance class, and vendor modification drawing are not present in the BOM row or resolved catalog evidence."
kb_implications:
  - "item_granularity: simple_part - standard aluminum timing pulley with row-specific finish bore; model as reusable pulley hardware rather than a calibrated purchased subsystem."
---

Research result for reAM250 BOM row 259.
