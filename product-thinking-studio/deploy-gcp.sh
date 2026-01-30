#!/bin/bash

# Google Cloud Platform Deployment Script for Product Playground

set -e

echo "🚀 Deploying Product Playground to Google Cloud Platform"
echo ""

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ gcloud CLI not found. Please install it first:"
    echo "   curl https://sdk.cloud.google.com | bash"
    exit 1
fi

# Source gcloud path
if [ -f "$HOME/google-cloud-sdk/path.bash.inc" ]; then
    source "$HOME/google-cloud-sdk/path.bash.inc"
fi

echo "📋 Step 1: Configuration"
echo ""

# Ask for project ID
read -p "Enter your GCP Project ID (or press Enter to use current): " PROJECT_ID

if [ -z "$PROJECT_ID" ]; then
    PROJECT_ID=$(gcloud config get-value project 2>/dev/null)
    if [ -z "$PROJECT_ID" ]; then
        echo "❌ No project ID provided and no default project set"
        exit 1
    fi
fi

echo "Using project: $PROJECT_ID"
gcloud config set project "$PROJECT_ID"

# Ask for OpenAI API key
read -p "Enter your OpenAI API Key: " OPENAI_KEY

if [ -z "$OPENAI_KEY" ]; then
    echo "❌ OpenAI API key is required"
    exit 1
fi

# Choose deployment method
echo ""
echo "Choose deployment method:"
echo "1) Cloud Run (Recommended - Serverless, auto-scaling)"
echo "2) App Engine (Managed platform)"
read -p "Enter choice (1 or 2): " DEPLOY_METHOD

if [ "$DEPLOY_METHOD" = "1" ]; then
    echo ""
    echo "🐳 Step 2: Building container image"
    
    # Enable required APIs
    echo "Enabling required APIs..."
    gcloud services enable cloudbuild.googleapis.com run.googleapis.com
    
    # Build container image
    IMAGE_NAME="gcr.io/$PROJECT_ID/product-playground"
    echo "Building: $IMAGE_NAME"
    gcloud builds submit --tag "$IMAGE_NAME"
    
    echo ""
    echo "🚢 Step 3: Deploying to Cloud Run"
    
    # Deploy to Cloud Run
    gcloud run deploy product-playground \
        --image "$IMAGE_NAME" \
        --platform managed \
        --region us-central1 \
        --allow-unauthenticated \
        --set-env-vars "OPENAI_API_KEY=$OPENAI_KEY" \
        --memory 2Gi \
        --cpu 2 \
        --timeout 120s \
        --max-instances 10
    
    # Get the service URL
    SERVICE_URL=$(gcloud run services describe product-playground \
        --platform managed \
        --region us-central1 \
        --format 'value(status.url)')
    
    echo ""
    echo "✅ Deployment successful!"
    echo "🌐 Your app is live at: $SERVICE_URL"
    echo ""
    echo "📝 Next steps:"
    echo "   1. Visit: $SERVICE_URL/app"
    echo "   2. Test all 9 features"
    echo "   3. Set up custom domain (optional):"
    echo "      gcloud run domain-mappings create --service=product-playground --domain=yourdomain.com"
    
elif [ "$DEPLOY_METHOD" = "2" ]; then
    echo ""
    echo "🚀 Step 2: Deploying to App Engine"
    
    # Enable App Engine API
    gcloud services enable appengine.googleapis.com
    
    # Set OpenAI API key in app.yaml
    echo "Setting environment variables..."
    sed -i "s/OPENAI_API_KEY: .*/OPENAI_API_KEY: \"$OPENAI_KEY\"/" app.yaml
    
    # Deploy to App Engine
    gcloud app deploy --quiet
    
    # Get the service URL
    SERVICE_URL="https://$(gcloud app describe --format='value(defaultHostname)')"
    
    echo ""
    echo "✅ Deployment successful!"
    echo "🌐 Your app is live at: $SERVICE_URL"
    echo ""
    echo "📝 Next steps:"
    echo "   1. Visit: $SERVICE_URL/app"
    echo "   2. Test all 9 features"
    echo "   3. Set up custom domain:"
    echo "      gcloud app domain-mappings create yourdomain.com"
    
else
    echo "❌ Invalid choice. Please run the script again."
    exit 1
fi

echo ""
echo "📊 Monitoring:"
echo "   Logs: gcloud logging read 'resource.type=cloud_run_revision OR resource.type=gae_app' --limit 50"
echo "   Console: https://console.cloud.google.com/"
echo ""
echo "🎉 Deployment complete!"
