from fastapi import APIRouter

router = APIRouter()

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "operational", "version": "1.0.0"}
