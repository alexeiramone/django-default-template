# -*- coding: UTF-8 -*-
# {% now "Y/m/d H:m" %} - Created

from django.utils import timezone

def base(request):
    """
    Tudo o que vai na página do site
    """
    retorno = {
        'BASE_BREADCRUMB_SEPARATOR': '&raquo;',
        'BASE_REGULAR_SEPARATOR': '&middot;',
        'BASE_COPYRIGHT_YEARS': '%d-%d' % (1997,timezone.now().year),
    }
    return retorno

def local(request):
    return base(request)

def remote(request):
    retorno = base(request)
    return retorno
