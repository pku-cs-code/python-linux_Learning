#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

# import shelve
# d = shelve.open("shelve_test")

class Test(object):
    def __init__(self,n):
        self.n = n

t = Test(123)
t2 = Test(12334)

name = ["alex","rain","test"]

f = open("pickle_test.pk1",'wb')
pickle.dump(name,f)
pickle.dump(t2,f)
pickle.dump(t,f)
f.close()

