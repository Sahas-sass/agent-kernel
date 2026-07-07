import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic._internal._generate_schema")

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
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
module = OpenAIModule([agronomy_agent])

# 2. CREATE A SEPARATE FASTAPI APP (This handles CORS and Routing reliably)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

import inspect

@app.post("/api/v1/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    
    # Extract data from the incoming JSON
    prompt_text = data.get("prompt")
    session_id = data.get("session_id")
    agent_instance = module.get_agent(data.get("agent"))
    
    # INSPECT the method signature to find out what it actually wants
    sig = inspect.signature(module.runner.run)
    params = list(sig.parameters.keys())
    
    # Log the exact parameter names it expects
    print(f"DEBUG - Runner expects these parameters: {params}")
    
    try:
        # Create a dictionary using the exact parameter names the framework demands
        # We assume the first parameter is the agent and the second/third are inputs
        kwargs = {
            params[0]: agent_instance,
            params[1]: prompt_text,
            params[2]: session_id
        }
        
        response = await module.runner.run(**kwargs)
        return {"result": response}
    except Exception as e:
        return {"error": f"Framework expects {params}. Details: {str(e)}"}


@app.get("/")
def health():
    return {"status": "LIVE"}

# 3. Boot using Uvicorn (The standard way to run FastAPI)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)