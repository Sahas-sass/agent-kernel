import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic._internal._generate_schema")

from fastapi import FastAPI, Request
from agentkernel.api import RESTAPI
from agentkernel.openai import OpenAIModule
from agents import Agent 
from tools import get_market_price, record_crop_planting, check_farm_history, get_weather_forecast, diagnose_crop_disease

# 1. Configure the Agent
agronomy_agent = Agent(
    name="agronomy_advisor",
    model="llama-3.3-70b-versatile",
    instructions="You are an expert Agricultural Consultant. Reply in the language the user speaks.",
    tools=[get_market_price, record_crop_planting, check_farm_history, get_weather_forecast, diagnose_crop_disease]
)

# 2. Register with the framework
module = OpenAIModule([agronomy_agent])

# 3. FORCE THE ROUTE EXPOSURE
# We manually tap into the RESTAPI's internal FastAPI app to ensure the route exists
app = RESTAPI.app

@app.post("/api/v1/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    # Manually pass the request through the module's processing logic
    return await module.process(data)

@app.get("/")
def health():
    return {"status": "LIVE"}

if __name__ == "__main__":
    RESTAPI.run()