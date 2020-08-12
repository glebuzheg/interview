from .settings_common import *
DEBUG = True

ALLOWED_HOSTS = '*'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'interview',
        'USER': 'postgres',
        'PASSWORD': '54trgfbv',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
