# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
import models
# Create your views here.
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from crm import forms
from permissions import check_permission
def dashboard(request):
    return render(request,'crm/dashboard.html')



# @check_permission
def customers(request):
    customer_list = models.Customer.objects.all()#获取结果集，但是没有提取
    paginator = Paginator(customer_list,2)

    page = request.GET.get('page')
    try:
        customer_objs = paginator.page(page)
    except PageNotAnInteger:
        customer_objs = paginator.page(1)#第一次访问没有page号，返回第一页
    except EmptyPage:
        customer_objs = paginator.page(paginator.num_pages)#超过page号返回最后一页

    # return render(request,'crm/customers.html',{'customer_list':customer_list})
    print('customer_list-->>',customer_objs)
    return render(request,'crm/customers.html',{'customer_list':customer_objs})#这里的customer_list是个包含了很多信息的对象

# @check_permission
def customer_detail(request,customer_id):
    customer_obj= models.Customer.objects.get(id=customer_id)
    print('request-->>',request)
    print("customer_obj-->>",customer_obj)
    print ('customer_id-->>',customer_id)
    if request.method == 'POST':
        form = forms.CustomerModelForm(request.POST,instance=customer_obj)#告诉修改customer_obj
        # print ('views request---:',request,('dir(request):',dir(request)))
        # print('--request.post:',request.POST)
        if form.is_valid():
            form.save()
            print('request url-->',request)
            print('request split-->',request.path.split('/'))
            base_url = "/".join(request.path.split('/')[0:-2])#最后一个不要
            #(u'request split-->', [u'', u'crm', u'customers', u'1', u''])

            # print('request url path:',base_url)
            # print("--form-->",form)
            # print("dir(form)", dir(form))

            return redirect(base_url)
        # else:
    else:
        form = forms.CustomerModelForm(instance=customer_obj)#在打开客户详细信息的页面如果是post修改形式，则把修改的数据传给后台
        #如果是其他方式，如get方式，就保持原有数据不变

    return render(request,'crm/customer_detail.html',{'customer_form':form})