from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get Mongo URI from environment, fallback to localhost
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Initialize client and DB at the module level
client = MongoClient(MONGO_URI)
db = client.get_database()  # Automatically picks database from URI if present

print(f"✅ Connected to MongoDB at: {MONGO_URI}")
