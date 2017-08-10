#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import resolve
from django.shortcuts import render

perm_dic = {'view_customer_list':['customer_list','GET',[]] ,
               'view_customer_info':['customer_detail','GET',[]],
            # 'edit_own_customer_info': ['customer_detail','POST',['test']],#最后的列表示存储一个或多个参数
            'edit_own_customer_info': ['customer_detail', 'POST', ['qq','name']],  # 最后的列表示存储一个或多个参数

            }

def perm_check(*args,**kwargs):
    request = args[0]
    print ('--perm_check request--',request,('\r\ndir(args[0])'),dir(request))
    url_resolve_obj = resolve(request.path_info)#resolve成别名了customer_detail
    current_url_namespace = url_resolve_obj.url_name
    print('url namespace:',current_url_namespace)
    matched_flag = False
    matched_perm_key = None
    if current_url_namespace is not None:
        print('find perm..')
        for perm_key in perm_dic:
            perm_val = perm_dic[perm_key]
            if len(perm_val) == 3:
                url_namespace,request_method,request_args = perm_val
                print (url_namespace,current_url_namespace)
                if url_namespace == current_url_namespace:#matched the url
                    if request.method == request_method:
                        if not request_args:#if empty, matched directly.pass
                            matched_flag = True
                            matched_perm_key = perm_key
                            print ('matched...')
                            break#no need fro other perms
                        else:
                            for request_arg in request_args:
                                request_method_func = getattr(request,request_method)#如果属性reques_method存在，则返回request.request_method值
                                print('args[0].qq---',request.POST)
                                if request_method_func.get(request_arg) is not None:
                                    matched_flag = True
                                else:
                                    matched_flag = False
                                    print ('request arg [%s] not matched'%request_arg)
                                    break#no need further

                            if matched_flag == True:
                                print ('--passed permission check--')
                                matched_perm_key = perm_key
                                break
    else:#permission doesn't work
        return True#可以定义报错信息，

    if matched_flag == True:
        perm_str = 'crm.%s' %matched_perm_key
        if request.user.has_perm(perm_str):
            print ("\033[42;1m---passed permission check---\033[0m")
            return True
        else:
            print ("\033[41;1m--no permission ---\033[0m")
            print (request.user,perm_str)
            return False
    else:
        print ("\033[41;1m ---no matched perssion ---\033[0m")




def check_permission(func):
    def wrapper(*args,**kwargs):
        print('--start check permission--')
        if perm_check(*args,**kwargs) is not True:#no permission
            return render(args[0],'crm/403.html')#args[0]是那个request
        return func(*args,**kwargs)
    return wrapper