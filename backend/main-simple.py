"""
CineStox: The Movie Stock Market - Simplified Main
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn

from app.core.config import settings
from app.core.database import engine, Base
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

# Simple movies endpoint
@app.get("/api/v1/movies")
async def list_movies():
    """List all movies"""
    return {
        "movies": [
            {
                "id": "1",
                "title": "RRR",
                "telugu_title": "ఆర్‌ఆర్‌ఆర్",
                "contract_symbol": "RRR",
                "current_price": 450.0,
                "hype_score": 95.0,
                "status": "released"
            },
            {
                "id": "2", 
                "title": "Pushpa: The Rise",
                "telugu_title": "పుష్ప: ది రైజ్",
                "contract_symbol": "PUSHPA",
                "current_price": 320.0,
                "hype_score": 88.0,
                "status": "released"
            },
            {
                "id": "3",
                "title": "Salaar",
                "telugu_title": "సలార్", 
                "contract_symbol": "SALAAR",
                "current_price": 180.0,
                "hype_score": 92.0,
                "status": "in_production"
            }
        ],
        "total": 3
    }

if __name__ == "__main__":
    uvicorn.run(
        "main-simple:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 