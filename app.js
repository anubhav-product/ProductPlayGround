// Product Studio JavaScript

// Notification System
function showNotification(message) {
    // Create notification element if it doesn't exist
    let notification = document.getElementById('notification');
    if (!notification) {
        notification = document.createElement('div');
        notification.id = 'notification';
        notification.setAttribute('role', 'alert');
        notification.setAttribute('aria-live', 'polite');
        document.body.appendChild(notification);
    }
    
    notification.textContent = message;
    notification.className = 'notification show';
    
    setTimeout(() => {
        notification.className = 'notification';
    }, 4000);
}

// Tab Navigation
document.addEventListener('DOMContentLoaded', function() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const tabId = button.getAttribute('data-tab');
            
            // Remove active class from all buttons and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Add active class to clicked button and corresponding content
            button.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });
});

// Problem Framing
function generateProblemFraming() {
    const problem = document.getElementById('pf-problem').value;
    const who = document.getElementById('pf-who').value;
    const impact = document.getElementById('pf-impact').value;
    const why = document.getElementById('pf-why').value;
    const assumptions = document.getElementById('pf-assumptions').value;
    
    if (!problem || !who || !impact) {
        showNotification('Please fill in at least the Problem Statement, Who is affected, and Impact fields.');
        return;
    }
    
    const output = document.getElementById('pf-output');
    
    let framing = '🎯 STRUCTURED PROBLEM STATEMENT\n\n';
    framing += `Problem:\n${problem}\n\n`;
    framing += `Affected Parties:\n${who}\n\n`;
    framing += `Impact:\n${impact}\n\n`;
    
    if (why) {
        framing += `Timing/Urgency:\n${why}\n\n`;
    }
    
    if (assumptions) {
        framing += `Key Assumptions:\n${assumptions}\n\n`;
    }
    
    framing += '📊 REFLECTION QUESTIONS:\n';
    framing += '• Are we solving the right problem?\n';
    framing += '• Have we considered all affected stakeholders?\n';
    framing += '• What might we be missing?\n';
    framing += '• How can we validate our assumptions?\n';
    
    output.textContent = framing;
    output.classList.add('filled');
}

// Root Cause Analysis
function generateRootCause() {
    const symptom = document.getElementById('rca-symptom').value;
    const why1 = document.getElementById('rca-why1').value;
    const why2 = document.getElementById('rca-why2').value;
    const why3 = document.getElementById('rca-why3').value;
    const why4 = document.getElementById('rca-why4').value;
    const why5 = document.getElementById('rca-why5').value;
    const factors = document.getElementById('rca-factors').value;
    
    if (!symptom) {
        showNotification('Please describe the observed symptom.');
        return;
    }
    
    const output = document.getElementById('rca-output');
    
    let analysis = '🔍 ROOT CAUSE ANALYSIS\n\n';
    analysis += `Observed Symptom:\n${symptom}\n\n`;
    
    if (why1 || why2 || why3 || why4 || why5) {
        analysis += '5 Whys Progression:\n';
        if (why1) analysis += `1. ${why1}\n`;
        if (why2) analysis += `2. ${why2}\n`;
        if (why3) analysis += `3. ${why3}\n`;
        if (why4) analysis += `4. ${why4}\n`;
        if (why5) analysis += `5. ${why5}\n`;
        analysis += '\n';
    }
    
    if (factors) {
        analysis += `Contributing Factors:\n${factors}\n\n`;
    }
    
    analysis += '💡 INSIGHTS:\n';
    analysis += '• What patterns emerge from this analysis?\n';
    analysis += '• Which causes are within your control?\n';
    analysis += '• What would address the root cause vs. symptoms?\n';
    analysis += '• What evidence supports this analysis?\n';
    
    output.textContent = analysis;
    output.classList.add('filled');
}

// Risk Management
function generateRiskAssessment() {
    const decision = document.getElementById('rm-decision').value;
    const technical = document.getElementById('rm-technical').value;
    const business = document.getElementById('rm-business').value;
    const ux = document.getElementById('rm-ux').value;
    const org = document.getElementById('rm-org').value;
    const mitigation = document.getElementById('rm-mitigation').value;
    
    if (!decision) {
        showNotification('Please describe the decision being considered.');
        return;
    }
    
    const output = document.getElementById('rm-output');
    
    let assessment = '⚠️ RISK ASSESSMENT\n\n';
    assessment += `Decision Under Consideration:\n${decision}\n\n`;
    
    assessment += 'IDENTIFIED RISKS:\n\n';
    
    if (technical) {
        assessment += `Technical Risks:\n${technical}\n\n`;
    }
    
    if (business) {
        assessment += `Business Risks:\n${business}\n\n`;
    }
    
    if (ux) {
        assessment += `User Experience Risks:\n${ux}\n\n`;
    }
    
    if (org) {
        assessment += `Organizational Risks:\n${org}\n\n`;
    }
    
    if (mitigation) {
        assessment += `Mitigation Strategies:\n${mitigation}\n\n`;
    }
    
    assessment += '🛡️ RISK MANAGEMENT QUESTIONS:\n';
    assessment += '• Which risks are most likely to materialize?\n';
    assessment += '• Which risks would have the highest impact?\n';
    assessment += '• Are the mitigation strategies realistic?\n';
    assessment += '• What is your risk tolerance for this decision?\n';
    assessment += '• What early warning signs should you monitor?\n';
    
    output.textContent = assessment;
    output.classList.add('filled');
}

// Tradeoff Evaluation
function generateTradeoffAnalysis() {
    const context = document.getElementById('te-context').value;
    const optionAName = document.getElementById('te-option-a-name').value || 'Option A';
    const optionADesc = document.getElementById('te-option-a-desc').value;
    const optionBName = document.getElementById('te-option-b-name').value || 'Option B';
    const optionBDesc = document.getElementById('te-option-b-desc').value;
    const tradeoffs = document.getElementById('te-tradeoffs').value;
    
    if (!context || !optionADesc || !optionBDesc) {
        showNotification('Please fill in the decision context and both options.');
        return;
    }
    
    const output = document.getElementById('te-output');
    
    let analysis = '⚖️ TRADEOFF ANALYSIS\n\n';
    analysis += `Decision Context:\n${context}\n\n`;
    
    analysis += `${optionAName}:\n${optionADesc}\n\n`;
    analysis += `${optionBName}:\n${optionBDesc}\n\n`;
    
    // Criteria comparison
    const timeA = document.getElementById('te-time-a').value;
    const timeB = document.getElementById('te-time-b').value;
    const resourcesA = document.getElementById('te-resources-a').value;
    const resourcesB = document.getElementById('te-resources-b').value;
    const impactA = document.getElementById('te-impact-a').value;
    const impactB = document.getElementById('te-impact-b').value;
    const complexityA = document.getElementById('te-complexity-a').value;
    const complexityB = document.getElementById('te-complexity-b').value;
    
    if (timeA || timeB || resourcesA || resourcesB || impactA || impactB || complexityA || complexityB) {
        analysis += 'COMPARISON:\n\n';
        
        if (timeA || timeB) {
            analysis += `Time to Implement:\n`;
            analysis += `  ${optionAName}: ${timeA || 'Not specified'}\n`;
            analysis += `  ${optionBName}: ${timeB || 'Not specified'}\n\n`;
        }
        
        if (resourcesA || resourcesB) {
            analysis += `Resource Requirements:\n`;
            analysis += `  ${optionAName}: ${resourcesA || 'Not specified'}\n`;
            analysis += `  ${optionBName}: ${resourcesB || 'Not specified'}\n\n`;
        }
        
        if (impactA || impactB) {
            analysis += `User Impact:\n`;
            analysis += `  ${optionAName}: ${impactA || 'Not specified'}\n`;
            analysis += `  ${optionBName}: ${impactB || 'Not specified'}\n\n`;
        }
        
        if (complexityA || complexityB) {
            analysis += `Technical Complexity:\n`;
            analysis += `  ${optionAName}: ${complexityA || 'Not specified'}\n`;
            analysis += `  ${optionBName}: ${complexityB || 'Not specified'}\n\n`;
        }
    }
    
    if (tradeoffs) {
        analysis += `Key Tradeoffs:\n${tradeoffs}\n\n`;
    }
    
    analysis += '🤔 DECISION CONSIDERATIONS:\n';
    analysis += '• Which factors are most important in this context?\n';
    analysis += '• What are you optimizing for?\n';
    analysis += '• What are you willing to sacrifice?\n';
    analysis += '• Are there hidden costs or benefits?\n';
    analysis += '• Can you test either approach on a smaller scale?\n';
    
    output.textContent = analysis;
    output.classList.add('filled');
}

// Next Steps Guidance
function generateNextSteps() {
    const situation = document.getElementById('ns-situation').value;
    const direction = document.getElementById('ns-direction').value;
    const confidence = document.getElementById('ns-confidence').value;
    const gaps = document.getElementById('ns-gaps').value;
    const validation = document.getElementById('ns-validation').value;
    const stakeholders = document.getElementById('ns-stakeholders').value;
    
    if (!situation || !direction) {
        showNotification('Please describe the current situation and proposed direction.');
        return;
    }
    
    const output = document.getElementById('ns-output');
    
    let guidance = '🧭 NEXT STEPS GUIDANCE\n\n';
    guidance += `Current Situation:\n${situation}\n\n`;
    guidance += `Proposed Direction:\n${direction}\n\n`;
    
    if (confidence) {
        guidance += `Confidence Level: ${confidence}\n\n`;
    }
    
    if (gaps) {
        guidance += `Information Gaps:\n${gaps}\n\n`;
    }
    
    // Provide appropriate next steps based on confidence
    guidance += 'RECOMMENDED APPROACH:\n\n';
    
    const confidenceLevel = confidence ? confidence.toLowerCase() : '';
    
    if (confidenceLevel.includes('low')) {
        guidance += '⚠️ Low Confidence - Proceed with Caution:\n';
        guidance += '• Focus on gathering critical information first\n';
        guidance += '• Conduct discovery and research\n';
        guidance += '• Avoid major commitments until gaps are filled\n';
        guidance += '• Consider a spike or exploration phase\n\n';
    } else if (confidenceLevel.includes('medium-low')) {
        guidance += '📋 Medium-Low Confidence - Validate First:\n';
        guidance += '• Run small experiments or prototypes\n';
        guidance += '• Gather data on key unknowns\n';
        guidance += '• Consult domain experts\n';
        guidance += '• Build in feedback loops\n\n';
    } else if (confidenceLevel.includes('medium-high') || confidenceLevel.includes('high')) {
        guidance += '✅ Higher Confidence - Proceed Thoughtfully:\n';
        guidance += '• Plan implementation in phases\n';
        guidance += '• Monitor key metrics and assumptions\n';
        guidance += '• Keep stakeholders informed\n';
        guidance += '• Build in checkpoints to reassess\n\n';
    } else {
        guidance += '📊 General Recommendations:\n';
        guidance += '• Assess your confidence level honestly\n';
        guidance += '• Identify what would increase confidence\n';
        guidance += '• Balance speed with learning\n';
        guidance += '• Stay open to pivoting based on new information\n\n';
    }
    
    if (validation) {
        guidance += `Validation Opportunities:\n${validation}\n\n`;
    }
    
    if (stakeholders) {
        guidance += `Stakeholders to Consult:\n${stakeholders}\n\n`;
    }
    
    guidance += '💭 FINAL REFLECTIONS:\n';
    guidance += '• What would change your mind?\n';
    guidance += '• What could you learn quickly and cheaply?\n';
    guidance += '• What is reversible vs. irreversible?\n';
    guidance += '• How will you know if you\'re on the right track?\n';
    
    output.textContent = guidance;
    output.classList.add('filled');
}
