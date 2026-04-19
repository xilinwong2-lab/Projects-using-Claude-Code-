from pydantic import BaseModel
from typing import Optional, List


class OutfitCreate(BaseModel):
    name: Optional[str] = None
    item_ids: List[int]
    occasion: Optional[str] = None
    destination: Optional[str] = None
    notes: Optional[str] = None


class OutfitOut(BaseModel):
    id: int
    name: Optional[str]
    item_ids: List[int]
    occasion: Optional[str]
    destination: Optional[str]
    ai_generated: bool
    notes: Optional[str]

    class Config:
        from_attributes = True
