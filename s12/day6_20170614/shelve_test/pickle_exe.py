#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
f = open("pickle_test.pk1",'rb')

class Test(object):
    def __init__(self,n):
        self.n = n



t = Test(123)
t2 = Test(12334)
a=pickle.load(f)
print(a)

b=pickle.load(f)
print(b)