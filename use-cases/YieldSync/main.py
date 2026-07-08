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
    
    # 1. Grab the raw text from the frontend
    user_text = data.get("prompt")
    
    # 2. THE SHOTGUN PAYLOAD
    # We give the framework every conceivable key it might be looking for.
    # It will simply grab the one it wants and ignore the rest!
    universal_message = {
        "text": user_text,
        "content": user_text,
        "message": user_text,
        "prompt": user_text,
        "query": user_text,
        "input": user_text,
        "role": "user",
        "type": "text"
    }
    
    # 3. Package it into the requests array exactly as the runner expects
    execution_params = {
        "agent": module.get_agent(data.get("agent", "agronomy_advisor")),
        "session": data.get("session_id", "default_session"),
        "requests": [universal_message]
    }
    
    try:
        response = await module.runner.run(**execution_params)
        return {"result": response}
    except Exception as e:
        print(f"CRITICAL ERROR: {str(e)}")
        return {"error": str(e)}


@app.get("/")
def health():
    return {"status": "LIVE"}

# 3. Boot using Uvicorn (The standard way to run FastAPI)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)