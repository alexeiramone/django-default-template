# -*- coding: utf-8 -*-
# {% now "Y/m/d H:m" %} - Created

import os

try:
    import newrelic.agent
    newrelic.agent.initialize('/home/dev/newrelic-{{ project_name }}.ini', 'django17')
except Exception, e:
    pass

settings_name = "settings.local" if os.name == 'nt' else "settings.remote"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_name)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
