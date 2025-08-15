# CineStox Project Structure

## 🏗️ Architecture Overview

CineStox is built as a modern, scalable microservices architecture with the following components:

```
CineStox/
├── 📁 backend/                    # FastAPI Python Backend
│   ├── 📁 app/
│   │   ├── 📁 api/               # API endpoints
│   │   │   └── 📁 v1/           # API version 1
│   │   │       ├── 📄 api.py    # Main router
│   │   │       └── 📁 endpoints/ # Individual endpoint modules
│   │   ├── 📁 core/              # Core configuration
│   │   │   ├── 📄 config.py     # Settings and environment
│   │   │   ├── 📄 database.py   # Database connection
│   │   │   └── 📄 cache.py      # Redis cache management
│   │   ├── 📁 models/            # Database models
│   │   │   ├── 📄 user.py       # User model
│   │   │   ├── 📄 movie.py      # Movie model
│   │   │   └── 📄 trading.py    # Trading models
│   │   ├── 📁 schemas/           # Pydantic schemas
│   │   │   └── 📄 movie.py      # Movie API schemas
│   │   ├── 📁 services/          # Business logic
│   │   └── 📁 utils/             # Utility functions
│   ├── 📄 main.py                # FastAPI app entry point
│   ├── 📄 requirements.txt       # Python dependencies
│   ├── 📄 Dockerfile             # Backend container
│   ├── 📄 init.sql               # Database seeding
│   └── 📄 env.example            # Environment template
│
├── 📁 frontend/                   # React Frontend
│   ├── 📁 src/
│   │   ├── 📁 components/        # Reusable components
│   │   │   ├── 📁 layout/        # Layout components
│   │   │   ├── 📁 common/        # Common UI components
│   │   │   └── 📁 trading/       # Trading-specific components
│   │   ├── 📁 pages/             # Page components
│   │   │   ├── 📄 HomePage.js    # Landing page
│   │   │   ├── 📄 MoviesPage.js  # Movie listings
│   │   │   ├── 📄 TradingPage.js # Trading interface
│   │   │   └── 📄 ...            # Other pages
│   │   ├── 📁 contexts/          # React contexts
│   │   ├── 📁 hooks/             # Custom hooks
│   │   ├── 📁 services/          # API services
│   │   ├── 📁 utils/             # Utility functions
│   │   ├── 📄 App.js             # Main app component
│   │   └── 📄 index.js           # App entry point
│   ├── 📄 package.json            # Node.js dependencies
│   ├── 📄 tailwind.config.js     # Tailwind CSS config
│   └── 📄 Dockerfile             # Frontend container
│
├── 📁 trading-engine/             # Real-time trading system
│   ├── 📁 price-feed/            # Price update services
│   ├── 📁 order-matching/        # Order matching engine
│   └── 📁 risk-management/       # Risk controls
│
├── 📁 telugu-nlp/                 # Telugu language processing
│   ├── 📁 voice-commands/        # Voice command processing
│   ├── 📁 sentiment-analysis/    # Telugu sentiment analysis
│   └── 📁 translation/           # Language translation
│
├── 📁 reddit-integration/         # Reddit community integration
│   ├── 📁 bots/                  # Reddit bots
│   ├── 📁 sentiment-scraper/     # Sentiment data collection
│   └── 📁 contract-generator/    # Post-to-contract conversion
│
├── 📁 nft-marketplace/            # NFT creation and trading
│   ├── 📁 minting/               # NFT minting service
│   ├── 📁 marketplace/           # NFT trading interface
│   └── 📁 metadata/              # NFT metadata management
│
├── 📁 analytics/                  # Data analysis and insights
│   ├── 📁 hype-trends/           # Hype trend analysis
│   ├── 📁 sentiment-analysis/    # Sentiment analysis
│   └── 📁 performance-metrics/   # Trading performance metrics
│
├── 📁 docs/                       # Documentation
│   ├── 📁 api/                   # API documentation
│   ├── 📁 user-guide/            # User guide
│   └── 📁 developer/             # Developer documentation
│
├── 📄 docker-compose.yml          # Service orchestration
├── 📄 start.sh                    # Startup script
├── 📄 README.md                   # Project overview
└── 📄 PROJECT_STRUCTURE.md        # This file
```

## 🔧 Technology Stack

### Backend
- **Framework**: FastAPI (Python 3.9+)
- **Database**: PostgreSQL 13+ with async SQLAlchemy
- **Cache**: Redis 6+ for real-time data
- **Search**: Elasticsearch 8+ for analytics
- **Authentication**: JWT with bcrypt
- **Real-time**: WebSockets for live trading

### Frontend
- **Framework**: React 18+ with hooks
- **Styling**: Tailwind CSS with custom design system
- **State Management**: Zustand + React Query
- **Animations**: Framer Motion
- **Charts**: Recharts for trading data
- **Icons**: Lucide React

### Infrastructure
- **Containerization**: Docker + Docker Compose
- **Database**: PostgreSQL with health checks
- **Cache**: Redis with persistence
- **Search**: Elasticsearch with single-node setup
- **Reverse Proxy**: Nginx for production routing

## 🚀 Key Features Implementation

### 1. Hype-Driven Viral Mechanics
- **Location**: `backend/app/services/hype_engine.py`
- **Frontend**: `frontend/src/components/trading/HypeTracker.js`
- **Real-time**: WebSocket price updates with hype multipliers

### 2. Telugu Fan Army Ecosystem
- **Location**: `backend/app/models/clan.py`
- **Frontend**: `frontend/src/pages/ClansPage.js`
- **Features**: Clan formation, fund pooling, star regiments

### 3. Reddit Community Integration
- **Location**: `backend/app/services/reddit_service.py`
- **Frontend**: `frontend/src/pages/RedditPage.js`
- **Bots**: Automated sentiment collection and contract generation

### 4. NFT Marketplace
- **Location**: `backend/app/services/nft_service.py`
- **Frontend**: `frontend/src/pages/NFTPage.js`
- **Features**: Prediction NFTs, limited editions, trading

## 📊 Data Flow

```
User Action → Frontend → Backend API → Database/Cache
     ↓
Real-time Updates → WebSocket → Frontend → UI Update
     ↓
Analytics → Elasticsearch → Dashboard → Insights
```

## 🔐 Security Features

- **Authentication**: JWT tokens with refresh mechanism
- **Authorization**: Role-based access control
- **Rate Limiting**: API rate limiting per user
- **Input Validation**: Pydantic schemas for all inputs
- **SQL Injection Protection**: Parameterized queries
- **XSS Protection**: React's built-in XSS protection

## 📱 Mobile Responsiveness

- **Design**: Mobile-first responsive design
- **Framework**: React Native ready (future expansion)
- **Components**: Responsive grid layouts
- **Touch**: Touch-friendly trading interface

## 🧪 Testing Strategy

- **Backend**: pytest with async support
- **Frontend**: React Testing Library + Jest
- **Integration**: API endpoint testing
- **E2E**: Playwright for full user journey testing

## 🚀 Deployment

### Development
```bash
./start.sh                    # Start all services
docker-compose logs -f        # View logs
docker-compose down           # Stop services
```

### Production
- **Backend**: Deploy to AWS EKS or similar
- **Frontend**: Deploy to CDN (CloudFront)
- **Database**: Managed PostgreSQL (RDS)
- **Cache**: Managed Redis (ElastiCache)
- **Search**: Managed Elasticsearch

## 📈 Performance Optimizations

- **Caching**: Redis for frequently accessed data
- **Database**: Connection pooling and indexing
- **Frontend**: Code splitting and lazy loading
- **Images**: Optimized image loading and caching
- **API**: Pagination and efficient queries

## 🔄 Development Workflow

1. **Setup**: Clone repo and run `./start.sh`
2. **Backend**: Develop in `backend/` with hot reload
3. **Frontend**: Develop in `frontend/` with hot reload
4. **Database**: Use `init.sql` for sample data
5. **Testing**: Run tests before committing
6. **Deploy**: Use Docker Compose for staging

## 🌟 Future Enhancements

- **Mobile App**: React Native mobile application
- **AI Integration**: Machine learning for price predictions
- **Blockchain**: Real NFT marketplace on blockchain
- **Social Features**: User profiles and social trading
- **Gamification**: Leaderboards and achievements
- **Internationalization**: Support for more languages

This structure provides a solid foundation for building and scaling CineStox into a comprehensive movie trading platform. 