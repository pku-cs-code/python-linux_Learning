#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
# from django.template.defaultfilters import stringfilter
from django.utils.html import format_html


register = template.Library()#自己注册到语法库里

@register.filter
def truncate_url(img_obj):
    # print(dir(img_url))
    # print(img_url.url)
    return img_obj.name.split('/',maxsplit=1)[-1]


@register.simple_tag
def filter_comment(article_obj):
    query_set = article_obj.comment_set.select_related()#根据文章反查评论
    comments = {
        'comment_count':query_set.filter(comment_type=1).count(),
        'thumb_count':query_set.filter(comment_type=2).count(),
    }

    return comments
