import django_heroku

from .settings_common import *

DEBUG = False
TEMPLATE_DEBUG = False

django_heroku.settings(locals())
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'