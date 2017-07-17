#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process,Pool,freeze_support
import time

def Foo(i):
    time.sleep(1)
    #print('exec....')
    return i+100

data = []
def Bar(arg):
    print('--->exec done:',arg)
    data.append(arg)

if __name__ == '__main__':
    freeze_support()

    pool = Pool(3)

    for i in range(10):
        pool.apply_async(func=Foo,args=(i,),callback=Bar)#callback回调函数，当Foo执行完会执行Bar，结果也会返回给Bar
                                                            #async异步。sync同步，不能掉callback

        #pool.apply(func=Foo,args=(i,))#同步
    print('end')
    pool.close()
    #print("--->",data)
    pool.join()
    print("--->",data)#子进程把结果返回给了主进程














