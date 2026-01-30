# Google Cloud Platform Deployment Guide

## 🚀 Quick Deploy to GCP Cloud Run

### Prerequisites
- Google Cloud account with billing enabled
- OpenAI API key
- Google Cloud SDK installed (✓ Already installed!)

### Option 1: Automated Deployment with Playwright Browser

This script deploys to GCP and automatically opens the site in a browser tab!

```bash
# 1. Set your OpenAI API key
export OPENAI_API_KEY='your-openai-api-key-here'

# 2. (Optional) Set custom project ID
export GCP_PROJECT_ID='my-project-id'  # Or it will use 'product-playground-demo'

# 3. Run the automated deployment
cd /workspaces/ProductPlayGround/product-thinking-studio
python3 deploy_gcp_playwright.py
```

**What it does:**
1. ✓ Authenticates with Google Cloud
2. ✓ Enables required APIs (Cloud Build, Cloud Run)
3. ✓ Builds Docker container image (~5-10 min)
4. ✓ Deploys to Cloud Run with auto-scaling
5. ✓ **Opens your live site in a new browser tab!**
6. ✓ Takes screenshot of deployed app
7. ✓ Validates all features are working

### Option 2: Manual Deployment

```bash
# 1. Authenticate
gcloud auth login

# 2. Set project (or create new one at console.cloud.google.com)
gcloud config set project YOUR-PROJECT-ID

# 3. Enable APIs
gcloud services enable cloudbuild.googleapis.com run.googleapis.com

# 4. Build container
gcloud builds submit --tag gcr.io/YOUR-PROJECT-ID/product-playground

# 5. Deploy to Cloud Run
gcloud run deploy product-playground \
    --image gcr.io/YOUR-PROJECT-ID/product-playground \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars "OPENAI_API_KEY=your-key" \
    --memory 2Gi \
    --cpu 2 \
    --timeout 120s \
    --max-instances 10

# 6. Get your live URL
gcloud run services describe product-playground \
    --platform managed \
    --region us-central1 \
    --format 'value(status.url)'
```

### Option 3: Interactive Script

```bash
./deploy-gcp.sh
```

This script will guide you through the deployment process step-by-step.

## 🌐 Custom Domain Setup

After deployment, add your custom domain:

```bash
# Map custom domain
gcloud run domain-mappings create \
    --service=product-playground \
    --domain=productplayground.com \
    --region=us-central1

# Update DNS records (shown after command above)
# Add the CNAME or A records to your domain registrar
```

## 💰 Pricing Estimate

**Cloud Run (Recommended):**
- First 2 million requests/month: FREE
- After that: ~$0.40 per million requests
- Memory (2GB): ~$0.0025/hour while running
- CPU (2 vCPUs): ~$0.024/hour while running

**Expected monthly cost:** $5-20 depending on traffic

Benefits:
- ✓ Auto-scales from 0 to 10 instances
- ✓ Only pay when requests are being processed
- ✓ Free SSL certificate
- ✓ Global CDN
- ✓ Zero maintenance

## 📊 Monitoring & Logs

```bash
# View logs
gcloud run logs tail --service=product-playground --region=us-central1

# View metrics in browser
gcloud run services describe product-playground \
    --region=us-central1 \
    --platform=managed
```

Visit Cloud Console: https://console.cloud.google.com/run

## 🔧 Update Deployment

```bash
# After making code changes
gcloud builds submit --tag gcr.io/YOUR-PROJECT-ID/product-playground

gcloud run deploy product-playground \
    --image gcr.io/YOUR-PROJECT-ID/product-playground \
    --region us-central1
```

## 🎯 What's Deployed

Your deployed app includes:
- ✓ Flask backend with Gunicorn
- ✓ OpenAI GPT-4o integration
- ✓ Playwright web scraper (with Chromium)
- ✓ PDF generation (ReportLab)
- ✓ All 9 PM features:
  - Challenge Analysis
  - Root Cause Analysis
  - Strategy Formulation
  - User Story Generation
  - Metrics & KPIs
  - Risk Assessment
  - Stakeholder Mapping
  - Product Teardown
  - PRD Generator

## 🚨 Troubleshooting

**Build fails:**
```bash
# Check Cloud Build logs
gcloud builds list --limit=5
gcloud builds log BUILD_ID
```

**Deployment fails:**
```bash
# Check service logs
gcloud run logs read --service=product-playground --limit=50
```

**Out of memory:**
```bash
# Increase memory
gcloud run services update product-playground \
    --memory 4Gi \
    --region us-central1
```

## 🎉 Success Checklist

After deployment, verify:
- [ ] Site loads at Cloud Run URL
- [ ] All 9 tabs visible and clickable
- [ ] Can submit form and get AI analysis
- [ ] PDF downloads work
- [ ] No console errors
- [ ] Playwright web scraper works (Product Teardown)

---

**Pro Tip:** The automated script (`deploy_gcp_playwright.py`) handles everything and opens your site in a browser automatically! Just set OPENAI_API_KEY and run it.
