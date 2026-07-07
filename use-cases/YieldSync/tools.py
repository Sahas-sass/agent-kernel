from agents import function_tool

@function_tool
def get_market_price(crop_name: str, region: str) -> str:
    """
    Fetches the current wholesale market price for a given crop in a specific region.
    """
    # A simulated database for the competition
    mock_database = {
        "rice": "Rs. 120 per kg",
        "corn": "Rs. 85 per kg",
        "tomato": "Rs. 150 per kg",
        "pumpkin": "Rs. 60 per kg",
        "chili": "Rs. 400 per kg"
    }
    
    crop = crop_name.lower().strip()
    if crop in mock_database:
        return f"The current wholesale market price for {crop_name} in {region} is {mock_database[crop]}."
    else:
        return f"I'm sorry, but real-time price data for {crop_name} is currently unavailable in the {region} region."


farm_database = {}

@function_tool
def record_crop_planting(farmer_id: str, crop_name: str, acres: float) -> str:
    """
    Saves a record of what a farmer planted to the database so the agent can track their farm over time.
    """
    farm_database[farmer_id] = {
        "crop": crop_name,
        "acres": acres,
        "status": "Growing - Week 1"
    }
    return f"Success. Recorded that {farmer_id} planted {acres} acres of {crop_name}. The system will now track this farm's progress."

@function_tool
def check_farm_history(farmer_id: str) -> str:
    """
    Checks the database to see what crop the farmer is currently growing.
    """
    if farmer_id in farm_database:
        data = farm_database[farmer_id]
        return f"Database Record: {farmer_id} is currently growing {data['acres']} acres of {data['crop']}. Status: {data['status']}."
    return f"No planting records found in the database for {farmer_id}."


@function_tool
def get_weather_forecast(location: str) -> str:
    """
    Checks the 5-day weather forecast for a specific farming location.
    Use this to advise farmers on the best days to plant, harvest, or apply fertilizer.
    """
    # Mocking a forecast for the hackathon
    return f"Weather Alert for {location}: Heavy afternoon thunderstorms expected for the next 48 hours. Days 3-5 will be mostly sunny and dry."

