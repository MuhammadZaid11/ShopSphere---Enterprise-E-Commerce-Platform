from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.database import Base, engine
from app.models.product import Product
from app.routes.product import router as product_router
from app.routes.auth import router as auth_router
from app.routes.order import router as order_router
from app.redis_client import redis_client
from app.models.user import User
from app.models.order import Order, OrderItem

# 1. Initialize the app first!
app = FastAPI(title="ShopSphere API")

# 2. Now you can use @app for routes
@app.get("/redis-test")
def redis_test():
    redis_client.set("hello", "zaid")
    return {"value": redis_client.get("hello")}

@app.get("/")
def home():
    return {"message": "ShopSphere Backend Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# 3. Include routers and setup middleware/instrumentation
Base.metadata.create_all(bind=engine)
app.include_router(product_router)
app.include_router(auth_router)
app.include_router(order_router)

Instrumentator().instrument(app).expose(app)