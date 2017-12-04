# -*- coding:UTF-8 -*-
from django.contrib import admin
from .models import Article

# 在管理页面注册相应的管理模块
admin.site.register(Article)
