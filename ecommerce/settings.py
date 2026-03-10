from pathlib import Path
import os
from db import DATABASES

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = 'django-insecure-30o*lba4)59$kpn!nvl65)#s%34=hzk=67e^sug$ski(=f08zd'
DEBUG = False
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'jazzmin',           # Must be above admin
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your Apps
    'accounts',
    'store',
    
    # Utilities
    'rest_framework',
    'drf_yasg',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # Top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS & CSRF
CORS_ALLOW_ALL_ORIGINS = True 
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    'https://dds0rq7n-8000.inc1.devtunnels.ms',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'

# Database
DATABASES = DATABASES

# Auth
AUTH_USER_MODEL = 'accounts.User'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static & Media Files
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# FIX: Media URL should not be '/'
# MEDIA_URL = '/media/' 
# MEDIA_ROOT = os.path.join(BASE_DIR, 'productImages')
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework
REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "accounts.utils.custom_exception_handler",
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ]
}

# Swagger
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': True,
    'LOGIN_URL': '/admin/login/',
    'LOGOUT_URL': '/admin/logout/',
}

# ========================================
# JAZZMIN CONFIGURATION (Corrected App Labels)
# ========================================

JAZZMIN_SETTINGS = {
    "site_title": "Local Baba Admin",
    "site_header": "Local Baba",
    "site_logo": "images/logo.avif",
    "login_logo": "images/logo.avif",
    "welcome_sign": "Welcome to Local Baba Admin Panel",
    "copyright": "Local Baba Marketplace",
    
    "search_model": "accounts.User", 
    "user_avatar": "profile_picture",
    
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "API Docs", "url": "/api/docs/", "new_window": True},
        {"model": "accounts.User"},
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "use_google_fonts": True,

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",
        "accounts.user": "fas fa-user-shield",
        "store.store": "fas fa-store",
        'store.storeproduct': "fas fa-box",
        "store.product": "fas fa-shopping-bag",
        "store.productcategory": "fas fa-th-list",

    },
    
    "order_with_respect_to": [
        "users",
        "accounts.User",
        "stores",
        "stores.Store", 
        "store",
        "store.ProductCategory",
        "store.Product",
        "auth",
    ],
    
    # Custom side menu apps/models
    "custom_links": {
        "stores": [{
            "name": "Pending Approvals",
            "url": "/admin/stores/store/?is_active__exact=0",
            "icon": "fas fa-clock",
            "permissions": ["stores.view_store"]
        }]
    },
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "brand_colour": "navbar-success",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "sidebar": "sidebar-dark-primary",
}