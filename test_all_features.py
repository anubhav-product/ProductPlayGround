#!/usr/bin/env python3
"""
Comprehensive test of all 9 Product Playground features
Tests each feature's API endpoint and PDF download capability
"""
import requests
import json
import time
from datetime import datetime

BASE_URL = "https://productplayground-1.onrender.com"
APP_URL = f"{BASE_URL}/app"

# ANSI colors for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Test data for each feature
test_data = {
    'challenge': {
        'input': 'Our mobile app retention dropped from 45% to 32% (D7) after we redesigned the onboarding flow.',
        'endpoint': '/api/analyze-challenge',
        'form_field': 'challenge_text'
    },
    'kpi': {
        'input': {'metric': 'DAU', 'current_value': '50000', 'previous_value': '55000', 'context': 'Monthly engagement'},
        'endpoint': '/api/analyze-kpi',
        'form_field': 'kpi_data'
    },
    'teardown': {
        'input': 'https://www.airbnb.com',
        'endpoint': '/api/analyze-product',
        'form_field': 'product_url'
    },
    'decision_frame': {
        'input': 'Should we pivot to mobile-first or stay with web-first strategy?',
        'endpoint': '/api/frame-decision',
        'form_field': 'decision_statement'
    },
    'decision_dashboard': {
        'input': 'Launch new feature or focus on tech debt?',
        'endpoint': '/api/decision-dashboard',
        'form_field': 'situation'
    },
    'confidence': {
        'input': 'We have 3 months of A/B test data showing 15% improvement',
        'endpoint': '/api/confidence-meter',
        'form_field': 'signals'
    },
    'defense_pack': {
        'input': 'We decided to consolidate product lines to reduce complexity',
        'endpoint': '/api/defense-pack',
        'form_field': 'decision'
    },
    'retrospective': {
        'input': 'We launched the new pricing model and conversion increased 8% but churn stayed the same',
        'endpoint': '/api/retrospective',
        'form_field': 'outcome'
    },
    'guided': {
        'input': 'We need to decide between two market opportunities',
        'endpoint': '/api/guided-walkthrough',
        'form_field': 'challenge'
    }
}

def print_header(text):
    print(f"\n{BOLD}{BLUE}{'='*80}{RESET}")
    print(f"{BOLD}{BLUE}{text:^80}{RESET}")
    print(f"{BOLD}{BLUE}{'='*80}{RESET}\n")

def test_website_accessibility():
    """Test if the website is accessible"""
    print_header("STEP 1: Website Accessibility Check")
    
    try:
        response = requests.head(APP_URL, timeout=10)
        if response.status_code == 200:
            print(f"{GREEN}✅ Website is accessible (HTTP 200){RESET}")
            return True
        else:
            print(f"{RED}❌ Website returned status {response.status_code}{RESET}")
            return False
    except Exception as e:
        print(f"{RED}❌ Cannot reach website: {e}{RESET}")
        return False

def test_feature_endpoint(feature_name, feature_display_name, endpoint, test_input):
    """Test individual feature API endpoint"""
    print(f"\n{YELLOW}Testing: {feature_display_name}{RESET}")
    
    url = f"{BASE_URL}{endpoint}"
    
    # Prepare payload based on feature
    if isinstance(test_input, dict):
        payload = test_input
    else:
        # For simple string inputs, find the appropriate field name
        form_field = test_data[feature_name]['form_field']
        payload = {form_field: test_input}
    
    try:
        start_time = time.time()
        response = requests.post(url, json=payload, timeout=60)
        elapsed = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            
            # Check if we got a response with content
            if data.get('analysis') or data.get('response') or data.get('result'):
                content = data.get('analysis') or data.get('response') or data.get('result')
                if len(str(content)) > 50:
                    print(f"  {GREEN}✅ Endpoint working - {elapsed:.1f}s response time{RESET}")
                    print(f"  {GREEN}✅ AI Response: {str(content)[:100]}...{RESET}")
                    return True
                else:
                    print(f"  {RED}❌ Empty response from AI{RESET}")
                    return False
            else:
                print(f"  {RED}❌ Unexpected response format: {str(data)[:100]}{RESET}")
                return False
        else:
            print(f"  {RED}❌ HTTP {response.status_code}: {response.text[:100]}{RESET}")
            return False
    except requests.exceptions.Timeout:
        print(f"  {RED}❌ Request timeout (60s) - API may be slow or overloaded{RESET}")
        return False
    except Exception as e:
        print(f"  {RED}❌ Error: {str(e)}{RESET}")
        return False

def test_pdf_download(feature_name, endpoint):
    """Test PDF download for a feature"""
    print(f"\n{YELLOW}Testing PDF for: {feature_name.upper()}{RESET}")
    
    # First, generate analysis
    test_input = test_data[feature_name]['input']
    form_field = test_data[feature_name]['form_field']
    
    if isinstance(test_input, dict):
        payload = test_input
    else:
        payload = {form_field: test_input}
    
    try:
        # Generate analysis first
        response = requests.post(f"{BASE_URL}{endpoint}", json=payload, timeout=60)
        
        if response.status_code != 200:
            print(f"  {RED}❌ Cannot generate analysis for PDF{RESET}")
            return False
        
        # Try to download PDF
        pdf_endpoint = endpoint.replace('/api/', '/api/download-').replace('/api/analyze-', '/api/download-')
        pdf_url = f"{BASE_URL}{pdf_endpoint}"
        
        # Alternative: try common PDF download patterns
        pdf_patterns = [
            f"{BASE_URL}/download/{feature_name}",
            f"{BASE_URL}/api/export-{feature_name}",
            f"{BASE_URL}/api/{feature_name}-pdf"
        ]
        
        for pdf_url in pdf_patterns:
            try:
                pdf_response = requests.post(pdf_url, json=payload, timeout=30)
                if pdf_response.status_code == 200:
                    if b'PDF' in pdf_response.content[:10]:  # Check PDF header
                        print(f"  {GREEN}✅ PDF generated successfully ({len(pdf_response.content)} bytes){RESET}")
                        return True
            except:
                pass
        
        print(f"  {YELLOW}⚠️  PDF endpoint not found (features may not have PDF export){RESET}")
        return False
        
    except Exception as e:
        print(f"  {RED}❌ PDF test failed: {str(e)}{RESET}")
        return False

def main():
    print_header("🚀 PRODUCT PLAYGROUND - COMPREHENSIVE FEATURE TEST")
    print(f"Testing URL: {APP_URL}")
    print(f"Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Step 1: Check website accessibility
    if not test_website_accessibility():
        print(f"\n{RED}{BOLD}Cannot proceed - website is not accessible{RESET}")
        return
    
    # Step 2: Test all 9 features
    print_header("STEP 2: Testing All 9 Features")
    
    feature_results = {}
    features_order = [
        ('challenge', '1. Product Challenge Analysis'),
        ('kpi', '2. Dashboard KPI Diagnostics'),
        ('teardown', '3. Product Teardown'),
        ('decision_frame', '4. Decision Framing Engine'),
        ('decision_dashboard', '5. Decision Dashboard'),
        ('confidence', '6. Confidence Meter'),
        ('defense_pack', '7. Decision Defense Pack'),
        ('retrospective', '8. Decision Retrospective'),
        ('guided', '9. Guided Walkthrough'),
    ]
    
    for feature_id, feature_display_name in features_order:
        endpoint = test_data[feature_id]['endpoint']
        test_input = test_data[feature_id]['input']
        
        result = test_feature_endpoint(feature_id, feature_display_name, endpoint, test_input)
        feature_results[feature_display_name] = result
        time.sleep(1)  # Rate limiting
    
    # Step 3: Summary
    print_header("STEP 3: Test Summary")
    
    passed = sum(1 for v in feature_results.values() if v)
    total = len(feature_results)
    
    print(f"\n{BOLD}Feature Test Results:{RESET}\n")
    for feature, status in feature_results.items():
        status_str = f"{GREEN}✅ PASS{RESET}" if status else f"{RED}❌ FAIL{RESET}"
        print(f"  {feature:<40} {status_str}")
    
    print(f"\n{BOLD}Summary: {passed}/{total} features working{RESET}")
    
    if passed == total:
        print(f"\n{GREEN}{BOLD}🎉 ALL FEATURES WORKING PERFECTLY!{RESET}")
    elif passed >= total * 0.7:
        print(f"\n{YELLOW}{BOLD}⚠️  Most features working ({int(passed/total*100)}%){RESET}")
    else:
        print(f"\n{RED}{BOLD}❌ ISSUES DETECTED - Less than 70% of features working{RESET}")
    
    # Step 4: File download tests
    print_header("STEP 4: PDF Download Capability")
    print("Note: PDF download testing requires specific implementation\n")
    
    pdf_results = {}
    for feature_id, feature_display_name in features_order[:3]:  # Test first 3
        result = test_pdf_download(feature_display_name, test_data[feature_id]['endpoint'])
        pdf_results[feature_display_name] = result
        time.sleep(0.5)
    
    return feature_results, pdf_results

if __name__ == "__main__":
    main()
