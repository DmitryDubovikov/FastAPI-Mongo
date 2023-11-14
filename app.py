from urllib.parse import parse_qs

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient

from utils import validate_form_value, typehint_dict

app = FastAPI()
mongo_client = AsyncIOMotorClient("mongodb://root:example@mongo:27017/")
db = mongo_client["form_templates"]


async def find_matching_template(form_data):
    async for template in db.form_templates.find():
        match = True

        for template_field_name, template_field_type in template.items():
            if template_field_name in ("name", "_id"):
                continue
            found_form_value = form_data.get(template_field_name)
            if not found_form_value or not validate_form_value(
                template_field_type, found_form_value
            ):
                match = False
                break
        if match:
            return template["name"]
    return None


@app.post("/form")
async def get_form_data(request: Request):
    body = await request.body()
    data_dict_lists = parse_qs(body.decode("utf-8"))
    data_dict = {key: value[0] for key, value in data_dict_lists.items()}
    template_name = await find_matching_template(data_dict)

    if template_name:
        return JSONResponse(content={"template_name": template_name})
    else:
        return JSONResponse(content=typehint_dict(data_dict))


@app.get("/")
async def root():
    return {"message": "Hello world"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)
