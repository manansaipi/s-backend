from fastapi import FastAPI
from core.database import engine, Base
from routers import favoritesRoute as favorites_router

# create the database tables on starttup (if they don't already exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="S-API",
    version="1.0.0",
    description="Backend service for managing user movie favorites."
)


@app.get('/')
def index():
    a=0
    return "Movie Favorites API is running! Check /docs for endpoints."

app.include_router(favorites_router.router)
