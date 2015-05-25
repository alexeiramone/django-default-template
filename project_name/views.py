# -*- coding: utf-8 -*-
# {% now "Y/m/d H:m" %} - Created

# from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404
# from django import forms
# from django.conf import settings
from django.views.decorators.cache import cache_page

@cache_page(600)
def home(request):
    return render(request, 'index.html', {
            'span_main': 9,
            'span_sidebar': 3,
        })