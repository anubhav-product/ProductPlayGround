"""
UI ONLY - Product Playground Interface
All visual components and styling
"""
import streamlit as st
from datetime import datetime


def apply_custom_css():
    """Apply custom CSS for full-page immersive experience"""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
        
        /* Global Variables */
        :root {
            --primary-gradient: linear-gradient(135deg, #3b82f6 0%, #60a5fa 50%, #93c5fd 100%);
            --accent-gradient: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%);
            --success-gradient: linear-gradient(135deg, #10b981 0%, #059669 100%);
        }
        
        /* Full Page Layout - Remove Container */
        .main, .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        
        /* Hero Header with Animation */
        .hero-header {
            background: var(--primary-gradient);
            padding: 4rem 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
            animation: gradientShift 8s ease infinite;
            background-size: 200% 200%;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .brand-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 3.5rem;
            font-weight: 700;
            color: white;
            margin: 0;
            text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            animation: fadeInDown 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }
        
        .hero-subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 1.3rem;
            color: rgba(255, 255, 255, 0.9);
            margin-top: 1rem;
            animation: fadeIn 1s ease 0.3s both;
        }
        
        .hero-badges {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 2rem;
            flex-wrap: wrap;
            animation: fadeIn 1s ease 0.6s both;
        }
        
        .badge {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            padding: 0.5rem 1.5rem;
            border-radius: 50px;
            color: white;
            font-weight: 600;
            font-size: 0.9rem;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        /* Content Sections */
        .content-section {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
        }
        
        /* Tab Styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
            background: linear-gradient(to bottom, #f8fafc, white);
            padding: 2rem 2rem 0;
            border-bottom: 2px solid #e2e8f0;
        }
        
        .stTabs [data-baseweb="tab"] {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 600;
            font-size: 1.1rem;
            padding: 1rem 2rem;
            color: #64748b;
            border-radius: 12px 12px 0 0;
            transition: all 0.3s ease;
        }
        
        .stTabs [aria-selected="true"] {
            background: white;
            color: #3b82f6;
            box-shadow: 0 -4px 12px rgba(59, 130, 246, 0.1);
        }
        
        /* KPI Cards */
        .kpi-card {
            background: linear-gradient(135deg, #f8fafc 0%, white 100%);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            border: 2px solid #e2e8f0;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }
        
        .kpi-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 24px rgba(59, 130, 246, 0.15);
            border-color: #bfdbfe;
        }
        
        .kpi-value {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 2rem;
            font-weight: 700;
            color: #3b82f6;
            margin: 0.5rem 0;
        }
        
        .kpi-title {
            font-family: 'Inter', sans-serif;
            font-size: 0.85rem;
            color: #64748b;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* App Footer */
        .app-footer {
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            color: white;
            padding: 3rem 2rem;
            margin-top: 4rem;
            text-align: center;
        }
        
        .app-footer p {
            color: rgba(255, 255, 255, 0.8);
            margin: 0.5rem 0;
        }
        
        /* Input Styling */
        .stTextArea textarea, .stNumberInput input {
            border-radius: 12px !important;
            border: 2px solid #e2e8f0 !important;
            padding: 1rem !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 1rem !important;
            transition: all 0.3s ease;
        }
        
        .stTextArea textarea:focus, .stNumberInput input:focus {
            border-color: #3b82f6 !important;
            box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1) !important;
        }
        
        /* Button Styling */
        .stButton button {
            background: var(--primary-gradient) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.75rem 2rem !important;
            font-weight: 700 !important;
            font-size: 1.1rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
        }
        
        .stButton button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 15px 35px rgba(59, 130, 246, 0.4) !important;
        }
        
        .stDownloadButton button {
            background: var(--success-gradient) !important;
            box-shadow: 0 10px 25px rgba(16, 185, 129, 0.3) !important;
        }
        
        /* Typography */
        h1, h2, h3 {
            font-family: 'Space Grotesk', sans-serif !important;
            color: #1e293b !important;
        }
        
        p, li {
            font-family: 'Inter', sans-serif !important;
            line-height: 1.7 !important;
            color: #475569 !important;
        }
        
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
        }
    </style>
    """, unsafe_allow_html=True)


def render_header():
    """Render the animated hero header"""
    st.markdown("""
        <div class="hero-header">
            <div class="brand-title">Product Playground</div>
            <div class="hero-subtitle">AI-Powered Product Strategy & Analytics Platform</div>
            <div class="hero-badges">
                <span class="badge">💡 Strategic Analysis</span>
                <span class="badge">📊 KPI Diagnostics</span>
                <span class="badge">🚀 Data-Driven Insights</span>
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_input_section():
    """Render the product challenge input section"""
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown("### 💡 Describe Your Product Challenge")
    
    product_context = st.text_area(
        "What product decision or situation are you facing?",
        height=200,
        placeholder="Example: Our DAU dropped 15% after launching a new onboarding flow. Users are completing the first 2 steps but dropping off at step 3 (payment info). Our team is split between simplifying the form vs adding more social proof. What should we prioritize?",
        key="product_challenge_input"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    return product_context


def render_dashboard_input():
    """Render the dashboard KPI input section"""
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown("### 📊 Enter Your Dashboard Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Engagement Metrics")
        dau = st.number_input("Daily Active Users (DAU)", min_value=0, value=0, step=1000)
        mau = st.number_input("Monthly Active Users (MAU)", min_value=0, value=0, step=1000)
        avg_session_time = st.number_input("Avg Session Time (minutes)", min_value=0.0, value=0.0, step=0.5)
        
        st.markdown("#### Conversion & Retention")
        conversion_rate = st.number_input("Conversion Rate (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
        retention_rate = st.number_input("7-Day Retention Rate (%)", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
    
    with col2:
        st.markdown("#### User Satisfaction & Revenue")
        churn_rate = st.number_input("Churn Rate (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
        nps_score = st.number_input("NPS Score", min_value=-100, max_value=100, value=0, step=1)
        revenue_per_user = st.number_input("Revenue Per User ($)", min_value=0.0, value=0.0, step=0.01)
    
    st.markdown("#### Recent Changes (Optional)")
    recent_changes = st.text_area(
        "Any recent product changes, launches, or context?",
        height=100,
        placeholder="Example: Launched new UI redesign 6 weeks ago, added AI features last month, changed pricing model..."
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    return {
        'dau': dau,
        'mau': mau,
        'avg_session_time': avg_session_time,
        'conversion_rate': conversion_rate,
        'churn_rate': churn_rate,
        'retention_rate': retention_rate,
        'nps_score': nps_score,
        'revenue_per_user': revenue_per_user,
        'recent_changes': recent_changes
    }


def display_kpi_cards(kpi_data):
    """Display KPI metrics in visual cards"""
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown("### 📈 Your Dashboard Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        dau_mau_ratio = (kpi_data['dau'] / kpi_data['mau'] * 100) if kpi_data['mau'] > 0 else 0
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">DAU/MAU Ratio</div>
                <div class="kpi-value">{dau_mau_ratio:.1f}%</div>
                <div class="kpi-title">Stickiness</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Conversion Rate</div>
                <div class="kpi-value">{kpi_data['conversion_rate']:.1f}%</div>
                <div class="kpi-title">Trial to Paid</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Retention (7-Day)</div>
                <div class="kpi-value">{kpi_data['retention_rate']:.0f}%</div>
                <div class="kpi-title">User Return Rate</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">NPS Score</div>
                <div class="kpi-value">{kpi_data['nps_score']}</div>
                <div class="kpi-title">Satisfaction</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_analyze_button(button_key="analyze"):
    """Render the analyze button"""
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    analyze = st.button("🚀 Analyze", use_container_width=True, type="primary", key=button_key)
    st.markdown('</div>', unsafe_allow_html=True)
    return analyze


def render_response(response: str, context: str = ""):
    """Render the AI response and store in session state"""
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown("### 🎯 Strategic Analysis")
    st.markdown(response)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Store in session state for PDF generation
    st.session_state.last_analysis = {
        'response': response,
        'context': context,
        'timestamp': datetime.now().strftime("%Y%m%d_%H%M%S")
    }


def generate_pdf(analysis_text: str, context: str = "") -> bytes:
    """Generate PDF from analysis"""
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.enums import TA_CENTER
    from io import BytesIO
    import markdown2
    
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                          rightMargin=72, leftMargin=72,
                          topMargin=72, bottomMargin=18)
    
    elements = []
    styles = getSampleStyleSheet()
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='#3b82f6',
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    elements.append(Paragraph("Product Playground", title_style))
    elements.append(Paragraph("Strategic Analysis Report", styles['Heading2']))
    elements.append(Spacer(1, 0.3*inch))
    
    # Context if provided
    if context:
        elements.append(Paragraph("Product Challenge:", styles['Heading3']))
        elements.append(Paragraph(context, styles['BodyText']))
        elements.append(Spacer(1, 0.2*inch))
    
    # Analysis
    elements.append(Paragraph("Analysis:", styles['Heading3']))
    
    # Convert markdown to HTML and then to PDF
    html_content = markdown2.markdown(analysis_text)
    
    # Split by paragraphs and add them
    for paragraph in html_content.split('\n'):
        if paragraph.strip():
            try:
                elements.append(Paragraph(paragraph, styles['BodyText']))
                elements.append(Spacer(1, 0.1*inch))
            except:
                pass
    
    doc.build(elements)
    buffer.seek(0)
    return buffer.getvalue()


def render_pdf_download_button(context: str = "", response: str = "", timestamp: str = ""):
    """Render PDF download button"""
    if not response:
        return
    
    pdf_bytes = generate_pdf(response, context)
    
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.download_button(
        label="📥 Download Analysis as PDF",
        data=pdf_bytes,
        file_name=f"product_analysis_{timestamp}.pdf",
        mime="application/pdf",
        use_container_width=True,
        key=f"pdf_download_{timestamp}"
    )
    st.markdown('</div>', unsafe_allow_html=True)


def render_footer():
    """Render footer with tips"""
    st.markdown("""
        <div class="app-footer">
            <p><strong>💡 Pro Tips:</strong></p>
            <p>• Be specific about metrics and context for better insights</p>
            <p>• Include timeframes and recent changes</p>
            <p>• Describe competing options and constraints</p>
        </div>
    """, unsafe_allow_html=True)
