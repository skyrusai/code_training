# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:44:32 2018

@author: shenliang-006
"""

for l in range(101):
    if l==0:
        continue
    if l%3==0:
        if l%5==0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif l%5==0:
        print("Buzz")
    else:
        print(l)
        
    