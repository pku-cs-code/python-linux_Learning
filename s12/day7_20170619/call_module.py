#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Foo:
    def __init__(self):
        """test"""
        print("__init__")
        self.n = 4

    # def __new__(cls, *args, **kwargs):#如果重写则整个类变化，程序可能不好使了
    #     print("__new__")
    def __call__(self, *args, **kwargs):

        print("__call__")
    def test(self):
        print("__test__")

obj = Foo()
#obj()
#obj.test()

print(obj.__doc__)
print(obj.__dict__)#查看一个类有多少变量
print(type(Foo))
print(type(obj))

class Foo:
    print("foo")

MyShinyClass = type('MyShiyClass',(Foo,),{"test":"123","name":"zhang"})
print(type(MyShinyClass))
a = MyShinyClass()
#print(a.__dict__)
print(a.test)
print(MyShinyClass.test)