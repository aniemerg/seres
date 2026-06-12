# Oscilloscope Basic

## Machine identity

- KB ID: `oscilloscope_basic`
- KB name: Oscilloscope (basic)
- KB file: `kb/items/machines/oscilloscope_basic.yaml`
- Current KB type: `machine`
- Current KB mass: 3 kg
- Current KB import status: `is_import: true`
- Current KB description: 2-4 channel basic analog or digital storage oscilloscope, roughly 20-100 MHz bandwidth and 100 MS/s-1 GS/s sampling.

## KB usage and needed function

The KB uses `oscilloscope_basic` in electronics testing and calibration processes, including `testing_and_calibration_circuit_v0` and `electrical_testing_basic_v0`. It is also a component of `bom_test_equipment_electronics` and appears in the minimal self-reproducing set.

The needed function is observation and measurement of voltage waveforms over time during circuit debugging, commissioning, and calibration. This is a genuine test-and-measurement role, not a production machine in the usual material-processing sense.

## Reality classification

Classification: real practical instrument.

An oscilloscope is a standard electronics test instrument. The KB's stated capability range maps well to entry-level or bench digital storage oscilloscopes. The 3 kg mass is plausible for a compact bench scope, although some common models are slightly heavier with probes and accessories.

The item overlaps with broader KB equipment sets such as `test_equipment_electronics`, `electrical_test_equipment`, and `test_bench_electrical`. Keeping it separate is still defensible because an oscilloscope is a distinct, nameable instrument and is frequently referenced independently.

## Evidence links

- Tektronix, "Oscilloscope Basics: Waveforms 101": explains that oscilloscopes observe one or more voltages varying over time and present them as a two-dimensional voltage-versus-time graph. Source: https://www.tek.com/en/blog/oscilloscope-basics-waveforms-101
- Rohde & Schwarz, "Understanding basic oscilloscope operation": describes the primary purpose of an oscilloscope as measuring and displaying voltage versus time, widely used for electrical and electronic design, testing, and debugging. Source: https://www.rohde-schwarz.com/us/products/test-and-measurement/essentials-test-equipment/rs-essentials-digital-oscilloscopes/understanding-basic-oscilloscope-operation_254512.html
- Keysight, "What Is an Oscilloscope Waveform?": describes waveform measurements such as voltage, frequency, period, and duty cycle. Source: https://www.keysight.com/used/us/en/knowledge/glossary/oscilloscopes/what-is-an-oscilloscope-waveform
- Rigol DS1054Z product page: commercial 4-channel, 50 MHz, 1 GSa/s digital oscilloscope, closely matching the KB's basic oscilloscope description. Source: https://www.rigol-uk.co.uk/product/rigol-ds1054z-50mhz-digital-oscilloscope/

## Commercial alternatives

- Entry-level bench digital oscilloscopes from Rigol, Siglent, Tektronix, Keysight, Rohde & Schwarz, and Pico Technology.
- USB oscilloscopes for lower-mass portable use where a computer is available.
- Used analog oscilloscopes where digital storage and automatic measurements are not required.

## Build or open-source references

Open-source and open-hardware oscilloscope projects exist, but high-bandwidth, calibrated oscilloscopes remain difficult local-manufacturing targets because they need fast ADCs, analog front ends, probes, timing references, shielding, firmware/software, and calibration.

Examples:

- ScopeFun open-source instrumentation combines oscilloscope, arbitrary waveform generator, spectrum analyzer, logic analyzer, and digital pattern generator; it publishes software, firmware, and hardware sources. Source: https://www.scopefun.com/
- Haasoscope Pro is an open-source/open-hardware USB oscilloscope project with published design resources. Source: https://github.com/drandyhaas/HaasoscopePro

The current KB choice to mark this as import is realistic unless the model explicitly wants to explore local precision electronics manufacturing.

## Related machine research

Related KB items:

- `test_equipment_electronics`
- `electrical_test_equipment`
- `test_bench_electrical`
- `oscilloscope_analog_v0`
- `multimeter_basic` or related metrology instruments if present in future cleanup

The local dedupe notes already suggest broad overlap among electrical/electronics test equipment sets. `oscilloscope_basic` can either remain a discrete instrument or be treated as a component of a larger test bench.

## Recommendation for KB realism

Keep as a real imported instrument.

For realism, keep `oscilloscope_basic` as a distinct instrument when processes specifically require waveform observation. Also allow broader recipes or machine sets such as `test_equipment_electronics` to include it as a component. Avoid modeling local manufacture in detail unless electronics closure becomes a priority; imported precision ADCs, displays, references, and probes are reasonable boundary assumptions.

If future dedupe is performed, do not delete the concept. Instead, decide whether process `resource_requirements` should call for `oscilloscope_basic` directly or for a bundled `electronics_test_bench`.

## Confidence and open questions

Confidence: high that the item represents real practical equipment and that the import status is realistic.

Open questions:

- Should `oscilloscope_basic` remain a standalone machine or only appear inside `test_equipment_electronics`?
- Should `oscilloscope_analog_v0` be a real alternative path, a deprecated experimental item, or a lower-capability local-manufacturing placeholder?
- What calibration reference standards should be modeled if electronics test equipment becomes a closure priority?
