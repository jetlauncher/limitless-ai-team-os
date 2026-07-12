# Limitless Writing & Thought Eval System — V1

Date: 2026-07-04 11:20 +07
Owner: Blaze
Status: Working spec after 3-subagent research fan-out

## Objective

Build an evaluation system that judges Jet / Limitless writing and raw thinking against the best persuasive long-form writing online, the strongest founder/operator essays, and the most durable nonfiction/copywriting principles.

This is not a grammar checker. It is a **taste + persuasion + thought-quality evaluator**.

It should answer:

1. Is this idea worth publishing?
2. Is the thinking sharp enough?
3. Is the writing persuasive enough?
4. Does it compound Jet’s Founder AI OS / premium operator worldview?
5. What must change before it becomes flagship-quality?

---

## Source corpus map

### Tier 1 — Must-study founder/operator writing

| Rank | Source | URL | Why it matters | Eval principle to steal |
|---:|---|---|---|---|
| 1 | Dario Amodei — *Machines of Loving Grace* | https://darioamodei.com/essay/machines-of-loving-grace | High-stakes AI vision that avoids both doom and hype | Bold positive vision + objection handling + calibrated humility |
| 2 | Anthropic — *Core Views on AI Safety* | https://www.anthropic.com/news/core-views-on-ai-safety | Institutional worldview made legible | Beliefs separated from uncertainties; principle-to-strategy linkage |
| 3 | Anthropic — *Responsible Scaling Policy* | https://www.anthropic.com/news/responsible-scaling-policy | Values translated into operating thresholds | Ethics become gates, triggers, and behavioral commitments |
| 4 | Paul Graham — *Do Things That Don’t Scale* | https://www.paulgraham.com/ds.html | Classic counterintuitive founder advice | One sticky phrase overturns a false assumption |
| 5 | Paul Graham — *Ramen Profitable* | https://www.paulgraham.com/ramenprofitable.html | Names an unarticulated founder state | New category = new decision tool |
| 6 | Bezos — Amazon 1997 Shareholder Letter | https://www.aboutamazon.com/news/company-news/amazon-1997-letter-to-shareholders | Selects for aligned long-term investors | Tradeoffs named before criticism arrives |
| 7 | Bezos — 2016 “Day 1” Letter | https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders | Culture as operating doctrine | Memorable metaphor + decision heuristics |
| 8 | Patrick Collison — *Fast* | https://patrickcollison.com/fast | Evidence-wall persuasion against learned helplessness | Many examples let the reader infer the argument |
| 9 | Patrick Collison — *Questions* | https://patrickcollison.com/questions | Shows intellectual taste through questions | Evaluating thought means evaluating question quality |
| 10 | Basecamp — *Shape Up* | https://basecamp.com/shapeup | Complete operator doctrine | Named system + precise terms + implementable rituals |
| 11 | 37signals / Jason Fried / DHH | https://world.hey.com/jason | Anti-consensus values-driven operator writing | Clear enemy + refusal + company philosophy |
| 12 | Brian Chesky — *Don’t Fuck Up the Culture* | https://medium.com/@bchesky/dont-fuck-up-the-culture-597cde9ee9d4 | Culture as strategic asset | Founder vulnerability + standard setting |
| 13 | Ben Horowitz — *Good Product Manager / Bad Product Manager* | https://a16z.com/good-product-manager-bad-product-manager/ | Brutal standard-setting via contrast | Good X / Bad X makes excellence unmistakable |
| 14 | Netflix Culture | https://jobs.netflix.com/culture | One of the strongest operator culture artifacts | Values translated into selection/filtering behavior |
| 15 | Sam Altman — *The Days Are Long But the Decades Are Short* | https://blog.samaltman.com/the-days-are-long-but-the-decades-are-short | Aphoristic ambition + life strategy | Earned maxims, not generic advice |

### Tier 2 — Must-study internet-native thinkers

| Source | Canonical works | What to steal |
|---|---|---|
| Naval Ravikant | https://nav.al/rich, https://www.navalmanack.com/ | Aphoristic compression, hidden distinctions, durable principles, leverage mental models |
| Dan Koe | https://thedankoe.com/ | Identity transformation, contrarian hooks, creator-business worldview; use with fluff filter |
| Alex Hormozi | https://www.acquisition.com/books | Equations, offer mechanics, measurable action, commercial specificity |
| Ben Thompson / Stratechery | https://stratechery.com/concept/aggregation-theory/ | Market-structure frameworks, incentives, value accrual, strategic prediction |
| Eugene Wei | https://www.eugenewei.com/blog/2019/2/19/status-as-a-service | Product/social-status causality, concept naming, long causal chains |
| Kevin Kelly | https://kk.org/thetechnium/1000-true-fans/ | Simple threshold concepts, creator economics, optimistic plausibility |
| Wait But Why | https://waitbutwhy.com/ | Long-form explanatory persuasion, analogy, humor, visual mental models |
| Lenny Rachitsky | https://www.lennysnewsletter.com/ | Product/growth operator usefulness |
| Packy McCormick | https://www.notboring.co/ | Narrative business synthesis |
| Byrne Hobart | https://www.thediff.co/ | Strategic/financial cognition |

### Tier 3 — Evergreen book/copywriting canon

| Book | Author | What it contributes to the evaluator |
|---|---|---|
| *On Writing Well* | William Zinsser | Clarity, economy, humane voice, nonfiction discipline |
| *Ogilvy on Advertising* | David Ogilvy | Concrete promise, proof, reader respect, sales discipline |
| *Made to Stick* | Chip & Dan Heath | Simple, unexpected, concrete, credible, emotional, stories |
| *The Elements of Style* | Strunk & White | Sentence-level discipline, concision, structure |
| *Storyworthy* | Matthew Dicks | Stakes, moment of change, narrative payoff |
| *Thinking, Fast and Slow* | Daniel Kahneman | Bias detection, assumption checking, uncertainty |
| *Influence* | Robert Cialdini | Ethical persuasion psychology |
| *The Pyramid Principle* | Barbara Minto | Executive structure, logical hierarchy |
| *Good Strategy Bad Strategy* | Richard Rumelt | Diagnosis, guiding policy, coherent action |
| *Poor Charlie’s Almanack* | Charlie Munger | Multidisciplinary models, incentives, inversion |
| *Breakthrough Advertising* | Eugene Schwartz | Market sophistication, desire, mechanism, differentiation |
| *Tested Advertising Methods* | John Caples | Benefit-led headlines, testability, conversion logic |
| *The Boron Letters* | Gary Halbert | Conversational force, audience hunger, momentum |
| *Positioning* | Ries & Trout | Category ownership, mental availability, differentiation |
| *Contagious* | Jonah Berger | Shareability, triggers, social currency, practical value |

---

## Current Amazon nonfiction top 10 observed

Source inspected directly with browser: https://www.amazon.com/Best-Sellers-Books-Nonfiction/zgbs/books/53

Observed: 2026-07-04 11:16 +07. Caveat: Amazon page title appeared as “Best undefined” and ranking may be region/personality affected.

1. *Under the Banner of Heaven* — Jon Krakauer
2. *Story of the World, Vol. 2* — Susan Wise Bauer
3. *Orientalism* — Edward W. Said
4. *Discipline and Punish* — Michel Foucault
5. *The Shock Doctrine* — Naomi Klein
6. *The Black Swan* — Nassim Nicholas Taleb
7. *Republic* — Plato
8. *We Wish to Inform You That Tomorrow We Will be Killed With Our Families* — Philip Gourevitch
9. *Propaganda: The Formation of Men's Attitudes* — Jacques Ellul
10. *The Foucault Reader* — Michel Foucault

### Implication

The visible nonfiction market rewards more than tactics. It rewards:

- worldview
- power analysis
- controversial frames
- narrative evidence
- structural explanation
- durable concepts
- social/political/philosophical stakes

So the Limitless evaluator should not only ask “is this useful?” It must also ask: **does this explain power, incentives, human behavior, and decision-making better than the reader currently does?**

---

## The master rubric

Score each dimension 1–5. Weighted score totals 100.

| # | Dimension | Weight | Core question |
|---:|---|---:|---|
| 1 | Thesis Power | 10% | Is there one large claim/promise worth reading? |
| 2 | Non-obvious Insight | 9% | Does it say something beyond conventional advice? |
| 3 | Reader Tension | 8% | Does it name a real conflict, fear, desire, or opportunity? |
| 4 | Mechanistic Clarity | 10% | Does it explain how/why the claim works? |
| 5 | Evidence & Concreteness | 10% | Are claims grounded in examples, proof, scenes, numbers, or operator context? |
| 6 | Strategic / Founder Usefulness | 10% | Would this improve a founder/operator decision? |
| 7 | Objection & Tradeoff Handling | 8% | Does it handle smart resistance and name costs? |
| 8 | Concept Portability | 8% | Is there a memorable phrase, frame, contrast, or model? |
| 9 | Worldview Coherence | 7% | Does it compound Jet’s broader Founder AI OS / premium operator POV? |
| 10 | Persuasive Force | 7% | Does it move belief or action ethically? |
| 11 | Voice Authority | 6% | Does it sound earned, specific, premium, and human? |
| 12 | Ending / Action Path | 4% | Does it land with a clear implication, decision, or CTA? |
| 13 | Narrative / Emotional Resonance | 3% | Does it create stakes, movement, or emotional payoff? |

### Score bands

| Score | Verdict | Meaning |
|---:|---|---|
| 90–100 | Flagship | Publish / build campaign around it |
| 80–89 | Strong | Publish after precision edit |
| 70–79 | Useful | Good idea, but needs sharper proof, structure, or hook |
| 60–69 | Mid | Rebuild the thesis or make it more concrete |
| 40–59 | Weak | Generic, under-supported, or unclear |
| <40 | Kill / restart | Not worth publishing in current form |

---

## Dimension definitions

### 1. Thesis Power
Question: Is there one large claim or promise worth reading for?

- 1 = vague topic
- 3 = clear claim but low stakes
- 5 = high-stakes, memorable, commercially/philosophically useful claim

Modeled by: Dario, PG, Bezos, Rumelt, Ogilvy.

### 2. Non-obvious Insight
Question: Does this reveal something the reader does not already believe?

- 1 = obvious advice
- 3 = familiar idea with decent framing
- 5 = changes the reader’s categories or assumptions

Modeled by: Naval, Ben Thompson, Eugene Wei, Taleb, Foucault/Said-style power analysis.

### 3. Reader Tension
Question: Does the piece begin from a real contradiction?

Good tension examples:
- “Everyone wants AI leverage, but most companies are just buying tools, not redesigning work.”
- “Founders want scale, but early companies win by doing unscalable things.”
- “AI feels like a productivity tool, but the real unlock is a new management layer.”

- 1 = no tension
- 3 = recognizable problem
- 5 = urgent contradiction the reader feels in business/life

### 4. Mechanistic Clarity
Question: Does it explain the causal engine?

Bad: “AI will change every business.”
Good: “AI changes businesses when recurring decisions become structured workflows with memory, tools, permissions, and feedback loops.”

- 1 = slogans
- 3 = basic explanation
- 5 = clear mechanism, constraints, examples, and second-order effects

### 5. Evidence & Concreteness
Question: Are claims grounded?

Evidence can be:
- specific owner scene
- case study
- mechanism
- source signal
- numbers
- before/after
- operating detail
- named example

- 1 = claims only
- 3 = some examples
- 5 = vivid, credible, hard to dismiss

### 6. Strategic / Founder Usefulness
Question: Would this change what a founder/operator does?

Decision categories:
- positioning
- product
- pricing
- hiring
- distribution
- AI workflow design
- delegation
- offer architecture
- operating cadence
- capital/time allocation

- 1 = interesting only
- 3 = somewhat actionable
- 5 = changes priorities or behavior

### 7. Objection & Tradeoff Handling
Question: Does it anticipate smart resistance?

Modeled by Anthropic and Bezos.

- 1 = ignores objections
- 3 = mentions objections
- 5 = turns objections into trust; names what is sacrificed

### 8. Concept Portability
Question: Can the idea travel?

Portable concepts:
- Day 1
- Ramen profitable
- Do things that don’t scale
- Aggregation Theory
- Status as a Service
- 1,000 True Fans
- Founder AI OS
- 10-80-10
- CLEAR

- 1 = no memorable handle
- 3 = understandable but not sticky
- 5 = named, repeatable, useful without the whole essay

### 9. Worldview Coherence
Question: Does it strengthen Jet’s body of thought?

Jet/Limitless worldview anchors:
- Founder AI OS
- premium operator leverage
- AI staff / Chief of Staff
- concrete owner scenes
- 10-80-10 delegation
- CLEAR execution
- KOI thinking
- business transformation over tool novelty

- 1 = isolated content
- 3 = fits the brand
- 5 = compounds a larger doctrine

### 10. Persuasive Force
Question: Does it move belief or action?

- 1 = inert
- 3 = convincing enough
- 5 = compelling, ethical, clear, and commercially useful

### 11. Voice Authority
Question: Does it sound like earned belief?

Penalize:
- AI slop
- generic founder clichés
- guru posture
- vague sovereignty language
- fake contrarianism
- over-polished LinkedIn tone

Reward:
- specificity
- warmth
- restraint
- crispness
- commercial usefulness
- owner/operator realism

### 12. Ending / Action Path
Question: Does the piece land?

Strong endings:
- tell the reader what to stop doing
- name the decision
- introduce the CTA
- create a memorable final contrast
- turn the idea into next action

### 13. Narrative / Emotional Resonance
Question: Does the piece create stakes or movement?

Good writing does not only instruct. It makes the reader feel the cost of staying the same.

---

## Additional specialized checks

### Anthropic-style calibrated ambition check
Use for AI/future/vision pieces.

Score 1–5:
- bold positive vision
- risk integration
- explicit uncertainty
- concrete domains
- moral seriousness
- principle-to-process linkage

### Naval-style compression check
Use for thought leadership and X/short essays.

Score 1–5:
- one-line memorability
- hidden distinction
- long-term durability
- founder decision utility
- low fluff

### Dan Koe-style identity transformation check
Use for creator/founder lifestyle pieces.

Score 1–5:
- contrarian hook
- reader identity shift
- executable path
- worldview coherence
- avoids vague “escape the matrix” motivation

### Hormozi-style commercial action check
Use for offers, launch copy, sales content.

Score 1–5:
- clear promise
- measurable outcome
- mechanism
- audience hunger
- offer clarity
- reason to act now

### Stratechery/Eugene Wei-style strategy check
Use for market/AI/business analysis.

Score 1–5:
- incentive analysis
- value accrual
- causal depth
- market structure
- predictive usefulness
- named framework

---

## Red flags / auto-penalties

Subtract points for:

- Generic AI-tool recap with no owner implication
- High-agency language without mechanism
- “Everyone should…” claims without audience specificity
- Fake contrarian hook that resolves to obvious advice
- No proof, no example, no scene
- Overclaiming without caveats
- Good vibes instead of tradeoffs
- Unclear reader or desired behavior
- Jargon that hides weak thinking
- Ending that does not change belief/action

---

## Evaluator output format

Every eval should return:

1. **Overall score / 100**
2. **Publish verdict**
3. **Dimension score table**
4. **One-sentence diagnosis**
5. **Strongest line**
6. **Weakest line**
7. **Missing proof or mechanism**
8. **Best source model to emulate**
9. **Three stronger hooks**
10. **Rewrite direction**
11. **If applicable: rewritten version**

---

## Recommended source-model mapping

| If the draft is… | Compare against… |
|---|---|
| AI future / AI worldview | Dario / Anthropic |
| Founder lesson | Paul Graham / Bezos |
| Operator doctrine | Shape Up / Amazon letters / Netflix culture |
| Market structure analysis | Ben Thompson / Eugene Wei |
| Creator leverage / internet work | Naval / Kevin Kelly / Dan Koe |
| Offer / launch / sales copy | Ogilvy / Schwartz / Hormozi / Caples |
| Narrative essay | Wait But Why / Storyworthy / Krakauer |
| Short sharp thought | Naval / Sam Altman |
| Strategic diagnosis | Rumelt / Munger / Taleb |

---

## Next build step

Turn this into a reusable prompt and, later, a lightweight scoring workflow:

1. Paste raw draft or idea.
2. Select mode: `post`, `essay`, `sales`, `strategy`, `raw thought`.
3. Select source model: `Dario`, `Naval`, `PG`, `Ogilvy`, etc.
4. Evaluator scores and rewrites.
5. Blaze decides whether it is publishable.

