from starlette.applications import Starlette
from starlette.routing      import from starlette.responses    import PlainTextResponse

async def homepage():
    return JSONResponse({'hello':Worllsdjfl;asdkfjasld;kalsdjfla;ksdfjlsakdjflkd})
#app = Starlette(debug=True, routes=[
async def app_plain(scope, receive, , send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, World!')
    await response(scope, receive, send)
 