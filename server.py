from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Add CORS middleware to allow WebSocket connections from your Godot client
origins = [
    "https://your-godot-client-domain.com",  # Replace with your actual client URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows connections from your specified domain
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (can be more restrictive if needed)
    allow_headers=["*"],  # Allows all headers (can be more restrictive if needed)
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Connected to WebSocket!")
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
