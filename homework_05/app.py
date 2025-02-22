from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/ping/")
async def name_func():
    return {"message": "pong"}
