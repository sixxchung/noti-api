from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.security import APIKeyHeader
from fastapi import FastAPI, Depends
import uvicorn
from typing import Optional
from dataclasses import asdict
from app.common.consts import EXCEPT_PATH_LIST, EXCEPT_PATH_REGEX
from app.database.conn import db
from app.common.config import conf
from app.middlewares.token_validator import access_control
from app.middlewares.trusted_hosts import TrustedHostMiddleware
from app.routes import index, auth, users, services
import os
import sys

# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


API_KEY_HEADER = APIKeyHeader(name="Authorization", auto_error=False)


def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)
    # 데이터 베이스 이니셜라이즈

    # 레디스 이니셜라이즈

    # 미들웨어 정의
    app.add_middleware(middleware_class=BaseHTTPMiddleware,
                       dispatch=access_control)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=conf().ALLOW_SITE,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=conf(
    ).TRUSTED_HOSTS, except_path=["/health"])

    # 라우터 정의
    app.include_router(index.router)
    app.include_router(auth.router, tags=["Authentication"], prefix="/api")
    if conf().DEBUG:
        app.include_router(services.router, tags=[
                           "Services"], prefix="/api", dependencies=[Depends(API_KEY_HEADER)])
    else:
        app.include_router(services.router, tags=["Services"], prefix="/api")

    app.include_router(users.router, tags=[
                       "Users"], prefix="/api", dependencies=[Depends(API_KEY_HEADER)])
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8886, reload=True)