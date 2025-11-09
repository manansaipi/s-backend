from pydantic import BaseModel, Field

class MovieData(BaseModel):
    id: int = Field(..., alias="tmdb_id", description="The ID from TMDB.")
    title: str = Field(..., description="Movie title.")
    poster_path: str | None = Field(None, description="Path to the movie poster.")


class MovieCreate(BaseModel):
    user_id: str = Field(..., description="The user ID marking this as a favorite.")
    movie: MovieData