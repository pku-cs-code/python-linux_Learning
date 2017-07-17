#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal(object):#新式类有新的方法，在底层实现上与经典类不一样，可以多继承
# class Animal():#经典类
    def __init__(self,name):
        self.name = name
        #self.num = None
        self.__num = None #加__变成了私有属性，对外隐藏
    hobbie = 'meat'
    #classmethod和staticmethod日常中没怎么用
    @classmethod#装饰器把函数变成像类一样的方法，不能访问实例变量，只能访问类变量
    def talk(self):
        print("%s is talking .."%self.hobbie)
    @staticmethod#实例不知道这个方法了，
    def walk():#静态化方法后不能访问实例变量和类变量，walk()括号中的参数不能有self
        #self.hobbie = food
        #print("%s is walking .."%self.hobbie)
        print("%s is walking ..")
    # def walk(self):#静态化方法后不能访问实例变量和类变量，walk()括号中的参数不能有self
    #     #self.hobbie = food
    #     #print("%s is walking .."%self.hobbie)
    #     print(" is walking ..",self.name)
    @property#属性，加了property后就不是方法了，是一个属性
    def habbit(self):
        print("%s habbit is xxoo" %self.name)
    @property
    def total_players(self):
        return self.__num
        #return 3
    @total_players.setter#这样声明可以改变属性
    def total_players(self,num ):
        self.__num  = num
        print("total players:" ,self.__num )
        #return self.num
    #     #return 3
    @total_players.deleter#这样声明可以改变属性，删除了num属性，报错AttributeError: 'Animal' object has no attribute 'num'
    def total_players(self):
        print("total players got deleted.")
        del self.__num


#Animal.hobbie
# Animal.talk()
d = Animal("sanjiang")
#d.talk()
#d.walk()
d.habbit
#d.habbit()
# d.total_players = 3
print(d.total_players)
d.total_players = 3
# print("out:",d.__num)
d.__num  = 5#外部的
print('access private variable',d._Animal__num)#访问私有变量
print("out:",d.__num)#  此处的d.__num和d.total_players是不同的，前者是私有的
#del d.total_players
print(d.total_players)
#

# del d.total_players
# print(d.total_players)
#print(d.total_players)
