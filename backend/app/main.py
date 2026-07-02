from fastapi import FastAPI
from sqlalchemy import text

from app.api.user import router as user_router
from app.core.config import settings
from app.db.session import SessionLocal

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

app.include_router(
    user_router,
    prefix=settings.API_V1_PREFIX,
)


@app.get("/")
async def root():
    """
    Root endpoint.
    """

    return {
        "status": "running",
        "project": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "environment": settings.ENVIRONMENT,
    }


@app.get("/health")
async def health():
    """
    Check API and database health.
    """

    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception as exc:

        return {
            "status": "error",
            "database": str(exc),
        }

    finally:
        db.close()