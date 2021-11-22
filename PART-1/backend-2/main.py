import requests
import json
import os
import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class GlobalContext:
    pass


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

GlobalContext.db_conn = psycopg2.connect(
    host=os.environ['DBHOST'],
    database=os.environ['DBNAME'],
    user=os.environ['DBUSER'],
    password=os.environ['DBPASS']
)


@app.get("/users")
async def get_users():
    cur = GlobalContext.db_conn.cursor()
    cur.execute(f"SELECT * FROM Users limit {os.environ['N_RESULTS']}")
    data = cur.fetchall()
    res = {'results': []}
    for d in data:
        res['results'].append({
            'login': {
                'username': d[2],
                'uuid': d[1]
            },
            'name': {
                'first': '',
                'last': d[3]
            },
            'picture': {
                'thumbnail': d[4]
            }
        })
    return res