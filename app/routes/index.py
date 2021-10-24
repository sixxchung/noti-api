from datetime import datetime

from fastapi import APIRouter
from starlette.responses import Response
from starlette.requests import Request

from inspect import currentframe as frame
from datetime import datetime

router = APIRouter()

@router.get("/")
async def index(): #index(session: Session=Depends(db.session)):
    """
    ELB 상태 체크용 API
    :return:
    """
    # user = Users(status='active')
    # session.add(user)
    # session.commit()
    #Users().create(session, auto_commit=Ture, name="꽐라")

    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")