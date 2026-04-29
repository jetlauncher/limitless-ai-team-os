# Prompting 101 — Short Course Lesson Plan

**Based on:** Anthropic Applied AI workshop “Prompting 101 | Code w/ Claude”  
**Original video:** https://www.youtube.com/watch?v=ysPbXH0LpIE  
**Prepared for:** Jet / Limitless Club  
**Format:** 60–90 minute teaching session  
**Audience:** founders, operators, educators, creators, and business owners who use AI but want better outputs

## Course Promise

By the end of this short course, students will know how to turn vague requests into structured AI briefs that produce clearer, more useful, more reliable outputs.

## Learning Outcomes

Students will be able to:

1. Explain why vague prompts create weak AI outputs.
2. Use the 8-part prompting framework: **Role → Task → Context → Inputs → Rules → Examples → Output Format → Reminders**.
3. Add domain context so AI does not guess.
4. Use delimiters like XML tags or Markdown sections to separate instructions from data.
5. Define output formats for content, analysis, business workflows, and automation.
6. Improve prompts through testing and iteration.
7. Build a reusable prompt template for their own business.

## Course Structure

### Module 1 — The Real Problem: Briefing, Not Prompting

**Duration:** 10 minutes

**Teaching point:** Most users under-brief the AI. The model may be capable, but it lacks the context and rules needed to perform well.

**Explain:**

- A prompt is not a magic command.
- A prompt is a work brief.
- Treat the AI like a talented but context-blind teammate.
- If you do not provide context, it will infer context — sometimes incorrectly.

**Example:**

Weak:

```text
Write a post about AI agents.
```

Better:

```text
You are a senior content strategist for Limitless Club. Write a premium founder-to-founder Instagram carousel for Thai SME owners explaining how AI agents can remove repetitive operational work. Avoid hype. Make it practical and revenue-oriented.
```

**Student reflection:** What information was missing in the weak version?

---

### Module 2 — Anthropic’s Case Study: Why the First Prompt Failed

**Duration:** 10 minutes

**Teaching point:** In the workshop, Claude was asked to analyze a Swedish accident report and sketch. A simple prompt caused misunderstanding because it lacked domain context.

**Key lesson:** The AI was not “dumb.” It was missing the setup.

**What was missing:**

- What kind of document it was
- What the fields meant
- What markings to look for
- What decision the analysis supported
- How uncertain cases should be handled

**Teaching line:** “When AI fails, first ask: what did I fail to explain?”

---

### Module 3 — The 8-Part Prompting Framework

**Duration:** 20 minutes

Use this as the core framework:

## 1. Role

Who should the AI act as?

Examples:

- Senior content strategist
- CFO analyst
- Legal intake assistant
- Course designer
- Customer research analyst

## 2. Task

What exactly should it produce or decide?

Good tasks are:

- Specific
- Observable
- Outcome-driven
- Easy to evaluate

## 3. Context

What situation is this for?

Include:

- Business context
- Audience context
- Domain rules
- Background details
- Decision criteria

## 4. Inputs

What should the model inspect?

Examples:

- Transcript
- Customer email
- Sales data
- Meeting notes
- Images
- Product brief

Use delimiters:

```xml
<input_data>
Paste source material here.
</input_data>
```

## 5. Rules

How should it behave?

Examples:

- Do not guess.
- Say when uncertain.
- Use only provided evidence.
- Keep tone premium and direct.
- Avoid generic advice.

## 6. Examples

Show what good looks like.

Examples are useful for:

- Tone
- Structure
- Edge cases
- Brand voice
- Judgment calls

## 7. Output Format

Tell the model exactly how to return the answer.

Examples:

- JSON
- Table
- Slide outline
- Carousel script
- Checklist
- Executive memo

## 8. Reminders

Repeat the critical rules at the end.

Examples:

- “Do not invent facts.”
- “Return only the final JSON.”
- “If evidence is missing, say so.”

---

### Module 4 — Prompting for Business Use Cases

**Duration:** 15 minutes

Show students how the framework applies to real business tasks.

## Use Case A — Content Creation

```text
You are my senior content strategist.
Task: Create a 7-slide carousel about [topic].
Audience: [specific audience].
Context: [brand, offer, market].
Rules: Be practical, premium, and non-generic. Avoid hype.
Output: Slide title + body copy + caption + CTA.
```

## Use Case B — Customer Analysis

```text
You are a customer research analyst.
Task: Analyze these customer messages and identify the top pain points, objections, and purchase triggers.
Context: We sell [offer] to [audience].
Rules: Use only the provided messages. Quote evidence.
Output: Table with pain point, evidence, implication, recommended message.
```

## Use Case C — Operations / Automation

```text
You are an operations architect.
Task: Turn this messy workflow into a clean SOP.
Context: This will be used by a small team with limited technical skill.
Rules: Make steps clear, assign owners, identify automation opportunities.
Output: SOP, checklist, automation ideas, risks.
```

---

### Module 5 — Live Exercise: Upgrade a Weak Prompt

**Duration:** 15–25 minutes

Give students this weak prompt:

```text
Help me use AI in my business.
```

Ask them to rewrite it using the framework.

**Worksheet:**

```text
Role:
Task:
Audience / user:
Business context:
Inputs:
Rules:
Examples:
Output format:
Final reminder:
```

**Debrief questions:**

1. What did you add that changed the quality of the answer?
2. Which part was hardest to define?
3. What would you test next?

---

### Module 6 — Prompt QA Checklist

**Duration:** 10 minutes

Before sending an important prompt, check:

- Did I define the role?
- Is the task specific?
- Did I provide enough business/domain context?
- Did I separate inputs from instructions?
- Did I tell it what to avoid?
- Did I include examples if quality/style matters?
- Did I specify the output format?
- Did I repeat the critical rules at the end?
- Can I evaluate whether the answer is good?

---

## Signature Teaching Framework

Call this the **Limitless AI Briefing Stack**:

```text
1. Identity — who the AI is acting as
2. Mission — what outcome it must produce
3. Context — what world it is operating in
4. Evidence — what data it must use
5. Rules — how it must behave
6. References — examples of good/bad
7. Format — how the answer must be delivered
8. Guardrails — what must not happen
```

## Closing Line

“Prompting is not about asking harder. It is about briefing clearer.”

## Homework

Students should take one recurring business task and create a reusable AI brief for it:

- Content calendar
- Customer research
- Sales objection analysis
- Email writing
- SOP creation
- Meeting summary
- Offer improvement

They should test it three times and improve it after each run.
