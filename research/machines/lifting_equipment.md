# Lifting equipment

## Machine identity

- KB ID: `lifting_equipment`
- KB name: Lifting Equipment (Hoist/Crane)
- KB file: `kb/items/machines/lifting_equipment.yaml`
- KB kind: `machine`
- Current KB mass: 150 kg
- Current KB scope: small overhead hoist or gantry crane with 500 kg load capacity, 3-4 m lift height, steel frame, trolley, and manual or electric hoist.

## KB usage and needed function

The KB uses `lifting_equipment` in `kb/processes/drive_motor_medium_assembly_v0.yaml`, where it supports assembly of heavier motor components such as housings, rotors, and stators.

The intended function is generic workshop material handling: lifting, positioning, and moving components too heavy or awkward for a labor bot or manual handling alone. The BOM models a gantry/hoist assembly with structural frame, hoist drive, trolley, controls, and fasteners.

## Reality classification

Classification: real practical machine category.

`lifting_equipment` is a generic category, but the KB description is specific enough to be realistic: a small gantry crane, chain hoist, or overhead hoist/trolley system. The 500 kg capacity and 150 kg machine mass are plausible for a light workshop gantry/hoist, though actual mass varies widely with span, lift height, mobility, safety factor, and whether the hoist is manual or electric.

## Evidence links

- Yuantai/BetterCrane lists 500 kg and 1 ton gantry cranes equipped with manual chain hoists and describes simple structure and installation. Source: https://www.bettercrane.com/portable-gantry-crane/1-ton-gantry-crane.html
- Hoist UK lists a steel portable gantry with manual trolley and lifting capacity from 500 kg to 2,000 kg. Source: https://www.hoistuk.com/products/industrial/vgps-steel-portable-gantry/
- Harrington Hoists sells manual hoists, trolleys, beam clamps, and hoist/trolley combinations for lifting and moving needs. Source: https://www.harringtonhoists.com/
- EMH describes trolley-mounted crane hoists suspended from trolleys on monorail or bridge beams, matching the KB trolley/hoist concept. Source: https://www.emhcranes.com/cranes-101-overhead-crane-hoist-suspension-types/

## Commercial alternatives

Commercial alternatives include:

- Manual chain hoist plus beam trolley.
- Portable A-frame gantry crane.
- Fixed overhead monorail hoist.
- Jib crane.
- Small electric chain hoist.
- Hydraulic shop crane or engine hoist for lower-cost local handling.

For the KB's current motor-assembly use, a small gantry/chain hoist system is appropriate and more realistic than requiring a full overhead bridge crane.

## Build or open-source references

Workshop gantries and hoist supports are commonly built from steel I-beams, columns, trolleys, and chain hoists, but load rating and safety factors are critical:

- Wilker Do's documents a garage gantry chain hoist using an I-beam, columns, trolley, and hoist: https://wilkerdos.com/garage-gantry/
- Hobby and workshop examples exist for DIY gantry cranes, but they should not replace engineering verification for rated lifting.

The KB can model local fabrication of the frame, but purchased or carefully manufactured hoist/trolley components may remain realistic imports until detailed safety-critical designs exist.

## Related machine research

Related KB entries include:

- `labor_bot_general_v0`
- `assembly_tools_basic`
- `fixturing_workbench`
- `material_handling_v0`
- `hydraulic_cylinder_large_v0`

`lifting_equipment` should not be replaced by the labor bot alone for components near or above labor bot payload limits. It is a sensible workshop support machine.

## Recommendation for KB realism

Keep the item as a generic workshop lifting system.

Recommended clarification: "Small rated gantry crane or overhead hoist/trolley system for 500 kg component handling during assembly." This prevents confusion with large cranes, forklifts, or mining material-handling systems.

Future cleanup should ensure:

- Capacity and safety factor are stated.
- Hoist/trolley are either part of the machine BOM or referenced as separate components.
- Load-bearing frame fabrication uses realistic structural steel and inspection/testing assumptions.

## Confidence and open questions

Confidence: high that this is real and practical; high that it matches current KB motor assembly needs.

Open questions:

- Is 500 kg enough for the heaviest machine assemblies in the self-reproducing set?
- Should the hoist be manual, electric, or both?
- Are slings, shackles, hooks, rated fasteners, and inspection/test procedures modeled or bundled into the equipment?
- Should `material_handling_v0` use this machine explicitly when heavy components are moved?
