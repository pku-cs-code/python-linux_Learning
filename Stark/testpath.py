#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

path1 = os.path.dirname(__file__)

print('The path1 is:', path1)

path2 = os.path.abspath(path1)

print ('The path2 is:', path2)
path4 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('path4:',path4)
print('hello.py join into path:',os.path.join(path4,'hello.py'))

# path3 = os.path.join(path1, 'hello.py')
#
# print ('The path3 is:',  path3)
#
# print('abspath of current file',os.path.abspath(__file__))