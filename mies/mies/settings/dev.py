from .base import *

# SECURITY WARNING: don't run with debug turned on in production!'192.168.0.132''192.168.1.4'
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'db_mies',

        'USER': 'postgres',

        'PASSWORD': '1234',

        'HOST': 'localhost',

        'PORT': '',

    }
}



