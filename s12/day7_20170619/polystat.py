#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

    hobbie = 'meat'#类属性

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):#重写了Animal的talk函数
        return 'Woof!Woof!'

def animal_talk(obj):  #obj是所有类的基类
    print(obj.name,obj.talk())

c = Cat("sanjiang")
d = Dog("Sanjiangyuan")#相当于Dog(d)

animal_talk(c)
animal_talk(d)

#animals = [Cat('Missy'),Dog('Lassie')]

# for animal in animals:
#     print (animal.name + ':' + animal.talk())