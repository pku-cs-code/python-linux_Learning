#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    if request.method == 'GET':
        html = '''
            <body>
                <h1>welcome to app01</h1>
                :::for_start
                <h2>user:|::name,name:|::username</h2>
                :::for_end
            </body>
        
        '''
        user_infos = [
            {'username': 'alex', 'name': 'zhang', },
            {'username': 'alex2', 'name': 'zhang2', },
            {'username': 'alex3', 'name': 'zhang3', },
            {'username': 'alex4', 'name': 'zhang4', },
        ]
        user_info ={
            'username':'alex',
            'name':'zhang',
        }
        print('user request:',request.GET.get('user'))
        # return render(request,'app01/index.html',{'user_obj':user_info})
        return render(request,'app01/index.html',{'user_objs':user_infos})

    else:
        return HttpResponse('transfered to zhang..success.')
    #return HttpResponse('index page')

def page1(request):
    return render(request,'app01/page1.html')

def page_1(request):
    return render(request,'app01/page1_1.html')

def pay_by_cash(request):
    return HttpResponse('pay_by_cash')

def special_case_2003(request,user):
    print('matched 2003',user)
    return HttpResponse('matched--->HttpResponse...')

def year_archive(request,year):#第二个参数给匹配到的值。会传给views
    #动态模糊的匹配，会把匹配的值当做一个参数传给函数
    print('',year)
    return HttpResponse(year)

def month_archive(request,year,month):
    print('-->',year,month)
    return HttpResponse("%s/%s" %(year,month))


def article_detail(request,year,month,article_id,file_type):
    print('-->',request,year,month,article_id,file_type)
    return HttpResponse("%s/%s--:[%s].[%s]" %(year,month,article_id,file_type))
