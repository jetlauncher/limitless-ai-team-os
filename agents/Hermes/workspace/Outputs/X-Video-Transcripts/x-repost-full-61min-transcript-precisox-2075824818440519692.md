# Full X Repost Transcript - @precisox status 2075824818440519692

## Source

- X repost: https://x.com/precisox/status/2075824818440519692
- Duration from X media: ~3665 seconds (61:05)
- Downloaded/transcribed from X video audio with 5-minute chunks.
- Original-source match for the latter ~46 minutes: Google Cloud Tech - Intent-driven development with Claude Code & Fable 5, https://www.youtube.com/watch?v=6ERUGFurDHY

## Caveat

The X repost is longer than the matched YouTube original. The first ~15 minutes discuss Claude Code internals, permissions, skills, hooks, plugins, MCP, and stateless model/harness architecture. I did not find a confirmed standalone original for that opening segment in this pass.

## Transcript

## chunks_000

ClaudMD, permissions, plan mode, skills, hooks, plugins, MCP, you name it. Everything to truly
personalize Claude code and get the best results out of it. With his deeper understanding of Claude
code, you can master agentic engineering. But the most important thing when working with Claude
code, again, is that the model is stateless. It has no in-session memory, no memory between the
calls. Every time we call the model, it essentially starts from zero. Yeah, so it's up to the
harness to provide all the states. So everything, your files, your conversation history, your entire
setup, your environment, that's all Claude code. But how does Claude code give that? So just to kind
of go back to our prompt, behind the scenes, like the moment you press enter, Claude code assembles
all of this data into one big request, into one big assembled prompt. So way more than we just have.
That's only in user one. So first we have the tool schemas. You don't have to know much about tools
yet, but these define every action that Claude code can take on your behalf. So bash, edit, read,
agent, web fetch, there's a bunch more. These are all in our docs, all the tools. And each one,
like, it's of course visualized differently here, but it's actually a JSON schema. So we have the
name, the description, and the input shape that this prompt has. So the model can read it, or now it
sees, like, okay, if I want to do something, I know that the harness could run a bash command or an
edit command. That's good to know. Again, the model cannot run that. The model will just send it
back to the harness, but we'll see that in a moment. Then we also have the system prompts, and this
is just hard-coded into Claude code itself. Anthropic, like, adds this to the harness. And this
tells, like, the model who it is, like, what tone it should have, the coding conventions, security
rules that we as Anthropic want to enforce, all that stuff. We also have your environment. So that's
the entire environment of your, like, coding session. So the operating system, your shell, which
model you're running, your git branch, all that stuff. So Claude code captures this whenever you
start a session. Okay, and then lastly, and this is kind of the most important one for us, that's
the messages array or the conversation array. So you can see here that we have our own prompts. So
we have the add a test for calc. But we also have the ClaudeMD file contents, if we have a ClaudeMD
file. And a list of all the skills that we might have in our project. We'll talk a bit more about
skills later on, but this is a list of skills and only their names and description. This is, like,
progressive disclosure. We will talk a bit more about this later. But so the first message that
we're sending to the model also has a ClaudeMD file contents, the skills, and then finally our
prompt. Now, of course, realistically, this looks something like this. And if you've used our SDK or
something like that, you should be very familiar with this structure. This is just JSON, like,
request body to the messages API. One kind of subtle, like, thing I do want to say is that the model
doesn't read JSON. Like, it's up to the API to internally turn this into the tokens. The model only
understands, like, these tokens, of course not plain JSON. But that's up to the API side, so either
Anthropic API or Bedrock, all that stuff. So now finally the API gets sent, or the request gets sent
to the API. So now the model sees this request and starts reasoning. It sees the entire assembled
prompt. It's like, well, the user wants to add a test in utils.ts, but nowhere in our assembled
prompts have we added this file yet. So it can't do anything. But what it does see is that in our
tool schema, we have a read tool call. So it does understand, like, okay, if I don't have access to
something, then just use this read tool call. So the response of the model here, or the API, is an
assistance message with this tool call. And in your network, you might see, like, tool use. And this
just, this again is a hint to the harness that it wants to read this file. So this starts that first
message. So only now when the API is responded will it show that read tool call in your CLI. Now
behind the scenes, this might run, like, fs read file or whatever you're using, Bun. But that's,
again, up to the harness because that can use sf read file. Eventually the file contents also come
back as a tool result. And then finally, when it's all successful, it again reassembles that entire
prompt with the exact messages and everything else above. I just kind of didn't want to clutter it.
But this should look the exact same. The only thing that's added here is, again, the assistant
message to the messages array. And then also now the tool result. So in this case, you can just
imagine that might be the contents of the file it just read. Please understand that this is, of
course, kind of pseudocode. Normally, these are just, like, again, the JSON objects. Don't take this
too literally. But it's more just the idea. Plan mode is kind of like permission mode. You know,
we're kind of telling Claude, like, hey, don't code anything yet. Don't touch anything. But

## chunks_001

I kind of want to remember that loop diagram back where the model emits a tool call and then the
harness executes it, but how do we know that what it's executing is actually stuff that we want? So
in our cloud settings JSON, we can also define specific permissions. And I have this pretty early on
in the workshop because I do think it's important that you understand the control you can have over
cloud code and make sure that it won't run anything that you don't want running on your machine. So
first we have an allow list. So this is a list that runs with no prompts. So if you've ever run any
command, like maybe here, now I can say, just make it dark mode. I haven't added any permissions
yet, so I think hopefully it will ask me if it can, yeah, here, if it can edit it because I haven't
told it that I'm okay with editing anything yet. But honestly, this is kind of annoying to like
babysit it like this. I'm like, yeah, I'm sure it's fine. I'm sure you're going to do a good job. So
either, well, we can either set auto mode, but permissions are a bit more deliberate. So first we
have allow, so we can always say like, okay, if the tool call is like npm run, yeah, just do it.
Like don't ask me. If it's a Git commit, maybe you're also always okay with that. But if it's a Git
push, please don't do that. Like don't touch any of my remotes. That's fine. If you always wanted to
ask, I mean, removing, honestly, I kind of always have it in ask. It's annoying to have it in deny
because then you just end up with so many like stale files that should have been deleted. So if
there is an RM, just ask, and you can also have a default mode. Okay, the best thing, I think, is to
control this with our built-in slash command called permissions. I'm just going to kind of exit this
if you don't mind. So we can run permissions here. And here you can either, you can add a new rule
if you want. You can also just see the other rules. So the only kind of annoying thing is that you
have to know which tools are available and what you, like, how you kind of write this permission
type code. But this is a very easy way to add these permission rules. Otherwise, we just have to do
it explicitly. So we can go to .claud, settings.json, and in here we can have like deny, ask all
these things. But we just added another command, which I really like. I'm just going to restart it.
And that is fewer permission prompts. And what this does, I'm just going to show you. I mean, this
is like a brand new laptop, so I'm curious if it'll see anything. It'll go through all your
transcripts and it will try to find the tool calls that you've been asked the most. So if you've
already run a couple sessions and you're like, I always see the same type of tool calls and I keep
allowing this, but how do I add this to my permissions? Fewer permission prompts is really good for
that. Let's see what it actually ended up with. Oh, so here. So it saw that I kept just like
accepting my linear MCP server and the bash bun run type check. So it added two of these to my
settings.json without like me having to touch it. It also skipped a few and it will tell you why.
The instructions say when in doubt, leave it out. It's already auto allowed by cloud, so no rule
needed. Mutating office. So it's also like very conservative with what it does add. So it still
thinks like, okay, is what I'm allowing actually safe? Is it like maybe like redundant? Do I not
want to add it? So anyway, I just wanted to point that out. If you, because if you've been using
cloud code for a while, there are so many kind of newish commands that are, that can be very useful
to your workflow. So question, the settings then, since we have them in, I guess as a personal
global setting and then per project, what happens if they collide with each other? So the highest
one has like as precedence, if that makes sense. So if you have something in managed settings, so
all the way up to your enterprise that will always take precedence, then it's like your user and
then goes down for project. So basically we want to make sure that as an individual team member, an
individual team's team member's permissions cannot override what your team or your company set up
for you. So the highest ones, the one that's most up, so it's almost like reverse hierarchy in that
sense, where the one that's closest to root wins and then it goes all the way down. I'm just going
to add a deny rule here with maybe bash, or actually I'm going to add a deny rule here with edit
package.json. And I'm just going to see what happens. Ugh, Git. Oh, because it created it for me,
right? Wait, don't save. So this is just a settings that Claude made for me, which is actually
pretty nice. But now I also want to add a deny rule, and I just want to see what happens. So if I
want to deny maybe, yeah, edit package.json. And now I'm going to still ask Claude to edit it for
me. So I'm just going to actually change this model to haiku because again, this is just a very
simple task.

## chunks_002

Fine. So I'm gonna, like, update the version in package.json to, I don't know what it is right now,
to 1. Now, hopefully, my permissions were set up correctly, and it will be like, can't do that. Oh.
Like, ignore it. Or see, I'm not sure if I now, like, prompted it to ignore the permissions. We'll
see. Hopefully not. No. Yeah, so it says, like, oh, I can't do that. So even if this was a tool call
coming from the model, it won't run it. So this is like a great way to add more control over what
Claude can and cannot do in your environment. We've seen how we can shape the behavior with Claude
MD and how we can guarantee it with permissions, but both of these are kind of passive. There's
often like a lot of workflows or a lot of steps that we want to take in Claude code, and we kind of
want to do it multiple times. And in that case, we can use skills. So a skill is just a markdown
file with a specific procedure. So something you'd otherwise have to, like, re-explain to Claude
every time. It's just repeat it, multi-steps. And in this case, it's just specific to our project.
So this could be anything like deployment or integrations, Q&A loop, anything that you want to do
multiple times, but you just don't want to keep, you know, typing the same prompt over and over. So
in our, or actually, before I start typing it myself, a really nice prompt that I like to use is
skill creator. I believe this is built into Claude code. Sometimes I add different plugins to my
environment, and then I forget whether this was built in or if I added it. I believe this one is
built in. And this one makes it super easy to add your custom skills. So for this one, let's say,
what skill would you like to have worked on? I might just see, like, a very simple, like, code
reviewer skill. I don't want to do too much. I just want to see what it ends up with. Also, what I
want to show here is, like, if you have a question or an example, the first thing that should come
to your mind is, like, has Claude code already automated this? Or do I really have to go into the
code base and code it myself? For a lot of these questions, you could just ask Claude and let it do
it for you. So it's kind of like updating your mindset. It's like, how much of my daily life can I
Claude-ify that way? And the nice thing also is that we have a lot of configuration options within a
skill. We can also set the model here. So in this case, it's just reviewing code. So I can just set
it, always use Sonnet. Even though I'm on Opus, whenever this specific skill is invoked, I want to
use Sonnet or Haiku in some cases. What's also nice is, for example, if we never want our model to
review our code, we just want to do it, like, a slash command, we can also, like, use disable model
invocation, true. And in this case, by setting that, we're not sending it to the model. We're only
keeping it locally. So the model can never invoke this skill, only us using it as a slash command.
If we want the opposite, if we only ever want the model to do it, we can set user invocable false.
And I know we, honestly, this should just be one front matter setting. It's two, and they're kind
of, like, negating each other. Just accept it for now. We might change it. But by doing that, just
adding this one, now it's no longer a slash command like we've just run, only the model can do it.
So that's kind of how you get more control over skills as well. Another thing that's kind of nice is
that you can pass arguments to it. And that's just with the normal, like, arguments syntax. So maybe
if we had a skill like find, I don't know, arguments, bugs, or maybe if we had, like, a deploy
skill, maybe we could have, like, deploy, and this is, like, deploys our code base to either staging
or production. Yeah, we can use Sonnet for that. And we can just have, like, deploy. Maybe first
it's like, run the tests, bundle the app, deploy to our environment. Again, nothing is set up, so I
know when I will ask Claude, it will be like, what am I supposed to do? There are no tests and I
can't deploy. But here you can also say, like, deploy to, for example, arguments. And now what I can
do is if I ran, let me just kind of rename this real quick. Rename this to deploy. I'm going to
reload plugins. If I now run deploy, I can just do, like, deploy staging, for example. And now in
our skills, it will always then deploy to staging. So this is, I found, very useful. You have a lot
of control over skills.

## chunks_003

Cloud Code has become one of the most talked about developer tools in the world right now. Engineers
everywhere are rethinking how they can build software because of it. And sitting right here with me
today, I've got Lydia Haley from Anthropic, the company behind Cloud Code. You might also know her
online as the Avocoder, and she's here to pull back the curtain on how Cloud Code actually works and
where it's heading. And I've also got YK Sugi, the creator of CSDojo, and he's also the author of
the Cloud Code Tips repository, which is one of the most popular community resources for mastering
Cloud Code. So if you search on how to get, you know, better results out of Cloud Code, you've
probably landed on his work. Welcome to the Asian Factory, both of you. Before we get into it, quick
one for both of you. What is the one thing about Cloud Code that most developers are completely
sleeping on? I would say auto mode. I mean, it's pretty new, so I get it, but using auto mode, and
we'll go over that a bit more today in your workflows, will enable so much. YK, so your Cloud Code
tips repository has like over 8,000 stars, right? And posts about it keep going viral. So like, what
was the moment that really clicked for you with Cloud Code and what made you start documenting those
tips for other people? It clicked for me right away, you know, I remember I started to use Cloud
Code as soon as it was launched and kind of a quick story about it. I was going through an interview
for my current job at Daft and I built like a demo project for that job interview and I didn't tell
them I used Cloud Code, but they were so surprised with the quality. So even back then, I think
there was like so much promise and I just kept using it. I kept learning and I kept sharing my
lessons. Lydia, so like from the Anthropic side, what's it been like watching the community run with
Cloud Code, you know, like when you see someone like YK building out these workflows and he's
sharing them at scale, like how does that feed back into how the team actually thinks about the
product? Yeah, I feel like most of my job is watching these power users like YK use Cloud Code and
seeing how they're using the tool. I feel like everyone uses it slightly different. How we use it
internally might not be how people use it externally. Even all the engineers on the Cloud Code site
here, we all use it differently. So it's extremely important for us and we really enjoy getting all
this feedback and seeing all these patterns coming from the community because it really helps us
shape our roadmap as well, see what's missing or what features we need to add or improve. We kind of
hear now the term intent-driven development actually being thrown around a lot and the idea, you
know, where you're telling Claude what you want to build rather than how to build it. So YK, what
made that shift for you and what made you start, you know, sharing that? First of all, there are
many different terms for it, but I personally like this term because to me, it's not about the exact
prompt. You know, sometimes people say, oh, use this prompt and you get better results. Sure, maybe,
but to me, it's more about expressing what your intent is exactly, knowing what your intent is
exactly, what you want to build, and then just being able to express it. So one thing I recommend
that people do is using your voice to type instead of using your hands to type. And one way where
it's better is, you know, so that you can express your intent faster. You might make mistakes. You
might say, um, but it doesn't matter as long as, you know, you're able to express it. Yeah, Lydia,
I'd love your take on that too. When, you know, Anthropic kind of thinks about how developers should
be working with Cloud Code, does intent-driven development match how the team designed it? And, you
know, what's it been like watching kind of the community shift in this direction? Yeah, I like the
term intent-driven development. I feel internally, we do focus a lot on making sure people
understand that Claude needs verification, right? And I feel like that's kind of part of intent.
It's like, part of it is how you structure your prompt. I still feel like having a software engineer
background does help refine your prompts and you can tell Claude a lot better what you actually want
it to do. So in that case, you know, like using plan mode, adding like images as verification, I
feel like it's kind of part of the intent. But also voice mode, by the way, I still have to use it.
It seems really fun. I feel like I probably would prompt a lot better if I'm not in my head as much
because I think I noticed when I type a prompt, I'm like, ah, maybe I shouldn't ask this. Maybe I
should do something else. But just brainstorming out loud might actually be very fun. I still have
to use it. But yeah, just like, I feel like it does show.

## chunks_004

Pattern words, like we want people to use cloud code the moment they have an idea, and we wanna make
sure that kind of that friction point going from your idea to an actual deployed website is as small
as possible or as easy as possible. So yeah, again, this is also a great community feedback. I feel
like we might focus more on these types of patterns. It's like, hey, you can use cloud code the
moment you have inspiration, just talk to it, brainstorm maybe in plan mode, and you know, get your
website deployed quickly. I love that. And also, I noticed that I love using VoiceMode too because I
feel like I'm much quicker at talking than I am at typing, so I'm getting frustrated at how slow I'm
typing, so I just switched to VoiceMode. I think what's also been really exciting is that, you know,
Cloud Code is not just a solo developer tool, it's also being used at enterprise scale. So like
Cloud Code can now, of course, you can run it on Google Cloud Agent platform. So when you're
actually ready to go from just experimenting to actually rolling this out across your team, the
platform is already there. So let's actually get into some of the super exciting demos that we have
planned. YK, you and I are going to kick off the first demo together. So in this demo, I'm going to
show you how you can set up Cloud Code on Agent platform. And YK is actually going to demonstrate
how he built something really cool on there. First, I'm going to quickly show how you can set up
Cloud Code on Google Cloud. And then this is going to be the foundation, right? So what I've done is
I've installed Cloud Code on my Mac already. And if you have not done that, you can do this super
easily by running these following commands. And then what I'm going to do next is actually install
GCloud SDK if you don't already have that. That's a great place to start because we're going to be
using GCloud to run all of these commands. And then I'm going to set my project ID, which you can
get from your own Google Cloud console. So I'm going to set my project ID. And then I'm going to
enable Vertex AI APIs, which will allow us to use all of the cloud models. And next I'm going to
enable a bunch of other variables, which will essentially enable the Vertex AI integration for
cloud. And all of these commands can actually be found in the links that I'll be leaving in the
description box below. And then once I've done that, I can just start cloud and now it's going to be
running on Google's Vertex AI. And off to you, YK. Thank you so much for that, Smita. What I'm going
to show here is essentially a demo of what I would call Intent-driven development. And I'm just
going to get right into it. And as I wait for the output to come in, hopefully I'll have some time
to discuss these tips and share some of these tips. So here I'm just going to start prompting. I'll
say, I want to create a 3D game. It's going to be a slingshot game where you're going to have a
stationary slingshot right in front of you, fixed camera, fixed slingshot. And I want to be able to
drag a ball that's attached to the slingshot in X and Y directions. So dragging should determine the
X and Y directions or the coordinates. And the duration of how long I'm holding the ball should
determine the Z direction. So that way I should be able to control the ball in three directions. And
whenever I release it, how far back it is held, the faster it should shoot. And what should I use to
build that? I want it to be all front end, HTML, JavaScript, and CSS. Feel free to use libraries if
you need to, but tell me the options I should use. I think that should be good enough. So as I said,
this is exactly what we're doing, building a slingshot game. And one quick tip I want to share is
setting up an alias. And your commands, you know, might look like it like this depending on the
exact OS you're using. So this is so that you don't have to type cloud every time. I mean, you can
if you want, but you know, this is a little bit faster for me that way. Okay, so here we have, you
know, different options. And this model is suggesting 3js, hand-rolled physics. I don't think I want
a hand-rolled physics, 3js plus Canon. I actually remember there is another option for physics. I
remember there is another option for physics that's not Canon. I don't remember what it is. Can you
remind me? Let's see if that works. So as you can see, I've been talking to the agent with my voice
here as I recommended earlier. There are a couple of different options for it. You can just use, you
know, the slash voice option or alternatively a dedicated desktop app. I actually built a desktop
app.

## chunks_005

Or myself, just for me. And that uses a local model. So if you want to go that route, there's that
option too. So we have ammo, rapier. So let's go with rapier. I did a little bit of research
beforehand. Let's go with rapier and 3.js. And then I'll say, let's create a new folder for it.
Let's call it something like slingshot podcast because I'm building this on a podcast. And just
build the slingshot. I don't have to have any targets right now. All I need is the slingshot, fixed
camera, as well as a way to control it and release it. And then I'll just say, manually, let's use
Vite for building it. So you may have noticed that I'm in the projects folder. And I personally like
to do it this way where I have most of my projects in a single folder. It's not necessarily for
everyone, but I highly recommend it so that it's convenient for the agent to be able to, you know,
refer to different projects and you can say stuff like, I want to take this element from this other
project and this other element from this other project and combine them into a single project. So
it's pretty helpful for that. And as you may have noticed, it's helpful to start with broader
questions first and then dig deeper as you go. So these might be questions like, you know, what
architecture should I use, what libraries, frameworks should I use. And then sort of go back and
forth with the agent to refine your idea over time. And I'm confident enough of this model that it
knows enough for this particular problem, but if it needs more latest information later, kind of
community feedback and stuff like that, you can ask it to do research on your behalf as well so that
you can make better architectural decisions. Do you ever use plan mode for this or do you just ask
Claude, like, hey, don't code anything yet? Because we have a specific plan mode, but often I just
end up talking to Claude instead, like a coworker. What do you prefer, YK? I don't think I ever
explicitly turn on plan mode, but I know it sometimes does that on its own. So that's kind of how I
do it. All right, while the output trims in, I'll just keep going with the tips. So number five is
you want to learn to use Git and GitHub CLI well. And just CLI commands in general, because it turns
out CLI is really, really powerful. There's so much stuff that you can do, you know, just starting
with Git and GH. So definitely learn to do that. And here, what I'm going to do is it looks like it
created this folder and the result is already coming in. But I'll just go in a new tab and I'll say,
if this project is not a Git project yet, turn it into a Git repository and then create a public
repository out of it. So I'll just do that in this other thread. It looks like it's actually testing
it itself. I didn't ask it to do it, but it looks like it started it in playwright, testing it. But
I should be able to personally test it myself here. All right, it looks like It's sort of working.
Nice. All right, it looks like it's working. Commit if you haven't yet. And let's show the
trajectory before I release it so I know where the ball is going. I mean, I guess it depends on how
hard you want to make it, but I think it's more convenient that way. All right, so it looks like it
was able to create this project, open it for me. I think it used the open command in the terminal
because I didn't open it explicitly. And going back to the browser here. All right, it's getting
confused with like the different agent doing the work, but I should be able to figure out what it's
doing here. Looks like it's adding this trajectory feature. Not quite there yet. All right, nice. So
it's got the trajectory. I think I can go to the next tip as it finishes the work. You want to learn
to verify the outputs. There are a few different ways to go about it. As I just showed, you can
directly verify the behavior of the app, not necessarily the code, but you can also check the code
yourself if you want and you can

## chunks_006

Also automate, you know, the process of verifying the output as much as possible by writing tests,
by writing GitHub actions, and things like that. It's much better. It looks like, and it looks like
it's committing the trajectory feature. That's perfect. And next up, I think this is going to be the
last feature I'm gonna add here. I want to have a few big targets in front of me, in front of this
slingshot. They should be like disc circular targets. And when I hit them, I want to have satisfying
visual effects, maybe like them shattering into particles or stuff like that. So as you may have
noticed, you know, these prompts sometimes are a little bit vague, but as long as your intent is
clear enough, you know, that I found that Claude is able to figure out what I mean, even if there
are like typos or transcription mistakes, you know, it's basically smart enough. And meanwhile,
while we wait for that particular feature, what I'm gonna say here is this project is almost done.
So let's give admin access because I think this is still a private repository to the following user.
That's Lydia's GitHub account that I pulled from the different screen. And it's saying, let's add
shatterable targets, plan three big bullseye discs at different distances, hit detection that
catches the ball crossing the display. Looks good. And this thread is running these GH commands so
that Lydia should be able to get an invitation with admin permission on this project soon. And it
looks like this thread is just finishing up with these targets. Nice. It might actually not reload
automatically. That might be something to fix next, but I think it's already a pretty satisfying
game. I feel like this was such a good example of your intent-driven, like the first moment that you
wanted to use a specific physics library. I feel like that that's also very perfectly shows like
having more context around what you want to build helps so much. Definitely. I think the rule of
thumb is you ask more questions when you have less context because I didn't know about these
particular physics libraries. I needed to ask questions earlier. But now that I'm a little more
familiar, I can ask. I mean, just like in a real colleague, right? Like you would still talk to them
before you implement something. So just to wrap up this demo, I think one last prompt I'm going to
do. I think it was trying to like test the app for me, but it doesn't have to do that. I'll say, all
right, let's commit and push, but don't push directly into main. Instead, create a new branch
because I want to sort of simulate, you know, the process of code review and then push that branch,
create a draft PR, and then open it for me using the open command. And that should be able to wrap
up this demo because one of the tips I had, actually, I have this whole section about managing your
code base. But one particular quick tip I had is creating a draft PR. You know, you can just ask the
agent to create a draft PR just like I did and then check it before marking it as review so that,
you know, people will know, OK, this PR, maybe it was created by the agent. It's not ready for
review yet or, you know, it is ready for review. So I think it makes things clearer. As you can see,
it's doing Git push here using Auto mode here, as you can see. GHPR create, draft, title, and body.
It's opening it for me. And that's it. I'll just say ready for review. You know, if I want, I can
check the code manually or, you know, interactively using a code. And then I'll just merge it here.
And that's it for the demo. I think this is such an awesome and Lydia, as Lydia was mentioning,
right? It's like, you know, seeing the intent driven development. I think this is like a super clear
example of that. And then so now the source code is kind of going over to Lydia for her demo. So
Lydia, it's your turn. I'm super, super excited on what you're going to showcase for us. Yeah, let's
get started. OK, so basically first what I did over the weekend is I pulled one of my case GitHub
repositories because he already showed me kind of the game that he wanted to build, which by the
way, this is such a difficult level to pass. I have not been able to do this. But when I see this
game, this is already really impressive, but I want to make it a bit better, right? To make it an
actual game.

## chunks_007

game, I might want to add more levels. I might want to change the environment per level, all that
kind of stuff. And I'm going to use Claude, of course, to help me out there. And what I really like
to do instead of, you know, prompting Claude with the changes I want to make, I really like to use a
visual flow. This is all created in Claude Design. I don't know if you've used Claude Design yet.
It's new in our research preview, but basically, you're able to create presentations, slides, entire
websites based on your prompts as well. It's basically Claude code, but for design. But I really
like having this visual approach for a plan. This is just HTML at this point. I could have also
exported it to Figma or Canva or anything else. But this allows me to really think about the plan
and the changes I want to make. So, for example, here, Claude came up with this Slingshot V2. So how
can we actually make it into a game? So we have the game flow with a main menu. We have a level
select, game play loop, all of this. Some more like visuals that we want to add here. The gameplay
screen. And this is all HTML. So this is pretty much already kind of what we had here, but we have
some health bars and also some systems to design. So we have the health bar here again, the charge
and aim. We already had this, or at least in the demo that YK just showed in the original didn't
have this yet. We have some haptics, which I think are nice to add if you're like on your phone, you
kind of want to feel, you know, that something is like pulling and then smashing the plates. And of
course, also scoring. We have some extras that maybe they want to add as well. The different levels,
which I think looks so cute. So again, this is all Claude Design. Claude came up with this. Okay, so
this is basically all the prompts that I gave Claude Design. So this is in Claude Design itself. And
the nice thing is that I can also just edit everything. So if maybe I want to change some of the
planning, I don't want to say slingshot here. I want to say a slingshot, whatever, it doesn't
matter. I can just do that and then I can later export this and use this as my prompt to Claude. So
what I did for the design wireframe is I just added it to my demo assets here. So this is all just
HTML. The entire plan that we just saw with the different screens and everything else is just here.
So now I can just open Claude real quick. Claude is already running here. And to make this, you
know, use the agent platform. It's already running on Vertex AI, but how I did it is that we
actually have a really nice built-in wizard called setup Vertex. So we have setup Vertex. And when
you run that, it'll automatically do most of the setup that we just saw. So for example here, I can
just say, okay, I want to use my application default credentials. Perfect. I want to use a different
project. This one is called project YRS on scratch of food. I'm going to do global. It's going to do
a quick check to haiku, just making sure that everything is set up correctly. And it's going to see
which models we can use here. Here we see that we have access to Opus 4.6. We can also enable more
in model garden and Google itself. And we also have access to Fable 5, which I'm very excited about.
I'll be using Fable for this demo specifically. I want to pin the working models to 1 million, save
it. And now we're good to go. So anyway, that was a quick setup. So now we're still running on
Vertex just like we saw before. The only thing what I really enjoy doing is using auto mode. And by
default in agent platform, that is an environment variable. So we actually have to turn that on
first. I'm actually going to quit this real quick. I'm just going to clear it. You can do this by
doing export cloud code enable auto mode. So now with that enabled and cloud restarted, we can now
see with a shift tab that we have auto mode here. And you could also see why K was using auto mode
as well. The nice thing about auto mode is that it makes it so much easier to just kind of not be as
hands on. So just to show real quick what it is, if you've used cloud code, you may have noticed
that you can use, you know, ask almost like ask everything, in which case cloud code will always ask
you like, hey, is it okay if I delete this file? Is it okay if I run this command? And after a
while, you're just like, yeah, go ahead, like whatever. And we call this a permission fatigue where
I do think it's very important that before cloud does something dangerous, it has to make sure that
it should be doing that. But at a certain point of ask or if cloud asks you questions, like every
time you won't read them as much anymore because you're kind of like, you've asked me like a hundred
times now, sure, just go ahead. That's permission fatigue, which is also dangerous. And then
previously, we also had the option to buy a dangerously skip permissions, in which case cloud will
never ask you anything, which is also not great because if it's about to like delete your root file,
there is no going back, right? So auto mode is our solution to that. It kind of sits in between your
deny list and allow list. So auto mode runs a different classifier between all the tool calls. So it
kind of thinks like, okay, is this tool call dangerous? First of all, if yes, okay, let's ask the
user if.

## chunks_008

Actually want to do it. But if it's just a normal like read or edit or something else, then no,
that's not dangerous in most cases. And let's not ask them, let's not bother them. Another thing
also is that it's much better against prompt injection. In some cases, a tool called might just be
like, ignore all instructions, that kind of stuff. Because it runs a classifier in between, it's
much better at catching that. Also, another nice thing is that it's more context dependent. Like, if
you're asking Claude, delete this folder, in some cases, that RMRF might be dangerous, but if you've
specifically asked for it, it's not dangerous. So in those cases, automote won't ask you because you
asked to delete it. It's not a dangerous thing. So this is a very nice way of working, and this
actually enables you to use Claude code or to run Claude code way more autonomously in these longer
running sessions. But anyway, so far, we haven't done anything yet. So I wanna implement that entire
wireframe that I just showed using something called dynamic workflows. And this is a new feature
that we've just added. And you just ask Claude to use a dynamic workflow. It's not a slash command,
it's nothing else. So I can just do like read this design file and use a dynamic workflow to rebuild
the game and match it. And I added it to my demo assets so I can just see demo assets. It was in
design wireframe. Yeah. So what I'm doing now is I'm giving Claude a way to verify and understand
what I wanna build because it has this HTML, it has the context. I could have made this prompt like
a lot more specific. I'm like, okay, add all these levels, add all these other features. But
honestly, I'm kind of just waiting to see if Claude will understand it. So in this case, we're going
to wait a little bit. I would kind of also prepare it like a cooking show. So if this takes quite a
while, there is a tab in which this is already finished. So we can always just go there. But it's
always interesting to see what Claude comes up with. So kind of to quickly explain what a dynamic
workflow is, again, I created a little visualization. Hopefully this kind of makes sense. So sub-
agents themselves aren't new. If you've used cloud code, you may have noticed that sometimes it
spawns a new sub-agent to perform a certain task. A sub-agent is essentially another cloud code
instance with its own context. And it's really good at just like focusing on that specific task. But
if you're just asking Claude every time to like use sub-agents, you don't even have to ask it. The
downside is that it's very non-deterministic. You know, sometimes it might spin up four sub-agents,
sometimes it might not even use sub-agents. The other time it uses 10 sub-agents, all that kind of
stuff. With workflows, it's kind of our deterministic solution to that. Workflows also spin up a lot
of sub-agents, and that's a feature. It can go into hundreds of sub-agents because like this is a
feature for tasks that takes hours or days or like these really long-spanning tasks. But the nice
thing is that cloud code actually generates a JavaScript file. And we'll see that in a moment as
it's like, eventually it will kick off the workflow. But you can see that JavaScript file and you
can save the workflow to then rerun it later on as a slash command. So if you really like a specific
kind of steps that cloud code took with specific sub-agents, you can save it and rerun it in that
very deterministic way. And because all these sub-agents run in parallel, you can also achieve a lot
more within usually the same amount of time as a single sub-agent would have, because it's parallel.
And what you'll see is Claude is pretty smart at like kind of delegating these sub-agents to be very
focused on the specific task. Okay, so just like a cooking show, I figured that Claude would take a
while to kind of spin this all up. That's all expected. Fable is a bit slower because it's such a
large model. But here I showed the exact same command. This is also what I just typed in my other
terminal, right? Read this design file and use a dynamic workflow to rebuild this game and to match
it. It's the exact same HTML file as well. And it then ran this workflow and we can see what it ran
with the workflows slash command. And here you can see that it ran this specific workflow. So here
we had four agents in the build phase. We had build engine, build UI, build audio, and levels and
haptics. We then had an integration phase. So this is another sub-agent, a review phase, and a
verify phase. So these phases run sequentially, but the actual build agents all run in parallel. You
can see that this is all fable five. We can also go into it. And the nice thing is that if we like
this workflow, in this case, it's like rebuilding a game, so it doesn't make too much sense to save
this, but we could by just pressing S. And then we could do like save dynamic workflow and save as
rebuilt thing showed game. Sure. For this demo.

## chunks_009

I'll save it as that. And now you can see that it's saved this JavaScript file. So I'm kind of just
want to open it and see if I can open it this way. I'm just gonna remove this. And you can see that
this is a JavaScript file that CloudCode created for this workflow. I didn't type this. This is all
cloud. And you can see that it's just a normal function. It's like a build phase. We see all the
builders. We see the prompt that it's using for all these sub-agents. We have a review phase, all
that kind of stuff. So if we want to, we can also be very specific here. Maybe I don't want all sub-
agents to use Fable like I did here if we go into workflows. You can see that it all used Fable 5.
In some cases, I don't need a model that's strong for this sub-agent. Maybe I wanna use Sonnet or
Opus. We can just ask Cloud, of course, to change that. We can just ask Cloud, like, hey, please use
Sonnet for all your sub-agents, but we can also actually see it in our code and edit the code
itself. And again, because this is all just a JavaScript file, this is deterministic. So then every
time we invoke that slash command, it will just run these exact same sub-agents. So that's
incredibly nice. I'm just gonna see what it came up with. I've run dev. So, yeah, it uses Workflow
to rebuild it according to our design spec. Let me see if it actually made it look good, though. So
it actually did make it almost in the exact same, like, design pattern with this kind of, like, draw
look. But it definitely added some levels. It added, I don't know if you can hear it, it added,
like, audio to the levels. And it actually made it into a real game. So now we have different
levels, everything else. So almost exactly like our original design, like, spec here. So honestly,
I'm happy with this. I'm not sure if I can clear all these levels. It's honestly very difficult.
Thank you both for those wonderful demos. So, like, let's kind of zoom out and get into some bigger
ideas. YK, your entire repo is a playbook for maximizing what CloudCode can kind of do autonomously.
But you also have tip number 38, which is, you know, simplify over-complicated code, where you kind
of note that code generation models have a bias towards writing more code than needed. So how do you
kind of balance the rapid prototyping with the discipline of actually keeping things clean? So I
think, in general, they have had that tendency over time, but it really depends on the particular
model that you're using. And depending on that, it might be able to generate concise code. But the
general principle that I try to convey through this particular tip and other tips on this repo is
that, you know, you want to be in control of the code, not necessarily, like, totally in control,
you know, micromanage everything, but in a way to make sure that your code quality is good, your
output quality, the behavior is correct, and all of that. So I would say just in general, you know,
don't necessarily commit all the code that's generated. Make sure that you only commit and, you
know, merge the ones that are important and valuable to your code base, and you need to be the
decider of that. So Lydia, with agents writing more and more code, what does understanding your code
base actually look like in 2026? So, and how do developers kind of stay in that privacy? Yeah, the
way I see it is, I think the role of the software engineer is changing more to be almost like a
product manager. At least that's what I've noticed. And also, it feels pretty logical. Like as a
software engineer, you're not just writing the code, but you are in charge of owning it,
understanding the architecture that you wanna build. And it's still up to you to kind of understand
why we need to implement a feature, all that kind of more of like product manager stuff, but we
still definitely need the technical expertise, almost with the intentional design that YK mentioned
is still very important. I always like to kind of draw a comparison to, like, I can write TypeScript
or JavaScript, but I'm not gonna focus on the machine code that gets generated afterwards. And it's
almost like, it's almost pretty similar where it's like software engineering used to focus on the
actual code syntax, almost like, you know, how machine code might've mattered, but we're going a
layer above that now. I think what's more important is understanding the architecture, understanding
the feature and understanding still what the shortcomings are, but then also building the right
environment for Claude around it with hooks, permissions, CloudMD file, that kind of stuff. And it
still requires a lot of technical expertise and good taste and high agency. Can we also talk a
little bit about what your own setup is? You're literally on the team that, you know, builds cloud
code. So you're probably the best person to ask this, you know, you're also shipping fast. I see all
of your content on like YouTube or LinkedIn. So what's kind of your personal cloud code workflow and
how does that look like? Personally, I think I really want to focus on setting up as many routines
as possible.

## chunks_010

Have a lot of um like um proactive or scheduled cloud code sessions kind of always keeping me in the
loop. And it's not just cloud code. This is just cloud in general. I kind of see cloud's entire
ecosystem more as like, okay, what is the problem I'm trying to solve because we have cloud code, we
have cowork, we have chat, um, where I try to like agencify or cloudify as much in my life as
possible. And I don't want to cloudify the things I actually enjoy doing. For example, I really, I
sound weird when I say this, but I really enjoy creating keynote slides. And I used to use cloud
code to automate that as well because we have computer use and it can actually do a lot on your
behalf. But I noticed like I kind of just enjoy doing this and I don't want cloud to do this. This
is like, you know, kind of my creative outlet. And then of course with cloud code, like we have the
cloud bot running on all of our like our issues and our PRs, so cloud automatically auto fixes all
of our PRs as well. Like YK after your demo, I was like, oh, I kind of just want to run auto fix PR
now. I don't know if you've set that up, but if you've installed the cloud app on GitHub, basically
what happens is if your CI fails or someone leaves a comment, cloud will automatically try to fix it
until your CI is green. So if a co or if a teammate leaves a comment like, hey, you forgot to add
this or that, cloud will take that feedback and try to fix it and immediately push it to that
branch. So all of these um like systems, everything we've set up is just to be as out of the loop as
possible and just kind of letting cloud do its thing, which sounds scary. But with the right hooks
and permissions and, you know, using sandboxes and all of that stuff, you get really, really far.
And also, of course, we're kind of trying to push it as far as we can because like we are at Thropic
still cloud code's number one user. It's like, okay, we want to make sure that the features we're
building are features that we like on the team. Um, yeah, so mainly that. I love the term cloudify.
I don't know if that is an official term which is used internally, but yeah, I think using just like
in general, like just using AI to automate the things that you don't want to do so that you can
enjoy doing the things that you like doing more. It kind of reminds me, I was on X the other day and
someone built an app to respond to their partner. And I was like, maybe we're optimizing too much.
Now you just got to be like scared that your partner is doing that all the time. Like, you're right
to push back. You're absolutely right. Okay, so YK and Lydia, I also want to get your take on kind
of what's happening in the developer community recently, right? Like we have all of these, you know,
coding agents out and then, but at the same time on Hacker News, and I'm on Hacker News a lot, I see
a lot of like popular posts kind of like saying, I'm going back to writing code by hand or, you
know, an AI coding agent needs to reduce your maintenance cost, not just write code faster. And so
it seems like there's a real conversation about kind of craft control, uh, technical debt, you know,
so what are your thoughts on that? Um, YK, I know you have a lot of tips on this. You said, you
know, the best way to get better at cloud code is by using it, right? Uh, you also said, be braver
in the unknown. So you're very clearly all in. So what do you say to developers who feel like
they're kind of losing their craft? My personal philosophy at the end of the day, it is a tool. Um,
so I, I'm not sure if this is the right analogy, but you know, it's sort of like as a painter,
instead of using a regular brush, you're using an electric automated brush. So you're responsible
for the output. That's the first thing I, I really, really wanna emphasize because I get frustrated
by this kind of discussion whenever I read it. You know, people say, oh, you know, people produce
like so much code and it's not, it's not good with AI in general, not just cloud code. And I say,
okay, don't produce it then, like, don't, don't push it. Like, as I said, there are so many ways to
review code, make sure it's good before it goes into production. You know, if it's like a one-time
uh vibe coding kind of casual projects like the game I built, that's totally fine. You don't have to
check the code, but if it's more of a serious production, you know, code base that you want to
really be secure and safe about, then, like I said, create a draft PR, make sure it's good, review
it manually or with AI. If you generate a hundred thousand lines of code, you don't have to commit a
hundred thousand lines of code. That's, that, it's not necessarily the way it is, you know, just
commit what you think is right and at the end of the day, you're responsible for the tool and the
output. Yeah, I can also only agree, agree with that. I feel like you still need to verify and like
you're really good at this. Like having that verification layer, I think is still very important,
but this is also important when you um hand-write code. But it's definitely true that I think when
you hand-write it, you, like 90% of the review process happens as you're writing it. I think with
cloud code, we've kind of shifted from like 90% uh coding to 10% review because like as you were
doing it, you were already reviewing with cloud code. It's like.

## chunks_011

90% coding and or 90%, you have to review it and 10% maybe like hand-coding the changes. So there's
definitely a lot more, um, like importance in the reviewing phase now. And I feel like a lot of
people have yet to kind of shift their mindset towards that, where it's like, no, you have to review
more. You can also automate that, and you definitely have to make that as easy for you as possible
with like, you know, permissions and hooks and all of that stuff just to make sure Claude was sort
of following your, your design spec already. But it's, it's definitely more important now than ever
to be a good reviewer and verify that the changes for sure. Agreed, yeah. Um, and also kind of
moving on from Claude code as just a coding tool, but beyond that, uh, YK, you've said that, you
know, it's the universal interface, your computer and the digital world. You use it for video
editing, uh, data analysis, storage cleanup, research, writing, etc. So, and you said you even saved
$10,000 using it for research. So can you unpack that and is the terminal really becoming the new
everything? Uh, yes, so the research thing I can definitely touch on that, but I think in general I
find it interesting how the computer started in the terminal, the computer just used to be, you
know, the terminal that was the whole UI, but then we got these different GUI apps and stuff like
that. But now we're back on the terminal, which I find pretty exciting. So I use it pretty much for
everything, uh, like, you know, research, if I, if I want to go through like a bunch of Reddit
threads and kind of find what the community is saying about a certain thing, I might like copy and
paste it manually, or I can just, you know, let Claude code handle it, you know, fetch information
from different sources. So I find that super helpful for that. On this particular case about like
saving $10,000, that's, that's entirely true. Um, I guess I can share a little bit more about it.
Basically, I was in the process of, you know, buying a property and I wanted to find a good realtor.
I didn't want to, you know, find it myself, so I had Claude code basically compile a list of
realtors and I really specifically said, Hey, give me a list of email addresses, give it to me, you
know, comma separated so I can like write the email, you know, email them directly. And that's how I
was able to essentially at the end of the day, you know, save $10,000. Lydia, a Claude code is
clearly being used for, you know, more than just writing code. Is that something intentional from an
office side? And how do you think about, you know, the expanding scope of what Claude code is
turning out to be? Yeah, it's interesting. This is, this is kind of the, the backstory behind Claude
CoWork as well. Because back in December, we noticed that internally a lot of our employees were
using Claude code for non-coding tasks. So the marketing team was using it to, you know, create like
marketing files, um, data science, and so on. Um, so we wanted to build a better harness for these
types of, of, of tasks. And that's how CoWork came out in like a week because we, of course, use
Claude code to build Claude CoWork as well on the desktop app. Um, so right now we kind of have two
services. So if you're doing anything technical, use Claude code. If you're using something, or if
you're doing something non-technical, like checking your email, calendar, booking flights, all of
that, CoWork is really good at that. It still uses the Claude code runtime underneath, so it can
still do coding and it can still do all of that, but we just have better like connectors and better
system prompts and co-work to focus on that non, non-technical stuff. But yeah, I, I also agree with
YK. I just ended up using the CLI for everything on my computer, even certain like kind of software
related things where if I have a video and I don't want to edit it, or, or image manipulation, for
example. Like I always had to go to like a website to do that or maybe use like specific software.
But with Claude code, I don't have to use that, that software anymore. I'll just ask it like, Hey,
please convert it to MP4, um, maybe like, you know, reduce the volume a little bit. I, we edit a lot
of our own videos just using Claude code in, in the CLI. We generate, you know, simple like audio
samples, all that kind of stuff. So it's really like the, the bottleneck now is just your
imagination. Claude code is, can do pretty much anything on your computer at this point. All right,
let's hop into the rapid fire round. I'm going to read out a statement. All you have to say is
agree, disagree, or a reason. You've blamed Claude code for a bug that was actually your fault.
That's a lie, YK. Uh, maybe, I, I don't remember though, yeah. AI makes senior developers more
valuable, not less. Yes. Mostly agree. Yeah. Depends on the engineer. Yeah. Uh, reading
documentation is dead. No, disagree. No. I just assumed you guys had it on like Claude is reading
documentation for you. It's also fun to read documentation, in my opinion. I like to just curiosity,
stay curious. Learning a new programming language in 2026 is a waste of time. No, I don't think so.
I would focus more on software architecture um, over specific language.

## chunks_012

Can you go back to coding without AI, you think? Yeah, I couldn't. I wouldn't, but... I have to.
Yeah. Final question, you know, the one that I ask every guest, what is one tool, framework, or
workflow that, you know, both of you could never give up? And I think I can guess, but, you know. I
thought I was going to say Cloud Code, but I realized I could build Cloud Code with Cloud, so. Fair
enough. Yeah, but then you still depend on Cloud Code. So I feel like it's Cloud Code for both of us
then. Thanks for watching. Everything that you've seen in this video is going to be linked in the
description box below, from YK's repository on Cloud Code tips, as well as documentation showing you
how you can run Cloud Code on Google's Asian platform. To watch more Asian factory content, check
out this next video on how you can run Asian CLI on Asian platform, as well as learn more about ADK
2.0. I'll see you in the next one.
