#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:29:50 2024

@author: cornelius
"""

"""
                    ARRAY FROM PRIMITIVE DATA TYPES
            
            The primitive data types are booleans, strings and
            numbers (integers and floats). With those it is possible
            to construct all types of data structures - arrays, 
            linked lists, trees, hashtables and graphs.
            
            A classical array has a fixed size and contains only 
            elements of one primitive data type. I wanted a class
            for such an array where each element of the array is
            an object itself with a value and an index. 

"""


# -----------------------------------------------------------------------------
#                               ARRAY ELEMENTS
# -----------------------------------------------------------------------------

# each element of an array is an object with a value and an index
class ArrayElement():
    # the constructor needs index and value to construct object
    def __init__(self,index,value=None):
        self.index = index
        self.value = value
        
# -----------------------------------------------------------------------------
#                               ARRAY ITSELF
# -----------------------------------------------------------------------------        
    
class Array():
    
    def __init__(self,size):
        
        self.size = size                    # predetermined size of array
        self.amount = 0                     # amount of elements that are not None
        self.datatype = None
        
        
        
        # Creation of Array
        for i in range(self.size):
            # creates attribute for each element of the array as 
            # an object of class ArrayElement with index i and value = None
            # so basically an empty list of size=size with None 
            # as elements size-times.
            setattr(self, f"element{i}", ArrayElement(i))
            
            
            
    def insert(self,item):
        
        # the first item to be added to the array determines the array type
        # all data added from now on must be of that type
        if self.amount == 0:
            self.datatype = type(item)
        
        #checking if the item to be added matches the data type of array
        if type(item) != self.datatype:
            raise TypeError(f"Wrong data type. Array is of type {self.datatype}")
        
        # checking if the array is full
        if self.amount >= self.size:
            raise OverflowError("Array is full bro.")
        
        # get the element of the first available index (with value = None)
        element = getattr(self, f"element{self.amount}") 
        element.value = item                    # change value of this element
        self.amount += 1                        # increase the amount of elements in array
        
        
        
    def search(self,item):
        
        # go through all elements one by one and compare
        for i in range(self.size):
            element = getattr(self, f"element{i}")
            if item == element.value:
                return element.index
        

    
    
    def delete(self,item):
        
        for i in range(self.size):                      # go through all elements of array to search item
            element = getattr(self, f"element{i}")      # take elements of array
            if item == element.value:                   # and compare them until right match is found
                
                for k in range(i,self.amount-1):        # range goes up to second last index
                    
                    # current element value is exchanged for the one
                    # of the next element's value
                    current_element = getattr(self, f"element{k}") 
                    next_element = getattr(self, f"element{k+1}")
                    current_element.value = next_element.value
                    
                # the loop only went up to the second last index
                # now we need the element of the last index
                last_element = getattr(self, f"element{self.amount-1}")
                last_element.value = None               # and set it to None
                self.amount -= 1                        # finally we decrease the amount of elements
                                                        # in the array
                
    def traverse(self):
        # go through all elements one by one and print them if
        # they are not None
        for i in range(self.size):
            element = getattr(self, f"element{i}")
            if element.value != None:
                print(element.value)
        


    # get the element with a specified index
    def get(self,index):
        
        if index < self.size:
            element = getattr(self, f"element{index}")
            return element.value
        else:
            raise IndexError("Array is not that big man.")
        


    def __len__(self):
        return self.amount
    
    
    # display array with print()-function
    def __str__(self):
        
        array_string = "["
        for i in range(self.size):
            element = getattr(self, f"element{i}") # get element via index
            value = str(element.value) # turn value of element into string
            
            # checking if the array is empty and if the element
            # to be added is not None
            if len(array_string)>1 and element.value != None: 
                array_string += ", " # the first element does not get a comma
                
            # only displaying element as part of array if not None
            if element.value != None:
                array_string += value # add value to the array string
      
        
        array_string += "]"
        return array_string
    
       

        
# -----------------------------------------------------------------------------
#                               TRYING IT OUT
# -----------------------------------------------------------------------------
       
array = Array(3)            # create array with 3 spaces for elements
array.insert(1)             # insert numbers
array.insert(2)
array.insert(3)
print(array.get(2))         # get element with index 2

                
print(len(array))           # print length of array
array.delete(2)             # delete element with value 2
print(len(array))           # print length of array
print(array)                # print array itself
array.traverse()            # traverse all the elements of the array
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    
