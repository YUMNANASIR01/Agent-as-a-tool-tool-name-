import os 
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from openai import AsyncOpenAI
import rich

load_dotenv()
set_tracing_disabled(disabled=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ------------------------------------------
client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
# ------------------ shooping agent ------------------
shooping_agent = Agent(
    name="shopping_Agent",
    instructions="You assist users in finding products and making purchase decisions.",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash-lite",openai_client=client ),
    handoff_description="A shopping agent to help user in post-purchase and queries."
)
# --------------------- support agent ---------------------
support_agent = Agent(
    name="support_Agent",
    instructions="You help users with post-purchase support and returns.",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash-lite",openai_client=client ),
    handoff_description="A support agent to help user in support."
)
# ------------------ triage agent ------------------
triage_agent = Agent(
    name="triage_Agent",
    instructions=(
        "You triage agent, you delegate the task to appropriate agent.\n\n"
        "when user asked for shopping related queries  , you always use given tools.\n\n"
        "you never reply on our own,  always use given tool to reply user "
    ),
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash-lite",openai_client=client ),
    tools=[shooping_agent.as_tool(
        tool_name= "transfer_to_shopping_agent",
        tool_description="A shopping agent to help user in post-purchase and queries, always add this ✅ emoji in your reply, start reply with this  ✅  emoji"
        ),
        support_agent.as_tool(
        tool_name= "transfer_to_support_agent",
        tool_description="A support agent to help users with post-purchase support and return, always add this 😍 emoji in your reply, start reply with this 😍 emoji"
        )
           ],
    )
# ------------------ run triage agent ------------------
res = Runner.run_sync(starting_agent=triage_agent, input="Help me to buy a good watch and I want to return my bag", max_turns=4)
rich.print(res.last_agent.name)
# ------------------------------------------
rich.print(res.final_output)

