#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Schoolmember(object):
    member_nums = 0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        Schoolmember.member_nums += 1
        #print(self.member_nums)
        #self.member_nums += 1

        #print("school member [%s] is enrolled!"%self.name)
        #Schoolmember.member_nums不能写成self.member_nums。因为实例里没有这个值
        print("\033[32;1mThe [%s] school member [%s] is enrolled!\033[0m" %(Schoolmember.member_nums,self.name))
        #print("\033[32;1mThe [%s] school member [%s] is enrolled!\033[0m" %(self.member_nums,self.name))


    def tell(self):
        print("My name is [%s]" %self.name)

class Teacher(Schoolmember):
    def __init__(self,name,age,sex,course,salary):  #不写默认继承父类的init,可以先重写再继承。先创建再重写
        super(Teacher,self).__init__(name,age,sex)  #继承父类，再把name,age,sex拿过来
        #Schoolmember.__init__(self,name,age,sex) 经典类，旧式类
        self.course = course
        self.salary = salary

    def teaching(self):
        print("Teacher [%s] is teaching [%s}" %(self.name,self.course))

class Student(Schoolmember):
    def __init__(self,name,age,sex,course,tuition):
        super(Student, self).__init__(name,age,sex)
        self.course = course
        self.tuition = tuition

    def pay_tuition(self):
        print("cao, student [%s] paying tuition [%s]" %(self.name,self.tuition))

t1 = Teacher("alex",22,'F',"PY",1000)
t2 = Teacher("tenglan",25,'N/A',"PY",900)

s1 = Student("sanjiang",24,'Female',"python",15000)
s2 = Student("baoan",23,'Female',"python",15000)

t1.tell()
s1.tell()

t1.teaching()
s1.pay_tuition()
