"""
CineStox Configuration Settings
"""

from pydantic_settings import BaseSettings
from typing import List, Optional
import os


class Settings(BaseSettings):
    """Application settings"""
    
    # App Info
    APP_NAME: str = "CineStox"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "CineStox: The Movie Stock Market"
    
    # Security
    SECRET_KEY: str = "cinestox-super-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    ALGORITHM: str = "HS256"
    
    # Database
    DATABASE_URL: str = "postgresql://cinestox:password@localhost:15432/cinestox"
    REDIS_URL: str = "redis://localhost:16379"
    
    # CORS
    ALLOWED_HOSTS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001", 
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001"
    ]
    
    # External APIs
    TMDB_API_KEY: Optional[str] = None
    REDDIT_CLIENT_ID: Optional[str] = None
    REDDIT_CLIENT_SECRET: Optional[str] = None
    REDDIT_USER_AGENT: str = "CineStox/1.0 (by /u/CineStoxBot)"
    TWITTER_API_KEY: Optional[str] = None
    TWITTER_API_SECRET: Optional[str] = None
    
    # Telugu NLP
    GOOGLE_CLOUD_PROJECT_ID: Optional[str] = None
    GOOGLE_CLOUD_CREDENTIALS: Optional[str] = None
    
    # Trading Engine
    INITIAL_BALANCE: float = 10000.0  # Starting balance for new users
    MAX_LEVERAGE: float = 5.0  # Maximum leverage allowed
    LIQUIDATION_THRESHOLD: float = 0.1  # 10% margin call threshold
    
    # Reddit Integration
    SUBREDDITS: List[str] = [
        "tollywood",
        "ne_bonda", 
        "bollywood",
        "kollywood"
    ]
    
    # Event Settings
    FDFS_HYPE_RADIUS_KM: float = 50.0  # Radius for FDFS hype zones
    SANKRANTHI_BATTLE_DURATION_DAYS: int = 3
    
    # NFT Settings
    NFT_MINTING_FEE: float = 100.0  # Cost to mint prediction NFTs
    MAX_NFT_SUPPLY: int = 1000  # Maximum NFTs per movie
    
    # Analytics
    ELASTICSEARCH_URL: str = "http://localhost:9200"
    SENTIMENT_ANALYSIS_ENABLED: bool = True
    
    # Performance
    MAX_CONCURRENT_TRADES: int = 1000
    WEBSOCKET_HEARTBEAT_INTERVAL: int = 30  # seconds
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()

# Environment-specific overrides
if os.getenv("ENVIRONMENT") == "production":
    settings.DEBUG = False
    settings.ALLOWED_HOSTS = [
        "https://cinestox.com",
        "https://app.cinestox.com"
    ]
elif os.getenv("ENVIRONMENT") == "staging":
    settings.DEBUG = True
    settings.ALLOWED_HOSTS = [
        "https://staging.cinestox.com",
        "http://localhost:3000"
    ] 