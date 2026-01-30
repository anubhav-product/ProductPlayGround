#!/bin/bash
# Simple PDF download test using curl

echo "=============================================="
echo "PDF Download Functionality Test"
echo "=============================================="
echo ""

# Test 1: Basic PDF generation
echo "Test 1: Basic PDF Generation"
echo "------------------------------"
curl -s -X POST http://localhost:5000/download-pdf \
  -H "Content-Type: application/json" \
  -d '{
    "analysis": "## Product Analysis Report\n\n### Summary\nThis is a test analysis.\n\n### Findings\n- Finding 1\n- Finding 2\n\n### Recommendations\n1. Recommendation 1\n2. Recommendation 2",
    "context": "Test context",
    "timestamp": "20260128_120000"
  }' \
  -o /tmp/test_basic.pdf \
  -w "HTTP Status: %{http_code}, Size: %{size_download} bytes\n"

if [ -f "/tmp/test_basic.pdf" ]; then
    echo "✅ PDF created: $(ls -lh /tmp/test_basic.pdf | awk '{print $5}')"
    file /tmp/test_basic.pdf | grep -q "PDF" && echo "✅ Valid PDF format" || echo "❌ Invalid PDF format"
else
    echo "❌ PDF not created"
fi

echo ""
echo "=============================================="
echo "Summary: Check /tmp/test_basic.pdf"
echo "=============================================="
