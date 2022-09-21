from fastapi import FastAPI
from prometheus_client import start_http_server

app = FastAPI()

METRICS_PORT = 5500
start_http_server(METRICS_PORT)

@app.get("/")
def read_root():
    return {"Hello": "World"}
