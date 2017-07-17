#!/usr/bin/env python

def calc(n):
    print(n)
    if n/2 > 1:

        res = calc(n/2)
        #return calc(n/2)
        print('res',res)
    print('N:',n)
        #return res
    return n
calc(10)