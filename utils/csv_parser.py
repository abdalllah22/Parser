import pandas as pd
from database.db import save_to_mongo_db
from utils.helper import save_json_file_from_csv 

def CSVParser(filename1, filename2):
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
                vehicle_object = {
                    "id": vehicle_row['id'],
                    "make": vehicle_row['make'],
                    "vin_number": vehicle_row['vin_number'],
                    "model_year": vehicle_row['model_year'],
                }
                vehicles.append(vehicle_object)
                data['transaction'][index1]['vehicles'] = vehicles
            
    
    # Save to json file
    save_json_file_from_csv(filename1, filename2, data)
    
    # Save to local mongo database
    save_to_mongo_db('csv', data)
    
    return data