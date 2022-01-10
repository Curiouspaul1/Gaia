import pymongo
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()


client = pymongo.MongoClient(os.getenv('DATABASE_URI'))
cors = CORS()
db = client.test
