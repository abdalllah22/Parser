import os
from glob import glob
import re
import json
from datetime import datetime


def get_format_of_file(formats):
    try:
        file_format = formats
    except Exception as e:
        print(e)
    else:
        return file_format

def get_first_file_name(name):
    try:
        first_file = name
    except Exception as e:
        print(e)
    else:
        return first_file

def get_second_file_name(name):
    try:
        second_file = name
    except Exception as e:
        print(e)
    else:
        return second_file        

def select_all_xml_files():
    os.chdir("input_data/xml")
    files = glob("*")
    return files

def select_all_CSV_files():
    os.chdir("input_data/csv")
    files = glob("*")
    return files

def match_csv_files(filename1, filename2):
    customer_pattern = "customer"
    vehicle_pattern = "vehicle"   
    customer_match = re.search(customer_pattern, filename1)
    vehicle_match = re.search(vehicle_pattern, filename2)
    if customer_match and vehicle_match:
        pass
    else:
        return "Switch Files !!"

def save_json_file_from_xml(filename, data, enriched=''):
    
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    filename_format = filename.split('.')
    
    
    with open(f"../../output/xml/{timestamp}_{filename_format[0]}{enriched}.json", 'w',encoding ='utf8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)

