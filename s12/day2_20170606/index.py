#!/usr/bin/env python
#-*-coding:utf-8 -*-

#import lib
#print('index')

#import sys
#print (sys.argv)

#l1 = [11,22,33]
#l1 = list
#print(type(l1))

#import twisted
#from twisted.internet.protocol import ServerFactory


#import time
#age = 18
#a = time.time()
#factory = ServerFactory()

#print(type(age))

#name = str('eric') #str类的__init__方法
#result = name.__contains__('er6')
#result = 'er6' in name
#print(result)

#name = 'eric{0}'
#name.__format__("alex")
#print(name)
#import string

# name = "ERic"
# result = name.casefold()
# #print(result)
# #print("*********888**********")
# #8*'*'输出八个*号
# result = name.center(20,'*')
# print(result)
#
# name = 'jklmnkkl'
# result = name.count('k',0,6)
# print(result)

# name = '李杰'
# result = name.encode()
# print(result)

# name ='alex'
# result = name.endswith('e',0,3)
# print(result)

# name = 'a\tlex'
# result = name.expandtabs()
# print(len(result))

# name = 'alex'
# result = name.find('e')
# print(result)
# name = 'alex'
# result = name.index('ex')
# print(result)
# name = 'alex {name} as {id}'
# result = name.format(name='sb',id='eric')
# print(result)

# li = ['s','b','a','l','e','x']
# result = "_".join(li)
# print(result)

# intab = "aeiou"
# outtab = "12345"
# transtab = maketrans(intab,outtab)
#
# str = "this is string example...WOW!!!"
# print (str.translate(transtab,'xm'))

# name = 'alexissb'
# result = name.partition('is')
# print(result)

# name = 'alexissbaa'
# result = name.replace('a','o',2)
# print(result)

# name = """
# ak
# bb
# cc"""
# #result = name.splitlines()
# result = name.split("\n")
# print(result)

# with open('h.log') as f:
#     f.write()

# li = list([1,2,3])
# #li = list((1,2,3))
# print(li)
# #li.extend((11,22,))
# ret = li.pop(0)
# print(li,ret)

# li = [11,11,2,22,2]
# print(li)
# li.remove(11)
# print(li)

# li = [11,11,2,22,2]
# print(li)
# li.reverse()
# print(li)
#
# tu = (11,22,34,)
# tu = tuple((11,22,34,))
# tu = tuple([11,22,34,])
# l1 = [11,22,34,]
# tu =tuple(l1)
# li = list(tu)

# dic = {'k1':'v1','k2':'v2'}
# #new_dict = dic.fromkeys(['k1','k2','k3'],'v1')
# #dic = dict(k1='v1',k2='v2')
# print(dic['k1'])
# print(dic['k2'])
# print(dic.get('k3','alex'))
# print(dic)
# #dic['k3']
# print(dic)
# #print(new_dict)

# dic = {'k1':'v1','k2':'v2'}
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# for k in dic.keys():
#     print(k)
# for v in dic.values():
#     print(v)
# for k,v in dic.items():
#     print(k,v)

# dic = {'k1':'v1','k2':'v2'}
# # dic.pop('k1')
# # print(dic)
#
# dic.popitem()
# print(dic)

# dic = {'k1':'v1','k2':'v2'}
# dic['k3'] = 123
# dic.setdefault('k4','fdf')
# print(dic)

# dic = {'k1':'v1','k2':'v2'}
# ret = dic.update({'k3':123})
# print(dic)

dic = {}
all_list=[11,22,33,44,55,66,77,88,99,100]
for i in all_list:
    if i>66:
        if "k1" in dic.keys():
            dic['k1'].append(i)
        else:
            dic['k1'] = [i,]
    else:
        if "k2" in dic.keys():
            dic['k2'].append(i)
        else:
            dic['k2'] = [i,]