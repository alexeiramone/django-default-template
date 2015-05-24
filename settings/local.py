# -*- coding: utf-8 -*-
from settings.base import *

DEBUG = True

SITE_ID = 2

MEDIA_URL = 'http://localhost:8080/'

DATABASES['default']['PASSWORD'] = '{{ db_pass }}'

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    "revistatenis.context_processors.local",
    "django.core.context_processors.debug",
)

INSTALLED_APPS += (
   'debug_toolbar',
)

FBGALLERY_THUMBNAIL_VERSION = "fixed_thumbnail"
FBGALLERY_IMAGE_VERSION = "free_big"