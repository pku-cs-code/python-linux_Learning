#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
class A(object):
    n = 'A'
    def f2(self):
        print("f2 from A")

class B:
    n = 'B'
    def f1(self):
        print("f1 from B")
    def f2(self):
        print("f2 from B")
class C(A):
    n = 'C'
    def f2(self):
        print("f2 from C")


class D(B,C):
    """Test class"""
    def __del__(self):#自己定义的，析构方法
        print("deleting the ...")

d = D()
d.f1()
d.f2()
print(d.n)
#print(d.__doc__)
d.__del__()
time.sleep(2)

print("haha")
