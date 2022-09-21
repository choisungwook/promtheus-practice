from fastapi import FastAPI
from prometheus_client import start_http_server, Counter

REQUEST_COUNTER = Counter('app_requests_count', 'total requets count')

app = FastAPI()

METRICS_PORT = 5500
start_http_server(METRICS_PORT)

@app.get("/")
def read_root():
    REQUEST_COUNTER.inc()
    return {"Hello": "World"}
