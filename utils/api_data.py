import requests

def get_api_data(vin_no, model):
    
    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvaluesextended/{vin_no}?format=json&modelyear={model}'
    API_data = requests.get(url).json()
    vehicle_enriched = {
                "Model": API_data["Results"][0]["Model"],
                "Manufacturer": API_data["Results"][0]["Manufacturer"],
                "PlantCountry": API_data["Results"][0]["PlantCountry"],
                "VehicleType": API_data["Results"][0]["VehicleType"]
    }
    return vehicle_enriched