#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy  import create_engine, Table, Column, Integer, String, MetaData, ForeignKey,select
metadata = MetaData()#实例化

user = Table('user',metadata,#父类实例化后传给Table。有点像Table继承metadata
             Column('id',Integer, primary_key=True),
             Column('name',String(20)),)

color = Table('color',metadata,
              Column('id',Integer, primary_key=True),
              Column('name',String(20)))
engine = create_engine("mysql+pymysql://root:123456@localhost:3306/test?charset=utf8mb4",max_overflow=5)
#engine = create_engine("mysql+pymysql://root:123456@192.168.31.60:3306/test",max_overflow=5)

#engine = create_engine("mysql+mysqldb://root:123456@:3306/test",max_overflow=5)

#metadata.create_all(engine)

#添加用户
conn = engine.connect()
# sql = user.insert().values(id=123,name='zhang')
# sql = user.insert().values(id=12,name='cai')
#sql = user.insert().values(name='caicai')

#sql = user.delete().where(user.c.id > 1)#删除用户,c代表column
#sql = user.delete().where(user.c.name ==  'zhang')#删除用户
#sql = select([user.c.id,])#需要导入select
sql = select([user,])#需要导入select

res = conn.execute(sql)
print(res.fetchall())

# sql = select([user.c.name,color.c.name]).where(user.c.id==color.c.id)
# res = conn.execute(sql)
# print(res.fetchall())

conn.close()

#
#conn = engine.connect()


