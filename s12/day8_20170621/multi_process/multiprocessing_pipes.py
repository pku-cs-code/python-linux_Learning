#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process,Pipe

def f(conn):
    conn.send([42,None,'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn,child_conn = Pipe()
    p = Process(target=f,args=(child_conn))
    p2 = Process(target=f,args=(child_conn))#同时两个一块传数据
    p.start()
    p2.start()
    print(parent_conn.recv())
    p.join()

