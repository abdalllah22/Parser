import pandas as pd
from database.db import save_to_mongo_db 
from utils.api_data import get_api_data
from typing import Dict
from .parser import Parser

class CSVParser(Parser):
    def __init__(self):
        Parser.__init__(self)

    def get_data(self,filename1, filename2) -> Dict:
        # Get csv file to parse
        customer_df = pd.read_csv(filename1)
        vehicle_df = pd.read_csv(filename2)

        # data stored in json file
        data = {}
        data['file_name'] = f'{filename1}_{filename2}'
        data['transaction'] = []
        
        # get customers data
        for index1, custoner_row in customer_df.iterrows():
            data['transaction'].append({
                    "date": custoner_row['date'],
                    "customer": {
                        "id": custoner_row['id'],
                        "name" : custoner_row['name'],
                        "address": custoner_row['address'],
                        "phone": custoner_row['phone'],
                        
                    }
                })
        
            # get vehicles data
            vehicles = []
            for index2, vehicle_row in vehicle_df.iterrows():
                if vehicle_row['owner_id'] == custoner_row['id']:
                    vehicle_enriched = get_api_data(vehicle_row['vin_number'], vehicle_row['model_year'])
                    vehicle_object = {
                        "id": vehicle_row['id'],
                        "make": vehicle_row['make'],
                        "vin_number": vehicle_row['vin_number'],
                        "model_year": vehicle_row['model_year'],
                        **vehicle_enriched
                    }
                    vehicles.append(vehicle_object)
                    data['transaction'][index1]['vehicles'] = vehicles
                
        # Save to local mongo database
        save_to_mongo_db('csv', data)
        
        return data