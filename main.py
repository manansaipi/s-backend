from fastapi import FastAPI
from core.database import init_db
from routers import favoritesRoute, authRoute
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
    return "Movie Favorites API is running! Check /docs for endpoints."

app.include_router(authRoute.router)
app.include_router(favoritesRoute.router)
