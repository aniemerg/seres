# Measurement Equipment

## Machine Identity

- KB ID: `measurement_equipment`
- KB name: Measurement equipment
- KB file: `kb/items/machines/measurement_equipment.yaml`
- Current KB type: `machine`
- Current KB mass: 30 kg
- Current KB description: general measurement and metrology equipment including multimeters, calipers, micrometers, dial indicators, and coordinate measuring equipment.
- Current KB BOM: precision calipers, micrometers, dial indicators, gauge blocks, multimeter, and small fasteners.

## KB Usage And Needed Function

The KB uses `measurement_equipment` for:

- `alignment_and_testing_basic_v0`
- `inspection_basic_v0`
- `calibration_basic_v0`
- `calibration_force_torque_sensor_v0`

Local dedupe notes say calibration standards were folded into `measurement_equipment`, making gauge blocks and reference artifacts implicit in this capability. The needed function is general dimensional/electrical measurement and calibration support for manufacturing quality control.

## Reality Classification

Classification: real practical metrology/tooling kit, not a single machine.

The item is realistic as a portable or bench metrology set. It combines dimensional tools and one electrical meter. The 30 kg mass is plausible if it includes a storage case, gauge blocks, calipers, micrometers, dial indicators, bases, and small electronics.

The main realism issue is scope. "Coordinate measuring equipment" is much larger and more specialized than a 30 kg hand metrology kit unless interpreted as small fixtures or not included. CMMs should remain separate.

## Evidence Links

- NIST states that gage blocks are the primary industrial method for standardizing dimension and discusses calibration by interferometry and mechanical comparison. Source: https://www.nist.gov/pml/sensor-science/dimensional-metrology/selected-publications-dimensional-metrology-gage-blocks
- Metric & Multistandard Components sells calipers, micrometers, dial indicators, gages, thread gages, and related measuring tools. Source: https://www.metricmcc.com/calipers-micrometers-dial-indicators
- Mitutoyo's precision measuring catalog presents a broad product line of precision measuring tools, instruments, and equipment for metrology. Source: https://www.mitutoyo.com/webfoo/wp-content/uploads/US-1005_Mitutoyo_Catalog.pdf
- MSC describes gauge blocks as used to calibrate micrometers, calipers, dial indicators, and other measuring equipment. Source: https://www.mscdirect.com/browse/tn/Measuring-Inspecting/Calibration-Layout-Machine-Setup-Tools/Gage-Blocks-Spacers-Balls/Gage-Blocks-Spacers
- CNC Cookbook's machinist metrology guide identifies digital calipers, micrometers, and dial test indicators with magnetic stands as basic tools for starting CNC/machine-shop measurement. Source: https://www.cnccookbook.com/metrology-machinist-tools-complete-guide/
- Allometrics describes calibrated gage blocks as known reference standards for validating micrometers, calipers, height gages, and CMM equipment. Source: https://allometrics.com/services/gage-block-calibration/

## Commercial Alternatives

- Manual metrology kit: calipers, micrometers, dial indicators, magnetic bases, gauge blocks.
- Inspection setup kit: surface plate, height gauge, squares, pins, blocks.
- Electrical measurement kit: multimeters, clamp meters, insulation testers.
- CMM or portable coordinate measuring arm for advanced dimensional inspection.
- Optical comparator or microscope for profile/visual inspection.
- Calibration lab standards for traceable measurement.

## Build Or Open-Source References

Basic mechanical holders, cases, stands, and gauges can be locally fabricated. Precision measurement artifacts are harder:

- Micrometers and calipers need accurate screws, jaws/anvils, scales, and calibration.
- Dial indicators need gears, racks, springs, jewels/bearings, and calibrated movement.
- Gauge blocks need hard stable material, precision grinding/lapping, flatness, dimensional calibration, and careful handling.
- Digital multimeters need stable references, precision resistors, ADCs, safety design, and calibration.

For early self-reproduction, calibrated imports are realistic even if storage cases and fixtures are local.

## Related Machine Research

Related reports already present:

- `inspection_tools_basic.md`
- `multimeter_set.md`
- `oscilloscope_basic.md`
- `tension_gauge.md`
- `precision_tooling_set.md`
- `cnc_mill.md`

`inspection_tools_basic` should cover lower-end manual inspection. `measurement_equipment` should be the broader calibrated metrology kit. Advanced optical metrology and CMMs should stay separate.

## Recommendation For KB Realism

Keep as a real metrology kit, but reclassify as a tool/equipment set rather than a machine.

Recommended cleanup:

- Define it as "calibrated measurement and metrology equipment set."
- Keep gauge blocks/reference standards explicitly or implicitly inside this item.
- Remove or clarify "coordinate measuring equipment" unless the KB intends a small portable measuring arm; a full CMM should be separate.
- Keep overlap with `inspection_tools_basic` controlled: inspection tools for basic checks, measurement equipment for calibrated metrology.

Do not treat this as a powered production machine in the imported-machine list.

## Confidence And Open Questions

Confidence: high that the item is real and necessary; high that it is a kit rather than a machine; medium on how advanced its CMM/electrical content should be.

Open questions:

- Should multimeters live here or only in `test_equipment_electronics`?
- Should a surface plate and height gauge be included?
- What calibration traceability level is assumed for self-reproduction?
