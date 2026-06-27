from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.database import Base, engine

# IMPORTANT
from app.models.product import Product

from app.routes.product import router as product_router

app = FastAPI(title="ShopSphere API")

Base.metadata.create_all(bind=engine)

app.include_router(product_router)

@app.get("/")
def home():
    return {"message": "ShopSphere Backend Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

Instrumentator().instrument(app).expose(app)