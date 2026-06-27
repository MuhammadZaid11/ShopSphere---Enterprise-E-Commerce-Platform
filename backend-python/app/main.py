from fastapi import FastAPI

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="ShopSphere API")

@app.get("/")

def home():
    return {"message": "ShopSphere Backend Running"}

@app.get("/health")

def health():
    return {"status": "healthy"}

# Enable Prometheus metrics

Instrumentator().instrument(app).expose(app)