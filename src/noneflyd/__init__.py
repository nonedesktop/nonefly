from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()


@app.get("/nonefly/simple/status")
def status():
    return {"message": "active"}


@app.websocket("/nonefly/ws")
def wsconn():
    ...


if __name__ == "__main__":
    uvicorn.run("noneflyd:app")