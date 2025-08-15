"""
CineStox: The Movie Stock Market
Main FastAPI application entry point
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import uvicorn

from app.core.config import settings
from app.core.database import engine, Base
from app.api.v1.api import api_router
from app.core.cache import redis_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    print("🚀 Starting CineStox...")
    
    # Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Test Redis connection
    try:
        await redis_client.ping()
        print("✅ Redis connected successfully")
    except Exception as e:
        print(f"❌ Redis connection failed: {e}")
    
    print("🎬 CineStox is ready for trading!")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down CineStox...")
    await engine.dispose()
    await redis_client.close()


# Create FastAPI app
app = FastAPI(
    title="CineStox: The Movie Stock Market",
    description="Where Film Fandom Meets Strategic Trading",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "CineStox",
        "version": "1.0.0",
        "message": "🎬 Ready for some movie trading action!"
    }

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint with CineStox branding"""
    return {
        "message": "Welcome to CineStox! 🎬📈",
        "tagline": "Where Film Fandom Meets Strategic Trading",
        "features": [
            "🔥 Hype-Driven Viral Mechanics",
            "🪖 Telugu Fan Army Ecosystem", 
            "🤝 Reddit Community Integration",
            "⚖️ Skill-Based Legal Compliance"
        ],
        "docs": "/docs",
        "health": "/health"
    }

# Error handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return {
        "error": "Route not found",
        "message": "The requested endpoint doesn't exist in CineStox",
        "available_endpoints": [
            "/api/v1/movies",
            "/api/v1/trading",
            "/api/v1/clans",
            "/api/v1/reddit"
        ]
    }

@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return {
        "error": "Internal server error",
        "message": "Something went wrong in the CineStox trading engine",
        "status": "Please try again later"
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 