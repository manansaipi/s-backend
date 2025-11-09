from fastapi import FastAPI
from core.database import init_db
from routers import favoritesRoute as favorites_router
from core.config import setup_cors

app = FastAPI(
    title="S-API",
    version="1.0.0",
    description="Backend service for managing user movie favorites."
)

setup_cors(app)
init_db() 

@app.get('/')
def index():
    a=0
    return "Movie Favorites API is running! Check /docs for endpoints."

app.include_router(favorites_router.router)
