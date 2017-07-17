#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent

def foo():
    print("\033[32;1mrunning in foo\033[0m")
    #gevent.sleep(0)
    gevent.sleep(1)
    print("\033[32;1mexplicit context switch to foo again\033[0m")

def bar():
    print("explicit context to bar")
    #gevent.sleep(0)
    gevent.sleep(1)
    print("implicit context switch back to bar")

def ex():
    print("\033[31;1mexplicit context to ex\033[0m")
    #gevent.sleep(0)
    gevent.sleep(1)
    print("\033[31;1mimplicit context switch back to ex\033[0m")
#切换顺序不是一定的，随机
gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(ex),
]
)
