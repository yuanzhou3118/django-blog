# -*- coding: UTF-8 -*-
from django.shortcuts import render, render_to_response
from .models import *
from django.http import Http404
from .forms import CommentForm


def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render_to_response('blog-list.html', {'blogs': blogs})


def get_blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.NotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created_at'),
        'form': form
    }
    return render(request, 'blog-details.html', ctx)
