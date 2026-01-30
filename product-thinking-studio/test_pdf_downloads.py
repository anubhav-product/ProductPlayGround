#!/usr/bin/env python3
"""
Test script to verify PDF download functionality for all features
"""
import requests
import json
import sys
from datetime import datetime

BASE_URL = "http://localhost:5000"

def test_pdf_generation(feature_name, analysis_type, test_data):
    """Test PDF generation for a specific feature"""
    print(f"\n{'='*60}")
    print(f"Testing: {feature_name}")
    print(f"{'='*60}")
    
    try:
        # Simulate analysis result
        test_analysis = {
            'analysis': f"""## {feature_name} Analysis Report

### Executive Summary
This is a test analysis for {feature_name} feature.

### Key Findings
- Finding 1: Test data processed successfully
- Finding 2: Analysis completed without errors
- Finding 3: PDF generation validated

### Recommendations
1. **Recommendation 1**: Implement test strategy
2. **Recommendation 2**: Monitor performance metrics
3. **Recommendation 3**: Iterate based on feedback

### Next Steps
- Review analysis results
- Share with stakeholders
- Track implementation progress

---

*Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*
""",
            'context': json.dumps(test_data),
            'timestamp': datetime.now().strftime("%Y%m%d_%H%M%S"),
            'type': analysis_type
        }
        
        # Test PDF generation
        print(f"📄 Generating PDF for {feature_name}...")
        response = requests.post(
            f"{BASE_URL}/download-pdf",
            json=test_analysis,
            timeout=30
        )
        
        if response.status_code == 200:
            # Save PDF to verify it's valid
            filename = f"test_{feature_name.replace(' ', '_').lower()}_{test_analysis['timestamp']}.pdf"
            with open(f"/tmp/{filename}", 'wb') as f:
                f.write(response.content)
            
            file_size = len(response.content)
            print(f"✅ SUCCESS: PDF generated ({file_size:,} bytes)")
            print(f"   Saved to: /tmp/{filename}")
            
            # Verify PDF header
            if response.content[:4] == b'%PDF':
                print(f"✅ Valid PDF format confirmed")
            else:
                print(f"⚠️  Warning: File may not be valid PDF")
            
            return True
        else:
            print(f"❌ FAILED: HTTP {response.status_code}")
            print(f"   Response: {response.text[:200]}")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all PDF generation tests"""
    print(f"\n{'#'*60}")
    print(f"# PDF Download Functionality Test Suite")
    print(f"# Testing all features at {BASE_URL}")
    print(f"{'#'*60}")
    
    # Check if server is running
    try:
        response = requests.get(BASE_URL, timeout=5)
        print(f"\n✅ Server is running (HTTP {response.status_code})")
    except Exception as e:
        print(f"\n❌ Server not accessible: {e}")
        print(f"Please start the Flask server first!")
        sys.exit(1)
    
    tests = [
        {
            'name': 'Product Challenge Analysis',
            'type': 'Product Challenge',
            'data': {
                'context': 'Our DAU dropped 15% after launching new onboarding flow.'
            }
        },
        {
            'name': 'Dashboard KPI Diagnostics',
            'type': 'KPI Analysis',
            'data': {
                'dau': 12000,
                'mau': 35000,
                'conversion_rate': 3.2,
                'retention_rate': 38
            }
        },
        {
            'name': 'Product Teardown',
            'type': 'Product Teardown',
            'data': {
                'url': 'https://example.com',
                'context': 'Competitive analysis'
            }
        },
        {
            'name': 'Decision Framing Engine',
            'type': 'Decision Framing',
            'data': {
                'decision': 'Should we build AI search or fix technical debt?',
                'stakeholders': 'Engineering, Product, CEO',
                'options': 'A) AI search, B) Technical debt, C) Both'
            }
        },
        {
            'name': 'Decision Dashboard',
            'type': 'Decision Dashboard',
            'data': {
                'problem': 'Mobile DAU dropped 18% in 3 weeks',
                'data': 'DAU: 45K → 37K, Session time: 8min → 6.2min'
            }
        },
        {
            'name': 'Confidence Meter',
            'type': 'Confidence Assessment',
            'data': {
                'decision': 'Launch new $199/month enterprise tier',
                'evidence': '12 customers requested features, survey shows willingness to pay'
            }
        },
        {
            'name': 'Decision Defense Pack',
            'type': 'Decision Defense Pack',
            'data': {
                'decision': 'Deprecate Android tablet app',
                'rationale': 'Tablets are 2% users but 30% engineering time'
            }
        },
        {
            'name': 'Decision Retrospective',
            'type': 'Decision Retrospective',
            'data': {
                'decision': 'Rebuilt dashboard with React',
                'expected': '8 weeks rebuild, 50% faster development',
                'actual': '14 weeks, improved morale, 1 of 3 features shipped'
            }
        },
        {
            'name': 'Guided Walkthrough',
            'type': 'Walkthrough Analysis',
            'data': {
                'targetUser': 'B2B SaaS product managers',
                'decision': 'Add AI-powered recommendations',
                'constraints': '3 month timeline, 2 engineers'
            }
        }
    ]
    
    # Run all tests
    results = []
    for test in tests:
        result = test_pdf_generation(
            test['name'],
            test['type'],
            test['data']
        )
        results.append({
            'feature': test['name'],
            'passed': result
        })
    
    # Summary
    print(f"\n{'='*60}")
    print(f"TEST SUMMARY")
    print(f"{'='*60}")
    
    passed = sum(1 for r in results if r['passed'])
    total = len(results)
    
    for result in results:
        status = "✅ PASS" if result['passed'] else "❌ FAIL"
        print(f"{status} - {result['feature']}")
    
    print(f"\n{passed}/{total} tests passed ({passed/total*100:.1f}%)")
    
    if passed == total:
        print(f"\n🎉 All PDF generation tests PASSED!")
        return 0
    else:
        print(f"\n⚠️  Some tests FAILED - please review errors above")
        return 1

if __name__ == "__main__":
    sys.exit(main())
