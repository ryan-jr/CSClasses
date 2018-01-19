# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 19:32:16 2017

@author: rjr
Covering the implementation of a while loop
"""

# Setting variables
i = 0
numbers = []

while i<6:
    print(f"At the top i is {i}")
    numbers.append(i)
    
    i += 1
    
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")
    
    print("The numbers")
    
    for num in numbers:
        print(num)
    

