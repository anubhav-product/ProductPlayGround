# Deployment Guide: Making Product Playground a .com

This guide covers deploying Product Playground as a professional .com website with custom domain and production infrastructure.

## 🚀 Deployment Options

### Option 1: Vercel (Recommended for Flask)
**Cost**: Free tier available, Pro at $20/month
**Best for**: Quick deployment, automatic scaling, edge network

#### Setup Steps:

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Create `vercel.json` configuration** (already included in project)

3. **Deploy**
   ```bash
   cd product-thinking-studio
   vercel
   ```

4. **Configure Custom Domain**
   - Go to Vercel Dashboard → Your Project → Settings → Domains
   - Add your domain (e.g., `productplayground.com`)
   - Update DNS records at your domain registrar:
     - Type: `A` Record, Name: `@`, Value: `76.76.21.21`
     - Type: `CNAME`, Name: `www`, Value: `cname.vercel-dns.com`

5. **Environment Variables**
   - Dashboard → Settings → Environment Variables
   - Add: `OPENAI_API_KEY=your-key-here`

---

### Option 2: Railway.app
**Cost**: $5/month startup plan
**Best for**: Full control, databases, background jobs

#### Setup Steps:

1. **Create account at railway.app**

2. **Create new project from GitHub**
   - Connect GitHub repository
   - Railway auto-detects Flask app

3. **Configure**
   - Add environment variable: `OPENAI_API_KEY`
   - Set start command: `gunicorn flask_app:app`

4. **Custom Domain**
   - Settings → Networking → Custom Domain
   - Add your domain
   - Update DNS:
     - Type: `CNAME`, Name: `@`, Value: `your-app.up.railway.app`

---

### Option 3: AWS (Professional/Enterprise)
**Cost**: ~$50-200/month depending on traffic
**Best for**: Full control, scalability, enterprise features

#### Architecture:
```
Route 53 (DNS) → CloudFront (CDN) → ALB → EC2/ECS → RDS (if needed)
```

#### Setup Steps:

1. **Create EC2 Instance**
   ```bash
   # Choose Ubuntu 22.04 LTS
   # t3.small minimum ($15/month)
   ```

2. **Install Dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip nginx
   pip3 install -r requirements.txt
   playwright install
   ```

3. **Configure Gunicorn**
   ```bash
   gunicorn --workers 3 --bind 0.0.0.0:8000 flask_app:app
   ```

4. **Setup Nginx Reverse Proxy**
   ```nginx
   server {
       listen 80;
       server_name productplayground.com;
       
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

5. **SSL Certificate (Let's Encrypt)**
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d productplayground.com -d www.productplayground.com
   ```

6. **Setup Domain**
   - Route 53 → Create Hosted Zone
   - Update nameservers at domain registrar
   - Create A record pointing to EC2 Elastic IP

---

### Option 4: DigitalOcean App Platform
**Cost**: $12/month basic plan
**Best for**: Simplicity, good value, managed infrastructure

#### Setup Steps:

1. **Create App**
   - Connect GitHub repository
   - Select `product-thinking-studio` folder

2. **Configure**
   - Detected: Python (Flask)
   - Build Command: `pip install -r requirements.txt && playwright install`
   - Run Command: `gunicorn flask_app:app`

3. **Environment Variables**
   ```
   OPENAI_API_KEY=your-key
   FLASK_ENV=production
   ```

4. **Custom Domain**
   - Settings → Domains → Add Domain
   - Update DNS CNAME to point to DigitalOcean

---

## 🌐 Domain Registration

### Recommended Registrars:
1. **Namecheap** - $8-12/year for .com
2. **Google Domains** - $12/year
3. **Cloudflare Registrar** - At-cost pricing (~$8/year)

### Domain Suggestions:
- productplayground.com
- productthinkingstudio.com
- pmplayground.com
- thinkingtools.io
- productanalyst.ai

---

## 🔒 Production Checklist

### Security:
- ✅ HTTPS enabled (SSL certificate)
- ✅ Environment variables secured (not in code)
- ✅ API rate limiting configured
- ✅ CORS properly configured
- ✅ Security headers added

### Performance:
- ✅ Gunicorn with multiple workers
- ✅ Static files served via CDN
- ✅ Database connection pooling (if using DB)
- ✅ Caching strategy implemented
- ✅ Request timeout limits

### Monitoring:
- ✅ Error tracking (Sentry recommended)
- ✅ Uptime monitoring (UptimeRobot free tier)
- ✅ Analytics (Google Analytics or Plausible)
- ✅ Log aggregation (CloudWatch or Papertrail)

---

## 📊 Cost Comparison

| Platform | Monthly Cost | Best For | Scalability |
|----------|-------------|----------|-------------|
| Vercel | $0-20 | Quick start | Excellent |
| Railway | $5-25 | Startups | Good |
| DigitalOcean | $12-50 | Value | Very Good |
| AWS | $50-200+ | Enterprise | Excellent |
| Render.com | $7-25 | Simplicity | Good |

---

## 🚀 Recommended Setup for Product Playground

**Stage 1: MVP Launch (Month 1-3)**
- Platform: **Railway or Render**
- Domain: **productplayground.com** via Namecheap
- Cost: ~$20/month total
- Features: Custom domain, SSL, auto-deploy

**Stage 2: Growth (Month 4-12)**
- Platform: **DigitalOcean or Vercel Pro**
- CDN: Cloudflare (free tier)
- Monitoring: Sentry + UptimeRobot
- Cost: ~$40/month

**Stage 3: Scale (Year 2+)**
- Platform: **AWS with auto-scaling**
- Database: RDS for user data
- CDN: CloudFront
- Cost: $100-300/month depending on traffic

---

## 🔧 Production Flask Configuration

Create `production_config.py`:

```python
import os

class ProductionConfig:
    DEBUG = False
    TESTING = False
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Security
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Performance
    SEND_FILE_MAX_AGE_DEFAULT = 31536000  # 1 year for static files
    
    # Rate limiting
    RATELIMIT_ENABLED = True
    RATELIMIT_DEFAULT = "100 per hour"
```

Update `flask_app.py`:

```python
if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object('production_config.ProductionConfig')
```

---

## 📝 Next Steps

1. **Choose platform** based on your budget and technical comfort
2. **Register domain** (recommend productplayground.com)
3. **Deploy to staging** first to test
4. **Configure monitoring** before going live
5. **Set up CI/CD** for automatic deployments
6. **Launch** 🎉

---

## 🆘 Support Resources

- **Vercel Docs**: https://vercel.com/docs
- **Railway Docs**: https://docs.railway.app
- **DigitalOcean Tutorials**: https://www.digitalocean.com/community/tutorials
- **AWS Flask Guide**: https://aws.amazon.com/getting-started/hands-on/deploy-python-application/

---

**Need help?** Open an issue on GitHub or reach out to the community!
