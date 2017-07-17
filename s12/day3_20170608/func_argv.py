#!/usr/bin/env python

"""
def show(argv,argv2):
    print(argv,argv2)

show('kkkk')
"""

"""
#默认参数
def show(argv,argv2=999):
    print(argv,argv2)

show('kkkk')
show('kkkk','000')
#默认参数必须放在最后
"""

"""
#指定参数
def show(a1,a2):
    print(a1,a2)

show(a2=123,a1=999)
"""
"""
def show(arg):
    print(arg)
n=[11,22,33,44]
show(n)
"""

# def show(*arg):
#     print(arg,type(arg))
# show(1,2)

#动态参数
# def show(**arg):
#     print(arg,type(arg))
# show(n1=12,uu=123,bb=999)

"""
def show(*args,**kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))

#show(11,22,33,n1=88,)
l = [11,22,33,]
d = {'n1':'88','n2':'99'}
show(l,d)
show(*l,**d)
"""
"""
s1 = "{0} is {1}"
l = ['alex','2b']
result = s1.format(*l)
print(result)
"""

"""
s1 = "{name} is {acter}"
d ={'name':'alex','acter':'sb'}
result = s1.format(**d)
print(result)
"""

"""
def func(a):
    b = a + 1
    return b

result = func(4)
print(result)
"""

"""
func = lambda a:a+1
#函数自动加了return值
#创建形式参数a
#函数内容a+1，结果return
#lambda表达式是简单函数的表达方式

re = func(99)
print(re)
"""

"""
class Foo:
    def __repr__(self):
        return 'bbbb'

f = Foo()
ret = ascii(f)
print(ret)
"""

"""
p = bytearray('无配置',encoding='utf-8',)
print(p)
"""

import random
ret = random.randint(1,99)
print(ret)

