# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:19:17 2017

@author: rjr

Adding to and modifying lists
"""


ten_things = "Apples Oranges Crows Telephone Light SUgar"

print("There are not 10 things in the list yet")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Person"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now")
    
print("There we go: ", stuff)
print("Now we can modify stuff")


print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))




