from typing import Union

from fastapi import FastAPI, Request, Query
from pydantic import BaseModel


class UserData(BaseModel):
    name: str
    surname: str
    detailed_occupation: Union[str, None]
    password: str


app = FastAPI()

users_bd = {}


@app.post("/sign_up")
def create_item(data: UserData):
    user_id = max(users_bd, default=0) + 1
    users_bd[user_id] = {
        'name': data.name,
        'surname': data.surname,
        'detailed_occupation': data.detailed_occupation,
        'password': data.password
    }
    return 'Success'


@app.get("/give_all_bd")
def give_all_bd():
    return users_bd
