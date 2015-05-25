# -*- coding: utf-8 -*-
# {% now "Y/m/d H:m" %} - Created

from django.conf.urls import patterns, include, url
from django.contrib import admin

from filebrowser.sites import site

urlpatterns = patterns('',
    # url(r'^', include('amdb.core.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?:index\.html)*$', '{{ project_name }}.views.home', name='home'),
)
