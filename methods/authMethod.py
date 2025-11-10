from sqlalchemy.orm import Session
from models import userModels
from schemas import userSchema
from fastapi import HTTPException, status
from utils import security


def register_user_to_db(db: Session, user: userSchema.UserCreate):
    db_user = db.query(userModels.User).filter(userModels.User.user_name == user.user_name).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User name already registered"
        )
    
    hashed_password = security.Hasher.get_password_hash(user.password)

    db_user = userModels.User(
        user_name=user.user_name, 
        hashed_password=hashed_password 
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user