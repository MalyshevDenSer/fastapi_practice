# from fastapi import Request, FastAPI
#
# app = FastAPI()
#
#
# @app.post('/sign_up')
# def sign_up(info):
#     req_info = info.json()
#     print(req_info)
#
# # @app.post('/unify_phone_from_json')
# # async def unify_phone_from_json(info: Request):
# #     req_info = await info.json()
# #     print(req_info)

from typing import Union

from fastapi import FastAPI, Request, Query
from pydantic import BaseModel
from pprint import pprint


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/sign_up")
async def create_item(item: Request):
    pprint(item)
    return item

#
# {"detail": [{"loc": ["query", "item"], "msg": "field required", "type": "value_error.missing"}]} %

# {"detail": [{"loc": ["body", "name"], "msg": "field required", "type": "value_error.missing"},
#             {"loc": ["body", "price"], "msg": "field required", "type": "value_error.missing"}]} %
