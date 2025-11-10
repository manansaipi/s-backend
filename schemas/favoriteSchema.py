from pydantic import BaseModel

class FavoriteCreate(BaseModel):
    movie_id: int
    title: str
    poster_path: str | None = None

class FavoriteOut(BaseModel):
    id: int
    user_id: str
    movie_id: int
    title: str
    poster_path: str | None

    class Config:
        orm_mode = True