# -*- coding:UTF-8 -*-
from django.conf.urls import url
from article import views

# 配置相应的页面的url和view
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
]
