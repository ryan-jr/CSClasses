# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 19:45:33 2017

@author: rjr

Going over branches/functions
"""

from sys import exit

def gold_room():
    print("This room is full of gold, how much do you take?")

    choice = int(input("> "))
    
    if choice < 50:
        print("You're not greedy!")
        exit(0)
    else:
        dead("You were too greedy!")
        
def bear_room():
    print("There's a bear here that has a bunch of honey in front of a door")
    print("How do you move the bear? TAKE its honey? TAUNT it?")
    bear_moved = False
    print("Choose either TAKE or TAUNT")
    
    while True:
        choice = input("> ")
    
        if choice == "TAKE":
            dead("The bear kills you")
        elif choice == "TAUNT" and not bear_moved:
            bear_moved = True
            print("The bear has moved from the door, you can OPEN the door now")
        elif choice == "OPEN" and bear_moved:
            gold_room()
        else:
            print("The bear gets mad and eats you")
            exit(0)
        
def cthulu_room():
    print("Here is Cthulu")
    print("Do you FLEE, or EAT?")
    
    choice = input("> ")
    
    if "FLEE" in choice:
        start()
    if "EAT" in choice:
        dead("You eat until you explode")
    else:
        cthulu_room()
        
def dead(why):
    print(why)
    exit(0)
        
def start():
    print("You are in a dark room with doors to the LEFT and RIGHT")
    print("Which door do you take?")
    
    choice = input("> ")
    
    if choice == "LEFT":
        bear_room()
    elif choice == "RIGHT":
        cthulu_room()
    else:
        dead("You wander around the dark until you starve")
        
start()

