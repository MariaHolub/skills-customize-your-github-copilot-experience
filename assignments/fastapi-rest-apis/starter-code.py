from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}


@app.get("/hello")
def read_hello():
    return {"message": "Hello from FastAPI!"}


@app.post("/items/")
def create_item(item: Item):
    return {"item": item}


@app.get("/items/{item_id}")
def read_item(item_id: int, discount: Optional[float] = None):
    response = {
        "item_id": item_id,
        "name": "Example item",
        "price": 9.99,
    }
    if discount is not None:
        response["discount"] = discount
        response["final_price"] = response["price"] - discount
    return response
