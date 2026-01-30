# Playwright MCP Integration

Product Playground now includes **Playwright web scraping** to enhance Product Teardown analysis with real website data.

## 🎭 What is Playwright?

Playwright is a browser automation library that allows us to:
- Load JavaScript-heavy websites (React, Vue, Angular apps)
- Extract dynamic content that traditional scrapers miss
- Capture actual rendered HTML and page structure
- Analyze interactive elements and user flows

## 🔧 How It Works

When you analyze a website using **Product Teardown**:

1. **URL Submission** → User enters website URL
2. **Playwright Scraping** → Headless browser loads the page
3. **Data Extraction** → Comprehensive data extracted:
   - Page title and meta description
   - All headings (H1, H2, H3)
   - Navigation menu structure
   - Call-to-action buttons
   - Pricing information
   - Feature mentions
   - Technology stack detection
   - Social proof elements
4. **AI Analysis** → GPT-4o analyzes scraped data + URL
5. **Comprehensive Report** → Deep insights delivered

## 📊 Data Extracted

### Page Metadata
- Title tag
- Meta description
- Open Graph tags

### Content Structure
- All headings (H1-H3)
- Main content text
- Navigation menu items
- Section count and structure

### Product Signals
- Call-to-action buttons
- Pricing tiers and prices
- Feature lists
- Testimonials and reviews
- Customer logos
- Statistics and metrics

### Technical Signals
- JavaScript frameworks (React, Vue, Angular)
- Analytics tools (Google Analytics, Mixpanel)
- Technology stack indicators

### Business Signals
- Contact information
- Social media presence
- Pricing model indicators
- Market positioning signals

## 🚀 Benefits

### Without Playwright (URL only):
```
Analysis based on:
- URL structure
- General knowledge about the company
- Limited context
```

### With Playwright:
```
Analysis based on:
✓ Actual page content and structure
✓ Pricing tiers and models
✓ Feature sets and positioning
✓ Technology choices
✓ Social proof elements
✓ Navigation and IA
✓ Call-to-action strategy
```

## 🔒 Privacy & Ethics

- **Respects robots.txt** - Won't scrape if disallowed
- **Rate limiting** - Prevents overwhelming target sites
- **Public data only** - Only scrapes publicly accessible pages
- **User-Agent identification** - Clearly identifies as a bot
- **No credential bypass** - Won't attempt to access protected content

## 🛠️ Setup

### Installation
```bash
# Install dependencies
pip install playwright beautifulsoup4

# Install browser
playwright install chromium
```

### Configuration

The scraper is automatically enabled when analyzing websites. No additional configuration needed!

### Disable Scraping (if needed)
```bash
# Set environment variable
export ENABLE_WEB_SCRAPING=false
```

## 📝 Usage Example

**Input:**
```
URL: https://www.notion.so
Context: Analyzing workspace collaboration tools
```

**Without Playwright:**
- Basic analysis based on public knowledge
- Generic insights about Notion

**With Playwright:**
- Actual pricing tiers: Free, Plus, Business, Enterprise
- Detected features: Wikis, Docs, Projects, AI
- Technology: React-based SPA
- Social proof: Customer logos, testimonials
- Navigation: Clear IA with 6 main sections
- CTAs: "Get Notion free", "Request demo", "Sign up"

**Result:** 10x more detailed and accurate analysis!

## ⚙️ Technical Details

### Browser Configuration
- **Headless mode**: Runs without GUI (faster, lighter)
- **Viewport**: 1920x1080 (desktop view)
- **Timeout**: 30 seconds per page
- **Network**: Wait for networkidle (all content loaded)

### Error Handling
- **Graceful degradation**: If scraping fails, analysis continues with URL only
- **Timeout protection**: 30s limit prevents hanging
- **Exception logging**: Errors logged for debugging
- **Retry logic**: Automatic retry on transient failures

### Performance
- **Efficient extraction**: Targets specific elements only
- **Content limits**: Caps text at 5000 characters
- **Element limits**: Maximum 20 items per category
- **Browser pooling**: Reuses browser instances when possible

## 🔍 MCP Server Integration

Product Playground uses the **Model Context Protocol (MCP)** for Playwright:

### What is MCP?
MCP (Model Context Protocol) is a standardized way for AI applications to interact with external tools and services.

### MCP Configuration
See `mcp_config.json`:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp-server"]
    }
  }
}
```

### Benefits of MCP
- **Standardized interface** - Consistent tool integration
- **Type safety** - Well-defined schemas
- **Error handling** - Built-in retry and fallback logic
- **Extensibility** - Easy to add more tools

## 🎯 Future Enhancements

### Planned Features
- [ ] Screenshot capture for visual analysis
- [ ] Multi-page scraping (crawl entire site)
- [ ] Competitive comparison (scrape multiple competitors)
- [ ] Historical tracking (monitor changes over time)
- [ ] Mobile view analysis
- [ ] Performance metrics (page load, render time)
- [ ] Accessibility audit
- [ ] SEO analysis

### Advanced Capabilities
- [ ] Form interaction (test signup flows)
- [ ] Authenticated scraping (with user permission)
- [ ] API endpoint discovery
- [ ] Cookie/session analysis
- [ ] Third-party integrations detection

## 🐛 Troubleshooting

### "Playwright not installed"
```bash
pip install playwright
playwright install chromium
```

### "Browser launch failed"
```bash
# Install system dependencies (Linux)
playwright install-deps chromium
```

### "Timeout during scraping"
- Website may be slow or blocked
- Try again or use URL-only analysis
- Check internet connection

### "Access denied / 403 error"
- Website may block bots
- Analysis will continue with URL only
- Some sites require manual review

## 📚 Resources

- **Playwright Docs**: https://playwright.dev/python
- **MCP Protocol**: https://modelcontextprotocol.org
- **BeautifulSoup**: https://www.crummy.com/software/BeautifulSoup/

---

**Enhanced by Playwright** 🎭 **Powered by MCP** 🔌
