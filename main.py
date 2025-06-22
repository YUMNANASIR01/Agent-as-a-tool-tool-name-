# --------------------------  Agent as a tool -------------------------
from dotenv import load_dotenv
from agents import Agent, Runner
import rich
load_dotenv()  # Yeh .env file ko load karega

# ---------------------------------------------------------------------
english_agent = Agent(
    model="gpt-4.1-nano" ,
    name= "english_agent",
    instructions= "You are an expert physician ready to answer medical queries.",
)
# -------------- agent as tool ----
# ----------- ek agent apny function sy bat kar raha hai 
# -------------- ek agent main agent ko hum ny route karenge agent ky sath 
# ------------main agent main english agent pass kiya
agent= Agent(
    model="gpt-4.1-nano" ,
    name= "my_agent",
    instructions= "You route user queries to the appropriate agents",
    tools=[
        english_agent.as_tool(tool_name="doctor_agent", tool_description="You are an expert physician")
    ]
)
# -------------------------------------------------------------
res = Runner.run_sync(agent, "What are the symptoms of diabetes?")
# rich.print(res.final_output)
rich.print(res)
    
# ------------------------------ end --------------------------------------










# from dotenv import load_dotenv
# from agents import Agent, Runner
# import rich
# load_dotenv()
# # ------------------------------------------------
# doctor_agent = Agent(
#     model="gpt-4.1-nano",
#     name="english_agent",
#     instructions="You are an expert physician ready to answer medical queries.",)
# # ---------------------------------------------------------------
# shopping_agent = Agent(
#     name="Shopping Assistant",
#     instructions="You assist users in finding products and making purchase decisions."
# )
# support_agent = Agent(
#     name="Support Agent",
#     instructions="You help users with post-purchase support and returns."
# )
# # Convert agents to tools
# doctor_tool = doctor_agent.as_tool(tool_name="doctor_agent", tool_description="You are an expert physician")
# shopping_tool = shopping_agent.as_tool(tool_name="shopping_agent", tool_description="You assist users in shopping")
# support_tool = support_agent.as_tool(tool_name="support_agent", tool_description="You provide post-purchase support")
# # ---------------------
# agent = Agent(
#     model="gpt-4.1-nano",
#     name="my_agent",
#     instructions="You route user queries to the appropriate agents",
#     tools=[doctor_tool, shopping_tool, support_tool]
# )
# # ----------------------------------------
# # res1 = Runner.run_sync(agent, "What are the symptoms of diabetes?")
# # rich.print(res1.final_output)
# res2 = Runner.run_sync(agent, "I need help with a recent purchase.")
# rich.print(res2.final_output)
# rich.print(res2)










# # -----------------------  function tool name sy khud chila gya function ky------------
# from dotenv import load_dotenv
# from agents import Agent, Runner,function_tool
# import rich
# load_dotenv()  # Yeh .env file ko load kareg

# # ---------------------------------------------------------------------
# @function_tool
# def weather_karachi():
#     """This function returns the weather in Karachi"""
#     print("The weather in Karachi is 0 degrees.")
# # ---------------------------

# @function_tool
# def prime_minister_of_Pakistan():
#     print("prime minister of Pakistan is Imran Khan.")

# agent= Agent(
#     model="gpt-4.1-mini" ,
#     name= "my_agent",
#     instructions= "you are a helpful assistant",
#     tools=[
#         weather_karachi,
#         prime_minister_of_Pakistan
#     ]
# )
# # -------------------------------------------------------------

# res = Runner.run_sync(agent, "What is the weather in karachi ")
# rich.print(res)

# ------------------------------------ end -----------------------------------------------

  











