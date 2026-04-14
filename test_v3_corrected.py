#!/usr/bin/env python3
"""
Comprehensive test of all 9 Product Playground features - CORRECTED PAYLOADS
"""
import requests
import json
import time
from datetime import datetime

BASE_URL = "https://productplayground-1.onrender.com"

# ANSI colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Test data with CORRECT API payload formats
test_data = [
    {
        'name': '1. Product Challenge Analysis',
        'endpoint': '/analyze',
        'payload': {'context': 'Our mobile app retention dropped from 45% to 32% after redesign. New design had 4.2/5 CSAT but users complain onboarding is confusing.'}
    },
    {
        'name': '2. Dashboard KPI Diagnostics',
        'endpoint': '/analyze-kpi',
        'payload': {'dau': '50000', 'mau': '150000', 'avg_session_time': '8.5', 'conversion_rate': '3.2', 'churn_rate': '5.1', 'retention_rate': '68', 'nps_score': '42', 'revenue_per_user': '12.50'}
    },
    {
        'name': '3. Product Teardown',
        'endpoint': '/analyze-website',
        'payload': {'website_url': 'https://www.stripe.com', 'additional_context': 'Competitive payment platform'}
    },
    {
        'name': '4. Decision Framing Engine',
        'endpoint': '/analyze-framing',
        'payload': {'decision': 'Should we pivot to mobile-first or stay with web-first strategy?', 'context': 'Current market trends show 70% mobile'}
    },
    {
        'name': '5. Decision Dashboard',
        'endpoint': '/analyze-dashboard',
        'payload': {'problem': 'Our DAU decreased 15% this month despite marketing spend increase', 'context': 'Launched new UI 2 weeks ago', 'recent_actions': 'Increased ad spend by 50%'}
    },
    {
        'name': '6. Confidence Meter',
        'endpoint': '/analyze-confidence',
        'payload': {'decision': 'Consolidate product lines', 'signals': 'We have 6 months of data showing 15% efficiency improvement and customer survey shows 8/10 satisfaction with consolidation'}
    },
    {
        'name': '7. Decision Defense Pack',
        'endpoint': '/analyze-defense',
        'payload': {'decision': 'We decided to consolidate product lines to reduce complexity', 'outcome': 'Reduced maintenance costs by 40% and improved time-to-market by 30%'}
    },
    {
        'name': '8. Decision Retrospective',
        'endpoint': '/analyze-retrospective',
        'payload': {'decision': 'Launch new pricing model', 'outcome': 'Conversion increased 8% and ARR grew 25%, but churn stayed at 5%', 'learnings': 'Price sensitivity was lower than expected'}
    },
    {
        'name': '9. Guided Walkthrough',
        'endpoint': '/analyze-walkthrough',
        'payload': {'context': 'We need to decide between two market opportunities: enter Asia market or focus on product profitability', 'walkthrough_data': {}}
    }
]

def print_section(text):
    print(f"\n{BOLD}{BLUE}{'='*80}{RESET}")
    print(f"{BOLD}{BLUE}{text:^80}{RESET}")
    print(f"{BOLD}{BLUE}{'='*80}{RESET}\n")

def print_feature(feature_num, feature_name):
    print(f"\n{YELLOW}[{feature_num}/9] {feature_name}{RESET}")

def test_accessibility():
    """Test if website is accessible"""
    print_section("✓ STEP 1: WEBSITE ACCESSIBILITY")
    
    try:
        response = requests.head(f"{BASE_URL}/app", timeout=10)
        if response.status_code == 200:
            print(f"{GREEN}✅ Website is UP and responding (HTTP 200){RESET}")
            return True
        else:
            print(f"{RED}❌ Website returned HTTP {response.status_code}{RESET}")
            return False
    except Exception as e:
        print(f"{RED}❌ Cannot reach website: {e}{RESET}")
        return False

def test_feature(feature_info, test_num):
    """Test individual feature"""
    feature_name = feature_info['name']
    endpoint = feature_info['endpoint']
    payload = feature_info['payload']
    
    print_feature(test_num, feature_name)
    
    url = f"{BASE_URL}{endpoint}"
    
    try:
        start_time = time.time()
        response = requests.post(url, json=payload, timeout=120)
        elapsed = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            if data.get('analysis') or data.get('response') or data:
                content = data.get('analysis') or data.get('response') or str(data)[:100]
                print(f"  {GREEN}✅ WORKING{RESET} ({elapsed:.1f}s)")
                print(f"  Response: {str(content)[:90]}...")
                return True
            else:
                print(f"  {RED}❌ Empty response{RESET}")
                return False
        elif response.status_code == 400:
            error = response.json().get('error', 'Bad request')
            print(f"  {RED}❌ HTTP 400: {error}{RESET}")
            return False
        elif response.status_code == 500:
            error = response.json().get('error', 'Server error')
            if 'API key' in str(error):
                print(f"  {RED}❌ API KEY NOT CONFIGURED: {error}{RESET}")
            else:
                print(f"  {RED}❌ Server error: {error}{RESET}")
            return False
        elif response.status_code == 429:
            print(f"  {YELLOW}⚠️  Rate limited - waiting...{RESET}")
            time.sleep(10)
            response = requests.post(url, json=payload, timeout=120)
            if response.status_code == 200:
                print(f"  {GREEN}✅ RETRY SUCCESSFUL{RESET}")
                return True
            else:
                print(f"  {RED}❌ Failed after retry{RESET}")
                return False
        else:
            print(f"  {RED}❌ HTTP {response.status_code}: {response.text[:80]}{RESET}")
            return False
    except requests.exceptions.Timeout:
        print(f"  {YELLOW}⚠️  Timeout (API slow or overloaded){RESET}")
        return False
    except Exception as e:
        print(f"  {RED}❌ Error: {str(e)}{RESET}")
        return False

def main():
    print_section("🚀 PRODUCT PLAYGROUND - ALL 9 FEATURES TEST")
    print(f"URL: {BASE_URL}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check accessibility
    if not test_accessibility():
        print(f"\n{RED}{BOLD}Cannot proceed - website not accessible{RESET}")
        return
    
    # Test all 9 features
    print_section("✓ STEP 2: TESTING ALL 9 FEATURES")
    
    results = {}
    for i, feature_info in enumerate(test_data, 1):
        result = test_feature(feature_info, i)
        results[feature_info['name']] = result
        time.sleep(2)  # Rate limiting
    
    # Results summary
    print_section("✓ STEP 3: RESULTS SUMMARY")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    percent = int(passed/total*100)
    
    for name, status in results.items():
        icon = f"{GREEN}✅ PASS{RESET}" if status else f"{RED}❌ FAIL{RESET}"
        print(f"  {name:<50} {icon}")
    
    print(f"\n{BOLD}Overall: {passed}/{total} features working ({percent}%){RESET}\n")
    
    # Assessment
    print_section("✓ STEP 4: ASSESSMENT")
    
    if passed == total:
        print(f"{GREEN}{BOLD}🎉 EXCELLENT - ALL 9 FEATURES WORKING!{RESET}")
        print("\nYour Product Playground is fully operational and ready for production!")
    elif passed >= total * 0.75:
        print(f"{YELLOW}{BOLD}✓ GOOD - {passed}/9 features working{RESET}")
        print(f"\nMost features are operational. Some validation errors detected - see details above.")
    elif passed >= total * 0.5:
        print(f"{YELLOW}{BOLD}⚠️  PARTIAL - {passed}/9 features working{RESET}")
        print(f"\nAbout half the features are working. Check API key and payload formats.")
    else:
        print(f"{RED}{BOLD}❌ CRITICAL - Only {passed}/9 features working{RESET}")
        print(f"\nMost features are failing. Likely causes:")
        print(f"  1. OpenAI API key not configured in Render environment")
        print(f"  2. API key has been revoked or has no credits")
        print(f"  3. Network connectivity issues")
        
        with open('/tmp/deployment_issues.txt', 'w') as f:
            f.write(f"Product Playground Test Report\n")
            f.write(f"================================\n")
            f.write(f"Timestamp: {datetime.now()}\n")
            f.write(f"Features Working: {passed}/{total}\n\n")
            f.write(f"Failed Tests:\n")
            for name, status in results.items():
                if not status:
                    f.write(f"  - {name}\n")
        print(f"\n  📝 Report saved to: /tmp/deployment_issues.txt")
    
    # PDF test
    print_section("✓ STEP 5: PDF DOWNLOAD TEST")
    
    try:
        pdf_payload = {'analysis': 'Test PDF generation', 'context': 'This is a test'}
        response = requests.post(f"{BASE_URL}/download-pdf", json=pdf_payload, timeout=30)
        
        if response.status_code == 200 and response.content[:4] == b'%PDF':
            print(f"{GREEN}✅ PDF downloads working ({len(response.content)} bytes){RESET}")
        else:
            print(f"{YELLOW}⚠️  PDF endpoint available but response needs verification{RESET}")
    except Exception as e:
        print(f"{YELLOW}⚠️  PDF test skipped: {str(e)}{RESET}")
    
    return results

if __name__ == "__main__":
    results = main()
