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
    
    def build_walkthrough_prompt(self, user_context: str, walkthrough_data: Dict) -> str:
        """
        Build a specialized prompt for walkthrough mode analysis
        
        Args:
            user_context: Combined context from walkthrough steps
            walkthrough_data: Structured user inputs from walkthrough
            
        Returns:
            Formatted prompt string for walkthrough mode
        """
        return f"""
You are guiding a Product Manager through structured product thinking in Walkthrough Mode.

The user has already done the work to frame their problem and form hypotheses.
Your job is to BUILD ON their thinking, not replace it.

## User's Own Framing

**Target User:** {walkthrough_data.get('targetUser', 'Not specified')}

**Decision to Make:** {walkthrough_data.get('decision', 'Not specified')}

**Constraints:** {walkthrough_data.get('constraints', 'Not specified')}

**User's Hypotheses about Causes:** {walkthrough_data.get('causes', 'Not specified')}

**User's Success Criteria:** {walkthrough_data.get('success', 'Not specified')}

---

Your response should EXPLICITLY REFERENCE the user's own framing above.

Provide analysis in this structure:

## 🎯 Building on Your Framing

Start by acknowledging what the user got right in their problem framing.
Then expand on it with:
- Additional dimensions they might not have considered
- Clarifications or refinements to their framing
- What their constraints imply about viable options

## 💡 Exploring Decision Options

Based on their stated decision and constraints, outline 2-3 possible approaches.

For each option, use language like:
- "One possible approach is..."
- "This would prioritize... at the expense of..."
- "A key tradeoff to consider is..."

**For each option:**
- What it prioritizes (connect to user's success criteria)
- Key tradeoffs (what you gain vs sacrifice)
- How it relates to the user's hypotheses
- Second-order effects to anticipate

## ⚠️ Risk Management

For EACH option above, assess risks:

**User Trust Risk:**
- Likelihood: Low/Medium/High
- Impact: Low/Medium/High  
- Mitigation: Specific strategies

**Delivery / Execution Risk:**
- Likelihood: Low/Medium/High
- Impact: Low/Medium/High
- Mitigation: Specific strategies

**Technical Risk:**
- Likelihood: Low/Medium/High
- Impact: Low/Medium/High
- Mitigation: Specific strategies

**Business / Metrics Risk:**
- Likelihood: Low/Medium/High
- Impact: Low/Medium/High
- Mitigation: Specific strategies

Include: "These risks don't mean you shouldn't proceed—they mean you need visibility and mitigation plans."

## 🎲 Suggested Direction (with Caveats)

Use cautious language:
- "Based on your constraints, one direction to consider is..."
- "This assumes that [list key assumptions]"
- "This would NOT be appropriate if [conditions]"

State explicitly:
- Key assumptions that must be true
- Scenarios where this could fail
- What would change your recommendation

## 🚀 Next Steps

Provide 4-6 concrete, actionable validation steps:

1. **[Action]** - What to do and why
2. **[Action]** - What to do and why
3. **[Action]** - What to do and why

Focus on:
- Learning and validation (not building)
- Quick experiments to test assumptions
- Risk mitigation
- Preserving optionality

## 📊 Success Signals

**Early signals of success (within 2-4 weeks):**
- [Specific, measurable indicators]

**Warning signs to watch for:**
- [Specific red flags that should trigger reconsideration]

**Metrics to track:**
- [Specific KPIs tied to user's success criteria]

---

**CRITICAL TONE REQUIREMENTS:**

❌ DON'T say: "The best choice is...", "You should definitely...", "This will succeed..."

✅ DO say: "One possible approach is...", "A risk to consider is...", "If X is true, then Y might make sense..."

Remember: The user has done their own thinking. Your job is to:
1. Validate and expand their thinking
2. Surface risks and tradeoffs they might miss
3. Provide structure for their decision
4. Acknowledge uncertainty
5. Keep ownership of the decision with them

**Full Context:**
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
    
    def analyze_walkthrough(self, user_context: str, walkthrough_data: Dict) -> str:
        """
        Analyze a product challenge in walkthrough mode with guided steps
        
        Args:
            user_context: The combined context from walkthrough steps
            walkthrough_data: Dictionary with structured walkthrough inputs
            
        Returns:
            Strategic analysis tailored for walkthrough mode
        """
        prompt = self.build_walkthrough_prompt(user_context, walkthrough_data)
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """You are an elite AI Product Thinking coach in Walkthrough Mode.

Your role is to guide structured product thinking, NOT to provide final answers upfront.

Key principles for Walkthrough Mode:
- Reference the user's own context and hypotheses explicitly
- Use cautious, decision-support language ("One possible approach is...", "A risk to consider is...")
- Avoid "best choice", numerical scores, or rigid rankings
- Emphasize tradeoffs over definitive answers
- Make risks and assumptions visible
- Remind users that final judgment remains with them

Structure your response to support learning and critical thinking."""
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
    
    def _format_headings(self, headings: dict) -> str:
        """Format headings for prompt"""
        result = []
        for level, items in headings.items():
            if items:
                result.append(f"{level.upper()}: {', '.join(items[:5])}")
        return '\n'.join(result) if result else "N/A"
    
    def _format_pricing(self, pricing: dict) -> str:
        """Format pricing information"""
        if not pricing:
            return "N/A"
        parts = []
        if pricing.get('has_pricing_page'):
            parts.append("Has dedicated pricing page")
        if pricing.get('pricing_tiers'):
            parts.append(f"Tiers: {', '.join(pricing['pricing_tiers'])}")
        if pricing.get('pricing_signals'):
            parts.append(f"Prices found: {', '.join(pricing['pricing_signals'][:5])}")
        return '\n'.join(parts) if parts else "N/A"
    
    def _format_list(self, items: list) -> str:
        """Format a list of items"""
        return '\n- ' + '\n- '.join(items) if items else "N/A"
    
    def _format_tech_stack(self, tech: dict) -> str:
        """Format technology stack"""
        if not tech:
            return "N/A"
        parts = []
        if tech.get('frameworks'):
            parts.append(f"Frameworks: {', '.join(tech['frameworks'])}")
        if tech.get('analytics'):
            parts.append(f"Analytics: {', '.join(tech['analytics'])}")
        return '\n'.join(parts) if parts else "N/A"
    
    def _format_structure(self, structure: dict) -> str:
        """Format page structure"""
        if not structure:
            return "N/A"
        parts = []
        if structure.get('has_hero'):
            parts.append("✓ Hero section")
        if structure.get('has_navigation'):
            parts.append("✓ Navigation menu")
        if structure.get('sections_count'):
            parts.append(f"{structure['sections_count']} content sections")
        return ', '.join(parts) if parts else "N/A"
    
    def _format_social_proof(self, proof: dict) -> str:
        """Format social proof elements"""
        if not proof:
            return "N/A"
        parts = []
        if proof.get('testimonials'):
            parts.append(f"{len(proof['testimonials'])} testimonials found")
        if proof.get('customer_logos'):
            parts.append("Customer logos displayed")
        if proof.get('stats'):
            parts.append(f"Stats: {', '.join(proof['stats'][:3])}")
        return '\n'.join(parts) if parts else "N/A"
    
    def analyze_website(self, website_url: str, additional_context: str = "") -> str:
        """
        Analyze a website and provide product/market teardown insights
        
        Args:
            website_url: The URL of the website to analyze
            additional_context: Optional additional context about the product
            
        Returns:
            Comprehensive product teardown analysis
        """
        import httpx
        
        # Try to scrape the website for actual content
        scraped_data = None
        try:
            from app.web_scraper import scrape_website_sync
            print(f"Scraping website: {website_url}")
            scraped_data = scrape_website_sync(website_url)
            print(f"Successfully scraped: {scraped_data.get('title', 'Unknown')}")
        except Exception as scrape_error:
            print(f"Web scraping failed (continuing without): {str(scrape_error)}")
            # Continue without scraped data
        
        prompt = self.build_website_teardown_prompt(website_url, additional_context, scraped_data)
        
        try:
            # Create custom HTTP client with extended timeout
            http_client = httpx.Client(timeout=120.0)
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": """You are a senior Product Strategy Consultant specializing in comprehensive product teardowns.

Analyze with depth and precision:
- Extract insights from observable product signals
- Identify strategic patterns and competitive positioning  
- Assess risks with second-order implications
- Deliver actionable, high-value recommendations

Be thorough yet concise. Every insight must be unique and valuable."""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.75,
                max_tokens=6000,
                presence_penalty=0.3,
                frequency_penalty=0.3
            )
            
            if not response or not response.choices:
                raise Exception("Empty response from AI service")
            
            content = response.choices[0].message.content
            
            if not content or len(content.strip()) < 100:
                raise Exception("Generated analysis was too short or empty")
            
            # Check if response was truncated
            if response.choices[0].finish_reason == "length":
                content += "\n\n---\n**Note**: Analysis reached token limit. Key insights captured above."
            
            return content
            
        except Exception as e:
            error_msg = str(e)
            print(f"ERROR in analyze_website: {error_msg}")
            import traceback
            traceback.print_exc()
            
            if "timeout" in error_msg.lower() or "timed out" in error_msg.lower():
                raise Exception("Analysis timeout - the website may be too complex. Please try again.")
            elif "rate_limit" in error_msg.lower():
                raise Exception("API rate limit reached. Please wait a moment and try again.")
            elif "api_key" in error_msg.lower():
                raise Exception("API authentication failed. Please check your API key configuration.")
            else:
                raise Exception(f"Analysis failed: {error_msg}")
    
    def build_website_teardown_prompt(self, website_url: str, additional_context: str, scraped_data: dict = None) -> str:
        """
        Build the prompt for website teardown analysis
        
        Args:
            website_url: URL of the website to analyze
            additional_context: Optional context about the product
            scraped_data: Optional scraped website data from Playwright
            
        Returns:
            Formatted prompt string
        """
        context_section = f"\n\n**Additional Context:**\n{additional_context}" if additional_context else ""
        
        # Build scraped data section if available
        scraped_section = ""
        if scraped_data:
            scraped_section = f"""

**Scraped Website Data:**

**Page Title:** {scraped_data.get('title', 'N/A')}

**Meta Description:** {scraped_data.get('meta_description', 'N/A')}

**Main Headings:**
{self._format_headings(scraped_data.get('headings', {}))}

**Navigation Menu:** {', '.join(scraped_data.get('navigation', [])[:15])}

**Call-to-Actions:** {', '.join(scraped_data.get('call_to_actions', [])[:10])}

**Pricing Information:**
{self._format_pricing(scraped_data.get('pricing_signals', {}))}

**Key Features Mentioned:**
{self._format_list(scraped_data.get('features_mentioned', [])[:10])}

**Technology Stack:**
{self._format_tech_stack(scraped_data.get('technology_stack', {}))}

**Page Structure:**
{self._format_structure(scraped_data.get('page_structure', {}))}

**Social Proof:**
{self._format_social_proof(scraped_data.get('social_proof', {}))}

**Main Content Preview:**
{scraped_data.get('main_content', '')[:1000]}...
"""
        
        return f"""You are conducting a high-stakes product and market teardown for a strategic decision-maker who needs deep, actionable insights.

**Website URL:** {website_url}{context_section}{scraped_section}

---

This teardown must be EXCEPTIONALLY DETAILED and go far beyond surface-level observations. Every section should provide insights that aren't immediately obvious from a quick glance.

## Product Overview & Intent

**Core Functionality:**
- What does this product actually DO? (Be specific about the mechanism, not just the benefit)
- What is the primary job-to-be-done? What job is it REALLY hired for vs what it claims?
- How is the problem framed: as urgent (pain-driven), strategic (opportunity-driven), or operational (efficiency-driven)?

**Positioning Signals:**
- Is this positioned as a tool (tactical), platform (strategic), or capability (transformational)?
- What analogies or mental models does the product anchor to? (e.g., "Stripe for X", "Figma meets Y")
- What category does it claim to belong to? Does it try to create a NEW category or dominate an existing one?

**Strategic Intent (Read Between the Lines):**
- Based on messaging emphasis, what does the company ACTUALLY prioritize? (growth vs monetization vs defensibility)
- What problem might the team THINK they're solving vs what users might actually need?
- What does the website OMIT that's revealing? (missing features, unaddressed objections, avoided comparisons)

**Evidence & Confidence:**
- Quote specific copy or structural elements that reveal intent
- Confidence level: [Low/Medium/High] - explain why

---

## Target Customer Segments

**Primary Customer Profile:**
- **Company size/type**: Individual, SMB (1-50), Mid-market (50-500), Enterprise (500+), or mixed?
- **Buyer persona**: Who signs the check? (Founder, PM, Eng Lead, CFO, Procurement)
- **End user persona**: Who actually uses it? (if different from buyer)
- **Sophistication level**: Beginner, intermediate, expert? Technical vs non-technical?
- **Buying context**: What triggers the search for this product? (pain event, growth stage, compliance need)

**Evidence from Website:**
- What specific language, examples, or use cases reveal the target customer?
- What pricing or packaging signals indicate customer size?
- Who is featured in testimonials, case studies, or logos?

**Secondary/Adjacent Segments:**
- What other segments could this serve but aren't emphasized?
- Why might the company NOT be targeting them? (strategic focus, capability gap, profitability)

**Who This Product is NOT For:**
- Be explicit about who would be a poor fit
- Why this matters strategically (focus, resource allocation, competitive positioning)

**Confidence Assessment:**
- Confidence level: [Low/Medium/High]
- What additional signals would increase confidence?

---

## Customer Jobs & Pain Points

**Functional Jobs-to-be-Done:**
- What task is the customer trying to accomplish?
- What's the current alternative/workaround they're using?
- What functional outcome defines success?

**Emotional Jobs-to-be-Done:**
- What does using this product say about the user? (status, competence, values)
- What anxiety or fear does it address? (looking incompetent, missing opportunity, falling behind)
- What aspiration does it enable? (being innovative, data-driven, customer-centric)

**Social Jobs (if applicable):**
- How does this affect their standing with peers, managers, or customers?
- What tribal identity does it signal? (early adopter, pragmatist, thought leader)

**Pain Points Being Relieved:**
- **Explicit pains** (directly stated on website): List with quotes
- **Implicit pains** (inferred from positioning): What's the pain beneath the pain?
- **Pain severity**: Is this a "hair on fire" problem or a "nice to have" improvement?

**Value Hierarchy:**
- What do customers likely care about MOST: Speed? Cost? Quality? Trust? Control? Insight? Simplicity?
- Rank top 3 value drivers based on message emphasis

**Potential Misalignments:**
- Where might customer expectations not match product reality?
- What jobs might customers THINK this does but it doesn't?
- What pain points are underserved or ignored?

---

## Market & Category Analysis

**Category Definition:**
- What market does this operate in? (e.g., "Marketing Automation", "Collaboration Tools", "Developer Infrastructure")
- Is this an established category or emerging/new category?
- If new category: What existing categories is it pulling from? What's the "category creation" narrative?

**Category Maturity:**
- **Emerging** (0-3 years, undefined, education needed)
- **Growing** (3-7 years, known but evolving)
- **Mature** (7+ years, well-understood, commoditizing)
- **Declining** (being replaced or consolidated)

**Competitive Dynamics:**
- **Competitive density**: Crowded (>20 players), Competitive (5-20), Specialized (2-5), Blue ocean (0-2)
- **Incumbent strength**: Strong incumbents (hard to displace) or weak/absent (opportunity)
- **Differentiation basis**: Technology, UX, pricing, distribution, brand, or unclear?

**Differentiation Signals:**
- How does this product claim to be different? (explicit positioning)
- Is differentiation: **Explicit** (clearly stated), **Implicit** (you must infer), or **Unclear** (me-too messaging)?
- What would users compare this against? (direct competitors, substitute solutions, status quo)
- Is the differentiation **defensible** or easily copied?

**Market Timing:**
- Does this feel early (market not ready), just right (timing window), or late (market saturated)?
- What macro trends support or threaten this category? (AI, remote work, privacy, etc.)

**Confidence Level:** [Low/Medium/High] with reasoning

---

## Value Proposition Assessment

**Primary Value Proposition:**
- What is the #1 value message on the hero/homepage?
- Is it framed as: **Outcome-based** ("10x your revenue") or **Feature-based** ("AI-powered analytics")?
- Is it **Quantified** (specific metrics) or **Qualitative** (better, faster, easier)?

**Value Claim Analysis:**
- **Clarity**: Crystal clear, somewhat clear, or vague/confusing?
- **Credibility**: What proof is offered? (testimonials, metrics, case studies, brand logos, awards)
- **Uniqueness**: Is this value claim unique or generic (could apply to any competitor)?
- **Relevance**: Does this value align with the likely top pain points?

**Secondary Values (Implicit):**
- What other benefits are emphasized lower on the page or in features section?
- What values are implied but not stated? (security, compliance, ease of use)

**Value Communication:**
- Is value communicated through: Stories, Data, Social proof, Metaphors/Analogies, Demos?
- What's the balance of emotion vs logic in the messaging?

**Gaps & Weaknesses:**
- What questions does the value prop leave unanswered?
- What objections are NOT addressed?
- Where does the value proposition feel vague, generic, or unsubstantiated?
- What's missing that should be there? (pricing transparency, security, integrations, etc.)

**Strength Assessment:**
- Strong: Compelling, specific, credible, differentiated
- Moderate: Clear but generic, or unique but not credible
- Weak: Vague, me-too, unsubstantiated

---

## Business & Monetization Signals

**Pricing Model (Inferred):**
- **Free/Freemium**: Free tier visible?
- **Subscription**: Monthly/Annual SaaS?
- **Usage-based**: Pay per seat, API call, transaction?
- **Enterprise/Custom**: "Contact sales" for pricing?
- **One-time**: License or perpetual?

**Pricing Visibility:**
- Transparent (prices shown) or Opaque (contact sales)?
- What does pricing visibility signal about sales motion and deal size?

**Revenue Drivers:**
- What's being monetized? (seats, usage, features, outcomes, services)
- What's the likely ACV (Annual Contract Value) range? ($100s, $1000s, $10,000s, $100,000s+)

**Sales Motion:**
- **Self-serve**: Sign up and use immediately (PLG - Product-Led Growth)
- **Sales-assisted**: Free trial → sales call → close
- **Sales-led**: Enterprise sales cycle with demos, pilots, procurement

**Buying Friction:**
- **Low friction**: Credit card signup, instant access
- **Medium friction**: Demo request, qualification call
- **High friction**: RFP, security review, legal, procurement

**Decision Complexity:**
- **Individual**: One person can decide and buy
- **Team**: Small team consensus needed
- **Organizational**: Multi-stakeholder, executive approval

**Monetization Maturity:**
- Does pricing feel well-thought-out or experimental?
- Are there signals of pricing optimization? (multiple tiers, add-ons, volume discounts)

**Strategic Implications:**
- What does the business model reveal about growth strategy? (land-and-expand, top-down, bottom-up)
- What are the likely monetization challenges? (willingness to pay, price anchoring, value metric alignment)

**Confidence:** [Low/Medium/High] - What evidence supports this assessment?

---

## Scalability & Growth Potential

**Customer Scalability:**
- **TAM signals**: How large is the addressable market? (millions, thousands, hundreds?)
- **Horizontal vs Vertical**: Can this scale across industries or is it niche-specific?
- **Geographic reach**: Global potential or region/language-limited?

**Product Scalability:**
- **Complexity at scale**: Does the product get easier or harder to deliver as it grows?
- **Marginal cost**: Low (software only) or high (services, hardware, manual work)?
- **Multi-tenancy**: Can one instance serve many customers or does each need custom deployment?

**Operational Scalability:**
- **Customer acquisition**: Scalable channels (SEO, PLG) or non-scalable (field sales, events)?
- **Onboarding**: Self-serve or hand-holding required?
- **Support burden**: Low-touch or high-touch post-sale?

**Growth Mechanics:**
- **Viral/Network effects**: Does value increase with more users? (Slack, Figma model)
- **Usage expansion**: Do customers naturally expand usage over time? (Stripe, Snowflake model)
- **Ecosystem lock-in**: Integrations, workflows, data that make switching hard?

**Constraints on Scale:**
- **Trust/Compliance**: Security, privacy, regulatory barriers to scale?
- **Quality control**: Can quality be maintained at scale or does it degrade?
- **Talent requirements**: Need for specialized skills that are hard to hire?

**What Scales Well:**
- List 2-3 aspects that have high leverage for growth

**What May Bottleneck Growth:**
- List 2-3 potential constraints with explanation

**Growth Potential Assessment:** Low, Moderate, High, or Very High - with reasoning

---

## Product & Strategic Risks

Assess each risk dimension with granular detail:

### Market Risk
**Wrong Target Segment:**
- Are they targeting a segment that can't/won't pay sufficiently?
- Evidence for/against this risk
- **Second-order effect**: If this is wrong, what happens to burn rate, runway, pivots needed?

**Weak Demand Signals:**
- Is the pain real or perceived? Is it severe enough to drive action?
- Evidence of demand strength or weakness
- **Second-order effect**: Low demand → slow growth → missed milestones → funding issues

**Category Timing:**
- Too early (market not ready) or too late (market saturated)?
- What would validate good timing?
- **Second-order effect**: Bad timing → wasted GTM spend → need for re-positioning

**Overall Market Risk:** Low/Medium/High

---

### Product Risk
**Value Proposition Clarity:**
- Can a visitor understand the value in <10 seconds?
- Is the problem-solution fit obvious or does it require explanation?
- **Second-order effect**: Unclear value → high CAC → poor unit economics

**Scope Risk:**
- Over-scoped (trying to do too much) or under-scoped (too narrow to matter)?
- Evidence from feature set, messaging, or positioning
- **Second-order effect**: Over-scope → slow shipping → competitive disadvantage

**Product-Market Fit Signals:**
- What evidence suggests strong or weak PMF?
- What's missing that would indicate traction?
- **Second-order effect**: Weak PMF → churn → retention issues → reputation damage

**Overall Product Risk:** Low/Medium/High

---

### Trust & Adoption Risk
**Credibility Barriers:**
- Unknown brand, no social proof, weak trust signals?
- What would it take for customers to trust this?
- **Second-order effect**: Low trust → long sales cycles → high CAC

**Switching Costs:**
- How painful is it to switch FROM current solution TO this?
- Data migration, workflow changes, training required?
- **Second-order effect**: High switching costs → slow adoption → limited growth

**Learning Curve:**
- How steep is the onboarding? Can users get value quickly?
- **Second-order effect**: High learning curve → activation drop-off → low retention

**Overall Adoption Risk:** Low/Medium/High

---

### Differentiation Risk
**Weak Positioning:**
- Is positioning clear and defensible or generic and copyable?
- **Second-order effect**: Weak positioning → price competition → margin compression

**Commoditization Threats:**
- Could this be easily replicated by bigger players or AI/automation?
- **Second-order effect**: Commoditization → pricing pressure → unsustainable economics

**Defensibility:**
- What moats exist? (network effects, data, brand, switching costs, technology IP)
- **Second-order effect**: No moat → intense competition → acquisition pressure

**Overall Differentiation Risk:** Low/Medium/High

---

### Execution & Scaling Risk
**Delivery Complexity:**
- How hard is this to build and maintain?
- **Second-order effect**: High complexity → slow iteration → competitive lag

**Resource Requirements:**
- Capital intensive or lean? Talent requirements rare or common?
- **Second-order effect**: High resource needs → funding dependency → dilution

**Go-to-Market Fit:**
- Does the GTM motion match the product economics?
- **Second-order effect**: GTM mismatch → burn inefficiency → runway risk

**Overall Execution Risk:** Low/Medium/High

---

## Opportunity Areas for PM Focus

Identify 4-6 HIGH-LEVERAGE strategic areas where PM attention would matter most:

1. **[Opportunity Area Title]**
   - **Why it matters**: Strategic importance and impact
   - **Current gap**: What's missing or underoptimized
   - **Leverage**: Why focusing here creates disproportionate value
   - **Risk if ignored**: What gets worse if this isn't addressed

2. **[Repeat for each opportunity]**

**What Should NOT Be Expanded Yet:**
- List 2-3 things that seem tempting but would be premature or distracting
- Explain why restraint matters more than action here

**Critical Assumptions to Validate First:**
- What foundational beliefs must be TRUE for the strategy to work?
- How would you test each assumption quickly and cheaply?

---

## Key PM Questions to Investigate

Generate 10-12 EXCEPTIONAL strategic questions that:
- Probe critical assumptions
- Identify what could break the business model
- Reveal hidden risks or opportunities
- Guide validation and learning

Format each as:
**"If [assumption], then [consequence]... but what if [challenge]?"**

Examples:
1. **"What assumption, if wrong, would completely invalidate the current GTM strategy?"**
   - Why this matters: [explanation]

2. **"What would we see in user behavior within 90 days if we're right about [key hypothesis]?"**
   - Why this matters: [explanation]

3. **"If this becomes successful, who has the most incentive to kill it, and how would they do it?"**
   - Why this matters: [explanation]

4. **"What user segment is currently ignored that could be a 10x bigger opportunity?"**
   - Why this matters: [explanation]

5. **"Where are we most likely overconfident, and what blind spot does that create?"**
   - Why this matters: [explanation]

[Continue with 5-7 more equally thoughtful questions]

---

**CRITICAL QUALITY STANDARDS:**

✅ **Specific over generic**: Every insight must cite observable evidence  
✅ **Deep over shallow**: Go beyond what's obvious - add genuine analytical value  
✅ **Actionable over academic**: Insights should inform real decisions  
✅ **Honest about uncertainty**: State confidence levels, acknowledge gaps  
✅ **Strategic over tactical**: Focus on direction-setting, not feature details  
✅ **Nuanced over binary**: Acknowledge tradeoffs and context-dependency  

**Remember**: This analysis will inform major strategic decisions. Make every section count. If you're writing something that could apply to ANY product, delete it and write something specifically insightful about THIS product.
"""

    def analyze_decision_framing(self, framing_data: Dict) -> str:
        """
        Clarify and refine decision framing
        
        Args:
            framing_data: Dictionary containing decision framing inputs
            
        Returns:
            Clarified decision frame analysis
        """
        prompt = f"""You are a decision architecture expert helping to clarify what decision is actually being made.

**User's Decision Statement:**
{framing_data.get('decision', '')}

**Stakeholders:**
{framing_data.get('stakeholders', 'Not specified')}

**Options on the Table:**
{framing_data.get('options', 'Not specified')}

**Constraints:**
{framing_data.get('constraints', 'Not specified')}

**Success Signals:**
{framing_data.get('success', 'Not specified')}

**Key Unknowns & Risks:**
{framing_data.get('unknowns', 'Not specified')}

---

Please provide a comprehensive, senior-level decision frame analysis with:

## 🎯 Clarified Decision Statement

Restate the decision in clear, specific terms:
- **What exactly is being decided?** (Be precise - not "should we build X" but "should we commit Y resources to build X by Z date")
- **Who has decision authority?** (Individual, committee, needs escalation?)
- **When must this be decided?** (Hard deadline, soft deadline, ongoing?)
- **What triggers action?** (What happens after deciding yes vs no?)

**Precision check:** Could someone unfamiliar with context understand exactly what's being decided? If not, refine further.

## 🔍 What This Decision Is Really About

Look beneath the surface to identify the deeper strategic question:
- **Surface decision:** [What they stated]
- **Underlying tension:** [What's really at stake - e.g., resource allocation, strategic direction, competitive positioning]
- **Why now?** What's forcing this decision at this moment? (Market pressure, internal trigger, opportunity window?)
- **Second-order implications:** What future decisions does this enable or foreclose?

**Strategic context:** How does this fit into the broader product/company strategy? Is this a bet on a new direction or doubling down on current path?

## 👥 Stakeholder Landscape & Power Dynamics

### Decision Makers (Formal Authority)
- **Ultimate decision maker:** [Name/role]
- **Required sign-offs:** [Who must approve]
- **Veto power:** [Who can block this]

### Influencers (No Formal Authority but High Impact)
- **Internal champions:** [Who will advocate for different options]
- **Skeptics/blockers:** [Who might resist, and why]
- **Domain experts:** [Whose input is critical]

### Impacted Parties
- **Directly affected:** [Teams, customers, partners who experience immediate impact]
- **Indirectly affected:** [Those affected by cascading consequences]

### Alignment Requirements
- **Must be aligned before decision:** [Critical stakeholders who need buy-in first]
- **Can be informed after:** [Those who need to know but don't influence decision]
- **Potential conflicts:** [Where stakeholder interests diverge and how to navigate]

**Power map insight:** Who has the most to gain/lose? Where are the hidden incentives that might influence positions?

## ⚖️ The Real Options (Including Hidden Alternatives)

### Stated Options
**Option A: [Name]**
- **Description:** [What this entails]
- **Resources required:** [Time, money, people]
- **Reversibility:** [Easy/Hard/Impossible to undo]
- **Risks:** [What could go wrong]
- **Upside:** [Best-case scenario]

**Option B: [Name]**
[Same structure]

### Unconsidered Alternatives
**Option C: [Hidden/Hybrid approach]**
- **Why this wasn't mentioned:** [Assumption blocking it]
- **How it differs:** [What makes this distinct]
- **Worth exploring?** [Yes/No and why]

### The "Do Nothing" Baseline
- **What happens if we don't decide?** [Natural drift, status quo consequences]
- **Is "do nothing" actually an option?** [Or does indecision = default to something]
- **Opportunity cost:** [What we miss by not acting]

**Decision tree insight:** Are these really mutually exclusive options, or could we phase/combine them?

## 🔒 Binding Constraints (Real vs Assumed)

### Hard Constraints (Unchangeable)
- **[Constraint 1]:** [Why it's immovable - e.g., regulatory requirement, physics, contract]
- **[Constraint 2]:** [Why it's immovable]

### Soft Constraints (Changeable with Effort)
- **[Constraint 1]:** [What it would take to change this - e.g., budget reallocation, timeline extension]
- **[Constraint 2]:** [What it would take to change]

### Assumed Constraints (May Not Be Real)
- **[Assumption 1]:** [Why we believe this is a constraint]
  - **Challenge:** [What if this isn't actually true?]
  - **How to test:** [Quick way to validate]
- **[Assumption 2]:** [Why we believe this]
  - **Challenge:** [What if this isn't actually true?]
  - **How to test:** [Quick way to validate]

**Constraint audit:** Which "constraints" are actually just historical habits or unexamined assumptions?

## ✅ What "Good" Looks Like (Success Definition)

### Measurable Outcomes (3-6 months)
- **Metric 1:** [Specific target] - Why this matters
- **Metric 2:** [Specific target] - Why this matters
- **Metric 3:** [Specific target] - Why this matters

### Observable Signals (What you'd see happening)
- **User behavior:** [What users would do differently]
- **Team dynamics:** [How work would change]
- **Market response:** [External validation]

### Leading Indicators (Early signs of success/failure)
- **Week 1-2:** [What should be visible immediately]
- **Month 1:** [What should be visible in first month]
- **Month 3:** [What should be visible by quarter]

**Failure definition:** What would indicate this was the wrong decision? Be specific about red flags.

## ❓ Critical Unknowns (Ranked by Impact & Learn-ability)

### High Impact, Easy to Learn (DO THESE FIRST)
1. **[Unknown 1]**
   - **Why it matters:** [Impact if assumption is wrong]
   - **How to learn:** [Specific, cheap test]
   - **Timeline:** [How long to get answer]

### High Impact, Hard to Learn (BIGGEST RISK)
1. **[Unknown 1]**
   - **Why it matters:** [Impact if assumption is wrong]
   - **Why it's hard:** [What makes this difficult to validate]
   - **Best proxy:** [Closest thing we can measure]

### Low Impact (DEPRIORITIZE)
- [List unknowns that don't materially affect the decision]

**De-risking sequence:** What's the optimal order to resolve uncertainties to maximize learning per dollar/hour spent?

## ⚠️ What Could Make This Decision Irrelevant

### External Disruptors
- **Market shifts:** [What market change would moot this?]
- **Competitive moves:** [What could a competitor do?]
- **Technology change:** [What tech advancement would change the game?]
- **Regulatory change:** [What policy shift would matter?]

### Internal Disruptors
- **Strategy pivot:** [What internal decision would supersede this?]
- **Resource constraints:** [What budget/people change would block this?]
- **Leadership change:** [How dependent is this on current leadership?]

**Resilience check:** How robust is this decision to foreseeable disruptions? Is it adaptable or brittle?

## 🎯 Decision Readiness Assessment

### What's Clear
- [List elements that are well-understood and stable]

### What's Uncertain But Acceptable
- [List unknowns that won't materially change the decision]

### What's Uncertain And Critical
- [List gaps that should be filled before deciding]

**Recommendation on timing:** 
- ✅ **Ready to decide** if [conditions]
- ⏸️ **Wait and learn** if [conditions]
- 🔄 **Reframe the decision** if [conditions]

---

**CRITICAL QUALITY STANDARDS:**
- Write at the level of a senior product leader presenting to executives
- Be specific and concrete - no generic platitudes
- Challenge assumptions explicitly
- Identify what's NOT being said but should be
- Frame with strategic nuance - acknowledge complexity
- Use clear, professional language - no jargon without explanation

**Remember:** The goal is clarity and rigor before analysis, not recommendations. Help them understand what they're actually deciding with the depth expected in a senior-level strategic brief.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a senior product strategy advisor and decision framing expert. Provide executive-level analysis with the depth and rigor expected in Fortune 500 strategic planning."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=5000
        )
        
        return response.choices[0].message.content

    def analyze_decision_dashboard(self, dashboard_data: Dict) -> str:
        """
        Analyze what signals suggest is going wrong
        
        Args:
            dashboard_data: Dictionary containing problem description and data
            
        Returns:
            Dashboard signal analysis
        """
        prompt = f"""You are a product diagnostics expert. Your job is to help understand what signals suggest is going wrong and form competing hypotheses.

**What Appears to be Going Wrong:**
{dashboard_data.get('problem', '')}

**Supporting Data:**
{dashboard_data.get('data', 'Not provided')}

**Timeline & Context:**
{dashboard_data.get('context', 'Not provided')}

---

Provide a comprehensive diagnostic analysis with:

## 📉 Signal Summary & Pattern Recognition

### What the Data Is Telling Us
Translate the signals into clear, executive-friendly language:
- **Primary pattern observed:** [Main trend or anomaly]
- **Magnitude of change:** [How significant is this deviation from baseline?]
- **Velocity:** [Is this accelerating, stable, or decelerating?]
- **Consistency:** [Is this signal consistent across segments/cohorts/time periods?]

### Visual Pattern Description
Describe what someone looking at the data would see:
- **Shape of the curve:** [Sudden drop, gradual decline, plateauing, etc.]
- **Outliers or anomalies:** [Any data points that don't fit the pattern]
- **Correlation with events:** [Does timing align with product changes, market events, seasonality?]

### Signal Strength Assessment
- **🔴 Strong Signal:** Clear, consistent, significant deviation requiring attention
- **🟡 Moderate Signal:** Noticeable pattern but with confounding factors
- **🟢 Weak Signal:** Could be noise, variance, or early indication

**Current assessment:** [Which category and why]

## 🔍 Competing Hypotheses (Diagnostic Framework)

Generate 4-6 distinct explanations, ranked by likelihood:

### Hypothesis 1: [Descriptive Name - e.g., "User Activation Bottleneck"]
**Likelihood: High/Medium/Low**

**Core Claim:**
[One-sentence statement of what you think is happening]

**What This Would Explain:**
- [Signal 1 this accounts for]
- [Signal 2 this accounts for]
- [Signal 3 this accounts for]

**What This Would NOT Explain:**
- [Aspect of the data this doesn't account for]
- [Conflicting evidence]

**Supporting Evidence:**
- [Data point 1 that supports this]
- [Data point 2 that supports this]
- [External factor that makes this plausible]

**Contradicting Evidence:**
- [Data point that weakens this hypothesis]
- [Why this might be less likely than it appears]

**How to Test This:**
- **Quick test (days):** [Simple validation approach]
- **Rigorous test (weeks):** [More comprehensive validation]
- **Key metric to watch:** [What would move if this hypothesis is true]

**If This Is True, Then...**
- **Implication 1:** [What this means for product strategy]
- **Implication 2:** [What this means for roadmap]
- **Urgency:** [How quickly this needs to be addressed]

---

### Hypothesis 2: [Descriptive Name]
[Same complete structure as Hypothesis 1]

---

### Hypothesis 3: [Descriptive Name]
[Same complete structure]

---

### Hypothesis 4: [Descriptive Name]
[Same complete structure]

---

## 📊 What the Data Shows vs What We're Inferring

### Hard Facts (High Confidence)
**From the data, we can confidently say:**
- [Fact 1: Specific observation with numbers]
- [Fact 2: Specific observation with numbers]
- [Fact 3: Specific observation with numbers]

**Confidence level:** 90%+ - These are direct observations with minimal interpretation

### Reasonable Inferences (Medium Confidence)
**We can reasonably infer:**
- [Inference 1: Pattern suggesting X]
- [Inference 2: Correlation suggesting Y]
- [Inference 3: Trend suggesting Z]

**Confidence level:** 60-80% - These require some interpretation but are well-supported
**Assumption risk:** [What would make these inferences wrong]

### Speculative Interpretations (Low Confidence)
**We might speculate:**
- [Speculation 1: Possible explanation]
- [Speculation 2: Possible explanation]

**Confidence level:** <50% - These are hypotheses requiring validation
**Why uncertain:** [What's missing to increase confidence]

### Critical Data Gaps
**What's Missing That Would Help:**
1. **[Data type 1]:** Why it matters, how hard to get
2. **[Data type 2]:** Why it matters, how hard to get
3. **[Data type 3]:** Why it matters, how hard to get

**Prioritization:** Which gaps to fill first based on impact vs effort

## 🚩 Signal vs Noise Assessment

### Likely Meaningful Signals
**These indicators warrant attention:**
- **[Signal 1]:** Why this is probably real (consistency, magnitude, timing)
- **[Signal 2]:** Why this is probably real
- **[Signal 3]:** Why this is probably real

**Combined weight:** When multiple signals point same direction, confidence increases

### Possible Noise / Natural Variance
**These might be statistical fluctuation:**
- **[Metric 1]:** Why this could be random (sample size, seasonality, measurement error)
- **[Metric 2]:** Why this could be random

**Variance check:** What's the normal range for these metrics? Is this within 1-2 standard deviations?

### Factors That Would Increase Confidence
- **Time:** [How long to observe to confirm pattern]
- **Replication:** [What consistency across segments would confirm]
- **Leading indicators:** [What upstream metrics should also move]

### Factors That Would Decrease Confidence
- **Alternative explanations:** [What else could cause this]
- **Data quality issues:** [Known measurement problems]
- **External events:** [One-time occurrences that could skew data]

## ⚠️ Risks of Acting Too Quickly (Premature Optimization)

### Type I Error Risk: Acting on False Positive
**If we react and this is just noise:**
- **Resource cost:** [Wasted effort, diverted attention]
- **Opportunity cost:** [What we don't do instead]
- **Team morale:** [Whiplash from constant direction changes]
- **Strategic cost:** [Optimizing wrong thing, losing focus]

**Example scenario:** [Concrete example of how this could go wrong]

### Type II Error Risk: Ignoring Real Problem
**If we don't react and this is a real issue:**
- **Escalation:** [How much worse this could get]
- **Recovery cost:** [Harder to fix later than now]
- **Competitive risk:** [What competitors might do]
- **User trust:** [How this affects perception]

**Example scenario:** [Concrete example of cost of inaction]

### Balanced Approach
**Low-cost validation steps:**
- [Action 1: Small test that reduces uncertainty]
- [Action 2: Observation that provides more data]
- [Action 3: Reversible change that tests hypothesis]

**Escalation triggers:** What evidence would justify bigger action?

## 🔄 What to Watch Next (Monitoring Plan)

### Primary Metrics (Check Daily/Weekly)
- **[Metric 1]:** Current value, threshold for concern, why it matters
- **[Metric 2]:** Current value, threshold for concern, why it matters
- **[Metric 3]:** Current value, threshold for concern, why it matters

### Secondary Metrics (Check Weekly/Monthly)
- **[Metric 1]:** What this confirms/refutes
- **[Metric 2]:** What this confirms/refutes

### Leading Indicators (Early Warning)
- **[Metric 1]:** What this predicts
- **[Metric 2]:** What this predicts

### Cohort/Segment Analysis
- **Which segments to track separately:** [Why certain segments matter more]
- **What differences would be meaningful:** [What variance would change interpretation]

### Decision Checkpoints
**Week 1:** Review [specific metrics] - Decision: Continue monitoring vs escalate
**Week 4:** Review [specific metrics] - Decision: Maintain course vs adjust
**Month 3:** Review [specific metrics] - Decision: Validate hypothesis vs pivot

## 🎯 Recommended Diagnostic Sequence

**Phase 1: Validate Signal (1-2 weeks)**
1. [Specific action to confirm data quality]
2. [Specific action to rule out external factors]
3. [Specific action to test primary hypothesis]

**Phase 2: Narrow Hypotheses (2-4 weeks)**
1. [Test that would confirm/refute Hypothesis 1]
2. [Test that would confirm/refute Hypothesis 2]
3. [Data gathering to fill critical gaps]

**Phase 3: Targeted Action (if warranted)**
1. [Smallest intervention that would improve situation]
2. [Measurement plan to assess impact]
3. [Rollback plan if ineffective]

---

**CRITICAL QUALITY STANDARDS:**
- Use probabilistic language ("appears to," "suggests," "could indicate," "one explanation might be")
- Distinguish clearly between observation and interpretation
- Acknowledge uncertainty explicitly
- Provide specific, actionable next steps
- Write at senior PM/exec level - rigorous but accessible
- Avoid false precision (no spurious confidence percentages unless backed by stats)

**Remember:** The goal is to illuminate possibilities and structure thinking, not claim certainty. Good diagnostics expand the hypothesis space before narrowing it.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a senior product analytics and diagnostics expert. Provide rigorous, hypothesis-driven analysis that helps product leaders make evidence-based decisions."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=6000
        )
        
        return response.choices[0].message.content

    def analyze_decision_confidence(self, confidence_data: Dict) -> str:
        """
        Assess decision confidence level
        
        Args:
            confidence_data: Dictionary containing decision and evidence
            
        Returns:
            Confidence assessment
        """
        prompt = f"""You are a decision confidence assessor. Your job is to qualitatively evaluate whether there's enough signal to act.

**Decision Being Considered:**
{confidence_data.get('decision', '')}

**Evidence Supporting This:**
{confidence_data.get('evidence', '')}

**Gaps & Uncertainties:**
{confidence_data.get('gaps', 'Not specified')}

**Decision Timeline:**
{confidence_data.get('timeline', 'Not specified')}

---

Provide a comprehensive, qualitative confidence assessment:

## ⚡ Overall Signal Strength Assessment

Characterize the evidence quality and decision readiness. Select ONE level that best fits:

### 🟢 Strong Signal - HIGH CONFIDENCE (Actionable)
**Characteristics of strong signal:**
- Multiple independent sources of evidence converge on same conclusion
- Key assumptions have been tested with real data/users
- Downside is bounded and manageable even if partially wrong
- Waiting longer would not materially improve decision quality
- Cost of delay exceeds cost of being wrong
- Reversibility is possible if needed

**What this means for action:**
- Proceed with conviction but maintain monitoring
- Allocate resources confidently
- Communicate decision with clarity
- Plan for course-correction if needed

---

### 🟡 Emerging Signal - MODERATE CONFIDENCE (Promising but Incomplete)
**Characteristics of emerging signal:**
- Some solid evidence exists but with gaps in coverage
- A few key assumptions tested, others remain unvalidated
- Could go either way with additional information
- Uncertainty is material but not fatal
- More research would likely improve decision quality
- Timeline allows for some additional validation

**What this means for action:**
- Consider phased approach or pilot
- Invest in validation before full commitment
- Set clear decision checkpoints
- Build in flexibility to adjust course
- Communicate with appropriate caveats

---

### 🔴 Weak Signal - LOW CONFIDENCE (Not Ready)
**Characteristics of weak signal:**
- Evidence is sparse, contradictory, or unreliable
- Most critical assumptions remain untested
- High stakes if wrong, limited ability to recover
- Major gaps in understanding key dynamics
- Decision feels premature given what's known
- Substantial additional research would materially improve quality

**What this means for action:**
- Do NOT proceed with major commitment
- Invest in de-risking and learning first
- Question whether decision can be deferred
- Consider smaller experiments to gain data
- Communicate that more work is needed

---

**YOUR ASSESSMENT:** [Which category applies and why - be specific about which criteria are met/not met]

## 📋 Evidence Quality & Reliability Review

### Source Reliability Assessment
**Primary Evidence Sources:**

**Source 1: [Type - e.g., "User interviews," "Usage analytics," "Market research"]**
- **Reliability:** High / Medium / Low
- **Why:** [Firsthand data, large sample, methodologically sound] OR [Hearsay, small sample, potential bias]
- **Recency:** [How current is this information]
- **Representativeness:** [Does this cover the right users/segments/scenarios]
- **Weight in decision:** [How much should this influence the call]

**Source 2: [Type]**
[Same structure]

**Source 3: [Type]**
[Same structure]

### Evidence Quality Dimensions

**Breadth of Coverage:**
- ✅ **Covered:** [Which aspects/segments/scenarios have data]
- ❌ **Not Covered:** [Which aspects/segments/scenarios lack data]
- **Impact:** [How much does lack of breadth matter]

**Depth of Understanding:**
- **Surface-level:** [What we know at high level]
- **Detailed:** [Where we have deep understanding]
- **Missing detail:** [Where depth would help]

**Temporal Coverage:**
- **Point-in-time:** [Snapshot data]
- **Longitudinal:** [Trends over time]
- **Predictive:** [Leading indicators of future state]
- **Gap:** [What time horizon is missing]

### Bias & Limitation Assessment

**Potential Biases:**
1. **[Selection bias / Confirmation bias / Recency bias / etc.]**
   - **How it manifests:** [Specific way this could skew evidence]
   - **Severity:** High / Medium / Low
   - **Mitigation:** [How to account for this]

2. **[Another bias]**
   [Same structure]

**Data Quality Issues:**
- **Measurement error:** [Any known instrumentation problems]
- **Sample size:** [Is N large enough to be confident]
- **Confounding factors:** [Other variables that could explain the signal]

**Known Limitations:**
- [Limitation 1: What this evidence CAN'T tell us]
- [Limitation 2: What this evidence CAN'T tell us]

## ❓ Critical Gaps That Matter Most

Rank gaps by impact on decision quality:

### Tier 1: Must-Have (Deal-Breakers)
**Gap 1: [Specific unknown]**
- **Why this matters:** [How this could change the decision]
- **Current assumption:** [What we're assuming in absence of data]
- **Risk if wrong:** [Consequence of bad assumption]
- **How to fill:** [Specific approach to get this data]
- **Effort:** [Days/weeks/months + cost]
- **Timeline:** [How long this takes to learn]

**Gap 2: [Specific unknown]**
[Same structure]

### Tier 2: Important (Should-Have)
**Gap 1: [Specific unknown]**
- **Why this matters:** [Improves decision but not fatal if missing]
- **Workaround:** [How to proceed without this]
- **How to fill:** [Approach to get this data]

**Gap 2: [Specific unknown]**
[Same structure]

### Tier 3: Nice-to-Have (Incrementally Helpful)
- [Gap that would add confidence but is low-priority]
- [Gap that would add confidence but is low-priority]

**Prioritization Logic:** Which gaps to fill in what order, given time/resource constraints

## 🎯 Confidence-Building Pathway

Specific actions to strengthen the signal:

### Quick Wins (Can Execute in Days/Weeks)
1. **[Action 1]**
   - **What you'd learn:** [Specific question this answers]
   - **Effort:** [Hours/days required]
   - **Impact on confidence:** [How much this helps]
   - **Method:** [Specific approach - e.g., "Interview 5 users from segment X"]

2. **[Action 2]**
   [Same structure]

3. **[Action 3]**
   [Same structure]

### Medium-Term Efforts (Weeks to Months)
1. **[Action 1]**
   - **What you'd learn:** [Specific question this answers]
   - **Effort:** [Weeks/months required]
   - **Impact on confidence:** [How much this helps]
   - **Method:** [Specific approach - e.g., "Run controlled pilot with cohort"]

2. **[Action 2]**
   [Same structure]

### Learn-By-Doing (Can Only Know After Acting)
- **[Aspect 1]:** [What you can only learn through execution]
- **[Aspect 2]:** [What you can only learn through execution]
- **Implication:** [What this means for approach - phased rollout, built-in checkpoints, etc.]

## ⏱️ Confidence vs Timeline Trade-off Analysis

### Decision Timeline
- **Hard deadline:** [If applicable - regulatory, competitive, etc.]
- **Soft deadline:** [Preferred decision date]
- **Cost of delay:** [What happens if we wait - opportunity cost, competitive risk, etc.]
- **Available time:** [Days/weeks/months until decision needed]

### What's Possible in Available Time
- **If we have [X time]:** [Which gaps can be filled]
- **If we have [Y time]:** [Which gaps can be filled]
- **If we need to decide today:** [What we go with]

### Trade-off Framing
**Option A: Decide Now with Current Evidence**
- **Pro:** [Speed to market, first-mover, etc.]
- **Con:** [Higher uncertainty, risk of wrong call]
- **Best if:** [Conditions where speed matters more than certainty]

**Option B: Delay to Improve Evidence**
- **Pro:** [Higher confidence, better decision quality]
- **Con:** [Missed opportunity, competitive disadvantage]
- **Best if:** [Conditions where getting it right matters more than speed]

**Option C: Phased Approach with Learning**
- **Pro:** [Balance speed and learning]
- **Con:** [Complexity, longer total timeline]
- **Best if:** [Conditions where reversibility is possible]

### Time-Boxed Learning Plan
Given available time, optimal sequence:
1. **[Week/Month 1]:** [Highest-priority gap to fill]
2. **[Week/Month 2]:** [Next-priority gap]
3. **[Decision checkpoint]:** [Evaluate evidence, make go/no-go/iterate call]

## ⚠️ Risk Assessment

### Downside Risk (What if we're wrong?)
**If decision fails:**
- **Resource loss:** [Wasted time/money/people]
- **Opportunity cost:** [What we didn't do instead]
- **Reputation/trust:** [Internal/external credibility impact]
- **Reversibility:** [Can we undo this? How hard/costly?]
- **Recovery time:** [How long to get back to neutral]

**Severity:** High / Medium / Low
**Manageability:** [Can we limit downside through design?]

### Upside Potential (What if we're right?)
**If decision succeeds:**
- **Business impact:** [Revenue, growth, efficiency gains]
- **Strategic position:** [Market position, competitive advantage]
- **Learning value:** [What we gain even if only partially successful]
- **Optionality:** [Future opportunities this enables]

**Magnitude:** High / Medium / Low

### Asymmetric Payoff Analysis
- **Expected value framing:** [Upside × probability vs Downside × probability]
- **Convex/Concave:** [Are returns linear or non-linear?]
- **Portfolio view:** [How does this fit with other bets?]

## 🧠 Final Judgment & Recommendation

### Confidence Characterization
"You have **[strong/emerging/weak] evidence** for a decision that:
- **Stakes:** [High/Medium/Low - what's at risk]
- **Timeline:** [Urgent/Normal/Flexible - when decision needed]
- **Reversibility:** [Easy/Hard/Impossible - can you course-correct]
- **Opportunity:** [Large/Moderate/Small - upside potential]

The central question is whether **[specific key uncertainty]** is acceptable given **[timeline pressure / stakes / strategic importance]**."

### Recommendation on Decision Readiness

**✅ PROCEED** if:
- [Condition 1]
- [Condition 2]
- [Condition 3]

**⏸️ PAUSE & LEARN** if:
- [Condition 1]
- [Condition 2]
- [Condition 3]

**🔄 REFRAME DECISION** if:
- [Condition 1]
- [Condition 2]
- [Condition 3]

### Next Best Action
[Specific, concrete next step - not "gather more data" but "Interview 10 users from segment X about behavior Y by date Z"]

---

**CRITICAL QUALITY STANDARDS:**
- NO percentages, scores, or numerical confidence ratings
- Qualitative assessment supporting human judgment
- Explicit about what's known vs unknown vs unknowable
- Honest about uncertainty without paralyzing decision-making
- Senior PM/executive level analysis - rigorous but actionable
- Balance between thorough analysis and clarity

**Remember:** Confidence assessment is about helping leaders understand what they're betting on, not providing algorithmic certainty. The goal is informed judgment, not false precision.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a senior product strategy advisor specializing in decision confidence assessment. Help leaders understand the strength of their evidence and make informed risk-adjusted decisions."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=6000
        )
        
        return response.choices[0].message.content

    def generate_decision_defense(self, defense_data: Dict) -> str:
        """
        Generate decision defense brief for stakeholders
        
        Args:
            defense_data: Dictionary containing decision details
            
        Returns:
            Executive-friendly defense brief
        """
        prompt = f"""You are an executive communication expert. Create a clear, compelling brief to defend a decision to stakeholders.

**Decision Made:**
{defense_data.get('decision', '')}

**Rationale:**
{defense_data.get('rationale', '')}

**Tradeoffs Considered:**
{defense_data.get('tradeoffs', 'Not specified')}

**Known Risks:**
{defense_data.get('risks', 'Not specified')}

**Target Audience:**
{defense_data.get('audience', 'General stakeholders')}

---

Create an executive-friendly decision defense brief:

## 📋 Executive Summary (3-4 sentences)
The decision, the why, and the expected outcome in plain language. Make it email-ready.

## 🎯 Decision Statement
Clear, one-sentence statement of what was decided.

## 💡 Why This Decision
Explain the rationale in terms of:
- Business impact
- User/customer benefit  
- Strategic alignment
- Opportunity cost of alternatives

## ⚖️ Tradeoffs Evaluated
Present the options considered and why this path was chosen:

| Option | Pros | Cons | Why Chosen/Not Chosen |
|--------|------|------|-----------------------|
| [This decision] | ... | ... | ✓ Selected because... |
| [Alternative 1] | ... | ... | ✗ Rejected because... |
| [Alternative 2] | ... | ... | ✗ Rejected because... |

## 🚨 Risks & Mitigation
Be honest about what could go wrong:

**Risk 1: [Name]**
- Impact if it happens: [High/Medium/Low]
- Likelihood: [Our assessment]
- Mitigation plan: [What we're doing]

[Continue for each risk]

## ✅ Success Metrics
How we'll know if this was the right call:
- [Metric 1]: Target by [timeframe]
- [Metric 2]: Target by [timeframe]
- [Leading indicator]: What we'll watch early

## 🛡️ Addressing Likely Objections

**"Why not [alternative approach]?"**
[Your response]

**"What if [concern]?"**
[Your response]

**"How can you be sure this will work?"**
[Your response]

## 📅 Next Steps & Timeline
- [Date]: [Milestone]
- [Date]: [Checkpoint for review]
- [Date]: [Evaluation of outcomes]

## 💬 Talking Points (for Q&A)
Bullet points you can use when discussing this decision:
- [Key point 1]
- [Key point 2]
- [Key point 3]

---

**Tone:** Confident but not overconfident. Acknowledge uncertainty. Show you've thought through objections. Make it clear this was a deliberate, reasoned choice—not impulsive.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a senior executive communications specialist. Create decision defense briefs at Fortune 500 caliber - comprehensive, rigorous, and designed for C-level stakeholder communication."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=7000
        )
        
        return response.choices[0].message.content

    def analyze_retrospective(self, retro_data: Dict) -> str:
        """
        Analyze decision retrospective to extract learnings
        
        Args:
            retro_data: Dictionary containing retrospective details
            
        Returns:
            Retrospective analysis and learnings
        """
        prompt = f"""You are a decision learning expert. Help extract learnings from a past decision—focus on learning, not blame.

**Original Decision:**
{retro_data.get('decision', '')}

**What We Expected:**
{retro_data.get('expected', '')}

**What Actually Happened:**
{retro_data.get('actual', '')}

**Assumptions Analysis:**
{retro_data.get('assumptions', 'Not specified')}

**What Would You Do Differently:**
{retro_data.get('differently', 'Not specified')}

---

Provide a learning-focused retrospective analysis:

## 🔄 Outcome Summary
Concise comparison:
- **Expected:** [Summary]
- **Actual:** [Summary]
- **Variance:** [What differed and by how much]

## ✅ What Went Right (and Why)
Identify what worked and the underlying reasons:
- [Success 1]: Why this happened, what enabled it
- [Success 2]: Why this happened, what enabled it
[Continue...]

## ❌ What Didn't Go as Planned (and Why)
Identify misses without blame:
- [Miss 1]: What happened, why it diverged from expectations
- [Miss 2]: What happened, why it diverged from expectations
[Continue...]

## 🔍 Assumption Testing Results

**Assumptions That Held True:**
- [Assumption]: How it was validated, why it held
- [Assumption]: How it was validated, why it held

**Assumptions That Broke:**
- [Assumption]: How/when it broke, why we believed it, what we learned
- [Assumption]: How/when it broke, why we believed it, what we learned

**Assumptions We Never Actually Tested:**
- [Assumption]: Why we didn't test it, what that cost us

## 💡 Key Learnings

### About Our Decision-Making Process
- What decision process worked well?
- What should we change next time?
- What signals did we miss or misinterpret?

### About Our Estimates
- Were timelines accurate? If not, where did we misjudge?
- Were resource estimates accurate? If not, what did we undercount?
- Were impact estimates accurate? If not, what did we misunderstand?

### About Our Product/Market
- What did we learn about users?
- What did we learn about our capabilities?
- What did we learn about the competitive landscape?

## 🎯 Concrete Guidance for Next Time

**Do More Of:**
- [Specific practice that worked]
- [Specific practice that worked]

**Do Less Of:**
- [Specific practice that didn't work]
- [Specific practice that didn't work]

**Start Doing:**
- [New practice to adopt]
- [New practice to adopt]

**Stop Doing:**
- [Practice to abandon]
- [Practice to abandon]

## 📚 Pattern Recognition
Does this retrospective reveal any recurring patterns?
- Do we consistently over/underestimate certain things?
- Do we have blind spots in specific areas?
- What type of assumptions do we tend to get wrong?

## 🏆 If You Could Do It Over
With perfect hindsight, what's the ONE thing you'd change that would have had the biggest positive impact?

---

**CRITICAL:** Frame everything as learning, not blame. Use "we" language. Focus on process improvement and pattern recognition. The goal is to improve future decision-making, not relitigate the past.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a senior organizational learning expert. Extract deep insights from past decisions with the rigor expected in high-performing product organizations. Focus on patterns, systemic issues, and actionable improvements."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=6000
        )
        
        return response.choices[0].message.content
