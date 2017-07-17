#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

# def bubble_sort(array):
#     for i in range(len(array)-1):
#         for j in range(i+1,len(array)):
#             if array[i] < array[j]:
#                 temp = array[j]
#                 array[j] = array[i]
#                 array[i] = temp

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp



if __name__ == '__main__':
    array = []
    #k = 0
    for i in range(5000):
        array.append(random.randrange(100000))
    print(array)
    array1 =array
    time_start = time.time()

    bubble_sort(array1)

    time_end =time.time()
    print(array1)
    print(time_end-time_start)


    # for i in range(len(array)):
    #     for j in range(len(array1)):
    #         if array[i] == array1[j]:
    #             k += 1
    # print(k)



