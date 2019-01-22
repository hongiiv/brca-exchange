"""
Django settings for brca project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from site_settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

INSTALLED_APPS = [
    'users',
    'data.apps.DataConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework.authtoken',

    # project
    'brca',

    'corsheaders',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
    'brcaexchange.cloudapp.net',
    'brcaexchange.org',
    'brca-website.cloudapp.net',
    'brcaexchange-prod.gi.ucsc.edu'
)

ROOT_URLCONF = 'brca.urls'

TEMPLATES = [
    {'BACKEND': 'django.template.backends.django.DjangoTemplates',
     'DIRS': [[os.path.join(BASE_DIR, 'templates')]],
     'APP_DIRS': True,
     'OPTIONS': {
         'context_processors': [
             'django.template.context_processors.debug',
             'django.template.context_processors.request',
             'django.contrib.auth.context_processors.auth',
             'django.contrib.messages.context_processors.messages',
             'django.template.context_processors.request',
         ],
     },
     },
]

WSGI_APPLICATION = 'wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "uploads")
MEDIA_URL = "/site_media/media/"

DOWNLOADS_ROOT = os.path.join(PROJECT_ROOT, "downloads")
DOWNLOADS_URL = "/downloads/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'data/static'),
)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'noreply@brcaexchange.org'

AUTH_USER_MODEL = 'users.MyUser'

PASSWORD_RESET_LINK_DURATION = 1

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s | %(asctime)s | %(module)s | %(process)d | %(thread)d | %(message)s',
            'datefmt': "%m/%d/%Y %H:%M:%S"
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}
