#!/usr/bin/env python

f = open('test.log','r+',encoding='utf-8')
#ret = f.read(2)
#python3是按字符读

# print(f.tell())
# f.seek(3)
#
# ret = f.read()
# # print(f.tell())
# print(ret)
# f.close()
#print(ret)

f.seek(2)
# print(f.read())
f.truncate()
f.close()

