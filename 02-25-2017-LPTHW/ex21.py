# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:25:15 2017

@author: rjr

covering operations of functions and return statements
"""

def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b
    
def sub(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b
    
def multi(a, b):
    print(f"Multiplying {a} * {b}")   
    return a * b
    
def div(a, b):
    print(f"Dividing {a} / {b}")  
    return a / b

print("doing math with functions")

age = add(30, 5)
height = sub(78, 4)
weight = multi(90, 2)
iq = div(100, 2)


print(f"Age: {age}, height: {height}, weight: {weight}, IQ: {iq}")

what = add(age, sub(height, multi(weight, div(iq,2))))

print(what)
    
