# -*- coding:UTF-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Article


# 创建view视图
def index(request):
    article_list = Article.objects.order_by('-create_time')[:10]
    print(article_list)
    return render(request, 'article/index.html', {'article_list': article_list})


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article/detail.html', {'article': article})
