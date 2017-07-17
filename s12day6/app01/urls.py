#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""s12day6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from app01 import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^p1/',views.page1),
    url(r'^p1_1/', views.page_1),

    #url(r'', views.index),#不能这样写
    url(r'cash/$', views.pay_by_cash),

    url(r'^articles/2003/$',views.special_case_2003,{'user':'zhang'}),#后面的每条都需要设置一个user参数
    # url(r'^articles/([0-9]{4})/$', views.year_archive),
    # url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    # url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),#这条放在前面不会会产生影响，因为这条不包含上条
    # url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+).(\w+)/$', views.article_detail),
]
