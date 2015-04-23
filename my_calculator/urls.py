# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.conf import settings
from .views import SimpleStaticView


urlpatterns = patterns('',
    url(r'^api/', include('my_calculator.api.urls', namespace='api')),
    url(r'^calculator_form$', TemplateView.as_view(template_name='calculator_form.html'))
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^(?P<template_name>\w+)$', SimpleStaticView.as_view(), name='example'),
                            )