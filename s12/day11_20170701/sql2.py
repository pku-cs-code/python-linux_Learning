#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine,and_,or_,func,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base()#生成一个sqlORM基类，不用metedata了
Host2Group = Table('host_2_group',Base.metadata,#不是类，是实例，可以直接增删改查，而类需要先实例化才可以进行增删改查
            Column('host_id',ForeignKey('host.id'),primary_key=True),#主键
            Column('group_id',ForeignKey('group.id'),primary_key=True)#主键。有两个主键。让两个字段结合起来非空且为1
                   )


#engine = create_engine("mysql+pymysql://root:123456@localhost:3306/test",echo=False)
engine = create_engine("mysql+pymysql://root:123456@localhost:3306/test",echo=True)

class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22)
    #group_id = Column(Integer,ForeignKey('group.id'))#一台主机对应一个组，一对多
    # group = relationship("Group")
    #group = relationship("Group",backref='host_list')#反向关联。也可以用back_populates，但back_populates是双向关联，需要两边都对应上

    groups = relationship('Group',secondary=Host2Group,backref='host_list')#关联上了，不用foreignkey
    #group = relationship("Group", back_populates='host_list')

    def __repr__(self):#返回字符串格式
        return "<id=%s,hostname=%s,ip_addr=%s>" %(self.id, self.hostname, self.ip_addr)

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True,nullable=False)
    #host_id = Column(Integer,ForeignKey('host.id'))
    #hosts = relationship("Host")
    # host_list = relationship("Host",back_populates='group')
    #host_list = relationship("Host",backref='group')

    def __repr__(self):
        return "<id=%s,name=%s>" %(self.id, self.name)



Base.metadata.create_all(engine)

if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine)#创建与数据库的会话session class，创建一个连接的实例，返回的是一个session class
    #返回的是一个类名
    session = SessionCls()#连接的实例
    '''
    h1 = Host(hostname='h1',ip_addr='127.0.0.1')
    h2 = Host(hostname='h2', ip_addr='192.168.31.60')
    h3 = Host(hostname='h3', ip_addr='192.168.31.61')
    # session.add(h1)
    # session.add(h2)
    session.add_all([h1,h2,h3]'''

    g1 = session.query(Group).first()
    groups = session.query(Group).all()
    #h1 = session.query(Host).filter(Host.hostname=='h1').first()
    h2 = session.query(Host).filter(Host.hostname=='h2').first()
    #h2.groups = groups[1:-1]
    print("---",h2.groups)
    print("---g1",g1.host_list)

    #h1.groups = groups
    #h1.groups.pop()
    # obj = session.query(Host).filter(Host.hostname=='localhost2').first()
    # print("++>",obj)
    # #obj.hostname = 'localhost2'
    # #session.delete(obj)
    # objs = session.query(Host).filter(and_(Host.hostname.like("ce%"),Host.port > 20)).all()
    # print("-->",objs)

    # g1 = Group(name='g1')
    # g2 = Group(name='g2')
    # g3 = Group(name='g3')
    # g4 = Group(name='g4')
    #
    # session.add_all([g1,g2,g3,g4,])

    # g5 = Group(name='g5')
    # session.add_all([g5,])

    #g5 = session.query(Group).filter(Group.name=='g5').first()
    # h = session.query(Host).filter(Host.hostname=='localhost').update({'group_id':g5.id})
    #h = session.query(Host).filter(Host.hostname=='localhost').first()
    #print("h1:",h.group.name)#这个没有关联打印不出来,需要relationship
    # print("g：",g5.hosts)
    #print("g：", g5.host_list)

    # h1 = Host(hostname='localhost',ip_addr='127.0.0.1',group_id=g5.id)
    #session.add(h1)
    #h2 = Host(hostname='centos', ip_addr='192.168.31.60')

    #objs = session.query(Host).join(Host.group).group_by(Group.name).all()
    #objs = session.query(Host,func.count(Group.name)).join(Host.group).group_by(Host.group_id).all()
    #objs = session.query(Host,func.count(Group.name)).join(Host.group).group_by(Host.id).all()
    #objs = session.query(Host,func.count(Group.name)).join(Host.group).group_by(Group.name).all()#每组有几台机器

    #print("--->",objs)
    session.commit()#这里commit才是真正地提交，可以回滚



