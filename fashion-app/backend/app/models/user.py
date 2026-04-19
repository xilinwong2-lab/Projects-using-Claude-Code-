from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)

    # Avatar / body profile
    height_cm = Column(Float)
    weight_kg = Column(Float)
    body_shape = Column(String)       # e.g. hourglass, pear, rectangle
    face_shape = Column(String)       # e.g. oval, round, square
    skin_tone = Column(String)        # e.g. warm, cool, neutral
    style_preferences = Column(String)  # JSON string of preferred styles
    celebrity_inspirations = Column(String)  # JSON string of names

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    clothing_items = relationship("ClothingItem", back_populates="owner")
    outfits = relationship("Outfit", back_populates="owner")
