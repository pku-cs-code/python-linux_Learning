#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

pool = redis.ConnectionPool(host='192.168.31.60')
#r = redis.Redis(host='192.168.31.60')
r = redis.Redis(connection_pool=pool)

#统计uv
r.delete("uv_count")
r.setbit("uv_count",5,1)
r.setbit("uv_count",8,1)
r.setbit("uv_count",3,1)
r.setbit("uv_count",3,1)
print("uv_count:",r.bitcount("uv_count"))#bitcount统计多少位是1
#r.set("uv_count")

n = '371'
r.set('t',n)
for i in n:
    print(i,ord(i),bin(ord(i))) #ord获取字符在ascii中的位置？bin是转成二进制
#r.setbit("t",5,1)
#r.setbit("t",6,0)
r.setbit("t",4,1)#4下标对应的是第5位

print("res:",r.get("t").decode())



#all_keys = r.keys()
# for k in all_keys:
#     #print(k, r.get(k).decode())
#     print(k, r.get(k))
#print(r.keys())
#r.set("Name","zzz",ex=3)
#r.set("Name","zzz",nx=True)
#r.set("Name","zzz",xx=True)
#print(r.get("Name"))

#print(r.getset("AGE","B"))#设置新值返回旧值
#print(r.get("AGE"))

"""
r.set("id","3123456789")
r.setbit("id",66,1)
print(r.getbit("id",5))
print(r.get("id"))
"""

#r.setrange("id",3,"AAA")
#print(r.getrange("id",0,-1))

