#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
def sayhi(num):
    print("running on number:%s" %num)
    time.sleep(3)

if __name__ == '__main__':
    """
    t1 =threading.Thread(target=sayhi,args=(1,))#生成一个线程
    t2 =threading.Thread(target=sayhi,args=(2,))#生成另一个线程

    t1.start()
    t2.start()
    print(t1.getName())
    print(t2.getName())
    t1.join()#等待t1子线程执行完

    t2.join()#等待t2子线程执行完"""
    t_list = []
    for i in range(10):
        t = threading.Thread(target=sayhi,args=[i,])
        t.start()
        t_list.append(t)
    for j in t_list:
        j.join()
    print("---main---")#主线程启动后和子线程没有关系，所以不等两个子线程，故---main---先打印


