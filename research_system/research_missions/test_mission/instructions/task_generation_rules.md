# Test Mission Task Generation Rules

Generate one task per unique part number. Preserve all source BOM row IDs in the
task payload.

Expected grouping for the fake BOM:

- `M3x12` rows should group into one fastener-family task.
- `ABC-123` should remain a motor task.
- `AL-2040` should remain an extrusion/structure task.
- `SENS-9` should remain a sensor task.
- `BRG-608` should remain a bearing task.
- `GT2-200` should remain a timing belt task.
- `PUL-20T` should remain a pulley task.
- `PSU-24V` should remain a power supply module task.
- `WIRE-22` should remain a wire task.
- `PLATE-3MM` should remain a mounting plate task.

Do not group records when:
- Part number differs.
- Material or function differs.
- One item is an electronics module and another is a structural/mechanical part.
