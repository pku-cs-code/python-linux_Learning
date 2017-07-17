#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

# def bubble_sort(array):
#     for i in range(len(array)):
#         for j in range(i,len(array)):
#             if array[i] > array[j]:
#                 temp = array[i]
#                 array[i] = array[j]
#                 array[j] = temp


def bubble_sort(array):
    for i in range(len(array)):
        smallest_index = i
        for j in range(i,len(array)):
            if array[smallest_index] > array[j]:
                smallest_index = j
        temp = array[i]
        array[i] = array[smallest_index]
        array[smallest_index] = temp




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



