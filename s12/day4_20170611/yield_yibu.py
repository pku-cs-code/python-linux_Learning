#!/usr/bin/env python
#_*_coding:utf-8 _*_

import time
def consumer(name):
    print("%s is 吃包子啦" %name)
    while True:
        baozi=yield
        print("包子[%s]来了，被[%s]吃了" %(baozi,name))

# def producer(name):
def producer():

    c = consumer('A')
    c2 = consumer('B')
    # c.__next__()
    # c2.__next__()
    c.next()
    c2.next()
    print("老子开始准备做包子了")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子！")
        #c.send('zhang')
        c.send(i)
        c2.send(i)

# producer("alex")
producer()