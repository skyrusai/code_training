# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:24:11 2017

@author: shenliangLE
"""

def shellsort(arr):
    length=len(arr)
    step=length/2
    while step>0:
        for j in range(step,length):
            temp=arr[j]
            i=j
            while i>0 and arr[i-step]>temp:
               arr[i]=arr[i-step]
               i-=step
            arr[i]=temp   
        step=step/2
    return arr       
                      
def shellsort1(arr):
    length=len(arr)
    #D=length/3
    D=length/3
    
    while D>0:
        j=D
        while j<length:
            temp = arr[j]
            i = j
            while i > 0 and arr[i-D] > temp:
                arr[i] = arr[i-D]
                i -= D
            arr[i] = temp     
            j +=1
        D=D/2
    return arr                  
#import java.util.*;
#
#public class ShellSort {
#    public int[] shellSort(int[] A, int n) {
#        //要插入的纸牌
#        int temp,j,i;
#        //设定增量D,增量D/2逐渐减小
#        for(int D = n/2;D>=1;D=D/2){
#
#            //从下标d开始，对d组进行插入排序
#            for(j=D;j<n;j++){
#
#                temp = A[j];
#                for(i=j;i>=D&&A[i-D]>temp;i-=D){
#                    A[i]=A[i-D];
#                }
#
#                A[i]=temp;
#            }
#
#        }
#
#        return A;
#    }
#}        
            
    
