# Render.com Deployment Guide

## 🚀 Deploy Product Playground to Render (Free)

### Prerequisites
- GitHub account with your repository
- OpenAI API key

---

## Deployment Steps

### 1. **Sign Up on Render**
- Go to https://render.com
- Click **Get Started for Free**
- Sign up with your GitHub account

### 2. **Create New Web Service**
1. Click **New +** → **Web Service**
2. Connect your GitHub account if not already connected
3. Select repository: **anubhav-product/ProductPlayGround**
4. Click **Connect**

### 3. **Configure Service**

Render will auto-detect the `render.yaml` file. Verify these settings:

- **Name**: `product-playground` (or your choice)
- **Runtime**: `Python 3`
- **Build Command**: 
  ```
  pip install -r product-thinking-studio/requirements.txt && pip install gunicorn
  ```
- **Start Command**: 
  ```
  gunicorn --chdir product-thinking-studio --bind 0.0.0.0:$PORT flask_app:app
  ```
- **Plan**: `Free`

### 4. **Add Environment Variables**

In the **Environment** section, add:

| Key | Value |
|-----|-------|
| `OPENAI_API_KEY` | `your-actual-openai-api-key` |
| `OPENAI_MODEL` | `gpt-4o` |
| `TEMPERATURE` | `0.7` |
| `MAX_TOKENS` | `4000` |
| `SECRET_KEY` | Auto-generated |

⚠️ **Important**: Keep `OPENAI_API_KEY` as **Secret** (don't check "Public")

### 5. **Deploy**
1. Click **Create Web Service**
2. Render will:
   - Clone your repository
   - Install dependencies
   - Start your Flask app
   - Give you a live URL

### 6. **Access Your App**
Your app will be live at: `https://product-playground-xxxx.onrender.com`

---

## ✨ Features

✅ **Free SSL/HTTPS** - Automatic  
✅ **Auto-deploy** - Updates on git push  
✅ **Custom domain** - Add your own (optional)  
✅ **Build logs** - Monitor deployment  
✅ **Zero downtime** - Automatic restarts  

---

## 🔄 Updates

To update your app:
```bash
git add .
git commit -m "Update message"
git push origin main
```

Render will automatically detect changes and redeploy! 🎉

---

## 🐛 Troubleshooting

### App not starting?
- Check **Logs** tab in Render dashboard
- Verify environment variables are set
- Ensure `OPENAI_API_KEY` is valid

### Module not found errors?
- Check `requirements.txt` includes all packages
- Verify build command ran successfully

### Need help?
- Render docs: https://render.com/docs
- Check deployment logs for specific errors

---

## 💰 Free Tier Limits

- **750 hours/month** of runtime
- App sleeps after 15 min of inactivity
- First request after sleep takes ~30 seconds
- Upgrade to paid tier for always-on service

---

## 🎯 Next Steps

Once deployed:
1. Test both analysis features
2. Try PDF download
3. Share your live URL!

Your **Product Playground** is now live on the web! 🚀
