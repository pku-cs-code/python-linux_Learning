#!/usr/bin/env python
# -*- coding: utf-8 -*-


def heap_adjust(array,heap_index):

    left_child = heap_index * 2
    right_child = heap_index * 2 +1

    node = array[heap_index-1]
    while True:
        if right_child > len(array):
            break
        if array[left_child-1] > node:
            tmp = array[left_child-1]
            array[left_child-1] = node
            array[heap_index-1] = tmp
            node = array[heap_index - 1]

        elif array[right_child-1] > node:
            tmp = array[right_child-1]
            array[right_child-1] = node
            array[heap_index - 1] = tmp
            node = array[heap_index - 1]
        else:
            break


def heap_sort(array):

    #先构建大顶堆
    i = int(len(array) / 2)
    for heap_index in range(i,0,-1):
        print(heap_index)
        heap_adjust(array,heap_index)





array = [16,9,21,13,4,11,3,15,8,22]

heap_sort(array)
print('-----', array)
