"""
Product Thinking Studio - Decision Support Logic

This module provides structured frameworks for product decision support:
- Root Cause Analysis (RCA)
- Risk Management
- Decision Guidance
"""

from typing import Dict, List
from dataclasses import dataclass


@dataclass
class RiskAssessment:
    """Represents a risk with likelihood, impact, and mitigation."""
    category: str
    description: str
    likelihood: str  # Low, Medium, High
    impact: str  # Low, Medium, High
    mitigation: str


class DecisionSupportEngine:
    """
    Core engine for product decision support.
    Follows a structured, prompt-driven approach without ML models.
    """
    
    # Root Cause Analysis dimensions (non-negotiable)
    RCA_DIMENSIONS = [
        "User",
        "Product", 
        "Technology",
        "Process",
        "External / Market"
    ]
    
    # Risk Management categories (non-negotiable)
    RISK_CATEGORIES = [
        "User Trust",
        "Delivery / Execution",
        "Technical",
        "Legal / Compliance",
        "Business / Metrics"
    ]
    
    LIKELIHOOD_LEVELS = ["Low", "Medium", "High"]
    IMPACT_LEVELS = ["Low", "Medium", "High"]
    
    @staticmethod
    def get_rca_template() -> Dict[str, str]:
        """Returns empty template for Root Cause Analysis."""
        return {dim: "" for dim in DecisionSupportEngine.RCA_DIMENSIONS}
    
    @staticmethod
    def get_risk_template() -> List[str]:
        """Returns list of risk categories to analyze."""
        return DecisionSupportEngine.RISK_CATEGORIES.copy()
    
    @staticmethod
    def generate_analysis_prompt(problem_statement: str) -> str:
        """
        Generate a structured prompt for analyzing the product decision.
        This guides the user through the decision-support framework.
        """
        prompt = f"""
# Product Decision Analysis

## Problem Statement
{problem_statement}

## Analysis Framework

### 1. Problem Reframing
Consider:
- What is the underlying problem you're trying to solve?
- Who is experiencing this problem?
- What assumptions are you making?
- What would happen if you didn't solve this?

### 2. Root Cause Analysis
Examine each dimension:

**User:**
- What user needs, behaviors, or pain points contribute to this?
- What user feedback or data informs this?

**Product:**
- What product design or feature gaps exist?
- How does current product behavior contribute?

**Technology:**
- What technical constraints or limitations apply?
- Are there technical debt or architecture factors?

**Process:**
- What team, workflow, or organizational processes are involved?
- Are there collaboration or communication gaps?

**External / Market:**
- What market forces, competitors, or external factors matter?
- How might regulations or industry trends affect this?

### 3. Decision Options
List potential approaches (avoid ranking):
- Option A: [Description]
- Option B: [Description]
- Option C: [Description]

### 4. Risk Management
For EACH option, analyze risks across:

**User Trust:**
- Likelihood: [Low/Medium/High]
- Impact: [Low/Medium/High]
- Mitigation: [Concrete, testable action]

**Delivery / Execution:**
- Likelihood: [Low/Medium/High]
- Impact: [Low/Medium/High]
- Mitigation: [Concrete, testable action]

**Technical:**
- Likelihood: [Low/Medium/High]
- Impact: [Low/Medium/High]
- Mitigation: [Concrete, testable action]

**Legal / Compliance:**
- Likelihood: [Low/Medium/High]
- Impact: [Low/Medium/High]
- Mitigation: [Concrete, testable action]

**Business / Metrics:**
- Likelihood: [Low/Medium/High]
- Impact: [Low/Medium/High]
- Mitigation: [Concrete, testable action]

### 5. Suggested Direction (with Caveats)
- What direction seems reasonable given current information?
- What key assumptions does this rely on?
- When would this advice NOT apply?
- What tradeoffs are you accepting?

### 6. Next Steps
- What can you do to test assumptions?
- What data or feedback would reduce uncertainty?
- Who needs to be involved?
- What is the smallest valuable experiment?

### 7. Success Signals
- What would indicate you're on the right track?
- What would indicate you need to pivot?
- What metrics matter (and which don't)?
"""
        return prompt
    
    @staticmethod
    def validate_output_structure(content: str) -> Dict[str, bool]:
        """
        Validates that output follows the required structure.
        Returns a dict of section presence.
        """
        required_sections = [
            "Problem Reframing",
            "Root Cause Analysis",
            "Decision Options",
            "Risk Management",
            "Suggested Direction",
            "Next Steps",
            "Success Signals"
        ]
        
        validation = {}
        for section in required_sections:
            validation[section] = section.lower() in content.lower()
        
        return validation
    
    @staticmethod
    def get_guidance_principles() -> List[str]:
        """
        Returns the core principles for decision guidance.
        These ensure we maintain humility and avoid false certainty.
        """
        return [
            "❌ Never rank options numerically",
            "❌ Never assign scores or ratings",
            "❌ Never claim certainty about outcomes",
            "❌ Never say 'best decision' or 'optimal choice'",
            "✅ Always explain tradeoffs explicitly",
            "✅ Always state assumptions clearly",
            "✅ Always mention when advice would NOT apply",
            "✅ Always acknowledge what you don't know"
        ]
    
    @staticmethod
    def format_output_template() -> str:
        """
        Returns the exact output structure template.
        """
        return """## Problem Reframing

## Root Cause Analysis
### User
### Product
### Technology
### Process
### External / Market

## Decision Options

## Risk Management

## Suggested Direction (with Caveats)

## Next Steps

## Success Signals
"""
