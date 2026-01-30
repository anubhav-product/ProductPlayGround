"""
Web scraping module using Playwright for dynamic content extraction
"""

import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import json
from typing import Dict, Optional

class WebScraper:
    """Advanced web scraper using Playwright for JS-heavy sites"""
    
    def __init__(self):
        self.browser = None
        self.context = None
        
    async def initialize(self):
        """Initialize Playwright browser"""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.context = await self.browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        
    async def close(self):
        """Clean up resources"""
        if self.context:
            await self.context.close()
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
            
    async def scrape_website(self, url: str) -> Dict:
        """
        Scrape a website and extract comprehensive information
        
        Args:
            url: The website URL to scrape
            
        Returns:
            Dictionary containing scraped data
        """
        try:
            if not self.browser:
                await self.initialize()
                
            page = await self.context.new_page()
            
            # Navigate and wait for content
            await page.goto(url, wait_until='networkidle', timeout=30000)
            
            # Extract comprehensive page data
            data = {
                'url': url,
                'title': await page.title(),
                'meta_description': await self._get_meta_description(page),
                'headings': await self._get_headings(page),
                'main_content': await self._get_main_content(page),
                'navigation': await self._get_navigation(page),
                'call_to_actions': await self._get_ctas(page),
                'pricing_signals': await self._get_pricing_info(page),
                'features_mentioned': await self._get_features(page),
                'technology_stack': await self._detect_technology(page),
                'page_structure': await self._analyze_structure(page),
                'social_proof': await self._get_social_proof(page),
                'contact_info': await self._get_contact_info(page)
            }
            
            await page.close()
            return data
            
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            raise
            
    async def _get_meta_description(self, page) -> str:
        """Extract meta description"""
        try:
            return await page.locator('meta[name="description"]').get_attribute('content') or ""
        except:
            return ""
            
    async def _get_headings(self, page) -> Dict:
        """Extract all headings (H1-H3)"""
        headings = {
            'h1': [],
            'h2': [],
            'h3': []
        }
        
        for level in ['h1', 'h2', 'h3']:
            try:
                elements = await page.locator(level).all()
                for elem in elements:
                    text = await elem.inner_text()
                    if text.strip():
                        headings[level].append(text.strip())
            except:
                pass
                
        return headings
        
    async def _get_main_content(self, page) -> str:
        """Extract main content text"""
        try:
            # Try common content selectors
            selectors = ['main', 'article', '[role="main"]', '#content', '.content']
            
            for selector in selectors:
                try:
                    content = await page.locator(selector).first.inner_text()
                    if content and len(content) > 100:
                        return content[:5000]  # Limit to 5000 chars
                except:
                    continue
                    
            # Fallback to body
            return await page.locator('body').inner_text()
        except:
            return ""
            
    async def _get_navigation(self, page) -> list:
        """Extract navigation menu items"""
        nav_items = []
        try:
            nav_links = await page.locator('nav a, header a').all()
            for link in nav_links[:20]:  # Limit to 20 links
                text = await link.inner_text()
                if text.strip():
                    nav_items.append(text.strip())
        except:
            pass
        return nav_items
        
    async def _get_ctas(self, page) -> list:
        """Extract call-to-action buttons"""
        ctas = []
        try:
            # Look for buttons and prominent links
            buttons = await page.locator('button, a.btn, a.button, [role="button"]').all()
            for btn in buttons[:15]:
                text = await btn.inner_text()
                if text.strip():
                    ctas.append(text.strip())
        except:
            pass
        return ctas
        
    async def _get_pricing_info(self, page) -> Dict:
        """Detect pricing information"""
        pricing = {
            'has_pricing_page': False,
            'pricing_tiers': [],
            'pricing_signals': []
        }
        
        try:
            content = await page.content()
            content_lower = content.lower()
            
            # Check for pricing page
            if 'pricing' in content_lower or 'plans' in content_lower:
                pricing['has_pricing_page'] = True
                
            # Look for price indicators
            price_elements = await page.locator('text=/\\$\\d+|€\\d+|£\\d+/').all()
            for elem in price_elements[:10]:
                text = await elem.inner_text()
                pricing['pricing_signals'].append(text.strip())
                
            # Look for tier names
            tier_keywords = ['free', 'pro', 'premium', 'enterprise', 'basic', 'starter', 'business']
            for keyword in tier_keywords:
                if keyword in content_lower:
                    pricing['pricing_tiers'].append(keyword)
                    
        except:
            pass
            
        return pricing
        
    async def _get_features(self, page) -> list:
        """Extract mentioned features"""
        features = []
        try:
            # Look for feature sections
            feature_elements = await page.locator('.feature, .features li, [class*="feature"]').all()
            for elem in feature_elements[:20]:
                text = await elem.inner_text()
                if text.strip() and len(text) < 200:
                    features.append(text.strip())
        except:
            pass
        return features
        
    async def _detect_technology(self, page) -> Dict:
        """Detect technology stack from page source"""
        tech = {
            'frameworks': [],
            'libraries': [],
            'analytics': []
        }
        
        try:
            content = await page.content()
            
            # Check for common frameworks
            if 'react' in content.lower():
                tech['frameworks'].append('React')
            if 'vue' in content.lower():
                tech['frameworks'].append('Vue.js')
            if 'angular' in content.lower():
                tech['frameworks'].append('Angular')
            if 'next' in content.lower():
                tech['frameworks'].append('Next.js')
                
            # Check for analytics
            if 'google-analytics' in content or 'gtag' in content:
                tech['analytics'].append('Google Analytics')
            if 'mixpanel' in content:
                tech['analytics'].append('Mixpanel')
            if 'segment' in content:
                tech['analytics'].append('Segment')
                
        except:
            pass
            
        return tech
        
    async def _analyze_structure(self, page) -> Dict:
        """Analyze page structure"""
        structure = {
            'has_hero': False,
            'has_footer': False,
            'has_navigation': False,
            'sections_count': 0
        }
        
        try:
            # Check for hero section
            hero_selectors = ['.hero', '[class*="hero"]', '.banner', '#hero']
            for selector in hero_selectors:
                if await page.locator(selector).count() > 0:
                    structure['has_hero'] = True
                    break
                    
            # Check for footer
            structure['has_footer'] = await page.locator('footer').count() > 0
            
            # Check for navigation
            structure['has_navigation'] = await page.locator('nav').count() > 0
            
            # Count sections
            structure['sections_count'] = await page.locator('section').count()
            
        except:
            pass
            
        return structure
        
    async def _get_social_proof(self, page) -> Dict:
        """Extract social proof elements"""
        social_proof = {
            'testimonials': [],
            'customer_logos': False,
            'stats': []
        }
        
        try:
            # Look for testimonials
            testimonial_elements = await page.locator('.testimonial, [class*="testimonial"], .review').all()
            for elem in testimonial_elements[:5]:
                text = await elem.inner_text()
                if text.strip():
                    social_proof['testimonials'].append(text.strip()[:200])
                    
            # Check for customer logos
            logo_sections = await page.locator('.customers, .clients, [class*="logo"]').count()
            social_proof['customer_logos'] = logo_sections > 0
            
            # Look for stats/numbers
            stat_patterns = await page.locator('text=/\\d+[KM]?\\+?\\s*(users|customers|companies)/i').all()
            for stat in stat_patterns[:5]:
                text = await stat.inner_text()
                social_proof['stats'].append(text.strip())
                
        except:
            pass
            
        return social_proof
        
    async def _get_contact_info(self, page) -> Dict:
        """Extract contact information"""
        contact = {
            'email': None,
            'social_links': []
        }
        
        try:
            content = await page.content()
            
            # Look for email
            import re
            email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', content)
            if email_match:
                contact['email'] = email_match.group(0)
                
            # Look for social media links
            social_domains = ['twitter.com', 'linkedin.com', 'facebook.com', 'instagram.com', 'github.com']
            for domain in social_domains:
                if domain in content:
                    contact['social_links'].append(domain.replace('.com', ''))
                    
        except:
            pass
            
        return contact


def scrape_website_sync(url: str) -> Dict:
    """Synchronous wrapper for async scraping"""
    async def run():
        scraper = WebScraper()
        try:
            data = await scraper.scrape_website(url)
            return data
        finally:
            await scraper.close()
    
    return asyncio.run(run())
