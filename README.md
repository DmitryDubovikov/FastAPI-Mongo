# FastAPI-Mongo

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

### To try:

http://localhost:8000/docs

or