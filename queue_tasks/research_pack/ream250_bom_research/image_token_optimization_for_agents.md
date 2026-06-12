# Image Token Optimization For CAD Render Agents

This note is for agents using `gpt-5.5` to inspect reAM250 CAD preview images.
It is a token-budget note; the authoritative task workflow remains
`agent.md`.

## What OpenAI Counts

OpenAI image inputs are billed as tokens, and the conversion depends on the model and image detail setting. For `gpt-5.5`, the Images and Vision docs say:

- `detail` can be `low`, `high`, `original`, or `auto`.
- If `detail` is omitted, `gpt-5.5` treats it like `original`.
- `low` gives the model a low-resolution 512px x 512px version, suitable when fine detail is not important.
- `high` allows up to 2,500 image patches or a 2048px maximum dimension.
- `original` allows up to 10,000 image patches or a 6000px maximum dimension.
- Patch-based tokenization covers the image with 32px x 32px patches:

```text
patches = ceil(width / 32) * ceil(height / 32)
```

For `gpt-5.5`, avoid relying on the omitted/default detail behavior for routine CAD triage because it uses `original`, which is more detail than most part-identification tasks need.

Sources:

- OpenAI Images and Vision guide, detail levels and `gpt-5.5` sizing behavior: https://developers.openai.com/api/docs/guides/images-vision
- OpenAI Images and Vision guide, patch-based tokenization formula: https://developers.openai.com/api/docs/guides/images-vision
- OpenAI pricing page, GPT-5.5 input token price and image-token pricing note: https://openai.com/api/pricing/

## Practical Token Budgets

For `gpt-5.5` patch-based image input, approximate image token use before any model-specific multiplier by patch count:

```text
512 x 512   -> 16 * 16 = 256 patches
768 x 768   -> 24 * 24 = 576 patches
1024 x 1024 -> 32 * 32 = 1024 patches
1200 x 900  -> 38 * 29 = 1102 patches
```

Rendering four separate roughly 900-1000px images per part can cost several
thousand image tokens per part if all views are sent.

The reAM250 task renderer produces one compact 2x2 contact sheet. A typical
contact sheet near 512px square is approximately:

```text
ceil(512 / 32) * ceil(512 / 32) = 16 * 16 = 256 patches
```

That gives the agent iso/front/top/right context for roughly the same patch budget as one 512px image.

## Recommended Render Defaults

Use one 2x2 contact sheet per part for first-pass inspection.

Command:

```bash
output_dir="$(dirname "<output_path>")"
output_stem="$(basename "<output_path>" .md)"
queue_tasks/research_pack/ream250_bom_research/research_scripts/render_step_views.sh \
  "<canonical_step_path>" \
  --output-dir "$output_dir" \
  --output-stem "$output_stem"
```

Output:

```text
research/ream250_bom/<result-stem>__views_2x2.png
```

Current defaults:

```text
dpi = 128
views = iso, front, top, right
output = one compact 2x2 PNG contact sheet
individual views = disabled unless --individual-views is passed
```

Use separate images only when the contact sheet is insufficient:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/render_step_views.sh \
  "<canonical_step_path>" \
  --output-dir "$output_dir" \
  --output-stem "$output_stem" \
  --individual-views
```

## Recommended API Usage

For routine CAD triage, ask the model to inspect the compact contact sheet with `detail: "low"` first.

Example Responses API content:

```json
{
  "role": "user",
  "content": [
    {
      "type": "input_text",
      "text": "Inspect this CAD contact sheet. Identify the likely part type, visible holes/features, and whether a higher-detail render is needed."
    },
    {
      "type": "input_image",
      "image_url": "data:image/png;base64,...",
      "detail": "low"
    }
  ]
}
```

Escalate to `detail: "high"` or `detail: "original"` only when:

- the part has small text, dense holes, threads, tiny fastener features, or thin seals;
- the agent needs to compare two nearly identical profiles;
- the contact sheet makes the part too small to inspect;
- downstream work depends on precise visual localization.

Do not omit `detail` for `gpt-5.5` unless `original` is intentional.

## Render Workflow For Agents

1. Start with `context.canonical_step_path` from the leased queue item.

2. Generate a contact sheet:

```bash
output_dir="$(dirname "<output_path>")"
output_stem="$(basename "<output_path>" .md)"
queue_tasks/research_pack/ream250_bom_research/research_scripts/render_step_views.sh \
  "<canonical_step_path>" \
  --output-dir "$output_dir" \
  --output-stem "$output_stem"
```

3. Send only the `__views_2x2.png` image to `gpt-5.5` with `detail: "low"`.

4. If the response says the part is too small or details are not visible, rerender individual views:

```bash
queue_tasks/research_pack/ream250_bom_research/research_scripts/render_step_views.sh \
  "<canonical_step_path>" \
  --output-dir "$output_dir" \
  --output-stem "$output_stem" \
  --individual-views
```

5. Send only the specific view needed, not all views by default.

## Why This Is Better

- One contact sheet keeps all standard views in one image.
- The default output lands near 512px square, which keeps patch count low.
- Explicit `detail: "low"` prevents accidental `gpt-5.5` `original` processing.
- Individual high-detail views remain available when a part genuinely needs them.

## Limitations

- The renderer uses FreeCAD tessellation plus matplotlib, not native FreeCAD viewport screenshots.
- Broad flat faces may show triangulation or shading artifacts.
- The model does not receive original file metadata from the image itself; include the CAD filename in the prompt text.
- OpenAI notes that image resizing can affect original dimensions, and models may struggle with precise spatial localization. Do not use these previews for exact measurements.
