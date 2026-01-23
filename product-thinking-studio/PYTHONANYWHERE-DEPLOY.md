# PythonAnywhere Deployment Guide

## 🚀 Complete Deployment Steps

### 1. Prepare Repository

```bash
cd /workspaces/ProductPlayGround
git add .
git commit -m "Convert to Flask for PythonAnywhere deployment"
git push origin main
```

### 2. Create PythonAnywhere Account

1. Go to https://www.pythonanywhere.com
2. Sign up for free account
3. Confirm email and login

### 3. Clone Repository on PythonAnywhere

In PythonAnywhere Bash console:

```bash
git clone https://github.com/anubhav-product/ProductPlayGround.git
cd ProductPlayGround/product-thinking-studio
```

### 4. Create Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.10 productplayground
workon productplayground
pip install -r requirements.txt
```

### 5. Set Environment Variables

Create `.env` file:

```bash
nano .env
```

Add your configuration:

```
OPENAI_API_KEY=your-actual-api-key-here
OPENAI_MODEL=gpt-4o
TEMPERATURE=0.7
MAX_TOKENS=4000
SECRET_KEY=generate-a-random-secret-key-here
```

Save: `Ctrl+X`, then `Y`, then `Enter`

### 6. Configure Web App

1. Go to **Web** tab in PythonAnywhere dashboard
2. Click **Add a new web app**
3. Choose **Manual configuration**
4. Select **Python 3.10**

### 7. Configure WSGI File

Click on WSGI configuration file link, replace content with:

```python
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/YOUR_USERNAME/ProductPlayGround/product-thinking-studio'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Load environment variables
from dotenv import load_dotenv
load_dotenv(os.path.join(project_home, '.env'))

# Import your Flask app
from flask_app import app as application
```

Replace `YOUR_USERNAME` with your actual PythonAnywhere username.

### 8. Set Virtual Environment

In Web tab:
1. Find **Virtualenv** section
2. Enter: `/home/YOUR_USERNAME/.virtualenvs/productplayground`

### 9. Set Static Files (Optional)

If you add CSS/JS files later:
- URL: `/static/`
- Directory: `/home/YOUR_USERNAME/ProductPlayGround/product-thinking-studio/static`

### 10. Reload Web App

Click the big green **Reload** button

### 11. Test Your App

Visit: `https://YOUR_USERNAME.pythonanywhere.com`

---

## 🔧 Troubleshooting

### Check Error Logs

In Web tab:
- Click on **Error log** link
- Check for Python errors

### Common Issues

**Import Error:**
```bash
workon productplayground
pip install -r requirements.txt
```

**Environment Variables Not Loading:**
- Verify `.env` file exists in correct directory
- Check file permissions: `chmod 600 .env`

**OpenAI API Error:**
- Verify API key is valid
- Check OpenAI account has credits

### Update Code

When you push new changes to GitHub:

```bash
cd ~/ProductPlayGround/product-thinking-studio
git pull origin main
workon productplayground
pip install -r requirements.txt
```

Then click **Reload** in Web tab.

---

## 📊 Usage Limits (Free Tier)

- **CPU seconds/day**: 100 seconds
- **Disk space**: 512 MB
- **Domain**: `username.pythonanywhere.com`
- **Always-on**: No (app sleeps after inactivity)

For production use, consider upgrading to paid plan.

---

## 🔒 Security Checklist

- ✅ `.env` file is in `.gitignore`
- ✅ Never commit API keys to GitHub
- ✅ Use strong `SECRET_KEY` in production
- ✅ Set proper file permissions: `chmod 600 .env`

---

## 🎯 Quick Commands Reference

```bash
# SSH into PythonAnywhere
# Use bash console in web interface

# Activate virtual environment
workon productplayground

# Update code
cd ~/ProductPlayGround/product-thinking-studio
git pull

# Install/update packages
pip install -r requirements.txt

# View logs
tail -f /var/log/YOUR_USERNAME.pythonanywhere.com.error.log

# Edit environment
nano .env
```

---

## ✨ Success!

Your Product Playground app should now be live at:
`https://YOUR_USERNAME.pythonanywhere.com`

Share this URL to let others use your AI-powered product analysis tool!
