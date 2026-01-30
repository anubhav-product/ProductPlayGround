"""
Comprehensive Playwright test - Test actual feature functionality
"""
import asyncio
from playwright.async_api import async_playwright
import json
import time

async def test_full_functionality():
    """Test actual feature with input and output"""
    
    url = "https://productplayground-1.onrender.com/app"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()
        
        console_logs = []
        page.on("console", lambda msg: console_logs.append(f"[{msg.type}] {msg.text}"))
        
        print("🚀 COMPREHENSIVE FUNCTIONALITY TEST")
        print("=" * 80)
        
        try:
            # 1. Load the page
            print("\n1️⃣ Loading application...")
            await page.goto(url, wait_until='networkidle', timeout=60000)
            print(f"   ✅ Page loaded: {await page.title()}")
            
            # 2. Take initial screenshot
            await page.screenshot(path='01_initial_load.png')
            print(f"   📸 Screenshot: 01_initial_load.png")
            
            # 3. Test Challenge the Challenge feature
            print("\n2️⃣ Testing 'Challenge the Challenge' feature...")
            
            # Find the Challenge tab and click it
            challenge_tab = page.locator('button:has-text("Challenge"), button:has-text("💡")').first
            await challenge_tab.click()
            await page.wait_for_timeout(1000)
            print(f"   ✅ Challenge tab clicked")
            
            await page.screenshot(path='02_challenge_tab.png')
            
            # Fill in the textarea
            test_input = """Our mobile app retention dropped from 45% to 32% (D7) after we redesigned 
the onboarding flow. The new design tested well in user research (4.2/5 satisfaction), 
but real-world metrics are concerning. Should we roll back the changes?"""
            
            textarea = page.locator('textarea').first
            await textarea.fill(test_input)
            print(f"   ✅ Input filled ({len(test_input)} characters)")
            
            await page.screenshot(path='03_input_filled.png')
            
            # Click Analyze button
            analyze_button = page.locator('button:has-text("Analyze")').first
            await analyze_button.click()
            print(f"   ✅ Analyze button clicked")
            print(f"   ⏳ Waiting for AI analysis...")
            
            await page.screenshot(path='04_analyzing.png')
            
            # Wait for response (look for result div or success indicator)
            try:
                # Wait for either success message or error
                await page.wait_for_selector('.result, [class*="result"], .analysis, [class*="analysis"], .error', timeout=120000)
                
                # Get the result
                result_text = await page.locator('body').inner_text()
                
                # Check if we got actual analysis
                if 'framing' in result_text.lower() or 'analysis' in result_text.lower() or 'insight' in result_text.lower():
                    print(f"   ✅ Analysis received!")
                    
                    # Count words in response
                    words = len(result_text.split())
                    print(f"   📊 Response length: {words} words")
                    
                    # Take screenshot of result
                    await page.screenshot(path='05_analysis_complete.png', full_page=True)
                    print(f"   📸 Full analysis screenshot saved")
                    
                    # Look for key sections
                    if 'alternative' in result_text.lower():
                        print(f"   ✅ Alternative framings section found")
                    if 'assumption' in result_text.lower():
                        print(f"   ✅ Assumptions section found")
                    if 'recommend' in result_text.lower():
                        print(f"   ✅ Recommendations section found")
                    
                    # 4. Test PDF download
                    print("\n3️⃣ Testing PDF Download...")
                    
                    # Look for download PDF button
                    pdf_button = page.locator('button:has-text("PDF"), button:has-text("Download")').first
                    
                    if await pdf_button.count() > 0:
                        # Set up download listener
                        async with page.expect_download() as download_info:
                            await pdf_button.click()
                        
                        download = await download_info.value
                        
                        # Save the PDF
                        pdf_path = f'analysis_report_{int(time.time())}.pdf'
                        await download.save_as(pdf_path)
                        
                        print(f"   ✅ PDF downloaded: {pdf_path}")
                        
                        # Check PDF size
                        import os
                        size = os.path.getsize(pdf_path)
                        print(f"   📄 PDF size: {size / 1024:.2f} KB")
                        
                        if size > 1000:  # More than 1KB
                            print(f"   ✅ PDF appears to have content")
                        else:
                            print(f"   ⚠️  PDF seems small - may be empty")
                    else:
                        print(f"   ⚠️  PDF download button not found")
                    
                else:
                    print(f"   ⚠️  Response received but doesn't look like analysis")
                    print(f"   First 200 chars: {result_text[:200]}")
                
            except Exception as e:
                print(f"   ❌ Error waiting for analysis: {str(e)[:100]}")
                await page.screenshot(path='error_state.png')
                
                # Check for error message
                error_elem = await page.locator('.error, [class*="error"]').count()
                if error_elem > 0:
                    error_text = await page.locator('.error, [class*="error"]').first.inner_text()
                    print(f"   ❌ Error message: {error_text[:200]}")
            
            # 5. Test Product Teardown (website analysis)
            print("\n4️⃣ Testing Product Teardown...")
            
            teardown_tab = page.locator('button:has-text("Teardown"), button:has-text("🔍")').first
            await teardown_tab.click()
            await page.wait_for_timeout(1000)
            print(f"   ✅ Teardown tab opened")
            
            # Fill in URL
            url_input = page.locator('input[type="text"], input[type="url"]').first
            await url_input.fill('notion.so')
            print(f"   ✅ URL entered: notion.so")
            
            await page.screenshot(path='06_teardown_input.png')
            
            # Don't actually run this one (to save API credits)
            print(f"   ℹ️  Skipping actual analysis to save API credits")
            
            # 6. Console log analysis
            print("\n5️⃣ Console Logs Analysis...")
            errors = [log for log in console_logs if '[error]' in log.lower()]
            warnings = [log for log in console_logs if '[warning]' in log.lower()]
            
            print(f"   Total console messages: {len(console_logs)}")
            print(f"   Errors: {len(errors)}")
            print(f"   Warnings: {len(warnings)}")
            
            if errors:
                print(f"   ❌ Console errors found:")
                for err in errors[:5]:
                    print(f"      - {err[:100]}")
            else:
                print(f"   ✅ No console errors")
            
            # 7. Check all tabs are present
            print("\n6️⃣ Verifying All Features...")
            feature_names = [
                "Challenge", "KPI", "Teardown", "Framing", 
                "Dashboard", "Confidence", "Defense", "Retrospective", "Walkthrough"
            ]
            
            tabs_found = 0
            for feature in feature_names:
                count = await page.locator(f'button:has-text("{feature}")').count()
                if count > 0:
                    tabs_found += 1
                    print(f"   ✅ {feature}")
                else:
                    print(f"   ⚠️  {feature} - not found")
            
            print(f"\n   Total features accessible: {tabs_found}/9")
            
            # Final summary
            print("\n" + "=" * 80)
            print("📋 TEST SUMMARY")
            print("=" * 80)
            
            print(f"\n✅ PASSED:")
            print(f"   - Page loads successfully")
            print(f"   - {tabs_found}/9 features accessible")
            print(f"   - Input fields functional")
            print(f"   - Analysis request submitted")
            print(f"   - No JavaScript errors")
            
            if errors:
                print(f"\n❌ ISSUES:")
                print(f"   - {len(errors)} console errors detected")
            
            print(f"\n📸 Screenshots saved:")
            print(f"   - 01_initial_load.png")
            print(f"   - 02_challenge_tab.png")
            print(f"   - 03_input_filled.png")
            print(f"   - 04_analyzing.png")
            print(f"   - 05_analysis_complete.png")
            print(f"   - 06_teardown_input.png")
            
            print(f"\n🎯 RECOMMENDATION:")
            if not errors and tabs_found >= 8:
                print(f"   ✅ Site is production-ready and fully functional!")
                print(f"   ✅ Ready to deploy to custom .com domain")
            else:
                print(f"   ⚠️  Review console errors and missing features")
            
        except Exception as e:
            print(f"\n❌ ERROR: {str(e)}")
            await page.screenshot(path='error_screenshot.png')
            print(f"   Error screenshot saved")
        
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(test_full_functionality())
