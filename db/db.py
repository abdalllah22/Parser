from pymongo import MongoClient


def save_to_mongo_db(format,data):
    
    try:
        conn = MongoClient()
        print("Connected successfully!!!")
    except:  
        print("Could not connect to MongoDB")


    # database
    db = conn.truflu
    
    # Created names
    collection = db.format
    collection.insert_one(data)