---
row_identity:
  item: 2APF
  cad_file: 2APF_shim_disk
  source_row_number: 85
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Thin annular shim disk used as a spacer or tolerance-compensation washer, most plausibly to set axial clearance or stack height around a small shaft or fastener in the adjacent 2AP assembly.
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APF_shim_disk.step; https://www.metricmcc.com/precision-shim-ring"
    cited_fact_or_basis: "BOM row 85 names the item 2APF_shim_disk with quantity 4. FreeCAD measured one solid with bounding box about 13.00 x 1.00 x 13.00 mm and volume 94.248 mm^3; the rendered preview shows a thin annular washer. Metric DIN 988 shim rings are a standard washer family used to limit excess space and axial movement; the CAD-derived 7 mm ID, 13 mm OD, 1 mm thickness gives complete standard-family dimensions for the functional interpretation."
    evidence_basis: standard_part_convention
  assumptions:
    - The shim is used for spacing or axial-clearance adjustment because the BOM provides no parent subassembly note beyond the adjacent 2AP rows.
  uncertainty_notes:
    - The exact installed interface is not identified in the row context, so the function is assigned at the shim-washer level rather than to a specific shaft or bearing.
mass:
  value_kg: 0.00074
  basis: "Per physical shim disk. FreeCAD volume is 94.248 mm^3 = 9.4248e-8 m^3. Using local kb/materials/properties.yaml generic steel density of 7850 kg/m^3 gives 0.0007398 kg, rounded to 0.00074 kg per unit. BOM quantity is 4, so the row total is about 0.00296 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APF_shim_disk.step; kb/materials/properties.yaml; https://shop.arvidnilsson.com/en/bolts-nuts-washers-36374/washers/shims/shim-washer-din-988.html?p=2"
    cited_fact_or_basis: "FreeCAD measured volume 94.248 mm^3 for one CAD solid. The Arvid Nilsson DIN 988 listing includes the complete matching standard designation D988-T.1 St 7 (7x13x1), supporting steel shim-washer convention for this size. Local material properties list steel density as 7850 kg/m^3."
    evidence_basis: standard_part_convention
  assumptions:
    - The shim is treated as steel because the measured 7 x 13 x 1 mm geometry matches a DIN 988 steel shim-washer size and no row-specific material metadata is available.
  uncertainty_notes:
    - Assembly STEP material extraction returned only Generic with density 1000 kg/m^3, which is placeholder metadata and was not used for mass.
    - If the actual part is stainless steel rather than generic steel, the per-unit mass would remain close, about 0.00075 kg using 8000 kg/m^3.
material:
  primary_material: steel shim washer material; exact grade unspecified for the BOM row
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APF_shim_disk.step; https://shop.arvidnilsson.com/en/bolts-nuts-washers-36374/washers/shims/shim-washer-din-988.html?p=2; https://www.aspenfasteners.com/content/pdf/Metric_DIN_988_spec.pdf"
    cited_fact_or_basis: "The CAD geometry resolves to the complete DIN 988-style dimensions 7 mm ID, 13 mm OD, and 1 mm thickness. The Arvid Nilsson shim-washer catalog lists D988-T.1 St 7 (7x13x1), and the Aspen DIN 988 specification covers steel metric DIN 988 shim washers and stainless steel classes; this supports steel-family material but not a row-specific grade."
    evidence_basis: standard_part_convention
  assumptions:
    - Use steel-family material for KB planning because the row name and CAD match standard shim washer practice and no manufacturer or material field is provided.
  uncertainty_notes:
    - The BOM row has no manufacturer, product ID, material hint, or Link URL, so the exact grade, heat treatment, and coating remain unspecified.
    - "targeted_web_search: queries tried: '2APF shim disk', '2APF_shim_disk', 'reAM250 2APF shim disk', 'DIN 988 7x13x1 shim ring material'; results found the BOM row repeated and standard DIN 988 shim references, but no row-specific material source."
how_to_make:
  summary: "Prepare as a standard 7 x 13 x 1 mm shim washer; a blanking or laser-cutting the annulus from 1 mm steel shim stock, followed by deburring, thickness inspection, and corrosion-protective finishing if required"
  manufacturing_steps:
    - Blank, punch, waterjet, or laser-cut the 7 mm ID and 13 mm OD annulus from sheet stock if made locally.
    - Deburr both faces and edges so the shim seats flat without damaging adjacent parts.
    - Inspect thickness and flatness; finish or oil lightly if corrosion protection is needed.
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2APF_shim_disk.step; https://www.metricmcc.com/precision-shim-ring; https://www.accu-components.com/us/shim-washers/917018-HSHN-20-28-2-A2"
    cited_fact_or_basis: "CAD preview and geometry show a simple flat annular washer. MetricMCC describes DIN 988 shim rings as washer-style parts used to limit excess space and axial movement. Accu lists DIN 988 shim washers as metric parts with specified ID, OD, thickness, material family, and thickness tolerance; this supports procurement as a standard part, while the local cutting/deburring process is inferred from the simple sheet-metal geometry."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The manufacturing route uses sheet-stock cutting because the part is a flat 1 mm annulus with no visible formed or assembled features.
  uncertainty_notes:
    - "Targeted_web_search: queries tried: '2APF shim disk manufacturing', 'DIN 988 7x13x1 shim washer', 'DIN 988 shim washers material steel'; searches found standard shim-washer catalog evidence but no row-specific manufacturing process for 2APF."
    - "The result does not claim a sourced manufacturing method for the original part"
kb_implications:
  - "item_granularity: simple_part - Model as a reusable small shim washer or shim-disk part, not as a machine-specific assembly; dimensions can be stored as a 7 x 13 x 1 mm variant note."
---
