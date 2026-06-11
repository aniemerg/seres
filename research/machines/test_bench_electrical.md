# Electrical Test Bench Machine Reality Research

## Machine identity

- KB machine id: `test_bench_electrical`
- KB name: Electrical test bench
- KB file: `kb/items/machines/test_bench_electrical.yaml`
- Current KB mass: 200 kg
- Current BOM: `bom_test_bench_electrical_v0`
- Current recipe: `recipe_test_bench_electrical_v0`

## KB usage and needed function

The bench is used for electrical testing, burn-in, load testing/commissioning, integration testing, alignment/testing, electrical wiring and controls, and electronics assembly. Some processes also require `multimeter_set` or `power_supply_benchtop` separately.

The needed function is a safe, organized test environment: work surface, power distribution and protection, terminals/fixtures, instrument mounting, cooling/ventilation, grounding, and access to test instruments. For electronics work, it may also need a bench supply, multimeter, oscilloscope, signal/function generator, loads, probes, isolation, and calibration references.

## Reality classification

Real practical workstation or test station bundle.

Electrical test benches are real and common in labs, factories, motor shops, and electronics development. The KB item is realistic as a station that integrates power, fixtures, and instruments. The main issue is internal consistency: the current recipe says the bench "integrates existing instruments" and the BOM mostly contains frame/power/mounting parts, while dedupe notes describe it as the canonical item that consolidates portable electrical and electronics test equipment. Those two interpretations differ.

## Evidence links

- JM Test Systems offers customizable electrical and motor test benches that centralize electrical testing equipment and accessories: <https://jmtest.com/electrical-test-bench/>
- DirectIndustry lists electric test benches and stations for motors, electronics, energy meters, EV components, and industrial testing: <https://www.directindustry.com/industrial-manufacturer/electric-test-bench-226966.html>
- Rohde & Schwarz describes essential electronics bench tools including power supply, digital multimeter, oscilloscope, spectrum analyzer, and application-specific instruments: <https://www.rohde-schwarz.com/us/products/test-and-measurement/essentials-test-equipment/dc-power-supplies/5-essential-tools-on-an-electronics-bench_256910.html>
- Mouser's electronics test bench overview frames a bench as a bundle of instruments selected for electronics development and troubleshooting: <https://www.mouser.com/applications/electronic-test-bench/>

## Commercial alternatives

- Custom electrical test bench or motor test bench with integrated safety, loads, fixtures, and meters.
- Electronics lab bench assembled from discrete bench instruments: DC supply, DMM, oscilloscope, signal generator, electronic load, probes, ESD mat, and isolation transformer.
- Automated test equipment rack with switching, programmable supplies, data acquisition, and fixture interface.
- Portable test kit using multimeters, clamp meters, insulation testers, and test leads for field electrical work.

## Build or open-source references

The physical bench is straightforward to build from a frame, work surface, power distribution, terminal blocks, shelves/rails, cooling, grounding, and fixtures. The hard-to-reproduce parts are calibrated instruments and safety-rated protection equipment.

The current KB recipe is plausible if `test_bench_electrical` means a bench infrastructure that uses existing instruments. If it is intended to replace `electrical_test_equipment` and `test_equipment_electronics`, then the BOM should eventually include or reference instruments such as `multimeter_set`, `power_supply_benchtop`, `oscilloscope_basic`, signal source, loads, probes/test leads, and calibration references.

## Related machine research

Related local reports:

- `research/machines/multimeter_set.md`
- `research/machines/power_supply_benchtop.md`
- `research/machines/oscilloscope_basic.md`
- `research/machines/pcb_development_station.md`
- `research/machines/high_temperature_power_supply_v0.md`

Local dedupe notes:

- `docs/dedupe_decisions.md` keeps `test_bench_electrical` as the canonical electrical/electronics test bench and consolidates `electrical_test_equipment` and `test_equipment_electronics` into it.

## Recommendation for KB realism

Keep the item, but choose one interpretation and align the BOM/process usage.

Recommended options:

- If it is bench infrastructure, rename or note as `electrical_test_bench_infrastructure` and keep separate instrument requirements in processes.
- If it is the canonical full electrical/electronics test capability, update future BOM/modeling to include or reference `multimeter_set`, `power_supply_benchtop`, `oscilloscope_basic`, test leads, loads, and signal generation as appropriate.
- Keep `multimeter_set` and `power_supply_benchtop` as discrete instruments for simple processes; use `test_bench_electrical` for integrated testing, burn-in, commissioning, and electronics workflows.
- Add safety notes for mains isolation, fusing/breakers, grounding, ESD control, high-voltage guarding, and load dissipation where relevant.
- Keep the 200 kg mass for a bench-plus-fixtures station; it is too high for only portable instruments and too low for some large motor/transformer test benches.

## Confidence and open questions

Confidence: high that electrical test benches are real and useful; medium on the current KB scope because the BOM and dedupe notes imply different levels of included instrumentation.

Open questions:

- Should `test_bench_electrical` subsume `multimeter_set`, `power_supply_benchtop`, and `oscilloscope_basic`, or should processes list those instruments separately?
- Does the self-reproducing set require calibrated measurement capability or only functional pass/fail testing?
- Are high-voltage, motor-load, and electronics signal tests all intended to share one bench, or should those be split by voltage/power domain?
