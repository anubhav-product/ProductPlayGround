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
    """Apply custom CSS for professional styling with animations"""
    st.markdown("""
    <style>
        /* Import Google Fonts - Premium Typography */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
        
        /* Root Variables */
        :root {
            --primary-gradient: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #d946ef 100%);
            --secondary-gradient: linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%);
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --error-color: #ef4444;
            --dark-bg: #0f172a;
            --light-bg: #f8fafc;
        }
        
        /* Global Styles */
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            letter-spacing: -0.01em;
        }
        
        /* Hide Streamlit Elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}
        
        /* Main Background - Sophisticated Gradient */
        .main {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
            padding: 0;
            min-height: 100vh;
        }
        
        /* Premium Glass Card Container */
        .block-container {
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(20px);
            border-radius: 32px;
            padding: 4rem 3.5rem !important;
            box-shadow: 
                0 25px 50px -12px rgba(0, 0, 0, 0.25),
                0 0 0 1px rgba(255, 255, 255, 0.1),
                inset 0 1px 0 0 rgba(255, 255, 255, 0.9);
            max-width: 1400px;
            margin: 3rem auto !important;
            animation: slideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
        }
        
        .block-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: var(--primary-gradient);
            border-radius: 32px 32px 0 0;
        }
        
        @keyframes slideUp {
            from { 
                opacity: 0; 
                transform: translateY(40px) scale(0.98);
            }
            to { 
                opacity: 1; 
                transform: translateY(0) scale(1);
            }
        }
        
        /* Premium Typography */
        h1 {
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 700 !important;
            font-size: 4rem !important;
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem !important;
            line-height: 1.1 !important;
            animation: fadeInDown 0.8s cubic-bezier(0.16, 1, 0.3, 1);
            text-align: center;
        }
        
        @keyframes fadeInDown {
            from { 
                opacity: 0; 
                transform: translateY(-30px);
            }
            to { 
                opacity: 1; 
                transform: translateY(0);
            }
        }
        
        h2 {
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 600 !important;
            color: #1e293b !important;
            font-size: 2rem !important;
            margin-top: 3rem !important;
            margin-bottom: 1.5rem !important;
            padding-bottom: 1rem;
            border-bottom: 3px solid;
            border-image: var(--primary-gradient) 1;
            display: inline-block;
            width: 100%;
        }
        
        h3 {
            font-family: 'Inter', sans-serif !important;
            font-weight: 700 !important;
            color: #334155 !important;
            font-size: 1.4rem !important;
            margin-top: 2rem !important;
            margin-bottom: 1rem !important;
        }
        
        /* Subtitle with Premium Badge */
        .subtitle {
            font-size: 1.25rem;
            color: #64748b;
            font-weight: 500;
            margin-bottom: 3rem;
            text-align: center;
            animation: fadeInDown 1s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
        }
        
        .badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            background: var(--primary-gradient);
            color: white;
            border-radius: 100px;
            font-size: 0.875rem;
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
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem !important;
            animation: slideDown 0.8s ease-out;
        }
        
        @keyframes slideDown {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        h2 {
            font-family: 'Poppins', sans-serif !important;
            font-weight: 600 !important;
            color: #2d3748 !important;
            font-size: 1.8rem !important;
            margin-top: 2rem !important;
            padding-bottom: 0.5rem;
            border-bottom: 3px solid #667eea;
            display: inline-block;
        }
        
        h3 {
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            color: #4a5568 !important;
            font-size: 1.3rem !important;
            margin-top: 1.5rem !important;
        }
        
        /* Subtitle/Caption */
        .subtitle {
            font-size: 1.1rem;
            color: #718096;
            font-weight: 400;
            margin-bottom: 2.5rem;
            animation: slideDown 0.9s ease-out;
        }
        
        /* Text area */
        .stTextArea textarea {
            border-radius: 12px !important;
            border: 2px solid #e2e8f0 !important;
            padding: 1rem !important;
            font-size: 1rem !important;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        
        .stTextArea textarea:focus {
            border-color: #667eea !important;
            box-shadow: 0 4px 16px rgba(102, 126, 234, 0.2) !important;
            transform: translateY(-2px);
        }
        
        /* Buttons */
        .stButton button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.75rem 2.5rem !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
            letter-spacing: 0.5px;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            text-transform: uppercase;
        }
        
        .stButton button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 6px 25px rgba(102, 126, 234, 0.5) !important;
        }
        
        .stButton button:active {
            transform: translateY(-1px) !important;
        }
        
        /* Spinner */
        .stSpinner > div {
            border-top-color: #667eea !important;
        }
        
        /* Success/Warning/Error messages */
        .stAlert {
            border-radius: 12px !important;
            border-left: 4px solid !important;
            padding: 1rem 1.5rem !important;
            animation: slideIn 0.4s ease-out;
        }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        /* Markdown content */
        .element-container {
            animation: fadeInContent 0.5s ease-in;
        }
        
        @keyframes fadeInContent {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        /* Lists */
        ul, ol {
            line-height: 1.8;
            color: #4a5568;
        }
        
        li {
            margin-bottom: 0.5rem;
        }
        
        /* Strong text */
        strong {
            color: #2d3748;
            font-weight: 600;
        }
        
        /* Code blocks */
        code {
            background: #f7fafc;
            padding: 0.2rem 0.5rem;
            border-radius: 6px;
            color: #667eea;
            font-size: 0.9em;
        }
        
        /* Divider */
        hr {
            margin: 2rem 0;
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
        }
        
        /* Risk badges */
        .risk-high {
            background: #fed7d7;
            color: #c53030;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85rem;
        }
        
        .risk-medium {
            background: #feebc8;
            color: #c05621;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85rem;
        }
        
        .risk-low {
            background: #c6f6d5;
            color: #2f855a;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85rem;
        }
        
        /* Feature cards */
        .feature-card {
            background: linear-gradient(135deg, #f6f8fb 0%, #ffffff 100%);
            border-radius: 16px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-left: 4px solid #667eea;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateX(8px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.15);
        }
        
        /* Floating labels */
        .floating-label {
            font-weight: 600;
            color: #4a5568;
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
            display: block;
        }
        
        /* Loading animation */
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        .loading {
            animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }
        
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        }
    </style>
    """, unsafe_allow_html=True)


def render_header():
    """Render the main header with premium branding"""
    st.markdown("""
    <h1><span class="emoji">🚀</span> Product Thinking Studio</h1>
    <div class='subtitle'>
        <span>Elite Decision Support for Product Managers</span>
        <span class='badge'>✨ AI-Powered</span>
        <span class='badge'>🧠 Strategic Insights</span>
    </div>
    """, unsafe_allow_html=True)


def render_input_section():
    """Render the premium input section for user context"""
    st.markdown("""
    <div class='input-wrapper'>
        <span class='floating-label'>📝 Describe Your Product Challenge</span>
    </div>
    """, unsafe_allow_html=True)
    
    user_context = st.text_area(
        "Product Situation",
        height=220,
        placeholder="Example: Our mobile app's DAU dropped 18% over the past 3 weeks after we launched a new personalized home feed powered by ML. The algorithm is working as designed, but session times decreased from 12 mins to 8 mins average. PM lead wants to roll back immediately. Engineering says rollback takes 2 weeks. Marketing already announced this as our flagship feature. What should we do?",
        label_visibility="collapsed",
        key="context_input"
    )
    
    return user_context


def render_analyze_button():
    """Render the premium analyze button"""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        return st.button("✨ Analyze & Get Insights", use_container_width=True, type="primary")


def render_response(response_text, user_context=""):
    """Render the AI response with premium formatting"""
    st.markdown("<div class='response-card'>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(response_text)
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
