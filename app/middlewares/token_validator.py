import time
import typing
import re

import jwt

from fastapi.params import Header
from jwt.exceptions import ExpiredSignatureError, DecodeError
from pydantic import BaseModel
from starlette.requests import Request
from starlette.datastructures import URL, Headers
from starlette.responses import JSONResponse
from app.errors import exceptions as ex
from starlette.types import ASGIApp, Receive, Scope, Send

from app.common import config, consts
from app.common.config import conf
from app.errors.exceptions import APIException
from app.models import UserToken

from app.utils.date_utils import D

from app.common.consts import EXCEPT_PATH_LIST, EXCEPT_PATH_REGEX
from app.utils.logger import api_logger
# class AccessControl:
#     def __init__(
#
#         app: ASGIApp,
#         except_path_list: typing.Sequence[str] = None,
#         except_path_regex: str = None,
#     ) -> None:
#         if except_path_list is None:
#             except_path_list = ["*"]
#         app = app
#         except_path_list = except_path_list
#         except_path_regex = except_path_regex

# async def __call__( scope: Scope, receive: Receive, send: Send) -> None:


async def access_control(request: Request, call_next):
    #request = Request(scope=scope)
    request.state.req_time = D.datetime()
    request.state.start = time.time()
    request.state.inspect = None
    request.state.user = None
    request.state.is_admin_access = None
    headers = request.headers
    #headers = Headers(scope=scope)
    ip = headers["x-forwarded-for"] if "x-forwarded-for" in headers.keys() else request.client.host
    print(f'sixx---ip: {ip}')
    request.state.ip = ip.split(",")[0] if "," in ip else ip
    cookies = request.cookies
    url = request.url.path

    if await url_pattern_check(url, EXCEPT_PATH_REGEX) or url in EXCEPT_PATH_LIST:
        response = await call_next(request)
        if url != "/":
            await api_logger(request=request, response=response)
        return response
    try:
        if url.startswith("/api"):
            # api 인경우 헤더로 토큰 검사
            if "authorization" in headers.keys():
                token_info = await token_decode(access_token=headers.get("Authorization"))
                request.state.user = UserToken(**token_info)
                # 토큰 없음
            else:
                if "Authorization" not in headers.keys():
                    print("=====Autho=========")
                    raise ex.NotAuthorized()
        else:
            # 템플릿 렌더링인 경우 쿠키에서 토큰 검사
            cookies["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTQsImVtYWlsIjoia29hbGFAZGluZ3JyLmNvbSIsIm5hbWUiOm51bGwsInBob25lX251bWJlciI6bnVsbCwicHJvZmlsZV9pbWciOm51bGwsInNuc190eXBlIjpudWxsfQ.4vgrFvxgH8odoXMvV70BBqyqXOFa2NDQtzYkGywhV48"

            if "Authorization" not in cookies.keys():
                raise ex.NotAuthorized()

            token_info = await token_decode(access_token=cookies.get("Authorization"))
            request.state.user = UserToken(**token_info)

        response = await call_next(request)
        await api_logger(request=request, response=response)
        # request.state.req_time = D.datetime()
        # res = await app(scope, receive, send)
    # except APIException as e:
    except Exception as e:
        error = await exception_handler(e)
        error_dict = dict(status=error.status_code, msg=error.msg,
                          detail=error.detail, code=error.code)
        response = JSONResponse(
            status_code=error.status_code, content=error_dict)
        await api_logger(request=request, error=error)
    # finally:
        # Logging
    return response

# @staticmethod


async def url_pattern_check(path, pattern):
    result = re.match(pattern, path)
    if result:
        return True
    return False


# @staticmethod
async def token_decode(access_token):
    """
    :param access_token:
    :return:
    """
    try:
        access_token = access_token.replace("Bearer ", "")
        payload = jwt.decode(access_token, key=consts.JWT_SECRET, algorithms=[
                             consts.JWT_ALGORITHM])
    except ExpiredSignatureError:
        raise ex.TokenExpiredEx()
    except DecodeError:
        raise ex.TokenDecodeEx()
    return payload


# @staticmethod
async def exception_handler(error: Exception):
    if not isinstance(error, APIException):
        error = APIException(ex=error, detail=str(error))
    return error
