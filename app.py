from dotenv import load_dotenv
from agents import Agent, Runner
import rich
load_dotenv()
# ------------------------------------------------
doctor_agent = Agent(
    model="gpt-4.1-nano",
    name="english_agent",
    instructions="You are an expert physician ready to answer medical queries.",)
# ---------------------------------------------------------------
shopping_agent = Agent(
    name="Shopping Assistant",
    instructions="You assist users in finding products and making purchase decisions."
)
support_agent = Agent(
    name="Support Agent",
    instructions="You help users with post-purchase support and returns."
)
# Convert agents to tools
doctor_tool = doctor_agent.as_tool(tool_name="doctor_agent", tool_description="You are an expert physician")
shopping_tool = shopping_agent.as_tool(tool_name="shopping_agent", tool_description="You assist users in shopping")
support_tool = support_agent.as_tool(tool_name="support_agent", tool_description="You provide post-purchase support")
# ---------------------
agent = Agent(
    model="gpt-4.1-nano",
    name="my_agent",
    instructions="You route user queries to the appropriate agents",
    tools=[doctor_tool, shopping_tool, support_tool]
)
# ----------------------------------------
# res1 = Runner.run_sync(agent, "What are the symptoms of diabetes?")
# rich.print(res1.final_output)
res2 = Runner.run_sync(agent, "I need help with a recent purchase.")
rich.print(res2.final_output)
rich.print(res2)
