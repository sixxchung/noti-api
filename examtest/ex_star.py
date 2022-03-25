from starlette.applications import Starlette
from starlette.responses    import JSONResponse
from starlette.routing      import Route

from starlette.responses    import PlainTextResponse

async def homepage(request):
    return JSONResponse({'hello':'world'})
#app = Starlette(debug=True, routes=[Route('/', homepage)])

async def app_plain(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, World!')
    await response(scope, receive, send)
 