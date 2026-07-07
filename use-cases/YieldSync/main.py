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

@app.post("/api/v1/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    
    # We use 'text' as the parameter name instead of 'prompt'
    text_input = data.get("prompt") 
    session_id = data.get("session_id")
    agent_instance = module.get_agent(data.get("agent"))
    
    try:
        # Most runners expect the input text in the 'text' argument
        response = await module.runner.run(
            agent=agent_instance, 
            text=text_input, 
            session_id=session_id
        )
        return {"result": response}
    except Exception as e:
        # This will show us the EXACT arguments the method wants
        print(f"DEBUG - Full Error: {str(e)}")
        return {"error": str(e)}

@app.get("/")
def health():
    return {"status": "LIVE"}

# 3. Boot using Uvicorn (The standard way to run FastAPI)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)