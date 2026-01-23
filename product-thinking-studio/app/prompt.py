"""
ALL LOGIC LIVES HERE
Product Thinking Engine - Core business logic and AI interaction
"""
import os
from openai import OpenAI
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class ProductThinkingEngine:
    """
    Core engine for product thinking analysis
    Handles all business logic, AI interactions, and data processing
    """
    
    def __init__(self):
        """Initialize the Product Thinking Engine"""
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        # Get model from environment, default to gpt-4o for best results
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o")
        
        # Get response quality settings
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))
        self.max_tokens = int(os.getenv("MAX_TOKENS", "4000"))
    
    def analyze_kpis(self, kpi_data: Dict) -> str:
        """
        Analyze dashboard KPIs and identify issues
        
        Args:
            kpi_data: Dictionary containing KPI metrics
            
        Returns:
            Diagnostic analysis of the KPIs
        """
        prompt = self.build_kpi_analysis_prompt(kpi_data)
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """You are an elite product analytics expert and data scientist with 15+ years of experience analyzing product metrics for top tech companies.

You specialize in:
- KPI analysis and diagnostics
- Product health assessment
- Identifying metric correlations and causations
- Root cause analysis from data patterns
- Actionable recommendations based on metrics

Your approach:
- Data-driven insights
- Pattern recognition across multiple metrics
- Understanding metric interdependencies
- Practical, actionable recommendations
- Clear communication of technical insights"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            presence_penalty=0.1,
            frequency_penalty=0.1
        )
        
        return response.choices[0].message.content
    
    def build_kpi_analysis_prompt(self, kpi_data: Dict) -> str:
        """
        Build the prompt for KPI analysis
        
        Args:
            kpi_data: Dictionary containing KPI metrics
            
        Returns:
            Formatted prompt string
        """
        return f"""
Analyze the following product dashboard metrics and provide comprehensive diagnostic insights.

## Dashboard Metrics

**Engagement Metrics:**
- Daily Active Users (DAU): {kpi_data['dau']:,}
- Monthly Active Users (MAU): {kpi_data['mau']:,}
- Average Session Time: {kpi_data['avg_session_time']} minutes

**Conversion & Retention:**
- Conversion Rate: {kpi_data['conversion_rate']}%
- 7-Day Retention Rate: {kpi_data['retention_rate']}%
- Churn Rate: {kpi_data['churn_rate']}%

**User Satisfaction & Revenue:**
- NPS Score: {kpi_data['nps_score']}
- Average Revenue Per User (ARPU): ${kpi_data['revenue_per_user']:.2f}

**Recent Context:**
{kpi_data['recent_changes'] if kpi_data['recent_changes'] else "No recent changes mentioned"}

---

Please provide a comprehensive analysis in the following structure:

## 🎯 Dashboard Health Overview
- Overall product health assessment
- Key strengths and weaknesses
- Critical metrics requiring attention

## 📊 Metric-by-Metric Analysis

### Engagement Health
- DAU/MAU ratio analysis (stickiness)
- Session time implications
- What the engagement metrics tell us

### Conversion Funnel
- Conversion rate benchmarking
- Relationship between engagement and conversion
- Potential conversion blockers

### Retention & Churn
- Retention quality assessment
- Churn rate implications
- Cohort health indicators

### User Satisfaction
- NPS score interpretation
- Correlation with other metrics
- Voice of customer signals

### Monetization
- ARPU health and trends
- Revenue quality indicators
- Monetization efficiency

## 🔍 Cross-Metric Insights
Identify relationships and patterns across metrics:
- Which metrics are correlated?
- What do the patterns suggest?
- Hidden insights from metric combinations

## ⚠️ Red Flags & Concerns
List specific issues that need immediate attention:
- Critical problems
- Warning signs
- Deteriorating trends

## 💡 Root Cause Hypotheses
Based on the metrics, what could be causing the patterns?
- Most likely explanations
- Secondary factors
- External influences

## 🎯 Recommended Actions
Prioritized list of what to do next:
1. Immediate actions (this week)
2. Short-term initiatives (this month)
3. Strategic moves (this quarter)

## 📈 Metrics to Watch
Which metrics should the team monitor closely and why?

## ✅ Benchmarking Context
How do these metrics compare to industry standards?
- What's good
- What's concerning
- What's exceptional

---

**Critical Rules:**
- Be specific with numbers and percentages
- Explain WHY each metric matters
- Identify cause-and-effect relationships
- Provide actionable, prioritized recommendations
- Use product thinking, not just data analysis
- Consider user psychology and behavior
"""
        
    def build_prompt(self, user_context: str) -> str:
        """
        Build the structured prompt for AI analysis
        
        Args:
            user_context: The product situation described by the user
            
        Returns:
            Formatted prompt string
        """
        return f"""
You are an elite AI Product Thinking assistant for Product Managers.

Your role is to support structured reasoning under uncertainty.
You must avoid false certainty, numerical scoring, or rigid ranking.

Return output STRICTLY in the following structure with clear formatting:

## 🎯 Problem Reframing
- Restate the core problem in clear terms
- Distinguish symptoms from underlying issues
- Identify what's really at stake

## 🔍 Root Cause Analysis
Analyze plausible causes across multiple dimensions:

**User Dimension:**
- What user behaviors or needs might explain this?

**Product Dimension:**
- What product design or experience factors could contribute?

**Technology Dimension:**
- What technical constraints or issues may be involved?

**Process Dimension:**
- What organizational or process factors are at play?

**External / Market Dimension:**
- What external forces or market dynamics could influence this?

## 💡 Decision Options
Provide 2–3 viable strategic options.

For each option:
- **What it prioritizes:** Core focus and value proposition
- **Key Tradeoffs:** What you gain vs what you sacrifice
- **Second-order effects:** Downstream consequences to consider

## ⚠️ Risk Management
For EACH option above, assess risks across these categories:

**User Trust Risk:**
- Likelihood: Low/Medium/High
- Impact: Low/Medium/High
- Mitigation strategies

**Delivery / Execution Risk:**
- Likelihood: Low/Medium/High
- Impact: Low/Medium/High
- Mitigation strategies

**Technical Risk:**
- Likelihood: Low/Medium/High
- Impact: Low/Medium/High
- Mitigation strategies

**Legal / Compliance Risk:**
- Likelihood: Low/Medium/High
- Impact: Low/Medium/High
- Mitigation strategies

**Business / Metrics Risk:**
- Likelihood: Low/Medium/High
- Impact: Low/Medium/High
- Mitigation strategies

## 🎲 Suggested Direction (with Caveats)
- Recommend a direction with clear conditions
- State key assumptions explicitly
- Explain scenarios where this would NOT be appropriate
- Acknowledge uncertainty

## 🚀 Next Steps
Provide 3–5 concrete, actionable steps focused on:
- Validation and learning
- Risk mitigation
- Quick wins where possible

## 📊 Success Signals

**Leading Indicators of Success:**
- What early signals would validate this approach?

**Leading Indicators of Failure:**
- What warning signs should trigger a pivot?

**Key Metrics to Track:**
- What should you measure?

---

**Critical Rules:**
- NO numerical scores or certainty percentages
- Be explicit about tradeoffs and limitations
- Avoid generic platitudes - be specific and actionable
- Acknowledge what you DON'T know
- Ground insights in product thinking frameworks

**User Context:**
{user_context}
"""
    
    def analyze(self, user_context: str) -> str:
        """
        Analyze the product situation and return insights
        
        Args:
            user_context: The product situation to analyze
            
        Returns:
            Formatted analysis response
        """
        # Build the prompt
        prompt = self.build_prompt(user_context)
        
        # Call OpenAI API with optimized settings
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """You are an elite product strategy advisor with 15+ years of experience at top tech companies (Google, Amazon, Meta, Apple). 
                    
You have deep expertise in:
- Product management frameworks (Jobs-to-be-Done, North Star Metrics, OKRs)
- Strategic decision-making under uncertainty
- Organizational dynamics and stakeholder management
- Technical architecture and engineering tradeoffs
- Growth, engagement, and retention strategies
- Risk assessment and mitigation

Your thinking style:
- First principles reasoning
- Systems thinking and second-order effects
- Evidence-based decision making
- Nuanced understanding of tradeoffs
- Clear communication with actionable insights

You help PMs navigate complex decisions with clarity, avoiding false certainty while providing concrete direction."""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            presence_penalty=0.1,  # Encourage diverse insights
            frequency_penalty=0.1  # Reduce repetition
        )
        
        # Extract and return the response
        return response.choices[0].message.content
    
    def validate_context(self, user_context: str) -> Dict[str, any]:
        """
        Validate the user input context
        
        Args:
            user_context: The user's input
            
        Returns:
            Dictionary with validation results
        """
        if not user_context or not user_context.strip():
            return {
                "valid": False,
                "message": "Please provide a product situation to analyze."
            }
        
        if len(user_context.strip()) < 20:
            return {
                "valid": False,
                "message": "Please provide more details about your product situation (at least 20 characters)."
            }
        
        return {
            "valid": True,
            "message": "Input validated successfully."
        }
    
    def extract_key_themes(self, context: str) -> List[str]:
        """
        Extract key themes from the context (for future analytics)
        
        Args:
            context: User's product context
            
        Returns:
            List of identified themes
        """
        # Placeholder for future enhancement
        themes = []
        
        # Simple keyword detection
        keywords = {
            "engagement": "User Engagement",
            "growth": "Growth",
            "retention": "Retention",
            "monetization": "Monetization",
            "technical": "Technical Debt",
            "legal": "Legal/Compliance",
            "ai": "AI/ML",
            "feature": "Feature Development"
        }
        
        context_lower = context.lower()
        for keyword, theme in keywords.items():
            if keyword in context_lower:
                themes.append(theme)
        
        return themes if themes else ["General Product Strategy"]
