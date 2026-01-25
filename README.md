# Product Playground 🚀

> AI-Powered Product Strategy & Analytics Platform for Product Managers

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-purple.svg)](https://openai.com/)

## Overview

Product Playground is an intelligent decision-support platform designed for product managers and product leaders. Leveraging GPT-4o's advanced reasoning capabilities, it provides strategic analysis for product decisions and diagnostic insights for product metrics.

### Key Features

- **🎯 Product Challenge Analysis**: Get comprehensive strategic recommendations for complex product decisions
- **📊 Dashboard KPI Diagnostics**: Analyze product metrics, identify issues, and receive actionable improvement strategies
- **� Product Teardown**: Conduct structured product and market analysis based on any website URL
- **�📥 PDF Export**: Generate professional analysis reports for stakeholder distribution
- **🎨 Professional Interface**: Clean, sophisticated design optimized for executive audiences
- **⚡ Real-time Analysis**: Instant AI-powered insights using GPT-4o

## Use Cases

### For Product Managers
- Evaluate feature prioritization decisions
- Analyze A/B test results and next steps
- Navigate technical debt vs. new features trade-offs
- Assess competitive positioning strategies
- Conduct competitive product analysis and teardowns

### For Product Leaders
- Review team's strategic proposals with AI-augmented perspective
- Identify red flags in product metrics
- Benchmark KPIs against industry standards
- Prepare data-driven presentations for executives
- Analyze competitor products and market positioning

### For Startups
- Make informed product decisions with limited resources
- Validate product-market fit hypotheses
- Optimize growth metrics efficiently
- Prepare investor-ready product analyses
- Research competitor products and market opportunities

## Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Flask 3.0 (Python) |
| **AI Engine** | OpenAI GPT-4o |
| **PDF Generation** | ReportLab |
| **Frontend** | Vanilla JavaScript, HTML5, CSS3 |
| **Deployment** | PythonAnywhere (WSGI) |
| **Fonts** | Inter (body), Playfair Display (headings) |

## Design Philosophy

The interface employs a refined, professional color palette designed for extended use:

- **Primary**: `#2c3e50` - Sophisticated dark slate
- **Secondary**: `#34495e` - Elegant slate gray  
- **Accent**: `#5d6d7e` - Muted steel blue
- **Background**: `#f8f9fa` - Soft neutral
- **Success**: `#27ae60` - Refined emerald

Typography uses a combination of **Playfair Display** for headings (classical, authoritative) and **Inter** for body text (modern, highly readable).

## Getting Started

### Prerequisites

- Python 3.10 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Git

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/anubhav-product/ProductPlayGround.git
   cd ProductPlayGround/product-thinking-studio
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the `product-thinking-studio` directory:
   ```env
   OPENAI_API_KEY=sk-your-actual-api-key-here
   OPENAI_MODEL=gpt-4o
   TEMPERATURE=0.7
   MAX_TOKENS=4000
   SECRET_KEY=your-secure-random-secret-key
   ```

   **Security Note**: Never commit the `.env` file. It's already in `.gitignore`.

5. **Run the application**
   ```bash
   python flask_app.py
   ```

6. **Access the application**
   
   Open your browser and navigate to: `http://localhost:5000`

## Deployment

### PythonAnywhere (Recommended)

Comprehensive deployment guide available in [`PYTHONANYWHERE-DEPLOY.md`](product-thinking-studio/PYTHONANYWHERE-DEPLOY.md)

**Quick Deploy Steps:**
1. Create free account at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Clone repository in PythonAnywhere bash console
3. Set up virtual environment and install dependencies
4. Configure WSGI file with project path
5. Add environment variables to `.env` file
6. Reload web app

Your app will be live at: `https://yourusername.pythonanywhere.com`

### Alternative Deployment Options

- **Railway.app**: Auto-detects Flask, simple GitHub integration
- **Render.com**: Free tier available, supports Flask natively
- **Heroku**: Classic PaaS, requires Procfile

## Project Structure

```
ProductPlayGround/
├── product-thinking-studio/
│   ├── app/
│   │   ├── app.py              # Legacy Streamlit orchestration
│   │   ├── prompt.py           # AI engine & business logic
│   │   └── ui.py               # Streamlit UI components
│   ├── templates/
│   │   └── index.html          # Flask application template
│   ├── flask_app.py            # Flask application (production)
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example            # Environment variables template
│   ├── .gitignore             # Git exclusions
│   ├── PYTHONANYWHERE-DEPLOY.md # Deployment guide
│   └── PRD.md                  # Product Requirements Document
└── README.md                   # This file
```

## API Configuration

The application uses OpenAI's GPT-4o model with the following default configuration:

- **Model**: `gpt-4o` (most capable model)
- **Temperature**: `0.7` (balanced creativity/consistency)
- **Max Tokens**: `4000` (comprehensive responses)

These can be adjusted in the `.env` file based on your needs and API budget.

## Features Deep Dive

### Product Challenge Analysis

Input any product decision scenario and receive:
- **Problem Reframing**: Clarification of the core challenge
- **Context Analysis**: Key factors and constraints evaluation
- **Options Exploration**: Comprehensive alternatives assessment
- **Trade-offs Matrix**: Risks vs. benefits for each option
- **Strategic Recommendation**: Data-driven decision with rationale
- **Execution Roadmap**: Prioritized next steps
- **Success Metrics**: KPIs to track decision effectiveness

### Dashboard KPI Diagnostics

Analyze 8 key product metrics:
- Daily Active Users (DAU)
- Monthly Active Users (MAU)
- Average Session Time
- Conversion Rate
- Churn Rate
- 7-Day Retention Rate
- Net Promoter Score (NPS)
- Average Revenue Per User (ARPU)

Receive analysis including:
- Overall product health assessment
- Metric-by-metric deep dives
- Cross-metric pattern insights
- Red flags and concerns
- Root cause hypotheses
- Prioritized action recommendations
- Industry benchmarking context

## Security & Privacy

- ✅ API keys stored in environment variables, never in code
- ✅ `.env` file excluded from version control via `.gitignore`
- ✅ HTTPS recommended for production deployments
- ✅ No user data stored or logged
- ✅ OpenAI API calls comply with their data usage policies

## Cost Considerations

**OpenAI API Costs** (as of 2026):
- GPT-4o: ~$0.01 per analysis (varies by length)
- Estimated monthly cost for moderate use: $10-30

**Hosting**:
- PythonAnywhere Free Tier: $0/month (with limitations)
- PythonAnywhere Paid: $5+/month (recommended for production)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Roadmap

- [ ] Support for multiple AI models (Claude, Gemini)
- [ ] Historical analysis storage and comparison
- [ ] Team collaboration features
- [ ] Custom prompt templates
- [ ] Integration with product analytics tools (Mixpanel, Amplitude)
- [ ] Export to Notion/Confluence
- [ ] Mobile-optimized interface

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions, issues, or feature requests:
- Open an issue on GitHub
- Contact: [Your contact method]

## Acknowledgments

- Built with [OpenAI GPT-4o](https://openai.com/)
- Inspired by the product management community
- Typography: [Inter](https://rsms.me/inter/) by Rasmus Andersson
- Design inspiration: Medium, Notion, Linear

---

**Made with ❤️ for Product Managers by Product Managers**