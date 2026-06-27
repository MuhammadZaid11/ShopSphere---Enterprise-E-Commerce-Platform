from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

# Database
from app.database import Base, engine

# Routers
from app.routes.product import router as product_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(
    title="ShopSphere API",
    description="Enterprise E-Commerce Backend API",
    version="1.0.0"
)

# Enable Prometheus Metrics
Instrumentator().instrument(app).expose(app)

# Register Routers
app.include_router(product_router)

# Root Endpoint
@app.get("/", tags=["Home"])
def home():
    return {
        "message": "🚀 Welcome to ShopSphere API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
        "metrics": "/metrics"
    }

# Health Check Endpoint
@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "healthy",
        "application": "ShopSphere API"
    }