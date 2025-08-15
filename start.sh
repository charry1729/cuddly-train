#!/bin/bash

# CineStox Startup Script
# This script will start the entire CineStox platform

echo "🎬 Starting CineStox: The Movie Stock Market..."
echo "================================================"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

# Check if Docker Compose is available
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose and try again."
    exit 1
fi

echo "🐳 Starting services with Docker Compose..."

# Start all services
docker-compose up -d

echo "⏳ Waiting for services to be ready..."

# Wait for services to be healthy
echo "📊 Waiting for PostgreSQL..."
until docker-compose exec -T postgres pg_isready -U cinestox > /dev/null 2>&1; do
    sleep 2
done

echo "🔴 Waiting for Redis..."
until docker-compose exec -T redis redis-cli ping > /dev/null 2>&1; do
    sleep 2
done

echo "🔍 Waiting for Elasticsearch..."
until curl -s http://localhost:9200/_cluster/health > /dev/null 2>&1; do
    sleep 2
done

echo "🐍 Waiting for Backend..."
until curl -s http://localhost:8000/health > /dev/null 2>&1; do
    sleep 2
done

echo "⚛️  Waiting for Frontend..."
until curl -s http://localhost:3000 > /dev/null 2>&1; do
    sleep 2
done

echo ""
echo "🎉 CineStox is now running!"
echo "================================================"
echo "🌐 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo "🗄️  Database: localhost:5432 (cinestox/cinestox)"
echo "🔴 Redis: localhost:6379"
echo "🔍 Elasticsearch: http://localhost:9200"
echo ""
echo "📱 You can now open http://localhost:3000 in your browser"
echo ""
echo "🛑 To stop all services, run: docker-compose down"
echo "📊 To view logs, run: docker-compose logs -f"
echo "🧹 To clean up everything, run: docker-compose down -v"
echo ""
echo "Happy trading! 🚀📈" 