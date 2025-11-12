"""
Django settings for my_django_project project.
"""

import os
from pathlib import Path
import dj_database_url
from decouple import config  # pip install python-decouple

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------
# SECURITY SETTINGS
# -------------------

SECRET_KEY = config('SECRET_KEY', default='django-insecure-default-key')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=lambda v: [s.strip() for s in v.split(',')])

# -------------------
# APPLICATIONS
# -------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'my_app',

    # Third-party
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for static files in production
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_django_project.urls'

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

WSGI_APPLICATION = 'my_django_project.wsgi.application'

# -------------------
# DATABASE
# -------------------

DATABASES = {
    'default': dj_database_url.config(
        default=config(
            'DATABASE_URL',
            default='postgresql://vending_db_rp0h_user:qvDnsSmyRnzdUb7xE7vEYKtuEdaUjwEA@dpg-d4aeif8gjchc73flfgqg-a.singapore-postgres.render.com/vending_db_rp0h'
        )
    )
}

# -------------------
# PASSWORD VALIDATION
# -------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------
# INTERNATIONALIZATION
# -------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Indian/Mauritius'
USE_I18N = True
USE_TZ = True

# -------------------
# STATIC & MEDIA FILES
# -------------------

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# -------------------
# CORS (Optional)
# -------------------

CORS_ALLOW_ALL_ORIGINS = True  # adjust for production

# -------------------
# DEFAULT AUTO FIELD
# -------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
