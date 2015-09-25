# -*- coding: utf-8 -*-
# {% now "Y/m/d H:m" %} - Created

from settings.base import *

DEBUG = True

SITE_ID = 2

MEDIA_URL = 'http://127.0.0.1:8080/'

DATABASES['default']['PASSWORD'] = ''

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    "{{ project_name }}.context_processors.local",
    "django.core.context_processors.debug",
)

INSTALLED_APPS += (
   'debug_toolbar',
)

# python -m smtpd -n -c DebuggingServer localhost:1025
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_PORT = 1025
# EMAIL_SUBJECT_PREFIX = '[DummyEmail] '

