from pymongo.mongo_client import MongoClient


##username = "yadavbipin79817_db_user"

uri="mongodb+srv://yadavbipin79817_db_user:Bipin79817@cluster0.nlfmlcc.mongodb.net/"

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Connected successfully")

except Exception as e:
    print("Connection failed:", e)