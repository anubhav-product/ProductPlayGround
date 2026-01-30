#!/bin/bash

# Production setup script for Product Playground
# This script prepares the application for production deployment

set -e  # Exit on error

echo "🚀 Product Playground - Production Setup"
echo "========================================"

# Check Python version
echo ""
echo "📦 Checking Python version..."
python3 --version || { echo "❌ Python 3 is required"; exit 1; }

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo ""
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo ""
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Install Playwright browsers
echo ""
echo "🎭 Installing Playwright browsers..."
playwright install chromium

# Check for OpenAI API key
echo ""
echo "🔑 Checking environment configuration..."
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  WARNING: OPENAI_API_KEY not set"
    echo "   Please set it in .env file or environment variables"
    echo "   Example: export OPENAI_API_KEY='your-key-here'"
else
    echo "✅ OPENAI_API_KEY is configured"
fi

# Create necessary directories
echo ""
echo "📁 Creating necessary directories..."
mkdir -p logs
mkdir -p static/downloads

# Set permissions
echo ""
echo "🔒 Setting permissions..."
chmod +x run.sh
chmod +x setup-api-key.sh

# Run verification
echo ""
echo "🧪 Running verification tests..."
python3 verify.sh || echo "⚠️  Some verification tests failed"

# Production checklist
echo ""
echo "✅ Production Checklist:"
echo "========================"
echo ""
echo "Security:"
echo "  ✓ Set OPENAI_API_KEY environment variable"
echo "  ✓ Set SECRET_KEY for Flask sessions"
echo "  ✓ Set FLASK_ENV=production"
echo "  ✓ Enable HTTPS/SSL certificate"
echo "  ✓ Configure CORS_ORIGINS for your domain"
echo ""
echo "Performance:"
echo "  ✓ Use Gunicorn with multiple workers"
echo "  ✓ Set up reverse proxy (Nginx/Apache)"
echo "  ✓ Enable gzip compression"
echo "  ✓ Configure CDN for static files"
echo ""
echo "Monitoring:"
echo "  ✓ Set up error tracking (Sentry)"
echo "  ✓ Configure uptime monitoring"
echo "  ✓ Enable application logging"
echo "  ✓ Set up analytics (optional)"
echo ""
echo "Deployment:"
echo "  ✓ Configure custom domain DNS"
echo "  ✓ Set up SSL certificate"
echo "  ✓ Configure auto-deployment from GitHub"
echo "  ✓ Set up backup strategy"
echo ""

# Display next steps
echo ""
echo "🎯 Next Steps:"
echo "==============="
echo ""
echo "For local development:"
echo "  ./run.sh"
echo ""
echo "For production (Gunicorn):"
echo "  gunicorn --workers 3 --bind 0.0.0.0:8000 flask_app:app"
echo ""
echo "For deployment guides, see:"
echo "  docs/PRODUCTION-DEPLOYMENT.md"
echo ""
echo "✨ Setup complete! Ready to deploy."
