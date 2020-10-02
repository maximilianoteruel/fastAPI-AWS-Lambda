from fastapi import APIRouter, WebSocket

from app.cruds.notes import crud_note
from app.schemas.notes import Note
from app.core.db.session import SessionScoped

router = APIRouter()


@router.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        note = crud_note.get(db=SessionScoped, id=int(data))
        result = f"Note ID: {data} | "
        if note:
            result += str(note.__dict__)
        else:
            result += "Not found"
        await websocket.send_text(result)


# Test Endpoint
from fastapi.responses import HTMLResponse
from app.core.settings import get_settings

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("{get_settings().API_HOST.replace("http://","ws://")}/v1/notes/ws/");
            ws.onmessage = function(event) {{
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            }};
            function sendMessage(event) {{
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }}
        </script>
    </body>
</html>
"""


@router.get("/test")
async def get():
    return HTMLResponse(html)
