# 🔑 How to Add Your OpenAI API Key

## Quick Start

### 1. Get Your API Key
1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in to your account
3. Click "Create new secret key"
4. Copy your API key (starts with `sk-...`)

### 2. Add to .env File
Open the `.env` file and replace `your-openai-api-key-here` with your actual key:

```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
```

### 3. Choose Your Model

**For Best Quality (Recommended):**
```env
OPENAI_MODEL=gpt-4o
```
- Most intelligent responses
- Best for complex product decisions
- More expensive (~$2.50 per 1M input tokens)

**For Speed & Cost:**
```env
OPENAI_MODEL=gpt-4o-mini
```
- Fast responses
- Good quality
- Very affordable (~$0.15 per 1M input tokens)

**For Maximum Intelligence:**
```env
OPENAI_MODEL=gpt-4-turbo
```
- Highest quality reasoning
- Best for strategic decisions
- Higher cost

## Configuration Options

### Temperature (Creativity)
```env
TEMPERATURE=0.7  # Default (balanced)
```
- `0.0-0.3`: Very focused, consistent, deterministic
- `0.4-0.7`: Balanced creativity and consistency (recommended)
- `0.8-1.0`: More creative, varied responses

### Max Tokens (Response Length)
```env
MAX_TOKENS=4000  # Default
```
- `2000`: Shorter, concise responses
- `4000`: Comprehensive analysis (recommended)
- `8000`: Very detailed (may be slower/costly)

## Complete Example .env

```env
# Your actual API key
OPENAI_API_KEY=sk-proj-aBcDeFgHiJkLmNoPqRsTuVwXyZ123456789

# Best quality model
OPENAI_MODEL=gpt-4o

# Balanced settings
TEMPERATURE=0.7
MAX_TOKENS=4000
```

## Testing Your Setup

After adding your API key:

```bash
# Run the application
./run.sh

# Or manually
streamlit run app/app.py
```

## Troubleshooting

### "Invalid API Key" Error
- ✅ Check that key starts with `sk-`
- ✅ No extra spaces or quotes
- ✅ Key is active on OpenAI platform

### "Rate Limit" Error
- ✅ Check your OpenAI usage limits
- ✅ Add payment method if needed
- ✅ Upgrade to paid plan

### "Model Not Found" Error
- ✅ Ensure you have access to the model
- ✅ Try `gpt-4o-mini` if `gpt-4o` doesn't work
- ✅ Check OpenAI documentation for available models

## Cost Estimation

### GPT-4o (Recommended)
- **Input**: $2.50 per 1M tokens
- **Output**: $10.00 per 1M tokens
- **Typical analysis**: $0.02 - $0.05 per query

### GPT-4o-mini (Budget-Friendly)
- **Input**: $0.15 per 1M tokens
- **Output**: $0.60 per 1M tokens
- **Typical analysis**: $0.001 - $0.003 per query

### GPT-4-turbo (Premium)
- **Input**: $10.00 per 1M tokens
- **Output**: $30.00 per 1M tokens
- **Typical analysis**: $0.08 - $0.15 per query

## Security Best Practices

✅ **Never commit .env to git** (already in .gitignore)  
✅ **Rotate keys regularly**  
✅ **Use organization keys for teams**  
✅ **Monitor usage on OpenAI dashboard**  
✅ **Set usage limits** in OpenAI settings  

## Ready to Start!

Once your `.env` is configured:

```bash
./run.sh
```

Your Product Thinking Studio will use the optimized settings for the **best possible AI-powered insights**! 🚀

---

**Need help?** Check [OpenAI Documentation](https://platform.openai.com/docs)
