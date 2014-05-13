# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function  # python3
from __future__ import unicode_literals, division  # python3

import os
from os.path import join as location
from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = location(BASE_DIR, "project")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    #'django.core.context_processors.csrf',
)

TEMPLATE_DIRS = (
    location(PROJECT_DIR, 'templates'),
)

MIDDLEWARE_CLASSES = global_settings.MIDDLEWARE_CLASSES + (
    'django.middleware.transaction.TransactionMiddleware',
    #'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = (
    'djangocms_admin_style',  # needs to be before admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # generic third party
    'south',
    'django_extensions',
    # own apps
    'project',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# is in settings_local.py

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Zurich'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = location(PROJECT_DIR, 'collected_static')
STATICFILES_DIRS = (
    location(PROJECT_DIR, 'static'),
)

MEDIA_ROOT = location(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

CMD_RUNSERVER = "runserver"

try:
    from project.settings_local import *
    if 'INSTALLED_APPS_LOCAL' in locals():
        INSTALLED_APPS = INSTALLED_APPS + INSTALLED_APPS_LOCAL
    if 'MIDDLEWARE_CLASSES_LOCAL' in locals():
        MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + MIDDLEWARE_CLASSES_LOCAL
    if 'HAYSTACK_CONNECTIONS_LOCALS' in locals():
        HAYSTACK_CONNECTIONS.update(HAYSTACK_CONNECTIONS_LOCALS)
except ImportError:
    pass
