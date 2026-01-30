"""
Simpler test using requests library to check the deployed site
"""
import requests
from bs4 import BeautifulSoup
import json

def test_deployed_site():
    """Test deployed site without Playwright"""
    
    url = "https://productplayground-1.onrender.com/"
    
    print(f"🌐 Testing: {url}")
    print("=" * 80)
    
    try:
        # Test main page
        print("\n1️⃣ Testing Landing Page...")
        response = requests.get(url, timeout=30)
        print(f"   Status: {response.status_code}")
        print(f"   Response time: {response.elapsed.total_seconds():.2f}s")
        
        if response.status_code == 200:
            print(f"   ✅ Landing page loads successfully")
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title')
            print(f"   Title: {title.string if title else 'No title'}")
        else:
            print(f"   ❌ Unexpected status code: {response.status_code}")
        
        # Test app page
        print("\n2️⃣ Testing Main App Page...")
        app_response = requests.get(url + "app", timeout=30)
        print(f"   Status: {app_response.status_code}")
        print(f"   Response time: {app_response.elapsed.total_seconds():.2f}s")
        
        if app_response.status_code == 200:
            print(f"   ✅ Main app loads successfully")
            app_soup = BeautifulSoup(app_response.text, 'html.parser')
            
            # Check for key elements
            tabs = app_soup.find_all('button', {'role': 'tab'})
            inputs = app_soup.find_all(['input', 'textarea'])
            buttons = app_soup.find_all('button')
            
            print(f"   Tabs found: {len(tabs)}")
            print(f"   Input fields: {len(inputs)}")
            print(f"   Buttons: {len(buttons)}")
            
            if len(tabs) > 0:
                print(f"   ✅ Interactive tabs detected")
                print(f"   Tab names: {[tab.get_text(strip=True)[:30] for tab in tabs[:5]]}")
            else:
                print(f"   ⚠️  No tabs detected - checking for navigation...")
                nav_links = app_soup.find_all('a', {'class': lambda x: x and 'tab' in x.lower()})
                if nav_links:
                    print(f"   Found {len(nav_links)} navigation links")
        else:
            print(f"   ❌ App page error: {app_response.status_code}")
        
        # Test API health (if exists)
        print("\n3️⃣ Testing API Endpoints...")
        test_endpoints = [
            '/analyze-challenge',
            '/analyze-kpi',
            '/analyze-website',
            '/analyze-framing',
            '/analyze-dashboard',
            '/analyze-confidence',
            '/analyze-defense',
            '/analyze-retrospective',
            '/analyze-walkthrough'
        ]
        
        api_working = []
        api_errors = []
        
        for endpoint in test_endpoints[:3]:  # Test first 3
            try:
                # Just check if endpoint exists (HEAD request)
                test_url = url.rstrip('/') + endpoint
                api_resp = requests.head(test_url, timeout=5)
                if api_resp.status_code in [200, 405]:  # 405 = Method Not Allowed (expects POST)
                    api_working.append(endpoint)
                else:
                    api_errors.append(f"{endpoint}: {api_resp.status_code}")
            except Exception as e:
                api_errors.append(f"{endpoint}: {str(e)[:50]}")
        
        if api_working:
            print(f"   ✅ {len(api_working)} API endpoints responding")
        if api_errors:
            print(f"   ⚠️  Some endpoints had issues:")
            for err in api_errors:
                print(f"      - {err}")
        
        # Check for static resources
        print("\n4️⃣ Checking Page Resources...")
        scripts = app_soup.find_all('script')
        styles = app_soup.find_all('style')
        links = app_soup.find_all('link', {'rel': 'stylesheet'})
        
        print(f"   Inline scripts: {len([s for s in scripts if not s.get('src')])}")
        print(f"   External scripts: {len([s for s in scripts if s.get('src')])}")
        print(f"   Inline styles: {len(styles)}")
        print(f"   External stylesheets: {len(links)}")
        
        # Look for potential JavaScript errors in HTML
        page_text = app_response.text.lower()
        if 'error' in page_text or 'exception' in page_text:
            print(f"   ⚠️  Found 'error' or 'exception' in HTML (may be false positive)")
        
        # Summary
        print(f"\n" + "=" * 80)
        print(f"📋 SUMMARY")
        print(f"=" * 80)
        
        issues = []
        successes = []
        
        if response.status_code == 200:
            successes.append("✅ Landing page loads (HTTP 200)")
        else:
            issues.append(f"❌ Landing page status: {response.status_code}")
        
        if app_response.status_code == 200:
            successes.append("✅ Main app page loads (HTTP 200)")
        else:
            issues.append(f"❌ App page status: {app_response.status_code}")
        
        if len(tabs) > 0:
            successes.append(f"✅ {len(tabs)} interactive tabs found")
        else:
            issues.append("⚠️  No tab elements detected")
        
        if len(inputs) > 0:
            successes.append(f"✅ {len(inputs)} input fields present")
        else:
            issues.append("⚠️  No input fields found")
        
        if response.elapsed.total_seconds() < 5:
            successes.append(f"✅ Fast response time ({response.elapsed.total_seconds():.2f}s)")
        else:
            issues.append(f"⚠️  Slow response time ({response.elapsed.total_seconds():.2f}s)")
        
        print("\n✅ WORKING:")
        for success in successes:
            print(f"   {success}")
        
        if issues:
            print("\n⚠️  POTENTIAL ISSUES:")
            for issue in issues:
                print(f"   {issue}")
        
        # Recommendations
        print(f"\n💡 RECOMMENDATIONS")
        print(f"=" * 80)
        
        if len(tabs) == 0:
            print(f"1. Verify JavaScript is loading correctly")
            print(f"   - Check browser console for errors")
            print(f"   - Ensure all script tags are loading")
        
        if response.elapsed.total_seconds() > 3:
            print(f"2. Consider optimizing page load time")
            print(f"   - Enable gzip compression")
            print(f"   - Minimize JavaScript/CSS")
            print(f"   - Use CDN for static assets")
        
        if not api_working:
            print(f"3. Test API endpoints with actual POST requests")
            print(f"   - Endpoints may require authentication or specific payload")
        
        print(f"\n4. Manual testing recommended:")
        print(f"   - Open {url}app in browser")
        print(f"   - Check browser console (F12) for JavaScript errors")
        print(f"   - Test each feature tab")
        print(f"   - Try submitting a form")
        
        print(f"\n✨ Site appears to be live and accessible!")
        print(f"   Next: Visit in browser and test interactive features")
        
    except requests.exceptions.Timeout:
        print(f"\n❌ ERROR: Request timed out after 30 seconds")
        print(f"   Possible causes:")
        print(f"   - Site is experiencing high load")
        print(f"   - Server is slow to respond")
        print(f"   - Network connectivity issues")
    
    except requests.exceptions.ConnectionError:
        print(f"\n❌ ERROR: Could not connect to site")
        print(f"   Possible causes:")
        print(f"   - Site is down")
        print(f"   - DNS issues")
        print(f"   - Firewall blocking connection")
    
    except Exception as e:
        print(f"\n❌ ERROR: Unexpected error")
        print(f"   {str(e)}")

if __name__ == "__main__":
    test_deployed_site()
