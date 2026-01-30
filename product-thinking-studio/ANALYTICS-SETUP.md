# 📊 Google Analytics Setup Guide

## Quick Setup (5 minutes)

### Step 1: Create Google Analytics Account

1. Go to: https://analytics.google.com
2. Click **"Start measuring"**
3. Account name: `Product Playground`
4. Next → Check all boxes → Next
5. Property name: `Product Playground`
6. Reporting timezone: Your timezone
7. Currency: Your currency
8. Next → Select industry category: **Software & Technology**
9. Business size: **Small**
10. Click **Create**
11. Accept Terms of Service

### Step 2: Set Up Data Stream

1. Choose platform: **Web**
2. Website URL: `https://productplayground-1.onrender.com`
3. Stream name: `Product Playground - Main`
4. Click **Create stream**

### Step 3: Get Your Measurement ID

You'll see something like: `G-XXXXXXXXXX`

**Copy this ID!**

### Step 4: Add to Your Site

Replace `G-PLACEHOLDER123` in `templates/index.html` with your actual ID:

```javascript
// Find this line (around line 28-29):
gtag('config', 'G-PLACEHOLDER123', {

// Replace with:
gtag('config', 'G-XXXXXXXXXX', {  // Your actual ID
```

### Step 5: Deploy

```bash
git add templates/index.html
git commit -m "chore: add real Google Analytics ID"
git push origin main
```

Wait 2-3 minutes for Render to deploy.

### Step 6: Verify

1. Visit your site: https://productplayground-1.onrender.com/app
2. In Google Analytics → Reports → Realtime
3. You should see **1 active user** (you!)

---

## 📈 What Gets Tracked:

### Automatic Events:
- ✅ Page views
- ✅ Session duration
- ✅ User demographics
- ✅ Device types (mobile/desktop)
- ✅ Traffic sources
- ✅ Geographic location

### Custom Events (Already Configured):
- ✅ **Feature Usage**: Which tabs users click
- ✅ **PDF Downloads**: How many reports generated
- ✅ **Analysis Completion**: Successful AI analyses

### Event Tracking Examples:

The code already includes tracking functions:

```javascript
// Track when user uses a feature
trackFeature('Challenge Analysis');
trackFeature('Root Cause Analysis');

// Track PDF downloads
trackPDFDownload('Challenge Report');
```

---

## 📊 Key Metrics to Monitor:

### User Metrics:
- **Total Users**: How many people visited
- **New vs Returning**: User retention
- **Session Duration**: Engagement level
- **Bounce Rate**: First impression quality

### Feature Metrics:
- **Most Used Feature**: Which tab is most popular
- **PDF Downloads**: Conversion rate
- **Analysis Success Rate**: How often users complete analysis

### Traffic Sources:
- **Direct**: People typing URL
- **Referral**: Links from other sites
- **Social**: Twitter, LinkedIn shares
- **Search**: Google organic traffic

---

## 🎯 Custom Tracking Examples:

### Track Tab Clicks:
```javascript
function showTab(tab) {
    // ... existing code ...
    
    // Add tracking
    if (typeof gtag !== 'undefined') {
        trackFeature(tab);
    }
}
```

### Track Analysis Success:
```javascript
async function analyzeChallenge() {
    // ... existing code ...
    
    if (data.success) {
        // Add tracking
        if (typeof gtag !== 'undefined') {
            gtag('event', 'analysis_complete', {
                'analysis_type': 'challenge',
                'word_count': data.analysis.split(' ').length
            });
        }
    }
}
```

### Track PDF Downloads:
```javascript
function downloadPDF() {
    // ... existing code ...
    
    if (typeof gtag !== 'undefined') {
        trackPDFDownload('Challenge Analysis');
    }
}
```

---

## 📈 Dashboard Setup:

### Create Custom Report:

1. Go to Analytics → Explore
2. Click **Create new exploration**
3. Name: "Feature Usage"
4. Add dimensions:
   - Event name
   - Page path
5. Add metrics:
   - Event count
   - Total users
6. Filter: `event_name` contains "feature_used"

### Set Up Conversions:

1. Go to Admin → Events
2. Click **Create event**
3. Name: `pdf_download`
4. Mark as conversion: ✅

---

## 🔒 Privacy Compliance:

### Cookie Consent (Optional):

Add this to show a cookie banner:

```html
<div id="cookie-banner" style="position: fixed; bottom: 0; left: 0; right: 0; background: #1a1a24; padding: 1rem; text-align: center; border-top: 1px solid rgba(255,255,255,0.1);">
    <p style="color: #fff; margin-bottom: 0.5rem;">
        We use cookies to analyze site usage. 
        <a href="/privacy" style="color: #6366f1;">Privacy Policy</a>
    </p>
    <button onclick="acceptCookies()" style="background: #6366f1; color: white; border: none; padding: 0.5rem 1.5rem; border-radius: 8px; cursor: pointer;">
        Accept
    </button>
</div>

<script>
function acceptCookies() {
    localStorage.setItem('cookiesAccepted', 'true');
    document.getElementById('cookie-banner').style.display = 'none';
}

if (localStorage.getItem('cookiesAccepted')) {
    document.getElementById('cookie-banner').style.display = 'none';
}
</script>
```

### Anonymize IPs:

Already configured in the setup:
```javascript
gtag('config', 'G-XXXXXXXXXX', {
    'anonymize_ip': true  // Add this if needed
});
```

---

## 📱 Mobile App Tracking (Future):

If you build a mobile app later:

```javascript
// Firebase Analytics for mobile
gtag('config', 'G-XXXXXXXXXX', {
    'app_name': 'Product Playground',
    'app_version': '1.0.0'
});
```

---

## 🎁 Bonus: Advanced Tracking

### Track Search Terms:
```javascript
gtag('event', 'search', {
    'search_term': searchQuery
});
```

### Track Outbound Links:
```javascript
document.querySelectorAll('a[href^="http"]').forEach(link => {
    link.addEventListener('click', () => {
        gtag('event', 'click', {
            'event_category': 'outbound',
            'event_label': link.href
        });
    });
});
```

### Track Errors:
```javascript
window.addEventListener('error', (e) => {
    gtag('event', 'exception', {
        'description': e.message,
        'fatal': false
    });
});
```

---

## ✅ Verification Checklist:

- [ ] Created Google Analytics account
- [ ] Got Measurement ID (G-XXXXXXXXXX)
- [ ] Replaced placeholder in code
- [ ] Deployed to production
- [ ] Verified in Realtime reports
- [ ] Set up custom events
- [ ] Created conversion goals
- [ ] Tested tracking on different devices

---

## 📞 Need Help?

- **GA4 Help Center**: https://support.google.com/analytics
- **Tag Assistant**: Chrome extension to verify tracking
- **Debug Mode**: Add `?debug_mode=true` to URL

---

**Note:** It takes 24-48 hours for data to fully populate in reports. Realtime works immediately though!
