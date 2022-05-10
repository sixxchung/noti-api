import json
import os
from time import time, sleep

import yagmail

import requests
from fastapi import APIRouter
from fastapi.logger import logger
from starlette.background import BackgroundTasks
from starlette.requests import Request

from app.errors import exceptions as ex

from app.models import MessageOk, KakaoMsgBody, SendEmail

router = APIRouter(prefix='/services')


@router.get('')
async def get_all_services(request: Request):
    return dict(your_email=request.state.user.email)


@router.post('/kakao/send')
async def send_kakao(request: Request, body: KakaoMsgBody):
    # for headers ----
    token = os.environ.get(
        "KAKAO_KEY", "YB0ZooZ33a3cikIPAxRKE5zx_HlQtg8c_V3m4go9c-sAAAGArEK-Eg")
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Bearer {token}"
    }
    # for data ----
    # body = {
    #     "object_type": "text",
    #     "text": "텍스트 영역입니다. 최대 200자 표시 가능합니다.",
    #     "link": {
    #         "web_url": "https://developers.kakao.com",
    #         "mobile_web_url": "https://developers.kakao.com"
    #     },
    #     "button_title": "바로 확인"
    # }
    body = dict(
        object_type="text",
        text=body.msg,
        link=dict(
            web_url="https://onesixx.com",
            mobile_web_url="https://onesixx.com"
        ),
        button_title="지금 확인"
    )
    data = {"template_object": json.dumps(body, ensure_ascii=False)}

    res = requests.post(
        "https://kapi.kakao.com/v2/api/talk/memo/default/send", headers=headers, data=data)

    try:
        res.raise_for_status()
        if res.json()["result_code"] != 0:
            raise Exception("KAKAO SEND FAILED")
    except Exception as e:
        print(res.json())
        logger.warning(e)
        raise ex.KakaoSendFailureEx

    return MessageOk()


email_content = """
{} 님, find the attachement.
"""
def send_email(**kwargs):
    #os.environ["EMAIL_addr"]= 'sixx.chung@gmail.com'
    mailing_list = kwargs.get("mailing_list", None)
    email_pw = os.environ.get("EMAIL_PW", None)
    email_addr   = os.environ.get("EMAIL_ADDR", "sixx.chung@gmail.com")
    last_email   = ""
    print(f' {email_addr}:{email_pw} to {mailing_list}')
    if mailing_list:
        try:
            yag = yagmail.SMTP({email_addr: "sixx"}, email_pw)
            # https://myaccount.google.com/u/1/lesssecureapps
            for m_l in mailing_list:
                contents = [ email_content.format(m_l.name) ]
                sleep(1)
                yag.send(m_l.email, '이렇게 한번 보내봅시다.', contents)
                last_email = m_l.email
            return True
        except Exception as e:
            print(e)
            print(last_email)
    print("발송 실패시 실패라고 알려야 합니다.")

@router.post("email/send_by_gmail")
async def email_by_gmail(request: Request, mailing_list: SendEmail):
    t = time()  
    send_email(mailing_list=mailing_list.email_to) 
    print("+*+*" * 30)
    print(str(round((time() - t) * 1000, 5)) + "ms")
    print("+*+*" * 30)
    return MessageOk()

@router.post("email/send_by_gmail2")
async def email_by_gmail2(request: Request, mailing_list: SendEmail, background_tasks: BackgroundTasks):
    background_tasks.add_task(
        send_email, mailing_list=mailing_list.email_to
    )
    return MessageOk()

