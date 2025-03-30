from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn

app = FastAPI()

clients = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)
    print("Client connected")

    try:
        while True:
            message = await websocket.receive_text()
            print(f"Received: {message}")

            # Broadcast message to all clients
            for client in clients:
                if client != websocket:
                    await client.send_text(message)
    
    except WebSocketDisconnect:
        print("Client disconnected")
        clients.remove(websocket)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
