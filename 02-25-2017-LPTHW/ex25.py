# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:24:19 2017

@author: rjr
Mor practice covering functions
"""


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print(word)
    
    
def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print(word)
        
def sort_sentence(sentence):
    """Takes a sentence and returns sorted words."""
    words = break_words(sentence)
    return sort_words(words)    

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts words then prints first and last words"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
    
sent = "All good things come to those who wait"
print(sent)

wrd = break_words(sent)
srt_wrds = sort_words(wrd)

print_first_word(wrd)
print_last_word(wrd)

srt_wrds = sort_sentence(sent)
print_first_and_last(sent)
print_first_and_last_sorted(sent)
