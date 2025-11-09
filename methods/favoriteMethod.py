from sqlalchemy.orm import Session
from models import favoriteModels
from schemas import favoriteSchema
from fastapi import HTTPException, status


def get_favorites_by_user(db: Session, user_id: str):
    return db.query(favoriteModels.Favorite).filter(favoriteModels.Favorite.user_id == user_id).all()

def create_favorite(db: Session, favorite_data: favoriteSchema.FavoriteCreate):
    # check if thhe movie already exists for this user
    existing_favorite = db.query(favoriteModels.Favorite).filter(
        favoriteModels.Favorite.user_id == favorite_data.user_id,
        favoriteModels.Favorite.movie_id == favorite_data.movie_id
    ).first()

    if existing_favorite:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Movie is already in favorites."
        )

    # Map the incoming data to the model
    db_favorite = favoriteModels.Favorite(
        user_id=favorite_data.user_id,
        movie_id=favorite_data.movie_id,
        title=favorite_data.title,
        poster_path=favorite_data.poster_path
    )
    
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite

# # 3. DELETE: Remove a favorite by its internal ID
def delete_favorite(db: Session, fav_id: int):
    favorite_to_delete = db.query(favoriteModels.Favorite).filter(favoriteModels.Favorite.id == fav_id).first()

    if not favorite_to_delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Favorite with ID {fav_id} not found."
        )

    db.delete(favorite_to_delete)
    db.commit()
    return {"message": f"Favorite {fav_id} successfully removed."}