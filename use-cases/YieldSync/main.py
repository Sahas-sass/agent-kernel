import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic._internal._generate_schema")

from agentkernel.api import RESTAPI
from agentkernel.openai import OpenAIModule
from agents import Agent 

from tools import (
    get_market_price, 
    record_crop_planting, 
    check_farm_history,
    get_weather_forecast,
    diagnose_crop_disease
)

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

# 1. This prevents Linux from deleting your routes!
active_module = OpenAIModule([agronomy_agent])
RESTAPI.add(active_module)

# 2. Add Health Check
from fastapi import APIRouter
health_router = APIRouter()

@health_router.get("/")
def health_check():
    return {"status": "YieldSync Backend is LIVE"}

RESTAPI.add(router=health_router)

# 3. Boot the server
if __name__ == "__main__":
    RESTAPI.run()