from fastapi.middleware.cors import CORSMiddleware

# Allowed origins for frontend apps (adjust for production)
ALLOWED_ORIGINS = [
    "http://localhost:5173",  # React dev server
    "http://127.0.0.1:5173",
    # Add your deployed frontend URL here later
]

def setup_cors(app):
    """Attach CORS middleware to FastAPI app."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
