import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic._internal._generate_schema")

from agentkernel.api import RESTAPI
from agentkernel.openai import OpenAIModule
from agents import Agent 
from tools import get_market_price, record_crop_planting, check_farm_history, get_weather_forecast, diagnose_crop_disease

# 1. Setup Agent
agronomy_agent = Agent(
    name="agronomy_advisor",
    model="llama-3.3-70b-versatile",
    instructions="You are an expert Agricultural Consultant. Reply in the language the user speaks.",
    tools=[get_market_price, record_crop_planting, check_farm_history, get_weather_forecast, diagnose_crop_disease]
)

# 2. Register the module
# The RESTAPI automatically detects any initialized modules.
module = OpenAIModule([agronomy_agent])

# 3. Boot using the native RESTAPI runner
if __name__ == "__main__":
    RESTAPI.run()