# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 21:31:32 2017

@author: rjr

Script to wipe a file and ask a user for input
"""

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want to do that, hit CTRL-C")
print("If you do want that hit RETURN")

input("?")

print("Opening the file...")

target = open(filename, "w")

print("Truncating the file")
target.truncate()

print("I will now ask you for 3 lines of input")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")


print("I'm going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("closing...")
target.close()



