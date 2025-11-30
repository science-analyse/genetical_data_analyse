#!/bin/bash

# Gene Expression Classifier - Startup Script

set -e

echo "=================================="
echo "Gene Expression Cancer Classifier"
echo "=================================="
echo ""

# Check if models directory exists
if [ ! -d "models" ] || [ -z "$(ls -A models)" ]; then
    echo "⚠️  Warning: Models directory is empty or doesn't exist!"
    echo ""
    echo "Please run the analysis notebook first to train models:"
    echo "  1. pip install -r notebooks/analyse_requirements.txt"
    echo "  2. jupyter notebook notebooks/analyse.ipynb"
    echo "  3. Run all cells in the notebook"
    echo ""
    read -p "Do you want to continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed!"
    echo "Please install Docker from: https://docs.docker.com/get-docker/"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed!"
    echo "Please install Docker Compose from: https://docs.docker.com/compose/install/"
    exit 1
fi

echo "✅ Docker is installed"
echo ""

# Build and start the application
echo "🔨 Building Docker image..."
docker-compose build

echo ""
echo "🚀 Starting application..."
docker-compose up -d

echo ""
echo "⏳ Waiting for application to start..."
sleep 5

# Check if container is running
if docker-compose ps | grep -q "Up"; then
    echo ""
    echo "✅ Application started successfully!"
    echo ""
    echo "🌐 Access the application at:"
    echo "   http://localhost:8000"
    echo ""
    echo "📚 API Documentation:"
    echo "   http://localhost:8000/docs"
    echo ""
    echo "📊 View logs:"
    echo "   docker-compose logs -f"
    echo ""
    echo "🛑 Stop application:"
    echo "   docker-compose down"
    echo ""
else
    echo ""
    echo "❌ Failed to start application!"
    echo "Check logs with: docker-compose logs"
    exit 1
fi
