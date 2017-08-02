#-*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    """
    用户
    """
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=60)
    account = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField('标签名称', max_length=10)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    """
    博客分类
    """
    name = models.CharField('标签名称', max_length=10)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    """
    博客
    """
    title = models.CharField('标题', max_length=30)
    content = models.TextField('内容')
    author = models.CharField('作者', max_length=10)
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    category = models.ForeignKey(Category, verbose_name='分类')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    """
    评论
    """
    blog = models.ForeignKey(Blog, verbose_name='博客')
    name = models.CharField('姓名', max_length=20)
    email = models.EmailField('邮箱')
    content = models.CharField('评论内容', max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content
