#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading

data = []
def run(n):
    time.sleep(5)
    data.append(n**n)
    print('from child')
    return n**n

res_list = []
for i in range(5):
    t =threading.Thread(target=run,args=[i,])
    t.start()
    res_list.append(t)
    #t.join()
for r in res_list:#一共花了3秒钟
    r.join(timeout=0.1)#主线程最多等1秒，如果超过了则主线程不等了。放在daemon不好使了
    #break
print("-----",data)
#print(dir(t))
#print(t.run())
#print(data)
#t.join()


