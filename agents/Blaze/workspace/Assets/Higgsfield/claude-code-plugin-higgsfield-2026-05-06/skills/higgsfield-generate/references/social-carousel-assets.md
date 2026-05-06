# Social carousel / graphics asset workflow

Use this when Higgsfield is used to create Instagram carousel slides, X covers, thumbnails, or other text-heavy social graphics.

## Learned workflow

1. **Prefer GPT Image 2 for premium graphic design.** It works well for editorial social slides, banners, typography-led layouts, and luxury brand visuals.
2. **Check the model schema before choosing dimensions.** Example: `gpt_image_2` supports `1:1`, `4:3`, `3:4`, `16:9`, `9:16`, `3:2`, `2:3`; it may not support Instagram `4:5` directly.
3. **Generate at closest supported aspect ratio, then post-process deterministically.** For IG carousel `1080x1350` (4:5), generate `3:4` at high/2k, then crop/resize locally to exact 4:5.
4. **Use `--wait --json` for pipeline work.** Save the job JSON beside the asset so the result URL, prompt, model, and dimensions are recoverable without exposing credentials.
5. **Download with `curl` for reliability.** Python `urllib.request.urlretrieve` may hang/time out on some CDN downloads; use `curl --max-time 180 --retry 2 -L`.
6. **Always QA text-heavy images with vision before delivery.** Confirm spelling, readability, contrast, and brand fit. AI-generated text can look premium but have small or garbled handles.
7. **For final/production carousels, separate visual generation from text precision.** Use Higgsfield for background/visual direction, then overlay exact text locally when brand handles, Thai text, or small labels must be perfect.

## Example: Higgsfield slide → exact IG carousel JPEG

```bash
ASSET_DIR="$HOME/Documents/Obsidian Vault/Agents/Blaze/Assets/Higgsfield/carousel-slide-test-$(date +%F)"
mkdir -p "$ASSET_DIR"

PROMPT='Create a premium Instagram carousel slide for Limitless Club in a Midnight Luxe Editorial style. Portrait 3:4 composition, black charcoal graphite background, subtle silver gridlines, editorial serif typography, clean sans supporting text, high negative space, luxury founder-media feel. Exact readable text only: Header at top: "Limitless Club". Main headline: "AI IS NOT THE ADVANTAGE". Subheadline: "The workflow around it is." Footer handle: "@jeditrinupab". No extra words, no fake logos, no watermark, no misspellings. Minimal, elegant, mobile-readable, premium.'

higgsfield generate create gpt_image_2 \
  --prompt "$PROMPT" \
  --aspect_ratio 3:4 \
  --resolution 2k \
  --quality high \
  --wait \
  --wait-timeout 20m \
  --json > "$ASSET_DIR/job.json"

URL=$(python3 - <<'PY' "$ASSET_DIR/job.json"
import json, sys
obj=json.load(open(sys.argv[1]))
print(obj[0].get('result_url',''))
PY
)

curl --max-time 180 --retry 2 -L "$URL" -o "$ASSET_DIR/raw.png"

python3 - <<'PY' "$ASSET_DIR/raw.png" "$ASSET_DIR/final-1080x1350.jpg"
from PIL import Image
import sys
src, dst = sys.argv[1:]
im = Image.open(src).convert('RGB')
w,h = im.size
target = 4/5
cur = w/h
if cur > target:
    nw = int(h*target)
    left = (w-nw)//2
    im = im.crop((left,0,left+nw,h))
else:
    nh = int(w/target)
    top = (h-nh)//2
    im = im.crop((0,top,w,top+nh))
im = im.resize((1080,1350), Image.LANCZOS)
im.save(dst, quality=95, optimize=True)
PY
```

## Delivery notes

- In Telegram, send finished media as `MEDIA:/absolute/path/to/file`.
- Mention QA issues briefly: e.g. “handle is small; for final I’d overlay it locally.”
- Keep raw output, final asset, and job metadata in a durable asset folder for reuse.

## Pitfalls

- Foreground terminal calls may cap at 600 seconds. If a generation needs longer, run it as a background command with notification or use a shorter foreground timeout.
- Do not print auth headers, account email, tokens, or signed/private URLs in user-facing summaries.
- `gpt_image_2` may return job metadata with an internal model/job_set label that differs from the submitted ID; trust the completed result and saved JSON unless the API reports an error.
