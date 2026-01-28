# 🚀 Product Thinking Studio

A professional, AI-powered suite for Product Managers to structure their thinking, analyze complex decisions, and gain strategic clarity. Built with Flask and GPT-4o.

## ✨ Features

### 🎯 Core Decision Support Tools

- **Challenge the Challenge**: Reframe problems to uncover the real issues beneath the symptoms
- **KPI Diagnostics**: Deep dive into dashboard metrics with root cause analysis and actionable insights
- **Product Teardown**: Comprehensive product & market analysis from any website URL
- **Problem Framing**: Structure complex situations with clear constraints, stakeholders, and contexts
- **Dashboard Analysis**: Transform raw metrics into strategic insights with trend analysis

### 🛡️ Risk & Validation Tools

- **Confidence Builder**: Evaluate decision confidence with structured validation frameworks
- **Defensive Strategy**: Anticipate criticism and build bulletproof defense for your proposals
- **Product Retrospective**: Learn from shipped features with structured post-mortem analysis
- **Walkthrough Mode**: Step-by-step guided analysis for complex strategic decisions

### 💎 Professional Output

- **📥 PDF Export**: Download professional, beautifully formatted analysis reports with color-coded sections
- **⚡ Real-time Analysis**: Get instant, comprehensive insights powered by GPT-4o
- **🎨 Modern UI**: Clean dark theme with glassmorphism effects and smooth animations
- **📱 Mobile Responsive**: Works seamlessly on desktop, tablet, and mobile devices

## 🎨 Design Philosophy

- **Modern Glassmorphism**: Dark theme (#1a1d2e background) with translucent glass-morphic cards
- **Professional Typography**: SF Pro Display for headings, Inter for body text
- **Smooth Animations**: Thoughtful micro-interactions, hover effects, and loading states
- **Gradient Accents**: Purple-blue gradient branding (#6366f1 → #8b5cf6)
- **Responsive Layout**: Fluid design optimized for all screen sizes
- **Accessibility First**: High contrast ratios, clear visual hierarchy, keyboard navigation

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key (GPT-4o access)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/anubhav-product/ProductPlayGround.git
   cd ProductPlayGround/product-thinking-studio
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**
   
   Option A: Use the setup script
   ```bash
   ./setup-api-key.sh
   ```
   
   Option B: Set environment variable directly
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
   
   Option C: Create `.env` file
   ```bash
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```

4. **Run the application**
   ```bash
   python flask_app.py
   ```
   
   Or use the run script:
   ```bash
   ./run.sh
   ```

5. **Open in browser**
   ```
   Navigate to http://127.0.0.1:5000
   ```

## 📁 Project Structure

```
product-thinking-studio/
├── flask_app.py        # Main Flask application & PDF generation
├── app/
│   ├── app.py          # Core application orchestration
│   ├── prompt.py       # AI engine & business logic (ALL LOGIC HERE)
│   └── ui.py           # UI components & templates
├── templates/
│   └── index.html      # Main single-page application
├── docs/
│   ├── product-decisions.md     # Document your decisions
│   ├── PRODUCT-TEARDOWN.md      # Feature documentation
│   └── ui-ux-features.md        # UI/UX guidelines
├── requirements.txt    # Python dependencies
├── run.sh             # Quick start script
└── setup-api-key.sh   # API key configuration helper
```

## 🎯 How to Use

### 1️⃣ Challenge the Challenge
Enter a product situation or problem statement. The tool will:
- Reframe your problem from multiple angles
- Identify hidden assumptions
- Surface alternative problem statements
- Recommend the most valuable framing

### 2️⃣ KPI Diagnostics
Describe your dashboard metrics and context. Get:
- Root cause analysis of metric movements
- Second-order effects and hidden impacts
- Data validation recommendations
- Actionable next steps

### 3️⃣ Product Teardown
Enter any website URL (e.g., swiggy.com, notion.so). Receive:
- Deep product strategy analysis
- Business model assessment
- Competitive positioning insights
- Market dynamics evaluation
- Strategic risks and opportunities

### 4️⃣ Additional Tools
- **Problem Framing**: Structure complex situations
- **Dashboard Analysis**: Transform metrics into insights
- **Confidence Builder**: Validate decision confidence
- **Defensive Strategy**: Prepare for stakeholder challenges
- **Retrospective**: Learn from shipped features
- **Walkthrough**: Step-by-step guided analysis

## 💡 Example Use Cases

### Engagement Drop Investigation
```
Our user engagement dropped 15% after launching the new AI-powered 
recommendation feature. Legal raised explainability concerns during 
the rollout. Engineering team is at 90% capacity with upcoming 
compliance work. How should we proceed?
```

### Feature Prioritization Dilemma
```
We have three competing initiatives: improving onboarding flow, 
adding enterprise SSO, and building a mobile app. Sales wants SSO, 
users want mobile, and metrics show onboarding needs work. Q2 capacity 
allows for only one major initiative.
```

### Product Teardown Analysis
```
URL: https://www.notion.so
Context: Analyzing Notion's product strategy, pricing model, 
and competitive moat for inspiration on our own workspace tool.
```

### Dashboard Deep Dive
```
DAU dropped 8% week-over-week. MAU is flat. Session duration increased 
by 12%. New feature adoption is at 23%. Mobile crashes up 15%. 
What's really happening?
```

## 🛠 Technology Stack

- **Backend**: Flask 3.0 (Python web framework)
- **AI Engine**: OpenAI GPT-4o with optimized prompts
- **PDF Generation**: ReportLab with custom styling
- **Frontend**: Vanilla JavaScript with modern ES6+
- **Styling**: Custom CSS with animations and glassmorphism
- **Fonts**: SF Pro Display, Inter (Google Fonts)

## 📊 Analysis Framework

Each tool provides structured analysis across multiple dimensions:

### Challenge the Challenge
1. **Alternative Framings** - Different ways to view the problem
2. **Hidden Assumptions** - What you might be taking for granted
3. **Stakeholder Lenses** - How different groups see this
4. **Recommended Framing** - Most valuable problem statement

### Product Teardown
1. **Product Overview** - Core functionality and value prop
2. **Business Model** - Revenue streams and unit economics
3. **Market Position** - Competitive landscape analysis
4. **Strategy Assessment** - Strengths, weaknesses, opportunities
5. **Risk Analysis** - Threats and vulnerabilities
6. **Key Insights** - Strategic takeaways

### KPI Diagnostics
1. **Metric Breakdown** - What each number actually means
2. **Root Cause Hypotheses** - Potential drivers of changes
3. **Correlation Analysis** - How metrics relate to each other
4. **Validation Steps** - How to test your hypotheses
5. **Action Items** - What to do next

## 🔐 Environment Variables

```bash
# Required
OPENAI_API_KEY=your-openai-api-key-here

# Optional (with defaults)
FLASK_ENV=development
FLASK_DEBUG=1
```

## 🚀 Deployment

### Render.com (Recommended)
1. Fork this repository
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Set environment variable: `OPENAI_API_KEY`
5. Deploy! (uses `render.yaml` configuration)

See [RENDER-DEPLOY.md](RENDER-DEPLOY.md) for detailed instructions.

### PythonAnywhere
See [PYTHONANYWHERE-DEPLOY.md](PYTHONANYWHERE-DEPLOY.md) for deployment guide.

## 🎨 UI/UX Features

- **Glassmorphism Cards**: Translucent cards with backdrop blur
- **Gradient Branding**: Purple-blue gradient (#6366f1 → #8b5cf6)
- **Smooth Animations**: Fade-ins, slide-ups, hover transitions
- **Loading States**: Elegant spinners with progress indicators
- **Custom Scrollbars**: Styled to match dark theme
- **Tab Navigation**: Smooth transitions between 9 analysis tools
- **PDF Downloads**: Professional formatted reports with color coding
- **Mobile Responsive**: Fluid layout adapts to all screen sizes
- **Toast Notifications**: Non-intrusive success/error messages

## 🤝 Contributing

Contributions are welcome! This is a product thinking playground. Feel free to:

- **Add new analysis frameworks** - Create new tabs for different PM scenarios
- **Enhance AI prompts** - Improve the quality of generated insights
- **Improve UI/UX** - Make the interface more beautiful and intuitive
- **Add features** - PDF customization, collaborative features, saved analyses
- **Fix bugs** - Report issues or submit pull requests

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

MIT License - feel free to use this for your product work!

## 🌟 Pro Tips

- **Be Specific**: Include metrics, constraints, and stakeholder perspectives for better analysis
- **Add Context**: The more context you provide, the deeper and more actionable the insights
- **Use Multiple Tools**: Different tools reveal different angles on the same problem
- **Download PDFs**: Save your analyses for reference and stakeholder sharing
- **Iterate**: Run multiple analyses as you gather more information
- **Document**: Keep your insights in `docs/product-decisions.md` for future reference

## 🐛 Troubleshooting

### Common Issues

**Server Error (502/504)**
- Check your OpenAI API key is set correctly
- Verify you have GPT-4o access on your OpenAI account
- Wait a moment and try again (temporary API overload)

**Empty or Short Responses**
- Provide more context in your input
- Check your API rate limits
- Try again with a simpler query

**PDF Download Issues**
- Ensure analysis completed successfully before downloading
- Check browser console for errors
- Try a different browser if issues persist

**Installation Issues**
```bash
# Clean install
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 📚 Additional Documentation

- [Product Decisions Log](docs/product-decisions.md) - Track your product decisions
- [Product Teardown Guide](docs/PRODUCT-TEARDOWN.md) - How to use teardown feature
- [UI/UX Features](docs/ui-ux-features.md) - Design system documentation
- [API Key Setup](docs/API-KEY-SETUP.md) - Detailed API configuration guide

---

**Built with ❤️ for Product Managers who think deeply about their craft.**

*Powered by OpenAI GPT-4o • Flask 3.0 • Modern CSS*
