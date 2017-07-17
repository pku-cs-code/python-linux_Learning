#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time


def quick_sort(array,start,end):
    #print('-->',start,end)
    if start >= end:
        return
    key = array[start]
    left_flag = start
    right_flag = end
    while left_flag < right_flag:
        while left_flag < right_flag and array[right_flag] > key:#代表要继续移动小旗子
            right_flag -= 1
        temp = array[left_flag]
        array[left_flag] = array[right_flag]
        array[right_flag] = temp

        #左边小旗子开始向右移动
        while left_flag < right_flag and array[left_flag] <= key:
            left_flag += 1
        #上面的循环跳出代表左边小旗子现在所处的位置的值比key大

        temp = array[left_flag]
        array[left_flag] = array[right_flag]
        array[right_flag] = temp
        #print(array)
    #开始把问题分半
    quick_sort(array,start,left_flag-1)
    quick_sort(array,left_flag+1,end)
    #quick_sort(array,right_flag,end)



if __name__ == '__main__':
    array = []
    for i in range(5000):
        array.append(random.randrange(100000))
    print(array)
    # array = [87, 80, 74, 49, 86, 96, 97, 22, 59, 60,80,22]
    #print(array)
    time_start = time.time()
    quick_sort(array,0,len(array)-1)
    time_end =time.time()
    print(array)
    print(time_end-time_start)



