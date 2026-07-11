"""
Application entry point.
"""

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from starlette.status import HTTP_301_MOVED_PERMANENTLY
from app.logging import logger
from app.models import urls

from app.config import settings
from app.crud import (
    create_short_url,
    get_url_by_short_code,
    increment_click_count,
)
from app.database import Base, engine, get_db
from app.schemas import URLCreate, URLResponse

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/health")
def health():
    return {"status": "healthy"}
logger.info("Health check endpoint called")


@app.post("/shorten", response_model=URLResponse)
def short_code(
    url: URLCreate,
    db: Session = Depends(get_db),
):
    return create_short_url(db, url)
logger.info(f"Creating short URL for {urls.original_url}")
logger.info(f"Redirecting {short_code}")


@app.get("/{short_code}")
def redirect_url(
    short_code: str,
    db: Session = Depends(get_db),
):
    db_url = get_url_by_short_code(db, short_code)

    if db_url is None:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found",
        )

    increment_click_count(db, db_url)

    return RedirectResponse(
    url=db_url.original_url,
    status_code=HTTP_301_MOVED_PERMANENTLY,
)