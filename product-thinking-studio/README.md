# 🚀 Product Thinking Studio

A professional, AI-powered playground for Product Managers to structure their thinking, analyze complex decisions, and gain strategic clarity.

## ✨ Features

- **🎯 Structured Decision Framework**: Navigate complex product decisions with a proven framework
- **🧠 AI-Powered Analysis**: Leverage GPT-4 for deep strategic insights
- **💎 Beautiful UI/UX**: Professional interface with smooth animations and modern design
- **⚡ Real-time Insights**: Get instant, actionable recommendations
- **📊 Multi-Dimensional Analysis**: Evaluate risks, options, and outcomes comprehensively

## 🎨 Design Philosophy

- **Professional Fonts**: Inter for body text, Poppins for headings
- **Smooth Animations**: Thoughtful micro-interactions and transitions
- **Modern Aesthetics**: Gradient accents, card-based layouts, and clean spacing
- **Responsive Design**: Works beautifully on all screen sizes
- **Accessibility First**: High contrast, clear hierarchy, and intuitive navigation

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   cd product-thinking-studio
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

4. **Run the application**
   ```bash
   streamlit run app/app.py
   ```

5. **Open in browser**
   ```
   Navigate to http://localhost:8501
   ```

## 📁 Project Structure

```
product-thinking-studio/
├── app/
│   ├── app.py          # Main entry point - orchestrates UI and logic
│   ├── prompt.py       # ALL LOGIC LIVES HERE - AI engine & business logic
│   └── ui.py           # UI ONLY - Components, styling, animations
├── docs/
│   └── product-decisions.md  # Document your product decisions
├── README.md           # You are here!
└── requirements.txt    # Python dependencies
```

## 🎯 How to Use

1. **Describe Your Challenge**: Enter your product situation, including context, constraints, and stakeholders
2. **Analyze**: Click the analyze button to get AI-powered insights
3. **Review Framework**: Get structured analysis across multiple dimensions:
   - Problem Reframing
   - Root Cause Analysis
   - Decision Options with Tradeoffs
   - Risk Assessment
   - Suggested Direction
   - Next Steps
   - Success Signals

## 💡 Example Scenarios

**Engagement Drop**
```
Our user engagement dropped 15% after launching the new AI-powered 
recommendation feature. Legal raised explainability concerns during 
the rollout. Engineering team is at 90% capacity with upcoming 
compliance work. How should we proceed?
```

**Feature Prioritization**
```
We have three competing initiatives: improving onboarding flow, 
adding enterprise SSO, and building a mobile app. Sales wants SSO, 
users want mobile, and metrics show onboarding needs work. Q2 capacity 
allows for only one major initiative.
```

**Technical Debt vs Features**
```
Backend performance degraded by 40% over the past 6 months. Customer 
complaints are increasing. Meanwhile, our roadmap has 5 high-priority 
features that leadership committed to. How do we balance technical 
debt with feature delivery?
```

## 🎨 UI/UX Highlights

- **Gradient Branding**: Purple-blue gradient theme throughout
- **Smooth Animations**: Fade-ins, slide-downs, hover effects
- **Professional Typography**: Google Fonts (Inter & Poppins)
- **Custom Scrollbars**: Styled to match the theme
- **Responsive Cards**: Hover effects and smooth transitions
- **Loading States**: Elegant spinners and progress indicators
- **Risk Badges**: Color-coded severity indicators

## 🛠 Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Engine**: OpenAI GPT-4o-mini
- **Styling**: Custom CSS with animations
- **Fonts**: Google Fonts (Inter, Poppins)

## 📊 Framework Components

The analysis engine evaluates your situation across:

1. **Problem Reframing** - Clarify what you're really solving
2. **Root Cause Analysis** - Multi-dimensional investigation
3. **Decision Options** - Viable paths with clear tradeoffs
4. **Risk Management** - Comprehensive risk assessment
5. **Direction** - Recommended approach with caveats
6. **Next Steps** - Actionable validation steps
7. **Success Signals** - How to measure outcomes

## 🔐 Environment Variables

```bash
OPENAI_API_KEY=your-openai-api-key
```

## 🤝 Contributing

This is a product thinking playground! Feel free to:
- Add new analysis frameworks
- Enhance the UI/UX
- Improve the AI prompts
- Add new features

## 📝 License

MIT License - feel free to use this for your product work!

## 🌟 Pro Tips

- **Be Specific**: Include metrics, constraints, and stakeholder perspectives
- **Add Context**: The more context you provide, the better the analysis
- **Iterate**: Use this for multiple scenarios and compare approaches
- **Document**: Save your insights in `docs/product-decisions.md`

---

Built with ❤️ for Product Managers who think deeply about their craft.
