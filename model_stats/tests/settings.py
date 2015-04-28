# -*- coding: utf-8 -*-

import os

DEBUG = True

APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',
    'model_stats.tests',
]

INTERNAL_APPS = [
    'model_stats',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

NOSE_ARGS = ['--nologcapture']

SECRET_KEY = 'secretkey'
