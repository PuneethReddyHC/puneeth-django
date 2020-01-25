# -*- coding: utf-8 -*-
from aldryn_client import forms


class Form(forms.BaseForm):
    enable_dashboard = forms.CheckboxField(
        'Enable dashboard',
        initial=True,
        required=False,
    )

    def to_settings(self, data, settings):
        settings['DIVIO_DJANGO_JET_ENABLE_DASHBOARD'] = data['enable_dashboard']

        # add our urls at the topmost position to override django.contrib.admin
        settings['ADDON_URLS'].insert(0, 'divio_django_jet.urls')

        # insert jet apps before django.contrib.admin
        dj_admin_app_index = settings['INSTALLED_APPS'].index('django.contrib.admin')
        settings['INSTALLED_APPS'].insert(dj_admin_app_index, 'jet')

        if settings['DIVIO_DJANGO_JET_ENABLE_DASHBOARD']:
            settings['INSTALLED_APPS'].insert(dj_admin_app_index, 'jet.dashboard')

        # ensure we have the django context processor installed
        dj_request_processor = 'django.template.context_processors.request'
        context_processors = settings['TEMPLATES'][0]['OPTIONS']['context_processors']
        if dj_request_processor not in context_processors:
            context_processors.append(dj_request_processor)
        return settings
