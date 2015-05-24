# -*- coding: utf-8 -*-
from settings.base import *

DEBUG = False
TEMPLATE_DEBUG = False

URL_PREFIX = u'http://www.{{ site_domain }}'

ALLOWED_HOSTS = ['.{{ project_name }}.uol.com.br', '.{{ site_domain }}']

DATABASES['default']['PASSWORD'] = '{{ db_pass }}'

TEMPLATE_CONTEXT_PROCESSORS += (
    "{{ project_name }}.context_processors.remote",
)

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'locmem_{{ project_name }}',
#         },
#     }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR + '/_cache',
        'TIMEOUT': 600, # DJ17-only 300 default
        'OPTIONS': {
            'MAX_ENTRIES': 500, #DJ17-only 300 default
        },
        'KEY_PREFIX': '{{ project_name }}',
    }
}

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
        'handler_teste': {                # define and name a handler
            'level': 'DEBUG',
            'class': 'logging.FileHandler', # set the logging class to log to a file
            'formatter': 'verbose',         # define the formatter to associate
            'filename': os.path.join(BASE_DIR, '_log', 'default.log') # log file
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            #'filters': ['special']
        },
    },
    'loggers': {
        'LOG_TESTE': {              # define a logger - give it a name
            'handlers': ['handler_teste'], # specify what handler to associate
            'level': 'INFO',                 # specify the logging level
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}


EMAIL_SUBJECT_PREFIX = ''
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = ''
MAILGUN_SERVER_NAME = 'mg.{{ site_domain }}'


TWITTER_USERNAME = '{{ project_name }}'
GOOGLE_ANALYTICS_CODE = 'UA-40696379-2'
TYNT_CODE = 'ahT0N-opGr5kOOacwqm_6l'
GOOGLE_WEBMASTERS_CODE = ['8524e35e655bacb9', '09a9d0b0b5f7d139']
BING_WEBMASTERS_CODE = None
ADDTHIS_CODE = 'ra-51966fd03329991f'
FACEBOOK_USERNAME = '{{ project_name }}'
DISQUS_SHORTNAME = '{{ project_name }}'
MSCONFIG_TILECOLOR = '#00aba9'

UOL_BANNERS_CONFIG = {
    'affiliate': 'par{{ project_name }}',
    'group': 6,
}

UOL_CATALYST_CODE = '{{ project_name }}'