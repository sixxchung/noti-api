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
async def read_items(item: Item, q: Optional[str] = None):   # Query(None)
    results = {"items": [{"item_id": "Foo"}, **item.dict()]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items1/")
async def read_items(q: Optional[str] = fastapi.Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

if __name__ == '__main__':
    uvicorn.run("request_body:app", host="0.0.0.0", port=8886, reload=True)