from datetime import datetime
from sqlalchemy import DateTime, Column, Integer, String
from app.database import Base

class URL(Base):
    """
    Represents a shortened URL.
    """
    __tablename__ = "urls"
    
    id = Column(Integer,
                primary_key = True, index = True)
    
    original_url = Column(
        String, 
        nullable = False,
    )

    short_url = Column(
        String(10),
        unique = True,
        nullable = False,
        index = True,
    )

    click_count = Column(
        Integer,
        default = 0,
        nullable = False,
    )

    created_at = Column(
        DateTime,
        default = datetime.utcnow,
        nullable = False,
    )