#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:55:13 2024

@author: cornelius
"""

"""

            An algorithm to determine all the subsets of a given list
            would be of order O(2^n) because there exist 2^n subsets to
            any given list, array or set. 
            The empty set also counts as a subset of any set.
            It will be denoted with []
            
"""


def powerset(input_list):
    
    powerset = [[]] # empty set already a subset of the powerset
    
    for element in input_list:
        # combine subsets already existing with elements from input_list
        powerset += [subset + [element]  for subset in powerset]
        
    return powerset


example = [1,2]
powerset = powerset(example)
print(powerset)








