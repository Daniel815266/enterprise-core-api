from fastapi import FastAPI
from src.api.v1 import health

app = FastAPI(
    title="Enterprise Core API",
    description="High-performance backend with automated cloud provisioning.",
    version="1.0.0"
)

app.include_router(health.router)
