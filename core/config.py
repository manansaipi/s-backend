import os
from fastapi.middleware.cors import CORSMiddleware

ALLOWED_ORIGINS = [
    "http://localhost:5173",  
    "http://127.0.0.1:5173",
]

SECRET_KEY = os.getenv("SECRET_KEY", "A_VERY_LONG_AND_RANDOM_STRING_FOR_JWT_SIGNING!") 

def setup_cors(app):
    """Attach CORS middleware to FastAPI app."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
