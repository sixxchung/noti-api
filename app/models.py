from enum import Enum

from pydantic.main import BaseModel
from pydantic.networks import EmailStr

class SnsType(str, Enum): # Request모델 - incoming 들어오는거 
    email:str    = "email"
    facebook:str = "facebook"
    google:str   = "google"
    kakao:str    = "kakao"


class Token(BaseModel):  #Response모델 - 나가는거 , 이런 모델을 가지고 있는 객체를 json으로 변경해서 내보냄 
    Authorization: str = None


class UserToken(BaseModel):
    id: int
    pw: str           = None
    email: str        = None
    name: str         = None
    phone_number: str = None
    profile_img: str  = None
    sns_type: str     = None

    class Config:
        orm_mode = True


class UserRegister(BaseModel):
    # pip install 'pydantic[email]'
    email: EmailStr = None
    pw: str         = None