# Mold Tooling Migration Notes

## Context
Current KB processes model generic mold tooling as machine requirements (e.g.,
`pressing_mold_set`, `ceramic_press_or_mold_set`). This is a convenient abstraction,
but it is not physically accurate: molds are usually specific to the part geometry.

## Why migrate
- Part-specific molds improve realism and traceability of tooling requirements.
- It makes it possible to track which parts require hardened tooling vs. simple
  ISRU metal molds.
- It avoids a single generic mold incorrectly enabling many unrelated processes.

## Suggested migration direction
- Introduce part-specific mold items (e.g., `mold_ceramic_tube_body_v0`,
  `mold_ferrite_toroid_core_v0`) and update recipes that call forming/pressing
  processes to require the appropriate mold.
- Keep the press machine separate (e.g., `molding_press_basic`), and treat molds
  as distinct tooling.
- Use part-specific molds first for high-impact recipes (largest mass or most
  frequent use) and expand coverage over time.

## Modeling guidance
Molds are not consumed in normal operation, so recipes should be explicit about
preserving the mold item. One practical pattern is to override process inputs
and outputs in the recipe step so the mold appears in both:

```
steps:
  - process_id: ceramic_forming_v0
    inputs:
      - item_id: mold_ceramic_tube_body_v0
        qty: 1
        unit: unit
      - item_id: ceramic_powder_mixture
        qty: 5.0
        unit: kg
    outputs:
      - item_id: mold_ceramic_tube_body_v0
        qty: 1
        unit: unit
      - item_id: green_ceramic_part
        qty: 5.0
        unit: kg
```

If a mold is consumed or damaged (e.g., single-use investment molds), model that
explicitly by omitting it from outputs or reducing the output quantity.
