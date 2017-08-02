# -*- coding: UTF-8 -*-
from django import forms

class CommentForm(forms.Form):

    name = forms.CharField(label='姓名', max_length=16, error_messages={
        'required': '请输入您的姓名',
        'max_length': '名字太长了'
    })

    email = forms.EmailField(label='邮箱', error_messages={
        'required': '请输入邮箱',
        'valid': '邮箱格式不正确'
    })

    content = forms.CharField(label='评论内容', error_messages={
        'required': '请填写您的评论内容！',
        'max_length': '评论内容太长咯'
    })
