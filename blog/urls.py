from blog.views import *
from django.conf.urls import url
from django.urls import include
from django.urls import path
from blog.feeds import LatestPostsFeed, AtomSiteNewsFeed
app_name = "blogs"
urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", PostList.as_view(), name="blogs"),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("<slug:slug>/", post_detail, name="post_detail"),
    url(r'^summernote/', include('django_summernote.urls')),
    path('employer/blog/create', index, name='employer-blog-create'),
]

