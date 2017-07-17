#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process,Lock

def f(l,i):
    l.acquire()
    try:
        print('helloworld',i)
    finally:
        pass
        l.release()

if __name__ =='__main__':
    lock = Lock()
    for num in range(100):
        Process(target=f,args=(lock,num)).start()
