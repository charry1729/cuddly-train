"""
CineStox Trading Models
"""

from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, Text, JSON, Enum, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime
import uuid
import enum


class TradeType(enum.Enum):
    """Trade type enumeration"""
    BUY = "buy"
    SELL = "sell"
    SHORT = "short"
    COVER = "cover"


class TradeStatus(enum.Enum):
    """Trade status enumeration"""
    PENDING = "pending"
    EXECUTED = "executed"
    CANCELLED = "cancelled"
    FAILED = "failed"


class PredictionType(enum.Enum):
    """Prediction type enumeration"""
    TRAILER_REACTION = "trailer_reaction"
    BOX_OFFICE = "box_office"
    OPENING_WEEKEND = "opening_weekend"
    LIFETIME_COLLECTION = "lifetime_collection"
    HYPE_SCORE = "hype_score"
    REDDIT_SENTIMENT = "reddit_sentiment"


class Trade(Base):
    """Trade model for CineStox"""
    
    __tablename__ = "trades"
    
    # Core trade fields
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    movie_id = Column(String(36), ForeignKey("movies.id"), nullable=False, index=True)
    
    # Trade details
    trade_type = Column(Enum(TradeType), nullable=False)
    status = Column(Enum(TradeStatus), default=TradeStatus.PENDING)
    shares = Column(Integer, nullable=False)  # Number of shares
    price_per_share = Column(Float, nullable=False)  # Price at execution
    total_amount = Column(Float, nullable=False)  # Total trade value
    
    # Leverage and margin
    leverage = Column(Float, default=1.0)  # Leverage used
    margin_required = Column(Float, nullable=False)  # Margin required
    margin_used = Column(Float, nullable=False)  # Actual margin used
    
    # Execution details
    executed_at = Column(DateTime(timezone=True), nullable=True)
    execution_price = Column(Float, nullable=True)  # Actual execution price
    slippage = Column(Float, default=0.0)  # Price slippage
    
    # P&L tracking
    profit_loss = Column(Float, default=0.0)  # Current P&L
    profit_loss_percentage = Column(Float, default=0.0)  # P&L percentage
    
    # Metadata
    order_id = Column(String(36), nullable=True)  # External order ID
    notes = Column(Text, nullable=True)  # User notes
    tags = Column(JSON, default=[])  # Trade tags
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="trades")
    movie = relationship("Movie", back_populates="trades")
    
    def __repr__(self):
        return f"<Trade(id={self.id}, type={self.trade_type.value}, shares={self.shares}, movie={self.movie_id})>"
    
    @property
    def is_open(self) -> bool:
        """Check if trade is still open"""
        return self.status == TradeStatus.EXECUTED and self.shares > 0
    
    @property
    def is_profitable(self) -> bool:
        """Check if trade is profitable"""
        return self.profit_loss > 0
    
    @property
    def trade_value(self) -> float:
        """Calculate current trade value"""
        return self.shares * (self.execution_price or self.price_per_share)
    
    def execute_trade(self, execution_price: float, slippage: float = 0.0):
        """Execute the trade"""
        self.execution_price = execution_price
        self.slippage = slippage
        self.status = TradeStatus.EXECUTED
        self.executed_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    
    def calculate_pnl(self, current_price: float):
        """Calculate current P&L"""
        if self.trade_type == TradeType.BUY:
            self.profit_loss = (current_price - self.execution_price) * self.shares
        elif self.trade_type == TradeType.SELL:
            self.profit_loss = (self.execution_price - current_price) * self.shares
        elif self.trade_type == TradeType.SHORT:
            self.profit_loss = (self.execution_price - current_price) * self.shares
        elif self.trade_type == TradeType.COVER:
            self.profit_loss = (current_price - self.execution_price) * self.shares
        
        if self.execution_price > 0:
            self.profit_loss_percentage = (self.profit_loss / (self.execution_price * self.shares)) * 100
        
        self.updated_at = datetime.utcnow()


class Portfolio(Base):
    """Portfolio model for user holdings"""
    
    __tablename__ = "portfolio"
    
    # Core fields
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    movie_id = Column(String(36), ForeignKey("movies.id"), nullable=False, index=True)
    
    # Holdings
    shares_owned = Column(Integer, default=0)  # Total shares owned
    shares_shorted = Column(Integer, default=0)  # Total shares shorted
    average_buy_price = Column(Float, default=0.0)  # Average purchase price
    average_sell_price = Column(Float, default=0.0)  # Average short price
    
    # Current value
    current_value = Column(Float, default=0.0)  # Current portfolio value
    total_invested = Column(Float, default=0.0)  # Total amount invested
    unrealized_pnl = Column(Float, default=0.0)  # Unrealized P&L
    realized_pnl = Column(Float, default=0.0)  # Realized P&L
    
    # Performance metrics
    total_return = Column(Float, default=0.0)  # Total return percentage
    return_24h = Column(Float, default=0.0)  # 24-hour return
    return_7d = Column(Float, default=0.0)  # 7-day return
    return_30d = Column(Float, default=0.0)  # 30-day return
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_trade_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="portfolio")
    movie = relationship("Movie", back_populates="portfolio_holdings")
    
    def __repr__(self):
        return f"<Portfolio(user={self.user_id}, movie={self.movie_id}, shares={self.shares_owned})>"
    
    @property
    def net_position(self) -> int:
        """Get net position (owned - shorted)"""
        return self.shares_owned - self.shares_shorted
    
    @property
    def is_long(self) -> bool:
        """Check if position is long"""
        return self.shares_owned > self.shares_shorted
    
    @property
    def is_short(self) -> bool:
        """Check if position is short"""
        return self.shares_shorted > self.shares_owned
    
    @property
    def is_flat(self) -> bool:
        """Check if position is flat"""
        return self.shares_owned == self.shares_shorted
    
    def update_holdings(self, trade: Trade):
        """Update portfolio based on trade"""
        if trade.trade_type == TradeType.BUY:
            # Calculate new average buy price
            total_cost = (self.shares_owned * self.average_buy_price) + (trade.shares * trade.execution_price)
            self.shares_owned += trade.shares
            self.average_buy_price = total_cost / self.shares_owned if self.shares_owned > 0 else 0
            
        elif trade.trade_type == TradeType.SELL:
            # Calculate realized P&L
            if self.shares_owned >= trade.shares:
                realized_pnl = (trade.execution_price - self.average_buy_price) * trade.shares
                self.realized_pnl += realized_pnl
                self.shares_owned -= trade.shares
                
        elif trade.trade_type == TradeType.SHORT:
            # Calculate new average short price
            total_proceeds = (self.shares_shorted * self.average_sell_price) + (trade.shares * trade.execution_price)
            self.shares_shorted += trade.shares
            self.average_sell_price = total_proceeds / self.shares_shorted if self.shares_shorted > 0 else 0
            
        elif trade.trade_type == TradeType.COVER:
            # Calculate realized P&L for short
            if self.shares_shorted >= trade.shares:
                realized_pnl = (self.average_sell_price - trade.execution_price) * trade.shares
                self.realized_pnl += realized_pnl
                self.shares_shorted -= trade.shares
        
        self.last_trade_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    
    def calculate_current_value(self, current_price: float):
        """Calculate current portfolio value and P&L"""
        self.current_value = (self.shares_owned * current_price) - (self.shares_shorted * current_price)
        
        # Calculate unrealized P&L
        long_pnl = (current_price - self.average_buy_price) * self.shares_owned if self.average_buy_price > 0 else 0
        short_pnl = (self.average_sell_price - current_price) * self.shares_shorted if self.average_sell_price > 0 else 0
        self.unrealized_pnl = long_pnl + short_pnl
        
        # Calculate total return
        total_value = self.current_value + self.realized_pnl
        if self.total_invested > 0:
            self.total_return = ((total_value - self.total_invested) / self.total_invested) * 100
        
        self.updated_at = datetime.utcnow()


class Prediction(Base):
    """Prediction model for user predictions"""
    
    __tablename__ = "predictions"
    
    # Core fields
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    movie_id = Column(String(36), ForeignKey("movies.id"), nullable=False, index=True)
    
    # Prediction details
    prediction_type = Column(Enum(PredictionType), nullable=False)
    predicted_value = Column(Float, nullable=False)  # Predicted value
    actual_value = Column(Float, nullable=True)  # Actual value when known
    confidence = Column(Float, default=50.0)  # User confidence 0-100
    
    # Scoring
    accuracy_score = Column(Float, default=0.0)  # How accurate the prediction was
    points_earned = Column(Integer, default=0)  # Research points earned
    
    # Metadata
    description = Column(Text, nullable=True)  # User's reasoning
    source = Column(String(100), nullable=True)  # Source of prediction
    tags = Column(JSON, default=[])  # Prediction tags
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=True)  # When prediction expires
    
    # Relationships
    user = relationship("User", back_populates="predictions")
    movie = relationship("Movie", back_populates="predictions")
    
    def __repr__(self):
        return f"<Prediction(id={self.id}, type={self.prediction_type.value}, user={self.user_id})>"
    
    @property
    def is_expired(self) -> bool:
        """Check if prediction has expired"""
        if not self.expires_at:
            return False
        return datetime.utcnow() > self.expires_at
    
    @property
    def is_resolved(self) -> bool:
        """Check if prediction has been resolved"""
        return self.actual_value is not None
    
    @property
    def accuracy_percentage(self) -> float:
        """Calculate accuracy percentage"""
        if not self.is_resolved or self.actual_value == 0:
            return 0.0
        
        error = abs(self.predicted_value - self.actual_value) / self.actual_value
        return max(0, (1 - error) * 100)
    
    def resolve_prediction(self, actual_value: float):
        """Resolve the prediction with actual value"""
        self.actual_value = actual_value
        self.accuracy_score = self.accuracy_percentage
        
        # Calculate points based on accuracy
        if self.accuracy_score >= 90:
            self.points_earned = 100
        elif self.accuracy_score >= 80:
            self.points_earned = 75
        elif self.accuracy_score >= 70:
            self.points_earned = 50
        elif self.accuracy_score >= 60:
            self.points_earned = 25
        else:
            self.points_earned = 10
        
        self.updated_at = datetime.utcnow()
    
    def get_prediction_summary(self) -> str:
        """Get a summary of the prediction"""
        if self.prediction_type == PredictionType.TRAILER_REACTION:
            return f"Predicted {self.predicted_value:.1f}% trailer reaction for {self.movie_id}"
        elif self.prediction_type == PredictionType.BOX_OFFICE:
            return f"Predicted ${self.predicted_value:,.0f} box office for {self.movie_id}"
        elif self.prediction_type == PredictionType.HYPE_SCORE:
            return f"Predicted {self.predicted_value:.1f} hype score for {self.movie_id}"
        else:
            return f"Predicted {self.predicted_value} for {self.movie_id}" 