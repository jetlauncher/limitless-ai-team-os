# Qwen 3.8 OpenRouter Fleet Cost Projection

**Audit date:** 2026-08-22 (+07)

## Executive answer

For a full-fleet swap to **Qwen3.8 Max** (`qwen/qwen3.8-max`), budget against the raw-ledger peak rather than the smaller `hermes insights` view:

- **Peak 31-day API cost with recorded cache behavior:** **$3,915.97**
- **OpenRouter credit-purchase fee (5.5%):** **$215.38**
- **Hostinger KVM2:** **$12.00**
- **Peak all-in monthly budget:** **$4,143.35** (about **฿140,874** at ฿34/USD)
- **No-cache failure ceiling:** **$6,722.25 all-in** (about **฿228,557**)

Current trailing 31-day pace is lower: **$2,644.57 all-in** with the recorded cache mix.

## Model prices verified on OpenRouter

### Qwen3.8 Max — flagship
- Model: `qwen/qwen3.8-max`
- Released: 2026-08-03
- Context: 1M
- Input: **$2.00/M tokens**
- Output: **$6.00/M tokens**
- Cache read: **$0.25/M tokens**
- Cache create/write: **$2.50/M tokens**
- Source: https://openrouter.ai/qwen/qwen3.8-max

### Qwen3.8 27B — newest release in the 3.8 family
- Model: `qwen/qwen3.8-27b`
- Released: 2026-08-14
- Context: 1M
- Headline price: **$0.40/M input, $3.00/M output**
- Cache read varies by provider (as low as **$0.04/M** on the listed Chutes route; $0.15/M on CoreWeave)
- Source: https://openrouter.ai/qwen/qwen3.8-27b

OpenRouter's FAQ states a **5.5% fee ($0.80 minimum)** when purchasing credits: https://openrouter.ai/docs/faq#pricing-and-fees

## Log audit scope and method

Audited 13 Hermes state databases:
- default, blaze, bolt, jekjack, kaijeaw, oracle, pixel, protocol, qwen, signal, tiff, unclechris, zegna
- Data coverage: **2026-04-22 through 2026-08-22**
- Raw `session_model_usage` rows: **21,377**
- Deduplicated rows: **20,964**
- Copied-profile history rows removed: **413**

Deduplication key: `(session_id, model, billing_provider, task)`, retaining the largest cumulative usage row and preferring a currently indexed session on ties.

Hermes token accounting was separated into input, output, cache-read, and cache-write categories. Reasoning tokens were not charged separately because they are part of model output accounting.

## Highest observed 31-day usage

**Window:** 2026-07-04 through 2026-08-03

| Token class | Tokens |
|---|---:|
| Input | 1,666,842,263 |
| Output | 29,296,445 |
| Cache read | 1,403,200,022 |
| Cache write | 22,283,391 |
| Total recorded | 3,121,622,121 |

Qwen3.8 Max calculation:
- Input: 1,666.842263M × $2.00 = $3,333.68
- Output: 29.296445M × $6.00 = $175.78
- Cache read: 1,403.200022M × $0.25 = $350.80
- Cache write: 22.283391M × $2.50 = $55.71
- **API subtotal: $3,915.97**
- OpenRouter 5.5% credit fee: $215.38
- Hostinger: $12.00
- **All-in: $4,143.35**

### Why this is higher than `hermes insights`

The raw usage ledger contains valid historical usage rows whose parent session records were later removed or are no longer indexed. `hermes insights` inner-joins usage to surviving sessions and therefore omits those rows. The session-indexed-only 31-day view is:

- Input: 137,350,477
- Output: 4,354,570
- Cache read: 652,863,286
- Qwen3.8 Max all-in with fee + host: **$501.63**

That is a useful lower bound, but not safe as the fleet budget ceiling. The recommended planning number is the raw-ledger peak **$4.15K/month**, with **$6.75K/month** as a rounded no-cache reserve.

## Alternative if “latest” means Qwen3.8 27B

Using the cheapest listed cache-capable route ($0.40/M input, $3/M output, $0.04/M cache read), plus 5.5% fee and $12 hosting:

- Peak raw-ledger all-in: **$876.75/month** (about **฿29,809**)
- No-cache all-in ceiling: **$1,409.68/month** (about **฿47,929**)
- Provider routing can raise the cached figure; a practical rounded budget is **$900–$1,100/month**, or **$1,450/month** with no-cache reserve.

## Recommendation

Do not send the entire fleet to Qwen3.8 Max without a spend cap. Safer rollout:
1. Pin high-volume low-stakes cron/worker traffic to **Qwen3.8 27B**.
2. Keep **Qwen3.8 Max** for Kelly, complex reasoning, and high-value agent runs.
3. Set an OpenRouter monthly cap and alert at 50% / 75% / 90%.
4. Run a 7-day parallel pilot to verify cache-read reporting and tool-call reliability before fleet-wide routing.

## Planning caveats

- The $12 Hostinger figure is user-provided and treated as fixed.
- THB uses the planning rate ฿34/USD, not a card-statement conversion.
- OpenRouter provider selection can change effective 27B pricing.
- Cache persistence across a provider/model swap must be verified; the no-cache ceiling exists for that reason.
- This is a usage projection, not a provider invoice reconciliation.
