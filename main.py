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

  











