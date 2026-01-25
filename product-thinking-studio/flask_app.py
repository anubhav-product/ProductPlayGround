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
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import markdown2
import re
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

@app.route('/analyze-website', methods=['POST'])
def analyze_website():
    """Handle product/market teardown analysis"""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        website_url = data.get('website_url', '').strip()
        additional_context = data.get('additional_context', '').strip()
        
        if not website_url:
            return jsonify({'error': 'Please provide a website URL'}), 400
        
        # Basic URL validation
        if not website_url.startswith(('http://', 'https://')):
            website_url = 'https://' + website_url
        
        # Check if API key is configured
        if not os.getenv('OPENAI_API_KEY'):
            return jsonify({'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY environment variable.'}), 500
        
        engine = ProductThinkingEngine()
        response = engine.analyze_website(website_url, additional_context)
        
        return jsonify({
            'success': True,
            'analysis': response,
            'website_url': website_url,
            'timestamp': datetime.now().strftime("%Y%m%d_%H%M%S")
        })
    except Exception as e:
        print(f"Error in /analyze-website: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500

@app.route('/download-pdf', methods=['POST'])
def download_pdf():
    """Generate and download professional PDF report"""
    try:
        data = request.json
        analysis_text = data.get('analysis', '')
        context = data.get('context', '')
        timestamp = datetime.now()
        
        buffer = BytesIO()
        
        # Custom page template with header/footer
        class NumberedCanvas(canvas.Canvas):
            def __init__(self, *args, **kwargs):
                canvas.Canvas.__init__(self, *args, **kwargs)
                self._saved_page_states = []

            def showPage(self):
                self._saved_page_states.append(dict(self.__dict__))
                self._startPage()

            def save(self):
                num_pages = len(self._saved_page_states)
                for state in self._saved_page_states:
                    self.__dict__.update(state)
                    self.draw_page_decorations(num_pages)
                    canvas.Canvas.showPage(self)
                canvas.Canvas.save(self)

            def draw_page_decorations(self, page_count):
                self.saveState()
                
                # Header with gradient effect (simulated with lines)
                self.setStrokeColor(colors.HexColor('#6366f1'))
                self.setLineWidth(3)
                self.line(0.75*inch, letter[1] - 0.5*inch, letter[0] - 0.75*inch, letter[1] - 0.5*inch)
                
                self.setStrokeColor(colors.HexColor('#8b5cf6'))
                self.setLineWidth(2)
                self.line(0.75*inch, letter[1] - 0.52*inch, letter[0] - 0.75*inch, letter[1] - 0.52*inch)
                
                # Header text
                self.setFont('Helvetica-Bold', 10)
                self.setFillColor(colors.HexColor('#2c3e50'))
                self.drawString(0.75*inch, letter[1] - 0.35*inch, "Product Playground · Strategic Analysis Report")
                
                # Footer
                self.setFont('Helvetica', 9)
                self.setFillColor(colors.HexColor('#7f8c8d'))
                footer_text = f"Generated on {timestamp.strftime('%B %d, %Y at %I:%M %p')}"
                self.drawString(0.75*inch, 0.5*inch, footer_text)
                
                # Page number
                page_num = f"Page {self._pageNumber} of {page_count}"
                self.drawRightString(letter[0] - 0.75*inch, 0.5*inch, page_num)
                
                # Footer line
                self.setStrokeColor(colors.HexColor('#e1e8ed'))
                self.setLineWidth(1)
                self.line(0.75*inch, 0.65*inch, letter[0] - 0.75*inch, 0.65*inch)
                
                self.restoreState()

        doc = SimpleDocTemplate(
            buffer, 
            pagesize=letter,
            rightMargin=0.75*inch, 
            leftMargin=0.75*inch,
            topMargin=1*inch, 
            bottomMargin=0.85*inch,
            title="Product Analysis Report",
            author="Product Playground"
        )
        
        elements = []
        
        # Define custom styles
        styles = getSampleStyleSheet()
        
        # Cover page title style
        cover_title = ParagraphStyle(
            'CoverTitle',
            parent=styles['Heading1'],
            fontSize=36,
            textColor=colors.HexColor('#6366f1'),
            spaceAfter=20,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold',
            leading=42
        )
        
        # Subtitle style
        cover_subtitle = ParagraphStyle(
            'CoverSubtitle',
            parent=styles['Normal'],
            fontSize=16,
            textColor=colors.HexColor('#7f8c8d'),
            spaceAfter=40,
            alignment=TA_CENTER,
            fontName='Helvetica',
            leading=20
        )
        
        # Section header (H2)
        section_header = ParagraphStyle(
            'SectionHeader',
            parent=styles['Heading2'],
            fontSize=18,
            textColor=colors.HexColor('#6366f1'),
            spaceBefore=24,
            spaceAfter=12,
            fontName='Helvetica-Bold',
            borderWidth=0,
            borderColor=colors.HexColor('#6366f1'),
            borderPadding=8,
            backColor=colors.HexColor('#f8f9fa'),
            leftIndent=10,
            leading=22
        )
        
        # Subsection header (H3)
        subsection_header = ParagraphStyle(
            'SubsectionHeader',
            parent=styles['Heading3'],
            fontSize=14,
            textColor=colors.HexColor('#8b5cf6'),
            spaceBefore=16,
            spaceAfter=8,
            fontName='Helvetica-Bold',
            leftIndent=5,
            leading=18
        )
        
        # Body text style
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['BodyText'],
            fontSize=11,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=10,
            alignment=TA_JUSTIFY,
            fontName='Helvetica',
            leading=16,
            leftIndent=0,
            rightIndent=0
        )
        
        # Bullet point style
        bullet_style = ParagraphStyle(
            'BulletPoint',
            parent=body_style,
            fontSize=10,
            leftIndent=20,
            bulletIndent=10,
            spaceAfter=6,
            leading=14
        )
        
        # Highlight box style
        highlight_style = ParagraphStyle(
            'Highlight',
            parent=body_style,
            fontSize=11,
            backColor=colors.HexColor('#f0f4ff'),
            borderWidth=1,
            borderColor=colors.HexColor('#6366f1'),
            borderPadding=10,
            borderRadius=5,
            leftIndent=10,
            rightIndent=10,
            spaceBefore=10,
            spaceAfter=10
        )
        
        # Warning/Risk style
        warning_style = ParagraphStyle(
            'Warning',
            parent=body_style,
            fontSize=10,
            backColor=colors.HexColor('#fff4e6'),
            borderWidth=1,
            borderColor=colors.HexColor('#f39c12'),
            borderPadding=10,
            leftIndent=10,
            rightIndent=10,
            spaceBefore=8,
            spaceAfter=8
        )
        
        # === COVER PAGE ===
        elements.append(Spacer(1, 2*inch))
        elements.append(Paragraph("🚀 Product Playground", cover_title))
        elements.append(Paragraph("AI-Powered Strategic Analysis Report", cover_subtitle))
        
        # Info box on cover
        cover_info_data = [
            ['Report Type:', 'Product & Market Analysis'],
            ['Generated:', timestamp.strftime('%B %d, %Y')],
            ['Time:', timestamp.strftime('%I:%M %p')],
            ['Powered by:', 'GPT-4o Advanced Analysis']
        ]
        
        cover_table = Table(cover_info_data, colWidths=[2*inch, 3.5*inch])
        cover_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8f9fa')),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#6366f1')),
            ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#2c3e50')),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e1e8ed')),
        ]))
        
        elements.append(cover_table)
        elements.append(Spacer(1, 1*inch))
        
        # Context box if provided
        if context:
            elements.append(Paragraph("📋 Analysis Context", subsection_header))
            elements.append(Paragraph(context, highlight_style))
        
        elements.append(PageBreak())
        
        # === ANALYSIS CONTENT ===
        # Parse the markdown analysis
        lines = analysis_text.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                elements.append(Spacer(1, 0.1*inch))
                continue
            
            # Handle headers
            if line.startswith('## '):
                # H2 - Major section
                title = line.replace('## ', '').strip()
                # Add emoji if not present
                if not any(char in title for char in '🎯📊💡🔍⚠️🚀📈✅'):
                    title = '▸ ' + title
                elements.append(Spacer(1, 0.15*inch))
                elements.append(Paragraph(title, section_header))
                
            elif line.startswith('### '):
                # H3 - Subsection
                title = line.replace('### ', '').strip()
                elements.append(Paragraph(title, subsection_header))
                
            elif line.startswith('**') and line.endswith('**'):
                # Bold standalone lines (labels)
                text = line.replace('**', '')
                label_style = ParagraphStyle(
                    'Label',
                    parent=body_style,
                    fontSize=11,
                    textColor=colors.HexColor('#6366f1'),
                    fontName='Helvetica-Bold',
                    spaceBefore=8,
                    spaceAfter=4
                )
                elements.append(Paragraph(text, label_style))
                
            elif line.startswith('- ') or line.startswith('* '):
                # Bullet points
                text = line[2:].strip()
                # Convert markdown bold
                text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
                elements.append(Paragraph(f'• {text}', bullet_style))
                
            elif line.startswith(('1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ')):
                # Numbered lists
                text = re.sub(r'^\d+\.\s+', '', line)
                text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
                number = line.split('.')[0]
                elements.append(Paragraph(f'{number}. {text}', bullet_style))
                
            elif '**' in line:
                # Inline bold text - convert to HTML
                text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
                
                # Check if this is a risk/warning line
                if any(word in text.lower() for word in ['risk', 'warning', 'concern', 'threat', 'danger']):
                    elements.append(Paragraph(text, warning_style))
                # Check if this is a key insight
                elif any(word in line for word in ['Confidence:', 'Overall', 'Key:', 'Critical:']):
                    elements.append(Paragraph(text, highlight_style))
                else:
                    elements.append(Paragraph(text, body_style))
                    
            else:
                # Regular paragraph
                text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
                elements.append(Paragraph(text, body_style))
        
        # === FOOTER PAGE ===
        elements.append(PageBreak())
        elements.append(Spacer(1, 2*inch))
        
        footer_title = ParagraphStyle(
            'FooterTitle',
            parent=cover_title,
            fontSize=24,
            textColor=colors.HexColor('#6366f1'),
            alignment=TA_CENTER
        )
        
        elements.append(Paragraph("Thank you for using Product Playground", footer_title))
        elements.append(Spacer(1, 0.3*inch))
        
        footer_text = ParagraphStyle(
            'FooterText',
            parent=body_style,
            fontSize=11,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#7f8c8d')
        )
        
        elements.append(Paragraph(
            "This analysis was generated using advanced AI to provide strategic product insights.<br/>"
            "For best results, combine these insights with your domain expertise and market knowledge.",
            footer_text
        ))
        
        elements.append(Spacer(1, 1*inch))
        
        # Contact/info table
        footer_info = [
            ['🌐 Product Playground', 'AI-Powered PM Intelligence'],
            ['💡 Features', 'Challenge Analysis • KPI Diagnostics • Product Teardown'],
            ['🚀 Powered by', 'OpenAI GPT-4o'],
        ]
        
        footer_table = Table(footer_info, colWidths=[2.5*inch, 3.5*inch])
        footer_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8f9fa')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2c3e50')),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e1e8ed')),
        ]))
        
        elements.append(footer_table)
        
        # Build PDF with custom canvas
        doc.build(elements, canvasmaker=NumberedCanvas)
        buffer.seek(0)
        
        return send_file(
            buffer,
            as_attachment=True,
            download_name=f'ProductAnalysis_{timestamp.strftime("%Y%m%d_%H%M%S")}.pdf',
            mimetype='application/pdf'
        )
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
