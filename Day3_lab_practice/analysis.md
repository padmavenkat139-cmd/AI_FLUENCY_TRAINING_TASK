ok tell the process in step by step.Now i have to use Day3_lab_practice 
Pasted markdown(3).md
File
use this as sample model and give the step by step work with other question dont use same fees registration
these are the output

Yes 👍 These four screenshots clearly show the required outputs. We can use these actual outputs in your analysis.md.

Your final observations

1. B3 — Plain LLM

Your screenshot shows that the plain LLM said it could not provide the exact B3 schedule.

➡️ Observation: Without the tool, the LLM did not know the private bus schedule.

2. B3 — With Tool

Your my_agent.py output shows:

Tool: lookup_bus_schedule
Arguments: {"route":"B3"}

TOOL RESULT:
Route B3: Departure: 8:00 AM;
First stop: College Campus;
Final stop: Town Bus Stand.

➡️ Observation: The tool provided the exact information, and the LLM used it for the final answer.

3. B4 — With Tool

Your output shows:

Tool: lookup_bus_schedule
Arguments: {"route":"B4"}

TOOL RESULT:
Route B4: Departure: 8:15 AM;
First stop: College Campus;
Final stop: Market Road.

➡️ Observation: The same tool successfully handled another route.

4. General question — Plain LLM

Your output:

Don’t miss the ride—be at the bus stop on time, every time!

➡️ Observation: The LLM could answer this directly without external information.

One small thing

Your screenshots show the actual terminal outputs, which is exactly what we need. Don't edit the outputs.

For the screenshots folder, you can use these names:

screenshots
├── plain_b3.png
├── tool_b3.png
├── tool_b4.png
└── plain_reminder.png

The exact names don't matter as long as they are clear.

Now we're ready for analysis.md

This is the main written part of the assignment. We will create it next and cover exactly what your assignment asks:

What is an LLM?
What is an agent?
What is a tool?
What is a tool call?
What does the tool schema mean?
Step-by-step tool-call flow
Why the tool returns text instead of stopping with an error
Comparison table
Your 3-question observations
When a plain LLM is enough
When a tool is necessary
Conclusion

We can now 
create analysis.md with your actual B3/B4 results, not made-up results.

Create analysis.md with your actual B3/B4 results

Done. I created analysis.md using your actual B3, B4, and plain-LLM outputs, including the required sections from the assignment.

Download analysis.md

It includes:

LLM explanation
Agent explanation
Tool and tool-call explanation
Tool schema
Step-by-step B3 tool flow
Why tools should return text on failure
Plain LLM vs tool comparison table
Your actual B3 result
Your actual B4 result
Your actual one-line reminder result
Suitability and conclusion

Next, you can put this analysis.md inside your Day3_lab_practice folder. 

analysis.md
Document
this contain the api key.now i have to push this in the github so how can i protect my api key

Yes — do not push your API key to GitHub. 🔐

Your config.py is actually set up correctly because it reads the key from an environment variable:

API_KEY = os.getenv("GROQ_API_KEY")

So the important thing is to keep your .env file private.

Step 1 — Check where the key is

In your Day1_lab_practice, you have:

.env

That is where your actual API key should remain.

Do NOT upload .env to GitHub.

Your project can contain:

Day3_lab_practice
├── my_tools.py
├── my_agent.py
├── my_agent_plain.py
├── analysis.md
└── screenshots

but not:

.env
Step 2 — Create .gitignore

Since you are going to push the project to GitHub, create a file named:

.gitignore

inside the folder that you are going to push.

Put this inside:

# Environment variables and API keys
.env
*.env

# Python
__pycache__/
*.pyc

# Virtual environment
.venv/

# VS Code
.vscode/

Save it.

Important

If you are pushing the whole AI_assigned_task folder, create .gitignore here:

AI_assigned_task
├── .gitignore
├── Day1_lab_practice
├── Day2_lab_practice
├── Day3_lab
└── Day3_lab_practice

If you are pushing only Day3_lab_practice, put .gitignore inside Day3_lab_practice.

Step 3 — Don't copy .env into Day3

Your my_agent.py currently uses:

DAY1_FOLDER = Path(
    r"C:\Users\padma\OneDrive\Desktop\AI_assigned_task\Day1_lab_practice"
)

load_dotenv(DAY1_FOLDER / ".env")

This means your Day3 project can use the existing .env without putting the API key inside Day3_lab_practice.

However, there's one issue before you push it: this absolute Windows path is specific to your computer.

A better GitHub-safe approach is to use an environment variable / local setup instead of publishing your personal Windows path.

But don't change it yet if your immediate goal is just protecting the API key. We can clean that up before the final push.

Step 4 — Very important: If the API key was already pushed

If you have never pushed the API key to GitHub, you're fine. Just add .gitignore before git add.

If the key was already pushed, simply deleting .env is not enough, because Git can retain it in commit history.

In that situation:

Revoke/rotate the API key immediately in the provider dashboard.
Remove the secret from the repository/history.
Create a new key.
Keep the new key only in .env.
Your final GitHub structure should look like
Day3_lab_practice/
│
├── my_tools.py
├── my_agent.py
├── my_agent_plain.py
├── analysis.md
├── .gitignore
│
└── screenshots/
    ├── plain_b3.png
    ├── tool_b3.png
    ├── tool_b4.png
    └── plain_reminder.png

No .env and no API key. 🔒

And one more thing: the analysis.md I created for you does not contain your actual API key. It only discusses the LLM/tool experiment.

If you want, I can now give you the 
exact Git commands to safely push Day3_lab_practice to GitHub without exposing the API key, step by step.

Cloudflare

Deploy serverless functions

Start building for free.

Ad
More options
Ads do not influence the answers you get from ChatGPT. Your chats stay private. 
Learn about ads and personalization

Sponsored options
Ad
Library
/
analysis.md
Analysis: From Prompt to Action --- LLM, Tool, and Agent
1. Scenario

For this task, I created a small college bus schedule assistant. The
assistant has access to one external tool called lookup_bus_schedule.
The tool contains a small private bus schedule for routes B1, B2, B3,
and B4.

The purpose of this scenario is to compare a plain LLM with an LLM that
can use one external tool. The bus schedule is local information stored
in the program, so the LLM should not be expected to know it from its
general knowledge.

The main comparison question was:

What time does College Bus Route B3 leave, and what is its final stop?

The tool contains the following information for B3:

Departure: 8:00 AM
First stop: College Campus
Final stop: Town Bus Stand

A second tool-enabled question was also tested for Route B4.

2. What is an LLM?

A Large Language Model (LLM) is a model trained on large amounts of text
so that it can understand prompts and generate natural-language
responses.

An LLM can answer many general questions from patterns and information
learned during training. It is useful for tasks such as explaining
concepts, writing messages, summarizing information, and generating
text.

However, an LLM does not automatically have access to private data
stored in a user's program. It can also produce an uncertain or
incorrect answer when information is missing, highly specific, or needs
an external calculation or lookup. In my experiment, the plain LLM did
not know the private college bus schedule for Route B3. Instead, it said
that it could not provide the exact schedule and suggested checking an
official transportation source.

This shows that an LLM should not be treated as a reliable database for
information that exists outside its available knowledge.

3. What is an Agent?

An AI agent is a system in which an LLM can decide what action is needed
to complete a task and can use available tools when necessary.

A plain chat interaction normally follows:

User question → LLM → Answer

A tool-using agentic interaction can follow:

User question → LLM decides whether a tool is needed → Tool call →
Tool result → LLM → Final answer

In this task, my_agent.py demonstrates this basic agentic tool-calling
behavior. It is intentionally a minimal implementation. It does not
implement a full ReAct loop or multiple tools because the assignment
requires only one working tool call.

4. What is a Tool and What is a Tool Call?

A tool is an external function that an LLM can request to perform an
operation or obtain information that is outside the LLM's direct
response.

In this project, the tool is:

lookup_bus_schedule(route)

It looks up the route in the local bus schedule and returns the relevant
schedule as text.

A tool call is the request made by the LLM to use that function. For
example, during the B3 test, the output showed:

Tool: lookup_bus_schedule
Arguments: {"route":"B3"}

The program then executed the function and returned:

Route B3: Departure: 8:00 AM; First stop: College Campus; Final stop: Town Bus Stand.
5. Tool Schema

The tool is described to the LLM using a schema. The schema tells the
model:

name --- the name of the function it can call.
description --- what the function does and when it should be
used.
parameters --- the inputs that the function expects.

For this project, the important parameter is:

route

It is a string such as B1, B2, B3, or B4.

The schema is needed because the LLM needs a clear description of the
available action and the correct format for its arguments. Without this
information, the model would not have a structured way to request the
tool.

6. Step-by-Step Tool Call Flow

The B3 experiment followed these steps:

User question
The user asks: "What time does College Bus Route B3 leave, and what
is its final stop?"
Model decides whether a tool is needed
The LLM has access to the lookup_bus_schedule tool and decides to
use it because the question asks for a specific college bus
schedule.
Tool call is generated
The model requests: lookup_bus_schedule({"route":"B3"})
Tool runs
The Python program executes the lookup_bus_schedule function.
Tool result is returned
The tool returns:
Route B3: Departure: 8:00 AM; First stop: College Campus; Final stop: Town Bus Stand.
Final answer
The result is sent back to the LLM, which produces the final answer:
"College Bus Route B3 departs at 8:00 AM, and its final stop is the
Town Bus Stand."

The B4 test followed the same flow, but the model requested route B4.

7. Why Should a Tool Return Text Even When It Fails?

A tool should return a useful text result even when it cannot complete
the requested operation, instead of immediately raising an error that
stops the whole program.

Returning text keeps the tool result inside the agent workflow. The LLM
can then see what went wrong and potentially explain the problem or
decide what to do next.

For example, if a requested route does not exist, the tool can return:

No schedule found for route B9.

This is easier for the LLM to understand than abruptly terminating the
program.

In a larger agent system, this approach also makes tool failures visible
to the model so that the system can respond gracefully.

8. Plain LLM vs LLM with One Tool

Aspect Plain LLM LLM with one tool

Source of answer The LLM's learned LLM plus information
knowledge and reasoning returned by the
external tool

Can it fetch or compute No, not through this Yes, through the
outside its own memory? script provided tool

Reliability on Can be limited when Can be improved when
factual/numeric information is private, the tool contains the
questions current, or unavailable required information

Transparency The source of a The tool name,
specific answer may not arguments, and tool
be visible result can be displayed

The table describes the behavior of the implementations in this project.
It does not mean that every tool-enabled system is always more accurate
or that every plain LLM answer is incorrect.

9. Observations from the Experiment
Question 1 --- Route B3 without a tool

Question:

What time does College Bus Route B3 leave, and what is its final stop?

The plain LLM did not provide a departure time or final stop. It
responded that it could not pull real-time transit schedules and
suggested checking an official college transportation source.

This was expected because the B3 schedule was private data created
inside the project.

Question 1 --- Route B3 with the tool

The tool-enabled run showed:

TOOL CALL:
Tool: lookup_bus_schedule
Arguments: {"route":"B3"}

TOOL RESULT:
Route B3: Departure: 8:00 AM; First stop: College Campus; Final stop: Town Bus Stand.

The final answer was:

College Bus Route B3 departs at 8:00 AM, and its final stop is the
Town Bus Stand.

This demonstrates that the tool supplied information that the plain LLM
did not have.

Question 2 --- Route B4 with the tool

Question:

What is the departure time and final stop of College Bus Route B4?

The tool-enabled run showed:

TOOL CALL:
Tool: lookup_bus_schedule
Arguments: {"route":"B4"}

TOOL RESULT:
Route B4: Departure: 8:15 AM; First stop: College Campus; Final stop: Market Road.

The final answer stated that Route B4 departs at 8:15 AM and its final
stop is Market Road.

This demonstrates that the same single tool can be used with a different
parameter to retrieve another route's information.

Question 3 --- Question that does not require the tool

Question:

Write a one-line message reminding college students to arrive at the
bus stop on time.

The plain LLM answered:

Don't miss the ride---be at the bus stop on time, every time!

This question did not require the private bus schedule. The LLM could
generate the requested message directly.

10. What the Experiment Shows

The experiment shows that a plain LLM is useful when the task mainly
requires language generation or general knowledge. For example, the
one-line reminder did not need an external tool.

A tool becomes useful when the answer depends on information that is
stored outside the LLM's own knowledge. In this project, the exact B3
and B4 bus schedules were stored in the Python program. The plain LLM
could not access that information, while the tool-enabled version could
retrieve it.

The experiment also shows the importance of making the tool's purpose
and parameters clear through a schema. The model used the route
parameter to request the correct schedule.

11. Suitability

A plain LLM can be suitable for:

Writing and rewriting text
General explanations
Summaries
Creative language tasks
Questions that do not depend on private or external data

A tool can be necessary when the task requires:

Private application data
A database lookup
A file lookup
A reliable calculation
Current or external information, when an appropriate external source
is connected

The correct choice depends on what information the task requires. Adding
a tool also introduces an extra step and therefore may require more
processing than a direct LLM response.

12. Conclusion

This project demonstrated the difference between a plain LLM and an LLM
that can use one external tool.

The plain LLM could generate a general bus reminder, but it could not
provide the private B3 schedule. When the lookup_bus_schedule tool was
available, the model requested the tool with the route parameter,
received the stored schedule, and used the result to produce the final
answer. The same tool also successfully retrieved the B4 schedule.

Therefore, the main lesson from this experiment is that an LLM provides
language understanding and generation, while tools allow an agentic
system to access information or perform actions outside the LLM's direct
knowledge.