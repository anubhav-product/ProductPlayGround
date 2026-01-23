#!/bin/bash

# Product Thinking Studio - Quick Start Script

echo "🚀 Starting Product Thinking Studio..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -q -r requirements.txt

# Check for .env file
if [ ! -f ".env" ]; then
    echo ""
    echo "⚠️  No .env file found!"
    echo "📝 Please create a .env file with your OPENAI_API_KEY"
    echo "   You can copy .env.example to .env and add your key"
    echo ""
    read -p "Do you want to continue anyway? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Run the application
echo ""
echo "✨ Launching Product Thinking Studio..."
echo "📍 Opening in your browser at http://localhost:8501"
echo ""

streamlit run app/app.py
