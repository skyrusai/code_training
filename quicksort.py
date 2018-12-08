# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:28:14 2018

@author: shenliang-006
"""

#List=[1,2,3,4,5,6,7,8]

def quicksort(List):
    if len(List)<2:
        return List
    else:
        base=List[0]
        left=[m for m in List[1:] if m<base]
        
        right=[m for m in List[1:] if m>base]
        
        middle=[m for m in List if m ==base]
        
    
    return quicksort(left)+middle+quicksort(right)

array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
quicksort(array)
print(quicksort(array))



