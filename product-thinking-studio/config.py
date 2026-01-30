"""
Production configuration for Product Playground
"""
import os

class ProductionConfig:
    """Production environment configuration"""
    
    # Flask settings
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24).hex())
    
    # API Keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Security settings
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hour
    
    # CORS settings
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*').split(',')
    
    # Performance settings
    SEND_FILE_MAX_AGE_DEFAULT = 31536000  # 1 year for static files
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max request size
    
    # Rate limiting
    RATELIMIT_ENABLED = True
    RATELIMIT_STORAGE_URL = os.getenv('REDIS_URL', 'memory://')
    RATELIMIT_DEFAULT = "100 per hour"
    RATELIMIT_HEADERS_ENABLED = True
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # AI Service settings
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o')
    OPENAI_TIMEOUT = int(os.getenv('OPENAI_TIMEOUT', '120'))
    OPENAI_MAX_RETRIES = int(os.getenv('OPENAI_MAX_RETRIES', '3'))
    
    # Feature flags
    ENABLE_WEB_SCRAPING = os.getenv('ENABLE_WEB_SCRAPING', 'true').lower() == 'true'
    ENABLE_PDF_DOWNLOAD = os.getenv('ENABLE_PDF_DOWNLOAD', 'true').lower() == 'true'
    ENABLE_ANALYTICS = os.getenv('ENABLE_ANALYTICS', 'false').lower() == 'true'


class DevelopmentConfig:
    """Development environment configuration"""
    
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'dev-secret-key-change-in-production'
    
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Disable security features for dev
    SESSION_COOKIE_SECURE = False
    
    # Performance
    SEND_FILE_MAX_AGE_DEFAULT = 0  # No caching in dev
    
    # Rate limiting (more permissive)
    RATELIMIT_ENABLED = False
    
    # Logging
    LOG_LEVEL = 'DEBUG'
    
    # Feature flags
    ENABLE_WEB_SCRAPING = True
    ENABLE_PDF_DOWNLOAD = True
    ENABLE_ANALYTICS = False


# Environment-based config selection
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config():
    """Get configuration based on FLASK_ENV"""
    env = os.getenv('FLASK_ENV', 'development')
    return config.get(env, config['default'])
