import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner,set_tracing_disabled, OpenAIChatCompletionsModel, function_tool
import rich
load_dotenv()  # Yeh .env file ko load karega
set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# -------------------------------------
@function_tool      # ap ka function hamesha string written karta hai
def weather_karachi(city : str ): #yah function ka signature hai 
        #  is ka name llm parta hai  
        #  yah body hai function ki 
        """
        Get the current weather in Karachi.
        """
        # yah dono ko function schema mai convert karta hai means signature of doc string (3 quotes)
        return f"The weather of {city} is -0C."
# ---------------------------------------------------------------------
client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)
agent = Agent(
    name="my_agent",
    model=OpenAIChatCompletionsModel(model="mistralai/mistral-small-24b-instruct-2501",openai_client=client),
    instructions="Always use weather_karachi tool when user ask for weather of Karachi ,You are a helpful assistant.",
    tools = [weather_karachi]
)
# -------------------------------------------------------------
res = Runner.run_sync(agent, "What is the weather of Karachi?")
# rich.print(res._last_agent.tools[0].name)
rich.print(res.final_output)





