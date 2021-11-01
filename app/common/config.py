from dataclasses import dataclass, asdict
from os          import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

# dictionary형태로 가져오기 위해 dataclass형태로 사용
@dataclass
class Config:
    """
    기본 Configuration  부모클래스
    """
    BASE_DIR= base_dir
    DB_POOL_RECYCLE:int = 900
    DB_ECHO:bool = True

@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    DB_URL:str = "+pymysql://travis@localhost/notification_api?charset=utf8mb4"
    TRUSTED_HOSTS=["*"]
    ALLOW_SITE=["*"]

# print(LocalConfig())
# LocalConfig()
# LocalConfig().DB_ECHO

# def abc(DB_ECHO=None, DB_POOL_RECYCLE=None, **kwargs): 
#     print(DB_ECHO, DB_POOL_RECYCLE)
# abc(LocalConfig())

# asdict(LocalConfig())
# arg = asdict(LocalConfig())
# abc(arg)
# abc(**arg)

@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False

    TRUSTED_HOSTS=["*"]
    ALLOW_SITE=["*"]

def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))

