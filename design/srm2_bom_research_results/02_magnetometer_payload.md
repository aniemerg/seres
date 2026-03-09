1. `System boundary`
   A rover-mounted **vector magnetometer payload** for prospecting that:

* Measures **DC to low-frequency** magnetic field (≈0–10 Hz) near the lunar surface to detect **crustal anomalies** and **local ferromagnetic sources** (NiFe metal, troilite-bearing lithologies, impact-generated ferromagnetic phases).
* Includes **mounting/boom**, **front-end sensor(s)**, **low-noise electronics**, **thermal + dust mitigation**, **magnetic cleanliness controls**, and **calibration + in-field compensation**.
* Outputs **timestamped, temperature-tagged vector field** (Bx, By, Bz) plus diagnostics suitable for automated “process gating” (e.g., “stop & sample,” “flag contamination,” “promising anomaly”).

Out of scope:

* Drilling/sampling hardware, ground-penetrating radar, full geologic interpretation pipeline (only the data-quality constraints and gating signals are in scope).

---

2. `Functional decomposition`
   **F0. Field sensing**

* F0.1 Vector sensing (3-axis)
* F0.2 (Optional) **gradiometry** via two sensors separated along a boom (reject rover self-field)

**F1. Signal conditioning + digitization**

* Low-noise analog front end (AFE), ADC, sampling control, anti-alias filtering

**F2. Thermal/dust robustness**

* Thermal isolation, heater (optional), temperature sensing at sensor + electronics
* Dust-tolerant housing, sealed connectors

**F3. Magnetic cleanliness + self-field control**

* Non-magnetic materials near sensor
* Cable routing, current management, characterization of rover magnetic dipole

**F4. Calibration + compensation**

* Ground calibration: scale factors, orthogonality, offsets vs temperature
* In-field: offset tracking, rover-field subtraction, quality flags

**F5. Data products + gating metrics**

* Cleaned B-field estimate, noise metrics, rover-activity flags, “anomaly score”

---

3. `Candidate architecture options (A/B/C)`

### A) Dual-sensor **fluxgate gradiometer** on a short boom (Recommended for prospecting)

* **Sensors:** 2× tri-axial fluxgate heads, separated by ~0.5–1.0 m (baseline).
* **Why:** Fluxgates are the workhorse for planetary DC/low-f magnetics; dual sensors help remove rover-generated fields (common-mode) and detect local gradients (near-field dipoles).
* **Tradeoffs:** Slightly more mass/power and integration complexity. Needs strong magnetic cleanliness discipline. Planetary missions commonly use fluxgates; Lunar Prospector used a 3-axis fluxgate MAG with boom separation from spacecraft to reduce contamination. ([Planetary Data System][1])

### B) Single-sensor fluxgate on a boom (Simplest “real” science-grade baseline)

* **Sensors:** 1× tri-axial fluxgate head.
* **Why:** Lowest complexity while maintaining high-quality DC capability.
* **Tradeoffs:** Harder to subtract rover self-field; more conservative gating thresholds needed.

### C) Solid-state (AMR/TMR/Hall) “micro-mag” array + signal processing (Advanced/optional)

* **Sensors:** AMR (anisotropic magnetoresistance) or similar miniaturized sensors; potentially multiple sensors arranged as a small array for gradient estimation.
* **Why:** Lower mass/power; easier mechanical integration; AMR is discussed as a small-sensor approach for space when resources are tight. ([PMC][2])
* **Tradeoffs:** Typically higher offsets/temperature dependence and calibration burden vs fluxgate; more vulnerable to thermal cycling drift for absolute measurements (but can still be useful for **relative anomaly mapping** with careful procedures).

---

4. `Recommended architecture`
   **First-generation (high confidence): Option A — Dual-sensor fluxgate gradiometer** designed for “stop-and-sense” rover operations.

Key design choices:

* **Two tri-axial fluxgates** on a **non-magnetic boom/mast**, baseline 0.7 m (target range 0.5–1.0 m).
* Place the **outer sensor** as far from rover electronics/motors as practical; use inner sensor as reference for rover-field subtraction.
* **Operate in measurement modes** that minimize rover magnetic noise:

  * “Traverse mode”: higher noise tolerated, map trends.
  * “Station mode”: motors off, stable power state, collect low-noise record (e.g., 60–180 s) for gating.
* Adopt a **magnetic cleanliness plan** (materials screening + layout rules) inspired by spacecraft magnetics practice. ([NASA Technical Reports Server][3])

**Second-generation (optional):**

* Replace/wrap fluxgate head with locally manufacturable “PCB fluxgate” or AMR array once coil winding, core materials, and precision assembly are available (higher uncertainty).

---

5. `BOM draft` (component, material, qty, unit, rationale, manufacturability)

### Sensor stack (choose per option)

1. **Tri-axial fluxgate sensor head** (space/industrial grade, ±65,000 nT class)

* Material: mixed (per vendor; ferrite/metglas core, copper coils, ceramic/FR4)
* Qty: 2 (Option A) / 1 (Option B)
* Unit: ea
* Rationale: best DC/low-f stability; proven in planetary missions. ([Planetary Data System][1])
* Manufacturability: **Imported (1st gen)**; **2nd gen** possible with coil/core production (uncertain)

2. **Precision temperature sensor at each head** (PT1000 or silicon temp IC)

* Material: platinum element / silicon
* Qty: 2
* Unit: ea
* Rationale: correct offset/scale vs temperature; essential for thermal cycling compensation

3. **(Optional) Small calibration coil** around each head (single-turn or multi-turn)

* Material: copper
* Qty: 2
* Unit: set
* Rationale: inject known test field for health checks; also helps track sensitivity drift

### Boom/mounting + harness

4. **Non-magnetic boom/mast section**

* Material: **GFRP**, CFRP (verify magnetic cleanliness), or **titanium/aluminum** (keep ferromagnetics away)
* Qty: 1
* Unit: asm
* Rationale: standoff from rover self-field; dual sensor baseline support
* Manufacturability: **Locally manufacturable** (composites are harder 1st gen; aluminum/titanium machining likely earlier)

5. **Sensor mounts + fasteners (non-magnetic)**

* Material: titanium, aluminum, brass; avoid steel
* Qty: 1
* Unit: kit
* Rationale: prevent local dipoles near sensors

6. **Twisted-pair shielded cable harness**

* Material: copper + braided shield + PTFE/FEP insulation
* Qty: 1
* Unit: set
* Rationale: reduce EMI pickup; stable insulation in vacuum/thermal extremes

7. **Vacuum-rated connectors (sealed)**

* Material: metal shell (non-magnetic), gold-plated contacts
* Qty: 2–4
* Unit: ea
* Rationale: field serviceability and module swap-out

### Electronics (in rover warm electronics bay)

8. **Low-noise AFE + ADC board**

* Material: FR-4 PCB, rad-tolerant/industrial components
* Qty: 1
* Unit: ea
* Rationale: digitize at 10–100 Hz, low offset drift

9. **MCU/FPGA interface + time sync**

* Material: electronics
* Qty: 1
* Unit: ea
* Rationale: timestamping; rover bus integration; mode control

10. **EMI filtering + power conditioning**

* Material: inductors/caps (non-magnetic types selected)
* Qty: 1
* Unit: set
* Rationale: suppress conducted noise from rover power

### Thermal/dust

11. **Sensor head housing**

* Material: aluminum/PEEK + dust seals
* Qty: 2
* Unit: ea
* Rationale: dust shielding + radiative control

12. **MLI patch + (optional) micro-heater**

* Material: aluminized film + Kapton heater
* Qty: 2
* Unit: set
* Rationale: mitigate extreme temperature swings (especially for night survival if required)

**Note on shielding:** magnetic shielding (mu-metal) is usually counterproductive near a magnetometer (it distorts the ambient field). Instead: distance + cleanliness + subtraction using dual sensors.

---

6. `Manufacturing route draft` (ordered process steps with inputs/outputs)

**First-generation (ISRU-feasible structure + imported sensors/electronics):**

1. Fabricate boom sections (machining aluminum/titanium)

   * Inputs: stock material, CNC/manual machining
   * Outputs: boom tube/struts, mounting interfaces

2. Produce non-magnetic brackets + sensor cradles

   * Inputs: aluminum/titanium/PEEK, fasteners
   * Outputs: sensor mount kit

3. Cable harness fabrication

   * Inputs: shielded twisted-pair wire, connectors, strain relief
   * Outputs: tested harness (continuity, insulation resistance)

4. Electronics assembly (rover bay PCB)

   * Inputs: PCB, components, soldering/reflow
   * Outputs: AFE/ADC + controller board

5. Final integration on rover

   * Inputs: boom, mounts, sensor heads, harness
   * Outputs: installed payload with baseline separation measured and logged

**Second-generation (advanced/optional):**

* Wind fluxgate drive/sense coils, fabricate cores, potting, precision alignment/orthogonality calibration (high process maturity required; not recommended for earliest lunar staging).

---

7. `Test/verification steps`

**Bench / Earth (pre-flight)**

1. **3-axis Helmholtz coil calibration** (scale factors, orthogonality, offsets) across temperature sweep

   * Record calibration model: B = M·(raw) + b(T)
   * Temperature sweep is critical (thermal drift is a dominant error driver). InSight IFG calibration work highlights the need for careful ground calibration and correction modeling. ([USRA Houston][4])

2. **Magnetic cleanliness screening** of nearby rover parts (motors, fasteners, batteries, speakers, magnets)

   * Build a “do-not-place” radius map around the sensor.

3. EMI susceptibility test with rover power states

   * Drive motors, comms, heaters; measure spectral contamination.

**On-Moon / field commissioning**
4) **Static offset check** (motors off, stable power state) at multiple rover orientations
5) **Figure-8 / yaw sweep**: rotate rover slowly; fit rover dipole + sensor offsets
6) **Dual-sensor subtraction validation**: compare (outer-inner) gradient channel stability over time

**Routine ops verification**
7) Periodic “health injection” via calibration coil (if included): confirm sensitivity + axis integrity
8) Noise-floor tracking: compute PSD in 0.1–5 Hz band during station mode; flag regressions

---

8. `Failure modes and maintenance plan`

**Likely failure modes**

* **Thermal drift / offset jumps** after extreme cycles (sensor core stress, electronics drift)
* **Cable/connector intermittency** from thermal contraction, dust intrusion
* **Rover self-field growth** (aging motors, magnetized parts after shocks)
* **EMI bursts** from switching power supplies, comms, actuator transients
* **Mechanical misalignment** (boom flex changes sensor attitude)

**Maintenance/mitigations**

* Modular replaceable sensor head + harness (field swappable)
* Dual-sensor architecture: if one head degrades, fallback to single-sensor mode with stricter gating
* Enforce “magnetics-safe service kit” (non-magnetic tools/fasteners)
* Periodic recalibration maneuvers (short yaw sweep) to refresh rover-field model
* Conservative operational rule: **only trust gating decisions from station-mode records** with motors off and stable power loads

---

9. `Assumptions and uncertainties`

**Assumptions**

* Prospecting targets produce anomalies that are detectable at rover standoff distances. Lunar crustal anomaly intensities can be significant in some regions (strong anomalies exist; surface intensities can be high in mapped anomaly regions). ([AGU Publications][5])
* Most useful prospecting will be done in “stop-and-sense” mode, not while driving.
* Rover can provide attitude/orientation knowledge good enough to rotate vectors into local frame (or at least compare consistent frames).

**Uncertainties**

* **Local detectability of NiFe/troilite** depends heavily on target size/depth and geology; magnetometer sees fields, not composition directly. Troilite is only weakly magnetic unless associated phases are present; NiFe metal is the stronger driver (site dependent).
* Night survival: if rover sleeps cold-soaked, you may lose absolute calibration across nights unless you maintain sensor/electronics within a controlled thermal envelope (power trade).
* Exact noise levels depend on rover EM environment; integration discipline dominates performance more than sensor datasheet.

---

10. `Sources and confidence` (high/medium/low confidence per major claim)

**High confidence**

* Fluxgate magnetometers are a proven approach for planetary magnetic-field measurement; Lunar Prospector MAG/ER instrumentation included a 3-axis fluxgate magnetometer with common electronics. ([Planetary Data System][1])
* Dual-sensor / boom standoff is a standard contamination-mitigation strategy (magnetic cleanliness practice emphasizes reducing stray fields at sensor location via design and screening). ([NASA Technical Reports Server][3])
* Thermal/operational contamination and the need for correction modeling are real and addressed in planetary magnetometer calibration work (e.g., InSight IFG calibration discussions). ([USRA Houston][4])

**Medium confidence**

* Dual-sensor gradiometry on a rover meaningfully improves subtraction of rover self-field for prospecting operations (strongly supported by general magnetometer practice and multi-sensor payloads, but rover-specific performance is integration-dependent). ([PMC][6])
* “Stop-and-sense” operational gating is the best practical way to get low-noise data on a rover (depends on rover design, but typically true).

**Low confidence (second-generation / advanced)**

* Near-term lunar ISRU manufacture of fluxgate heads (cores/coils) with sufficiently low drift for absolute vector science (possible in principle, but requires mature materials + precision processes; not first-gen).

---

### Data-quality constraints that affect process gating decisions (practical rules of thumb)

Use these as **hard gates** before declaring “anomaly detected”:

* **Station mode only**: motors off, steering actuators idle, comms in steady state.
* **Dual-sensor coherence**: if outer and inner sensors show identical spikes, treat as rover EMI (reject); if gradient channel (outer−inner) shows stable deviation, treat as local source candidate.
* **Thermal stability window**: require sensor temperature rate |dT/dt| below a threshold during the record (reduces drift-driven false positives).
* **Spectral cleanliness**: if strong narrowband tones appear synchronized with rover subsystems, reject or down-weight.
* **Repeatability**: anomaly must reproduce on a second pass (different heading) to reduce false positives from rover dipole geometry.

[1]: https://pds.nasa.gov/ds-view/pds/viewContext.jsp?identifier=urn%3Anasa%3Apds%3Acontext%3Ainstrument%3Alp.mager&version=1.0&utm_source=chatgpt.com "PDS: Context Information"
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3348798/?utm_source=chatgpt.com "Small Magnetic Sensors for Space Applications - PMC - NIH"
[3]: https://ntrs.nasa.gov/api/citations/19710003603/downloads/19710003603.pdf?utm_source=chatgpt.com "ASSESSMENT AND CONTROL OF SPACECRAFT ..."
[4]: https://www.hou.usra.edu/meetings/lpsc2020/pdf/1331.pdf?utm_source=chatgpt.com "insight fluxgate magnetometer data calibration assessment ..."
[5]: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014JE004785?utm_source=chatgpt.com "Surface vector mapping of magnetic anomalies over the Moon ..."
[6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12227506/?utm_source=chatgpt.com "The MAGnetometers for Innovation and Capability (MAGIC ..."
