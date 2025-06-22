# file search tool 
from dotenv import load_dotenv
from agents import Agent, Runner,set_tracing_disabled,FileSearchTool
import rich
load_dotenv()  # Yeh .env file ko load karega
set_tracing_disabled(disabled=True)
# ---------------------------------------------------------------------
agent = Agent(
    model="gpt-4.1-mini" ,
    name= "my agent",
    instructions= "You are a helpful assistant.",
    tools = [FileSearchTool(
        max_num_results=3,
        vector_store_ids=["vs_685714759f648191867d6b6fc9474e43"]
    )]
)
# -------------------------------------------------------------
res = Runner.run_sync(agent, "Who is yumna")
rich.print(res.final_output)
# ------------------------------ end --------------------------------------
