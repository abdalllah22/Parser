from pymongo import MongoClient


def save_to_mongo_db(format,data):
    
    try:
        conn = MongoClient()
        print("Connected to MongoDB successfully!!!")
    except:  
        print("Could not connect to MongoDB")


    # database
    db = conn.truflu
    
    # Created names
    if format == 'csv':
        collection = db.csv
    elif format == 'xml':
        collection = db.xml
    else:
        print('Wrong Format !!')
    
    collection.insert_one(data)