#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.html import format_html

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name =models.CharField(max_length=32)
    email = models.EmailField()

    def __unicode__(self):
        return "<%s %s>" %(self.first_name,self.last_name)

    class Meta:
        verbose_name_plural = '作者'

class Publisher(models.Model):
    name = models.CharField(max_length=64,unique=True)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50,help_text='write your country here.',verbose_name='所属省')
    website = models.URLField()

    def __unicode__(self):
        return "<%s>" %(self.name)

class Book(models.Model):
    name = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)#多对多
    publisher = models.ForeignKey(Publisher)
    publish_date = models.DateField()#DataTimeField精确到秒
    status_choices = (('published',u'已出版'),
                      ('producing',u'待出版'),
                      ('forbidden',u'禁书'),

    )
    status = models.CharField(choices=status_choices,max_length=32,default='producing')
    def __unicode__(self):
        return "<%s>" % (self.name)

    def colored_status(self):
        if self.status == 'published':
            # format_td = format_html('<span style="padding:2px;background-color:yellowgreen;color:white">已出版</span>')
            format_td = format_html('<span style="padding:2px;background-color:yellowgreen;color:white">已出版</span>')

        elif self.status == 'producing':
            format_td = format_html('<span style="padding:2px;background-color:gray;color:white">待出版</span>')
        elif self.status == 'forbidden':
            format_td = format_html('<span style="padding:2px;background-color:red;color:white">禁书</span>')
        return format_td
    colored_status.short_description = 'status'


