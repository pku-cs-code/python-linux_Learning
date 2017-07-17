#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

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

    def __unicode__(self):
        return "<%s>" % (self.name)
