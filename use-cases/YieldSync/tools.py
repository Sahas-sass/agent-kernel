from agents import function_tool

@function_tool
def get_market_price(crop: str) -> str:
    """Fetches the current market price for a specified crop."""
    
    # Standardize the input
    crop_name = crop.lower().strip()
    
    # Mock database for testing
    prices = {
        "rice": "220.00",
        "tomato": "150.00",
        "corn": "90.00"
    }
    
    price = prices.get(crop_name)
    
    if price:
        # Return a highly explicit string so the AI cannot misunderstand it
        return f"The current market price for 1kg of {crop_name} is {price} LKR."
    else:
        return f"Sorry, I do not have current pricing data for {crop_name}."

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

@function_tool
def diagnose_crop_disease(crop_name: str, symptoms: str) -> str:
    """
    Searches the agricultural database to identify plant diseases based on symptoms and suggests treatments.
    """
    crop = crop_name.lower().strip()
    symptoms = symptoms.lower()
    
    # Mock pest & disease database
    database = {
        "tomato": {
            "yellow spots": "Diagnosis: Early Blight (Fungal). Treatment: Apply a copper-based fungicide, remove affected leaves, and avoid overhead watering.",
            "holes in leaves": "Diagnosis: Tomato Hornworm. Treatment: Hand-pick worms, apply Bacillus thuringiensis (Bt) spray."
        },
        "rice": {
            "brown lesions": "Diagnosis: Rice Blast. Treatment: Maintain proper flood levels, avoid excessive nitrogen fertilizer, apply Tricyclazole if severe."
        }
    }
    
    if crop in database:
        for key, diagnosis in database[crop].items():
            if key in symptoms:
                return diagnosis
                
    return f"I could not find an exact match for those symptoms on {crop_name} in my database. Recommend taking a photo to your local extension officer."

    