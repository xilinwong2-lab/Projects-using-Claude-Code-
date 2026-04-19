from fastapi import APIRouter, Depends
from app.models.user import User
from app.routers.auth import get_current_user
from app.services.shopping import find_similar_items

router = APIRouter()


@router.get("/recommendations")
def recommendations(
    category: str,
    style: str = "",
    color: str = "",
    current_user: User = Depends(get_current_user),
):
    results = find_similar_items(category=category, style=style, color=color, user=current_user)
    return {"items": results}
