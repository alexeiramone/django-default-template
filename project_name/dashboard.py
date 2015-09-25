# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        # append a group for "Administration" & "Applications"
        self.children.append(modules.Group(
            u'Administração',
            column=1,
            collapsible=True,
            children = [
                modules.AppList(
                    u'Áreas principais do site',
                    column=1,
                    css_classes=('collapse closed',),
                    exclude=('django.contrib.*',),
                ),
                modules.AppList(
                    u'Administração',
                    column=1,
                    collapsible=False,
                    models=('django.contrib.*',),
                ),
            ]
        ))
        
        # append an app list module for "Applications"
        # self.children.append(modules.AppList(
        #     _('AppList: Applications'),
        #     collapsible=True,
        #     column=1,
        #     css_classes=('collapse closed',),
        #     exclude=('django.contrib.*',),
        # ))
        
        # append an app list module for "Administration"
        # self.children.append(modules.ModelList(
        #     _('ModelList: Administration'),
        #     column=1,
        #     collapsible=False,
        #     models=('django.contrib.*',),
        # ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Tools'),
            column=2,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                    'description': u'Upload de imagens'
                },
                {
                    'title': 'Trello',
                    'url': 'https://trello.com/',
                    'external': True,
                    'description': u'Projeto no Trello'
                },
            ]
        ))
        
        # self.children.append(modules.LinkList(
        #     'Atalhos',
        #     column=2,
        #     children=[
        #         {
        #             'title': u'Transações Ativas',
        #             'url': '/admin/pagseguro/transacao/?o=-5&status__id__exact=ACTIVE',
        #             'external': False,
        #             'description': u'Últimas transações ativas'
        #         },
        #         {
        #             'title': 'Consulta Pagseguro 10',
        #             'url': '/pagseguro/consulta_pagseguro',
        #             'external': False,
        #             'description': u'Consulta modificações nas transações do Pagseguro nos últimos 10 dias'
        #         },
        #         {
        #             'title': 'Consulta Pagseguro 30',
        #             'url': '/pagseguro/consulta_pagseguro?q=30',
        #             'external': False,
        #             'description': u'Consulta modificações nas transações do Pagseguro nos últimos 30 dias'
        #         },
        #         # {
        #         #     'title': _('Grappelli Documentation'),
        #         #     'url': 'http://packages.python.org/django-grappelli/',
        #         #     'external': True,
        #         # },
        #         # {
        #         #     'title': _('Grappelli Google-Code'),
        #         #     'url': 'http://code.google.com/p/django-grappelli/',
        #         #     'external': True,
        #         # },
        #     ]
        # ))
        
        # append a feed module
        # self.children.append(modules.Feed(
        #     _('Latest Django News'),
        #     column=2,
        #     feed_url='http://www.djangoproject.com/rss/weblog/',
        #     limit=5
        # ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


