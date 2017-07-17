#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process,Queue


def f(q):
    q.put([42,None,'hello'])

if __name__ == '__main__':
    que = Queue()
    p = Process(target=f,args=(que,))
    p2 = Process(target=f,args=(que,))
    p.start()
    p2.start()
    print('from parent process',que.get())
    print('from parent process',que.get())
    p.join()
