# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import authenticate,login,logout

@login_required#装饰器认证
def index(request):
    return render(request,'index.html')

def acc_login(request):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            #pass authentication
            login(request,user)#通过django验证
            return HttpResponseRedirect('/')#跳转
        else:
            log_err = "wrong username or password"
            return render(request,'login.html',{'log_err':log_err})


    return render(request,'login.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')