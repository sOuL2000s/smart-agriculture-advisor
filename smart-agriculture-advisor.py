import pandas as pd
import random

# Sample data for soil types and crops
crop_data = {
    "SoilType": ["Sandy", "Clay", "Loamy", "Silty", "Peaty"],
    "Winter": ["Wheat", "Barley", "Peas", "Lettuce", "Broccoli"],
    "Summer": ["Corn", "Tomato", "Carrot", "Cucumber", "Strawberry"]
}

# Convert to DataFrame
df = pd.DataFrame(crop_data)

# Function to recommend a crop
def recommend_crop(season, soil_type, temperature):
    # Filter by soil type and season
    crop_options = df[df["SoilType"] == soil_type][season].values
    if not crop_options:
        return "No recommendations available for this soil type."
    
    # Simulate temperature-based suggestion
    if temperature > 30:
        recommended_crop = random.choice([crop_options[0], "Heat-resistant variety"])
    else:
        recommended_crop = crop_options[0]
    
    return recommended_crop

# User input
soil_type = "Loamy"  # Example soil type
season = "Summer"    # Example season
temperature = 28     # Example temperature in Celsius

# Generate recommendation
crop = recommend_crop(season, soil_type, temperature)
print(f"Recommended crop for {soil_type} soil in {season} with temperature {temperature}°C: {crop}")
