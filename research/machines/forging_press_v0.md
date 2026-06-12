# Forging Press v0 Machine Reality Research

## Machine identity

- KB machine id: `forging_press_v0`
- KB name: Forging press unit v0
- KB file: `kb/items/machines/forging_press_v0.yaml`
- Current KB mass: 850 kg
- Current BOM: `bom_forging_press_v0`
- Current recipe: `recipe_forging_press_v0`

## KB usage and needed function

The item is used by `metal_forging_process_v0`. Other forging processes use `power_hammer_or_press` or the general `hydraulic_press`.

The needed function is controlled deformation of heated metal under high force, with frame rigidity, ram/platen guidance, dies/tooling, hydraulic or mechanical drive, controls, and safety guarding. A forging press differs from a power hammer: it applies slower controlled pressure rather than repeated impact blows.

## Reality classification

Real practical machine, but it overlaps with other press/forging entries.

Forging presses are standard industrial and workshop machines. The KB's 850 kg mass is plausible for a compact shop hydraulic forging press, though industrial forging presses can be much larger. This item should remain distinct from `power_hammer_or_press` only if the process needs sustained controlled press force rather than impact hammering. It should remain distinct from `hydraulic_press` only if hot-forging duty, frame, dies, stroke, speed, and thermal environment matter.

## Evidence links

- Coal Iron Works sells hydraulic forging presses and self-contained forging machines for blacksmithing and small-shop forging: <https://coaliron.com/collections/forging-macines>
- Anyang USA sells hydraulic forging presses and forging hammers, illustrating the commercial distinction between press and hammer forging equipment: <https://anyangusa.net/>
- Big Blu Hammer sells hydraulic forging presses for blacksmithing and bladesmithing: <https://www.bigbluhammer.com/hydraulic-presses.html>
- Schuler describes forging presses for hot, warm, and cold forging, showing the industrial end of the same machine family: <https://www.schulergroup.com/en/products/forging-presses/>

## Commercial alternatives

- Compact hydraulic forging press for blacksmithing and small-batch forging.
- Mechanical forging press or screw press for repeated production forging.
- Power hammer for impact forging and drawing-out operations.
- General hydraulic shop press for non-hot-forging pressing, straightening, bearings, and compaction.
- Closed-die forging press with dedicated die sets for near-net-shape parts.

## Build or open-source references

Workshop hydraulic forging presses are commonly shop-built from welded frames, hydraulic cylinders, pumps/power units, valves, dies, and controls. The KB recipe's frame, hydraulic power unit, cylinder, die plates, controls, assembly, pressure test, and inspection are directionally realistic.

The safety and performance risks are substantial: frame deflection, weld quality, hydraulic pressure, die retention, hot scale, guarding, ram alignment, and pressure relief. A locally built forging press is plausible but should not be treated as a trivial variant of a general shop press.

## Related machine research

Related local reports:

- `research/machines/power_hammer_or_press.md`
- `research/machines/hydraulic_press.md`
- `research/machines/hydraulic_power_unit_basic.md`
- `research/machines/steel_forming_press.md`
- `research/machines/induction_forge_v0.md`

These reports support a hierarchy: heat source (`induction_forge_v0`), general press (`hydraulic_press`), impact hammer (`power_hammer_or_press`), and dedicated forging press (`forging_press_v0`) where needed.

## Recommendation for KB realism

Keep only if the KB needs dedicated hot-forging press capability.

Recommended options:

- Use `hydraulic_press` for general pressing, compaction, bearings, and cold forming.
- Use `power_hammer_or_press` where impact forging or hammer-like drawing is intended.
- Use `forging_press_v0` where controlled hot forging under sustained force is specifically needed.
- Add required tooling/dies and heat source assumptions to forging processes; the press alone does not heat metal.
- Consider dedupe later if only one `metal_forging_process_v0` uses this item and the process could be satisfied by existing `power_hammer_or_press` plus `induction_forge_v0`.

## Confidence and open questions

Confidence: high that forging presses are real; medium that the KB needs this separate item in addition to `hydraulic_press` and `power_hammer_or_press`.

Open questions:

- Does `metal_forging_process_v0` require press forging specifically, or would impact hammer forging be acceptable?
- What force rating is implied by the 850 kg compact press?
- Should forging dies/anvils be modeled as separate tooling requirements?
