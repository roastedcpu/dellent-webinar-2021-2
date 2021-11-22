import requests
import json
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/users")
async def get_users():
    response = requests.get(f"https://randomuser.me/api/?results={os.environ['N_RESULTS']}")
    return json.loads(response._content)
