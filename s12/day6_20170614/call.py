#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Foo(object):
    def __init__(self):
        print("__init__")
        self.n = 4
    # def __new__(cls, *args, **kwargs):
    #     print("__new__")
    def __call__(self, *args, **kwargs):
        print("__call__")
    def test(self):
        print("__test__")

obj =Foo() #执行__init__
#obj()       #执行__call__
#obj.test()
# print(obj.__dict__)
# print(type(obj))
# print(type(Foo))
# print(type(Foo()))

MyShinyClass = type('MyShinyClass',(Foo,),{"test":123,"name":"alex"})
a = MyShinyClass()
print(type(MyShinyClass))
print(MyShinyClass.test)
print(a.test)

