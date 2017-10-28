#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,sys,os

if __name__ == '__main__':

    file = sys.argv[1]
    print file
    if not os.path.isfile(file):
        exit("the file you input doesn't exist")


    f = open('test.txt','rb')
    first_len = len(f.read())

    f.close()
    while True:
        f2 = open('test.txt','rb')
        second_len = len(f2.read())
        if first_len < second_len:
            f2.seek(first_len)
            first_len = second_len
            print f2.read()
        time.sleep(1)
        f2.close()

