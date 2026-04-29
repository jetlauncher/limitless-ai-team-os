# Prompting 101 — Limitless Club Short Course Pack

## Files in this pack

1. `Prompting_101_Gamma_Deck.md` — copy/paste/import into Gamma.
2. `Prompting_101_Lesson_Plan.md` — facilitator lesson plan.
3. Transcript appendix below.

---

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


---

# Gamma Deck Import Markdown

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


---

# Transcript Appendix



## Chunk chunk_000
Hi everyone, thank you for joining us today for Prompting 101. My name is Hannah. I'm part of the Applied AI team here at Anthropic, and with me is Christian, also part of the Applied AI team. And what we're going to do today is take you through a little bit of prompting best practices, and we're going to use a real-world scenario and build up a prompt together. So a little bit about what prompt engineering is. Prompt engineering, you're all probably a little bit familiar with this. This is the way that we communicate with a language model and try to get it to do what we want. So this is the practice of writing clear instructions for the model, giving the model the context that it needs to complete the task, and thinking through how we want to arrange that information in order to get the best result. So there's a lot of detail here, a lot of different ways you might want to think about building out a prompt. And as always, the best way to learn this is just to practice doing it. So today, we're going to go through a hands-on scenario. We're going to use an example inspired by a real customer that we worked with. So we've modified what the actual customer asked us to do, but this is a really interesting case of trying to analyze some images and get factual information out of the images and have Claude make a judgment about what content it finds there. And I actually do not speak the language that this content is in, but luckily Christian and Claude both do. So I'm going to pass it over to Christian to talk about the scenario and the content. So for this example that we have here, it's intended, so to set the stage, imagine you're working for a Swedish insurance company and you deal with car insurance claims on a daily manner. And the purpose of this is that you have two pieces of information. We're going through these in detail as well, but visually you can see on the left-hand side, we have a car accident report form just detailing out what transpired before the accident actually took place. And then finally, we have a sort of human drawn sketch of how the accident took place as well. So these two pieces of information is what we're going to try to pass on to Claude. And to begin with, we can just take these two and throw them into a console and just see what happens. So if we transition over to our console as well, we can actually do this in a real manner. And in this case here, you can see we have our shiny, beautiful Anthropic console. We're using the new Claude for solid model as well. In this case, setting temperature to zero and having a huge max token budget as well, just helping us make sure that there's no limitations to what Claude can do. In this case, you can see we have a very simple prompt just setting the stage of what Claude is supposed to do. In this case, mentioning that this is intended to review an accident report form and eventually also determine what happened in the accident and who's at fault. So you can see here with this very simple prompt, if I just run this, let me go to preview, we can see here that Claude thinks that this is in relation to a skiing accident that happened on a street called Shafamangatan. It's a very common street in Sweden. And in many ways, you can sort of understand this innocent mistake in the sense that in our prompt, we actually haven't done anything to set the stage on what is actually taking place here. So this sort of first guess is not too bad, but we still know there's a lot of intuition that we can bake into Claude. So we switch back to slides. You can see here that in many ways, prompt engineering is a very iterative empirical science. And in this case here, we could almost have a test case where Claude is supposed to make sure that it understands it's in a car or a vehicular environment, nothing to do with skiing. And in that way, you iteratively build upon your prompt to make sure it's actually tackling the problem you're intending to solve. And to do so, we'll go through some best practices of how we at Anthropic break this down internally and how we recommend others do so as well. So we're going to talk about some best practices for developing a great prompt. First, we want to talk a little bit about what a great prompt structure looks like. So you might be familiar with kind of interacting with a chatbot, with Claude, going back and forth, having a more kind of conversational style interaction. When we're working with a task like this, we're probably using the API and we kind of want to send one single message to Claude and have it nail the task the first time around without needing to kind of move back and forth. So the kind of structure that we recommend is setting the task description up front. So telling Claude, what are you here to do? What's your role? What task are you trying to accomplish today? Then we provide content. So in this case, it's the images that Christian was showing, the form and the drawing of the accident and how they occurred. That's our dynamic content. This might also be something you're retrieving from another system, depending on what your use case is. We're going to give some detailed instructions to Claude. So almost like a step-by-step list of how we want Claude to go through the task and how we want it to tackle the reasoning. We may give some examples to Claude.


## Chunk chunk_001
Here is an example of if some piece of content you might receive, here's how you should respond when given that content. And at the end, we usually recommend repeating anything that's really important for Claude to understand about this task, kind of reviewing the information with Claude, emphasizing things that are extra critical, and then telling Claude, okay, go ahead and do your work. So here's another view. This has a little bit more detail, a little bit more of a breakdown, and we're going to walk through each of these 10 points individually and show you how we build this up in the console. So the first couple of things, Christian is going to talk about the task context and the tone context. Perfect. So yeah, if we begin with the task context, as you realized when I went through a little demo there, we didn't have much elaborating what scenario Claude is actually working within. And because of that, you can also tell that Claude doesn't necessarily need to guess a lot more on what you actually want from it. So in our case, we really want to break that down and make sure we can give more clear-cut instructions and also make sure we understand what's the task that we're asking Claude to do. Secondly as well, we also make sure we add a little bit of tone into it all. Key thing here is we want Claude to stay factual and to stay confident. So if Claude can't understand what it's looking at, we don't want it to guess and just sort of mislead us. We want to make sure that any assessment, and in our case, we want to make sure that we can understand who's at fault here, we want to make sure that assessment is as clear and as confident as possible. If not, we're sort of losing track of what we're doing. So if we transition back to the console, we can jump to a V2 that we have here. So I'll just navigate to V2. And you can see here, I'll also just illustrate the data because we didn't really do that last time around, just to really highlight what we're looking at. So what we're seeing here, this is that car accident report form. And it's just 17 different checkboxes going through what actually happened. You can see there's a vehicle A and vehicle B, both on the left and right-hand side. And the main purpose of this is that we want to make sure that Claude can understand this manually generated data to assess what's actually going on. And that is corroborated by, if I navigate back here, to this sketch that we can highlight here as well. In this case, the form is just a different data point for the same scenario. And in this case here, we want to bake in more of that information into our version two. And by doing so, I'm actually elaborating a lot more on what's going on. So you can see here, I'm specifying that this AI system is supposed to help a human's claims adjuster that's reviewing car accident report forms in Swedish as well. You can see here, we're also elaborating that it's a human drawn sketch of the incident and that you should not make an assessment if it's not actually fully confident. And that's really key because if we run this, you'll see that, and you can see it's the same settings as well, Claude 4, a new shiny model, zero temperature as well. If we run this, we can see here what actually happens. In this case, Claude is able to pick up that now it's relating to car accidents, not skiing accidents, which is great. We can see it's able to pick up that vehicle A was marked on checkbox 1 and then vehicle B was on 12. And if we scroll down though, we can still tell that there's some information missing for Claude to make a fully confident determination of who's at fault here. And this is great. This is pertaining to the task that I've set. Make sure you don't make any claims that aren't factual and make sure you only sort of set things when you're in your confidence. But there's a lot of information we're still missing here regarding the form, what the form actually entails and a lot of that information is what we want to want to bake into this LLM application as well. And the best way of doing so is actually adding it to the system prompt, which Hannah will elaborate on. So back in the slides, we have the next item we're going to add to the prompt. And this is background detail, data, documents and images. And here, as Christian was saying, we actually know a lot about this form. The form is going to be the same every single time. The form will never change. And so this is a really great type of information to provide to Claude, to tell Claude, here's the structure of the form you'll be looking at. We know that will not ever alter between different queries. The way the form is filled out will change, but the form itself is not going to change. And so this is a great type of information to put into the system prompt. Also a great thing to use prompt caching for if you're considering using prompt caching. This will always be the same. And what this will help Claude do is spend less time trying to figure out what the form is the first time it sees the form each time. And it's going to do a better job of reading the form because it already knows what to expect there. So another thing I want to touch on here is how we like to organize information in prompts. So Claude really loves structure, loves organization. That's why we recommend following kind of a standard structure in your prompts. And there's a couple other tools you can use to help Claude understand the information better. I also just want to mention all


## Chunk chunk_002
This is in our docs with a lot of really great examples, so definitely take pictures, but if you forget to take a picture, don't worry. All of this content is online with lots of examples and definitely encourage you guys to check it out there, too. Anyway, the, so some things you can use, delimiters, like XML tags. Also markdown is pretty useful to Claude, but XML tags are nice because you can actually specify what's inside those tags. So we can tell Claude, here's, here's the user preferences. Now you're going to read some content, and these XML tags are letting you know that everything wrapped in those tags is related to the user's preferences, and it helps Claude refer back to that information, maybe at later points in the prompt. So I want to show in the, back in the console, how we actually do this in this case. And Christian's going to pull up our version 3. So we're keeping everything about the other part of the user prompt the same. And we've decided in this case to put this information in the system prompt. You could try this different ways. We're doing it in the system prompt here. And we're going to tell Claude everything it needs to know about this form. So this is a Swedish car accident form. The form will be in Swedish. It'll have this title. It'll have two columns. The columns represent different vehicles. We'll tell Claude about each of the 17 rows and what they mean. You might have noticed when we ran it before, Claude was reading individually each of the lines to understand what they are. We can provide all of that information up front. And we're also going to give Claude a little bit of information about how this form should be filled out. This is also really useful for Claude. We can tell it things like, you know, humans are filling this form out, basically. So it's not going to be perfect. People might put a circle. They might scribble. They might not put an X in the box. There could be many types of markings that you need to look for when you're reading this form. We can also give Claude a little bit of information about how to interpret this or what the purpose or meaning of this form is. And all of this is context that is hopefully really going to help Claude do a better job analyzing the form. So if we run it, everything else is still the same. So we've kept the same user prompt down here. Oh, your scroll is backwards from mine. We have the same user prompt here, still asking Claude to do the same task, same context. And we'll see here that it's spending less time. It's kind of narrating to us a little bit less about what the form is because it already knows what that is. And it's not concerned with kind of bringing us that information back. It's going to give us a whole list of what it found to be checked, what the sketch shows. And here Claude is now becoming much more confident with this additional context that we gave to Claude. Claude now feels it's appropriate to say vehicle B was at fault in this case, based on this drawing and based on this sketch. So already we're seeing some improvement in the way Claude is analyzing these. I think we could probably all agree if we looked at the drawing and at the list that vehicle B is at fault. So we'd like to see that. So we're going to go back to the slides and talk about a couple of other items that we're not really using in this prompt, but can be really helpful to building up your prompt and making it work better. Exactly. I think one thing that we really highlight is examples. I think examples or few shot is a mechanism that really is powerful in steering Claude. So you can imagine this in quite a non-trivial way as well. So imagine you have scenarios, situations, even in this case concrete accidents have happened that are tricky for Claude to get right. But you with your human intuition and your human labeled data is able to actually get to the right conclusion. Then you can bake that information into the system prompt itself by having clear cut examples of A, the data that it's supposed to look at. So you can have visual examples. You can use base 64 encoded an image and have that as part of the data that you're passing along into the examples. And then on top of that, you can have the sort of depiction or description rather of how to break that down and understand it. This is something we really highlight and emphasize in how you can sort of push the limits of your LLM application is by baking in these examples into the system prompt. And this again is sort of the empirical science of prompt engineering is that you sort of always want to push the limits of your application and get the feedback loop in where it's going wrong and try to add that to the system prompt so that next time when example that sort of mimics that takes place, it's able to actually reference it in its example set. You can see here as well, this is just a little example of how we do this. Again, really emphasizing the sort of XML structure that we enjoy. This gives a lot of structure to Claude. It's what it's been fine tuned on as well. And it works perfectly well for this example. And in our case, we're not doing this just because it's a simple demo, but you can realistically imagine if you were building this for an insurance company, you'd have tens, maybe even hundreds of examples are quite difficult, maybe in the gray that you'd like to make sure that Claude actually has some basis in to make the verdict next time.


## Chunk chunk_003
Another topic we really want to highlight, which we're not doing in this demo, is conversation history. It's in the same vein as examples. We use this to make sure that enough context-rich information is at Claude's disposal when Claude's working on your behalf. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a perfect place in the system prompt to include because it enriches the context that Claude works within. In our case now, this isn't really a user-facing LLM application. It's more something happening in the background. You can imagine for this insurance company, they have this automated system. Some data is generated out of this, and then you might have a human in the loop towards the end. If you were to build something much more user-facing where you'd have a long conversation history that would be relevant to bring in, this is a


## Chunk chunk_004
add to this to really make it useful for a real-world task. Indeed. Thank you so much. So as Hannah mentioned, we sort of set the stage in this prompt to make sure that Claude's really acting on our behalf in the right manner. And a key step that we also add towards the end of this prompt that I'm going to show you in a second is a simple sort of guidelines or reminder part as well. It's just strengthening and reinforcing exactly what we want to get out of it. And one important piece is actually output formatting. You can imagine if you're a data engineer working on this LLM application, all this sort of fancy preamble is great, but at the end of the day, you want your piece of information to be stored in, let's say, your SQL database, wherever you want to store that data. And the rest of it that is necessary for Claude to sort of give its verdict isn't really that necessary for your application. You want the nitty-gritty information for your application. So if we transition back to the console, you'll see here that we just added a simple importance guidelines part. And again, this is just reinforcing the sort of mechanical behavior that we want out of Claude here. We want to make sure that the summary is clear, concise, and accurate. We want to make sure that nothing is sort of impeding in Claude's assessment apart from the data it's analyzing. And then finally, when it comes to output formatting, in my case here, I'm just going to ask Claude to wrap its final verdict. All other stuff I'm actually going to ignore for my application and just look at what it's actually assessing. And that is I can use this if I want to build some sort of analytics tool afterwards as well, or if I just want a clear-cut determination, this is the way I can do so. So if I just run this here, you'll see it's going through the same sort of process that we've seen before. In this case, it's much more succinct because we've asked it to be, to summarize its findings in a much more straightforward manner. And then finally, towards the end, you'll see that it'll wrap my output in these final verdict XML tags. So you can see that during this demo, we've gone from a skiing accident to sort of unconfident, insecure outputs from perhaps a car accident in the second version to now a much more strictly formatted, confident output that we can actually build an LLM application around and actually help a real-world car insurance company, for example. Finally, if we transition back to the slides, another key way of shaping Claude's output is actually putting words in Claude's mouth, or as we call it, pre-filled responses. You can imagine that parsing XML tags is nice and all, but maybe you want a structured JSON output to make sure that this JSON is serializable and you can use this in a subsequent call, for example. This is quite simple to do. You could just add that Claude needs to begin its output with a certain format. This could be, for example, a open square bracket, for example. Or even in this case that we see in front of us, this would be an XML tag for itinerary. In our case, it could also be that final verdict XML tag. And this is just a great way of, again, shaping how Claude is supposed to respond without all the preamble if you don't want that, even though that is also key in shaping its output to make sure that Claude is reasoning through the steps that we want it. So in our case here, we would just wrap it in the final verdict and then parse it afterwards. But you can use pre-fill as well. Now, finally, one step that I would like to highlight here as well is that both Claude 3.7 and especially Claude 4, of course, is a hybrid reasoning model, meaning that there's extended thinking at your disposal. And this is something we want to highlight because you can use extended thinking as a crutch for your prompt engineering. Basically, you can enable this to make sure that Claude actually has time to think. It adds this thinking tags in the scratchpad. And the beauty of that is that you can actually analyze that transcript to understand how Claude is going about that data. So as we mentioned, we have these checkboxes where it goes through step-by-step of the scenario that transpired for the accident. And in many ways there, you can actually try to help Claude in building this into the system prompt itself. It's not only more token efficient, but it's a good way of understanding how these intelligent models that don't have our intuition actually go about the data that we provide them. And because of that, it's quite key in actually trying to break down how your system prompt can get a lot better. And with that said, I think I'd like to thank all of you for coming today. We'll be around as well. So if you have any questions on prompting, please go ahead. I know there's a prompting. You want to learn more about prompting in an hour. We have prompting for agents. And right now we have an amazing demo of Claude plays Pokemon. So don't go anywhere for that. And as Christian said, we'll be around all day. So I know we didn't have time for Q&A in this session, but please come find us if you want to chat. And thank you guys for coming. Thank you so much.
