#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shelve
d = shelve.open("shelve_test")

class Test(object):
    def __init__(self, n):
        self.n = n



t = Test(123)
t2 = Test(12334)

name = ["alex","rain","test"]
d["test"] = name #持久化列表
d["t1"] = t       #持久化类
d["t2"] = t2

#print(d.get("t2").n)
d.close()


