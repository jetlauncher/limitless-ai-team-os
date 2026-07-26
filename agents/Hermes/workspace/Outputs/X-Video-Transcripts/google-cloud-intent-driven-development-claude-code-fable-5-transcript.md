# Transcript - Intent-driven development with Claude Code & Fable 5

## Source

- Original video: https://www.youtube.com/watch?v=6ERUGFurDHY
- Title: Intent-driven development with Claude Code & Fable 5
- Channel: Google Cloud Tech
- Duration: 2761 seconds (46:01)
- Upload date: 20260706
- Matched from X repost: https://x.com/precisox/status/2075824818440519692

## Description excerpt

Fable 5 on Google Cloud → https://goo.gle/4wlhp8L Cloud Fable 5 blog → https://goo.gle/4eYyBtP
Claude Code on Google Vertex AI → https://goo.gle/4v4gTuP

## Notes

This is the clean YouTube caption transcript for the original Google Cloud Tech source. The X repost is longer (61:05) and appears to include roughly 15 minutes of extra Claude Code workshop/context before this original Google Cloud episode begins.

## Transcript

Cloud Code has become one of the most talked about developer tools in the world right now. Engineers
everywhere are rethinking how they can build software because of it. And sitting right here with me
today, I've got Lydia Haley from Anthropic, the company behind Cloud Code. You might also know her
online as the Avocado, and she's here to pull back the curtain on how Cloud Code actually works and
where it's heading. And I've also got YK Sugy, the creator of CS Dojo, and he's also the author of
the Cloud Code Tips Repository, which is one of the most popular community resources for mastering
Cloud Code. So, if you've searched on how to get, you know, better results out of Cloud Code, you've
probably landed on his work. Welcome to the Agent Factory, both of you. Uh before we get into it,
quick one for both of you, what is the one thing about Cloud Code that most developers are
completely sleeping on? &gt;&gt; I would say auto mode. I mean, it's pretty new, so I get it, but uh
using auto mode, and we'll go over that a bit more today, in your workflows will enable so much.
&gt;&gt; YK, so your Cloud Code uh tips repository has like over 8,000 stars, right? And posts about
it keep going viral. So, like, what was the moment that really clicked for you uh with Cloud Code?
And what made you start documenting those tips for other people? &gt;&gt; It clicked for me right
away, you know, I I remember I started to use Cloud Code as soon as it was launched. And kind of a
quick story about it, I was going through an interview for my current job at at Daft. And I built
like a demo project for that job interview, and I didn't tell them I used Cloud Code, but they were
so surprised with the quality. Uh so, even back then, I think there was like so much promise, and I
just kept using it, I kept learning, and I kept sharing my lessons. &gt;&gt; Uh Lidia, so like from
the Anthropic side, what's it been like uh watching the community run with Claude Code, you know,
like when you see someone like YK building out these workflows, and he's sharing them at scale, like
how does it How does that feed back into how the the team actually thinks about the product?
&gt;&gt; Yeah, I feel like most of my job is watching these power users like YK use Claude Code, and
seeing how they're using the tool. I feel like everyone uses it slightly different. How we use it
internally might not be how people use it externally. Even all the engineers on the Claude Code side
here, we all use it differently. Um so, it's extremely important for us, and we really enjoy getting
all this feedback, and seeing all these patterns coming from the community, because it really helps
us shape our road map as well, see what's missing, or what features we need to add or or improve.
&gt;&gt; We kind of hear now the term intent-driven development, actually means from a lot, and the
idea, you know, where you're telling Claude what you want to build, rather than how to build it. Um
so, YK, what made that shift for you, and what made you start, you know, sharing that? &gt;&gt; Uh
first of all, there are many different terms for it, but I personally like this term, because um to
me, it's not about the exact prompt. You know, sometimes people say, "Oh, use this prompt, and you
get better results." Sure, maybe. But, uh to me, it's more about expressing what your intent is
exactly, knowing what your intent is exactly, what you want to build. And then, just being able to
express it. So, one thing I recommend uh that people do is using your voice to type, instead of
using your hands to type. And uh one way where it's it's better is you know, so that you can express
your intent faster. You might make mistakes, you might say, "Um." But, it doesn't matter, as long as
you know, you're able to express it. &gt;&gt; Yeah, uh Lidia, I'd love your take on that, too. When,
you know, Anthropic kind of thinks about how developers should be working with Claude Code, does
intent-driven development match how the team uh designed it? And, you know, what's what's it been
like watching kind of the the community shift in this direction? &gt;&gt; Yeah, I like the term
intent-driven development. I feel internally we do focus a lot on making sure people understand that
Claude needs verification, right? And I feel like that's kind of part of intent. It's like part of
it is how you structure your prompt. I still feel like having a software engineering background does
help refine your prompts, and you can tell Claude a lot better what you actually want it to do. Um
so, in that case, you know, like using plan mode, adding like images as verification, I feel like
it's kind of part of the intent. Um but also voice mode, by the way, I still have to use it. It
seems really fun. I feel like I I probably would prompt a lot better if I'm not in my head as much,
cuz I think I notice when I type a prompt, I'm like, "Ah, maybe I shouldn't ask this. Maybe I should
do something else." But it's brainstorming out loud might actually be be very fun. I still have to
use it. Um but yeah, just like I I feel like it does show a pattern where it's like we want people
to use Claude Code the moment they have an idea. And we want to make sure that kind of that friction
point going from your idea to an actual deployed website is as small as possible or as easy as
possible. Um so, yeah, again, this is also great community feedback. I feel like we might focus more
on these types of patterns. It's like, "Hey, you can use Claude Code the moment you have
inspiration. Just talk to it. Brainstorm maybe in plan mode, and you know, get your get your website
deployed quickly." &gt;&gt; I love that. And also, I I noticed that I love using voice mode too, cuz
I feel like I'm I'm much quicker at talking than I am at typing. So, I'm I'm getting frustrated at
how slow I'm typing, so I just switch to voice mode. Um I think what's also been really exciting is
that, you know, Claude Code is not just a solo developer tool. It's also being used at enterprise
scale. So, like Claude Code can now, of course, you can run it on Google Cloud agent platform. So,
when you're actually ready to go from just experimenting to actually rolling this out across your
team, uh the platform is already there. So, let's actually get into some of the super exciting demos
that we have planned. Uh YK, you and I are going to kick off the first demo together. So, in this
demo, I'm going to show you how you can set up Cloud Code on uh agent platform, and YK is actually
going to demonstrate how he built something really cool on there. Uh first, I'm going to quickly
show how you can set up Cloud Code on Google Cloud, and then this is going to be the foundation,
right? So, uh what I've done is I've installed Cloud Code on my Mac already, and if you have not
done that, you can do this super easily by running these following commands. And then, uh what I'm
going to do next is actually install uh G Cloud SDK. If you don't already have that, that's a great
place to start because we're going to be using uh G Cloud to run all of these commands. And then,
I'm going to set my uh project ID, which you can get from your own Google Cloud console. So, I'm
going to set my project ID, &gt;&gt; [clears throat] &gt;&gt; and then I'm going to enable Vertex AI
APIs, which will allow us to use all of the Cloud models. And next, I'm going to enable a bunch of
other uh variables, which will which will essentially enable the Vertex AI integration for Cloud.
And all of these commands can actually be found in the links that I'll be leaving in the description
box below. And then, once I've done that, I can just start Cloud, and now it's going to be running
on uh Google's Vertex AI. And off to you, YK. &gt;&gt; Thank you so much for that, Smita. Uh what
I'm going to show here is essentially a demo of what I would call intent-driven development, And I'm
just going to get right into it. And as I wait for the output to come in, hopefully I'll have some
time to discuss these tips and share some of these tips. So, here I'm just going to start prompting.
I'll say, "I want to create a 3D game. It's going to be a slingshot game where you're going to have
a stationary slingshot right in front of you, fixed camera, fixed uh slingshot. And I want to be
able to drag a ball uh that's attached to the slingshot in X and Y direction. So, dragging should
determine the X and Y directions or the coordinates. And the duration of how long I'm holding the
ball should determine the Z direction. So, that way I should be able to control the ball in three
directions. And whenever I release it, uh further back it is held, the faster it should shoot. And
what should I use to build that? I want it to be all front end, HTML, JavaScript, and CSS. Feel free
to use libraries if if you need to, but tell me the options I should use." I think that should be
good enough. So, as I said, uh this is exactly what we're doing. I'm building a slingshot game. And
uh one quick tip I want to share is setting up an alias. And your command, you know, might look like
it like this depending on the exact OS you're using. So, this is so that you don't have to uh type
Claude every time. I mean, you can if you want, but you know, this is a little bit faster for me
that way. Okay, so here we have, you know, different options. Uh this model is suggesting 3 JS and
control hand rolled physics. I don't think I want I want to hand roll physics. 3 JS plus Cannon. I
actually remember there's another option for physics. I remember there is another option for physics
that's not Cannon. Uh I don't remember what it is. you remind me? Let's see if that works. So, as
you can see, I've been talking to the agent with my voice here as I recommended earlier. There are a
couple of different options for it. You can just use, you know, the {slash} voice option or
alternatively a dedicated desktop app. I actually built a desktop app for myself, uh just for me.
And that uses a local model. So, if you want to go that route, there is that option, too. So, we
have uh ammo rapier. So, let's go with rapier. I did a little research beforehand. Uh let's go with
rapier and uh 3.js. And then I'll say, let's create a new folder for it. Uh let's call it something
like slingshot podcast because I'm building this on a podcast. And uh just build a slingshot. I I
don't have to have any targets right now. All I need is, now, the slingshot, fixed camera, as well
as a way to control it and release it. And then, I'll just say manually let's use Beat for building
it. So, you may have noticed that I'm in the projects folder. And I personally like to do it this
way where I have most of my projects in a single folder. It's not necessarily for everyone, but I
highly recommend it so that it's convenient for the agent to be able to, you know, refer to
different projects and you can say stuff like, "I want to take this element from this other project
and this other element from this other project and combine them into a single project." So, it's
pretty helpful for that. And as you may have noticed, it's helpful to start with broader questions
first and then dig deeper as you go. So, these might be questions like, you know, what architecture
should I use, what libraries, frameworks should I use? And then sort of go back and forth with the
agent to refine your idea over time. And I'm confident enough of this model that it knows enough for
this particular problem, but if it needs more latest information, later kind of community feedback
and stuff like that, you can ask it to do research on your behalf as well, so that you can make
better architectural decisions. &gt;&gt; Do you ever use plan mode for this, or do you just ask
Claude like, "Hey, don't code anything yet." Cuz we have a specific plan mode, but often I just end
up talking to Claude instead like a co-worker. What what do you prefer, YK? &gt;&gt; Uh I don't
think I ever explicitly turn on plan mode, but I know it sometimes does that on its own. So, that's
that's kind of how I do it. All right. While the output streams in, I'll just keep going with the
tips. So, number five is you want to learn to use Git and GitHub CLI well, and just CLI commands in
general because turns out CLI is really really powerful. There's so much uh stuff that you can do,
you know, just starting with Git and GH. So, definitely learn to do that. And here, what I'm going
to do is it looks like it created this folder, and the result is already coming in. But, I'll just
go in a new tab, and I'll say, "If this project is not a Git project yet, turn it into a Git
repository, and then create a public repository out of it." So, I'll just do that in this other
thread. It looks like it's actually testing it itself. I I didn't ask it to do it, but it looks like
it started it in Playwright, testing it. Uh but, I should be able to personally test it myself here.
All right, it looks like it's sort of working. Nice. All right, it looks like it's working. Uh
commit if you haven't yet. And um let's show the trajectory before I release it so I know where the
ball is going. I mean I guess it depends on how how hard you want to make it, but I think it's more
convenient that way. All right, so it looks like it was able to create this project, open it for me.
Uh I think it used the open command in a terminal because I didn't open it explicitly. And going
back to uh the browser here. All right, it's getting confused with like uh the different agent doing
the work, but I should be able to figure out what it's doing here. Looks like it's adding this
trajectory uh feature. Not quite there yet. All right, nice. So it's got a trajectory. I think I can
go to the next tip as it finishes the work. You want to learn to verify the output. Um there are a
few different ways to go about it. As I just showed, you can directly um verify the behavior of the
app, not necessarily the code, but you can also check the code yourself if you want. And you can
also automate, you know, the process of verifying the output as much as possible by writing tests,
um by writing GitHub actions, and things like that. It's much better, it looks like. And looks like
it's committing the trajectory feature. That's perfect. Uh next up, I think this is going to be the
last feature I'm going to add here. I want to have a few big uh targets in front of me in front in
front of this slingshot. They should be like discs, circular targets, and when I hit them, I want to
have a satisfying visual effect, maybe like them shattering into particles or stuff like that. So,
as you may have noticed, you know, the these prompts sometimes are a little bit vague, but as long
as your intent is clear enough, you know, that I found that uh Claude is able to figure out what I
mean even if there are like typos or transcription mistakes. You know, it's it's basically smart
enough. And meanwhile, uh while we wait for that particular feature, what I'm going to say here is
this project is almost done, so let's give admin access because I think this is still a private
repository to the following user. That's Lydia's GitHub account uh that I pulled from the different
screen. And it's saying, "Let's add shatterable targets. Plan three big bull's-eye discs at
different distances. Hit detection that catch catches the ball across in the display." Looks good.
And this thread is running these uh GH commands so that Lydia should be able to uh get an invitation
with admin permission on this uh project soon, and it looks like this thread is just finishing up
with these targets. Nice. Uh it might actually not uh reload automatically. That might be uh
something to fix next, but I think it's already a pretty satisfying game. &gt;&gt; I feel like this
was such a good example of your intent-driven, like the first moment that you wanted to use a
specific physics library. Um I I like that that's also very perfectly shows like having more context
around what you want to build helps helps so much. &gt;&gt; Definitely. I think the rule of thumb is
you ask more questions when you have less context because I didn't know about these particular
physics libraries. I needed to ask questions earlier, but now that I'm like, you know, a little more
familiar, I can &gt;&gt; I'm just like in a real colleague, right? Like you would still talk to them
before you implement something, so. &gt;&gt; Uh so, just to wrap up this uh demo, I think one last
prompt I'm going to do I think I think it was trying to like test uh the app for me, but it doesn't
have to do that. I'll say, "All right, let's commit and push, but don't push directly into main.
Instead, create a a new branch because I want to sort of simulate, you know, the the process of code
review, and then push that branch, create a draft PR, and then open it for me using the open
command." And that should be able to wrap up this demo because one of the tips I had uh actually I I
have this whole section about managing your code base, but one particular quick tip I had is
creating a draft PR. You know, you can just ask the agent to create a draft PR just like I did, and
then check it before marking it it as reviewed so that, you know, people will know, "Okay, this this
PR maybe it was created by the agent. It's not ready for review yet." Or, you know, "It is ready for
review." So, I think it makes things clearer. As you can see, it's doing get push here uh using
automode here, as you can see. gh pr create draft title and body. It's opening it for me, and that's
it. I'll just say, "Ready for review." You know, if I want, I can check the code manually or, you
know, interactively using a code code, and then I'll just merge it here, and that's it for the demo.
&gt;&gt; I think this is such an awesome and Lydia as she as Lydia was mentioning, right? It's like,
you know, seeing the intent-driven development. I think this is like a super clear example of that.
Um and then so now the source code is kind of going over to Lydia for her demo. So, Lydia, it's your
turn. I'm super super excited on what you're going to showcase for us. &gt;&gt; Yeah, let's get
started. Okay, so basically first what I did over the weekend is I pulled one of YC's GitHub
repositories cuz he already showed me kind of the game that he wanted to build, which by the way,
this is such a difficult level to pass. I have not been able to do this, but when I see this game,
this is already really impressive, but I want to make it a bit better, right? To make it an actual
game, I might want to add more levels. I might want to change the environment per level, all that
kind of stuff. And I want to use Claude, of course, to help me out there. And what I really like to
do instead of, you know, prompting Claude with the changes I want to make, I really like to use a
visual flow. This is all created in Claude design. I don't know if you've used Claude design yet.
It's a new in our research preview, but basically you're able to create uh presentations, slides,
entire websites based on your prompts as well. It's basically Claude code, but for design. But I
really like having this visual approach for a plan. This is just HTML at this point. I could have
also exported it to Figma or Canva or anything else, but this allows me to really think about the
plan and the changes I want to make. So, for example, here Claude came up with this slingshot V2.
So, how can we actually make it into a game? So, we have the game flow with a main menu. We have a
level select, game play loop, all of this. So, more like visuals that we want to add here, um the
game play screen, and this is all HTML. So, this is pretty much already kind of what we had here,
but we have some health bars, um and also some systems to design. So, we have the health bar here
again to charge and aim. We already had this or at least in the demo that Y K just showed in the
original didn't have this yet. We have some haptics, which I think are nice to add if you're like on
your phone, you kind of want to feel, you know, that something is like pulling and then and then
smashing the plates. And of course also scoring. Um we have some extras that maybe they want to they
want to add as well. Um the different levels, which I think looks so cute. So, again, this is all
Claude designed. Claude came up with this. Okay, so this is basically all the prompts that I gave
Claude design. So, this is in Claude design itself. And the nice thing is that I can also just edit
everything. So, if maybe I want to change some of the planning, I don't want to say slingshot here,
I want to say a slingshot, whatever, it doesn't matter. I can just do that and then I can later
export this and use this as my prompt to Claude. So, what I did for the uh design wireframe is I
just added it to my demo assets here. So, this is all just HTML. The entire plan that we just saw
with the different screens and everything else is just here. So, now I can just open Claude real
quick. Claude is already running here. And to make this um you know, use uh the uh agent platform,
it's already running on Vertex AI, but how I did it is that we actually have a really nice built-in
wizard called setup Vertex. So, we have setup Vertex. And when you run that, it'll automatically do
most of the setup that we just saw. So, for example here, I can just say, "Okay, I want to use my
application default credentials." Perfect. Uh I want to use a different project. This one is called
project where ours on scratch a foo. I'm going to do global. It's going to do a quick check to Haiku
just making sure that everything is set up correctly. Um and it's going to see which models we can
use here. Here we see that we have access to Opus 4 6. We can also enable more in Model Garden in
Google itself. And we also have access to Fable 5, which I'm very excited about. I'll be using Fable
for this demo specifically. Uh I want to pin the working models to 1 million, save it, and now we're
good to go. So, anyway, that was a quick setup. So, now we're still running on Vertex just like we
saw before. The only thing what I really enjoyed doing is using auto mode. And by default in in
Agent Platform, that is an environment variable. So, we actually have to turn that on first. I'm
actually going to quit this real quick. I'm just going to clear it. You can do that by doing export
Claude code enable auto mode. So, now with that enabled and Claude restarted, we can now see with a
shift tab that we have auto mode here. And you could also see why K was using auto mode as well. The
nice thing about auto mode is that it makes it so much easier to just kind of not be as hands-on.
So, just to show real quick what it is. If you've used Claude code, you may have noticed that you
can use you know, ask almost like ask everything, in which case Claude code will always ask you
like, "Hey, is it okay if I delete this file? Is it okay if I run this command?" And after a while,
you're just like, "Yeah, go ahead. Like, whatever." And we call this a permission fatigue, where I I
do think it's very important that before Claude does something dangerous, it has to make sure that
it should be doing that. Um but at a certain point if asked or if Claude asks you a questions like
every time, you won't read them as much anymore cuz you're kind of like, "You've asked me like a
hundred times now. Sure, just go ahead." That's permission fatigue, which is also dangerous. And
then previously, we also had the option to buy a a dangerously skip permissions, in which case
Claude will never ask you anything, which is also not great cuz if it's about to like delete your
root file, there's no going back, right? So, auto mode is our solution to that. It kind of sits in
between your deny list and allow list. So, auto mode runs a a different classifier between all the
tool calls. So, it kind of thinks like, "Okay, is this tool call dangerous, first of all? If yes,
okay, let's ask the user if they actually want to do it." But if it's just a normal like read or
edit or something else, then no, that's not dangerous in most cases, and let's not ask them. Let's
not bother them. Um another thing also is that it's much better against prompt injection. Um in some
cases, a tool called might just be like ignore all instructions, that kind of stuff. Because it runs
a classifier in between, it's much better at catching that. Also, another the nice thing is that
it's more context dependent. Like, if you're asking Claude delete this folder, um in some cases that
rmrf might be dangerous, but if you've specifically asked for it, it's not dangerous. So, in those
cases, automode won't ask you cuz you you you asked to delete it. It's It's not a dangerous thing.
So, this is a very nice way of working, and this actually enables you to use Claude code or to run
Claude code way more autonomously in these longer-running sessions. But, anyway, so far we haven't
done any anything yet. So, um I want to implement that entire wireframe that I just showed using
something called dynamic workflows, and this is a new feature that we've just added. And you just
ask Claude to use a dynamic workflow. It's not a slash command, it's nothing else. So, I can just do
like read this design file and use a dynamic workflow to rebuild the game and match it. And I added
it to my demo assets, so I can just see um demo assets. Um it was in design wireframe. Yeah. So,
what I'm doing now is I'm giving Claude a way to verify and understand what I want to build. Because
it has this HTML, it has the context. Um I could have made this prompt like a lot more specific. I'm
like, "Okay, add all these levels, add all these other features." But, honestly, I'm kind of just
waiting to see if Claude will understand it. So, in this case, we're going to wait a little bit. I
would kind of also uh prepared it like a cooking show. So, if the if this takes quite a while, there
is a tab in which this is already finished. So, we can always just go there, but it's always
interesting to see what Claude comes up with. So, it kind of to quickly explain what a dynamic
workflow is. Again, I created a little um visualization. Hopefully, this kind of makes sense. So,
sub-agents themselves aren't new. If you've used Claude Code, you may have noticed that sometimes it
spawns a new sub-agent to perform a certain task. A sub-agent is essentially a um another Claude
Code instance with with its own context. And it's really good at just like focusing on that specific
task. But, if you're just asking Claude every time to like use sub-agents, you don't even have to
ask it. The downside is it is that it's very non-deterministic. You know, sometimes it might spin up
four sub-agents, sometimes it might not even use sub-agents. The other time it uses 10 sub-agents,
all that kind of stuff. With workflows, it's kind of our deterministic solution to that. Um
workflows also spin up a lot of sub-agents, and that's a feature. It can go into hundreds of sub-
agents because like this is a feature for tasks that takes hours or days or like these really long-
spending tasks. But, the nice thing is that Claude Code actually generates a JavaScript file. And
we'll see that in a moment as it's uh like eventually it will it will kick off the workflow. Um but,
you can see that JavaScript file, and you can save the workflow uh to then rerun it later on as a
slash command. So, if you really like a specific kind of uh steps a Claude could Claude Code took,
what specific sub-agents, you can save it and rerun it uh in that very deterministic way. And
because all these sub-agents run in parallel, you can also achieve a lot more within usually the
same amount of time as a single sub-agent would have because it's it's parallel. Um and what you'll
see is Claude is pretty smart at like kind of delegating these sub-agents to be very focused on a
specific task. Okay, so just like a cooking show, I figured that Claude would take a while to kind
of spin this all up. That's all expected. Fable is a bit slower because it's such a large model. Um
but here I I showed the exact same command. This is also what I just typed in my in my other
terminal, right? Read this design file and use a dynamic workflow to rebuild this game and to match
it. It's the exact same HTML file as well. Um and it then it ran this workflow and we can see what
it ran by uh with the workflows {slash} command. And here you can see that it ran this specific
workflow. So here we had four agents in uh the build phase. We had build engine, build UI, build
audio, and levels and haptics. We then had an integration phase, so this is another subagent, a
review phase, and a verify phase. So this So these phases run sequentially, but the actual build
agents all run in parallel. Uh you can see that this is all Fable 5. We can also go into it. And the
nice thing is that if we like this workflow, in this case it's like rebuilding a game, so it doesn't
make too much sense to save this, but we could by just pressing S. And then we could do like save
dynamic workflow and save as rebuild sing show game, sure. For this demo, I'll save it as that. Um
and now you can see that it saved this JavaScript file. So I'm kind of just want to open it and see
if I can open it this way. I'm just going to remove this. And you can see that this is a JavaScript
file that that Claude code created for this workflow. I didn't type this. This is all Claude. You
can see that it's it's just a normal function. It's like a build phase. We see all the builders. We
see the prompt that it's using for all these subagents. We have a review phase, all that kind of
stuff. So if we want to, we can also be very specific here. Maybe I don't want all subagents to use
um Fable like it did here. If we go into workflows, you can see that it all used Fable 5. In some
cases, I don't need a model that strong for this subagent. Maybe I want to use Sonnet or or Opus. We
can all We can just ask Claude, of course, to change that. We can just ask Claude like, "Hey, please
use Sonnet for all your sub agents." But we can also actually see it in our code and edit the code
itself. And again, because this is all just a JavaScript file, this is deterministic. So then every
time we invoke that slash command, it will just run these exact same sub agents. So that's
incredibly nice. Um I'm just going to see what it came up with. I'm going to run dev. So yeah, it
uses workflow to rebuild it according to our design spec. Let me see if it actually made it look
good, though. &gt;&gt; [sighs] &gt;&gt; So it actually did make it almost in the exact same like
design pattern with this kind of like draw look. Um but it definitely added some levels. It added I
don't know if you can hear it. It added like audio to the levels. And it actually made it into a
real game. So now we have different levels, everything else. So it's almost exactly like our
original design like spec here. Um so honestly, I'm I'm pretty happy with this. I'm not sure if I
can like clear all these levels. Yeah, it's obviously very difficult. &gt;&gt; Thank you both for
those wonderful demos. So like let's kind of zoom out and get into some bigger ideas. YK, your
entire repo is a playbook for maximizing what Claude code can kind of do autonomously. Uh but you
also have tip number 38, which is you know, simplify over complicated code where you kind of note
that code generation models have a bias towards writing more code than needed. So how do you kind of
balance the rapid prototyping with the discipline of actually keeping things clean? &gt;&gt; So I
think in general, they have had that tendency over time, but it really depends on the particular
model that you're using. And depending on that, it might be able to generate concise code. Um but
the general principle that I try to convey through this particular tip and other tips on this repo
is that you know, you want to be in control of the code, not necessarily like totally in control,
you know, micromanage everything, but in a way to make sure that your code quality is good, your
output quality, the behavior is correct, and all of that. So, I would say just in general, you know,
don't necessarily commit all the code that's generated. Make sure that you only commit and you know,
merge the one ones that are important and valuable to your code base, and you need to be the decider
of that. &gt;&gt; So, Lydia, with agents writing more and more code, what does understanding your
code base actually look like in 2026? So, and how do developers kind of just stay in the driver's
seat? &gt;&gt; Yeah. The way I see it is I think the role of a software engineer is changing more to
be almost like a product manager. Um at least that's that's what I've noticed, and also it feels
pretty logical. Like as a software engineer, you're not just writing the code, but you're in charge
of owning it, understanding the architecture that you want to build, and it's still up to you to
kind of understand why we need to implement a feature, all that kind of more like product manager
stuff, but we still definitely need the technical expertise, almost with the um intentional design
that YK mentioned. Um it's still very important. Um I always like to kind of draw a comparison to
like I can write TypeScript or JavaScript, but I'm not going to focus on the machine code that gets
generated afterwards. And it's almost like uh it's it's almost pretty similar where it's like
software engineering used to focus on the actual code syntax, almost like, you know, how machine
code might have mattered, but we're going a layer above that now. I think what's more important is
understanding the architecture, understanding the feature, and understanding still what the
shortcomings are. Um but then also building the right environment for Claude around it with hooks,
permissions, ClaudeMD file, that kind of that kind of stuff. And it still requires a lot of
technical expertise and and good taste and high agency. &gt;&gt; Can we also talk a little bit about
what your own setup is? You're literally on the team that, you know, builds Claude code, so you're
probably the best person to ask this. You know, you're also shipping fast. I see all of your content
on like YouTube or LinkedIn. So, what's kind of your personal Claude code workflow and how does that
look like? &gt;&gt; Personally, I think I really want to focus on setting up as many routines as
possible. I have a lot of um like um proact or scheduled Claude code sessions, kind of always
keeping me in the loop. And it's not just Claude code. This is just Claude in general. I kind of see
Claude's entire ecosystem more as like, okay, what is the problem I'm trying to solve? Cuz we have
Claude code, we have co-work, we have um chat. Um where I I try to like agentify or Claudify as much
in my life as possible. And I don't want to Claudify the things I actually enjoy doing. For example,
I really I sound weird when I say this, but I really enjoy creating keynote slides. And I used to
use Claude code to automate that as well cuz we have computer used and it can actually do a lot on
your behalf. But I noticed like I kind of just enjoy doing this and I don't want Claude to do this.
This is like, you know, kind of my creative outlet. And then of course with Claude code, like we
have the Claude bot running on all of our like our issues and our PRs. So, Claude automatically auto
fixes all of our PRs as well. Um like YK, after your demo, I was like, oh, I kind of just want to
run auto fix PR now. I don't know if you've set that up, but if you've installed the Claude app on
GitHub, basically what happens is if your CI fails or someone leaves a comment, Claude will
automatically try to fix it until your CI is green. So, if a co- or if a teammate leaves a comment
like, hey, you forgot to add this or that, uh Claude will take that feedback and try to fix it and
it immediately push it to that branch. So, all of these um like systems, everything we've set up is
just to be as out of the loop as possible and just kind of letting Claude do its thing. Which sounds
scary, but with the right hooks and permissions and, you know, using sandboxes and all of that
stuff, you get really, really far. And also, of course, we're kind of trying to push it as far as we
can cuz like we are Anthropic's still Cloud Code's number one user. It's like, okay, we want to make
sure that the features we're building are features that we like on the team. Um yeah, so mainly
that. &gt;&gt; I I love the term cloudify. I don't know if that is an official term which is used
internally, but yeah. Um I think using just like in general like just using AI to automate the
things that you don't want to do so that you can enjoy doing the things that you like doing more. It
kind of reminds me I was on X the other day and someone built an app to respond to their partner.
And I was &gt;&gt; [clears throat and laughter] &gt;&gt; thinking maybe we're optimizing too much.
&gt;&gt; That's so sad. That's Now you just got to be like scared that your partner's doing that all
the time. Like, &gt;&gt; [clears throat] &gt;&gt; you're right to push back. You're absolutely
right. &gt;&gt; Okay, so why can't Lydia I also want to get your take on kind of what's happening in
the developer community recently, right? Like we have all of these, you know, coding agents out and
then but at the same time on Hacker News and I'm on Hacker News a lot. Um I I see a lot of like
popular posts kind of like saying, "I'm going back to writing code by hand." Or um you know, an AI
coding agent needs to reduce your maintenance cost, not just write code faster. And so it seems like
there's a real conversation about kind of craft, control, uh technical debt, you know, so what are
your thoughts on that? Um YK, I know you have a lot of tips on this. You said, "You know, the best
way to get better at Cloud Code is by using it, right?" Uh you also said, "Be braver in the
unknown." So you're very clearly all in. So what do you say to developers who feel like they're kind
of losing their craft? &gt;&gt; My personal philosophy, at the end of the day it is a tool. Um so I
I'm not sure if this is the right analogy, but you know, it's sort of like as a instead of using
regular brush, you're using a electric automated brush. So, you're responsible for the output.
That's the first thing I I I really really want to emphasize because I get frustrated by this kind
of discussion whenever I read it. You know, people say, "Oh, you know, I people produce like so much
code and it's not it's not good with AI in general, not just cloud code." And I say, "Okay, then
don't produce it then. Like then don't don't push it." Like I as I said, there are so many ways to
review code, make sure it's it's good before it goes into production. You know, if it's like a one-
time uh five five coding kind of casual project, like the game I built, that's totally fine. You
don't have to check the code. But if it's more of a serious production, you know, code base that you
want to really be secure and safe about, then like I said, create a draft PR, make sure it's good,
review it manually or with AI. If you generate 100,000 lines of code, you don't have to commit
100,000 lines of code. That's that it's not necessarily the way it is, you know. Just commit what
you think is right. And at the end of the day, you're responsible for the tool and the output.
&gt;&gt; Yeah. I can also only agree agree with that. I feel like you still need to verify, and like
you're really good at this. Like having that verification layer, I think is still very important.
But this is also important when you um handwrite code. But it's definitely true that I think when
you handwrite it, you like 90% of the review process happens as you're writing it. I think with
cloud code, we've kind of shifted from like 90% uh coding to 10% review cuz like as you were doing
it, you were already reviewing. With cloud code, it's like 90% coding and or 90% you have to review
it and 10% maybe like hand coding the changes. So, there's definitely a lot more um like importance
in the reviewing phase now. And I feel like a lot of people um have yet to kind of shift their
mindset towards that, where it's like, "No, you have to review more." You can also automate that,
and you definitely have to make that as easy for you as possible with like, you know, permissions
and hooks and all of that stuff just to make sure Claude was sort of following your your design spec
already. But it's it's definitely more important now than ever to be a good reviewer and verify that
the changes for sure. &gt;&gt; Agreed. Yeah. &gt;&gt; [clears throat] &gt;&gt; Um and also kind of
moving on from Claude Code as just a coding uh tool but to beyond that. Uh YC, you've said that, you
know, it's the universal interface your computer and the digital world. You use it for video
editing, uh data analysis, storage cleanup, research, writing, etc. So and you said you even saved
$10,000 using it for research. So can you unpack that and is the terminal really becoming the new
everything? &gt;&gt; Uh yes. So the research thing I can definitely touch on that. But I think in
general I find it interesting how the computer started in the terminal. The computer just used to
be, you know, the terminal that was the whole UI. But then we got these different GUI uh apps and
stuff like that. But now we're back on the terminal which I find pretty exciting. So I use it pretty
much for everything. Uh like, you know, research. If I if I want to go through like a bunch of
Reddit threads and kind of find what the community is saying about a certain thing, I might like
copy and paste it manually or I can just, you know, let Claude Code handle it, you know, fetch
information from different sources. So I find that super helpful for that. On this particular case
about like saving $10,000, that's that's entirely true. Um I guess I can share a little bit more
about it. Basically, I was in the process of, you know, buying a property and I wanted to find a
good realtor. I didn't want to, you know, find it myself. So I had Claude Code basically compile a
list of realtors and I really uh specifically said, "Hey, give me a list of email addresses. Give
give it to me, you know, comma separated so I can like write the email and you know, email them
directly." And that's how I was able to essentially at the end of the day, you know, save $10,000.
&gt;&gt; Lydia, Cloud Code is clearly being used for, you know, more than just writing code. Is that
something intentional from Anthropic side? And how do you think about, you know, the expanding scope
of what Cloud Code is turning out to be? &gt;&gt; Yeah, it's interesting. This is This is kind of
the the backstory behind Cloud Co-work as well, because back in December, we noticed that internally
a lot of our employees were using Cloud Code for non-coding tasks. So, the marketing team was using
it to, you know, create like marketing profiles, um data science, and so on. Um so, we wanted to
build a better harness for these types of of of tasks. And that's how Co-work came out in like a
week, cuz we of course use Cloud Code to build Cloud Co-work as well on the desktop app. Um so,
right now we kind of have two services. So, if you're you're doing anything technical, use Cloud
Code. If you're using something or if you're doing something non-technical, like checking your
email, calendar, booking flights, all of that, Co-work is really good at that. It still uses the
Cloud Code runtime underneath, so it can still do coding, it can still do all of that, but we just
have better like connectors and better system prompts in Co-work to focus on that non-technical
stuff. But yeah, I I also agree with YC. I just ended up using the CLI for everything on my
computer, even certain like kind of software-related things where if I have a video and I don't want
to edit it, or or image manipulation, for example, like I always had to go to like a website to do
that or maybe use like specific software, but with Cloud Code, I don't have to use that that
software anymore. I'll just ask it like, "Hey, please convert it to MP4." Um maybe like, you know,
reduce the volume a little bit. I We edit a lot of our own videos just using Cloud Code in in the
CLI. We generate, you know, simple like audio samples, all that kind of stuff. So, it's really like
the the bottleneck now is just your imagination. Cloud Code is can do pretty much anything on your
computer at this point. &gt;&gt; All right, let's hop into the rapid fire round. I'm going [clears
throat] to read out a statement. All you have to say is agree, disagree, or a reason. You've blamed
Cloud Code for a bug that was actually your fault. &gt;&gt; Oh, yeah. &gt;&gt; [laughter] &gt;&gt;
That's a lie, like &gt;&gt; Uh, maybe. I don't remember though, yeah. &gt;&gt; AI makes senior
developers more valuable, not less. &gt;&gt; Yes. &gt;&gt; Mostly agree. &gt;&gt; Yeah. &gt;&gt;
Depends on the engineer, but yeah. &gt;&gt; [laughter] &gt;&gt; Uh, reading documentation is dead.
&gt;&gt; I disagree. &gt;&gt; No. [laughter] &gt;&gt; I just assumed you guys had it on, like Claude
is reading the documentation for you. &gt;&gt; It's also fun to read documentation, in my opinion. I
like to just curiosity, stay curious. &gt;&gt; Learning a new programming language in 2026 is a
waste of time. &gt;&gt; [clears throat] &gt;&gt; No, I don't think so. &gt;&gt; I would focus more
on software architecture over specific language features, but yeah. &gt;&gt; Can you go back to
coding without AI, you think? &gt;&gt; Yeah, I could. I I wouldn't, but &gt;&gt; [laughter] &gt;&gt;
if I have to. &gt;&gt; Yeah. &gt;&gt; Uh, final question. You know, the one that I ask every guest.
Uh, what is one tool, framework, or workflow that you know, both of you could never give up? And I I
think I can guess, but you know. &gt;&gt; I thought I was going to say Claude code, but I realized I
could build Claude code with Claude, so &gt;&gt; [laughter] &gt;&gt; Fair enough. Yeah, but then you
still depend on Claude code. So, I feel like it's Claude code for both of us then. &gt;&gt; Thanks
for watching. Everything that you've seen in this video is going to be linked in the description box
below [music] from Y K's repository on Claude code tips, as well as documentation showing you how
you can [music] run Claude code on Google's agent platform. To watch more agent factory content,
check out this next [music] video on how you can run agent CLI on agent platform, as well as learn
more about ADK 2.0. I'll see you in the next one.
