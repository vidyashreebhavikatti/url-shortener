"""
Database CRUD operations.
"""

from sqlalchemy.orm import Session

from app.models import URL
from app.schemas import URLCreate
from app.utils import generate_short_code


def create_short_url(db: Session, url: URLCreate):
    """
    Create a shortened URL.
    """

    short_code = generate_short_code()

    db_url = URL(
        original_url=str(url.original_url),
        short_code=short_code,
    )

    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return db_url


def get_url_by_short_code(db: Session, short_code: str):
    """
    Find URL by short code.
    """
    return (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )


def increment_click_count(db: Session, url: URL):
    """
    Increase click count.
    """

    url.click_count += 1

    db.commit()

    db.refresh(url)