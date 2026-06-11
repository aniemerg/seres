# Tension Control System

## Machine identity

- KB ID: `tension_control_system`
- KB name: Tension control system
- KB file: `kb/items/machines/tension_control_system.yaml`
- Current KB type: `machine`
- Current KB mass: 25 kg
- Current KB description: mechanical or electronic tension control system for wire, fiber, and cable winding operations, including a brake mechanism and feedback control.

## KB usage and needed function

The item is used as a subsystem in `bom_fiber_drawing_tower` and as a required machine in `fiber_drawing_basic_v0`. The modeled process draws fiber from molten material or a preform and needs controlled tension and speed while the fiber is drawn, guided, and wound.

The local recipe `recipe_tension_control_system_v0` builds a small feedback-controlled brake/actuator assembly from machined metal, wiring, electronics, sensors, a control board, terminals, and fasteners. That interpretation is plausible for a self-reproducing-system model: it represents the control loop and hardware for maintaining tension, not a full draw tower.

## Reality classification

Classification: real practical subsystem / generic industrial equipment category.

`tension_control_system` is not usually a single universal standalone machine. It is a generic category covering dancer arms, load-cell feedback, controllers, brakes, clutches, drives, and capstan or winder controls. It is a real and commercially available industrial subsystem for web handling, wire/fiber winding, rewinding, and fiber drawing.

For KB realism, the item is acceptable as a coarse imported machine/subsystem. It would be more precise if named `tension_control_subsystem` or split later into lower-level components such as `tension_sensor_or_load_cell`, `tension_controller`, `brake_or_drive_actuator`, and `dancer_arm_or_idler`.

## Evidence links

- Montalvo, "Web Tension Control Basics": describes open-loop and closed-loop tension control systems. Closed-loop systems use web tension measurement devices such as load cells or dancer position feedback sensors, a controller, and a torque device such as a brake, clutch, or drive. Source: https://montalvo.com/what-is-tension-control/
- Supertek, "Optical Fiber Drawing Tower": lists draw tower subsystems including belt-type capstan, tension dancer control, and bobbin winder, and explains that the draw-off controls precise fiber speed and decouples tension or pull force between drawing and take-up. Source: https://www.winding-technology.com/eu-en/optical-fiber/optical-fiber-drawing-tower
- Supertek WLT, "Tensile Force Controller": commercial electromagnetic dancer products are presented for winding wire, fiber, glass fiber, and optical fiber. The system includes dancer position sensing, integrated PID control, motor signal output, and digital tension setting. Source: https://www.supertek-wlt.com/winding-technology/tensile-force-controller
- Jenkins and Nagurka, "Capstan Design and Control for Drawing Optical Fiber": an ASME case study on feedback-controlled capstan drive design for optical fiber manufacture; it notes that draw speed and draw tension disturbances affect fiber quality and diameter control. Source: https://www.eng.mu.edu/nagurka/JenkinsNagurka_CapstanDesign%26Control__IMECE2007-41105.pdf

## Commercial alternatives

- Web-handling tension controllers and components from suppliers such as Montalvo, Double E, Maxcess/MAGPOWR, Nexen, Renova, and DFE.
- Fiber, wire, and filament winding/drawing tension systems from Supertek WLT, including electromagnetic dancer controllers and draw tower subsystems.
- Typical commercial implementations combine a sensing element, controller, and actuator rather than selling the whole category as one universal item.

## Build or open-source references

No mature open-source industrial fiber-drawing tension control package was found in this pass. However, the build concept is straightforward and matches the KB recipe: a load cell or dancer position sensor, microcontroller/PLC or PID controller, motor drive or brake actuator, idler/dancer mechanics, and calibration procedure.

Search attempts included open web queries for "open source tension controller winding dancer load cell" and fiber draw tower tension control. Results were mostly commercial products, control theory papers, and forum discussions rather than complete open-source hardware builds.

## Related machine research

No prior local `research/machines` report existed for this item at the time of writing. Closely related KB items likely needing consistent interpretation include:

- `fiber_drawing_tower`
- `drawing_rollers_precision`
- `fiber_collection_spool`
- `control_panel_basic`
- `tension_gauge`

## Recommendation for KB realism

Keep, but treat as a generic subsystem rather than a single highly specific machine.

Recommended wording if the KB is later edited: rename or document it as `tension_control_subsystem` for fiber/wire/web handling. The current 25 kg mass is plausible for a compact industrial subsystem with frame, sensor, brake/drive, and electronics. The recipe is also directionally plausible, although it duplicates some BOM concepts and should eventually align component names with the BOM.

Do not replace this with labor alone. Controlled fiber drawing and winding need continuous feedback and actuator response; a labor bot could install or calibrate the unit, but should not be the primary tension regulator during production.

## Confidence and open questions

Confidence: high that this represents real industrial equipment and is needed for fiber drawing/winding realism.

Open questions:

- Whether the KB wants one generic tension control subsystem or a decomposed set of sensor/controller/actuator parts.
- Whether the system should be modeled as part of `fiber_drawing_tower` only, rather than also as a separate required machine in the process.
- Whether mass should remain 25 kg or be parameterized by fiber/web size and required tension range.
