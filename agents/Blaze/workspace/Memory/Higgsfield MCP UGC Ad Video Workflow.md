---
title: Higgsfield MCP UGC Ad Video Workflow
agent: Blaze
created: 2026-04-29
tags:
  - higgsfield
  - mcp
  - ugc-ads
  - video-generation
  - product-ads
---

# Higgsfield MCP UGC Ad Video Workflow

A repeatable workflow for generating premium vertical product/UGC ad videos through the **Higgsfield MCP** using product images, creator/face references, and precise prompt control.

## What worked

The strongest results came from this pattern:

1. Connect Higgsfield MCP via OAuth device flow.
2. Use the MCP directly with JSON-RPC over `https://mcp.higgsfield.ai/mcp`.
3. Upload product and creator/reference images through `media_upload` using `upload_url`.
4. PUT the local image bytes to the presigned upload URL.
5. Confirm with `media_confirm`.
6. Call `generate_video` with `marketing_studio_video`.
7. Poll `job_status` until completed.
8. Download the resulting `.mp4` and deliver to Telegram.

## Config

Higgsfield MCP is configured at:

```yaml
mcp_servers:
  higgsfield:
    url: https://mcp.higgsfield.ai/mcp
    headers:
      Authorization: Bearer <token>
    timeout: 180
    connect_timeout: 60
```

Do **not** store raw tokens in Obsidian or Notion. Credentials live in `~/.hermes/config.yaml`.

## Working model/settings

Use:

- Tool: `generate_video`
- Model: `marketing_studio_video`
- Aspect ratio: `9:16` for ads/Reels/TikTok
- Duration: `10s` for UGC-style ad tests
- Reference role: `image`
- Poll: `job_status` with `sync: true`

## MCP tools used

### `media_upload`

Use this to get a presigned upload URL:

```json
{
  "method": "upload_url",
  "filename": "product.jpg",
  "content_type": "image/jpeg"
}
```

Then upload bytes to the returned `upload_url` with HTTP `PUT` and the exact content type.

### `media_confirm`

```json
{
  "type": "image",
  "media_id": "<media_id>"
}
```

### `generate_video`

Single product reference:

```json
{
  "params": {
    "model": "marketing_studio_video",
    "prompt": "<prompt>",
    "count": 1,
    "aspect_ratio": "9:16",
    "duration": 10,
    "medias": [
      {"value": "<product_media_id>", "role": "image"}
    ]
  }
}
```

Product + face/creator reference:

```json
{
  "params": {
    "model": "marketing_studio_video",
    "prompt": "<prompt>",
    "count": 1,
    "aspect_ratio": "9:16",
    "duration": 10,
    "medias": [
      {"value": "<product_media_id>", "role": "image"},
      {"value": "<creator_media_id>", "role": "image"}
    ]
  }
}
```

### `job_status`

```json
{
  "jobId": "<job_id>",
  "sync": true
}
```

Poll every ~8–10 seconds until status is completed or failed.

## Prompt formula

```text
Create a premium 9:16 vertical UGC ad video using two references:
Image 1 is the product reference: [exact product details]. Preserve product identity, label, color, shape, and scale. Keep the product front-facing and readable.
Image 2 is the creator/face reference: use this exact person as the on-camera creator, preserving [face/hair/glasses/clothes/expression].

Scene: [realistic environment].
Action: [simple ad action: presents product, takes sip, smiles, holds product to camera].
Motion: handheld-but-polished iPhone-style vertical ad, slow push-in, subtle parallax, natural light glints, smooth camera.
Mood: [brand mood].
Avoid distorted hands, warped text, extra fingers, extra people near foreground, surreal product changes, or changing the creator's face.
End frame holds clearly on creator + product.
```

## CALM OS ad prompt that worked especially well

```text
Create a premium 9:16 vertical social ad video from the provided CALM OS™ reference image. Preserve the product identity, premium black-and-gold can, founder-at-desk setting, warm dusk high-rise office, city lights, laptop, notebooks, and sophisticated wellness/productivity mood. Motion direction: slow cinematic push-in from a slightly wider vertical crop, subtle parallax between foreground desk objects and the city skyline, soft rain-or-city-light bokeh outside the windows, tasteful can highlight sweep, tiny condensation glints on the can, founder gives a calm confident micro-smile and gently raises/presents the can. Keep typography clean and legible where possible; avoid warped text. Premium founder wellness ad, calm focus, functional fuel for founders, dark charcoal + warm wood + gold accents, shallow depth of field, polished commercial lighting, smooth camera, no jitter, no distorted hands, no extra people, no surreal changes. End frame holds clearly on the can and brand message.
```

Result:

- Job ID: `697fda4d-3529-4693-8b4f-f1d954e4f961`
- Output file: `/tmp/calm_os_9x16_ad_higgsfield.mp4`

## Oi Ocha + Jet face prompt

```text
Create a premium 9:16 vertical social ad video using two references: Image 1 is the product reference: ITO EN Oi Ocha Unsweetened Green Tea plastic bottle with vivid green label, Japanese characters, ITO EN logo, red Japan's No.1 Green Tea Brand badge. Image 2 is the creator/face reference: use this exact person as the on-camera founder/creator, preserving his face shape, short dark hair, translucent tan glasses, neat mustache/goatee, navy hoodie, calm friendly expression.

Scene: bright modern cafeteria / communal workspace with warm sunlight, wooden tables and benches, clean founder-lifestyle feel. The creator sits at a wooden table and presents the Oi Ocha bottle naturally to camera, then takes a small refreshing sip or gently raises it beside his face. Product label must remain front-facing and readable as much as possible; do not rotate the bottle away from camera. Preserve the green tea bottle shape, label color, cap/open top details, and hand-held scale. Keep identity realistic and flattering.

Motion direction: handheld-but-polished iPhone-style vertical ad, slow push-in, subtle parallax, sunlight glints on plastic bottle, crisp green label pop against neutral cafeteria background, creator gives a calm confident micro-smile. Mood: refreshing, calm focus, clean energy, Japanese green tea break for founders. Avoid distorted hands, warped text, extra fingers, extra people near the foreground, surreal product changes, or changing the creator's face. Premium UGC ad, natural, believable, smooth camera, 10 seconds, end frame holds on creator smiling with product clearly visible.
```

Result:

- Job ID: `5db0adc0-e541-41cf-bf4c-7976080bcdf2`
- Output file: `/tmp/oi_ocha_face_9x16_higgsfield.mp4`

## Implementation script references

Temporary scripts created during testing:

- `/tmp/higgsfield_calm_os_ad_video.py`
- `/tmp/higgsfield_two_ref_ad_video.py`
- `/tmp/higgsfield_generate_video.py`

These scripts implement direct JSON-RPC calls to Higgsfield MCP, upload local images, confirm media, start generation, poll job status, and extract the final MP4 URL.

## Pitfalls / lessons

- The first Higgsfield token was accepted for MCP initialization but rejected by generation calls. Refreshing OAuth through the device flow fixed it.
- The MCP returns `text/event-stream`; parse the `data:` JSON line.
- `media_upload` may redact the presigned URL in the text response, but the structured content contains the usable URL.
- For product ads, explicitly say:
  - keep label front-facing
  - preserve product identity/shape/color
  - avoid warped text
  - avoid distorted hands / extra fingers
  - end frame holds clearly on product
- Higgsfield may internally enhance prompts into UGC style and add an angle lock; this helped product preservation.

## Recommended future uses

- Founder product ads: product photo + Jet selfie/reference.
- Thai creator ads: product photo + Thai-speaking creator prompt.
- Premium supplement/beverage ads: can/bottle front label + office/cafe context.
- Quick ad variants: same reference images, change only scene/action/mood.

## Related future workflow

Jet also asked about using his image to share a Bible verse in Thai. Before interruption, the local reference selfie was confirmed at:

- `/Users/ultrafriday/.hermes/profiles/blaze/image_cache/img_7cfbfd580445.jpg`
- Size: `959 × 1280`

Thai-capable fonts available locally include:

- `/System/Library/Fonts/Supplemental/SukhumvitSet.ttc`
- `/Library/Fonts/Arial Unicode.ttf`

This can be used for a Thai Bible verse graphic overlay workflow.
