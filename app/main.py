from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/mission/{name}")
def get_mission(name: str):
    return {"message": f"{name}, your mission is to explore strange new code, to seek out new infrastructure, to boldly deploy where no developer has deployed before"}



class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}