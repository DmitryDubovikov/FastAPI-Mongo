from motor.motor_asyncio import AsyncIOMotorClient

mongo_client = AsyncIOMotorClient("mongodb://root:example@mongo:27017/")
db = mongo_client["form_templates"]

db.form_templates.drop()

# Пример шаблона формы
form_template = {
    "name": "user_email + user_phone",
    "user_email": "email",
    "user_phone": "phone",
}

form_template2 = {"name": "user_name only", "user_name": "text"}
form_template3 = {"name": "date only", "important_date": "date"}

# Добавление шаблона формы в базу данных
db.form_templates.insert_one(form_template)
db.form_templates.insert_one(form_template2)
db.form_templates.insert_one(form_template3)
