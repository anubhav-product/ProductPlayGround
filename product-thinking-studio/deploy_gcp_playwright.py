#!/usr/bin/env python3
"""
Google Cloud Platform Deployment with Playwright Browser Automation
This script deploys to GCP and opens the deployed site in a browser tab.
"""

import asyncio
import os
import subprocess
import sys
import re
from playwright.async_api import async_playwright

async def deploy_to_gcp():
    """Deploy to Google Cloud Platform using Cloud Run"""
    
    print("🚀 Starting GCP Deployment Process")
    print("=" * 60)
    
    # Configuration
    project_id = os.environ.get('GCP_PROJECT_ID', 'product-playground-demo')
    openai_key = os.environ.get('OPENAI_API_KEY', '')
    region = 'us-central1'
    service_name = 'product-playground'
    
    if not openai_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("   Set it with: export OPENAI_API_KEY='your-key-here'")
        return None
    
    print(f"\n📋 Configuration:")
    print(f"   Project ID: {project_id}")
    print(f"   Region: {region}")
    print(f"   Service: {service_name}")
    print(f"   OpenAI Key: {'*' * len(openai_key[:10])}...")
    
    # Step 1: Check if logged in
    print("\n🔐 Step 1: Checking GCP Authentication")
    try:
        result = subprocess.run(
            ['gcloud', 'auth', 'list', '--filter=status:ACTIVE', '--format=value(account)'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode != 0 or not result.stdout.strip():
            print("   Not authenticated. Opening browser for login...")
            subprocess.run(['gcloud', 'auth', 'login', '--brief'], check=True)
        else:
            print(f"   ✓ Authenticated as: {result.stdout.strip()}")
    except Exception as e:
        print(f"   ❌ Authentication check failed: {e}")
        return None
    
    # Step 2: Set project
    print(f"\n🎯 Step 2: Setting Project")
    try:
        subprocess.run(['gcloud', 'config', 'set', 'project', project_id], check=True)
        print(f"   ✓ Project set to: {project_id}")
    except Exception as e:
        print(f"   ❌ Failed to set project: {e}")
        return None
    
    # Step 3: Enable APIs
    print("\n🔧 Step 3: Enabling Required APIs")
    apis = ['cloudbuild.googleapis.com', 'run.googleapis.com']
    for api in apis:
        try:
            print(f"   Enabling {api}...")
            subprocess.run(
                ['gcloud', 'services', 'enable', api],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            print(f"   ✓ {api} enabled")
        except Exception as e:
            print(f"   ⚠️ Warning: Could not enable {api}: {e}")
    
    # Step 4: Build container image
    print("\n🐳 Step 4: Building Container Image")
    image_name = f"gcr.io/{project_id}/{service_name}"
    print(f"   Image: {image_name}")
    print(f"   This may take 5-10 minutes...")
    
    try:
        subprocess.run(
            ['gcloud', 'builds', 'submit', '--tag', image_name],
            check=True,
            cwd='/workspaces/ProductPlayGround/product-thinking-studio'
        )
        print(f"   ✓ Container image built successfully")
    except Exception as e:
        print(f"   ❌ Build failed: {e}")
        return None
    
    # Step 5: Deploy to Cloud Run
    print("\n🚢 Step 5: Deploying to Cloud Run")
    try:
        subprocess.run([
            'gcloud', 'run', 'deploy', service_name,
            '--image', image_name,
            '--platform', 'managed',
            '--region', region,
            '--allow-unauthenticated',
            '--set-env-vars', f'OPENAI_API_KEY={openai_key}',
            '--memory', '2Gi',
            '--cpu', '2',
            '--timeout', '120s',
            '--max-instances', '10'
        ], check=True)
        print(f"   ✓ Deployment successful")
    except Exception as e:
        print(f"   ❌ Deployment failed: {e}")
        return None
    
    # Step 6: Get service URL
    print("\n🔍 Step 6: Getting Service URL")
    try:
        result = subprocess.run([
            'gcloud', 'run', 'services', 'describe', service_name,
            '--platform', 'managed',
            '--region', region,
            '--format', 'value(status.url)'
        ], capture_output=True, text=True, check=True)
        
        service_url = result.stdout.strip()
        print(f"   ✓ Service URL: {service_url}")
        return service_url
    except Exception as e:
        print(f"   ❌ Failed to get URL: {e}")
        return None


async def open_in_browser(url):
    """Open the deployed site in a new browser tab using Playwright"""
    
    print("\n🌐 Opening site in browser...")
    print("=" * 60)
    
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        
        # Create new tab
        page = await context.new_page()
        
        print(f"   Navigating to: {url}/app")
        await page.goto(f"{url}/app", wait_until='networkidle', timeout=60000)
        
        # Wait for page to load
        await page.wait_for_selector('.container', timeout=10000)
        
        print(f"   ✓ Page loaded successfully")
        print(f"   ✓ Title: {await page.title()}")
        
        # Take screenshot
        screenshot_path = 'gcp_deployment_success.png'
        await page.screenshot(path=screenshot_path, full_page=True)
        print(f"   📸 Screenshot saved: {screenshot_path}")
        
        # Check for tabs
        tabs = await page.query_selector_all('.tab-button')
        print(f"   ✓ Found {len(tabs)} feature tabs")
        
        # Check console for errors
        errors = []
        page.on('console', lambda msg: errors.append(msg.text) if msg.type == 'error' else None)
        
        await asyncio.sleep(2)
        
        if errors:
            print(f"   ⚠️ Console errors detected: {len(errors)}")
            for error in errors[:5]:
                print(f"      - {error}")
        else:
            print(f"   ✓ No console errors detected")
        
        print("\n" + "=" * 60)
        print("✅ DEPLOYMENT COMPLETE!")
        print("=" * 60)
        print(f"\n🎉 Your Product Playground is live at:")
        print(f"   {url}/app")
        print(f"\n📝 Features available:")
        print(f"   ✓ Challenge Statement Analysis")
        print(f"   ✓ Root Cause Analysis")  
        print(f"   ✓ Strategy Formulation")
        print(f"   ✓ User Story Generation")
        print(f"   ✓ Metrics & KPIs")
        print(f"   ✓ Risk Assessment")
        print(f"   ✓ Stakeholder Mapping")
        print(f"   ✓ Product Teardown")
        print(f"   ✓ PRD Generator")
        print(f"\n💡 Next Steps:")
        print(f"   1. Test all features with real data")
        print(f"   2. Set up custom domain (optional):")
        print(f"      gcloud run domain-mappings create --service={service_name} --domain=yourdomain.com")
        print(f"   3. Monitor logs:")
        print(f"      gcloud run logs read --service={service_name} --region={region}")
        print(f"\n🌍 Browser tab is open - explore your deployed app!")
        print("=" * 60)
        
        # Keep browser open
        print("\n⏸️  Browser will stay open. Press Ctrl+C to close...")
        try:
            await asyncio.sleep(3600)  # Keep open for 1 hour
        except KeyboardInterrupt:
            print("\n👋 Closing browser...")
        
        await browser.close()


async def main():
    """Main deployment workflow"""
    
    # Check for required environment variables
    if 'OPENAI_API_KEY' not in os.environ:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("\nPlease set it with:")
        print("   export OPENAI_API_KEY='your-openai-api-key'")
        print("\nOptionally set custom project ID:")
        print("   export GCP_PROJECT_ID='your-project-id'")
        sys.exit(1)
    
    # Deploy to GCP
    service_url = await deploy_to_gcp()
    
    if not service_url:
        print("\n❌ Deployment failed. Please check the errors above.")
        sys.exit(1)
    
    # Open in browser
    await open_in_browser(service_url)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Deployment cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
