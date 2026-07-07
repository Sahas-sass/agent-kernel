import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic._internal._generate_schema")

from agentkernel.api import RESTAPI
from agentkernel.openai import OpenAIModule
from agents import Agent 

# IMPORT ALL YOUR TOOLS HERE
from tools import (
    get_market_price, 
    record_crop_planting, 
    check_farm_history,
    get_weather_forecast,
    diagnose_crop_disease
)

# Configure the Agronomy Advisor Agent
agronomy_agent = Agent(
    name="agronomy_advisor",
    model="llama-3.3-70b-versatile",
    instructions=(
        "You are an expert Agricultural Consultant for the YieldSync project. "
        "Your goal is to help rural Sri Lankan farmers optimize crop yields. "
        "MULTI-LANGUAGE SUPPORT: You are fluent in English, Sinhala, and Tamil. ALWAYS reply in the exact language the farmer uses. "
        "Always use your tools to provide data-backed answers. "
        "If they ask about weather, use get_weather_forecast. "
        "If they describe sick plants, use diagnose_crop_disease to help them. "
        "IMPORTANT GUARDRAIL: If a farmer reports a severe biological hazard or asks for human medical advice, "
        "you must decline to answer and refer them to a medical professional."
    ),
    tools=[
        get_market_price, 
        record_crop_planting, 
        check_farm_history, 
        get_weather_forecast, 
        diagnose_crop_disease
    ]
)

# 2. Register the agent with Agent Kernel's OpenAI integration
OpenAIModule([agronomy_agent])

# 3. Boot up the framework's internal API server
if __name__ == "__main__":
    RESTAPI.run()