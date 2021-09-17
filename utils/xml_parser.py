import xml.etree.ElementTree as ET
import json
from datetime import datetime
import os
from database.db import save_to_mongo_db

def XMLParser(filename):
    print(filename)
    tree = ET.parse(filename)
    root = tree.getroot()
    
    data = {}
    data['file_name'] = filename
    data['transaction'] = []
    
    for elm in root.findall("Transaction"):
        date = elm.find('Date').text
        customer_id = elm.find('Customer').get('id')
        name = elm.find('Customer/Name').text
        address = elm.find('Customer/Address').text
        phone = elm.find('Customer/Phone').text
        data['transaction'].append({
            "date": date,
            "customer": {
                "customer_id": customer_id,
                "name" : name,
                "phone": phone,
                "address": address,
            }
        })
    
    vehicles = []
    for elm in root.findall("Transaction/Customer/Units/Auto/Vehicle"):
        vehicle_object = {
                "id": elm.get('id'),
                "make": elm.find('Make').text,
                "vin_number": elm.find('VinNumber').text,
                "model_year": elm.find('ModelYear').text
        }
        vehicles.append(vehicle_object)
    data['transaction'][0]['vehicles'] = vehicles
        
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    
    filename_format = filename.split('.')
    
    
    with open(f"../../output/xml/{timestamp}_{filename_format[0]}.json", 'w',encoding ='utf8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)
    
    # Save to local mongo database
    save_to_mongo_db('xml', data)
