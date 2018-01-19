# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 02:21:32 2017

@author: rjr

A script that provides multiple examples of methods
"""

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg 2: {arg2}")
    
def print_one(arg1):
    print(f"arg1: {arg1}")
    

def print_none():
    print("nothing")
    


print_two("Ryan", "R")
print_two_again("Ryan", "Re")
print_one("First!")
print_none()