#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
# from io import BytesIO


obj = subprocess.Popen(['python'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# c=bytes("hello")
# c=bytes("hello",'utf-8')

# obj.stdin.write('print("hello\n".encode())')
#print(type(c))
# obj.stdin.write("print(bytes('hello','utf-8'))")
# d = bytes(print(c),encoding='utf-8')
# obj.stdin.write(d)
# obj.stdin.write('print(c))\n')
obj.stdin.write(bytes("print('hello1')\n",encoding='utf-8'))
obj.stdin.write(bytes("print('hello2'\n)",encoding='utf-8'))


obj.communicate()