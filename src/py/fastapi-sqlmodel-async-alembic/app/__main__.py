import uvicorn
from fastapi import FastAPI

from app import settings
from app.core.models import HealthCheck
from loguru import logger


logger.info(f"settings debug: {settings.debug}")

app = FastAPI(
    title = settings.project_name,
    version = settings.version,
    openapi_uri = f"{settings.api_v1_prefix}/openapi.json",
    debug = settings.debug
)

@app.get("/", response_model=HealthCheck, tags=["status"])
async def health_check():
    return {
        "name": settings.project_name,
        "version": settings.version,
        "description": settings.description
    }


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host="0.0.0.0", reload=True)