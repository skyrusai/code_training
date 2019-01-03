# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:09:59 2017
思想：每趟从待排序的记录序列中选择关键字最小的记录放置到已排序表的最前位置，直到全部排完。
@author: shenliangLE
"""

def selectionsort(arr):
    """
    implementation of selection sort
    """
    length=len(arr)
    k=0
    j=1
    while k<length-1:
         mini=arr[k]
         min=k
         while j<length:#k+1-length
             if mini>arr[j]:
                 mini=arr[j]
                 min=j
             j+=1
         arr[k],arr[min]=arr[min],arr[k]
         k+=1         
         j=k+1
    return arr

def selectionsort1(arr):    
    length=len(arr)
    for i in range(0,length-1):
        min_i=-1
        min=arr[i]
        for j in range(i + 1, length):
            if min>arr[j]:
                min_i=j
                min=arr[j]                 
        if min_i!=-1:
            arr[i],arr[min_i]=arr[min_i],arr[i]
    return arr  