from fastapi import APIRouter, FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import Optional

itemRouter = APIRouter(prefix="/itms", tags=["Items"])

items = []


# In-memory DB
items_db = {}


class ItemCreate(BaseModel):
    name: str
    price: float

class ItemUpdate(BaseModel):
    name: str
    price: float

class ItemPatch(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float



@itemRouter.get("/")
def read_root():
    return {"message": "FastAPI is running 🚀"}


@itemRouter.get("/")
def push_item(item: str):
    items.append(item)
    return items

# POST (Create)
@itemRouter.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate):
    item_id = len(items_db) + 1
    items_db[item_id] = item.dict()
    return {"id": item_id, **items_db[item_id]}

#@itemRouter.post("/")
def create_item(item: str = Query(..., description="Item name", min_length=1)):
    items.append(item)
    return items

@itemRouter.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


# PUT (Full Update)
@itemRouter.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemUpdate):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    items_db[item_id] = item.dict()
    return {"id": item_id, **items_db[item_id]}

# PATCH (Partial Update)
@itemRouter.patch("/{item_id}", response_model=ItemResponse)
def patch_item(item_id: int, item: ItemPatch):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    stored_item = items_db[item_id]

    update_data = item.dict(exclude_unset=True)
    stored_item.update(update_data)

    return {"id": item_id, **stored_item}

# DELETE
@itemRouter.delete("/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    del items_db[item_id]
    return {"message": "Item deleted successfully"}