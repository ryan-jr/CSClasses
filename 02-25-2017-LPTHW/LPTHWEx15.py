# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:45:36 2017

@author: rjr
"""

from sys import argv


script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


txt_again.close()
txt.close()