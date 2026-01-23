"""
UI Components - All visual elements and styling
"""
import streamlit as st
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import re
import io


def apply_custom_css():
    """Apply custom CSS for full-page immersive styling"""
    st.markdown("""
    <style>
        /* Import Premium Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
        
        /* Hide Streamlit Elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}
        
        /* Full Page Layout - No Container */
        .main {
            padding: 0 !important;
            max-width: 100% !important;
        }
        
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        
        /* Animated Header with Gradient Background */
        .hero-header {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 25%, #312e81 50%, #4c1d95 75%, #581c87 100%);
            padding: 3rem 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
            border-bottom: 4px solid;
            border-image: linear-gradient(90deg, #6366f1, #8b5cf6, #d946ef) 1;
        }
        
        .hero-header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.1) 0%, transparent 70%);
            animation: rotate 20s linear infinite;
        }
        
        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .brand-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 0%, #e0e7ff 50%, #c7d2fe 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 0;
            position: relative;
            z-index: 1;
            animation: slideInFromTop 1s cubic-bezier(0.16, 1, 0.3, 1);
            letter-spacing: -0.02em;
        }
        
        @keyframes slideInFromTop {
            0% {
                opacity: 0;
                transform: translateY(-50px) scale(0.9);
            }
            100% {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }
        
        .hero-subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 1.25rem;
            color: #c7d2fe;
            font-weight: 400;
            margin-top: 1rem;
            position: relative;
            z-index: 1;
            animation: slideInFromTop 1.2s cubic-bezier(0.16, 1, 0.3, 1);
        }
        
        .hero-badges {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 1.5rem;
            flex-wrap: wrap;
            position: relative;
            z-index: 1;
            animation: slideInFromTop 1.4s cubic-bezier(0.16, 1, 0.3, 1);
        }
        
        .hero-badge {
            padding: 0.5rem 1.25rem;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 100px;
            color: #e0e7ff;
            font-size: 0.875rem;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.3s ease;
        }
        
        .hero-badge:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-2px);
        }
        
        /* Main Content Area */
        .content-section {
            max-width: 1400px;
            margin: 0 auto;
            padding: 3rem 2rem;
        }
        
        /* Tab Navigation */
        .stTabs {
            background: transparent;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            padding: 1rem;
            border-radius: 16px;
            border: 1px solid #e2e8f0;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: white;
            border-radius: 12px;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            color: #475569;
            border: 2px solid transparent;
            transition: all 0.3s ease;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: #fef3c7;
            border-color: #fbbf24;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
            color: white !important;
            border-color: #6366f1 !important;
        }
        
        /* Section Headers */
        .section-header {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 2rem;
            font-weight: 700;
            color: #1e293b;
            margin: 2rem 0 1.5rem 0;
            padding-bottom: 0.75rem;
            border-bottom: 3px solid;
            border-image: linear-gradient(90deg, #6366f1, #8b5cf6, transparent) 1;
        }
        
        /* Input Areas */
        .stTextArea textarea, .stTextInput input {
            border-radius: 12px !important;
            border: 2px solid #e2e8f0 !important;
            padding: 1rem !important;
            font-size: 1rem !important;
            font-family: 'Inter', sans-serif !important;
            transition: all 0.3s ease;
            background: white;
        }
        
        .stTextArea textarea:focus, .stTextInput input:focus {
            border-color: #6366f1 !important;
            box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.1) !important;
            transform: translateY(-2px);
        }
        
        /* Buttons */
        .stButton button {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.875rem 2rem !important;
            font-weight: 700 !important;
            font-size: 1rem !important;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 0 4px 14px rgba(99, 102, 241, 0.4);
        }
        
        .stButton button:hover {
            transform: translateY(-3px) scale(1.02) !important;
            box-shadow: 0 8px 25px rgba(99, 102, 241, 0.5) !important;
        }
        
        .stDownloadButton button {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
            box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4) !important;
        }
        
        .stDownloadButton button:hover {
            box-shadow: 0 8px 25px rgba(16, 185, 129, 0.5) !important;
        }
        
        /* Response Cards */
        .response-card {
            background: white;
            border-radius: 16px;
            padding: 2.5rem;
            margin: 2rem 0;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid #e2e8f0;
            animation: fadeIn 0.6s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Headers in Response */
        h1, h2, h3 {
            font-family: 'Space Grotesk', sans-serif;
            color: #1e293b;
        }
        
        h2 {
            font-size: 1.75rem;
            font-weight: 700;
            margin-top: 2rem;
            margin-bottom: 1rem;
            color: #6366f1;
        }
        
        h3 {
            font-size: 1.25rem;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }
        
        /* Lists */
        ul, ol {
            line-height: 1.8;
            color: #475569;
        }
        
        li {
            margin-bottom: 0.5rem;
        }
        
        strong {
            color: #1e293b;
            font-weight: 700;
        }
        
        /* Code */
        code {
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            padding: 0.25rem 0.5rem;
            border-radius: 6px;
            color: #6366f1;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9em;
        }
        
        /* Alerts */
        .stAlert {
            border-radius: 12px !important;
            border: none !important;
            padding: 1rem 1.5rem !important;
            font-weight: 500;
        }
        
        /* Success/Warning/Error specific styles */
        [data-testid="stNotification"] {
            border-radius: 12px;
        }
        
        /* Metrics/KPI Cards */
        .kpi-card {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            border-radius: 16px;
            padding: 1.5rem;
            border: 2px solid #e2e8f0;
            transition: all 0.3s ease;
            height: 100%;
        }
        
        .kpi-card:hover {
            border-color: #6366f1;
            box-shadow: 0 8px 24px rgba(99, 102, 241, 0.15);
            transform: translateY(-4px);
        }
        
        .kpi-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 0.875rem;
            font-weight: 600;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.5rem;
        }
        
        .kpi-value {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .kpi-change {
            font-size: 0.875rem;
            font-weight: 600;
            margin-top: 0.5rem;
        }
        
        .kpi-positive {
            color: #10b981;
        }
        
        .kpi-negative {
            color: #ef4444;
        }
        
        /* Footer */
        .app-footer {
            text-align: center;
            padding: 3rem 2rem;
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            border-top: 2px solid #e2e8f0;
            margin-top: 4rem;
        }
        
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 12px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
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


def render_analyze_button():
    """Render the analyze button"""
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    analyze = st.button("🚀 Analyze", use_container_width=True, type="primary")
    st.markdown('</div>', unsafe_allow_html=True)
    return analyze


def render_response(response: str):
    """Render the AI response"""
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown("### 🎯 Strategic Analysis")
    st.markdown(response)
    st.markdown('</div>', unsafe_allow_html=True)


def generate_pdf(analysis_text: str, context: str = "") -> bytes:
    """Generate PDF from analysis"""
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
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
        textColor='#6366f1',
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


def render_pdf_download_button(pdf_bytes: bytes, filename: str = "product_analysis.pdf"):
    """Render PDF download button"""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.download_button(
        label="📥 Download Analysis as PDF",
        data=pdf_bytes,
        file_name=f"{filename}_{timestamp}.pdf",
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
            font-weight: 600;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
            animation: pulse 2s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        /* Premium Input Section */
        .input-wrapper {
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            border-radius: 24px;
            padding: 2.5rem;
            margin: 2rem 0;
            border: 2px solid #e2e8f0;
            box-shadow: 
                0 10px 25px rgba(0, 0, 0, 0.05),
                inset 0 1px 0 rgba(255, 255, 255, 0.9);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .input-wrapper:hover {
            border-color: #c7d2fe;
            box-shadow: 
                0 20px 40px rgba(99, 102, 241, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.9);
        }
        
        .floating-label {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 600;
            color: #1e293b;
            font-size: 1.1rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        /* Text Area - Premium Input */
        .stTextArea textarea {
            border-radius: 16px !important;
            border: 2px solid #e2e8f0 !important;
            padding: 1.25rem !important;
            font-size: 1.05rem !important;
            line-height: 1.7 !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            background: white;
            font-family: 'Inter', sans-serif !important;
        }
        
        .stTextArea textarea:focus {
            border-color: #6366f1 !important;
            box-shadow: 
                0 0 0 4px rgba(99, 102, 241, 0.1),
                0 8px 24px rgba(99, 102, 241, 0.15) !important;
            transform: translateY(-2px);
            background: white;
        }
        
        .stTextArea textarea::placeholder {
            color: #94a3b8;
            font-style: italic;
        }
        
        /* Premium Buttons */
        .stButton button {
            background: var(--primary-gradient) !important;
            color: white !important;
            border: none !important;
            border-radius: 16px !important;
            padding: 1rem 3rem !important;
            font-weight: 700 !important;
            font-size: 1.1rem !important;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 
                0 10px 30px rgba(99, 102, 241, 0.4),
                0 0 0 0 rgba(99, 102, 241, 0.5);
            position: relative;
            overflow: hidden;
        }
        
        .stButton button::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }
        
        .stButton button:hover::before {
            width: 300px;
            height: 300px;
        }
        
        .stButton button:hover {
            transform: translateY(-4px) scale(1.02) !important;
            box-shadow: 
                0 20px 40px rgba(99, 102, 241, 0.5),
                0 0 0 0 rgba(99, 102, 241, 0.7) !important;
        }
        
        .stButton button:active {
            transform: translateY(-2px) scale(0.98) !important;
        }
        
        /* Download Button - Different Style */
        .stDownloadButton button {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
            box-shadow: 0 10px 30px rgba(16, 185, 129, 0.4) !important;
        }
        
        .stDownloadButton button:hover {
            box-shadow: 0 20px 40px rgba(16, 185, 129, 0.5) !important;
        }
        
        /* Success/Warning/Error Messages - Premium Style */
        .stAlert {
            border-radius: 16px !important;
            border: none !important;
            padding: 1.25rem 1.75rem !important;
            animation: slideInLeft 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
            font-weight: 500;
        }
        
        @keyframes slideInLeft {
            from { 
                opacity: 0; 
                transform: translateX(-30px);
            }
            to { 
                opacity: 1; 
                transform: translateX(0);
            }
        }
        
        .element-container:has(> .stAlert[data-baseweb="notification"][kind="success"]) .stAlert {
            background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
            color: #065f46;
            border-left: 4px solid #10b981 !important;
        }
        
        .element-container:has(> .stAlert[data-baseweb="notification"][kind="warning"]) .stAlert {
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
            color: #92400e;
            border-left: 4px solid #f59e0b !important;
        }
        
        .element-container:has(> .stAlert[data-baseweb="notification"][kind="error"]) .stAlert {
            background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
            color: #991b1b;
            border-left: 4px solid #ef4444 !important;
        }
        
        /* Response Container - Premium Card */
        .response-card {
            background: white;
            border-radius: 24px;
            padding: 3rem;
            margin: 2rem 0;
            box-shadow: 
                0 20px 40px rgba(0, 0, 0, 0.08),
                0 0 0 1px rgba(0, 0, 0, 0.05);
            animation: fadeInContent 0.6s cubic-bezier(0.16, 1, 0.3, 1);
            border: 2px solid #f1f5f9;
        }
        
        @keyframes fadeInContent {
            from { 
                opacity: 0;
                transform: translateY(20px);
            }
            to { 
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Lists - Premium Style */
        ul, ol {
            line-height: 1.9;
            color: #475569;
            margin-left: 1.5rem;
        }
        
        li {
            margin-bottom: 0.75rem;
            padding-left: 0.5rem;
        }
        
        li::marker {
            color: #6366f1;
            font-weight: 600;
        }
        
        /* Strong/Bold Text */
        strong {
            color: #1e293b;
            font-weight: 700;
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 50%);
            padding: 0.1rem 0.3rem;
            border-radius: 4px;
        }
        
        /* Code Blocks - Premium */
        code {
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            padding: 0.3rem 0.6rem;
            border-radius: 8px;
            color: #6366f1;
            font-size: 0.95em;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 500;
            border: 1px solid #e2e8f0;
        }
        
        /* Divider */
        hr {
            margin: 3rem 0;
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, #e2e8f0 20%, #e2e8f0 80%, transparent);
        }
        
        /* Premium Scrollbar */
        ::-webkit-scrollbar {
            width: 12px;
            height: 12px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: var(--primary-gradient);
            border-radius: 10px;
            border: 2px solid #f1f5f9;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        }
        
        /* Loading Spinner */
        .stSpinner > div {
            border-top-color: #6366f1 !important;
            border-right-color: #8b5cf6 !important;
        }
        
        /* Metrics/Stats Cards */
        .metric-card {
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            border-radius: 16px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-left: 4px solid #6366f1;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        
        .metric-card:hover {
            transform: translateX(8px);
            box-shadow: 0 8px 24px rgba(99, 102, 241, 0.15);
        }
        
        /* Paragraph Styling */
        p {
            line-height: 1.8;
            color: #475569;
            margin-bottom: 1.25rem;
        }
        
        /* Blockquote */
        blockquote {
            border-left: 4px solid #6366f1;
            padding-left: 1.5rem;
            margin-left: 0;
            font-style: italic;
            color: #64748b;
            background: #f8fafc;
            padding: 1rem 1.5rem;
            border-radius: 0 12px 12px 0;
        }
        
        /* Table Styling */
        table {
            border-collapse: separate;
            border-spacing: 0;
            width: 100%;
            margin: 2rem 0;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }
        
        th {
            background: var(--primary-gradient);
            color: white;
            padding: 1rem;
            font-weight: 600;
            text-align: left;
        }
        
        td {
            padding: 1rem;
            border-bottom: 1px solid #e2e8f0;
            color: #475569;
        }
        
        tr:last-child td {
            border-bottom: none;
        }
        
        tr:hover {
            background: #f8fafc;
        }
        
        /* Footer Styling */
        .footer-premium {
            text-align: center;
            padding: 3rem 0 2rem 0;
            margin-top: 4rem;
            border-top: 2px solid #e2e8f0;
            color: #64748b;
        }
        
        .footer-premium strong {
            background: none;
            color: #6366f1;
            font-weight: 700;
        }
        
        /* Emoji Enhancements */
        .emoji {
            font-size: 1.5em;
            vertical-align: middle;
            display: inline-block;
            animation: bounce 2s ease-in-out infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-5px); }
        }
    </style>
    """, unsafe_allow_html=True)


def render_header():
    """Render the animated hero header"""
    st.markdown("""
    <div class='hero-header'>
        <h1 class='brand-title'>🚀 Product Playground</h1>
        <p class='hero-subtitle'>AI-Powered Decision Intelligence for Product Leaders</p>
        <div class='hero-badges'>
            <span class='hero-badge'>✨ GPT-4 Powered</span>
            <span class='hero-badge'>🧠 Strategic Analysis</span>
            <span class='hero-badge'>📊 KPI Diagnostics</span>
            <span class='hero-badge'>📥 PDF Export</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_input_section():
    """Render the input section for product challenge"""
    st.markdown("<div class='content-section'>", unsafe_allow_html=True)
    
    user_context = st.text_area(
        "📝 Describe Your Product Challenge",
        height=200,
        placeholder="Example: Our mobile app's DAU dropped 18% over the past 3 weeks after we launched a new personalized home feed powered by ML. The algorithm is working as designed, but session times decreased from 12 mins to 8 mins average. PM lead wants to roll back immediately. Engineering says rollback takes 2 weeks. Marketing already announced this as our flagship feature. What should we do?",
        key="context_input"
    )
    
    st.markdown("</div>", unsafe_allow_html=True)
    return user_context


def render_dashboard_input():
    """Render dashboard KPI input section"""
    st.markdown("<div class='content-section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-header'>📊 Enter Your Dashboard Metrics</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        dau = st.number_input("Daily Active Users (DAU)", min_value=0, value=0, key="dau")
        mau = st.number_input("Monthly Active Users (MAU)", min_value=0, value=0, key="mau")
        conversion_rate = st.number_input("Conversion Rate (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="conversion")
        churn_rate = st.number_input("Churn Rate (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="churn")
    
    with col2:
        avg_session_time = st.number_input("Avg Session Time (mins)", min_value=0.0, value=0.0, step=0.1, key="session_time")
        retention_rate = st.number_input("7-Day Retention (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="retention")
        nps_score = st.number_input("NPS Score", min_value=-100, max_value=100, value=0, key="nps")
        revenue_per_user = st.number_input("ARPU ($)", min_value=0.0, value=0.0, step=0.01, key="arpu")
    
    # Add context about changes
    st.markdown("### 📈 Recent Changes (Optional)")
    recent_changes = st.text_area(
        "Describe any recent product changes or events",
        height=100,
        placeholder="E.g., Launched new feature X 2 weeks ago, ran marketing campaign, changed pricing...",
        key="dashboard_context"
    )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    return {
        'dau': dau,
        'mau': mau,
        'conversion_rate': conversion_rate,
        'churn_rate': churn_rate,
        'avg_session_time': avg_session_time,
        'retention_rate': retention_rate,
        'nps_score': nps_score,
        'revenue_per_user': revenue_per_user,
        'recent_changes': recent_changes
    }


def display_kpi_cards(kpi_data):
    """Display KPI data in card format"""
    st.markdown("<div class='content-section'>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-title'>Daily Active Users</div>
            <div class='kpi-value'>{kpi_data['dau']:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-title'>Conversion Rate</div>
            <div class='kpi-value'>{kpi_data['conversion_rate']}%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-title'>Retention Rate</div>
            <div class='kpi-value'>{kpi_data['retention_rate']}%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-title'>NPS Score</div>
            <div class='kpi-value'>{kpi_data['nps_score']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)


def render_analyze_button():
    """Render the analyze button"""
    st.markdown("<div class='content-section'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        result = st.button("✨ Analyze & Get Insights", use_container_width=True, type="primary")
    st.markdown("</div>", unsafe_allow_html=True)
    return result


def render_response(response_text, user_context=""):
    """Render the AI response"""
    st.markdown("<div class='content-section'>", unsafe_allow_html=True)
    st.markdown("<div class='response-card'>", unsafe_allow_html=True)
    st.markdown(response_text)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Store in session state for PDF export
    if 'last_analysis' not in st.session_state:
        st.session_state.last_analysis = {}
    
    st.session_state.last_analysis = {
        'context': user_context,
        'response': response_text,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def generate_pdf(context, response, timestamp):
    """Generate a professional PDF report of the analysis"""
    buffer = io.BytesIO()
    
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=1*inch,
        bottomMargin=0.75*inch
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor('#6366f1'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#64748b'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=20,
        spaceAfter=12,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#475569'),
        spaceAfter=12,
        leading=16,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    context_style = ParagraphStyle(
        'ContextBox',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#334155'),
        leftIndent=20,
        rightIndent=20,
        spaceAfter=20,
        spaceBefore=10,
        leading=14,
        fontName='Helvetica-Oblique',
        backColor=colors.HexColor('#f8fafc')
    )
    
    story.append(Paragraph("🚀 Product Playground", title_style))
    story.append(Paragraph(f"Strategic Analysis Report · Generated on {timestamp}", subtitle_style))
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("Product Challenge", heading_style))
    story.append(Paragraph(context.replace('\n', '<br/>'), context_style))
    story.append(Spacer(1, 0.2*inch))
    
    lines = response.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            story.append(Spacer(1, 0.1*inch))
            continue
        
        if line.startswith('## '):
            header_text = line.replace('##', '').strip()
            story.append(Spacer(1, 0.15*inch))
            story.append(Paragraph(header_text, heading_style))
        elif line.startswith('### '):
            subheader_text = line.replace('###', '').strip()
            sub_style = ParagraphStyle(
                'SubHeading',
                parent=heading_style,
                fontSize=13,
                textColor=colors.HexColor('#334155')
            )
            story.append(Paragraph(subheader_text, sub_style))
        elif line.startswith('**') and line.endswith('**'):
            bold_text = line.replace('**', '').strip()
            bold_style = ParagraphStyle(
                'BoldText',
                parent=body_style,
                fontName='Helvetica-Bold',
                textColor=colors.HexColor('#1e293b')
            )
            story.append(Paragraph(bold_text, bold_style))
        elif line.startswith('- '):
            list_text = '• ' + line[2:].strip()
            list_style = ParagraphStyle(
                'ListItem',
                parent=body_style,
                leftIndent=20,
                bulletIndent=10
            )
            story.append(Paragraph(list_text, list_style))
        elif line.startswith('---'):
            story.append(Spacer(1, 0.1*inch))
        else:
            clean_line = line.replace('**', '<b>').replace('**', '</b>')
            clean_line = clean_line.replace('*', '<i>').replace('*', '</i>')
            story.append(Paragraph(clean_line, body_style))
    
    story.append(Spacer(1, 0.5*inch))
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#94a3b8'),
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )
    story.append(Paragraph("Generated by Product Playground · AI-Powered Strategic Analysis", footer_style))
    story.append(Paragraph("This analysis is provided for strategic guidance and should be validated with additional research.", footer_style))
    
    doc.build(story)
    
    pdf_data = buffer.getvalue()
    buffer.close()
    
    return pdf_data


def render_pdf_download_button(context, response, timestamp):
    """Render the PDF download button"""
    if context and response:
        pdf_data = generate_pdf(context, response, timestamp)
        
        filename = f"product_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        
        st.markdown("<div class='content-section'>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="📥 Download Analysis as PDF",
                data=pdf_data,
                file_name=filename,
                mime="application/pdf",
                use_container_width=True,
                key=f"pdf_download_{timestamp}"
            )
        st.markdown("</div>", unsafe_allow_html=True)


def render_footer():
    """Render footer"""
    st.markdown("""
    <div class='app-footer'>
        <p style='font-size: 1rem; color: #475569; margin-bottom: 0.5rem;'>
            💡 <strong>Pro Tip:</strong> The more context and metrics you provide, the more actionable and specific the analysis will be.
        </p>
        <p style='font-size: 0.875rem; color: #94a3b8;'>
            Built with ❤️ for Product Managers · Powered by OpenAI GPT-4
        </p>
    </div>
    """, unsafe_allow_html=True)
    """Generate a professional PDF report of the analysis"""
    buffer = io.BytesIO()
    
    # Create PDF document
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=1*inch,
        bottomMargin=0.75*inch
    )
    
    # Container for PDF elements
    story = []
    
    # Define custom styles
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor('#6366f1'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Subtitle style
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#64748b'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    # Heading style
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=20,
        spaceAfter=12,
        fontName='Helvetica-Bold'
    )
    
    # Body style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#475569'),
        spaceAfter=12,
        leading=16,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    # Context box style
    context_style = ParagraphStyle(
        'ContextBox',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#334155'),
        leftIndent=20,
        rightIndent=20,
        spaceAfter=20,
        spaceBefore=10,
        leading=14,
        fontName='Helvetica-Oblique',
        backColor=colors.HexColor('#f8fafc')
    )
    
    # Add header
    story.append(Paragraph("🚀 Product Thinking Studio", title_style))
    story.append(Paragraph(f"Strategic Analysis Report · Generated on {timestamp}", subtitle_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Add context section
    story.append(Paragraph("Product Challenge", heading_style))
    story.append(Paragraph(context.replace('\n', '<br/>'), context_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Add horizontal line
    story.append(Paragraph("<hr/>", body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Parse and add response content
    lines = response.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            story.append(Spacer(1, 0.1*inch))
            continue
        
        # Handle headers (##)
        if line.startswith('## '):
            header_text = line.replace('##', '').strip()
            story.append(Spacer(1, 0.15*inch))
            story.append(Paragraph(header_text, heading_style))
        
        # Handle sub-headers (###)
        elif line.startswith('### '):
            subheader_text = line.replace('###', '').strip()
            sub_style = ParagraphStyle(
                'SubHeading',
                parent=heading_style,
                fontSize=13,
                textColor=colors.HexColor('#334155')
            )
            story.append(Paragraph(subheader_text, sub_style))
        
        # Handle bold (**text**)
        elif line.startswith('**') and line.endswith('**'):
            bold_text = line.replace('**', '').strip()
            bold_style = ParagraphStyle(
                'BoldText',
                parent=body_style,
                fontName='Helvetica-Bold',
                textColor=colors.HexColor('#1e293b')
            )
            story.append(Paragraph(bold_text, bold_style))
        
        # Handle list items (-)
        elif line.startswith('- '):
            list_text = '• ' + line[2:].strip()
            list_style = ParagraphStyle(
                'ListItem',
                parent=body_style,
                leftIndent=20,
                bulletIndent=10
            )
            story.append(Paragraph(list_text, list_style))
        
        # Handle horizontal rules
        elif line.startswith('---'):
            story.append(Spacer(1, 0.1*inch))
            story.append(Paragraph("<hr/>", body_style))
            story.append(Spacer(1, 0.1*inch))
        
        # Regular paragraph
        else:
            # Clean up markdown formatting
            clean_line = line.replace('**', '<b>').replace('**', '</b>')
            clean_line = clean_line.replace('*', '<i>').replace('*', '</i>')
            story.append(Paragraph(clean_line, body_style))
    
    # Add footer
    story.append(Spacer(1, 0.5*inch))
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#94a3b8'),
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )
    story.append(Paragraph("Generated by Product Thinking Studio · AI-Powered Strategic Analysis", footer_style))
    story.append(Paragraph("This analysis is provided for strategic guidance and should be validated with additional research.", footer_style))
    
    # Build PDF
    doc.build(story)
    
    # Get PDF data
    pdf_data = buffer.getvalue()
    buffer.close()
    
    return pdf_data


def render_pdf_download_button(context, response, timestamp):
    """Render the premium PDF download button"""
    if context and response:
        pdf_data = generate_pdf(context, response, timestamp)
        
        filename = f"product_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="📥 Download Analysis as PDF",
                data=pdf_data,
                file_name=filename,
                mime="application/pdf",
                use_container_width=True,
                type="secondary"
            )


def render_footer():
    """Render premium footer with helpful tips"""
    st.markdown("""
    <div class='footer-premium'>
        <hr>
        <p style='font-size: 1rem; margin-top: 2rem;'>
            💡 <strong>Pro Tip:</strong> The more context you provide (metrics, constraints, stakeholders), 
            the more actionable and specific the analysis will be.
        </p>
        <p style='font-size: 0.9rem; color: #94a3b8; margin-top: 1rem;'>
            Built with ❤️ for Product Managers · Powered by OpenAI GPT-4
        </p>
    </div>
    """, unsafe_allow_html=True)
