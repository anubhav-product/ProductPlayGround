"""
Test deployed Product Playground site for errors
"""
import asyncio
from playwright.async_api import async_playwright
import json

async def test_deployed_site():
    """Visit deployed site and check for errors"""
    
    url = "https://productplayground-1.onrender.com/app"
    
    console_messages = []
    console_errors = []
    network_errors = []
    page_errors = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'
        )
        page = await context.new_page()
        
        # Capture console messages
        page.on("console", lambda msg: console_messages.append({
            'type': msg.type,
            'text': msg.text
        }))
        
        # Capture page errors
        page.on("pageerror", lambda exc: page_errors.append(str(exc)))
        
        # Capture network failures
        page.on("requestfailed", lambda request: network_errors.append({
            'url': request.url,
            'failure': request.failure
        }))
        
        print(f"🌐 Testing: {url}")
        print("=" * 80)
        
        try:
            # Navigate to the site
            response = await page.goto(url, wait_until='networkidle', timeout=60000)
            
            print(f"\n✅ Page loaded successfully")
            print(f"   Status: {response.status}")
            print(f"   URL: {response.url}")
            
            # Get page title
            title = await page.title()
            print(f"   Title: {title}")
            
            # Check for common elements
            print("\n🔍 Checking page structure...")
            
            # Check for navigation
            nav_count = await page.locator('nav').count()
            print(f"   Navigation elements: {nav_count}")
            
            # Check for main content
            main_count = await page.locator('main, [role="main"]').count()
            print(f"   Main content areas: {main_count}")
            
            # Check for tabs/features
            tab_count = await page.locator('[class*="tab"], .nav-tabs a, button[role="tab"]').count()
            print(f"   Tabs/Features: {tab_count}")
            
            # Check for forms/inputs
            input_count = await page.locator('input, textarea').count()
            print(f"   Input fields: {input_count}")
            
            # Check for buttons
            button_count = await page.locator('button').count()
            print(f"   Buttons: {button_count}")
            
            # Take screenshot
            await page.screenshot(path='deployed_site_screenshot.png', full_page=True)
            print(f"\n📸 Screenshot saved: deployed_site_screenshot.png")
            
            # Wait a bit for any async content
            await page.wait_for_timeout(3000)
            
            # Check console errors
            console_errors = [msg for msg in console_messages if msg['type'] == 'error']
            
            print(f"\n📊 Console Messages:")
            print(f"   Total messages: {len(console_messages)}")
            print(f"   Errors: {len(console_errors)}")
            print(f"   Warnings: {len([m for m in console_messages if m['type'] == 'warning'])}")
            
            if console_errors:
                print(f"\n❌ Console Errors Found:")
                for i, error in enumerate(console_errors[:10], 1):
                    print(f"   {i}. {error['text'][:200]}")
            
            if page_errors:
                print(f"\n❌ Page Errors Found:")
                for i, error in enumerate(page_errors[:10], 1):
                    print(f"   {i}. {error[:200]}")
            
            if network_errors:
                print(f"\n❌ Network Errors Found:")
                for i, error in enumerate(network_errors[:10], 1):
                    print(f"   {i}. {error['url']}")
                    print(f"      Reason: {error['failure']}")
            
            # Test clicking on a tab if available
            print(f"\n🖱️  Testing interactivity...")
            try:
                # Try to find and click first tab
                first_tab = page.locator('button[role="tab"], .nav-tabs a, [class*="tab-"]').first
                if await first_tab.count() > 0:
                    await first_tab.click()
                    await page.wait_for_timeout(1000)
                    print(f"   ✅ Tab click successful")
            except Exception as e:
                print(f"   ⚠️  Tab interaction: {str(e)[:100]}")
            
            # Get page content sample
            body_text = await page.locator('body').inner_text()
            print(f"\n📝 Page Content Sample (first 300 chars):")
            print(f"   {body_text[:300]}...")
            
            # Final assessment
            print(f"\n" + "=" * 80)
            print(f"📋 SUMMARY")
            print(f"=" * 80)
            
            if response.status == 200:
                print(f"✅ Site is loading (HTTP {response.status})")
            else:
                print(f"⚠️  Unexpected status code: {response.status}")
            
            if not console_errors and not page_errors and not network_errors:
                print(f"✅ No JavaScript errors detected")
            else:
                print(f"❌ Errors detected:")
                if console_errors:
                    print(f"   - {len(console_errors)} console errors")
                if page_errors:
                    print(f"   - {len(page_errors)} page errors")
                if network_errors:
                    print(f"   - {len(network_errors)} network errors")
            
            if tab_count > 0:
                print(f"✅ Interactive elements present ({tab_count} tabs)")
            else:
                print(f"⚠️  No tab elements detected")
            
            if input_count > 0:
                print(f"✅ Input fields present ({input_count} fields)")
            else:
                print(f"⚠️  No input fields detected")
            
            # Recommendations
            print(f"\n💡 RECOMMENDATIONS")
            print(f"=" * 80)
            
            if console_errors:
                print(f"1. Fix JavaScript console errors (see list above)")
            
            if network_errors:
                print(f"2. Check failed network requests (API endpoints, resources)")
            
            if response.status != 200:
                print(f"3. Investigate HTTP status code {response.status}")
            
            if tab_count == 0:
                print(f"4. Verify that the single-page app JavaScript is loading correctly")
            
            if 'product' not in title.lower() and 'playground' not in title.lower():
                print(f"5. Consider updating page title for better SEO")
            
        except Exception as e:
            print(f"\n❌ ERROR: Failed to load page")
            print(f"   {str(e)}")
            print(f"\n   Possible causes:")
            print(f"   - Site is down or slow to respond")
            print(f"   - Network connectivity issues")
            print(f"   - Server configuration problems")
            print(f"   - SSL certificate issues")
        
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(test_deployed_site())
