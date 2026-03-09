1. `System boundary`
   Post-reduction **physical/thermal separation** step that takes *reduced ilmenite* (typically an intimate, partly sintered mix of **metallic Fe + Ti-oxide rich solids**) and outputs:

* **Fe-rich product** (metallic iron concentrate, ideally low Ti/oxide carryover)
* **TiO2-rich product** (rutile/suboxide-rich concentrate, ideally low metallic Fe carryover)

Assume upstream reduction is already done (e.g., H2 reduction for O2 production), leaving Fe metal + Ti-oxide phases as commonly described for lunar ilmenite processing residues. ([NASA Technical Reports Server][1])

---

2. `Functional decomposition`

* **F1. Receive & meter feed**: reduced, partly sintered granules/powder; control PSD and bed depth.
* **F2. Thermal “liquation” conditioning**: heat-treat to **coarsen/coalesce Fe metal** without fully smelting Ti-oxides.
* **F3. Deagglomerate & classify**: controlled crushing + screening to liberate Fe nodules from Ti-oxide matrix.
* **F4. Primary separation**: **magnetic separation** to pull Fe metal (plus any strongly magnetic phases).
* **F5. Secondary cleanup**:

  * Fe product: knock off adhered oxides; optional re-pass magnetic + density classification.
  * TiO2 product: remove residual metal fines (magnetic scavenger stage).
* **F6. QA/QC sampling**: phase ID + composition checks.
* **F7. Dust/thermal management**: vacuum-compatible seals, dust filtration, thermal shielding, modular maintenance.

---

3. `Candidate architecture options (A/B/C)`

### A) Solid-state liquation + crush/classify + magnetic separation (lowest complexity)

**Idea:** Heat below full smelting so Fe metal migrates/coarsens; then mechanically liberate and magnetically separate.

* **Thermal envelope:** ~1100–1350 °C (tunable), below typical ilmenite smelting temperatures (~1600–1700 °C). ([SAIMM][2])
* **Pros:** Lowest power/thermal severity; no molten slag handling; modular; well-aligned with “first-gen ISRU.”
* **Cons:** Purity depends on liberation; some Ti-oxide/Fe intergrowth; may need multiple passes and careful PSD control.
* **Notes on “why it works”:** Reduced ilmenite residues can be an intimate Fe metal + rutile/suboxide mix. ([NASA Technical Reports Server][1])  Liquation heat-treat promotes Fe coarsening (sintering/wetting/solid-state diffusion), improving magnetic/physical separability.

### B) Full smelting separation (two-liquid phases): molten Fe + titania-rich slag (highest purity, higher complexity)

**Idea:** Heat high enough that iron becomes a molten metal phase and Ti-oxide forms a separate molten/semimolten slag; tap/separate by density.

* **Thermal envelope:** ~1600–1700 °C (typical for ilmenite smelting). ([SAIMM][2])
* **Pros:** Cleanest separation (metal vs slag); high Fe recovery; scalable once infrastructure exists.
* **Cons:** High power, refractory demands, thermal cycling risk; molten slag handling is harder in vacuum/low-g; higher “second-gen” complexity.

### C) Additive-assisted smelt / partial melt to promote Fe granules (intermediate; depends on flux availability)

**Idea:** Use flux/additives to lower slag viscosity/liquidus and encourage **iron granule formation** and separation from titania-rich slag.

* Literature examples show improved separation with additives and staged heating (e.g., Na2CO3 additions helped iron granule separation from titania slag at ~1300→1500 °C). ([MDPI][3])
* **Pros:** Can reduce temperature vs full smelt; better separation than pure solid-state.
* **Cons:** Additive supply chain on Moon (Na, B, etc.) is nontrivial; chemistry control more demanding; still requires hot slag handling.

---

4. `Recommended architecture`
   **Recommended (first-generation): Option A — solid-state liquation + mechanical liberation + multi-stage magnetic separation.**

Why:

* Avoids the very high-temperature, molten slag regime of classic smelting while still leveraging the strong magnetic contrast of Fe metal.
* Matches lunar constraints: vacuum-friendly, modular, repairable; can be built from “fab-lab class” hardware scaled up (furnace + crushers + magnetic separators).
* Compatible with the known outcome that ilmenite reduction leaves **metallic Fe intimately mixed with TiO2-rich solids**. ([NASA Technical Reports Server][1])

**Second-generation upgrade path:** migrate to **Option B** (true smelting + tapping) once you have robust refractories, higher continuous power, and slag-handling automation; or **Option C** if you develop a dependable flux supply from local resources.

---

5. `BOM draft` (component, material, qty, unit, rationale, manufacturability)

### Core module: Liquation furnace (solid-state conditioning)

* High-temp furnace (resistive or induction heated hot zone), refractory-lined

  * **Material:** Al2O3-based refractory or stabilized ZrO2 hot-face; structural shell in steel/inconel-class alloy (as available)
  * **Qty:** 1 set
  * **Rationale:** 1100–1350 °C soak; withstand thermal cycling; vacuum-compatible enclosure.
* Retort/crucibles/trays (feed containment)

  * **Material:** alumina or high-alumina ceramics; optional Mo/W for trays if available
  * **Qty:** 4–20 trays (batch)
  * **Rationale:** thin-bed heat treatment improves uniformity and coarsening.
* Vacuum/low-leak furnace enclosure + seals

  * **Material:** metal shell + high-temp seals (ceramic/metallic)
  * **Qty:** 1 set
  * **Rationale:** lunar vacuum helps; but you still need dust-tight containment.
* Temperature sensing and control

  * **Material:** thermocouples (Type C/S) or optical pyrometry ports
  * **Qty:** 2–6 sensors
  * **Rationale:** maintain setpoints/ramps to tune Fe coarsening vs unwanted Ti suboxide formation.

### Liberation & classification

* Controlled crusher (jaw + rolls) or impact mill (low fines mode)

  * **Material:** wear liners (ceramic/SiC)
  * **Qty:** 1–2 units
  * **Rationale:** deagglomerate without overgrinding.
* Screen stack / vibratory sieve (vacuum-dust enclosed)

  * **Material:** steel mesh / perforated plates
  * **Qty:** 1 set
  * **Rationale:** PSD windows critical for magnetic separation efficiency.

### Separation train

* Primary drum magnetic separator (adjustable field/geometry)

  * **Material:** permanent magnet assembly + wear shell
  * **Qty:** 1 unit
  * **Rationale:** pull Fe metal nodules; robust first-pass concentrator.
* Scavenger magnetic separator (higher gradient / belt)

  * **Qty:** 1 unit
  * **Rationale:** remove residual Fe fines from TiO2 product.
* Optional density separator (dry “air table” analog using vibration in controlled gas, or centrifugal classifier if you have gas loop)

  * **Qty:** 0–1 unit
  * **Rationale:** backup polishing stage if magnetic alone insufficient.

### Handling & dust control

* Enclosed screw/auger feeders + rotary valves

  * **Qty:** as needed
  * **Rationale:** steady feed; dust containment.
* Dust filtration (HEPA-equivalent in sealed loop) + electrostatic dust trap

  * **Qty:** 1 set
  * **Rationale:** regolith dust is abrasive and pervasive.

### QC/Metrology

* Simple magnetic susceptibility meter (bench)

  * **Qty:** 1
  * **Rationale:** fast process control.
* XRD capability (second-gen “lab” module)

  * **Qty:** 0–1
  * **Rationale:** identify rutile vs Magnéli suboxides; confirm Fe metal. (Magnéli-like suboxide phases can appear during reduction pathways.) ([SciELO][4])
* Compositional assay (XRF or wet chem lab—likely second-gen)

  * **Qty:** 0–1
  * **Rationale:** quantify Fe/Ti/O impurities.

---

6. `Manufacturing route draft` (ordered process steps with inputs/outputs)

### Route A (recommended): Solid-state liquation + magnetic

1. **Receive reduced ilmenite residue**

   * *Input:* reduced feed (Fe metal + Ti-oxide rich solids; partially sintered). ([NASA Technical Reports Server][1])
   * *Output:* metered batches

2. **Pre-classify (optional)**

   * *Input:* as-reduced chunks/granules
   * *Process:* light crushing + sieve to remove oversize that blocks heat transfer
   * *Output:* controlled PSD feed to liquation

3. **Liquation heat treatment (key step)**

   * *Process:* ramp to ~1100–1350 °C; soak (e.g., 0.5–4 h) in thin bed; controlled cool
   * *Goal:* Fe metal coarsens into separable nodules; Ti-oxide matrix remains solid (no slag handling).
   * *Output:* heat-treated agglomerate with larger Fe domains

4. **Deagglomerate / liberation crushing**

   * *Process:* low-fines crushing to liberate Fe nodules from oxide
   * *Output:* liberated mixed particles

5. **Screening/classification**

   * *Process:* split into PSD bands (e.g., coarse nodules vs fines)
   * *Output:* size streams optimized for magnetics

6. **Primary magnetic separation**

   * *Output streams:*

     * **Magnetic concentrate:** Fe-rich product (with some adherent oxides)
     * **Non-magnetic:** TiO2-rich product (with some Fe fines)

7. **Regrind/clean + secondary magnetic scavenging**

   * Fe line: gentle tumbling/attrition to remove oxide films, then re-pass magnet
   * TiO2 line: high-gradient scavenger magnet to strip remaining Fe fines
   * *Outputs:* upgraded Fe concentrate and upgraded TiO2 concentrate

8. **Quality checkpoints + packaging**

   * *Outputs:*

     * Fe product bin
     * TiO2-rich bin (rutile/suboxide-rich)

### Route B (second-gen): Smelting separation

* Heat to liquid regime to produce **molten iron + titania-rich slag** (industrial analog: ilmenite smelting around 1600–1700 °C). ([SAIMM][2])
* Tap/decant phases; cast iron; granulate slag.

---

7. `Test/verification steps`

### Process-performance tests (per batch)

* **Magnetic recovery curve:** measure mass pull vs separator setting; estimate Fe recovery.
* **Product composition quick checks:**

  * Fe concentrate: magnetism + density + microscopy for oxide rind.
  * TiO2 concentrate: residual magnetics mass fraction.

### Phase/composition verification (periodic)

* **XRD on TiO2-rich product**: confirm rutile/anatase vs Magnéli suboxides; track shifts with heat-treatment setpoints. ([SciELO][4])
* **Fe metallization** (Fe⁰ vs FeO/Fe2O3): simple reductive/oxidative mass-balance test, or dedicated assay (second-gen lab).
* **Cross-contamination metrics:**

  * Fe product: Ti wt% and O wt% (targets depend on downstream use—structural iron tolerates more O than electrical steel).
  * TiO2 product: metallic Fe ppm/wt% carryover (important if used for further Ti processing or as feedstock).

### Acceptance targets (practical first-gen)

* **Fe concentrate:** high magnetic fraction; minimal visible oxide matrix; consistent density.
* **TiO2 concentrate:** “near-zero” magnetic pickup in scavenger stage; stable XRD signature.

---

8. `Failure modes and maintenance plan`

### Common failure modes

* **Over-sintering during liquation:** feed turns into hard clinker; poor liberation → low separation efficiency.
* **Over-reduction / unwanted phases:** more Ti suboxides (Magnéli-like) can change conductivity/magnetics and complicate separations. ([SciELO][4])
* **Excess fines generation:** fines adhere electrostatically; clog screens; contaminate both products.
* **Magnet separator wear/dust ingress:** abrasive regolith dust erodes drums/belts; bearings fail.
* **Thermal shock to refractories/crucibles:** cracking from aggressive ramps.

### Maintenance plan (modular)

* **Hot-zone consumables:** swap trays/crucibles; inspect refractory hot-face after defined thermal cycles.
* **Crusher liners & screens:** quick-change wear parts; keep spares.
* **Mag separator:** sealed bearing cartridges; replaceable drum shell; routine dust purge.
* **Dust system:** filter cassette replacement; periodic electrostatic trap cleaning.

---

9. `Assumptions and uncertainties`

* **Feed composition variability:** lunar regolith ilmenite varies with Mg/Fe content and accessory phases; residue may include glassy phases besides Fe/Ti oxides. (Expect tuning of ramp/soak.)
* **Exact “liquation” kinetics:** Fe coarsening rate depends strongly on temperature, PSD, and prior reduction history; you will need empirical tuning.
* **Ti-oxide phase state:** rutile vs suboxides depends on oxygen fugacity and temperature; some references note TiO2 reduction can occur under certain conditions at higher temperatures. ([NASA Technical Reports Server][5])
* **Separation purity limits:** purely magnetic separation may hit a ceiling if Fe is finely disseminated or locked; may require optional polishing steps (attrition, secondary classification) or eventual smelting.

---

10. `Sources and confidence` (high/medium/low confidence per major claim)

* **Reduced ilmenite residue is an intimate, partly sintered mix of metallic Fe and TiO2-rich solids (rutile/suboxides): High.** ([NASA Technical Reports Server][1])
* **Industrial ilmenite smelting produces titania-rich slag + molten iron at ~1600–1700 °C: High.** ([SAIMM][2])
* **Solid-state reduction pathways can yield metallic Fe plus Ti-oxide phases (including suboxides) and show phase evolution with reduction extent: Medium–High.** ([SciELO][4])
* **Additives (e.g., Na2CO3) and staged heating can promote separation of metallic iron granules from titania-rich slag in carbothermic systems: Medium.** ([MDPI][3])
* **Operationally, a first-gen lunar process should prefer solid-state liquation + magnetic separation over molten slag handling: Medium (engineering inference based on thermal/complexity constraints).** Supported by the high-temperature demands of smelting sources. ([SAIMM][2])

[1]: https://ntrs.nasa.gov/api/citations/19910015913/downloads/19910015913.pdf?utm_source=chatgpt.com "Extraction of Volatile and Metals From Extraterrestrial ..."
[2]: https://www.saimm.co.za/Conferences/HMC2007/075-84_Pistorius.pdf?utm_source=chatgpt.com "Ilmenite smelting: the basics"
[3]: https://www.mdpi.com/2075-4701/12/6/963?utm_source=chatgpt.com "Carbothermic Reduction of Ilmenite Concentrate with ..."
[4]: https://scielo.org.za/pdf/jsaimm/v117n5/04.pdf?utm_source=chatgpt.com "Solid-state reduction of an ilmenite concentrate with carbon"
[5]: https://ntrs.nasa.gov/api/citations/19910015054/downloads/19910015054.pdf?utm_source=chatgpt.com "n,31- 2,rz r-"
