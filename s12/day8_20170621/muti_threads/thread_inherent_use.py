#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)#继承，旧式类的写法
        self.num = num
    def run(self):#类名称必须写成run，这是写死了的
        print("running on number:%s" %self.num)
        time.sleep(3)


if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)

    t1.start()
    t2.start()
    print(t1.getName())
    print(t2.getName())
    t1.join()#等待t1子线程执行完

    t2.join()#等待t2子线程执行完

    print("---main---")#主线程启动后和子线程没有关系，所以不等两个子线程，故---main---先打印
