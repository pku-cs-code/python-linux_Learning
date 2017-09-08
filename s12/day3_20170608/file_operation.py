#!/usr/bin/env python
#-*- encoding:UTF-8 -*-
# import process


def process(string):
    print("string:",string)

# f = open('test.log','r+',encoding='utf-8')

while True:
    f = open('test.log','r+')



    char = f.read(1)
    while char:
        process(char)
        char = f.read(1)

    f.close()




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
#
# f.seek(2)
# # print(f.read())
#f.truncate()
# f.close()





