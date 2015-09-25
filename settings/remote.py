# -*- coding: utf-8 -*-
# {% now "Y/m/d H:m" %} - Created

from settings.base import *

DEBUG = False
TEMPLATE_DEBUG = False

URL_PREFIX = u'http://www.{{ project_name }}.com.br'

ALLOWED_HOSTS = ['.{{ project_name }}.uol.com.br', '.{{ project_name }}.com.br', '{{ project_name }}.amdb.com.br']

DATABASES['default']['PASSWORD'] = ''

TEMPLATE_CONTEXT_PROCESSORS += (
    "amdb.core.context_processors.remote",
    "{{ project_name }}.context_processors.remote",
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 600, # DJ17-only 300 default
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
MAILGUN_SERVER_NAME = 'mg.{{ project_name }}.com.br'


# UOL_BANNERS_CONFIG = {
#     'site': 'par',
#     'affiliate': 'par{{ project_name }}',
#     'chan': '',
#     'subchan': 'outros',
#     'campaignuol': '1',
#     'group': '6',
#     'floater': 'true',
#     'platform': 'web',
# }

# UOL_BANNERS_CONFIG_CHAN_PREFIX = 'par{{ project_name }}'
# UOL_CATALYST_CODE = '{{ project_name }}'
