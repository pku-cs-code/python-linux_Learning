#!/usr/bin/env python
# -*- coding: utf-8 -*-

class error_caught(Exception):

    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message

#print(error_caught("tttt"))#调用。下面的是异常
a = 1

try:
    assert a == 2 #判断这个条件不成立则报错。明确判断条件是否符合，不符合则整个程序停止
                   #比较重要的判断条件
    #raise error_caught('my abnormal error')#触发异常
except error_caught as e:
    print(e)
else:#没出现异常则执行这个
    print("haha else")
finally:
    print("no matter right or wrong, run this anyway")