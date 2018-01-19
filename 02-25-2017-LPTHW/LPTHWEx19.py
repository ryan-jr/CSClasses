# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 02:32:44 2017

@author: rjr

A script to emphasize functions, and function args
"""


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("That's enough for a party")
    print("Get a party tray")



# Direct input
print("Directly")
cheese_and_crackers(20, 30)

# Using Variables
print("Variables")
cheese = 10
crackers = 200
cheese_and_crackers(cheese,crackers)

# Using Math
print("Math")
cheese_and_crackers(20 + 10, 30 + 50)

# Combining Things
print("Combo")
cheese_and_crackers(20 + cheese, 30 + crackers)
