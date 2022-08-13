from pymongo import MongoClient
import pymongo
import dotenv
import os

dotenv.load_dotenv()
dburl= os.getenv("URL")

if not dburl:
    raise ValueError("No URL for database")

client = pymongo.MongoClient(dburl)
db = client["Ironhack"]
collection = db.get_collection("friends")
collection.find_one()