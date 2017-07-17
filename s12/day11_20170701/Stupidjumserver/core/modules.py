#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine,and_,or_,func,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,UniqueConstraint,\
    DateTime
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy_utils import ChoiceType,Password

Base = declarative_base()

HostUser2Group = Table('hostuser_2_group',Base.metadata,#不是类，是实例，可以直接增删改查，而类需要先实例化才可以进行增删改查
            Column('hostuser_id',ForeignKey('host_user.id'),primary_key=True),#主键
            Column('group_id',ForeignKey('group.id'),primary_key=True)#主键。有两个主键。让两个字段结合起来非空且为1
                   )

UserProfile2Group = Table('userprofile_2_group',Base.metadata,#不是类，是实例，可以直接增删改查，而类需要先实例化才可以进行增删改查
            Column('userprofile_id',ForeignKey('user_profile.id'),primary_key=True),#主键
            Column('group_id',ForeignKey('group.id'),primary_key=True)#主键。有两个主键。让两个字段结合起来非空且为1
                   )

UserProfile2HostUser = Table('userprofile_2_hostuser',Base.metadata,#不是类，是实例，可以直接增删改查，而类需要先实例化才可以进行增删改查
            Column('userprofile_id',ForeignKey('user_profile.id'),primary_key=True),#主键
            Column('hostuser_id',ForeignKey('host_user.id'),primary_key=True)#主键。有两个主键。让两个字段结合起来非空且为1
                   )

class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer, default=22)

    def __repr__(self):#返回字符串格式
        return "<id=%s,hostname=%s,ip_addr=%s>" %(self.id, self.hostname, self.ip_addr)


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True,nullable=False)

    def __repr__(self):
        return "<id=%s,name=%s>" %(self.id, self.name)

class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer,primary_key=True)
    username = Column(String(64),unique=True,nullable=False)
    password = Column(String(255),nullable=False)
    host_list = relationship('HostUser',
                          secondary=UserProfile2HostUser,
                          backref='userprofiles')
    groups = relationship('Group',
                          secondary=UserProfile2Group,
                          backref='userprofiles')

    def __repr__(self):
        return "<id=%s,name=%s>" % (self.id, self.username)


class HostUser(Base):
    __tablename__ = 'host_user'
    id = Column(Integer,primary_key=True)
    host_id = Column(Integer,ForeignKey('host.id'))
    AuthTypes= [
        (u'ssh-paswd',u'SSH/Password'),
        (u'ssh-key',u'SSH/KEY'),
    ]
    auth_type = Column(ChoiceType(AuthTypes))
    username = Column(String(64),unique=True,nullable=False)
    password = Column(String(255))
    groups = relationship('Group',
                          secondary=HostUser2Group,
                          backref='host_list')

    __table_args__ = (UniqueConstraint('host_id','username','password',name='_host_username_uc'),)#联合唯一

    def __repr__(self):
        return "<id=%s,name=%s>" % (self.id, self.username)

class AuditLog(Base):
    __tablename__ = 'audit_log'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('user_profile.id'))
    hostuser_id = Column(Integer,ForeignKey('host_user.id'))
    action_choices = [
        (0,'CMD'),
        (1,'Login'),
        (2,'Logout'),
        (3,'GetFile'),
        (4,'SendFile'),
        (5,'Exception'),
    ]

    action_choices2 = [
        (u'cmd',u'CMD'),
        (u'login',u'Login'),
        (u'logout',u'Logout'),
    ]

    action_type = Column(ChoiceType(action_choices2))
    cmd = Column(String(255))
    date = Column(DateTime)

    user_profile = relationship('UserProfile')
    #bind_host = relationship('BindHost')

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/stupidjumpserver",echo=True)

Base.metadata.create_all(engine)#创建所有表结构


