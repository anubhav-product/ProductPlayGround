#!/usr/bin/env python3
"""
Playwright Site Analyzer - Deep analysis of Product Playground
Analyzes UX, performance, accessibility, and suggests improvements
"""

import asyncio
import json
from playwright.async_api import async_playwright
from datetime import datetime

async def analyze_site():
    """Comprehensive site analysis with improvement suggestions"""
    
    url = "https://productplayground-1.onrender.com/app"
    
    print("🔍 PLAYWRIGHT SITE ANALYSIS - Product Playground")
    print("=" * 80)
    print(f"Target: {url}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'
        )
        
        page = await context.new_page()
        
        # Collect metrics
        metrics = {
            'performance': {},
            'accessibility': {},
            'ux_issues': [],
            'improvements': [],
            'seo': {},
            'mobile': {}
        }
        
        # Track console messages
        console_logs = []
        errors = []
        warnings = []
        
        page.on('console', lambda msg: console_logs.append({
            'type': msg.type,
            'text': msg.text
        }))
        
        page.on('pageerror', lambda err: errors.append(str(err)))
        
        print("\n📊 PHASE 1: Performance Analysis")
        print("-" * 80)
        
        # Measure page load
        start_time = asyncio.get_event_loop().time()
        await page.goto(url, wait_until='networkidle', timeout=60000)
        
        # Wait for actual content to load (Render can show loading page)
        print("Waiting for page content to load...")
        try:
            await page.wait_for_selector('.container, .tab-button, #app', timeout=30000)
        except:
            print("⚠️  Main content not loaded yet, waiting longer...")
            await asyncio.sleep(10)
        
        load_time = asyncio.get_event_loop().time() - start_time
        
        print(f"✓ Page load time: {load_time:.2f}s")
        metrics['performance']['load_time'] = load_time
        
        if load_time > 3:
            metrics['improvements'].append({
                'category': 'Performance',
                'priority': 'HIGH',
                'issue': f'Page load time is {load_time:.2f}s (should be <3s)',
                'suggestion': 'Consider: 1) Minify CSS/JS, 2) Lazy load images, 3) Use CDN for static assets'
            })
        
        # Check page size
        title = await page.title()
        print(f"✓ Page title: {title}")
        metrics['seo']['title'] = title
        
        # Analyze DOM
        print("\n📊 PHASE 2: Structure Analysis")
        print("-" * 80)
        
        # Count elements
        tabs = await page.query_selector_all('.tab-button')
        inputs = await page.query_selector_all('input, textarea')
        buttons = await page.query_selector_all('button')
        
        print(f"✓ Tabs found: {len(tabs)}")
        print(f"✓ Input fields: {len(inputs)}")
        print(f"✓ Buttons: {len(buttons)}")
        
        # Check tab labels
        print("\n📋 Tab Analysis:")
        for i, tab in enumerate(tabs[:9]):
            text = await tab.text_content()
            print(f"   {i+1}. {text.strip()}")
            
            # Check if text is clear
            if len(text.strip()) > 25:
                metrics['ux_issues'].append({
                    'element': 'Tab button',
                    'issue': f'Tab label too long: "{text.strip()}"',
                    'suggestion': 'Keep tab labels under 20 characters for better readability'
                })
        
        print("\n📊 PHASE 3: Accessibility Analysis")
        print("-" * 80)
        
        # Check for alt text on images
        images = await page.query_selector_all('img')
        images_without_alt = 0
        for img in images:
            alt = await img.get_attribute('alt')
            if not alt:
                images_without_alt += 1
        
        if images_without_alt > 0:
            print(f"⚠️  {images_without_alt} images missing alt text")
            metrics['improvements'].append({
                'category': 'Accessibility',
                'priority': 'MEDIUM',
                'issue': f'{images_without_alt} images without alt attributes',
                'suggestion': 'Add descriptive alt text to all images for screen readers'
            })
        else:
            print(f"✓ All images have alt text")
        
        # Check for proper heading hierarchy
        h1s = await page.query_selector_all('h1')
        h2s = await page.query_selector_all('h2')
        h3s = await page.query_selector_all('h3')
        
        print(f"✓ Heading structure: H1({len(h1s)}) H2({len(h2s)}) H3({len(h3s)})")
        
        if len(h1s) == 0:
            metrics['improvements'].append({
                'category': 'SEO & Accessibility',
                'priority': 'HIGH',
                'issue': 'No H1 heading found',
                'suggestion': 'Add a main H1 heading for better SEO and accessibility'
            })
        elif len(h1s) > 1:
            metrics['improvements'].append({
                'category': 'SEO & Accessibility',
                'priority': 'MEDIUM',
                'issue': f'{len(h1s)} H1 headings found (should be 1)',
                'suggestion': 'Use only one H1 per page for better SEO'
            })
        
        # Check for form labels
        inputs_without_labels = 0
        for inp in inputs:
            inp_id = await inp.get_attribute('id')
            if inp_id:
                label = await page.query_selector(f'label[for="{inp_id}"]')
                if not label:
                    inputs_without_labels += 1
        
        if inputs_without_labels > 0:
            print(f"⚠️  {inputs_without_labels} inputs missing associated labels")
            metrics['improvements'].append({
                'category': 'Accessibility',
                'priority': 'HIGH',
                'issue': f'{inputs_without_labels} form inputs without labels',
                'suggestion': 'Add <label> elements with for="" attributes for all inputs'
            })
        
        print("\n📊 PHASE 4: Mobile Responsiveness")
        print("-" * 80)
        
        # Test mobile viewport
        await page.set_viewport_size({'width': 375, 'height': 667})  # iPhone SE
        await asyncio.sleep(1)
        
        # Check if elements overflow
        body = await page.query_selector('body')
        scroll_width = await page.evaluate('document.body.scrollWidth')
        client_width = await page.evaluate('document.body.clientWidth')
        
        if scroll_width > client_width:
            print(f"⚠️  Horizontal scroll detected (width: {scroll_width}px > viewport: {client_width}px)")
            metrics['improvements'].append({
                'category': 'Mobile UX',
                'priority': 'HIGH',
                'issue': 'Page requires horizontal scrolling on mobile',
                'suggestion': 'Add responsive CSS with max-width: 100% and proper media queries'
            })
        else:
            print(f"✓ No horizontal scroll on mobile")
        
        # Test tablet viewport
        await page.set_viewport_size({'width': 768, 'height': 1024})  # iPad
        await asyncio.sleep(1)
        print(f"✓ Tested tablet viewport (768x1024)")
        
        # Reset to desktop
        await page.set_viewport_size({'width': 1920, 'height': 1080})
        await asyncio.sleep(1)
        
        print("\n📊 PHASE 5: User Experience Testing")
        print("-" * 80)
        
        # Test tab switching
        print("Testing tab interactions...")
        if len(tabs) == 0:
            print("⚠️  No tabs found - site may not have loaded properly")
            metrics['improvements'].append({
                'category': 'Critical',
                'priority': 'HIGH',
                'issue': 'Site content not loading - shows loading page',
                'suggestion': 'Check if Render service is awake. Free tier may sleep after inactivity.'
            })
        else:
            for i, tab in enumerate(tabs[:3]):  # Test first 3 tabs
            await tab.click()
            await asyncio.sleep(0.5)
            
            # Check if content changes
            active_tab = await page.query_selector('.tab-button.active')
            if active_tab:
                text = await tab.text_co - only if tabs exist
        if len(tabs) > 0:
            print("\nTesting Challenge Statement feature...")
            await tabs[0].click()
            await asyncio.sleep(0.5)
            
            # Find textarea
            textarea = await page.query_selector('textarea')
                    })
        
        # Test first feature (Challenge)
        print("\nTesting Challenge Statement feature...")
        await tabs[0].click()
        await asyncio.sleep(0.5)
        
        # Find textarea
        textarea = await page.query_selector('textarea')
        if textarea:
            await textarea.fill('Test: Quick product challenge for UX analysis')
            print(f"✓ Textarea input working")
            
            # Check character counter
            char_counters = await page.query_selector_all('.char-counter, .character-count, [class*="counter"]')
            if len(char_counters) == 0:
                metrics['improvements'].append({
                    'category': 'UX Enhancement',
                    'priority': 'LOW',
                    'issue': 'No character counter for text inputs',
                    'suggestion': 'Add live character counter to help users meet requirements'
                })
        
        # Check for loading indicators
        print("\nChecking UI feedback mechanisms...")
        loading_indicators = await page.query_selector_all('.loading, .spinner, [class*="loading"]')
        if len(loading_indicators) == 0:
            metrics['improvements'].append({
                'category': 'UX Enhancement',
                'priority': 'MEDIUM',
                'issue': 'No visible loading indicator',
                'suggestion': 'Add spinner/loading animation when AI is processing requests'
            })
        
        print("\n📊 PHASE 6: SEO & Meta Analysis")
        print("-" * 80)
        
        # Check meta tags
        meta_description = await page.query_selector('meta[name="description"]')
        if not meta_description:
            print(f"⚠️  Missing meta description")
            metrics['improvements'].append({
                'category': 'SEO',
                'priority': 'HIGH',
                'issue': 'No meta description tag',
                'suggestion': 'Add: <meta name="description" content="AI-powered PM decision support tool...">'
            })
        else:
            content = await meta_description.get_attribute('content')
            print(f"✓ Meta description: {content[:50]}...")
        
        # Check Open Graph tags
        og_title = await page.query_selector('meta[property="og:title"]')
        og_image = await page.query_selector('meta[property="og:image"]')
        
        if not og_title or not og_image:
            print(f"⚠️  Missing Open Graph tags")
            metrics['improvements'].append({
                'category': 'SEO & Social Sharing',
                'priority': 'MEDIUM',
                'issue': 'Missing Open Graph meta tags',
                'suggestion': 'Add og:title, og:description, og:image for better social media sharing'
            })
        
        print("\n📊 PHASE 7: Console & Error Analysis")
        print("-" * 80)
        
        await asyncio.sleep(2)  # Wait for any async errors
        
        error_msgs = [log for log in console_logs if log['type'] == 'error']
        warning_msgs = [log for log in console_logs if log['type'] == 'warning']
        
        print(f"Console errors: {len(error_msgs)}")
        print(f"Console warnings: {len(warning_msgs)}")
        
        if error_msgs:
            print("\n⚠️  JavaScript Errors:")
            for err in error_msgs[:5]:
                print(f"   - {err['text'][:100]}")
                metrics['improvements'].append({
                    'category': 'Code Quality',
                    'priority': 'HIGH',
                    'issue': f'JavaScript error: {err["text"][:80]}',
                    'suggestion': 'Fix JavaScript errors for better user experience'
                })
        else:
            print("✓ No console errors")
        
        # Take final screenshot
        await page.screenshot(path='analysis_screenshot.png', full_page=True)
        print("\n📸 Screenshot saved: analysis_screenshot.png")
        
        # Generate report
        print("\n" + "=" * 80)
        print("📋 IMPROVEMENT RECOMMENDATIONS")
        print("=" * 80)
        
        # Sort by priority
        priority_order = {'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
        sorted_improvements = sorted(
            metrics['improvements'],
            key=lambda x: priority_order.get(x.get('priority', 'LOW'), 3)
        )
        
        if not sorted_improvements:
            print("\n🎉 Excellent! No critical improvements needed.")
            print("✓ Site is well-structured and functional")
        else:
            for i, imp in enumerate(sorted_improvements, 1):
                print(f"\n{i}. [{imp.get('priority', 'MEDIUM')}] {imp.get('category', 'General')}")
                print(f"   Issue: {imp['issue']}")
                print(f"   💡 Suggestion: {imp['suggestion']}")
        
        print("\n" + "=" * 80)
        print("🎯 TOP PRIORITIES FOR .COM DEPLOYMENT")
        print("=" * 80)
        
        priorities = [
            {
                'title': 'Performance Optimization',
                'items': [
                    'Minify CSS and JavaScript files',
                    'Enable gzip compression on server',
                    'Add caching headers for static assets',
                    'Consider using a CDN (Cloudflare, etc.)'
                ]
            },
            {
                'title': 'SEO Improvements',
                'items': [
                    'Add comprehensive meta description',
                    'Implement Open Graph tags',
                    'Create sitemap.xml',
                    'Add robots.txt',
                    'Set up Google Analytics'
                ]
            },
            {
                'title': 'User Experience',
                'items': [
                    'Add loading spinners for AI requests',
                    'Implement character counters on inputs',
                    'Add success/error toast notifications',
                    'Improve mobile responsiveness',
                    'Add keyboard shortcuts for power users'
                ]
            },
            {
                'title': 'Production Readiness',
                'items': [
                    'Set up error tracking (Sentry)',
                    'Add rate limiting to prevent abuse',
                    'Implement user analytics',
                    'Create monitoring dashboard',
                    'Set up SSL certificate (auto with most hosts)'
                ]
            }
        ]
        
        for priority in priorities:
            print(f"\n📌 {priority['title']}")
            for item in priority['items']:
                print(f"   • {item}")
        
        print("\n" + "=" * 80)
        print("✅ ANALYSIS COMPLETE")
        print("=" * 80)
        print(f"\nTotal improvements suggested: {len(sorted_improvements)}")
        print(f"High priority: {len([x for x in sorted_improvements if x.get('priority') == 'HIGH'])}")
        print(f"Medium priority: {len([x for x in sorted_improvements if x.get('priority') == 'MEDIUM'])}")
        print(f"Low priority: {len([x for x in sorted_improvements if x.get('priority') == 'LOW'])}")
        
        # Save report to JSON
        with open('analysis_report.json', 'w') as f:
            json.dump(metrics, f, indent=2)
        print(f"\n📊 Detailed report saved: analysis_report.json")
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(analyze_site())
