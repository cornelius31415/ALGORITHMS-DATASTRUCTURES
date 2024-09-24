#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:34:50 2024

@author: cornelius
"""

"""
                    BASIC OPERATIONS ON DATASTRUCTURES
            
            1. INSERT 
            2. SEARCH
            3. DELETE
            4. TRAVERSE


                    DIFFERENCES BETWEEN LISTS AND ARRAYS
                    
            - items of a list do not all have to be of the same data type
            - for an array all elements must be of the same type
            - knowing the type of the items means knowing the amount of memory
              needed to represent each one
            - therefore the memory for the entire array can be allocated
            
            - arrays are of a fixed size from the start
            - the compiler needs to know how much space to set aside for the
              whole array and keep it separate from all the other data
            
"""




class Array():
    
    def __init__(self,initial_size):   # arrays have a fixed size 
        self.initial_size = initial_size
        self.array = [None]*initial_size # define array as list with None initial_size times
        self.amount = 0 # amount of elements in array
        self.initial_type = None # every array contains onyl elements of one data type


        
    def insert(self,item): # insert a new element into the array
    
        if self.amount == self.initial_size:
            print("Array is full")
            return False
    
        if self.amount == 0: # if no element is yet in the array 
            
            self.initial_type = type(item) # set type of array to type of item
            self.array[self.amount]=item # insert item at the current end of array
            self.amount += 1 # increase the amount of items by on
            
        elif self.amount > 0:
            if type(item) != self.initial_type: # check if type of element to be added
                print("Not the right data type") # is the same as the set initial type of array
            else:
                self.array[self.amount]=item # insert item at the current end of array
                self.amount += 1 # increase the amount of items by one 


    
    def search(self,item):
        for i in range(self.amount):
            if self.array[i] == item: # if found
                return self.array[i] # return item
        
        
        
    def delete(self,item):
        for i in range(self.amount):
            if self.array[i] == item: # if item found
                for k in range(i,self.amount): # go through elements with higher indizes
                    self.array[k] = self.array[k+1] # and shift them one down
                self.amount -= 1    
                
    
    
    def traverse(self): # print each element of the array
        for i in range(self.amount):
            print(self.array[i])
    
    
    def __str__(self):
        array_string = "["
        for i in range(self.amount):
            if len(array_string)>1:
                array_string += ", "
            array_string += str(self.array[i])
        array_string += "]"
        return array_string
    
    
    
    
    
    
    
ar = Array(3)

ar.insert(2)
ar.insert(3)
ar.insert(4)
ar.insert(10)
print(ar)
