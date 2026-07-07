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