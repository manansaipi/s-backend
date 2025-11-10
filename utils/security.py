from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from core.config import SECRET_KEY
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher:
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        """Checks if the plain password matches the stored hash."""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str):
        """Returns the hash of the provided password."""
        return pwd_context.hash(password)
    
class AccessToken:
    def create_access_token(data: dict):
        """Generates an access token with a user_name payload."""
        to_encode = data.copy()
        
        access_token_expires = timedelta(minutes=30)
        expire = datetime.now() + access_token_expires
        
        to_encode.update({"exp": expire}) 
        
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

        return encoded_jwt
    
   