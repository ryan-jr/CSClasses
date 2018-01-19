# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 19:12:37 2017

@author: rjr

Introduction to lists and for loops
"""

# Setting the variables
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Looping through the lists
for number in the_count:
    print(f"This is count{number}")


for fruit in fruits:
    print(f"The fruit{fruit}")
    
for i in change:
    print(f"I've got {i}")
    


# Creating an empty list
elements = []

# Using the range function to count
for i in range(0, 6):
    print(f"Adding {i} to the list")
    elements.append(i)
    
for i in elements:
    print(f"element was: {i}")

