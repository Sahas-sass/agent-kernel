import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic._internal._generate_schema")

from fastapi.middleware.cors import CORSMiddleware
from agentkernel.api import RESTAPI
from agentkernel.openai import OpenAIModule
from agents import Agent 
from tools import get_market_price, record_crop_planting, check_farm_history, get_weather_forecast, diagnose_crop_disease
import uvicorn

# 1. Setup Agent
agronomy_agent = Agent(
    name="agronomy_advisor",
    model="llama-3.3-70b-versatile",
    instructions="You are an expert Agricultural Consultant. Reply in the language the user speaks.",
    tools=[get_market_price, record_crop_planting, check_farm_history, get_weather_forecast, diagnose_crop_disease]
)
module = OpenAIModule([agronomy_agent])

# 2. USE THE NATIVE API 
# This automatically handles the complex JSON-to-Object parsing that was failing.
ak_api = RESTAPI(module)

# 3. FIX CORS ON THE NATIVE APP
# We extract the underlying FastAPI instance to apply your CORS rules.
app = getattr(ak_api, 'app', ak_api) 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Boot using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)