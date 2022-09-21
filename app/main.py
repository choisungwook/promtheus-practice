from fastapi import FastAPI
from prometheus_client import start_http_server, Counter

REQUEST_COUNTER = Counter(
    name='app_requests_count',
    documentation='total requets count',
    labelnames=['app_name', 'endpoint']
)

app = FastAPI()

METRICS_PORT = 5500
start_http_server(METRICS_PORT)

@app.get("/")
def read_root():
    REQUEST_COUNTER.labels('python-test-app', '/').inc()
    return {"Hello": "World"}
