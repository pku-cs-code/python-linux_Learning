#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multi_inherentance import D

a = D()
print(a.__module__)
"""出现两次deleting the ...deleting the ...是因为程序调用一次，模块调用一次
程序执行完统一销毁，后面才出现两次deleting the ...
"""
