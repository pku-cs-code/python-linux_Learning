#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading,queue
import time

def consumer(n):
    while True:

        print("\033[32;1mconsumer [%s]\033[0m get task: %s" %(n,q.get()))
        time.sleep(1)
        q.task_done()


def producer(n):
    count = 1
    while True:

        #time.sleep(1)
        if q.qsize() <3:

            print("producer [%s] produced a new task:%s" % (n, count))
            # for i in range(2):
            #     print("producer [%s] produced a new task:%s" %(n,i))
            q.put(count)
            count += 1
            q.join()#qsize is empty.如果join之后就挂起了，不占cpu资源
            print('all tasks has been consumed by consumers.')



q = queue.Queue()

c1 = threading.Thread(target=consumer,args=[1,])
c2 = threading.Thread(target=consumer,args=[2,])
c3 = threading.Thread(target=consumer,args=[3,])

p = threading.Thread(target=producer,args=["alex",])
p2 = threading.Thread(target=producer,args=["zhang",])
# p3 = threading.Thread(target=producer,args=["ZZ",])
# p4= threading.Thread(target=producer,args=["Z",])
# p5= threading.Thread(target=producer,args=["Zzz",])

c1.start()
c2.start()
c3.start()
p.start()
p2.start()
# p3.start()
# p4.start()
# p5.start()


