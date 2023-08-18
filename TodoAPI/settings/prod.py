from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

DEBUG = False

ALLOWED_HOSTS += ["todorestapi-20432433159e.herokuapp.com"]

INSTALLED_APPS += [
    'rest_framework',
    'todos'
]
