"""
Product Thinking Studio - Streamlit UI

A decision-support application for Product Managers to reason through
ambiguous product decisions with structured frameworks.

NOT a recommendation engine. NOT an optimization tool. NOT a scoring system.
"""

import streamlit as st
from decision_support import DecisionSupportEngine


def main():
    """Main application entry point."""
    
    # Page configuration
    st.set_page_config(
        page_title="Product Thinking Studio",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for better readability
    st.markdown("""
        <style>
        .main-header {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .sub-header {
            font-size: 1.2rem;
            color: #666;
            margin-bottom: 2rem;
        }
        .principle {
            padding: 0.5rem;
            margin: 0.25rem 0;
            border-radius: 4px;
        }
        .warning-box {
            padding: 1rem;
            background-color: #fff3cd;
            border-left: 4px solid #ffc107;
            margin: 1rem 0;
        }
        .info-box {
            padding: 1rem;
            background-color: #d1ecf1;
            border-left: 4px solid #17a2b8;
            margin: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<div class="main-header">🎯 Product Thinking Studio</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Support for reasoning through ambiguous product decisions</div>', unsafe_allow_html=True)
    
    # Sidebar with principles and guidance
    with st.sidebar:
        st.markdown("## 📋 Product Philosophy")
        st.markdown("""
        This tool prioritizes:
        - **Judgment** over automation
        - **Explainability** over precision
        - **Trust** over optimization
        - **Guidance** over decisions
        """)
        
        st.markdown("---")
        st.markdown("## 🎯 Decision Guidance Principles")
        principles = DecisionSupportEngine.get_guidance_principles()
        for principle in principles:
            st.markdown(f"{principle}")
        
        st.markdown("---")
        st.markdown("## 📚 Frameworks")
        
        with st.expander("Root Cause Analysis (RCA)"):
            st.markdown("Every analysis must consider:")
            for dim in DecisionSupportEngine.RCA_DIMENSIONS:
                st.markdown(f"- {dim}")
        
        with st.expander("Risk Management"):
            st.markdown("For each option, analyze:")
            for cat in DecisionSupportEngine.RISK_CATEGORIES:
                st.markdown(f"- {cat}")
            st.markdown("\nEach risk needs:")
            st.markdown("- Likelihood (Low/Medium/High)")
            st.markdown("- Impact (Low/Medium/High)")
            st.markdown("- Mitigation (concrete action)")
    
    # Main content area
    st.markdown("---")
    
    # Warning box
    st.markdown("""
        <div class="warning-box">
            <strong>⚠️ Important:</strong> This is NOT a recommendation engine. 
            It won't tell you what to do. It helps you think through decisions systematically.
        </div>
    """, unsafe_allow_html=True)
    
    # Problem statement input
    st.markdown("## 1️⃣ Describe Your Product Decision")
    st.markdown("What product decision or challenge are you facing?")
    
    problem_statement = st.text_area(
        "Problem Statement",
        height=150,
        placeholder="Example: Should we build a mobile app or improve our mobile web experience? We have limited resources and our mobile traffic is growing 30% QoQ, but most users still access from desktop...",
        label_visibility="collapsed"
    )
    
    if problem_statement:
        # Generate analysis prompt
        st.markdown("---")
        st.markdown("## 2️⃣ Analysis Framework")
        
        st.markdown("""
            <div class="info-box">
                <strong>💡 How to use this framework:</strong><br>
                Work through each section systematically. The framework helps you explore the problem space
                and consider multiple dimensions before making a decision.
            </div>
        """, unsafe_allow_html=True)
        
        # Tabs for different sections
        tab1, tab2, tab3 = st.tabs(["📝 Framework Guide", "📋 Output Template", "✍️ Working Space"])
        
        with tab1:
            st.markdown("### Structured Analysis Framework")
            prompt = DecisionSupportEngine.generate_analysis_prompt(problem_statement)
            st.markdown(prompt)
            
            if st.button("📋 Copy Framework to Clipboard"):
                st.code(prompt, language="markdown")
        
        with tab2:
            st.markdown("### Expected Output Structure")
            st.markdown("Your analysis should follow this exact structure:")
            template = DecisionSupportEngine.format_output_template()
            st.code(template, language="markdown")
        
        with tab3:
            st.markdown("### Your Analysis")
            st.markdown("Use this space to work through your analysis following the framework:")
            
            # Working space with sections
            user_analysis = st.text_area(
                "Complete Analysis",
                height=600,
                placeholder=DecisionSupportEngine.format_output_template(),
                help="Follow the output structure template. Work through each section systematically."
            )
            
            if user_analysis:
                st.markdown("---")
                st.markdown("### 📊 Structure Validation")
                
                validation = DecisionSupportEngine.validate_output_structure(user_analysis)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Required Sections:**")
                    for section, present in validation.items():
                        icon = "✅" if present else "❌"
                        st.markdown(f"{icon} {section}")
                
                with col2:
                    all_present = all(validation.values())
                    if all_present:
                        st.success("✅ All required sections found!")
                    else:
                        missing = [s for s, p in validation.items() if not p]
                        st.warning(f"⚠️ Missing sections: {', '.join(missing)}")
                
                # Download option
                st.markdown("---")
                st.download_button(
                    label="📥 Download Analysis",
                    data=user_analysis,
                    file_name="product_decision_analysis.md",
                    mime="text/markdown"
                )
    
    else:
        st.info("👆 Enter your product decision or challenge above to get started with the analysis framework.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; color: #666; font-size: 0.9rem;">
            <p>Product Thinking Studio • Decision Support for Product Managers</p>
            <p>Clarity > Features • Judgment > Automation • Guidance > Decisions</p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
