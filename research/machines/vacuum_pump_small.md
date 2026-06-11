# Vacuum Pump Small Machine Reality Research

## Machine identity

- KB item id: `vacuum_pump_small`
- KB name: Vacuum pump (small)
- KB file: `kb/items/machines/vacuum_pump_small.yaml`
- Current KB kind: `machine`
- Current KB mass: 22.3 kg
- Current BOM: `bom_vacuum_pump_small_v0`
- Current recipe: `recipe_machine_vacuum_pump_small_v0`

## KB usage and needed function

The pump is used directly in vacuum tube assembly/evacuation/sealing, hydrogen recycle separation, tube sealing, and vacuum pump station assembly. It is also a BOM component for vacuum chambers, controlled atmosphere chambers, glove boxes/dry rooms, inert atmosphere systems, leak test equipment, cell sealer stations, vapor capture systems, and vacuum furnaces.

The needed function is a compact pump that can evacuate small chambers or process lines to rough or medium vacuum. In some applications it may also serve as a backing pump for a higher-vacuum pump. It should not be assumed to provide clean high vacuum, ultra-high vacuum, high throughput, or corrosive gas compatibility unless specified.

## Reality classification

Real practical machine.

Small rotary-vane and diaphragm vacuum pumps are standard laboratory and light-industrial equipment. The KB's 22.3 kg mass is plausible for a small oil-sealed rotary vane pump or a larger diaphragm/roughing pump. The local recipe is directionally realistic for a rotary vane or diaphragm pump, but vacuum performance depends on precision machining, seals, oil or diaphragm materials, gas ballast, contamination control, and test equipment.

## Evidence links

- Edwards describes its small oil-sealed rotary-vane pumps as used for scientific, laboratory, and light-industrial applications and as backing pumps for turbomolecular pumps: <https://www.edwardsvacuum.com/en-us/vacuum-pumps/our-products/oil-rotary-vane-pumps-two-stage/e2m>
- Welch sells oil-free diaphragm vacuum pumps for laboratory and industrial applications, emphasizing clean operation and chemical compatibility options: <https://www.welchvacuum.com/en-nam/vacuum-pumps/diaphragm-pumps/>
- Pfeiffer Vacuum describes rotary-vane pumps as proven stand-alone and backing pumps with ultimate pressures in the rough/medium-vacuum range: <https://www.pfeiffervacuum.com/us/en/knowledge/vacuum-technology/knowledge-book/4-vacuum-generation/4_2_rotary_vane_vacuum_pumps/>
- NES Company lists small dry-running rotary-vane pumps in the 4-17 CFM range for rough vacuum applications: <https://nescompany.com/products/ndrv-series-dry-running-rotary-vane-vacuum-pumps-small-capacity/>

## Commercial alternatives

- Oil-sealed two-stage rotary-vane pump: good general roughing/medium-vacuum pump and backing pump.
- Oil-free diaphragm pump: lower vacuum but cleaner and often better for chemistry, filtration, and corrosive vapors when chemically resistant versions are used.
- Dry scroll pump: cleaner, more expensive option for lab and semiconductor-style work.
- Pump station: pump plus gauge, trap/filter, valves, exhaust handling, controls, and chamber fittings.
- High-vacuum stack: roughing pump plus turbomolecular or diffusion pump for tube/high-vacuum work.

## Build or open-source references

The KB recipe is plausible as a coarse local manufacturing route for a simple rotary-vane pump: cast/machine a housing and rotor chamber, machine rotor/vanes and sealing surfaces, install motor, bearings, seals, wiring, and test leakage/performance.

The difficult parts are tight tolerances, surface finish, seal materials, vacuum oil or dry-running materials, cleanliness, and performance verification. A locally built small pump is credible for rough vacuum if precision machining and leak testing exist. It is less credible as a high-vacuum solution without additional pump stages, traps, gauges, and clean assembly procedures.

## Related machine research

Related local reports:

- `research/machines/sintering_furnace_v0.md`
- `research/machines/dust_collection_system.md`

Related KB notes:

- `docs/dedupe_decisions.md` keeps `vacuum_pump_small` as the canonical vacuum pump machine and deprecates `vacuum_pump_basic` as an incorrectly categorized part.

## Recommendation for KB realism

Keep `vacuum_pump_small` as the canonical small vacuum pump.

Recommended boundaries:

- Treat it as a roughing/medium-vacuum pump unless a process states a deeper vacuum level.
- For vacuum tubes, semiconductor-like processing, vacuum furnaces, and high-purity systems, require or document additional equipment: vacuum chamber, gauges, valves, traps/filters, high-vacuum pump stage, and bakeout/cleaning where appropriate.
- Split future variants by pump type only when the process needs it: oil rotary vane, diaphragm chemistry pump, dry scroll, turbomolecular-backed station.
- Keep it separate from `vacuum_pump_station`, which should represent an integrated pumping skid with gauges, valves, traps, and controls.
- Revisit the 22.3 kg mass only if the KB wants consistency with older dedupe notes that mention 35 kg.

## Confidence and open questions

Confidence: high that this is a real machine and a useful canonical KB item; medium on whether it is adequate for all current vacuum-tube and furnace usages without a higher-vacuum stage.

Open questions:

- What ultimate pressure do the vacuum tube processes require?
- Should vacuum pump process requirements specify rough, medium, high, or ultra-high vacuum capability?
- Does the KB want pump capacity modeled by chamber volume and pump-down time, or is one unit of small pump enough at this abstraction level?
