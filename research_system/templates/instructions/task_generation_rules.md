# Task Generation Rules Template

Define how input rows, documents, or records should become research tasks.

For BOM missions, prefer one task per unique part or part family instead of one
task per source row. Preserve all source row IDs in the generated task payload.

Group records when:
- They have the same part number.
- They have the same normalized name, function, and material.
- Variants differ only by scale within the mission's acceptable tolerance.

Do not group records when:
- Material differs in a way that changes function.
- Electrical, thermal, precision, or environmental requirements differ.
- One item is consumable and another is reusable equipment.
