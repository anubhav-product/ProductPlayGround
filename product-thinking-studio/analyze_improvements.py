#!/usr/bin/env python3
"""Playwright Site Analyzer"""
import asyncio, json
from playwright.async_api import async_playwright
from datetime import datetime

async def main():
    url = "https://productplayground-1.onrender.com/app"
    print(f"🔍 Analyzing {url}\n")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        # Load
        start = asyncio.get_event_loop().time()
        await page.goto(url, timeout=60000)
        try:
            await page.wait_for_selector('.tab-button, .container', timeout=30000)
        except:
            pass
        load_time = asyncio.get_event_loop().time() - start
        
        # Analyze
        title = await page.title()
        tabs = len(await page.query_selector_all('.tab-button'))
        h1s = len(await page.query_selector_all('h1'))
        
        print(f"✓ Load: {load_time:.2f}s")
        print(f"✓ Title: {title}")
        print(f"✓ Tabs: {tabs}")
        print(f"✓ H1s: {h1s}\n")
        
        # Screenshot
        await page.screenshot(path='analysis.png', full_page=True)
        print(f"📸 Screenshot: analysis.png")
        
        await browser.close()
        
        # Recommendations
        print("\n" + "="*60)
        print("💡 TOP IMPROVEMENTS FOR .COM")
        print("="*60)
        
        recs = {
            "Performance": ["Minify CSS/JS", "Enable gzip", "Add CDN"],
            "SEO": ["Meta description", "Sitemap.xml", "Schema.org"],
            "UX": ["Loading spinners", "Toast notifications", "Char counters"],
            "Mobile": ["Responsive design", "Touch targets 44px+", "Test devices"],
            "Production": ["Error tracking (Sentry)", "Rate limiting", "Monitoring"],
            "Analytics": ["Google Analytics", "Track feature usage", "Funnels"],
            "Security": ["CORS headers", "CSP policy", "Hide errors"],
            "Content": ["FAQ section", "Tutorials", "Example outputs"]
        }
        
        for i, (cat, items) in enumerate(recs.items(), 1):
            print(f"\n{i}. {cat}")
            for item in items:
                print(f"   • {item}")
        
        print("\n" + "="*60)
        print("✅ Analysis complete!")
        print("="*60)

if __name__ == '__main__':
    asyncio.run(main())
