"""
CineStox Main API Router
"""

from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth,
    users,
    movies,
    trading,
    portfolio,
    predictions,
    clans,
    reddit,
    telugu,
    nft,
    analytics
)

# Main API router
api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

api_router.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

api_router.include_router(
    movies.router,
    prefix="/movies",
    tags=["Movies"]
)

api_router.include_router(
    trading.router,
    prefix="/trading",
    tags=["Trading"]
)

api_router.include_router(
    portfolio.router,
    prefix="/portfolio",
    tags=["Portfolio"]
)

api_router.include_router(
    predictions.router,
    prefix="/predictions",
    tags=["Predictions"]
)

api_router.include_router(
    clans.router,
    prefix="/clans",
    tags=["Clans"]
)

api_router.include_router(
    reddit.router,
    prefix="/reddit",
    tags=["Reddit Integration"]
)

api_router.include_router(
    telugu.router,
    prefix="/telugu",
    tags=["Telugu Features"]
)

api_router.include_router(
    nft.router,
    prefix="/nft",
    tags=["NFT Marketplace"]
)

api_router.include_router(
    analytics.router,
    prefix="/analytics",
    tags=["Analytics"]
) 