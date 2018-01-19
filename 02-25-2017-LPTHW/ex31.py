# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:48:57 2017

@author: rjr

Making a game with branching logic
"""



print("You enter a dark room with 2 doors, do you go through door 1 or 2?")

door = input("> ")

if door == "1":
    print("There is a bear eating cake, what do you do?")
    print("1.  Take the cake.")
    print("2.  Scream at the bear.")
    
    bear = input("> ")
    
        if bear == "1":
            print("The bear eats your face off.")
        elif bear == "2":
            print("The bear eats your legs.")
        else:
            print(f"Well doing {bear} is better, because the bear runs away.")

if door == "2":
    print("You end up staring into Cthulu's retina")
    print("1.  Blueberries")
    print("2.  Timecube")
    print("3.  D&G")
    
    insanity = input("> ")
    
        if insanity == "1" or insanity == "2":
            print("Your mind turns to jello")
        else:
            print("you get eaten by the ghost of Foucault" )
            
else:
    print("You wander around aimlessly")