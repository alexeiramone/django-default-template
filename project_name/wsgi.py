# -*- coding: utf-8 -*-
# {% now "Y/m/d H:m" %} - Created

"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""

import os
settings_name = "settings.local" if os.name == 'nt' else "settings.remote"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_name)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
