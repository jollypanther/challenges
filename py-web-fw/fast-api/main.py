from random import randint
from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(
        title="The description of the item", max_length=100
    )
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(
        ..., gt=0, title="The description of the item"
    )
    qty: Optional[int] = 0


db = {}


@app.get("/")
def read_root():
    return {"Welcome": "To FastAPI"}


# No Path / Query Params
# http://127.0.0.1:8000/items
@app.get("/items")
def read_all_items():
    return db


# Mandatory Path and Optional Query Params
# When you declare additional arguments that are not part of the path,
# they are automatically interpreted as "query" parameters.
# http://127.0.0.1:8000/items/I_9999?[a=name]
@app.get("/items/{item_id}")
def read_item(item_id: int, a: Optional[str] = None):
    i = db.get(item_id, {})
    if a:
        return {a: i.get(a, "")}
    else:
        return i


# http://127.0.0.1:8000/items/I_9999?a=name
@app.get("/items/{item_id}/")
def read_item_attribute(item_id: int, q: str):
    i = db.get(item_id, {})
    return {q: i.get(q, "")}


# Request Body
# Body is interpreted as per (model) type of arguments
# {
#   "name": "item_name",
#   "description": "item description", // optional
#   "qty": 1, // optional
#   "price" : 10.1
# }
@app.post("/items")
def create_item(item: Item):
    item_id = randint(10, 91280128019)
    db.update({item_id: item.dict()})
    return {item_id: db[item_id]}


# Path, Query and Request Body with embedded
# {"item": {
#   "name": "item_name",
#   "description": "item description", // optional
#   "qty": 1, // optional
#   "price" : 10.1
# }}
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item = Body(..., embed=True)):
    db[item_id] = item.dict()
    return {item_id: db[item_id]}
