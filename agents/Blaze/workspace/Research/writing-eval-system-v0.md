# Writing & Thought Eval System — V0

Date: 2026-07-04 11:16 +07
Owner: Blaze

## Objective
Build an evaluation system that scores Jet / Limitless writing and thinking against the best persuasive long-form writing on the internet and the strongest nonfiction/copywriting models.

## Active research tracks
1. Founder/operator long-form writing
   - Anchor: Dario Amodei / Anthropic founder writing, especially `Machines of Loving Grace`.
   - Adjacent models: Paul Graham, Patrick Collison/Stripe, Amazon shareholder letters, 37signals/Basecamp, Ben Horowitz, Eugene Wei.
2. Internet-native persuasive thinkers
   - Anchor: Naval Ravikant / Navalmanack.
   - Anchor: Dan Koe essays/newsletters.
   - Adjacent models: Ben Thompson, Kevin Kelly, Wait But Why, Alex Hormozi long-form, Farnam Street.
3. Books / copywriting canon
   - Current Amazon Nonfiction Best Sellers inspected from Amazon on 2026-07-04 11:16 +07.
   - Classic persuasion/copy books to include even if not current bestsellers: Ogilvy on Advertising, Breakthrough Advertising, Scientific Advertising, Influence, Made to Stick, On Writing Well, Storyworthy, Positioning, The Boron Letters.

## Source observations captured so far

### Dario Amodei — Machines of Loving Grace
URL: https://darioamodei.com/essay/machines-of-loving-grace

Persuasive mechanics:
- Starts by neutralizing the obvious objection: people see Anthropic as risk/doomer; he reframes risk work as the precondition for upside.
- Makes one large promise: radical AI upside may be underestimated.
- Establishes epistemic humility before making bold claims: “educated and useful guesses.”
- Avoids sci-fi abstraction by using concrete domains: biology, neuroscience, poverty, governance, work/meaning.
- Explains why the author has not over-promoted the upside, creating trust before vision.
- Creates moral tension: fear is not enough; people need something to fight for.

Eval criteria derived:
- Objection handling before thesis.
- Big promise with humility.
- Concrete domains instead of abstract optimism.
- Trust-building explanation of incentives.
- A positive moral frame, not just problem agitation.

### Navalmanack
URL: https://www.navalmanack.com/

Persuasive mechanics:
- Compresses complex life/business principles into memorable aphorisms, then expands with interviews/essays.
- Strong modular structure: wealth, judgement, happiness, self, how to live.
- High signal density; low dependency on trends.
- Works because the ideas feel like reusable mental models, not advice spam.

Eval criteria derived:
- Aphoristic compression: can the idea be remembered in one line?
- Mental model durability: will this still matter next year?
- Category clarity: wealth/judgement/happiness/self/work, etc.
- Low fluff, high leverage per sentence.

### Dan Koe
URL: https://thedankoe.com/

Persuasive mechanics:
- Sharp identity-based promises: “Work Less. Earn More. Enjoy Life.”
- Uses contrarian hooks: “You don’t need a niche, you need a point of view”; “Self-discipline is easy, actually.”
- Packages life/business/self-development into a coherent worldview.
- Strong creator-native ladder: free letters → guides/books/tools.

Eval criteria derived:
- Hook inversion: does the piece challenge a default belief?
- Worldview coherence: does it connect tactics to a larger life/business philosophy?
- Clear reader transformation: who does the reader become after believing this?
- Commercial pathway without feeling like pure pitch.

### Amazon Nonfiction Best Sellers — observed top 10
Source: https://www.amazon.com/Best-Sellers-Books-Nonfiction/zgbs/books/53
Observed on: 2026-07-04 11:16 +07; Amazon page title appeared as “Best undefined” and may be region/personality affected.

1. Under the Banner of Heaven — Jon Krakauer
2. Story of the World, Vol. 2 — Susan Wise Bauer
3. Orientalism — Edward W. Said
4. Discipline and Punish — Michel Foucault
5. The Shock Doctrine — Naomi Klein
6. The Black Swan — Nassim Nicholas Taleb
7. Republic — Plato
8. We Wish to Inform You That Tomorrow We Will be Killed With Our Families — Philip Gourevitch
9. Propaganda: The Formation of Men's Attitudes — Jacques Ellul
10. The Foucault Reader — Michel Foucault

Implication for eval design:
- Current nonfiction demand is not only “business tips”; it rewards worldview, power analysis, narrative evidence, controversial framing, and enduring conceptual tools.

## V0 scoring system
Score every draft 1–5 on each dimension.

### 1. Thesis power
Question: Is there one large promise or claim worth reading for?
- 1 = vague topic
- 3 = clear claim
- 5 = high-stakes, memorable, commercially or philosophically useful claim

### 2. Reader tension
Question: Does the piece name a real belief conflict, pain, opportunity, or status anxiety?
- 1 = no tension
- 3 = recognizable problem
- 5 = urgent contradiction the reader feels in their business/life

### 3. Objection handling
Question: Does it anticipate the smart reader’s resistance?
- 1 = ignores objections
- 3 = mentions objections
- 5 = reframes objections into trust and deeper authority

### 4. Concrete evidence
Question: Does it use proof, scenes, examples, numbers, source signals, or lived operator context?
- 1 = claims only
- 3 = some examples
- 5 = vivid proof that makes the idea hard to dismiss

### 5. Mental model value
Question: Does it give the reader a reusable frame?
- 1 = advice
- 3 = useful framework
- 5 = a concept they can use to make future decisions

### 6. Compression and memorability
Question: Can the core idea be repeated in one sentence?
- 1 = rambling
- 3 = understandable
- 5 = sticky aphorism / named frame / quotable line

### 7. Worldview coherence
Question: Does this piece fit Jet’s larger point of view: Founder AI OS, leverage, execution, premium operators?
- 1 = isolated post
- 3 = fits the brand
- 5 = strengthens a compounding body of thought

### 8. Commercial usefulness
Question: Does it move a founder/operator toward a better decision, purchase belief, or behavior?
- 1 = interesting only
- 3 = actionable
- 5 = changes priorities and increases buying readiness

### 9. Voice authority
Question: Does it sound like a premium founder/operator, not generic AI content?
- 1 = AI slop
- 3 = competent
- 5 = sharp, warm, specific, trusted

### 10. Ending / action path
Question: Does it land with a clear implication, CTA, or decision?
- 1 = fizzles
- 3 = clear conclusion
- 5 = reader knows exactly what to think/do next

## Output rubric
- 45–50 = Publish / flagship quality
- 38–44 = Strong, edit for precision
- 30–37 = Useful draft, needs sharper proof or thesis
- 20–29 = Generic; rebuild from reader tension
- <20 = Do not publish

## Recommended next artifact
Create a reusable evaluator prompt/template that accepts:
1. Draft text
2. Intended platform
3. Audience
4. Desired outcome
5. Source/style model to compare against

And returns:
- scorecard
- strongest sentence
- weakest sentence
- missing proof
- rewrite direction
- 3 stronger hooks
- publish/no-publish recommendation
