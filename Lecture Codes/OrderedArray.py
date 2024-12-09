#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:51:47 2024

@author: cornelius
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
            
    # -----------------------------------------------------------------------------
    #                               BASIC OPERATIONS 
    # -----------------------------------------------------------------------------      
            
    def insert(self, item):
        # Der erste Eintrag bestimmt den Datentyp des Arrays
        if self.amount == 0:
            self.datatype = type(item)

        # Prüfen, ob der Datentyp korrekt ist
        if type(item) != self.datatype:
            raise TypeError(f"Falscher Datentyp. Das Array ist vom Typ {self.datatype}")

        # Prüfen, ob das Array voll ist
        if self.amount >= self.size:
            raise OverflowError("Das Array ist voll.")

        # Suche nach der korrekten Position
        index = 0
        while index < self.amount and getattr(self, f"element{index}").value < item:
            index += 1

        # Verschieben der Elemente, um Platz für das neue Element zu schaffen
        for i in range(self.amount, index, -1):
            getattr(self, f"element{i}").value = getattr(self, f"element{i-1}").value

        # Einfügen des neuen Elements
        getattr(self, f"element{index}").value = item
        self.amount += 1

        
    def search(self,item):
        
    
        # go through all elements one by one and compare
        for i in range(self.size):
            element = getattr(self, f"element{i}")      # get element with index i
            if item == element.value:                   # compare
                return element.index                    # if correct return index
        

    
    
    def delete(self,item):
        
        for i in range(self.size):                      # go through all elements of array to search item
            element = getattr(self, f"element{i}")      # take elements of array
            if item == element.value:                   # and compare them until right match is found
                last_element = getattr(self, f"element{self.amount-1}") # get last element of the array
                element.value = last_element.value      # shift value to the position of element to be kicked out
                last_element.value = None               # set the value of the last element to None
                self.amount -= 1                        # finally we decrease the amount of elements in the array
     

    def del_index(self,index):
        
        element = getattr(self, f"element{index}")                  # get the element with index specified in function
        last_element = getattr(self, f"element{self.amount-1}")     # get last element of the array
        element.value = last_element.value                          # delete element by replacing it with last element
        last_element.value = None                                   # set last element to None
        self.amount -= 1                                            # and reduce amount of elements in array
        

                                                  
                
    def traverse(self):
        # go through all elements one by one and print them if
        # they are not None
        for i in range(self.size):                                  # go through all elements
            element = getattr(self, f"element{i}")
            if element.value != None:                               # check if element is not None
                print(element.value)                                # print the value of the element
        


    # get the element with a specified index
    def get(self,index):
        
        if index < self.size:                                       # check if index is smaller than size
            element = getattr(self, f"element{index}")
            return element.value                                    
        else:
            raise IndexError("Array is not that big man.")          # if index out of range spit out Index Error
            
            

        
    # -----------------------------------------------------------------------------
    #                               THE MAGIC SECTION
    # -----------------------------------------------------------------------------
        
    def __getitem__(self, index):                                   # function to get item of array with []-formalism
        
        if index < 0 or index >= self.size:
            raise IndexError("Array index out of range man take care yo.")
        
        element = getattr(self, f"element{index}")
                
        return element.value

    def __setitem__(self,index,value):                              # function to set item of array with []-formalism
        
        if self.amount == 0:
             self.datatype = type(value)
        
        if index < 0 or index >= self.size:
            raise IndexError("Array index out of range man take care yo.")
            
        if type(value) != self.datatype:
            raise TypeError(f"Wrong data type. Array is of type {self.datatype}")
            

        
        element = getattr(self, f"element{index}")
        element.value = value 
        
        
        
    def __contains__(self, element):                                    # make the in-operator usable
        
        for i in range(self.size):
            array_element = getattr(self, f"element{i}")
            if array_element.value == element:
                return True
            
            
        return False

        
    # make the array an iterable object
    # this does not work without the __next__ method
    def __iter(self):
        self._index = 0
        return self

        
    # def __next__(self):
    #     if self._index < self.amount:
    #         result = getattr(self, f"element{self._index}")
            
    #         self._index += 1
    #         return result.value
    #     else:
    #         StopIteration
        
    
    
    def __len__(self):                                              # function to get length of array with len()-function
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
# print(array.get(2))         # get element with index 2



print(array) 
            
            