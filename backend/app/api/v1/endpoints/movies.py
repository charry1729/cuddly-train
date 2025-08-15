"""
CineStox Movies API Endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from typing import List, Optional
import logging

from app.core.database import get_db
from app.models.movie import Movie, MovieStatus, MovieLanguage
from app.schemas.movie import MovieResponse, MovieListResponse, MovieSearchParams
from app.core.cache import trading_cache

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=MovieListResponse)
async def list_movies(
    skip: int = Query(0, ge=0, description="Number of movies to skip"),
    limit: int = Query(20, ge=1, le=100, description="Number of movies to return"),
    language: Optional[MovieLanguage] = Query(None, description="Filter by language"),
    status: Optional[MovieStatus] = Query(None, description="Filter by status"),
    genre: Optional[str] = Query(None, description="Filter by genre"),
    search: Optional[str] = Query(None, description="Search by title"),
    sort_by: str = Query("hype_score", description="Sort by: hype_score, price_change_24h, volume_24h"),
    sort_order: str = Query("desc", description="Sort order: asc, desc"),
    db: AsyncSession = Depends(get_db)
):
    """
    List movies with filtering and sorting options
    """
    try:
        # Build query
        query = select(Movie)
        
        # Apply filters
        if language:
            query = query.where(Movie.language == language)
        if status:
            query = query.where(Movie.status == status)
        if genre:
            query = query.where(Movie.genre.contains([genre]))
        if search:
            search_term = f"%{search}%"
            query = query.where(
                (Movie.title.ilike(search_term)) |
                (Movie.telugu_title.ilike(search_term)) |
                (Movie.contract_symbol.ilike(search_term))
            )
        
        # Apply sorting
        if sort_by == "hype_score":
            sort_column = Movie.hype_score
        elif sort_by == "price_change_24h":
            sort_column = Movie.price_change_24h
        elif sort_by == "volume_24h":
            sort_column = Movie.volume_24h
        elif sort_by == "current_price":
            sort_column = Movie.current_price
        else:
            sort_column = Movie.hype_score
        
        if sort_order.lower() == "asc":
            query = query.order_by(sort_column.asc())
        else:
            query = query.order_by(sort_column.desc())
        
        # Apply pagination
        query = query.offset(skip).limit(limit)
        
        # Execute query
        result = await db.execute(query)
        movies = result.scalars().all()
        
        # Get total count for pagination
        count_query = select(func.count(Movie.id))
        if language:
            count_query = count_query.where(Movie.language == language)
        if status:
            count_query = count_query.where(Movie.status == status)
        if genre:
            count_query = count_query.where(Movie.genre.contains([genre]))
        if search:
            search_term = f"%{search}%"
            count_query = count_query.where(
                (Movie.title.ilike(search_term)) |
                (Movie.telugu_title.ilike(search_term)) |
                (Movie.contract_symbol.ilike(search_term))
            )
        
        total_result = await db.execute(count_query)
        total = total_result.scalar()
        
        # Convert to response models
        movie_responses = []
        for movie in movies:
            # Try to get cached price data
            cached_price = await trading_cache.get_movie_price(movie.id)
            if cached_price:
                movie.current_price = cached_price.get("price", movie.current_price)
            
            movie_responses.append(MovieResponse.from_orm(movie))
        
        return MovieListResponse(
            movies=movie_responses,
            total=total,
            skip=skip,
            limit=limit,
            has_more=skip + limit < total
        )
        
    except Exception as e:
        logger.error(f"Error listing movies: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch movies")


@router.get("/trending", response_model=List[MovieResponse])
async def get_trending_movies(
    limit: int = Query(10, ge=1, le=50, description="Number of trending movies to return"),
    db: AsyncSession = Depends(get_db)
):
    """
    Get trending movies based on hype score and volume
    """
    try:
        query = select(Movie).where(
            Movie.is_trading_active == True
        ).order_by(
            Movie.hype_score.desc(),
            Movie.volume_24h.desc()
        ).limit(limit)
        
        result = await db.execute(query)
        movies = result.scalars().all()
        
        # Update with cached data
        movie_responses = []
        for movie in movies:
            cached_price = await trading_cache.get_movie_price(movie.id)
            if cached_price:
                movie.current_price = cached_price.get("price", movie.current_price)
            
            movie_responses.append(MovieResponse.from_orm(movie))
        
        return movie_responses
        
    except Exception as e:
        logger.error(f"Error fetching trending movies: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch trending movies")


@router.get("/telugu", response_model=List[MovieResponse])
async def get_telugu_movies(
    limit: int = Query(20, ge=1, le=100, description="Number of Telugu movies to return"),
    db: AsyncSession = Depends(get_db)
):
    """
    Get Telugu movies specifically
    """
    try:
        query = select(Movie).where(
            Movie.language == MovieLanguage.TELUGU,
            Movie.is_trading_active == True
        ).order_by(
            Movie.hype_score.desc(),
            Movie.created_at.desc()
        ).limit(limit)
        
        result = await db.execute(query)
        movies = result.scalars().all()
        
        movie_responses = []
        for movie in movies:
            cached_price = await trading_cache.get_movie_price(movie.id)
            if cached_price:
                movie.current_price = cached_price.get("price", movie.current_price)
            
            movie_responses.append(MovieResponse.from_orm(movie))
        
        return movie_responses
        
    except Exception as e:
        logger.error(f"Error fetching Telugu movies: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch Telugu movies")


@router.get("/fdfs", response_model=List[MovieResponse])
async def get_fdfs_movies(
    db: AsyncSession = Depends(get_db)
):
    """
    Get movies with FDFS (First Day First Show) events
    """
    try:
        query = select(Movie).where(
            Movie.is_fdfs_event == True,
            Movie.is_trading_active == True
        ).order_by(
            Movie.release_date.asc(),
            Movie.hype_score.desc()
        )
        
        result = await db.execute(query)
        movies = result.scalars().all()
        
        movie_responses = []
        for movie in movies:
            cached_price = await trading_cache.get_movie_price(movie.id)
            if cached_price:
                movie.current_price = cached_price.get("price", movie.current_price)
            
            movie_responses.append(MovieResponse.from_orm(movie))
        
        return movie_responses
        
    except Exception as e:
        logger.error(f"Error fetching FDFS movies: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch FDFS movies")


@router.get("/{movie_id}", response_model=MovieResponse)
async def get_movie(
    movie_id: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Get detailed information about a specific movie
    """
    try:
        query = select(Movie).where(Movie.id == movie_id)
        result = await db.execute(query)
        movie = result.scalar_one_or_none()
        
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        
        # Get cached data
        cached_price = await trading_cache.get_movie_price(movie.id)
        if cached_price:
            movie.current_price = cached_price.get("price", movie.current_price)
        
        cached_hype = await trading_cache.get_hype_score(movie.id)
        if cached_hype:
            movie.hype_score = cached_hype.get("score", movie.hype_score)
        
        cached_sentiment = await trading_cache.get_reddit_sentiment(movie.id)
        if cached_sentiment:
            movie.reddit_sentiment = cached_sentiment.get("sentiment", movie.reddit_sentiment)
        
        return MovieResponse.from_orm(movie)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching movie {movie_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch movie")


@router.get("/{movie_id}/market-data")
async def get_movie_market_data(
    movie_id: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Get detailed market data for a movie
    """
    try:
        query = select(Movie).where(Movie.id == movie_id)
        result = await db.execute(query)
        movie = result.scalar_one_or_none()
        
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        
        # Get cached data
        cached_price = await trading_cache.get_movie_price(movie.id)
        cached_volume = await trading_cache.get_trading_volume(movie.id)
        cached_hype = await trading_cache.get_hype_score(movie.id)
        cached_sentiment = await trading_cache.get_reddit_sentiment(movie.id)
        
        market_data = {
            "movie_id": movie.id,
            "contract_symbol": movie.contract_symbol,
            "current_price": cached_price.get("price", movie.current_price) if cached_price else movie.current_price,
            "price_change_24h": movie.price_change_24h,
            "price_change_percentage": movie.price_change_percentage,
            "high_24h": movie.high_24h,
            "low_24h": movie.low_24h,
            "volume_24h": cached_volume.get("volume", movie.volume_24h) if cached_volume else movie.volume_24h,
            "market_cap": movie.market_cap_current,
            "hype_score": cached_hype.get("score", movie.hype_score) if cached_hype else movie.hype_score,
            "reddit_sentiment": cached_sentiment.get("sentiment", movie.reddit_sentiment) if cached_sentiment else movie.reddit_sentiment,
            "twitter_sentiment": movie.twitter_sentiment,
            "trailer_reaction_score": movie.trailer_reaction_score,
            "available_shares": movie.available_shares,
            "total_shares": movie.total_shares,
            "last_price_update": movie.last_price_update.isoformat() if movie.last_price_update else None,
            "is_trading_active": movie.is_trading_active
        }
        
        return market_data
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching market data for movie {movie_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch market data")


@router.get("/{movie_id}/telugu-info")
async def get_movie_telugu_info(
    movie_id: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Get Telugu-specific information about a movie
    """
    try:
        query = select(Movie).where(Movie.id == movie_id)
        result = await db.execute(query)
        movie = result.scalar_one_or_none()
        
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        
        telugu_info = {
            "movie_id": movie.id,
            "telugu_title": movie.telugu_title,
            "display_title": movie.display_title,
            "telugu_description": movie.get_telugu_description(),
            "star_actor": movie.star_actor,
            "heroine": movie.heroine,
            "music_director": movie.music_director,
            "cinematographer": movie.cinematographer,
            "is_telugu_movie": movie.is_telugu_movie,
            "language": movie.language.value,
            "hype_level": movie.hype_level,
            "sentiment_emoji": movie.sentiment_emoji
        }
        
        return telugu_info
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching Telugu info for movie {movie_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch Telugu info") 