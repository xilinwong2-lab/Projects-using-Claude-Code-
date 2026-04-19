from pydantic import BaseModel
from typing import Optional, List


class ClothingItemCreate(BaseModel):
    name: Optional[str] = None
    category: str   # top, bottom, dress, skirt, outerwear, accessory, shoes
    color: Optional[str] = None
    brand: Optional[str] = None
    material: Optional[str] = None
    style_tags: Optional[List[str]] = None


class ClothingItemOut(BaseModel):
    id: int
    name: Optional[str]
    category: str
    color: Optional[str]
    brand: Optional[str]
    material: Optional[str]
    style_tags: Optional[List[str]]
    image_url: Optional[str]
    is_favorite: bool

    class Config:
        from_attributes = True
