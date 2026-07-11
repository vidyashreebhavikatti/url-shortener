"""
Database configuration.

This module creates the SQLAlchemy engine, session factory,
and declarative base used throughout the application.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo = True
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

# Base class for all database models
Base = declarative_base()

def get_db():
    """
    Dependency that provides a database session.

    FastAPI will use this function to inject a database session
    into API endpoints.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
