#!/usr/bin/env python3

def return_evens(num_list):
    list_items = [i for i in num_list if(i%2 == 0)]
    return list_items

# return_evens([0, 1, 3, 5, 7, 8, 9])

def make_exclamation(sentence_list):
    exclamation = [i+"!" for i in sentence_list]
    return exclamation

make_exclamation(["Hello", "I'm doing great", "Python is fun"])