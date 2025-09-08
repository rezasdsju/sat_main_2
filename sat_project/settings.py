from pathlib import Path
import os
from decouple import config
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ================== SECURITY ==================
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)

# Railway Free Tier subdomain deploy করার জন্য
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])  # Development/testing purpose, production এ আপনার actual Railway subdomain ব্যবহার করুন

# ================== INSTALLED APPS ==================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'satgpt',
]

# ================== MIDDLEWARE ==================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sat_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sat_project.wsgi.application'

# ================== DATABASES ==================
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),  # Railway automatically provides this
        conn_max_age=600,
        ssl_require=True
    )
}

# ================== PASSWORD VALIDATORS ==================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ================== INTERNATIONALIZATION ==================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ================== STATIC FILES ==================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / 'home' / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ================== MEDIA FILES ==================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ================== DEFAULT AUTO FIELD ==================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ================== AUTH REDIRECT ==================
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
