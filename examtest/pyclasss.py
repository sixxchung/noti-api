import uvicorn
from typing import Optional, List, Set
import fastapi
import pydantic
from fastapi import Path, Query, Body
from pydantic import BaseModel, Field

app = fastapi.FastAPI()

class Item(pydantic.BaseModel):
    name: str
    description: Optional[str] = pydantic.Field(None, max_length=16)
    price: float = Field(..., gt=0, description=" must be greater than 0")
    tax: Optional[float] = None
    tags:list =[]
    tags:List[str]=[]
    tags:Set[str]= set()

@app.put("/items/xxxxxx}")
async def update_item(: int, item: Item = Body(..., embed=True)):
    results = {"": , "item": item}
    return results

if __name__ == '__main__':
    uvicorn.run("pyclasss:app", host="0.0.0.0", port=8886, reload=True)