"""
CineStox User Model
"""

from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, Text, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime
import uuid


class User(Base):
    """User model for CineStox"""
    
    __tablename__ = "users"
    
    # Core user fields
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), unique=True, nullable=False, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    
    # Profile information
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    
    # Telugu-specific fields
    telugu_name = Column(String(100), nullable=True)  # Name in Telugu script
    preferred_language = Column(String(10), default="en")  # en, te, hi
    voice_commands_enabled = Column(Boolean, default=True)
    
    # Trading profile
    initial_balance = Column(Float, default=10000.0)
    current_balance = Column(Float, default=10000.0)
    total_profit_loss = Column(Float, default=0.0)
    trading_score = Column(Integer, default=1000)  # ELO-style rating
    research_score = Column(Integer, default=0)  # Points for research activities
    
    # Clan and community
    clan_id = Column(String(36), nullable=True, index=True)
    clan_role = Column(String(50), nullable=True)  # Leader, Member, etc.
    reddit_username = Column(String(50), nullable=True)
    reddit_karma = Column(Integer, default=0)
    
    # Verification and status
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    is_premium = Column(Boolean, default=False)
    email_verified = Column(Boolean, default=False)
    phone_verified = Column(Boolean, default=False)
    
    # Preferences and settings
    notification_preferences = Column(JSON, default={
        "email": True,
        "push": True,
        "sms": False,
        "telugu": False
    })
    trading_preferences = Column(JSON, default={
        "max_leverage": 2.0,
        "auto_liquidation": True,
        "risk_tolerance": "medium"
    })
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    trades = relationship("Trade", back_populates="user")
    portfolio = relationship("Portfolio", back_populates="user")
    predictions = relationship("Prediction", back_populates="user")
    nfts = relationship("NFT", back_populates="owner")
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
    
    @property
    def full_name(self) -> str:
        """Get user's full name"""
        if self.telugu_name and self.preferred_language == "te":
            return self.telugu_name
        return f"{self.first_name or ''} {self.last_name or ''}".strip()
    
    @property
    def is_telugu_user(self) -> bool:
        """Check if user prefers Telugu"""
        return self.preferred_language in ["te", "hi"]
    
    @property
    def can_trade(self) -> bool:
        """Check if user can trade"""
        return (
            self.is_active and 
            self.is_verified and 
            self.email_verified and
            self.current_balance > 0
        )
    
    @property
    def trading_level(self) -> str:
        """Get user's trading level based on score"""
        if self.trading_score >= 2000:
            return "Legendary Trader"
        elif self.trading_score >= 1500:
            return "Expert Trader"
        elif self.trading_score >= 1000:
            return "Advanced Trader"
        elif self.trading_score >= 500:
            return "Intermediate Trader"
        else:
            return "Beginner Trader"
    
    def update_balance(self, amount: float, trade_type: str = "trade"):
        """Update user balance after trade"""
        self.current_balance += amount
        if trade_type == "trade":
            self.total_profit_loss += amount
        self.updated_at = datetime.utcnow()
    
    def add_research_points(self, points: int, activity: str):
        """Add research points for activities"""
        self.research_score += points
        self.updated_at = datetime.utcnow()
    
    def get_telugu_greeting(self) -> str:
        """Get greeting in Telugu"""
        if self.preferred_language == "te":
            return f"నమస్కారం {self.telugu_name or self.username}!"
        return f"Hello {self.username}!"
    
    def to_dict(self, include_sensitive: bool = False) -> dict:
        """Convert user to dictionary"""
        data = {
            "id": self.id,
            "username": self.username,
            "email": self.email if include_sensitive else None,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "telugu_name": self.telugu_name,
            "preferred_language": self.preferred_language,
            "current_balance": self.current_balance,
            "trading_score": self.trading_score,
            "research_score": self.research_score,
            "clan_id": self.clan_id,
            "clan_role": self.clan_role,
            "is_verified": self.is_verified,
            "is_premium": self.is_premium,
            "trading_level": self.trading_level,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "last_login": self.last_login.isoformat() if self.last_login else None
        }
        
        if include_sensitive:
            data.update({
                "phone": self.phone,
                "reddit_username": self.reddit_username,
                "notification_preferences": self.notification_preferences,
                "trading_preferences": self.trading_preferences
            })
        
        return data 