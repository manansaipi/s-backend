from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas import favoriteSchema, movieSchema
from methods import favoriteMethod
from core.database import get_db

# Create an APIRouter instance
router = APIRouter(
    prefix="/api/favorites",
    tags=["favorites"]
)

# GET /api/favorites/{user_id}: Get all favorites for a specific user
@router.get("/{user_id}", response_model=list[favoriteSchema.FavoriteOut])
def list_favorites(user_id: str, db: Session = Depends(get_db)):
    favorites = favoriteMethod.get_favorites_by_user(db=db, user_id=user_id)
    return favorites

# POST /api/favorites: Add a new favorite
@router.post("/add-favorite", response_model=favoriteSchema.FavoriteOut, status_code=status.HTTP_201_CREATED)
def add_favorite(favorite_data: favoriteSchema.FavoriteCreate, db: Session = Depends(get_db)):
    return favoriteMethod.create_favorite(db=db, favorite_data=favorite_data)

# DELETE /api/favorites/{fav_id}: remmove a favorite by id
@router.delete("/{fav_id}", status_code=status.HTTP_200_OK)
def remove_favorite(fav_id: int, db: Session = Depends(get_db)):
    return favoriteMethod.delete_favorite(db=db, fav_id=fav_id)



