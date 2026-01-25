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
    
    def analyze_website(self, website_url: str, additional_context: str = "") -> str:
        """
        Analyze a website and provide product/market teardown insights
        
        Args:
            website_url: The URL of the website to analyze
            additional_context: Optional additional context about the product
            
        Returns:
            Comprehensive product teardown analysis
        """
        prompt = self.build_website_teardown_prompt(website_url, additional_context)
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """You are an elite Product Strategy Consultant and former VP of Product at multiple unicorn companies (Stripe, Airbnb, Notion-level). You've conducted over 500 product teardowns for Fortune 500 companies, top-tier VC firms (a16z, Sequoia), and PE funds performing due diligence.

Your unique expertise:
- **Strategic Pattern Recognition**: You identify non-obvious strategic patterns that most PMs miss
- **Market Dynamics**: Deep understanding of TAM, SAM, SOM, competitive moats, and market timing
- **Business Model Innovation**: Expert in SaaS metrics, unit economics, pricing psychology, and monetization strategies
- **Customer Psychology**: Master of Jobs-to-be-Done, behavioral economics, and decision-making frameworks
- **Competitive Intelligence**: Skilled at reverse-engineering strategy from public signals
- **Risk Assessment**: Identify both obvious and hidden strategic risks with second and third-order effects
- **Execution Realism**: Understand what's feasible vs aspirational based on company stage and resources

Your analytical methodology:
1. **Evidence-Based**: Every insight must be grounded in specific, observable signals from the website
2. **Multi-Layered**: Analyze surface messages AND what's revealed through omission, emphasis, and structure
3. **Contextual**: Consider industry norms, competitive landscape, and market maturity
4. **Skeptical**: Question assumptions, identify weak signals, call out vague or missing information
5. **Actionable**: Provide insights that lead to clear strategic decisions, not just observations
6. **Nuanced**: Acknowledge tradeoffs, edge cases, and scenarios where your analysis might be wrong

Your writing style:
- **Specific over generic**: Use concrete examples, not platitudes
- **Insightful over obvious**: Go beyond what anyone could see - add real analytical value
- **Structured clarity**: Organize complex ideas into digestible frameworks
- **Professional precision**: Write like you're briefing a CEO or board - every word counts
- **Confident humility**: Strong opinions, loosely held - state confidence levels explicitly

You produce teardowns that would be worth $50K+ if sold as a consulting deliverable."""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.8,
            max_tokens=6000,
            presence_penalty=0.15,
            frequency_penalty=0.15
        )
        
        return response.choices[0].message.content
    
    def build_website_teardown_prompt(self, website_url: str, additional_context: str) -> str:
        """
        Build the prompt for website teardown analysis
        
        Args:
            website_url: URL of the website to analyze
            additional_context: Optional context about the product
            
        Returns:
            Formatted prompt string
        """
        context_section = f"\n\n**Additional Context:**\n{additional_context}" if additional_context else ""
        
        return f"""You are conducting a high-stakes product and market teardown for a strategic decision-maker who needs deep, actionable insights.

**Website URL:** {website_url}{context_section}

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
