import xml.etree.ElementTree as ET
from database.db import save_to_mongo_db
from utils.helper import save_json_file_from_xml


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
                "model_year": elm.find('ModelYear').text,
        }
        vehicles.append(vehicle_object)
    data['transaction'][0]['vehicles'] = vehicles
        
    
    # Save to json file
    save_json_file_from_xml(filename,data)
    
    # Save to local mongo database
    save_to_mongo_db('xml', data)


