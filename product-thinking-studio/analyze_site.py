#!/usr/bin/env python3
"""
Simple Playwright Analyzer - Analyzes Product Playground and suggests improvements
"""

import asyncio
import json
from playwright.async_api import async_playwright
from datetime import datetime

async def main():
    url = "https://productplayground-1.onrender.com/app"
    
    print("🔍 PLAYWRIGHT ANALYSIS - Product Playground")
    print("=" * 80)
    print(f"URL: {url}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        improvements = []
        
        # Load page
        print("📊 Loading page...")
        start = asyncio.get_event_loop().time()
        await page.goto(url, timeout=60000)
        
        # Wait for actual content
        try:
            await page.wait_for_selector('.container, .tab-button', timeout=30000)
            await asyncio.sleep(2)  # Let JS finish
        except:
            print("⚠️  Content took long to load - might be sleeping service")
        
        load_time = asyncio.get_event_loop().time() - start
        print(f"✓ Load time: {load_time:.2f}s")
        
        if load_time > 5:
            improvements.append(("HIGH", "Performance", 
                f"Slow load time ({load_time:.1f}s)", 
                "Wake Render service or switch to paid tier for instant starts"))
        
        # Check title
        title = await page.title()
        print(f"✓ Title: {title}")
        
        if "loading" in title.lower():
            improvements.append(("HIGH", "Service Issue",
                "Render service may be sleeping",
                "Visit site to wake it up, or upgrade to paid tier"))
        
        # Count elements
        tabs = await page.query_selector_all('.tab-button')
        inputs = await page.query_selector_all('input, textarea')
        buttons = await page.query_selector_all('button')
        
        print(f"\n📋 Page Structure:")
        print(f"   • Tabs: {len(tabs)}")
        print(f"   • Inputs: {len(inputs)}")
        print(f"   • Buttons: {len(buttons)}")
        
        if len(tabs) == 0:
            improvements.append(("HIGH", "Content Loading",
                "No tabs found - page not fully loaded",
                "Check Render logs or redeploy service"))
        
        # Check accessibility
        print(f"\n♿ Accessibility:")
        h1s = await page.query_selector_all('h1')
        print(f"   • H1 headings: {len(h1s)}")
        
        if len(h1s) == 0:
            improvements.append(("MEDIUM", "SEO/A11y",
                "Missing H1 heading",
                "Add <h1> for better SEO and screen readers"))
        
        # Check meta tags
        meta_desc = await page.query_selector('meta[name="description"]')
        og_title = await page.query_selector('meta[property="og:title"]')
        
        if not meta_desc:
            improvements.append(("HIGH", "SEO",
                "No meta description",
                'Add: <meta name="description" content="AI PM tool...">'))
        
        if not og_title:
            improvements.append(("MEDIUM", "Social Sharing",
                "No Open Graph tags",
                'Add og:title, og:description, og:image for sharing'))
        
        # Mobile test
        print(f"\n📱 Mobile Test:")
        await page.set_viewport_size({'width': 375, 'height': 667})
        await asyncio.sleep(1)
        
        scroll_w = await page.evaluate('document.body.scrollWidth')
        client_w = await page.evaluate('document.body.clientWidth')
        
        if scroll_w > client_w + 10:
            print(f"   ⚠️  Horizontal scroll: {scroll_w}px > {client_w}px")
            improvements.append(("HIGH", "Mobile UX",
                "Page requires horizontal scrolling on mobile",
                "Add responsive CSS with max-width: 100%"))
        else:
            print(f"   ✓ No horizontal scroll")
        
        # Reset viewport
        await page.set_viewport_size({'width': 1920, 'height': 1080})
        
        # Console errors
        print(f"\n🐛 Console Check:")
        errors = []
        page.on('console', lambda msg: errors.append(msg) if msg.type == 'error' else None)
        await asyncio.sleep(3)
        
        print(f"   • JS errors: {len([e for e in errors if e.type == 'error'])}")
        
        # Screenshot
        await page.screenshot(path='site_analysis.png', full_page=True)
        print(f"\n📸 Screenshot: site_analysis.png")
        
        await browser.close()
        
        # Print improvements
        print("\n" + "=" * 80)
        print("💡 IMPROVEMENT SUGGESTIONS")
        print("=" * 80)
        
        if not improvements:
            print("\n🎉 No critical issues found! Site looks good.")
        else:
            for priority, category, issue, solution in sorted(improvements):
                print(f"\n[{priority}] {category}")
                print(f"   Issue: {issue}")
                print(f"   Fix: {solution}")
        
        # Top recommendations for .com
        print("\n" + "=" * 80)
        print("🎯 TOP 10 IMPROVEMENTS FOR .COM DEPLOYMENT")
        print("=" * 80)
        
        recommendations = [
            ("Performance", [
                "Minify CSS/JS files (use webpack/rollup)",
                "Enable gzip compression on server",
                "Add service worker for offline support",
                "Lazy load images and heavy components"
            ]),
            ("SEO", [
                "Add comprehensive meta tags (description, keywords)",
                "Create sitemap.xml and robots.txt",
                "Implement structured data (Schema.org)",
                "Set up Google Search Console"
            ]),
            ("User Experience", [
                "Add loading spinners for AI requests (spinner icon)",
                "Implement toast notifications for success/errors",
                "Add character counter on textareas",
                "Create keyboard shortcuts (Ctrl+Enter to submit)"
            ]),
            ("Mobile", [
                "Test on real devices (iPhone, Android)",
                "Improve touch target sizes (min 44x44px)",
                "Add viewport meta tag if missing",
                "Test landscape orientation"
            ]),
            ("Production", [
                "Set up error tracking (Sentry)",
                "Add rate limiting (prevent API abuse)",
                "Implement caching (Redis/Memcached)",
                "Create health check endpoint (/health)"
            ]),
            ("Analytics", [
                "Add Google Analytics or Plausible",
                "Track feature usage by tab",
                "Monitor PDF download rates",
                "Set up conversion funnels"
            ]),
            ("Security", [
                "Add CORS headers properly",
                "Implement CSP (Content Security Policy)",
                "Rate limit API endpoints",
                "Hide error details in production"
            ]),
            ("Branding", [
                "Create custom favicon (16x16, 32x32, 180x180)",
                "Add Apple touch icons",
                "Design custom 404 page",
                "Create branded loading screen"
            ]),
            ("Content", [
                "Add FAQ section",
                "Create tutorial/onboarding flow",
                "Add example outputs for each feature",
                "Write blog posts about PM use cases"
            ]),
            ("Infrastructure", [
                "Set up automated backups",
                "Create staging environment",
                "Implement CI/CD pipeline (GitHub Actions)",
                "Add monitoring (UptimeRobot, StatusCake)"
            ])
        ]
        
        for i, (title, items) in enumerate(recommendations, 1):
            print(f"\n{i}. {title}")
            for item in items:
                print(f"   • {item}")
        
        # Save report
        report = {
            'timestamp': datetime.now().isoformat(),
            'url': url,
            'load_time': load_time,
            'improvements': [
                {'priority': p, 'category': c, 'issue': i, 'solution': s}
                for p, c, i, s in improvements
            ]
        }
        
        with open('improvement_report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print("\n" + "=" * 80)
        print(f"✅ Analysis complete!")
        print(f"📊 Report saved: improvement_report.json")
        print("=" * 80)

if __name__ == '__main__':
    asyncio.run(main())
