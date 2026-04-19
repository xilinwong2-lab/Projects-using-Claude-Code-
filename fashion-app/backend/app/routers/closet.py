import json
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.models.clothing import ClothingItem
from app.models.user import User
from app.schemas.clothing import ClothingItemCreate, ClothingItemOut
from app.routers.auth import get_current_user
from app.services.image_classifier import classify_image
from app.services.storage import upload_image

router = APIRouter()


@router.get("/", response_model=List[ClothingItemOut])
def list_items(
    category: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    query = db.query(ClothingItem).filter(ClothingItem.owner_id == current_user.id)
    if category:
        query = query.filter(ClothingItem.category == category)
    return query.all()


@router.post("/", response_model=ClothingItemOut, status_code=201)
async def add_item(
    file: UploadFile = File(...),
    name: Optional[str] = None,
    category: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    image_bytes = await file.read()

    # Auto-classify if category not provided
    classification = classify_image(image_bytes)
    detected_category = category or classification.get("category", "other")
    detected_color = classification.get("color")
    detected_tags = classification.get("style_tags", [])

    image_url = upload_image(image_bytes, file.filename, current_user.id)

    item = ClothingItem(
        owner_id=current_user.id,
        name=name or classification.get("name"),
        category=detected_category,
        color=detected_color,
        style_tags=json.dumps(detected_tags),
        image_url=image_url,
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    item = db.query(ClothingItem).filter(ClothingItem.id == item_id, ClothingItem.owner_id == current_user.id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()


@router.patch("/{item_id}/favorite", response_model=ClothingItemOut)
def toggle_favorite(item_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    item = db.query(ClothingItem).filter(ClothingItem.id == item_id, ClothingItem.owner_id == current_user.id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.is_favorite = not item.is_favorite
    db.commit()
    db.refresh(item)
    return item
