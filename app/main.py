from typing import Optional
import uvicorn
from fastapi import FastAPI

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from dataclasses import asdict

from app.common.config import conf
from app.database.conn import db
from app.routes        import index, auth

def create_app():
    """
    앱 함수 실행
    :return:
    """
    app=FastAPI()

    c=conf()
    conf_dict = asdict(c)
    
    db.init_app(app, **conf_dict)

    # Initialize Database

    # Initialize Redis

    # define Middleware

    # define Router  (/routes/xxx.py)
    app.include_router(index.router)
    app.include_router(auth.router, tags=["Authentication"], prefix="/auth")

    # @app.get("/") 
    # def read_root():
    #     return {"Hello": "World"}

    # @app.get("/items/{item_id}")
    # def read_item(item_id: int, q: Optional[str] = None):
    #     return {"item_id": item_id, "q": q}    
    return app

#app = FastAPI()
app = create_app()




if __name__ == "__main__" :
    #uvicorn.run("main:app", host="0.0.0.0", port=8886, reload=conf().PROJ_RELOAD)
    uvicorn.run("app.main:app",host="0.0.0.0", port=8886, reload=True)