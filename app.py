#  web search tool
from dotenv import load_dotenv
from agents import Agent, Runner,set_tracing_disabled,WebSearchTool
import rich
load_dotenv()  # Yeh .env file ko load karega
set_tracing_disabled(disabled=True)
# ---------------------------------------------------------------------
agent = Agent(
    model="gpt-4.1-mini" ,
    name= "my_agent",
    instructions= "You are a helpful assistant.",
    tools = [WebSearchTool()]
)
# -------------------------------------------------------------
res = Runner.run_sync(agent, "Who is the PM of Pakistan?")
rich.print(res.final_output)
# ------------------------------ end --------------------------------------




