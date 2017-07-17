#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time


def insertion_sort(array):
    for i in range(1,len(array)):

        position = i #刚开始往左边走的第一个位置
        current_val = array[i]#先把当前值存下来
        while position > 0 and current_val < array[position-1]:
            array[position] = array[position-1]
            position -= 1
        array[position] = current_val#可以省略这句，好像也不能少？










if __name__ == '__main__':
    array = []
    for i in range(5000):
        array.append(random.randrange(100000))
    print(array)
    time_start = time.time()
    insertion_sort(array)
    time_end =time.time()
    print(array)
    print(time_end-time_start)



