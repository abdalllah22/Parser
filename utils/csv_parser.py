import pandas as pd
import json
from datetime import datetime
import os

def CSVParser(filename1, filename2):
    customer_df = pd.read_csv(filename1)
    vehicle_df = pd.read_csv(filename2)

    data = {}
    data['file_name'] = f'{filename1}_{filename2}'
    data['transaction'] = []
    
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
    
        vehicles = []
        for index2, vehicle_row in vehicle_df.iterrows():
            if vehicle_row['owner_id'] == custoner_row['id']:
                vehicle_object = {
                    "id": vehicle_row['id'],
                    "make": vehicle_row['make'],
                    "vin_number": vehicle_row['vin_number'],
                    "model_year": vehicle_row['model_year'],
                }
                vehicles.append(vehicle_object)
                data['transaction'][index1]['vehicles'] = vehicles
            
    
    
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    with open(f"../../output/csv/{timestamp}_{filename1}_{filename2}.json", 'w',encoding ='utf8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)