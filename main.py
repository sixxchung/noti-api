from fastapi import FastAPI

from typing  import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id:int, q:Optional[str]=None):
    return {"item_id": item_id, "q": q}

# uvicorn main:app --reload