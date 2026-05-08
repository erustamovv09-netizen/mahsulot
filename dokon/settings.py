"""
Django settings for dokon project.
Haqiqiy server (Production) va Localhost uchun moslashtirilgan.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================
# 1. XAVFSIZLIK SOZLAMALARI (SECURITY)
# ==========================================
# Agar serverda SECRET_KEY berilmagan bo'lsa, local key ishlaydi
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-ix-9d419k53ii*=f2+r%3m%q!lz^!w@6k*czqqy44b14i77-v#')

# Serverda avtomatik False bo'ladi, kompyuterda True
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# Server manzilini qabul qilish
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')


# ==========================================
# 2. DASTURLAR VA MIDDLEWARE
# ==========================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Biz qo'shgan kutubxonalar
    'rest_framework',
    'corsheaders',
    
    # Bizning app
    'mahsulot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    # CORS doim CommonMiddleware dan oldin turishi kerak
    "corsheaders.middleware.CorsMiddleware", 
    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dokon.urls'

# Frontend (Next.js) bemalol ma'lumot olishi uchun ruxsat
CORS_ALLOW_ALL_ORIGINS = True

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

WSGI_APPLICATION = 'dokon.wsgi.application'


# ==========================================
# 3. MA'LUMOTLAR BAZASI (DATABASE)
# ==========================================
# Server o'zgaruvchilari orqali xavfsiz ulanish
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'mahsulot'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'root'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432')
    }
}


# Password validation
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


# ==========================================
# 4. STATIK VA MEDIYA FAYLLAR (STATIC & MEDIA)
# ==========================================
STATIC_URL = '/static/'
# Serverda admin panel dizayni ishlashi uchun juda muhim qator:
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')