from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.websocket import ConnectionManager


router = APIRouter()

manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()

            # await manager.send_personal_message(f"Você enviou: {data}", websocket)
            await manager.broadcast(f"Você enviou: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
