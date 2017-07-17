#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
import time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread:%s\n" %n)
    semaphore.release()

if __name__ == '__main__':
    num = 0
    semaphore = threading.BoundedSemaphore(3)#同时允许3个线程运行
    for i in range(20):
        t = threading.Thread(target=run,args=(i,))
        t.start()


while threading.active_count() != 1:
    pass
else:
    print('---all the threads done---')
    print(num)