import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.models.outfit import Outfit
from app.models.clothing import ClothingItem
from app.models.user import User
from app.schemas.outfit import OutfitCreate, OutfitOut
from app.routers.auth import get_current_user
from app.services.ai_stylist import suggest_outfits

router = APIRouter()


@router.get("/", response_model=List[OutfitOut])
def list_outfits(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Outfit).filter(Outfit.owner_id == current_user.id).all()


@router.post("/", response_model=OutfitOut, status_code=201)
def create_outfit(body: OutfitCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    outfit = Outfit(
        owner_id=current_user.id,
        name=body.name,
        item_ids=json.dumps(body.item_ids),
        occasion=body.occasion,
        destination=body.destination,
        notes=body.notes,
        ai_generated=False,
    )
    db.add(outfit)
    db.commit()
    db.refresh(outfit)
    return outfit


@router.post("/ai-suggest", response_model=List[OutfitOut])
def ai_suggest(
    occasion: Optional[str] = None,
    destination: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    wardrobe = db.query(ClothingItem).filter(ClothingItem.owner_id == current_user.id).all()
    if not wardrobe:
        raise HTTPException(status_code=400, detail="Upload some clothes first.")

    suggestions = suggest_outfits(
        wardrobe=wardrobe,
        user=current_user,
        occasion=occasion,
        destination=destination,
    )

    saved = []
    for s in suggestions:
        outfit = Outfit(
            owner_id=current_user.id,
            name=s["name"],
            item_ids=json.dumps(s["item_ids"]),
            occasion=occasion,
            destination=destination,
            ai_generated=True,
            notes=s.get("notes"),
        )
        db.add(outfit)
        db.commit()
        db.refresh(outfit)
        saved.append(outfit)

    return saved


@router.delete("/{outfit_id}", status_code=204)
def delete_outfit(outfit_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    outfit = db.query(Outfit).filter(Outfit.id == outfit_id, Outfit.owner_id == current_user.id).first()
    if not outfit:
        raise HTTPException(status_code=404, detail="Outfit not found")
    db.delete(outfit)
    db.commit()
