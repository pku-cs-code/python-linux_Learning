#!/usr/bin/env python

def fibnachi(arg1,arg2,stop):
    if arg1 == 0:
        print(arg1,arg2)
    arg3 = arg1 + arg2
    print(arg3)
    if arg3 < stop:
        fibnachi(arg2,arg3,stop)

fibnachi(0,1,100)