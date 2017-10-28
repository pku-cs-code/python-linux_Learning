#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb

with open('query.txt','rb') as f:
    content = f.read()
    content_li = content.split('&')
    print content_li
del content_li[0]
# content_li[0].remove()
print content_li
li = []
for i in range(len(content_li)):
     li.append(content_li[i].split('=')[1])
print li
query = li[0]
count = li[1]
pv = li[2]
page = li[3]
print('value of query:%s,count:%s,pv:%s,page:%s' %(query,count,pv,page))
conn = MySQLdb.connect(user='root',host='127.0.0.1',passwd='123456',db='saving')
cur  = conn.cursor()
reCount = cur.execute('insert into log(query,count,pv,page) values(%s,%s,%s,%s)',li)
print ("reCount:%s",reCount)
#conn.rollback()
conn.commit()
cur.close()
conn.close()





