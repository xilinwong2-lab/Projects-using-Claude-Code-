from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, closet, outfits, shopping

app = FastAPI(
    title="AI Fashion App API",
    description="Personal AI stylist — digital closet, outfit suggestions, and shopping recommendations.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(closet.router, prefix="/closet", tags=["Closet"])
app.include_router(outfits.router, prefix="/outfits", tags=["Outfits"])
app.include_router(shopping.router, prefix="/shopping", tags=["Shopping"])


@app.get("/")
def root():
    return {"message": "AI Fashion App API is running."}
