import xml.etree.ElementTree as ET
from utils.api_data import get_api_data
from database.db import save_to_mongo_db
from typing import Dict
from .parser import Parser

class XMLParser(Parser): 

    def __init__(self):
        Parser.__init__(self)
    
    def get_data(self,filename) -> Dict:
        # Get xml file to parse
        tree = ET.parse(filename)
        root = tree.getroot()

        # data stored in json file
        data = {}
        data['file_name'] = filename
        data['transaction'] = []
        
        # get customers data
        for elm in root.findall("Transaction"):
            date = elm.find('Date').text
            customer_id = elm.find('Customer').get('id')
            name = elm.find('Customer/Name').text
            address = elm.find('Customer/Address').text
            phone = elm.find('Customer/Phone').text
            data['transaction'].append({
                "date": date,
                "customer": {
                    "id": customer_id,
                    "name" : name,
                    "phone": phone,
                    "address": address,
                }
            })
        
        # get vehicles data
        vehicles = []
        for elm in root.findall("Transaction/Customer/Units/Auto/Vehicle"): 
            vehicle_enriched = get_api_data(elm.find('VinNumber').text, elm.find('ModelYear').text)
            vehicle_object = {
                    "id": elm.get('id'),
                    "make": elm.find('Make').text,
                    "vin_number": elm.find('VinNumber').text,
                    "model_year": elm.find('ModelYear').text,
                    **vehicle_enriched
            }
            vehicles.append(vehicle_object)
        data['transaction'][0]['vehicles'] = vehicles
            
        # Save to local mongo database
        save_to_mongo_db('xml', data)

        return data
