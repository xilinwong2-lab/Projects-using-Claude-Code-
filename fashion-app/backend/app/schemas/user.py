from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    body_shape: Optional[str] = None
    face_shape: Optional[str] = None
    skin_tone: Optional[str] = None
    style_preferences: Optional[list[str]] = None
    celebrity_inspirations: Optional[list[str]] = None


class UserOut(BaseModel):
    id: int
    email: str
    full_name: Optional[str]
    body_shape: Optional[str]
    face_shape: Optional[str]
    skin_tone: Optional[str]

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
