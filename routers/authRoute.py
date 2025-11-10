from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas import userSchema
from methods import authMethod
from core.database import get_db

# Create an APIRouter instance
router = APIRouter(
    prefix="/api/users",
    tags=["auth"]
)


@router.post("/register", response_model=userSchema.UserInDB, status_code=status.HTTP_201_CREATED)
def register_user(user: userSchema.UserAuth, db: Session = Depends(get_db)):
    return authMethod.register_user_to_db(db, user)

@router.post("/token")
def login_for_access_token(user: userSchema.UserAuth, db: Session = Depends(get_db)):
    return authMethod.authenticate_user_and_get_token(db, user)