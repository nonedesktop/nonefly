from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()


@app.get("/nonefly/simple/status")
def status():
    return {"message": "active"}


@app.get("/nonefly/simple/file/list")
@app.get("/nonefly/simple/instances/{instance}/file/list")
def file_list(instance: str, dir: str, token: str):
    return {"instance": instance, "directory": dir, "token": token}


@app.websocket("/nonefly/ws")
def wsconn():
    ...


if __name__ == "__main__":
    uvicorn.run("noneflyd:app")