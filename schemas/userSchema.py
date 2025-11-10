from pydantic import BaseModel

class UserCreate(BaseModel):
    user_name: str
    password: str

class UserInDB(BaseModel):
    id: int
    user_name: str