from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['magic_info']


try:
    client.admin.command('ping')
    print("Connected successfully!")
except pymongo.errors.ConnectionFailure:
    print("Connection failed.")