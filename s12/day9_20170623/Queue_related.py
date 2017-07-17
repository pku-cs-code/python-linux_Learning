#!/usr/bin/env python
# -*- coding: utf-8 -*-

import queue

class Foo(object):
    def __init__(self,n):
        self.n = n


#q = queue.Queue(maxsize=30)
# q  = queue.LifoQueue(maxsize=30)
q  = queue.PriorityQueue(maxsize=30)#越小的优先级越大

q.put((1,[1,2,3]))#以元组的形式设定优先级，元组里的第二个元素是put的内容
#q.put(Foo(1))
q.put((10,1))
q.put((5,30),timeout=2)

#q.get(timeout=3)
#data = q.get_nowait()
q.put((2,2))
print(q.get())
print(q.get())
print(q.get())
print(q.get())
#data2 = q.get_nowait()
#print(data2,type(data2))

#print(data,type(data))
#print(type(q.full()))
#print(q.full())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# #print(q.get())
# q.task_done()













