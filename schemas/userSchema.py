from pydantic import BaseModel

class UserAuth(BaseModel):
    user_name: str
    password: str

class UserInDB(BaseModel):
    id: int
    user_name: str