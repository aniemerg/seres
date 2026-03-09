## 1. System boundary

**In-scope:** a rover-attachable `prospecting_module` that enables **mineral targeting + site qualification** for later extraction, sized for a **Kapvik-like microrover class** (Kapvik is ~41 kg, ~0.85 m long, solar + battery powered). ([Canadian Space Agency][1])

**Out-of-scope:** full-scale excavation/mining, large sample return, long-duration cryogenic storage, and production ISRU processing plants. (We *do* include interfaces and “handoff artifacts” for downstream extraction teams.)

**Operating context assumptions:** lunar vacuum, abrasive dust, temperature swings; prospecting is mostly **non-contact sensing + shallow ground truth**.

---

## 2. Functional decomposition

1. **Mounting & deployment**

   * Structural mount to rover hardpoints
   * Deployable booms/arms for standoff sensing (reduce rover magnetic/EM interference)
   * Tool-change / field-serviceable modules

2. **Targeting (regional → local)**

   * Rapid terrain imaging + spectral screening
   * Subsurface proxy mapping (hydration/volatiles proxy, layering, rocks)

3. **Ground-truth site qualification**

   * Shallow sampling/coring
   * In-situ material ID (mineralogy / elemental)
   * Geotechnical properties (penetration resistance, bearing, regolith density proxy)

4. **Data handling**

   * Time sync + localization tie-in (rover nav)
   * Calibration routines
   * Data products for extraction planning (maps, sample logs, confidence)

5. **Survivability & maintainability**

   * Dust seals, covers, purge/brush as needed
   * Replaceable wear parts (bits, shoes, brushes)
   * Health monitoring (motor current, vibration, temperature)

---

## 3. Candidate architecture options (A/B/C)

### A) “First-gen” **Lightweight multi-sensor + shallow sampler** (high confidence)

**Goal:** maximize prospecting value per kg and minimize mechanical complexity.

**Core elements**

* **Deployable magnetometer boom** (standoff)
* **Compact VNIR/SWIR point spectrometer or multispectral imager** (mineral screening)
* **Shallow corer/auger (10–30 cm)** with small sample cup
* **Penetrometer + thermal probe** (geotech + thermal conductivity proxy)
* Optional **compact GPR** (short-range layering, boulders, voids)

**Pros:** low mass, low power, high uptime, easier to field-service.
**Cons:** limited depth; volatiles confirmation indirect unless augmented.

---

### B) “Prospecting drill-lite” **0.5–1.0 m drill + minimal lab** (medium confidence)

**Goal:** confirm subsurface volatiles/mineral layers more directly.

* **Rotary-percussive drill** approaching VIPER/TRIDENT class depth (VIPER drill is ~1 m). ([NASA Science][2])
* Simple **cuttings capture** + sealed cups
* Optional **heating/volatiles release + small gas sensor** (not full MS)

**Pros:** stronger site qualification.
**Cons:** mass/power/thermal are much harder on a microrover; more failure modes.

---

### C) “Second-gen advanced” **Drill + sample processing (mini-lab)** (lower confidence for microrover)

**Goal:** emulate PROSPECT-like end-to-end volatile extraction + analysis.

* Drill to ~1 m and sample transfer
* **Heated ovens + gas processing + mass spectrometry** (PROSPECT’s drill + analysis package concept). ([Open University][3])

**Pros:** best science + ISRU relevance.
**Cons:** too heavy/complex for Kapvik-like rover unless rover grows substantially.

---

## 4. Recommended architecture

### Recommended: **Option A + “upgrade rails” toward B**

A **modular payload bay** with:

* **Core A stack** (mag boom + spectral + shallow sample + penetrometer/thermal),
* with mechanical/electrical provisions to later swap the shallow sampler for a deeper drill head (B) *without* redesigning the whole module.

This matches your constraints:

* **Physically realizable first-gen** (few actuators, mostly COTS-like sensors adapted for lunar),
* **Modular + repairable** (LRUs and wear parts),
* **ISRU-feasible** (produces maps/logs directly consumable by extraction planning).

---

## 5. BOM draft (submodules, mass ranges, interfaces)

> Mass ranges are **order-of-magnitude for Kapvik-class** payloading; exact numbers depend on sensor choice and shielding. Kapvik rover scale reference is ~41 kg total rover mass. ([Canadian Space Agency][1])

### 5.1 Structural + interface frame (First-gen, high confidence)

| Component                             |             Material | Qty | Unit | Rationale                        | Manufacturability                                          |
| ------------------------------------- | -------------------: | --: | ---- | -------------------------------- | ---------------------------------------------------------- |
| Payload baseplate w/ kinematic mounts | Al 6061 / Ti inserts |   1 | ea   | Stiff, light, repeatable swap    | **1st-gen:** imported; **2nd-gen:** ISRU Al possible later |
| Dust covers (hinged)                  |    Al + thin SS foil | 2–4 | ea   | Protect optics/tools in traverse | Imported early                                             |
| Quick-disconnect bracket set          |                Al/Ti |   1 | set  | Field swap in EVA/teleop         | Imported early                                             |

**Target mass:** 1.5–3.0 kg

---

### 5.2 Magnetometer boom (First-gen, high confidence)

| Component                             |                      Material | Qty | Unit | Rationale                                                                                                                                    | Manufacturability                              |
| ------------------------------------- | ----------------------------: | --: | ---- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Non-magnetic boom (1–1.5 m)           | GFRP/CFRP tube + Ti fasteners |   1 | ea   | Standoff reduces rover magnetic contamination                                                                                                | Imported early (composites)                    |
| Total-field or fluxgate magnetometer  |                   electronics |   1 | ea   | Mineral targeting, anomaly mapping; Kapvik has been used as a platform for magnetometer integration (research precedent) ([ResearchGate][4]) | Imported                                       |
| Boom deploy hinge + latch             |                         Ti/SS |   1 | set  | Simple 1-DOF deployment                                                                                                                      | Imported early                                 |
| Cable harness (twisted pair + shield) |                            Cu |   1 | set  | Noise control                                                                                                                                | Imported early; **2nd-gen:** Cu via ISRU later |

**Target mass:** 0.6–1.5 kg (boom + sensor)

---

### 5.3 Spectral + imaging head (First-gen, medium-high confidence)

| Component                                                |               Material | Qty | Unit | Rationale                                  | Manufacturability            |
| -------------------------------------------------------- | ---------------------: | --: | ---- | ------------------------------------------ | ---------------------------- |
| Context stereo camera (wide)                             |            electronics | 1–2 | ea   | Site context, rock/regolith discrimination | Imported                     |
| VNIR/SWIR point spectrometer **or** multispectral imager |     optics/electronics |   1 | ea   | Mineral screening, hydration features      | Imported optics              |
| Calibration target (diffuse + dark)                      | ceramic + coated metal |   1 | set  | Repeatable reflectance calibration         | Imported; later ceramic ISRU |

**Target mass:** 0.7–2.5 kg

---

### 5.4 Shallow sampling & geotech head (First-gen, high confidence)

| Component                      |                 Material | Qty | Unit | Rationale                                          | Manufacturability  |
| ------------------------------ | -----------------------: | --: | ---- | -------------------------------------------------- | ------------------ |
| Shallow corer/auger (10–30 cm) | tool steel / carbide tip |   1 | ea   | Ground truth with limited complexity               | Imported wear part |
| Sample cup carousel (4–8 cups) |             Al + SS cups |   1 | ea   | Multiple sites without cross-contam                | Imported early     |
| Penetrometer cone + load cell  |        SS + strain gauge |   1 | ea   | Bearing/compaction proxy for mobility & excavation | Imported           |
| Thermal needle probe (5–10 cm) |         SS + thermistors |   1 | ea   | Thermal gradient + conductivity proxy              | Imported           |

**Target mass:** 2.0–5.0 kg

---

### 5.5 Optional subsurface mapper: compact GPR (First-gen optional, medium confidence)

| Component                 |         Material | Qty | Unit | Rationale                                            | Manufacturability |
| ------------------------- | ---------------: | --: | ---- | ---------------------------------------------------- | ----------------- |
| GPR electronics (UHF/VHF) |      electronics |   1 | ea   | Layering, boulders, voids; helps excavation planning | Imported          |
| Antenna (skid-mounted)    | Al + RF laminate | 1–2 | ea   | Coupled to surface                                   | Imported          |

**Target mass:** 1.5–4.0 kg

---

### 5.6 Rover-module interfaces (First-gen, high confidence)

**Mechanical**

* 4-point hard mount (M6–M8 class) + **2 locating dowels** (repeatable alignment)
* Kinematic “drop-in” geometry: **one tapered pin + two slots** (tolerant of dust)
* Tool access envelope: allow **front/side** approach for service

**Electrical**

* **Primary power:** rover bus (recommend 24–28 V class) + fused branch for module
* **Peak power budgeting:** sampler motor transient peaks; provide local supercap or current limiting
* **Data:** CAN-FD or Ethernet (preferred for instruments), plus discrete GPIO for interlocks
* **Time sync:** PPS or PTP if rover supports it

**Thermal**

* Conductive mount pads to rover structure
* Survival heater line item only if rover cannot guarantee temperature

---

### 5.7 System-level mass & power (Kapvik-class plausible envelope)

**First-gen baseline (A, without GPR):** ~5–10 kg payload, ~15–40 W average, peaks 60–150 W during coring.
**With GPR:** +1.5–4 kg, +5–20 W.

---

## 6. Manufacturing route draft (ordered process steps)

### First-generation (import-heavy, lunar-assembly focused)

1. **Machine baseplate + brackets** (CNC Al 6061; Ti inserts)

   * Inputs: plate stock, fasteners
   * Outputs: mounting frame with alignment features
2. **Assemble magnetometer boom**

   * Inputs: composite tube, hinge/latch, harness
   * Outputs: deployable boom LRU
3. **Integrate sensor head**

   * Inputs: camera, spectrometer, calibration target
   * Outputs: calibrated instrument pod (sealed)
4. **Assemble sampling/geotech head**

   * Inputs: auger, motor/gearhead, cup carousel, penetrometer, thermal probe
   * Outputs: “sampler LRU” with replaceable bit
5. **Module integration**

   * Inputs: LRUs above, harness, dust covers
   * Outputs: complete `prospecting_module`
6. **Rover integration**

   * Mechanical mate + electrical mate + bus enumeration
   * Run calibration and interference characterization (mag/EM)

### Second-generation (ISRU-increasing, optional)

7. Replace Al structural parts with **ISRU Al** cast/extruded + finish-machined
8. Replace some ceramics (cal targets, insulators) with **ISRU ceramic/glass**
9. Transition harness conductors to **ISRU copper/aluminum** once refining exists

---

## 7. Test/verification steps

1. **Mechanical fit check**

   * Verify kinematic mounts seat under dust contamination (simulant + abrasive)
2. **Power integrity**

   * Peak-load test corer stall + current limiting; verify no rover brownout
3. **Magnetic cleanliness validation**

   * Boom deployed vs stowed; map rover interference; define operational constraints
4. **Spectral calibration**

   * Validate reflectance target stability vs temperature and dust; establish cleaning procedure
5. **Sampling performance**

   * Simulant bins: loose, compacted, gravelly; verify depth, sample volume, cross-contam rate
6. **Geotech correlation**

   * Penetrometer readings correlated to known compaction states; repeatability over temperature
7. **Thermal-vac**

   * Instrument health across expected thermal profile; verify heater duty if present
8. **End-to-end field rehearsal**

   * “Prospect loop”: traverse → scan → select site → sample → log → move

---

## 8. Failure modes and maintenance plan

### Likely failure modes

* **Dust ingress** into bearings, hinges, sample carousel
* **Bit wear / jam** in gravelly regolith (auger stalls)
* **Cable fatigue** at boom hinge
* **Thermal drift** in spectrometer calibration
* **Mag sensor contamination** from rover currents / moving ferrous items

### Maintenance / replacement strategy (swap-in field service)

* Design **LRUs**:

  1. magnetometer boom LRU
  2. sensor head LRU
  3. sampler LRU (motor + gearbox + carousel)
  4. wear kit (bits, skirts, brushes, seals)
* Provide **tool-less or single-tool fasteners** (captives) and **blind-mate connectors**
* Add **“cleaning posture”**: park tool head under a cover; actuate a simple brush/wiper
* Log **motor current signatures** to predict jams and schedule bit swaps

---

## 9. Assumptions and uncertainties

* **Payload capacity** of “Kapvik-like rover” is not specified publicly on the Kapvik overview page; I’m assuming ~5–10 kg is feasible for a microrover of this class (uncertainty: medium).
* Exact **power bus voltage** and data bus on your rover are unknown; interface described is a recommended standardization.
* Sensor selection (VNIR/SWIR vs multispectral vs compact XRF/LIBS) depends on your target minerals and allowable mass/power.
* GPR usefulness depends strongly on frequency choice and regolith properties at the intended sites.

---

## 10. Sources and confidence

**High confidence**

* Kapvik rover is ~41 kg and ~0.85 m scale; solar + battery powered. ([Canadian Space Agency][1])
* VIPER uses a ~1 m drill (TRIDENT) and integrates neutron + NIR + mass spec class instruments for volatile prospecting (as a reference for “deep drill” complexity). ([NASA Science][2])
* PROSPECT concept includes drill to ~1 m plus sample processing/analysis package (reference for second-gen mini-lab complexity). ([Open University][3])

**Medium confidence**

* Integration precedent for Kapvik-class rover with magnetometer (suggests feasibility of boom + magnetic cleanliness workflow), but detailed implementation data is not fully open in the snippet source. ([ResearchGate][4])
* Mass/power ranges provided here: representative for small rover payloads, but instrument-specific selections could shift totals significantly.

**Low confidence**

* Any claim about *exact* allowable payload mass/power margin on your specific rover build (needs your rover ICD).
* Performance of a given compact GPR configuration without site-specific regolith characterization.



[1]: https://www.asc-csa.gc.ca/eng/rovers/rover-fleet/kapvik.asp?utm_source=chatgpt.com "Kapvik (\"Wolverine\") | Canadian Space Agency"
[2]: https://science.nasa.gov/mission/viper/rover-and-instruments/?utm_source=chatgpt.com "VIPER Rover and Instruments"
[3]: https://oro.open.ac.uk/97111/1/frspt-05-1331828.pdf?utm_source=chatgpt.com "PROSPECT: A comprehensive sample acquisition and ... - ORO"
[4]: https://www.researchgate.net/publication/273474859_The_Kapvik_Robotic_Mast_An_Innovative_Onboard_Robotic_Arm_for_Planetary_Exploration_Rovers?utm_source=chatgpt.com "The Kapvik Robotic Mast: An Innovative Onboard ..."


I kept digging and still don’t see a **public, end-to-end Kapvik (“Wolverine”) bill of materials** (line-item BOM with vendor/part #/qty/cost) published by CSA or the build team. What *is* public is enough to build a **fairly detailed “inferred BOM”** from theses/books/papers plus photos.

Below is the most detailed “best-effort BOM guess” I can assemble **with citations for the parts that are explicitly named**.

---

## What Kapvik is (for BOM context)

* CSA describes Kapvik as one of its **science micro-rovers** intended as a helper/sidekick rover (e.g., digging for an astronaut). ([Canadian Space Agency][1])
* A Carleton thesis describes Kapvik as a **30 kg terrestrial prototype** built by a multi-institution team (MPB Technologies, Carleton, Ryerson, U of T, Xiphos, MDA Space Missions, U of Winnipeg). ([Library and Archives Canada][2])

---

## Inferred BOM (highest-confidence items first)

### 1) Mobility / drivetrain (explicit part names from the chassis thesis)

These are the closest thing to “real BOM lines” I’ve found.

**Per wheel drive train (very likely ×6):**

* **Maxon RE25 motor** (rated 36 V; operated from rover’s 24 V solar-array output per thesis) ([Library and Archives Canada][2])
* **Maxon GP26B planetary gearhead, 14:1** ([Library and Archives Canada][2])
* **Harmonic Drive gearhead, CSF-11-2XH-F, 100:1** ([Library and Archives Canada][2])
* **Motor encoders** are part of the sensor suite used on Kapvik (the thesis also discusses a specific absolute encoder as a candidate for later gen). ([Library and Archives Canada][2])

**Power budgeting clue (helps size electronics):**

* Thesis states Kapvik allocated **~24 W total** for the wheel drive systems (implying **~4 W/wheel if all six run**). ([Library and Archives Canada][2])

### 2) Force/terrain interaction instrumentation (explicit)

* **Memsense H3-IMU HP02-0300** IMU (3 accel + 3 rate gyros) ([Library and Archives Canada][2])
* **Sherborne Sensors “S4000M”** miniature load cell (the Springer excerpt also calls out **SS4000M-200 N load sensor with amplifier**) ([Library and Archives Canada][2])

### 3) Navigation perception sensors (explicit, from rover navigation literature + Springer excerpt)

A ResearchGate-hosted abstract for a Kapvik navigation/mapping paper says SLAM on Kapvik used:

* **Laser range finder** + **stereo cameras**, plus inertial sensors, sun sensor, wheel encoders. ([ResearchGate][3])

The Springer “Planetary Rovers” excerpt (figure list) gets more specific (these are presented as Kapvik components):

* **Hokuyo URG-04LX laser scanner** (a very common 2D lidar)
* **Point Grey Bumblebee XB3 stereovision system**
* **Sinclair Interplanetary SS-411 Sun sensor**
* A **pan–tilt unit** for Kapvik is explicitly called out (likely for the stereo/navigation camera package).

### 4) Avionics / compute / control (explicit names from Springer excerpt)

Again, we don’t have the full schematic in the excerpt, but it explicitly names:

* **Maxon EPOS 24/1 motor controller**
* **Xiphos Q6 FPGA processor card**
* A “**removable avionics box with backplane configuration**” and “avionics architecture and chassis electrical diagram” are referenced as Kapvik figures (suggesting modular electronics packaging).

### 5) Robotic arm / mast / scoop (visual evidence + published diagrams)

* CSA imagery shows Kapvik with a **soil scoop / digging end-effector** on an articulated arm/mast assembly. ([Canadian Space Agency][4])
* A published figure set for “Kapvik Robotic Mast” labels joints/sections: **turret, shoulder, elbow, wrist, scoop**, plus a “locking mechanism” and “navigation camera.” (This is a diagrammatic representation, but it’s very indicative of the mechanical subassemblies.)

---

## Visual inspection notes (what the photos suggest about construction)

From CSA’s Kapvik photos (not enough to identify exact vendor SKUs for most parts, but useful for “BOM category” inference):

* The chassis looks like **machined aluminum plate / box-frame construction** with a **top deck** carrying solar panels/electronics. ([Canadian Space Agency][4])
* The rocker-bogie arms appear to be **tubular/beam linkages** with **pinned joints** and visible **hard-stop geometry** consistent with standard rover suspensions (and that “hard stops” concept is explicitly referenced in the Springer excerpt).
* Wheel design in CSA photos appears like **lightweight spoked wheels** (typical of prototypes), and the Springer excerpt explicitly references “Kapvik rover wheel with cleats.”
* Visible wiring harnessing suggests **distributed motor controllers/sensors** routed back to an avionics enclosure. ([Canadian Space Agency][4])

---

## “Best-effort BOM guess” (structured)

Here’s a consolidated “guess BOM” (with confidence levels):

### Mobility (high confidence)

* 6× wheel modules:

  * Maxon RE25 motor ([Library and Archives Canada][2])
  * Maxon GP26B 14:1 planetary gearhead ([Library and Archives Canada][2])
  * Harmonic Drive CSF-11-2XH-F 100:1 strain-wave gearhead ([Library and Archives Canada][2])
  * Wheel + hub + bearings + mounts (custom fab; not vendor-identified)
* Rocker-bogie suspension links + differential mechanism (custom fab; thesis describes these subsystems but the snippet we pulled doesn’t enumerate vendors) ([Library and Archives Canada][2])

### Sensing (high confidence)

* Memsense H3-IMU HP02-0300 ([Library and Archives Canada][2])
* Sherborne SS/S4000M ~200 N class load sensors (+ amplifier) ([Library and Archives Canada][2])
* Wheel encoders (type/vendor not fully pinned down from what we pulled, but encoders are part of the sensing suite) ([ResearchGate][3])
* Hokuyo URG-04LX laser scanner
* Bumblebee XB3 stereo camera system
* Sinclair Interplanetary SS-411 sun sensor
* Pan–tilt unit for camera payload (vendor not identified)

### Control / compute (medium–high confidence)

* Maxon EPOS 24/1 motor controllers (quantity likely tied to #motors; could be 6 if one per wheel, or fewer if multiplexed—unclear)
* Xiphos Q6 FPGA processor card
* Removable avionics box + backplane (custom packaging)

### Manipulation / mast (medium confidence)

* Turret + shoulder + elbow + wrist + end-effector scoop subassemblies (actuator vendors not identified in the sources we successfully opened)
* Locking mechanism (likely for stow/deploy; details not identified)

### Power (low–medium confidence; we have hints but not the battery/charge controller SKU)

* Solar array output referenced as **24 V** (at least in the wheel-drive context). ([Library and Archives Canada][2])
* Battery pack(s), DC/DC conversion, and power distribution (no SKU-level sourcing found in the materials above)

[1]: https://www.asc-csa.gc.ca/eng/rovers/rover-fleet/kapvik.asp "Kapvik (\"Wolverine\") | Canadian Space Agency"
[2]: https://central.bac-lac.gc.ca/.item?app=Library&id=MR83070&oclc_number=898089144&op=pdf "ProQuest Dissertations"
[3]: https://www.researchgate.net/publication/289633480_Navigation_and_mapping_within_the_constraints_of_a_mars_micro-rover "Navigation and mapping within the constraints of a mars micro-rover | Request PDF"
[4]: https://www.asc-csa.gc.ca/eng/multimedia/search/image/4104 "Kapvik (\"Wolverine\")  - Canadian Space Agency"
