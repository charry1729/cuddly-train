"""
CineStox Movie Model
"""

from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, Text, JSON, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime
import uuid
import enum


class MovieStatus(enum.Enum):
    """Movie release status"""
    ANNOUNCED = "announced"
    IN_PRODUCTION = "in_production"
    SHOOTING = "shooting"
    POST_PRODUCTION = "post_production"
    TRAILER_RELEASED = "trailer_released"
    RELEASED = "released"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class MovieLanguage(enum.Enum):
    """Movie language"""
    TELUGU = "te"
    HINDI = "hi"
    TAMIL = "ta"
    KANNADA = "ka"
    MALAYALAM = "ml"
    ENGLISH = "en"
    MULTILINGUAL = "multilingual"


class Movie(Base):
    """Movie model for CineStox trading"""
    
    __tablename__ = "movies"
    
    # Core movie fields
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tmdb_id = Column(Integer, unique=True, nullable=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    original_title = Column(String(255), nullable=True)  # Title in original language
    telugu_title = Column(String(255), nullable=True)  # Title in Telugu
    
    # Basic information
    language = Column(Enum(MovieLanguage), default=MovieLanguage.TELUGU)
    status = Column(Enum(MovieStatus), default=MovieStatus.ANNOUNCED)
    genre = Column(JSON, default=[])  # List of genres
    runtime = Column(Integer, nullable=True)  # in minutes
    budget = Column(Float, nullable=True)  # in USD
    production_company = Column(String(255), nullable=True)
    
    # Release information
    release_date = Column(DateTime(timezone=True), nullable=True)
    trailer_release_date = Column(DateTime(timezone=True), nullable=True)
    teaser_release_date = Column(DateTime(timezone=True), nullable=True)
    
    # Cast and crew
    director = Column(JSON, default=[])  # List of directors
    cast = Column(JSON, default=[])  # List of main cast
    producer = Column(JSON, default=[])  # List of producers
    
    # Telugu-specific fields
    star_actor = Column(String(100), nullable=True)  # Main hero
    heroine = Column(String(100), nullable=True)
    music_director = Column(String(100), nullable=True)
    cinematographer = Column(String(100), nullable=True)
    
    # Trading contract fields
    contract_symbol = Column(String(10), unique=True, nullable=False, index=True)  # e.g., "PUSHPA", "RRR"
    initial_price = Column(Float, default=100.0)  # Starting stock price
    current_price = Column(Float, default=100.0)
    total_shares = Column(Integer, default=1000000)  # Total shares available
    available_shares = Column(Integer, default=1000000)  # Shares available for trading
    
    # Market data
    market_cap = Column(Float, default=100000000.0)  # Total market value
    volume_24h = Column(Float, default=0.0)  # 24-hour trading volume
    price_change_24h = Column(Float, default=0.0)  # 24-hour price change %
    high_24h = Column(Float, default=100.0)  # 24-hour high
    low_24h = Column(Float, default=100.0)  # 24-hour low
    
    # Hype and sentiment
    hype_score = Column(Float, default=50.0)  # 0-100 hype rating
    reddit_sentiment = Column(Float, default=0.0)  # -100 to +100 sentiment
    twitter_sentiment = Column(Float, default=0.0)
    trailer_reaction_score = Column(Float, default=0.0)  # Trailer performance
    
    # Box office predictions
    predicted_opening_weekend = Column(Float, nullable=True)  # in USD
    predicted_lifetime = Column(Float, nullable=True)  # in USD
    actual_opening_weekend = Column(Float, nullable=True)
    actual_lifetime = Column(Float, nullable=True)
    
    # Event flags
    is_fdfs_event = Column(Boolean, default=False)  # First Day First Show
    is_festival_release = Column(Boolean, default=False)  # Sankranthi, Diwali, etc.
    is_clan_boosted = Column(Boolean, default=False)  # Boosted by fan clans
    
    # Metadata
    poster_url = Column(String(500), nullable=True)
    backdrop_url = Column(String(500), nullable=True)
    trailer_url = Column(String(500), nullable=True)
    synopsis = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_price_update = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    trades = relationship("Trade", back_populates="movie")
    portfolio_holdings = relationship("Portfolio", back_populates="movie")
    predictions = relationship("Prediction", back_populates="movie")
    nfts = relationship("NFT", back_populates="movie")
    
    def __repr__(self):
        return f"<Movie(id={self.id}, title='{self.title}', symbol='{self.contract_symbol}')>"
    
    @property
    def display_title(self) -> str:
        """Get display title based on user preference"""
        if self.telugu_title:
            return self.telugu_title
        return self.original_title or self.title
    
    @property
    def is_telugu_movie(self) -> bool:
        """Check if movie is Telugu"""
        return self.language == MovieLanguage.TELUGU
    
    @property
    def is_trading_active(self) -> bool:
        """Check if movie is actively trading"""
        return (
            self.status in [
                MovieStatus.ANNOUNCED,
                MovieStatus.IN_PRODUCTION,
                MovieStatus.SHOOTING,
                MovieStatus.POST_PRODUCTION,
                MovieStatus.TRAILER_RELEASED
            ] and
            self.available_shares > 0
        )
    
    @property
    def price_change_percentage(self) -> float:
        """Calculate price change percentage"""
        if self.initial_price == 0:
            return 0.0
        return ((self.current_price - self.initial_price) / self.initial_price) * 100
    
    @property
    def market_cap_current(self) -> float:
        """Calculate current market cap"""
        return self.current_price * self.total_shares
    
    @property
    def hype_level(self) -> str:
        """Get hype level description"""
        if self.hype_score >= 80:
            return "🔥 INSANE HYPE"
        elif self.hype_score >= 60:
            return "🚀 HIGH HYPE"
        elif self.hype_score >= 40:
            return "📈 MODERATE HYPE"
        elif self.hype_score >= 20:
            return "📊 LOW HYPE"
        else:
            return "😴 NO HYPE"
    
    @property
    def sentiment_emoji(self) -> str:
        """Get sentiment emoji based on Reddit sentiment"""
        if self.reddit_sentiment >= 50:
            return "🚀"
        elif self.reddit_sentiment >= 20:
            return "📈"
        elif self.reddit_sentiment >= -20:
            return "➡️"
        elif self.reddit_sentiment >= -50:
            return "📉"
        else:
            return "💀"
    
    def update_price(self, new_price: float):
        """Update movie price and related metrics"""
        old_price = self.current_price
        self.current_price = new_price
        self.price_change_24h = ((new_price - old_price) / old_price) * 100
        
        # Update 24h high/low
        if new_price > self.high_24h:
            self.high_24h = new_price
        if new_price < self.low_24h:
            self.low_24h = new_price
        
        self.last_price_update = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    
    def update_hype_score(self, new_score: float):
        """Update hype score"""
        self.hype_score = max(0, min(100, new_score))
        self.updated_at = datetime.utcnow()
    
    def update_sentiment(self, reddit_score: float = None, twitter_score: float = None):
        """Update sentiment scores"""
        if reddit_score is not None:
            self.reddit_sentiment = max(-100, min(100, reddit_score))
        if twitter_score is not None:
            self.twitter_sentiment = max(-100, min(100, twitter_score))
        self.updated_at = datetime.utcnow()
    
    def get_telugu_description(self) -> str:
        """Get movie description in Telugu context"""
        if not self.is_telugu_movie:
            return f"{self.title} - {self.language.value.upper()} movie"
        
        desc = f"{self.telugu_title or self.title}"
        if self.star_actor:
            desc += f" - {self.star_actor} స్టార్"
        if self.director:
            desc += f" - {self.director[0]} దర్శకత్వం"
        if self.status == MovieStatus.TRAILER_RELEASED:
            desc += " - ట్రైలర్ విడుదలైంది"
        elif self.status == MovieStatus.RELEASED:
            desc += " - విడుదలైంది"
        
        return desc
    
    def to_dict(self, include_sensitive: bool = False) -> dict:
        """Convert movie to dictionary"""
        data = {
            "id": self.id,
            "title": self.title,
            "telugu_title": self.telugu_title,
            "display_title": self.display_title,
            "contract_symbol": self.contract_symbol,
            "language": self.language.value,
            "status": self.status.value,
            "genre": self.genre,
            "current_price": self.current_price,
            "price_change_24h": self.price_change_24h,
            "price_change_percentage": self.price_change_percentage,
            "hype_score": self.hype_score,
            "hype_level": self.hype_level,
            "reddit_sentiment": self.reddit_sentiment,
            "sentiment_emoji": self.sentiment_emoji,
            "market_cap": self.market_cap_current,
            "volume_24h": self.volume_24h,
            "is_trading_active": self.is_trading_active,
            "is_telugu_movie": self.is_telugu_movie,
            "poster_url": self.poster_url,
            "trailer_url": self.trailer_url,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "last_price_update": self.last_price_update.isoformat() if self.last_price_update else None
        }
        
        if include_sensitive:
            data.update({
                "tmdb_id": self.tmdb_id,
                "budget": self.budget,
                "predicted_opening_weekend": self.predicted_opening_weekend,
                "predicted_lifetime": self.predicted_lifetime,
                "available_shares": self.available_shares,
                "total_shares": self.total_shares
            })
        
        return data 