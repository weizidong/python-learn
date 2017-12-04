# -*- coding:UTF-8 -*-
from django.db import models


# 创建数据模型
class Article(models.Model):
    title = models.CharField('题目', max_length=30)
    create_time = models.DateTimeField('发布时间')
    deleted = models.BooleanField('删除状态')
    pub_name = models.CharField('发布人', max_length=10)
    content = models.CharField('发布内容', max_length=20000)

    def __str__(self):
        return self.content
