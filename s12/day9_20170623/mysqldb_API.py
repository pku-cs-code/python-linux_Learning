#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(host='192.168.31.60',user='root',passwd='123456',db='s12day9')
cur = conn.cursor()#连上mysql后处于mysql游标什么状态
#reCount = cur.execute('insert into students(name,sex,age,tel,nal) values(%s,%s,%s,%s,%s)',('jack','F',22,'13522','china'))
#前面的%和后面括号的对应上。如果是字符串，会帮你把数字转成字符串
#reCount = cur.execute('insert into students(name,sex,age,tel,nal) values(%s,%s,%s,%s,%s)',('rache','F',26,'13453','china'))
#reCount = cur.execute('insert into students(name,sex,age,tel,nal) values(%s,%s,%s,%s,%s)',('rache','F',26,'13453','china'))
#reCount = cur.execute('insert into students(name,sex,age,tel,nal) values(%s,%s,%s,%s,%s)',('rache','F',26,'13453','china'))
li =[
    ('alex','m',30,1234,'usa'),
    ('zhang','m',25,4321,'usa'),
    ('cai','m',26,6789,'cn'),
    ('zzz','m',27,9876,'cn'),
]
reCount =cur.executemany('insert into students(name,sex,age,tel,nal) values(%s,%s,%s,%s,%s)',li)
#reCount = cur.execute('select * from students')
#res = cur.fetchall()
#res = cur.fetchmany(3)
#res = cur.fetchone()

#print(res)
#conn.rollback()#回滚，前面有一个出错了都不会存数据
#如果rollback()后同样的数据不会写入，取消rollback()后写入，id值会增加，但之前rollback()时的数据没有了，找不回了
#提交事务后不能回滚
conn.commit()
cur.close()
conn.close()

print(reCount)