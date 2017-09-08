#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,time


if __name__ == '__main__':

    file_name = sys.argv[1]

    if not os.path.exists(file_name):
        #print("file doesn't exist.")
        exit("file doesn't exist.")

    f = open(file_name, 'r')
    first_len = len(f.read())
    #print('first_len',first_len)
    #f.seek(5)
    #print('f.seek(5):f.read()-->',f.read())
    f.close()
    time.sleep(5)
    while True:
        f = open(file_name, 'r')

        #content = f.readlines()
        content = f.read()
        # print("f.tell()",f.tell())
        # print(type(content))
        second_len =  len(content)
        # print("second_len:",second_len)
        # print('previous content:',content)
        if second_len > first_len:

            f.seek(first_len, 0)
            first_len = second_len
            #print("f.tell()",f.tell())
        #f.seek(0)
            content2 = f.read()
            # print('content2:',content2,end="")
            print(content2,end="")

        #f.seek(first_len,0)
        # new_file_content_index = f.seek(first_len)
        #print(content)
        #print(first_len)
        #print(type(content))
        # print('content:%s' %new_file_content_index.read())


        time.sleep(1)
        f.close()