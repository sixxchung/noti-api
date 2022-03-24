import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from dataclasses import asdict
from typing import Optional

import uvicorn
from fastapi import FastAPI
from app.routes import index, auth

from app.common.config import conf
from app.database.conn import db


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
    app.add_middleware(AccessControl, 
        except_path_list=EXCEPT_PATH_LIST, 
        except_path_regex=EXCEPT_PATH_REGEX
    )
    app.add_middleware(CORSMiddleware,
        allow_origins=conf().ALLOW_SITE,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(TrustedHostMiddleware, 
        allowed_hosts=conf().TRUSTED_HOSTS, except_path=["/health"]
    )

    # 라우터 정의
    app.include_router(index.router)
    app.include_router(auth.router, tags=["Authentication"], prefix="/auth")
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8886, reload=True)
