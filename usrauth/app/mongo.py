from pymongo import MongoClient
from usrauth.app.config import DATA_BASE_NAME

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017')
# db = client.usrauth
db = client[DATA_BASE_NAME]
# print(db)