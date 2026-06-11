# Inspection Tools Basic

## Machine identity

- KB ID: `inspection_tools_basic`
- KB name: Inspection tools (basic)
- KB file: `kb/items/machines/inspection_tools_basic.yaml`
- Current KB type: `machine`
- Current KB mass: 8 kg
- Current KB description: basic inspection and quality-control tools including magnifying glasses, straightedges, gauges, calipers, and visual inspection aids for manual inspection and sorting.

## KB usage and needed function

The KB uses `inspection_tools_basic` for:

- `manual_inspection_sorting_v0`
- `precision_grinding_and_scraping_v0`

The BOM includes `caliper_set_precision`, `micrometer_set`, and `gauge_block_set`. The recipe also mentions straightedges, gauge blocks, calipers, magnifying lenses, and packaging the tool set.

There is overlap with `measurement_equipment`, which includes calipers, micrometers, dial indicators, gauge blocks, multimeters, a case, wire, and fasteners. There is also a separate `optical_metrology_tools` item for optical alignment and precision optical measurement.

The needed function is manual quality control: dimensional checks, visual inspection, sorting, setup verification, and calibration/reference measurements for basic manufacturing workflows.

## Reality classification

Classification: real kit/tool bundle, not a standalone machine.

Basic inspection tools are real and essential in any machine shop or manufacturing cell. Calipers, micrometers, gauge blocks, straightedges, gauges, magnifiers, and dial indicators are commonly sold and used as separate instruments or organized metrology kits.

The KB mass of 8 kg is plausible for a compact hand-inspection kit. The issue is not realism; it is classification and overlap. This item should be a tool kit, tooling set, or metrology kit rather than a powered machine.

## Evidence links

- NIST describes dimensional measurement services and high-accuracy length calibrations as essential to trade, research, and industrial traceability. Source: https://www.nist.gov/programs-projects/dimensional-measurement-services
- NIST's gage block reference states that gage blocks are a primary industrial method for standardizing dimension, with calibration by interferometry and mechanical comparison. Source: https://www.nist.gov/pml/sensor-science/dimensional-metrology/selected-publications-dimensional-metrology-gage-blocks
- Starrett describes precision measuring tools and gages, including gage blocks as primary standards for dimensional quality control. Source: https://www.starrett.com/news-events/precision-measuring-tools-gages-primer
- MSC Industrial Supply sells measuring and inspecting equipment for quality control, including precision measuring tools and calipers. Source: https://www.mscdirect.com/browse/Measuring-Inspecting?navid=2107563
- Haas Tooling sells gauge block sets for manufacturing and quality control, made to ASME/ISO standards with calibration certificates. Source: https://www.haastooling.com/c/gauge-blocks-accessories
- Industrial Inspection & Analysis summarizes common dimensional inspection hand tools, including micrometers, indicators, comparators, and protractors, and notes that tools require calibration and operator training. Source: https://industrial-ia.com/10-types-of-dimensional-inspection-hand-tools-and-when-to-use-them/

## Commercial alternatives

- Caliper and micrometer sets.
- Gauge block sets with certificates.
- Dial indicator and magnetic base kits.
- Precision straightedges, squares, feeler gauges, thread gauges, plug gauges, and pin gauges.
- Stereo inspection microscope or magnifier for visual inspection.
- Full dimensional metrology kits in storage cases.
- Coordinate measuring machine, optical comparator, or optical metrology system for higher-end inspection.

## Build or open-source references

Some basic tools can be locally fabricated or repaired, but accurate metrology depends on reference standards and calibration:

- Straightedges and squares can be scraped, ground, and lapped if reference surfaces exist.
- Simple gauges can be machined and checked against known references.
- Calipers and micrometers can be manufactured mechanically, but require precision screws, jaws/anvils, scales, and calibration.
- Gauge blocks require high hardness, flatness, dimensional stability, lapping, and certified measurement. They are plausible as imports early in the self-reproduction path.

For a realistic self-reproducing system, the kit should distinguish "shop-made inspection aids" from "calibrated reference standards."

## Related machine research

Related reports already present:

- `oscilloscope_basic.md`
- `multimeter_set.md`
- `tension_gauge.md`
- `optical_metrology_tools` is referenced in other reports but does not yet have a local research file in this run.
- `cnc_mill.md` notes the importance of metrology for precision machine construction.

Related KB items:

- `measurement_equipment`
- `optical_metrology_tools`
- `caliper_set_precision`
- `caliper_vernier_v0`
- `micrometer_set`
- `micrometer_mechanical_v0`
- `gauge_block_set`
- `dial_indicator_set`
- `granite_surface_plate_large`
- `coordinate_measuring_machine_v0`
- `optical_comparator_v0`

## Recommendation for KB realism

Keep the concept, but rename or reclassify it as a tool kit rather than a machine.

Recommended future cleanup:

- Use `inspection_tools_basic` for low-end manual inspection and sorting: magnifier, straightedge, ruler, simple gauges, calipers, and visual aids.
- Use `measurement_equipment` for a broader calibrated metrology kit with micrometers, gauge blocks, dial indicators, and electrical instruments.
- Use `optical_metrology_tools`, optical comparators, microscopes, or CMMs for specialized precision measurement.

Avoid counting `inspection_tools_basic` as a complex imported machine if the self-reproducing list is meant to show difficult machinery. It is realistic as an import seed item, but it is a compact calibrated toolkit. The calibration chain may be more important than the physical mass.

## Confidence and open questions

Confidence: high that the item is real and useful; high that it is a kit rather than a machine; medium on whether it should be merged with `measurement_equipment`.

Open questions:

- Should this item include calibrated gauge blocks and micrometers, or should those live only under `measurement_equipment`?
- Does the KB need a distinction between "inspection aids" and "traceable metrology standards"?
- Should manual inspection processes require labor plus this kit rather than listing it as a machine resource?
