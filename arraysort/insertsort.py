# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:57:23 2017
思想：每步将一个待排序的记录，按其顺序码大小插入到前面已经排序的字序列的合适位置，直到全部插入排序完为止。
@author: shenliangLE
"""

def insertsort(arr):
    """
    implementation of insertion sort
    """
    length = len(arr)
    if length < 2:
        return arr
    for i in range(1, length):
        temp = arr[i]#要排序的数
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp #插入的位置
    return arr