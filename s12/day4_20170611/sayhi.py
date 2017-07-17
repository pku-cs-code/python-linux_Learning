#!/usr/bin/env python

def login(func):
    def wrapper(arg):#也可以定义动态参数def wrapper(*args,**kargs)
        print("Login...",arg)
        return func(arg)  #需要执行
    return wrapper

#@login #sayhi=login(sayhi)
def sayhi(name):
    print("hi...",name)
    return 9

#a = sayhi("zhang")
sayhi=login(sayhi)
sayhi('zhang')
#print(a)