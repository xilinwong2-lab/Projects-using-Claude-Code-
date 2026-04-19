from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Outfit(Base):
    __tablename__ = "outfits"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    name = Column(String)
    item_ids = Column(String, nullable=False)   # JSON list of ClothingItem IDs
    occasion = Column(String)                   # e.g. casual, formal, travel, beach
    destination = Column(String)                # optional travel context
    ai_generated = Column(String, default=False)
    notes = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    owner = relationship("User", back_populates="outfits")
