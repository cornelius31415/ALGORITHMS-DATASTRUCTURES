#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:31:16 2024

@author: cornelius
"""

"""

         FEATURES OF A SET
         
         1. Each element is unique
         2. There is no order in a set
         3. Elements do not have an index.
         4. Union of sets
         5. Intersection of sets
         6. Difference
         7. Symmetric difference

"""

from Array import Array



class Set():
    
    
    def __init__(self):
        
        self.amount = 0             # set amount of elements to zero
        self.set = Array(10)        # use an array data structure to store elements
        
        
    
    def add(self,element):
        
        if element not in self.set:     # check if element is already existent in the set
            self.set.insert(element)    # if not- go ahead and add it to the array
        
        

    
    
    def union(self, other_set):
        
        union_set = Set()               # union of two sets is a set again
        for element in self.set:        # add each element of set 1
            union_set.add(element)
        
        for element in other_set.set:   # add each element of set 2
            if element not in union_set.set:    # if it has not been added already
                union_set.add(element)

        
        return union_set
        
        
    
    
    def intersection(self, other_set):
        
        intersection_set = Set()
        
        for element in self.set:
            if element in other_set.set:
                intersection_set.add(element)

        return intersection_set
    
    
    def difference(self, other_set): # elements in self but not in other_set: (self \ other_set)
        
        difference_set = Set()
        
        for element in self.set:
            if element not in other_set.set:
                difference_set.add(element)
        
        return difference_set
    
    
    def symmetric_difference(self, other_set):
        
        symm_diff = Set()
        
        for element in self.set:                # put all elements that are in self.set but not in other_set
            if element in other_set.set:
                pass
            else:
                symm_diff.add(element)
                
        for element in other_set.set:           # put all elements that are in other_set but not in self.set
            if element not in self.set:
                symm_diff.add(element)
        return symm_diff
    
    
    def __str__(self):
        
        set_string = "{"
        for element in self.set:
            if len(set_string)>1 and element != None:
                set_string += ","
            if element != None:
                set_string +=   str(element)
        set_string += "}"
        
        return set_string
    
    
          
# -----------------------------------------------------------------------------
#                               TRYING IT OUT
# -----------------------------------------------------------------------------  
    
menge = Set()
menge.add(2)
print(menge)



set1 = Set()
set2 = Set()
set1.add(1)
set1.add(2)
set1.add(3)

set2.add(3)
set2.add(4)
set2.add(5)
union = set1.union(set2)
print(union)
inter = set1.symmetric_difference(set2)
print(inter)






















