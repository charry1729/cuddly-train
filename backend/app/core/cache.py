"""
CineStox Redis Cache Configuration
"""

import redis.asyncio as redis
from app.core.config import settings
import logging
import json
from typing import Optional, Any, Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Redis client
redis_client = redis.from_url(
    settings.REDIS_URL,
    encoding="utf-8",
    decode_responses=True,
    socket_keepalive=True,
    socket_keepalive_options={},
    retry_on_timeout=True
)


class CacheManager:
    """Redis cache manager for CineStox"""
    
    def __init__(self):
        self.client = redis_client
        self.default_ttl = 3600  # 1 hour default TTL
    
    async def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        """Set a key-value pair in cache"""
        try:
            if isinstance(value, (dict, list)):
                value = json.dumps(value)
            ttl = ttl or self.default_ttl
            return await self.client.set(key, value, ex=ttl)
        except Exception as e:
            logger.error(f"Cache set error for key {key}: {e}")
            return False
    
    async def get(self, key: str) -> Optional[Any]:
        """Get a value from cache"""
        try:
            value = await self.client.get(key)
            if value:
                try:
                    return json.loads(value)
                except json.JSONDecodeError:
                    return value
            return None
        except Exception as e:
            logger.error(f"Cache get error for key {key}: {e}")
            return None
    
    async def delete(self, key: str) -> bool:
        """Delete a key from cache"""
        try:
            return bool(await self.client.delete(key))
        except Exception as e:
            logger.error(f"Cache delete error for key {key}: {e}")
            return False
    
    async def exists(self, key: str) -> bool:
        """Check if a key exists in cache"""
        try:
            return bool(await self.client.exists(key))
        except Exception as e:
            logger.error(f"Cache exists error for key {key}: {e}")
            return False
    
    async def expire(self, key: str, ttl: int) -> bool:
        """Set expiration for a key"""
        try:
            return bool(await self.client.expire(key, ttl))
        except Exception as e:
            logger.error(f"Cache expire error for key {key}: {e}")
            return False


# Trading-specific cache methods
class TradingCache:
    """Cache methods specific to trading operations"""
    
    def __init__(self):
        self.cache = CacheManager()
    
    async def cache_movie_price(self, movie_id: str, price: float, ttl: int = 300):
        """Cache current movie price (5 minutes TTL)"""
        key = f"movie:price:{movie_id}"
        await self.cache.set(key, {"price": price, "timestamp": self._get_timestamp()}, ttl)
    
    async def get_movie_price(self, movie_id: str) -> Optional[Dict]:
        """Get cached movie price"""
        key = f"movie:price:{movie_id}"
        return await self.cache.get(key)
    
    async def cache_user_portfolio(self, user_id: str, portfolio: Dict, ttl: int = 600):
        """Cache user portfolio (10 minutes TTL)"""
        key = f"user:portfolio:{user_id}"
        await self.cache.set(key, portfolio, ttl)
    
    async def get_user_portfolio(self, user_id: str) -> Optional[Dict]:
        """Get cached user portfolio"""
        key = f"user:portfolio:{user_id}"
        return await self.cache.get(key)
    
    async def cache_trading_volume(self, movie_id: str, volume: Dict, ttl: int = 1800):
        """Cache trading volume (30 minutes TTL)"""
        key = f"movie:volume:{movie_id}"
        await self.cache.set(key, volume, ttl)
    
    async def get_trading_volume(self, movie_id: str) -> Optional[Dict]:
        """Get cached trading volume"""
        key = f"movie:volume:{movie_id}"
        return await self.cache.get(key)
    
    async def cache_hype_score(self, movie_id: str, score: float, ttl: int = 900):
        """Cache hype score (15 minutes TTL)"""
        key = f"movie:hype:{movie_id}"
        await self.cache.set(key, {"score": score, "timestamp": self._get_timestamp()}, ttl)
    
    async def get_hype_score(self, movie_id: str) -> Optional[Dict]:
        """Get cached hype score"""
        key = f"movie:hype:{movie_id}"
        return await self.cache.get(key)
    
    async def cache_reddit_sentiment(self, movie_id: str, sentiment: Dict, ttl: int = 3600):
        """Cache Reddit sentiment (1 hour TTL)"""
        key = f"reddit:sentiment:{movie_id}"
        await self.cache.set(key, sentiment, ttl)
    
    async def get_reddit_sentiment(self, movie_id: str) -> Optional[Dict]:
        """Get cached Reddit sentiment"""
        key = f"reddit:sentiment:{movie_id}"
        return await self.cache.get(key)
    
    async def cache_fdfs_hype_zone(self, location: str, hype_data: Dict, ttl: int = 1800):
        """Cache FDFS hype zone data (30 minutes TTL)"""
        key = f"fdfs:hype:{location}"
        await self.cache.set(key, hype_data, ttl)
    
    async def get_fdfs_hype_zone(self, location: str) -> Optional[Dict]:
        """Get cached FDFS hype zone data"""
        key = f"fdfs:hype:{location}"
        return await self.cache.get(key)
    
    def _get_timestamp(self) -> int:
        """Get current timestamp"""
        import time
        return int(time.time())


# Session cache methods
class SessionCache:
    """Cache methods for user sessions and authentication"""
    
    def __init__(self):
        self.cache = CacheManager()
    
    async def cache_user_session(self, user_id: str, session_data: Dict, ttl: int = 28800):
        """Cache user session (8 hours TTL)"""
        key = f"session:{user_id}"
        await self.cache.set(key, session_data, ttl)
    
    async def get_user_session(self, user_id: str) -> Optional[Dict]:
        """Get cached user session"""
        key = f"session:{user_id}"
        return await self.cache.get(key)
    
    async def invalidate_user_session(self, user_id: str) -> bool:
        """Invalidate user session"""
        key = f"session:{user_id}"
        return await self.cache.delete(key)
    
    async def cache_verification_code(self, email: str, code: str, ttl: int = 600):
        """Cache verification code (10 minutes TTL)"""
        key = f"verify:{email}"
        await self.cache.set(key, code, ttl)
    
    async def get_verification_code(self, email: str) -> Optional[str]:
        """Get cached verification code"""
        key = f"verify:{email}"
        data = await self.cache.get(key)
        return data if isinstance(data, str) else None


# Initialize cache managers
cache_manager = CacheManager()
trading_cache = TradingCache()
session_cache = SessionCache()


async def check_cache_health() -> bool:
    """Check if Redis cache is healthy"""
    try:
        await redis_client.ping()
        return True
    except Exception as e:
        logger.error(f"Cache health check failed: {e}")
        return False 