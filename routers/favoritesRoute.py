from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas import favoriteSchema
from methods import favoriteMethod, authMethod
from core.database import get_db
from models import userModels

# Create an APIRouter instance
router = APIRouter(
    prefix="/api/favorites",
    tags=["favorites"]
)

# GET /api/favorites/{user_id}: Get all favorites for a specific user
@router.get("", response_model=list[favoriteSchema.FavoriteOut])
def list_favorites(current_user: userModels.User = Depends(authMethod.get_current_user), db: Session = Depends(get_db)):
    favorites = favoriteMethod.get_favorites_by_user(db=db, current_user=current_user)
    return favorites

# POST /api/favorites: Add a new favorite
@router.post("/add-favorite", response_model=favoriteSchema.FavoriteOut, status_code=status.HTTP_201_CREATED)
def add_favorite(favorite_data: favoriteSchema.FavoriteCreate, db: Session = Depends(get_db), current_user: userModels.User = Depends(authMethod.get_current_user)):
    return favoriteMethod.create_favorite(db=db, favorite_data=favorite_data, current_user=current_user)

# DELETE /api/favorites/{fav_id}: remmove a favorite by id
@router.delete("/{fav_id}", status_code=status.HTTP_200_OK)
def remove_favorite(fav_id: int, db: Session = Depends(get_db), current_user: userModels.User = Depends(authMethod.get_current_user)):
    return favoriteMethod.delete_favorite(db=db, fav_id=fav_id, current_user=current_user)



