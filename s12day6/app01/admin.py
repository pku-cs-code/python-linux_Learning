#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
import models

def make_forbidden(modelAdmin,request,queryset):#可以后台获取到这些然后批量操作
    print ('--->',request,queryset)
    queryset.update(status='forbidden')
    make_forbidden.short_description = 'set to forbidden'

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','publisher','publish_date','colored_status','status',)#横向显示
    # list_display = ('id','name','publisher','publish_date','colored_status',)#横向显示

    # list_display = ('name','publisher','authors','publish_date')#这里不能用authors，因为authors可能一行显示不了，
    # 不能多对多，需要查询其他关联数据库

    search_fields = ('name','publisher__name')#__是关联到另外一个表，搜索查询
    list_filter = ('publisher','publish_date')#右侧过滤
    list_editable = ('name','publish_date',)#list_display设置id后就可以改了，因为不设置那么name为主键，修改不了
    list_per_page = 10   #每页显示多少
    #list_select_related = ('publisher',)#没用过
    filter_horizontal = ('authors',)#book进入选择更方便，for many to many
    raw_id_fields = ('publisher',)#改publisher可以搜索， for 外键
    actions = [make_forbidden,]





admin.site.register(models.Author)
admin.site.register(models.Publisher)
admin.site.register(models.Book,BookAdmin) #自己写的类作为参数传进注册里面
