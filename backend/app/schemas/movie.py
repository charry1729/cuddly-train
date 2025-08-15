"""
CineStox Movie Pydantic Schemas
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum


class MovieLanguage(str, Enum):
    """Movie language enumeration"""
    TELUGU = "te"
    HINDI = "hi"
    TAMIL = "ta"
    KANNADA = "ka"
    MALAYALAM = "ml"
    ENGLISH = "en"
    MULTILINGUAL = "multilingual"


class MovieStatus(str, Enum):
    """Movie status enumeration"""
    ANNOUNCED = "announced"
    IN_PRODUCTION = "in_production"
    SHOOTING = "shooting"
    POST_PRODUCTION = "post_production"
    TRAILER_RELEASED = "trailer_released"
    RELEASED = "released"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class MovieResponse(BaseModel):
    """Movie response schema"""
    id: str
    title: str
    telugu_title: Optional[str] = None
    display_title: str
    contract_symbol: str
    language: MovieLanguage
    status: MovieStatus
    genre: List[str] = []
    
    # Trading data
    current_price: float
    price_change_24h: float
    price_change_percentage: float
    volume_24h: float
    market_cap: float
    
    # Hype and sentiment
    hype_score: float
    hype_level: str
    reddit_sentiment: float
    sentiment_emoji: str
    
    # Metadata
    poster_url: Optional[str] = None
    trailer_url: Optional[str] = None
    is_trading_active: bool
    is_telugu_movie: bool
    
    # Timestamps
    created_at: Optional[datetime] = None
    last_price_update: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class MovieListResponse(BaseModel):
    """Movie list response schema with pagination"""
    movies: List[MovieResponse]
    total: int
    skip: int
    limit: int
    has_more: bool


class MovieSearchParams(BaseModel):
    """Movie search parameters"""
    language: Optional[MovieLanguage] = None
    status: Optional[MovieStatus] = None
    genre: Optional[str] = None
    search: Optional[str] = None
    sort_by: str = "hype_score"
    sort_order: str = "desc"
    skip: int = 0
    limit: int = 20


class MovieMarketData(BaseModel):
    """Movie market data response"""
    movie_id: str
    contract_symbol: str
    current_price: float
    price_change_24h: float
    price_change_percentage: float
    high_24h: float
    low_24h: float
    volume_24h: float
    market_cap: float
    hype_score: float
    reddit_sentiment: float
    twitter_sentiment: float
    trailer_reaction_score: float
    available_shares: int
    total_shares: int
    last_price_update: Optional[datetime] = None
    is_trading_active: bool


class MovieTeluguInfo(BaseModel):
    """Telugu-specific movie information"""
    movie_id: str
    telugu_title: Optional[str] = None
    display_title: str
    telugu_description: str
    star_actor: Optional[str] = None
    heroine: Optional[str] = None
    music_director: Optional[str] = None
    cinematographer: Optional[str] = None
    is_telugu_movie: bool
    language: str
    hype_level: str
    sentiment_emoji: str


class MovieCreate(BaseModel):
    """Movie creation schema"""
    title: str = Field(..., min_length=1, max_length=255)
    telugu_title: Optional[str] = Field(None, max_length=255)
    contract_symbol: str = Field(..., min_length=1, max_length=10, pattern="^[A-Z]+$")
    language: MovieLanguage = MovieLanguage.TELUGU
    genre: List[str] = []
    director: List[str] = []
    cast: List[str] = []
    star_actor: Optional[str] = None
    heroine: Optional[str] = None
    music_director: Optional[str] = None
    cinematographer: Optional[str] = None
    synopsis: Optional[str] = None
    budget: Optional[float] = None
    release_date: Optional[datetime] = None


class MovieUpdate(BaseModel):
    """Movie update schema"""
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    telugu_title: Optional[str] = Field(None, max_length=255)
    genre: Optional[List[str]] = None
    director: Optional[List[str]] = None
    cast: Optional[List[str]] = None
    star_actor: Optional[str] = None
    heroine: Optional[str] = None
    music_director: Optional[str] = None
    cinematographer: Optional[str] = None
    synopsis: Optional[str] = None
    budget: Optional[float] = None
    release_date: Optional[datetime] = None
    trailer_release_date: Optional[datetime] = None
    teaser_release_date: Optional[datetime] = None
    poster_url: Optional[str] = None
    backdrop_url: Optional[str] = None
    trailer_url: Optional[str] = None


class MoviePriceUpdate(BaseModel):
    """Movie price update schema"""
    new_price: float = Field(..., gt=0)
    volume: Optional[float] = None
    timestamp: Optional[datetime] = None


class MovieHypeUpdate(BaseModel):
    """Movie hype score update schema"""
    new_hype_score: float = Field(..., ge=0, le=100)
    source: Optional[str] = None
    timestamp: Optional[datetime] = None


class MovieSentimentUpdate(BaseModel):
    """Movie sentiment update schema"""
    reddit_sentiment: Optional[float] = Field(None, ge=-100, le=100)
    twitter_sentiment: Optional[float] = Field(None, ge=-100, le=100)
    source: Optional[str] = None
    timestamp: Optional[datetime] = None


class TrendingMovie(BaseModel):
    """Trending movie schema"""
    movie: MovieResponse
    trend_score: float
    trend_reason: str
    volume_change_24h: float
    hype_change_24h: float


class FDFSMovie(BaseModel):
    """FDFS movie schema"""
    movie: MovieResponse
    release_date: datetime
    fdfs_hype_score: float
    theater_count: Optional[int] = None
    advance_booking_status: str = "Not Started"
    clan_boost_multiplier: float = 1.0


class FestivalMovie(BaseModel):
    """Festival release movie schema"""
    movie: MovieResponse
    festival_name: str
    festival_date: datetime
    festival_hype_multiplier: float
    competing_movies: List[str] = []
    festival_ranking: Optional[int] = None 