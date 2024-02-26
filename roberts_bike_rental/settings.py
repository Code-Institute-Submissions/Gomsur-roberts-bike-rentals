"""
Django settings for roberts_bike_rental project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7!%*_%*0x9*#-k*1$b$^dax14hu2tazzrvk5tvj@#7vlg*h0ni'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['roberts-bistro-0918c883d3bc.herokuapp.com', '104.248.100.154', 'localhost', '127.0.0.1', '8000-gomsur-robertsbikerenta-teos8a0p2jr.ws-eu108.gitpod.io', 'roberts-bike-rental.herokuapp.com', '*.herokuapp.com']
CSRF_COOKIE_DOMAIN = 'gomsur-robertsbikerenta-teos8a0p2jr.ws-eu108.gitpod.io'
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://8000-gomsur-robertsbikerenta-teos8a0p2jr.ws-eu108.gitpod.io']
CSRF_COOKIE_DOMAIN = '8000-gomsur-robertsbikerenta-teos8a0p2jr.ws-eu108.gitpod.io'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'bike',
    'corsheaders',
    "accounts",  # new
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",

]

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8000",
    "http://127.0.0.1:9000",
    'https://8000-gomsur-robertsbikerenta-teos8a0p2jr.ws-eu108.gitpod.io',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'roberts_bike_rental.urls'

TEMPLATES = [
    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },

    },
]

WSGI_APPLICATION = 'roberts_bike_rental.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'robertsbikerentals',
#         'USER':'robertsbikerentals',
#         'PASSWORD':'robertsbikerentals',
#         'HOST':'207.154.248.72',
#         'PORT':'5432'
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
    

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

##########################################

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

##########################################

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = '/'

SESSION_COOKIE_AGE = 1800  # 30 minutes

#SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#SESSION_COOKIE_AGE = 180 # 3 minutes. "1209600(2 weeks)" by default

SESSION_SAVE_EVERY_REQUEST = True # "False" by default

##########################################

## https://www.w3schools.com/django/django_add_css_file_global.php

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [

    BASE_DIR / "static"

]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

##########################################
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'