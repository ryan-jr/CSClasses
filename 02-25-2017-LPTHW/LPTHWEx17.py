# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 21:46:41 2017

@author: rjr

A script to copy text from one file to another
"""

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")


# Opening/reading data
in_file = open(from_file)
indata = in_file.read()

# Output progress to user, get confirmation
print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# Write data to new file
out_file = open(to_file, "w")
out_file.write(indata)

# Confirm and cleanup
print("Done")

out_file.close()
in_file.close()
