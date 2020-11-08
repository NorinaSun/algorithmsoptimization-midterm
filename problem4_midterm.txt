#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 18:46:33 2020

@author: NorinaSun
"""
import itertools

def validate_sequence(sequence):
    diff_list = []
    validity = "valid"
    
    for i in range(len(sequence)-1):
        diff = abs(sequence[i] - sequence[i+1])
        diff_list.append(diff)
    
    for i in range(0,len(diff_list)-1):
        if diff_list[i] >= diff_list[i+1]:
            pass
        else:
            validity = "invalid"
            break

    return validity

#question 1 
permutations = itertools.permutations([2, 4, 7, 11])

for each in permutations:
    print(each,validate_sequence(each))

#question 2

def order_sequence(sequence):
    ordered_sequence = []
    current_value = min(sequence)
    
    while len(sequence) > 1:
        ordered_sequence.append(current_value)
        
        diff_list = []
        for i in sequence:
            diff = abs(current_value - i)
            diff_list.append(diff)
        
        index = diff_list.index(max(diff_list)) 
        old_value = current_value
        current_value = sequence[index]
        sequence.remove(old_value)
    
    ordered_sequence.append(sequence[0])
    
    return ordered_sequence

example = [4,7,13,19,22,24,27,36,37,42,45,49,53,58,63,67,70,75]
print(order_sequence(example))
print(validate_sequence(order_sequence(example)))


    



