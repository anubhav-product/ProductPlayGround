"""
Product Playground - Flask Application
Optimized for PythonAnywhere deployment
"""
from flask import Flask, render_template, request, jsonify, send_file
import sys
import os

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from prompt import ProductThinkingEngine
import os
from dotenv import load_dotenv
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER
import markdown2
from datetime import datetime
import traceback

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-in-production')

# Global error handler for all unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors"""
    return jsonify({
        'error': str(e),
        'type': type(e).__name__,
        'traceback': traceback.format_exc() if app.debug else None
    }), 500

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors with JSON"""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    """Handle method not allowed with JSON"""
    return jsonify({'error': 'Method not allowed'}), 405

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Handle product challenge analysis"""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        user_context = data.get('context', '')
        
        if not user_context.strip():
            return jsonify({'error': 'Please provide a product challenge'}), 400
        
        # Check if API key is configured
        if not os.getenv('OPENAI_API_KEY'):
            return jsonify({'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY environment variable.'}), 500
        
        engine = ProductThinkingEngine()
        response = engine.analyze(user_context)
        
        return jsonify({
            'success': True,
            'analysis': response,
            'timestamp': datetime.now().strftime("%Y%m%d_%H%M%S")
        })
    except Exception as e:
        print(f"Error in /analyze: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500

@app.route('/analyze-kpi', methods=['POST'])
def analyze_kpi():
    """Handle KPI dashboard analysis"""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        kpi_data = {
            'dau': int(data.get('dau', 0)),
            'mau': int(data.get('mau', 0)),
            'avg_session_time': float(data.get('avg_session_time', 0)),
            'conversion_rate': float(data.get('conversion_rate', 0)),
            'churn_rate': float(data.get('churn_rate', 0)),
            'retention_rate': float(data.get('retention_rate', 0)),
            'nps_score': int(data.get('nps_score', 0)),
            'revenue_per_user': float(data.get('revenue_per_user', 0)),
            'recent_changes': data.get('recent_changes', '')
        }
        
        if kpi_data['dau'] == 0 and kpi_data['mau'] == 0:
            return jsonify({'error': 'Please enter at least some KPI data'}), 400
        
        # Check if API key is configured
        if not os.getenv('OPENAI_API_KEY'):
            return jsonify({'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY environment variable.'}), 500
        
        engine = ProductThinkingEngine()
        response = engine.analyze_kpis(kpi_data)
        
        return jsonify({
            'success': True,
            'analysis': response,
            'kpi_data': kpi_data,
            'timestamp': datetime.now().strftime("%Y%m%d_%H%M%S")
        })
    except Exception as e:
        print(f"Error in /analyze-kpi: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500

@app.route('/download-pdf', methods=['POST'])
def download_pdf():
    """Generate and download PDF report"""
    try:
        data = request.json
        analysis_text = data.get('analysis', '')
        context = data.get('context', '')
        
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
            textColor='#2c3e50',
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
        html_content = markdown2.markdown(analysis_text)
        
        for paragraph in html_content.split('\n'):
            if paragraph.strip():
                try:
                    elements.append(Paragraph(paragraph, styles['BodyText']))
                    elements.append(Spacer(1, 0.1*inch))
                except:
                    pass
        
        doc.build(elements)
        buffer.seek(0)
        
        return send_file(
            buffer,
            as_attachment=True,
            download_name=f'product_analysis_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf',
            mimetype='application/pdf'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
