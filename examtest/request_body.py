import uvicorn
from typing import Optional
import fastapi
import pydantic

class Item(pydantic.BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = fastapi.FastAPI()


@app.get("/items0/")
async def read_items(q: Optional[str] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items1/")
async def read_items(q: Optional[str] = fastapi.Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results





@app.post("/item1/")
async def create_item(item: Item):
    return item

@app.post("/item2/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/item3/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


if __name__ == '__main__':
    uvicorn.run("request_body:app", host="0.0.0.0", port=8886, reload=True)