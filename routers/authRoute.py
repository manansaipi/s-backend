from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas import userSchema
from methods import authMethod
from core.database import get_db
from models import userModels

# Create an APIRouter instance
router = APIRouter(
    prefix="/api/users",
    tags=["auth"]
)


@router.post("/register", response_model=userSchema.UserInDB, status_code=status.HTTP_201_CREATED)
def register_user(user: userSchema.UserCreate, db: Session = Depends(get_db)):
    return authMethod.register_user_to_db(db, user)