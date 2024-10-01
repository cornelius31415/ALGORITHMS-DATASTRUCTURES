#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:41:38 2024

@author: cornelius
"""



class HashTable():
    
    def __init__(self):
        
        self.size = 2**16                   # hash table should store as many elements
        self.hashtable = [None]*self.size   # as there are possible hashes
        
        
    
    # -----------------------------------------------------------------------------
    #                                  HASH FUNCTION 
    # -----------------------------------------------------------------------------    
    
    def hash_int(self,string):
        string = str(string)
        hash_sum = sum((257**i)*ord(string[i]) for i in range(len(string)))
        hashvalue = bin(hash_sum % 2**16)
        return int(hashvalue,2)
        
    
    
    # -----------------------------------------------------------------------------
    #                               BASIC OPERATIONS 
    # -----------------------------------------------------------------------------    
    
    # O(1) search because you only have to calculate the hash to get the index
    def search(self, element):
        index = self.hash_int(element)
        return self.hashtable[index]
        
    
    
    # O(1) insertion because you just have to set index value to element value
    def insert(self, element):
        element = str(element)
        index = self.hash_int(element)
        self.hashtable[index] = element
        print("Index of element: ",self.hashtable.index(element))
        

    # O(1)
    def delete(self, element):
        index = self.hash_int(element)
        self.hashtable[index] = None
        

    
    # O(n)
    def traverse(self):
        for element in self.hashtable:
            if element != None:
                print(element)

    
   
    
    # -----------------------------------------------------------------------------
    #                               THE MAGIC SECTION
    # -----------------------------------------------------------------------------
        
   
    
    
    # display hash table with print()-function
    def __str__(self):
        
        array_string = "["
        for element in self.hashtable:
            if len(array_string)>1 and element != None:
                array_string += ", "
            
            if element != None:
                array_string += "("
                array_string += str(element)
                array_string += ","
                array_string += str(self.hashtable.index(element))
                array_string += ")"
        
        array_string += "]"
        return array_string
    
       

        
# -----------------------------------------------------------------------------
#                               TRYING IT OUT
# -----------------------------------------------------------------------------
    
h = HashTable()    
h.insert(34)
h.insert("kjfgdsj")
h.insert("4234nijg31itnitn")
print(h)

h.delete(34)
print(h)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    