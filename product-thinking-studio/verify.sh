#!/bin/bash

# Quick verification script for Product Thinking Studio

echo "🔍 VERIFYING PROJECT SETUP..."
echo ""

# Check Python version
echo "1. Checking Python version..."
python3 --version
echo ""

# Check if requirements.txt exists
echo "2. Checking dependencies file..."
if [ -f "requirements.txt" ]; then
    echo "✅ requirements.txt found"
    cat requirements.txt
else
    echo "❌ requirements.txt not found"
fi
echo ""

# Check project structure
echo "3. Checking project structure..."
tree -L 2 -I 'venv|__pycache__|*.pyc' 2>/dev/null || find . -maxdepth 2 -type f -o -type d | grep -v venv | grep -v __pycache__
echo ""

# Check if .env.example exists
echo "4. Checking environment template..."
if [ -f ".env.example" ]; then
    echo "✅ .env.example found"
else
    echo "❌ .env.example not found"
fi
echo ""

# Count Python files
echo "5. Counting Python files..."
echo "   App files: $(find app -name "*.py" 2>/dev/null | wc -l)"
echo "   Total .py files: $(find . -name "*.py" -not -path "*/venv/*" 2>/dev/null | wc -l)"
echo ""

# Check documentation
echo "6. Checking documentation..."
for doc in README.md PROJECT-SUMMARY.md docs/ui-ux-features.md docs/product-decisions.md; do
    if [ -f "$doc" ]; then
        echo "   ✅ $doc"
    else
        echo "   ❌ $doc"
    fi
done
echo ""

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  VERIFICATION COMPLETE                                       ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "📋 NEXT STEPS:"
echo "   1. cp .env.example .env"
echo "   2. Add your OPENAI_API_KEY to .env"
echo "   3. Run: ./run.sh"
echo ""
echo "💡 TIP: Read PROJECT-SUMMARY.md for complete overview"
echo ""
