from pymongo import MongoClient

MONGO_URI = "mongodb://root:example@mongo:27017/"
DB_NAME = "form_templates"
COLLECTION_NAME = "form_templates"

form_template = {
    "name": "user_email + user_phone",
    "user_email": "email",
    "user_phone": "phone",
}
form_template2 = {"name": "user_name only", "user_name": "text"}
form_template3 = {"name": "date only", "important_date": "date"}

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]

if COLLECTION_NAME in db.list_collection_names():
    db[COLLECTION_NAME].drop()

db[COLLECTION_NAME].insert_one(form_template)
db[COLLECTION_NAME].insert_one(form_template2)
db[COLLECTION_NAME].insert_one(form_template3)
