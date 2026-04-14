#!/usr/bin/env python3
"""
Comprehensive test of all 9 Product Playground features
Tests each feature's actual API endpoint and PDF download capability
"""
import requests
import json
import time
from datetime import datetime

BASE_URL = "https://productplayground-1.onrender.com"

# ANSI colors for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Test data for each feature - Updated with ACTUAL endpoints
test_data = [
    {
        'name': '1. Product Challenge Analysis',
        'endpoint': '/analyze',
        'payload': {'text': 'Our mobile app retention dropped from 45% to 32% (D7) after we redesigned the onboarding flow. The new design tested well in user research though.'}
    },
    {
        'name': '2. Dashboard KPI Diagnostics',
        'endpoint': '/analyze-kpi',
        'payload': {'metric': 'DAU', 'current': '50000', 'previous': '55000', 'context': 'Monthly engagement metrics'}
    },
    {
        'name': '3. Product Teardown',
        'endpoint': '/analyze-website',
        'payload': {'url': 'https://www.airbnb.com', 'product_name': 'Airbnb'}
    },
    {
        'name': '4. Decision Framing Engine',
        'endpoint': '/analyze-framing',
        'payload': {'decision': 'Should we pivot to mobile-first or stay with web-first strategy?', 'context': 'Current market trends'}
    },
    {
        'name': '5. Decision Dashboard',
        'endpoint': '/analyze-dashboard',
        'payload': {'situation': 'Launch new feature or focus on tech debt?', 'context': 'We are 2 months behind schedule'}
    },
    {
        'name': '6. Confidence Meter',
        'endpoint': '/analyze-confidence',
        'payload': {'signals': 'We have 3 months of A/B test data showing 15% improvement in conversion rate'}
    },
    {
        'name': '7. Decision Defense Pack',
        'endpoint': '/analyze-defense',
        'payload': {'decision': 'We decided to consolidate product lines to reduce complexity', 'outcome': 'Reduced maintenance costs by 40%'}
    },
    {
        'name': '8. Decision Retrospective',
        'endpoint': '/analyze-retrospective',
        'payload': {'decision': 'Launch new pricing model', 'outcome': 'Conversion increased 8% but churn stayed the same'}
    },
    {
        'name': '9. Guided Walkthrough',
        'endpoint': '/analyze-walkthrough',
        'payload': {'challenge': 'We need to decide between two market opportunities', 'context': 'Both have strong demand signals'}
    }
]

def print_header(text):
    print(f"\n{BOLD}{BLUE}{'='*80}{RESET}")
    print(f"{BOLD}{BLUE}{text:^80}{RESET}")
    print(f"{BOLD}{BLUE}{'='*80}{RESET}\n")

def test_website_accessibility():
    """Test if the website is accessible"""
    print_header("STEP 1: Website Accessibility Check")
    
    try:
        response = requests.head(f"{BASE_URL}/app", timeout=10)
        if response.status_code == 200:
            print(f"{GREEN}✅ Website is accessible (HTTP 200){RESET}")
            return True
        else:
            print(f"{RED}❌ Website returned status {response.status_code}{RESET}")
            return False
    except Exception as e:
        print(f"{RED}❌ Cannot reach website: {e}{RESET}")
        return False

def test_feature_endpoint(feature_info):
    """Test individual feature API endpoint"""
    feature_name = feature_info['name']
    endpoint = feature_info['endpoint']
    payload = feature_info['payload']
    
    print(f"\n{YELLOW}Testing: {feature_name}{RESET}")
    
    url = f"{BASE_URL}{endpoint}"
    
    try:
        start_time = time.time()
        response = requests.post(url, json=payload, timeout=120)
        elapsed = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            
            # Check if we got a response with content
            response_text = str(data)
            if len(response_text) > 50:
                analysis = data.get('analysis') or data.get('response') or data.get('result') or response_text
                print(f"  {GREEN}✅ Working ({elapsed:.1f}s) - Response: {str(analysis)[:80]}...{RESET}")
                return True
            else:
                print(f"  {RED}❌ Empty response{RESET}")
                return False
        elif response.status_code == 401 or response.status_code == 403:
            print(f"  {RED}❌ Authentication issue (HTTP {response.status_code}) - API key may not be configured{RESET}")
            print(f"     Response: {response.text[:100]}")
            return False
        elif response.status_code == 429:
            print(f"  {YELLOW}⚠️  Rate limited (HTTP 429) - Trying again...{RESET}")
            time.sleep(5)
            try:
                response = requests.post(url, json=payload, timeout=120)
                if response.status_code == 200:
                    print(f"  {GREEN}✅ Working (after retry){RESET}")
                    return True
            except:
                pass
            return False
        else:
            print(f"  {RED}❌ HTTP {response.status_code}: {response.text[:100]}{RESET}")
            return False
    except requests.exceptions.Timeout:
        print(f"  {YELLOW}⚠️  Request timeout (120s) - Server may be slow or overloaded{RESET}")
        return False
    except Exception as e:
        print(f"  {RED}❌ Error: {str(e)}{RESET}")
        return False

def test_pdf_download(feature_info):
    """Test PDF download for a feature"""
    feature_name = feature_info['name']
    endpoint = feature_info['endpoint']
    payload = feature_info['payload']
    
    print(f"\n{YELLOW}PDF: {feature_name}{RESET}")
    
    try:
        # PrependAnalysis data to payload for PDF generation
        pdf_payload = payload.copy()
        pdf_payload['analysis'] = 'Test analysis for PDF generation'
        
        url = f"{BASE_URL}/download-pdf"
        
        response = requests.post(url, json=pdf_payload, timeout=60)
        
        if response.status_code == 200:
            # Check if it's a PDF (should have PDF header)
            if response.content[:4] == b'%PDF':
                print(f"  {GREEN}✅ PDF generated ({len(response.content)} bytes){RESET}")
                return True
            else:
                print(f"  {YELLOW}⚠️  Response received but not PDF format ({len(response.content)} bytes){RESET}")
                return False
        elif response.status_code == 401 or response.status_code == 403:
            print(f"  {YELLOW}⚠️  PDF generation requires API configuration{RESET}")
            return False
        else:
            print(f"  {RED}❌ HTTP {response.status_code}{RESET}")
            return False
            
    except Exception as e:
        print(f"  {RED}❌ Error: {str(e)}{RESET}")
        return False

def main():
    print_header("🚀 PRODUCT PLAYGROUND - COMPREHENSIVE FEATURE TEST")
    print(f"Testing URL: {BASE_URL}") 
    print(f"Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Step 1: Check website accessibility
    if not test_website_accessibility():
        print(f"\n{RED}{BOLD}Cannot proceed - website is not accessible{RESET}")
        return
    
    # Step 2: Test all 9 features
    print_header("STEP 2: Testing All 9 Features")
    
    feature_results = {}
    for feature_info in test_data:
        result = test_feature_endpoint(feature_info)
        feature_results[feature_info['name']] = result
        time.sleep(2)  # Rate limiting between requests
    
    # Step 3: Summary
    print_header("STEP 3: Feature Test Summary")
    
    passed = sum(1 for v in feature_results.values() if v)
    total = len(feature_results)
    
    print(f"\n{BOLD}Results:{RESET}\n")
    for feature, status in feature_results.items():
        status_str = f"{GREEN}✅ PASS{RESET}" if status else f"{RED}❌ FAIL{RESET}"
        print(f"  {feature:<45} {status_str}")
    
    print(f"\n{BOLD}Summary: {passed}/{total} features working ({int(passed/total*100)}%){RESET}")
    
    if passed == total:
        print(f"\n{GREEN}{BOLD}🎉 ALL 9 FEATURES WORKING!{RESET}")
    elif passed >= total * 0.7:
        print(f"\n{YELLOW}{BOLD}⚠️  Most features working ({int(passed/total*100)}%){RESET}")
    elif passed == 0:
        print(f"\n{RED}{BOLD}❌ NO FEATURES WORKING - Likely missing API key or configuration{RESET}")
        print(f"\n{YELLOW}ISSUE: The application needs OPENAI_API_KEY environment variable configured{RESET}")
    else:
        print(f"\n{RED}{BOLD}❌ Issues detected ({int(passed/total*100)}% working){RESET}")
    
    # Step 4: File download tests
    print_header("STEP 4: PDF Download Tests")
    
    pdf_results = {}
    for feature_info in test_data[:3]:  # Test first 3
        result = test_pdf_download(feature_info)
        pdf_results[feature_info['name']] = result
        time.sleep(1)
    
    pdf_passed = sum(1 for v in pdf_results.values() if v)
    print(f"\n{BOLD}PDF Tests: {pdf_passed}/{len(pdf_results)}{RESET}")
    
    # Final recommendation
    print_header("STEP 5: Diagnosis & Recommendations")
    
    if passed == 0:
        print(f"""
{RED}{BOLD}🔴 CRITICAL: API Key Not Configured{RESET}

The deployment at https://productplayground-1.onrender.com is missing the
OpenAI API key. This prevents all AI features from working.

{BOLD}TO FIX:{RESET}
1. Go to https://render.com/dashboard
2. Select the 'product-playground' service
3. Go to Environment tab
4. Add: OPENAI_API_KEY = (your key from https://platform.openai.com/api-keys)
5. Click Deploy to redeploy with the key

{BOLD}Alternatively, for local testing:{RESET}
- Create a .env file with OPENAI_API_KEY=your-key
- Run: python3 product-thinking-studio/flask_app.py
        """)
    elif passed < total:
        print(f"""
{YELLOW}{BOLD}⚠️  Partial Issues Found{RESET}

{passed} out of {total} features are working. This could indicate:
- Rate limiting from OpenAI API
- Some endpoints may need specific configuration
- Check the error messages above for details
        """)
    else:
        print(f"""
{GREEN}{BOLD}✅ All Features Working!{RESET}

Your Product Playground deployment is fully functional.
All 9 features are responding correctly to API requests.
        """)

if __name__ == "__main__":
    main()
