# Prompting 101: How to Brief AI Like a Pro

A short course based on Anthropic's Applied AI workshop

**Teaching promise:** By the end, students can turn vague AI requests into structured prompts that get reliable, high-quality outputs.

---

# Slide 1 — The Big Idea

Most people do not have an AI problem.

They have a **briefing problem**.

If you brief the model like an intern, you get intern-quality work.  
If you brief it like a senior operator, you get strategic work.

**Speaker notes:** Open with the core reframing. Prompting is not magic words. It is structured communication.

---

# Slide 2 — What Anthropic Demonstrated

Anthropic's Applied AI team used a real-world style task:

- Analyze a Swedish car accident claim
- Read an accident form and a hand-drawn sketch
- Determine what happened and who may be at fault

The first simple prompt failed because Claude lacked context.

**Speaker notes:** The model was capable, but under-briefed. It initially misunderstood the domain because the prompt did not set the scene clearly.

---

# Slide 3 — Prompting Is Empirical

A prompt is not “one and done.”

It is an iterative system:

1. Try the prompt
2. Observe the failure mode
3. Add missing context or rules
4. Test again
5. Keep improving until reliable

**Speaker notes:** Teach students to treat prompting like product testing, not like guessing the perfect sentence.

---

# Slide 4 — The Master Framework

A great prompt is a complete brief:

**Role → Task → Context → Inputs → Rules → Examples → Output Format → Reminders**

Most people only provide the task.

That is why the result feels generic, incomplete, or unreliable.

---

# Slide 5 — Element 1: Role

Tell the model who it should act as.

Weak:

> Help me write content.

Strong:

> You are my senior content strategist for Limitless Club, advising Thai founders and business owners.

**Why it works:** Role narrows the model's lens and standards.

---

# Slide 6 — Element 2: Task

Define the exact job and success outcome.

Weak:

> Analyze this.

Strong:

> Review the claim documents, identify the factual sequence of events, and determine whether Vehicle A or Vehicle B appears more responsible.

**Speaker notes:** The task should be concrete enough that the answer can be judged.

---

# Slide 7 — Element 3: Context

Claude performs better when it understands the situation.

Include:

- Business context
- Audience context
- Domain definitions
- Relevant rules
- What the input means
- What decision the answer supports

**Speaker notes:** Context prevents the model from filling gaps with assumptions.

---

# Slide 8 — Element 4: Inputs

Separate the data from the instructions.

Use clear delimiters:

```xml
<context>
Domain rules go here.
</context>

<input_data>
Customer email / transcript / report / notes go here.
</input_data>
```

**Speaker notes:** Anthropic specifically highlighted XML tags and Markdown as useful ways to organize information for Claude.

---

# Slide 9 — Element 5: Rules

Tell the model how to behave.

Examples:

- Stay factual
- Do not guess if uncertain
- Base conclusions only on provided evidence
- State ambiguity clearly
- Prioritize accuracy over confidence

**Speaker notes:** Rules protect against hallucination and overconfident answers.

---

# Slide 10 — Element 6: Step-by-Step Instructions

Do not just ask for the output.

Give the process:

1. Identify key facts
2. Compare facts against context/rules
3. Note uncertainty or missing information
4. Produce final answer
5. Format cleanly

**Speaker notes:** This helps the model organize its work before producing the final response.

---

# Slide 11 — Element 7: Examples

Examples teach the model what “good” looks like.

Use examples when:

- The task is subjective
- The output style matters
- There are edge cases
- You need consistency at scale

**Speaker notes:** Anthropic noted that in production you may use many examples, especially difficult gray-area examples.

---

# Slide 12 — Element 8: Conversation History

For user-facing AI, include relevant history.

Useful history:

- User preferences
- Prior decisions
- Earlier conversation turns
- Known constraints
- Repeated corrections

**Speaker notes:** This is especially important for AI agents and assistants. Memory/context makes the model more useful.

---

# Slide 13 — Element 9: Output Format

If you care about usability, specify the output.

Examples:

```json
{
  "summary": "...",
  "confidence": "high | medium | low",
  "evidence": ["..."],
  "final_answer": "..."
}
```

Or:

- Slide title
- 3 bullet points
- Speaker notes
- CTA

**Speaker notes:** Output format turns a model response into something useful for workflows, databases, slides, posts, or apps.

---

# Slide 14 — Element 10: Reminders

Repeat the critical rules at the end.

Why?

The end of the prompt is close to where the model starts answering.

Use reminders like:

- Do not invent facts
- If uncertain, say “uncertain”
- Use only the provided evidence
- Return only the requested format

---

# Slide 15 — Before / After Prompt

## Weak prompt

> Make me a carousel about AI agents.

## Strong prompt

> You are my senior content strategist for Limitless Club. Create a 7-slide premium carousel for Thai founders about AI agents. Make it practical, founder-to-founder, not hype. Include one sharp headline per slide, one supporting sentence, and a CTA to DM “AGENT”.

---

# Slide 16 — The Limitless Prompt Formula

For Jet's ecosystem, use this:

```text
You are [expert role] for Limitless Club.
Task: [specific output].
Audience: [who this is for].
Context: [business/product/situation].
Inputs: [data/content/links].
Rules: [tone, constraints, what to avoid].
Examples: [what good looks like].
Output format: [exact structure].
Reminder: [critical rules].
```

---

# Slide 17 — Student Exercise

Take this weak prompt:

> Help me use AI in my business.

Rewrite it using:

1. Role
2. Task
3. Context
4. Inputs
5. Rules
6. Output format

**Group discussion:** What changed? What answer would now become possible?

---

# Slide 18 — Final Takeaway

Prompting is not about clever wording.

It is about giving AI enough structure to succeed.

**The better the brief, the better the work.**

Remember:

**Role → Task → Context → Inputs → Rules → Examples → Output Format → Reminders**
