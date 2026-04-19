from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class ClothingItem(Base):
    __tablename__ = "clothing_items"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    name = Column(String)
    category = Column(String, nullable=False)  # top, bottom, dress, skirt, outerwear, accessory, shoes
    color = Column(String)
    brand = Column(String)
    material = Column(String)
    style_tags = Column(String)   # JSON list, e.g. ["casual", "summer"]
    image_url = Column(String)    # S3 URL
    is_favorite = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    owner = relationship("User", back_populates="clothing_items")
