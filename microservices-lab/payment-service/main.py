from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory storage
items = ["Book", "Laptop", "Phone"]

class Item(BaseModel):
    name: str

@app.get("/items")
def get_items():
    return items

@app.post("/items", status_code=201)
def add_item(item: Item):
    items.append(item.name)
    return {"message": f"Item added: {item.name}"}

@app.get("/items/{id}")
def get_item(id: int):
    if id < 0 or id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": id, "name": items[id]}
