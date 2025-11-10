from sqlalchemy.orm import Session
from models import userModels
from schemas import userSchema
from fastapi import HTTPException, status, Depends
from utils.security import Hasher, AccessToken
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.config import SECRET_KEY
from sqlalchemy.orm import Session
from core.database import get_db
from jose import jwt, JWTError


bearer_scheme = HTTPBearer()

def authenticate_user_and_get_token(db: Session, user: userSchema.UserAuth):
    user_in_db = db.query(userModels.User).filter(userModels.User.user_name == user.user_name).first()

    if not user or not Hasher.verify_password(user.password, user_in_db.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user name or password",
        )

    access_token = AccessToken.create_access_token({"sub": user.user_name})

    return {"access_token": access_token, "token_type": "bearer"}

def register_user_to_db(db: Session, user: userSchema.UserAuth):
    db_user = db.query(userModels.User).filter(userModels.User.user_name == user.user_name).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User name already registered",
        )
    
    hashed_password = Hasher.get_password_hash(user.password)

    db_user = userModels.User(
        user_name=user.user_name, 
        hashed_password=hashed_password 
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), db: Session = Depends(get_db)):
        """Decodes the JWT and retrieves the user from the database."""
        # extract the raw token strring from the credentials object
        token = credentials.credentials

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user_name: str = payload.get("sub") 
            if user_name is None:
                raise JWTError

        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )

        user = db.query(userModels.User).filter(userModels.User.user_name == user_name).first() 
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        return user