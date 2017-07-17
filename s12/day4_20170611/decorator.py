#!/usr/bin/env python


def login(func):
    def inner(*arg,**kwargs):
        print("password user verificatiion...")
        return func(*arg,**kwargs)#tv
    #func()
    #return None
    return inner
#返回值是None类型

def home(name):
    print("welcom [%s]to homepage" % name)


@login
def tv(name,passwd=123):
    print("welcom [%s]to TV page  " % name)
    return 4
# def tv():
#     print("welcom [%s]to TV page  ")

@login
def movie(name):
    print("welcom [%s]to movie page" % name)


#不能是函数，应该是函数的内存指针
#tv = login(tv)
#@login就是相当于执行tv = login(tv)
#先找装饰器
t = tv('alex','123')
print(t)
movie('Alex')


