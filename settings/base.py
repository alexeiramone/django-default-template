# -*- coding: utf-8 -*-
# {% now "Y/m/d H:m" %} - Created

import os

SITE_ID = 1

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)
URL_PREFIX = u'http://127.0.0.1:8000'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Alexei Martchenko', 'alexei@amdb.com.br'),
    ('Vagner Ynsei Fokama', 'vagner@amdb.com.br'),
)

MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_name|slice:":8" }}_db',                      # Or path to database file if using sqlite3.
        'USER': '{{ project_name|slice:":8" }}_dbuser',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
        'CONN_MAX_AGE': 300
    }
}

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'America/Sao_Paulo' # America/Sao_Paulo
LANGUAGE_CODE = 'pt-br'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, "_media")
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "_static")
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '{{ secret_key }}'

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
    'easy_maps',
    'amdb.core',
    'amdb.bootstrap3',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'handler_padrao': {                # define and name a handler
            'level': 'DEBUG',
            'class': 'logging.FileHandler', # set the logging class to log to a file
            'formatter': 'verbose',         # define the formatter to associate
            'filename': os.path.join(BASE_DIR, '_log', 'default.log') # log file
        },
    },
    'loggers': {
        'LOG_TESTE': {              # define a logger - give it a name
            'handlers': ['console','handler_padrao'], # specify what handler to associate
            'level': 'INFO',                 # specify the logging level
            'propagate': True,
        },
    }
}


GRAPPELLI_ADMIN_TITLE = u'{{ project_name|capfirst }}'


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        },
    }

#Email defaults
DEFAULT_FROM_EMAIL = u'Webmaster <webmaster@{{ project_name }}.com.br>'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = u''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = '[Django] '
EMAIL_USE_TLS = False

#filebrowser defaults
FILEBROWSER_VERSIONS = {
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 70, 'height': 70, 'opts': 'crop'},
    'free_small': {'verbose_name': 'Livre Pequena (2C 170px)', 'width': 170, 'height': '', 'opts': ''},
    'free_medium': {'verbose_name': 'Livre Média (4C 370px)', 'width': 370, 'height': '', 'opts': ''},
    'free_big': {'verbose_name': 'Livre Grande (8C 770px)', 'width': 770, 'height': '', 'opts': ''},

    'fixed_thumbnail': {'verbose_name': 'Thumbnail (1C 70x43)', 'width': 70, 'height': 43, 'opts': 'crop'},
    'fixed_listagem': {'verbose_name': 'Listagem (2C 170x106)', 'width': 170, 'height': 106, 'opts': 'crop'},
    'fixed_small': {'verbose_name': 'Chamada Pequena (3C 270x168)', 'width': 270, 'height': 168, 'opts': 'crop'},
    'fixed_medium': {'verbose_name': 'Chamada Média (6C 570x356)', 'width': 570, 'height': 356, 'opts': 'crop'},
    'fixed_big': {'verbose_name': 'Chamada Grande (9C 870x543)', 'width': 870, 'height': 543, 'opts': 'crop'},
    'fixed_large': {'verbose_name': 'Galeria Fixa (12C 1170px)', 'width': 1170, 'height': 731, 'opts': 'crop'},
}

FILEBROWSER_ADMIN_VERSIONS = ['free_small', 'free_medium', 'free_big', 'fixed_small', 'fixed_medium', 'fixed_large']
FILEBROWSER_ADMIN_THUMBNAIL = 'thumbnail'
FILEBROWSER_SEARCH_TRAVERSE = True
FILEBROWSER_NORMALIZE_FILENAME = True
FILEBROWSER_CONVERT_FILENAME = True
FILEBROWSER_DIRECTORY = ''
FILEBROWSER_VERSIONS_BASEDIR = '_versions/'

DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

EASY_MAPS_CENTER = (-41.3, 32)

TWITTER_USERNAME = None
GOOGLE_ANALYTICS_CODE = None
TYNT_CODE = None
GOOGLE_WEBMASTERS_CODE = None
BING_WEBMASTERS_CODE = None
ADDTHIS_CODE = None # 'ra-????????????????'


