import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic._internal._generate_schema")

from agentkernel.api import RESTAPI
from agentkernel.openai import OpenAIModule
from agents import Agent 

from tools import get_market_price

# 1. Configure the Agronomy Advisor Agent
agronomy_agent = Agent(
    name="agronomy_advisor",
    model="llama3-8b-8192",
    instructions=(
        "You are an expert Agricultural Consultant for the YieldSync project. "
        "Your goal is to help rural farmers optimize crop yields and sell their harvest at the best possible prices. "
        "You speak plainly and clearly to farmers, avoiding overly complex scientific jargon. "
        "Always use the get_market_price tool to check real wholesale data before advising a farmer on where or when to sell. "
        "IMPORTANT GUARDRAIL: If a farmer reports a severe biological hazard or asks for human medical advice, "
        "you must decline to answer and immediately refer them to a local medical professional or government extension officer."
    ),
    tools=[get_market_price]
)

# 2. Register the agent with Agent Kernel's OpenAI integration
OpenAIModule([agronomy_agent])

# 3. Boot up the framework's internal API server
if __name__ == "__main__":
    RESTAPI.run()