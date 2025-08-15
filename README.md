# 🎬 CineStox: The Movie Stock Market

*Where Film Fandom Meets Strategic Trading*

## 🚀 Project Overview

CineStox is a cross-platform application enabling users to trade virtual "stocks" of movies, leveraging **Telugu fan culture**, **Reddit communities**, and **hype-driven events** to create a viral skill-based trading experience.

## ✨ Core Features

### 🔥 Hype-Driven Viral Mechanics
- **Trailer Reaction Gambits**: Bet on trailer metrics, mint NFTs for accurate predictions
- **Box Office Battle Royale**: Weekend competitions with hourly liquidations
- **Meme-Powered Trading**: Auto-generate shareable "Stonk Memes"

### 🪖 Telugu Fan Army Ecosystem
- **Star Regiment Clans**: Join factions, pool funds, real-world perks
- **Mass Event Integration**: FDFS Frenzy, Sankranthi Box Office Wars
- **Regional UX**: Telugu voice commands, Astrology-based predictions

### 🤝 Reddit Community Integration
- **r/Tollywood Elite Program**: Verified trader flairs, sentiment index
- **r/Ne_Bonda Chaos Engine**: Convert shitposts to tradable contracts
- **Subreddit vs. Subreddit**: Quarterly prediction battles

## 🏗️ Architecture

```
CineStox/
├── frontend/                 # React web app + React Native mobile
├── backend/                  # FastAPI Python backend
├── trading-engine/           # Real-time trading system
├── telugu-nlp/              # Telugu language processing
├── reddit-integration/      # Reddit bots and APIs
├── nft-marketplace/         # NFT creation and trading
├── analytics/               # Hype trend analysis
└── docs/                   # API documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+
- PostgreSQL 13+
- Redis 6+
- Docker & Docker Compose

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

### Database Setup
```bash
docker-compose up -d postgres redis
cd backend
alembic upgrade head
```

## 🔧 Environment Variables

Create `.env` files in respective directories:

```bash
# Backend
DATABASE_URL=postgresql://user:password@localhost/cinestox
REDIS_URL=redis://localhost:6379
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
TMDB_API_KEY=your_tmdb_api_key
```

## 📱 Features Roadmap

### Phase 1: MVP (3 Months) ✅
- [x] Web app foundation
- [x] Basic trading engine
- [x] User authentication
- [ ] Telugu voice trading
- [ ] 5 movie contracts
- [ ] r/tollywood data bot
- [ ] Fan Army clans

### Phase 2: Virality Expansion (6 Months)
- [ ] Mobile app
- [ ] Meme generator
- [ ] FDFS hype zones
- [ ] ne_bonda contract engine
- [ ] Sankranthi 2024 Battle Event

### Phase 3: Ecosystem (12 Months)
- [ ] NFT marketplace
- [ ] Theater QR partnerships
- [ ] Celebrity integrations
- [ ] User-generated contests

## 🎯 Success Metrics

| KPI | Target |
|-----|--------|
| MAU (Telugu users) | 500,000 (Year 1) |
| Clan Participation | 70% of users |
| Avg. Daily Trades | 5 per user |
| Reddit Conversion | 20% of subs |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎭 Made with ❤️ for Telugu Cinema

*"Make fan wars profitable."* # cuddly-train
