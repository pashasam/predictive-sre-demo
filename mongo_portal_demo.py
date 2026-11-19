import os
from pymongo import MongoClient

URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/demo")

def check_mongo(db_name, collection):
    print("JIT check: MongoDB access allowed for 30 min")
    client = MongoClient(URI, serverSelectionTimeoutMS=5000)
    try:
        db = client[db_name]
        docs = list(db[collection].find().limit(10))  # e.g. slow ops
        print(f"MongoDB: got {len(docs)} docs")
        return docs
    except Exception as e:
        print(f"MongoDB error: {e}")
        return []
    finally:
        client.close()
        print("MongoDB connection closed")
