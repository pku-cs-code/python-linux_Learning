#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

os.environ["DJANGO_SETTINGS_MODULE"] = "s12day6.settings"
import django
django.setup()

from blog import models
from django.db.models import F
from django.db.models import Q,Avg,Sum,Min,Max,Count

# objs = models.Entry.objects.filter(n_comments__lte=F('n_pingbacks'))
# objs = models.Entry.objects.filter(n_comments__lte=F('n_pingbacks')/2)
# objs = models.Entry.objects.filter(n_comments__lte=F('n_pingbacks'),
#                                    pub_date__gt='2016-05-20')#and的关系

# obj = models.Entry.objects.get(blog__name__contains='科技')
#
# objs = models.Entry.objects.filter(Q(n_comments__lte=F('n_pingbacks'))|Q(pub_date__gt='2017-08-05')
#                                    )#and的关系

# models.Entry.objects.update(n_pingbacks=F('n_pingbacks')+1)#统一自增，只能在Entry里自增，不能外键关联修改
print(models.Entry.objects.all().aggregate(Avg('n_pingbacks'),Sum('n_pingbacks'),Min('n_pingbacks'),
                                           Max('n_pingbacks')))

# print(objs)

from app01 import models as book_models
pub_obj = book_models.Publisher.objects.last()
#print(pub_obj.name,pub_obj.book_set.select_related())#表结构在数据库里是小写的，book是表名，后面的set是反向查询自己带的
#反向关联查询

# print(book_models.Publisher.objects.annotate(book_nums=Count('book')))
# pub_objs = book_models.Publisher.objects.annotate(book_nums=Count('book'))
#
# for publisher in pub_objs:
#     print publisher.book_nums

# print(models.Entry.objects.values())

# print(models.Entry.objects.values()[0])
# print(models.Entry.objects.values_list()[0])#取元素为元组的形式
# print(models.Entry.objects.values_list('pub_date').annotate(Count('pub_date')))
print(book_models.Book.objects.values_list('publish_date').annotate(Count('publish_date')))#基于表内字段的分类统计
print(book_models.Book.objects.values_list('publisher'))



"""
entry = models.Entry.objects.get(pk=1)
# entry = models.Entry.objects.filter(pk=1)

# tech_blog = models.Blog.objects.get(id=2)

tech_blog = models.Blog.objects.get(name='科技')

entry.blog = tech_blog
# entry.blog_id = tech_blog.id
entry.save()
print(entry,tech_blog)"""