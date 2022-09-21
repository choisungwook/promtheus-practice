from fastapi import FastAPI
# from prometheus_client import start_http_server

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
