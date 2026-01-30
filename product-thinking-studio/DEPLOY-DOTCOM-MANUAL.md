# 🚀 Complete Manual Guide: Deploy Your .COM Domain

## Overview
This guide walks you through deploying Product Playground to your own .com domain, step-by-step.

**Total Time:** 30-45 minutes  
**Cost:** $10-20/month (domain + hosting)

---

## 📋 STEP 1: Buy Your Domain (~5 min)

### Option A: Namecheap (Recommended)
1. Go to: https://www.namecheap.com
2. Search for: `productplayground.com` or your preferred name
3. Click "Add to Cart"
4. **Price:** ~$10-12/year
5. Complete purchase
6. **Save your login credentials**

### Option B: Google Domains
1. Go to: https://domains.google.com
2. Search and purchase (~$12/year)

### Option C: Cloudflare Registrar
1. Go to: https://www.cloudflare.com/products/registrar/
2. **Cheapest option:** At-cost pricing (~$8-9/year)
3. Requires Cloudflare account first

---

## 📋 STEP 2: Choose Hosting Platform (~10 min)

### 🎯 Option A: Vercel (EASIEST - Recommended)

**Pros:** Free, automatic HTTPS, global CDN, zero config  
**Cons:** 100GB bandwidth limit on free tier

**Steps:**
```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Login to Vercel
vercel login

# 3. Deploy from your project folder
cd /workspaces/ProductPlayGround/product-thinking-studio
vercel

# 4. Follow prompts:
#    - Set up new project? Y
#    - Link to existing? N
#    - Project name: product-playground
#    - Directory: ./ 
#    - Override settings? N

# 5. Add environment variable
vercel env add OPENAI_API_KEY production

# 6. Deploy to production
vercel --prod
```

**You'll get:** `your-project.vercel.app`

**Add custom domain:**
```bash
vercel domains add productplayground.com
```

Then add DNS records (Vercel shows you exactly what to add).

---

### 🎯 Option B: Railway (GREAT FOR PYTHON)

**Pros:** $5/month, PostgreSQL if needed, great Python support  
**Cons:** Not free

**Steps:**

1. **Sign up:** https://railway.app
2. **Connect GitHub:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose: `anubhav-product/ProductPlayGround`
   - Select: `product-thinking-studio` folder

3. **Set environment variables:**
   - Go to project → Variables
   - Add: `OPENAI_API_KEY` = `your-key-here`
   - Add: `PORT` = `8080`

4. **Add custom domain:**
   - Click "Settings" → "Domains"
   - Click "Custom Domain"
   - Enter: `productplayground.com`
   - Railway shows DNS records to add

5. **Configure build:**
   ```
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn --config gunicorn.conf.py flask_app:app
   ```

---

### 🎯 Option C: DigitalOcean App Platform

**Pros:** Professional, scalable, $12/month  
**Cons:** Slightly more complex

**Steps:**

1. **Sign up:** https://cloud.digitalocean.com/apps
2. **Create app:**
   - Click "Create" → "Apps"
   - Choose source: GitHub
   - Select repo: `ProductPlayGround`
   - Branch: `main`
   - Source directory: `product-thinking-studio`

3. **Configure:**
   - Type: Web Service
   - Build Command: `pip install -r requirements.txt`
   - Run Command: `gunicorn --config gunicorn.conf.py flask_app:app`
   - HTTP Port: `8080`

4. **Environment variables:**
   - Add `OPENAI_API_KEY`
   - Add `PORT=8080`

5. **Add domain:**
   - Go to "Settings" → "Domains"
   - Click "Add Domain"
   - Enter: `productplayground.com`
   - Add the CNAME record to your DNS

---

### 🎯 Option D: Google Cloud Run (Most Scalable)

Already set up! Just add custom domain:

```bash
# Deploy first (if not already)
gcloud builds submit --tag gcr.io/YOUR-PROJECT/product-playground
gcloud run deploy product-playground --image gcr.io/YOUR-PROJECT/product-playground

# Add domain
gcloud run domain-mappings create \
    --service=product-playground \
    --domain=productplayground.com \
    --region=us-central1
```

Follow DNS instructions shown.

---

## 📋 STEP 3: Configure DNS (~10 min)

### At Your Domain Registrar (Namecheap/Google Domains/etc.)

**For Vercel/Railway/DigitalOcean:**

1. Log into domain registrar
2. Go to DNS Management
3. Add these records:

```
Type: A
Host: @
Value: [IP from hosting platform]
TTL: Automatic

Type: CNAME
Host: www
Value: [provided by hosting platform]
TTL: Automatic
```

**Example for Vercel:**
```
A     @       76.76.21.21
CNAME www     cname.vercel-dns.com
```

**Example for Railway:**
```
CNAME @       your-app.railway.app
CNAME www     your-app.railway.app
```

**Example for DigitalOcean:**
```
A     @       [IP from DO]
CNAME www     your-app.ondigitalocean.app
```

### DNS Propagation
- **Wait time:** 10 minutes to 48 hours (usually <1 hour)
- **Check status:** https://dnschecker.org

---

## 📋 STEP 4: Enable HTTPS (~5 min)

Most platforms auto-enable HTTPS. If not:

### Vercel/Railway/DigitalOcean
✅ **Automatic!** SSL certificate issued automatically.

### Other platforms
1. Use **Cloudflare** (free):
   - Sign up: https://www.cloudflare.com
   - Add site: `productplayground.com`
   - Change nameservers at registrar to Cloudflare's
   - Enable "Always Use HTTPS" in SSL/TLS settings

---

## 📋 STEP 5: Verify Deployment (~5 min)

### Checklist:
```bash
# Test domain resolves
ping productplayground.com

# Test HTTPS
curl -I https://productplayground.com

# Should see: HTTP/2 200
```

### Manual Browser Test:
1. Visit: `https://productplayground.com`
2. ✓ Should redirect to HTTPS
3. ✓ Should show lock icon (secure)
4. ✓ Should load your app
5. ✓ Test all 9 features
6. ✓ Test PDF download

---

## 📋 STEP 6: Post-Deployment Setup (~10 min)

### A. Add Google Analytics
```html
<!-- Add to templates/index.html before </head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### B. Set Up Monitoring

**Option 1: UptimeRobot (Free)**
1. Sign up: https://uptimerobot.com
2. Add monitor: `productplayground.com`
3. Get alerts if site goes down

**Option 2: Sentry (Error Tracking)**
```bash
pip install sentry-sdk[flask]
```

Add to `flask_app.py`:
```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[FlaskIntegration()]
)
```

### C. Add robots.txt
Create `static/robots.txt`:
```
User-agent: *
Allow: /

Sitemap: https://productplayground.com/sitemap.xml
```

### D. Create sitemap.xml
Create `static/sitemap.xml`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://productplayground.com/</loc>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://productplayground.com/app</loc>
    <priority>0.9</priority>
  </url>
</urlset>
```

---

## 🎯 QUICK REFERENCE: Platform Comparison

| Platform | Setup Time | Monthly Cost | Free Tier | Best For |
|----------|-----------|--------------|-----------|----------|
| **Vercel** | 5 min | $0-20 | Yes (100GB) | Fastest setup |
| **Railway** | 10 min | $5 | $5 free credit | Python apps |
| **DigitalOcean** | 15 min | $12 | No | Production apps |
| **Google Cloud** | 20 min | $5-20 | Yes (generous) | Scalability |
| **Render** | 10 min | $7 | Yes (limited) | Already using! |

---

## 🚨 Common Issues & Fixes

### Issue: Domain not resolving
```bash
# Check DNS propagation
dig productplayground.com

# If no results, DNS not updated yet. Wait 1-24 hours.
```

### Issue: HTTPS not working
- Most platforms auto-provision SSL (10-30 min)
- Try Cloudflare for instant HTTPS
- Check platform docs for SSL settings

### Issue: App not loading
```bash
# Check environment variables set correctly
# Check build logs on platform dashboard
# Verify OPENAI_API_KEY is set
```

### Issue: 502/503 errors
- Check if app is running (platform dashboard)
- Check memory limits (increase if needed)
- Check logs for errors

---

## 📊 My Recommended Path

### For You (Based on Current Setup):

**Keep Render + Add Domain** (Easiest!)

Your app is already deployed on Render. Just add domain:

1. **Buy domain:** Namecheap ($10/year)
2. **On Render:**
   - Go to your service dashboard
   - Click "Settings" → "Custom Domain"
   - Add: `productplayground.com`
3. **Add DNS records** (Render shows exact values)
4. **Wait 10-30 min** for DNS + SSL
5. **Done!** Visit `https://productplayground.com`

**Total cost:** $17/year (domain) + $7/month (Render) = **$10/month**

---

## ✅ Final Checklist

Before announcing your .com:
- [ ] Domain purchased and registered
- [ ] DNS configured correctly
- [ ] HTTPS enabled (green lock)
- [ ] All 9 features tested
- [ ] PDF downloads working
- [ ] Mobile responsive
- [ ] Google Analytics added
- [ ] Uptime monitoring set up
- [ ] Error tracking configured
- [ ] robots.txt added
- [ ] sitemap.xml added

---

## 🎉 You're Live!

Once complete:
1. Share: `https://productplayground.com`
2. Test from different devices
3. Monitor traffic and errors
4. Iterate and improve

**Need help?** Check platform docs or ask for specific step clarification!
