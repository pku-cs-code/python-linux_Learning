#!/usr/bin/env python

print("lib")

t1 = (1,2,{'k1':'v1'})
#del t1[0]
#t1[2] = 123 #t1[2]字典元素
t1[2]['k1'] = 2
print (t1)