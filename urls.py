# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.contrib import admin
import hello
import hello.views
from django.urls import path, include

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    # add your own patterns here
    
    path('careers/', include('jobsapp.urls'), name="careers-urls"),
    path('blogs/', include('blog.urls'), name="blogs-urls"),
    path('', include('accounts.urls'), name="account-urls"),
    path('api/', include([
        path('', include('jobsapp.api.urls')),
    ])),
    path("summernote/", include("django_summernote.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    url(r'^$', hello.views.home, name='home'),
    url(r'^contact$', hello.views.contact, name='contact'),
    url(r'^services$', hello.views.services, name='services'),
    url(r'^portfolio$', hello.views.portfolio, name='portfolio'),
    url(r'^portfolio-single$', hello.views.contact, name='portfolio-single'),
    url(r'^single-blog$', hello.views.contact, name='single-blog'),
    url(r'^about$', hello.views.about, name='about'),
    
    
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
