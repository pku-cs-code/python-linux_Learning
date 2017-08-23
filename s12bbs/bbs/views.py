#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render,HttpResponseRedirect,HttpResponse

# Create your views here.
from bbs import models
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required

from bbs import models
from bbs import comment_handler

import json

from bbs import form

category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')  # 如果反向是 -'position_index'

def index(request):
    category_obj = models.Category.objects.get(position_index=1)
    article_list = models.Article.objects.filter(status='published')

    return render(request,'bbs/index.html',{'category_list':category_list,'article_list':article_list,'category_obj':category_obj})

def category(request,id):
    category_obj = models.Category.objects.get(id=id)
    if category_obj.position_index == 1:#首页
        article_list = models.Article.objects.filter(status='published')
    else:
        article_list = models.Article.objects.filter(category_id=category_obj.id,status='published')

    return render(request,'bbs/index.html',{'category_list':category_list,'category_obj':category_obj,'article_list':article_list})#要写在一个字典里

def acc_login(request):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            #pass authentication
            login(request,user)#通过django验证
            # return HttpResponseRedirect('/bbs/')#跳转
            return HttpResponseRedirect(request.GET.get('next') or '/bbs')#跳转

        else:
            log_err = "wrong username or password"
            return render(request, 'login.html', {'log_err':log_err})


    return render(request, 'login.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/bbs')

def article_detail(request,id):
    article_obj = models.Article.objects.get(id=id)
    # print('article_obj.comment_set.select_related()-->',article_obj.comment_set.select_related())#获取所有和该篇文章有关的评论
    # print('------end-----')
    comment_tree = comment_handler.build_tree(article_obj.comment_set.select_related())
    return render(request,'bbs/article_detail.html',{'article_obj':article_obj,'category_list':category_list,})
    pass


def comment(request):
    print(request.POST)
    if request.method == 'POST':
        new_comment_obj = models.Comment(article_id=request.POST.get('article_id'),
                                     parent_comment_id=request.POST.get('parent_comment_id') or None,
                                     comment_type = request.POST.get('comment_type'),
                                     user_id = request.user.userprofile.id,
                                     comment = request.POST.get('comment'),
                                     )
        new_comment_obj.save()


    return HttpResponse('post-comment-success')


def get_comments(request,article_id):
    article_obj = models.Article.objects.get(id=article_id)
    comment_tree = comment_handler.build_tree(article_obj.comment_set.select_related())
    tree_html = comment_handler.render_comment_tree(comment_tree)

    # return  HttpResponse(json.dumps(comment_tree))
    return  HttpResponse(tree_html)


# @login_required(login_url='/login/')
@login_required()

def new_article(request):

    if request.method == "GET":
        article_form = form.ArticleModelForm()
        return render(request,'bbs/new_article.html',{'article_form':article_form})
    elif request.method == "POST":
        print(request.POST)
        article_form = form.ArticleModelForm(request.POST,request.FILES)#django中图片文件是从request.FILES这个参数进去的
        if article_form.is_valid():
            data = article_form.cleaned_data
            data['author_id']  = request.user.userprofile.id

            print(article_form.cleaned_data)  # 变成一个字典

            article_obj = models.Article(**data)
            article_obj.save()
            # article_form.cleaned_data['author_id'] = request.user.userprofile.id
            # article_form.save()
            return HttpResponse('new article has been successfully published')

        else:
            return render(request, 'bbs/new_article.html', {'article_form': article_form})


def file_upload(request):
    print(request.FILES,request.FILES.get('filename'))#request.FILES.get('filename')是一个文件句柄，不是字符串
    file_obj = request.FILES.get('filename')
    with open('uploads/%s'%file_obj.name,'wb+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)

    return render(request, 'bbs/new_article.html')


def get_latest_article_count(request):
    latest_article_id = request.GET.get('latest_id')
    if latest_article_id:
        new_article_count = models.Article.objects.filter(id__gt = latest_article_id).count()

        #print('mew article count',new_article_count)
    else:
        new_article_count = 0
    return HttpResponse(json.dumps({'new_article_count': new_article_count}))
