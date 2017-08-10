#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import template
# from django.template.defaultfilters import stringfilter
from django.utils.html import format_html


register = template.Library()#自己注册到语法库里

@register.filter#自己注册到语法库里，注册成过滤语法
# @stringfilter
def upper(value):
    print("--value from template:",value)
    return value.upper()

@register.simple_tag
def guess_page(current_page,loop_num):
    offset = abs(current_page - loop_num)
    if offset < 3:
        if current_page == loop_num:
            page_ele = '''<li class ="active" > <a href="?page=%s" > %s </a> </li>''' %(loop_num,loop_num)
        else:
            page_ele = '''<li class ="" > <a href="?page=%s">%s</a></li>''' %(loop_num,loop_num)

        return  format_html(page_ele)
    else:
        return ''