"""
Pydantic schemas for request and response validation.
"""

from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    """
    Request schema for creating a shortened URL.
    """
    original_url: HttpUrl


class URLResponse(BaseModel):
    """
    Response schema returned after creating a short URL.
    """
    id: int
    original_url: HttpUrl
    short_code: str
    click_count: int

    class Config:
        from_attributes = True