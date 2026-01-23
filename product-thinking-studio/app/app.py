"""
Product Playground - Main Application
Entry point that orchestrates UI and logic
"""
import streamlit as st
from prompt import ProductThinkingEngine
from ui import (
    apply_custom_css,
    render_header,
    render_input_section,
    render_dashboard_input,
    display_kpi_cards,
    render_analyze_button,
    render_response,
    render_footer,
    render_pdf_download_button
)


def main():
    """Main application entry point"""
    # Configure page
    st.set_page_config(
        page_title="Product Playground · AI-Powered PM Intelligence",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Apply custom styling
    apply_custom_css()
    
    # Render header
    render_header()
    
    # Create tabs for different analysis types
    tab1, tab2 = st.tabs(["💡 Product Challenge Analysis", "📊 Dashboard KPI Diagnostics"])
    
    with tab1:
        # Product Challenge Analysis
        user_context = render_input_section()
        
        if render_analyze_button(button_key="analyze_challenge"):
            if not user_context.strip():
                st.warning("⚠️ Please describe your product situation to get started.")
            else:
                engine = ProductThinkingEngine()
                
                with st.spinner("🧠 Analyzing your product challenge with AI..."):
                    try:
                        response = engine.analyze(user_context)
                        render_response(response, user_context)
                        st.success("✅ Analysis complete! Review the strategic insights above.")
                        
                        # PDF download button
                        if 'last_analysis' in st.session_state and st.session_state.last_analysis:
                            render_pdf_download_button(
                                st.session_state.last_analysis['context'],
                                st.session_state.last_analysis['response'],
                                st.session_state.last_analysis['timestamp']
                            )
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                        st.info("💡 Make sure your OpenAI API key is set in the .env file.")
        
        # Show previous analysis download
        elif 'last_analysis' in st.session_state and st.session_state.last_analysis.get('context'):
            st.info("💡 Previous analysis available. Enter a new challenge or download your last analysis.")
            render_pdf_download_button(
                st.session_state.last_analysis['context'],
                st.session_state.last_analysis['response'],
                st.session_state.last_analysis['timestamp']
            )
    
    with tab2:
        # Dashboard KPI Analysis
        kpi_data = render_dashboard_input()
        
        # Display KPI cards if any data entered
        if kpi_data['dau'] > 0 or kpi_data['mau'] > 0:
            display_kpi_cards(kpi_data)
        
        if render_analyze_button(button_key="analyze_kpi"):
            if kpi_data['dau'] == 0 and kpi_data['mau'] == 0:
                st.warning("⚠️ Please enter at least some KPI data to analyze.")
            else:
                engine = ProductThinkingEngine()
                
                with st.spinner("🧠 Analyzing your dashboard metrics with AI..."):
                    try:
                        response = engine.analyze_kpis(kpi_data)
                        render_response(response, f"Dashboard KPI Analysis: {kpi_data}")
                        st.success("✅ KPI analysis complete! Review the diagnostic insights above.")
                        
                        # PDF download button
                        if 'last_analysis' in st.session_state and st.session_state.last_analysis:
                            render_pdf_download_button(
                                st.session_state.last_analysis['context'],
                                st.session_state.last_analysis['response'],
                                st.session_state.last_analysis['timestamp']
                            )
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                        st.info("💡 Make sure your OpenAI API key is set in the .env file.")
    
    # Render footer
    render_footer()


if __name__ == "__main__":
    main()
