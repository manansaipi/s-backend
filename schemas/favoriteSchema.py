from pydantic import BaseModel, Field

class FavoriteCreate(BaseModel):
    user_id: str
    movie_id: int
    title: str
    poster_path: str | None = None

class FavoriteOut(BaseModel):
    id: int
    user_id: str
    movie_id: int
    title: str
    poster_path: str | None