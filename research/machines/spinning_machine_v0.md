# Spinning machine v0

## Machine identity

- KB ID: `spinning_machine_v0`
- KB name: Spinning machine v0
- KB file: `kb/items/machines/spinning_machine_v0.yaml`
- KB kind: `machine`
- Current KB mass: 300 kg
- Current KB definition: textile/fiber spinning machine for yarn production, with capabilities `fiber_spinning` and `yarn_production`.

## KB usage and needed function

The KB uses `spinning_machine_v0` in two different ways:

- Textile/fiber use: `kb/processes/textile_manufacturing_basic_v0.yaml` uses it to convert fiber materials into fabric through spinning plus weaving/knitting.
- Metal forming use: `kb/processes/metal_spinning_process_v0.yaml` uses it to spin-form stainless sheet into tank shells for recipes such as `recipe_tank_shell_spun_v0`, `recipe_lh2_storage_tank_cryogenic_v0`, `recipe_lox_storage_tank_cryogenic_v0`, and `recipe_mixing_tank_medium_v0`.

These are different machine classes. A textile spinning frame twists/draws fibers into yarn. A metal spinning machine is a lathe-like forming machine that rotates sheet metal over a mandrel. The current KB item definition matches the textile machine, while the metal shell recipes need a metal spinning lathe or CNC spinning machine.

## Reality classification

Classification: real practical machine, but overloaded in the KB.

Textile spinning machines are real. Metal spinning machines are also real. The current `spinning_machine_v0` item is real as a textile/fiber/yarn machine, but it is not the right machine for metal spinning. The KB should not use one ID for both functions because the materials, tooling, forces, speed, fixtures, and outputs differ substantially.

The 300 kg mass is plausible for a small textile spinning frame or compact machine, but may be low for an industrial metal spinning lathe capable of cryogenic tank shells.

## Evidence links

- Toyota Industries sells textile spinning machinery, including high-speed ring spinning frames and roving frames for yarn production. Source: https://www.toyota-industries.com/products/textile/spinning/index.html
- Ramella describes a spinning frame with drafting zones for controlling fibers and producing yarns across a range of weights. Source: https://www.ramella.com/spinningframe.php
- Metal-spinners.net describes metal spin forming as sheet metal being rotated while forced against rollers/mandrels, typically using a manual or CNC lathe. Source: https://metal-spinners.net/spin-forming/
- IQS Directory describes metal spinning/spin forming as transforming flat circular blanks into axially symmetrical round shapes by lateral force from a roller and a mandrel. Source: https://www.iqsdirectory.com/articles/metal-spinning.html

## Commercial alternatives

For textile use:

- Ring spinning frame.
- Roving frame.
- Laboratory spinning frame.
- Small yarn spinning machine for low-volume fiber processing.

For metal spinning use:

- Manual metal spinning lathe.
- CNC metal spinning machine.
- Shear spinning or flow-forming machine for stronger/thicker shell parts.
- Alternative forming processes such as deep drawing, hydroforming, rolling/welding, or press forming.

## Build or open-source references

Textile spinning can be built at simple scales using spinning wheels, flyer/bobbin assemblies, and drafting rollers, but industrial ring frames are more complex.

Metal spinning can be performed on a lathe with mandrels, pressure pad/tailstock support, forming tools or rollers, and appropriate lubrication. Hobby and model-engineering references discuss metal spinning in a lathe, but those are limited to relatively small and ductile workpieces.

The KB's metal tank-shell usage likely needs a dedicated `metal_spinning_lathe_v0` or a more general `forming_lathe_v0`, not a textile spinning frame.

## Related machine research

Related KB entries include:

- `spinning_frame_basic`
- `spindle_assembly_spinning`
- `spinning_drive_motor`
- `draft_roller_set`
- `tensioning_equipment`
- `metal_forming_basic_v0`
- `steel_forming_press`
- `plate_rolling_mill`

Textile spinning components should stay with `spinning_machine_v0`. Metal spinning should relate to metal-forming equipment and possibly lathe-like machine tools.

## Recommendation for KB realism

Split or retarget the overloaded usage.

Recommended cleanup:

- Keep `spinning_machine_v0` as the textile/fiber/yarn spinning machine.
- Add or reuse a separate machine for metal spinning, such as `metal_spinning_lathe_v0` or `cnc_metal_spinning_machine_v0`.
- Update `metal_spinning_process_v0` to require the metal-spinning machine, not `spinning_machine_v0`.
- If the KB wants to avoid a new machine, consider whether existing `precision_lathe`, `milling_machine_general_v0`, or `steel_forming_press` can cover the task, but only if notes make clear that suitable mandrels, rollers, and forming tooling are included.

Do not delete `spinning_machine_v0`; it is valid for textile/fiber processes. The issue is mixed semantics.

## Confidence and open questions

Confidence: high that the current item is real for textile spinning; high that the metal-spinning usage is a mismatch.

Open questions:

- Does the self-reproduction scenario actually need textile/fabric production, metal tank-shell spinning, or both?
- Are the tank shells small enough for a general lathe with spinning tooling, or do they require a dedicated large metal spinning machine?
- Should textile manufacturing be decomposed into separate spinning, weaving/knitting, and tension-control machines later?
- Is `metal_spinning_process_v0` intended to model conventional metal spinning, shear spinning, or flow forming?
