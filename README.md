# FastAPI-Mongo

Web application for recognizing forms.


## Technologies used:
* __FastAPI:__
* __MongoDB:__
* __Docker:__

### To run:

```sh
docker compose build
docker compose up
```

### To initialize Mongo data: 
Connect to fastapi container:
```sh
docker exec -it fastapi-app /bin/sh
```
Run script:
```sh
python init_db.py
```

### Docs:

http://localhost:8000/docs

### To try:

Run in a separate terminal (you will need requests lib installed):
```sh
python sample_requests.py 
```

Expected responses:
```sh
Response 1: {"template_name":"user_name only"}
Response 2: {"template_name":"user_email + user_phone"}
Response 3: {"template_name":"date only"}
Response 4: {"user_email":"email","user_phone":"text"}
```