#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
import time


def f1():
    f = open('templates/test1.html')
    data = f.read()
    f.close()
    db_str = str(time.time())
    data = data.replace('((x))',db_str)
    #jinjia2提供复杂的替换
    return data

def f2():
    from jinja2 import Template

    f = open('templates/test2.html')
    result = f.read()
    #f.close()
    template = Template(result)
    #jinja2渲染，接收了进行特殊的替换

    data = template.render(name='John Doe',user_list=['alex','eric'])
    return data.encode('utf-8')
    #return "F2"
routers = {
    '/index/':f1,
    '/news/':f2,
}

def Runserver(environ,start_response):
    #environ封装用户相关信息
    #environ读取url
    #if url=xxx


    start_response('200 OK',[('Content-Type','text/html')])
    #return '<h1>Hello, web</h1>'
    url = environ['PATH_INFO']

    if url in routers.keys():
        fun_name = routers[url]
        ret = fun_name()
        return ret

    # if url == '/index/':
    #     return "index"
    # elif url == '/news/':
    #     return 'news'
    else:
        return '404'



if __name__ == '__main__':
    #用python2可以执行
    #创建socket server对象
    httpd = make_server('',8000,Runserver)
    print("Serving HTTP on port 8000...")
    #while循环等待用户请求到来
    #只要有请求过来就执行Runserver函数
    httpd.serve_forever()

