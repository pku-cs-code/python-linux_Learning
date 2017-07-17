#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Role(object):
    ac = None #写在这里下面的实例不能调用，类的变量,类的方法
    members = 0  #可以用来统计人数等
    def __init__(self,name,role,weapon,life_value):  #初始化函数，初始化方法，自动执行，self是内存中的一个对象
                                                     #实例属性，实例变量，不是类属性
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_val = life_value
        Role.members += 1


    def buy_weapon(self,weapon):     #类下的第一个参数都是self来保证调用初始化函数
        print("%s is buying [%s]" %(self.name,weapon))  #上面的name不能被这里访问，调用上面的初始化方法
        #这里的参数weapon不能换成别的
        self.weapon = weapon
        print(self.ac)

print(Role.buy_weapon)#只要函数一执行这个buy_weapon就开辟内存地址了
                      #实例化后调用函数不是把所有的函数copy到自己的内存，而是访问Role的buy_weapon函数内存地址
                      #即使把函数buy_weapon拷贝到自己的实例，也需要调用函数的地址，因为函数需要知道你是谁才能调用，事实上实例不拷贝，
                      #只是访问函数的公共内存地址
p1 = Role("sanjiang","Police","B10",90)
#上面的相当于Role(p1,"sanjiang","Police","B10",90)
#p1叫做实例，Role的实例，self是实例本身，类本身是Role，生成实例

t1 =Role("chunyun","Terrorist","B11",100)
#Role.buy_weapon(p1,"ak")
p1.buy_weapon("AK47")  #相当于Role.buy_weapon(p1,"AK47")
t1.buy_weapon("B51")
#Role.buy_weapon(p1,"ak")

t2 =Role("T2","Terrorist","B17",100)
t3 =Role("T3","Terrorist","B19",100)


p1.ac = "china brand"#实例中又自己生成了自己的方法ac，和ac=None的ac不同
                      #创建了实例的一个变量ac，这时不会访问Role中的ac对象，故屏幕打印china brand
t1.ac = "US brand"
p1.ace = "china2 brand"
t1.ace = "US2 brand"

Role.ac = "Japanese brand"
Role.weapon = "XD"  #如果不定义则会属性attribute报错，因为没有定义。另外一个类生成则使用内存
                    #在Role的类里创建了一个对象weapon
print(Role.weapon)
#print(Role("aa"))

print("p1:",p1.weapon,p1.ac,p1.ace)
print("t1:",t1.weapon,t1.ac,t1.ace)
print("t2:",t2.weapon,t2.ac)
print("t3:",t3.weapon,t3.ac)

print(Role.members)
# print("P1:",p1.weapon)
# print("T1:",t1.weapon)




