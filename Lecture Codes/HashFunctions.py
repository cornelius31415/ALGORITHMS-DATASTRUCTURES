#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:55:49 2024

@author: cornelius
"""

"""
                    HASH FUNCTION
                    
            Takes an element of arbitrary length and
            convertes it to a hash value of fixed length
            
            Here I take any string and convert it to a number
            between 1 and 2**32.
            So the hash value will always have a fixed length
            of 32 bits.

"""


# -----------------------------------------------------------------------------
#                               HASHLIB HASHES
# -----------------------------------------------------------------------------

import hashlib

print()

# creating a hash in hexadecimal code
hash_value = hashlib.sha256("hello".encode()).hexdigest()
print(f"Hash in hexadecimal: {hash_value}")

print("\n")

# Converting the hash to an integer in decimal
hash_integer = int(hash_value,16)
print(f"Hash in integer: {hash_integer}")

print()



# -----------------------------------------------------------------------------
#                           SIMPLE HASH FUNCTION
# -----------------------------------------------------------------------------

def hashfunction(string):
    
    hash_size = 32          # hash size in bits
    hash_sum = 0
    
    for idx in range(len(string)):
        char = string[idx]
        char_code = ord(char)
        pre_factor = 256 ** idx
        
        hash_sum += pre_factor * char_code
     
   
    hashvalue = hash_sum % (2**hash_size)   
   
    bin_hash = bin(hashvalue)[2:] # get rid of the 0b prefix
    
    bin_hash = bin_hash.zfill(hash_size)
       
    return bin_hash


print(hashfunction("746ubz4"))



# -----------------------------------------------------------------------------
#                         SHORT SIMPLE HASH FUNCTION
# -----------------------------------------------------------------------------

def shorthash(string):
    hash_sum = sum((256**i)*ord(string[i]) for i in range(len(string)))
    hashvalue = bin(hash_sum % 2**32)[2:]
    return hashvalue.zfill(32)

a = int(shorthash("746ubz4"),2)
b = int(shorthash("746ubz43dfgd"),2)
print(a==b)                             # already a collision between 2 elements

print()
hashvalue = shorthash("b43")
print(hashvalue)
print(int(hashvalue,2))



# -----------------------------------------------------------------------------
#                    SHORT SIMPLE  ***PRIME***  HASH FUNCTION
# -----------------------------------------------------------------------------

"""

                 WITH PRIME NUMBERS AS A BASE WE CAN CREATE MORE
                 RANDOMNESS IN THE DISTRIBUTION OF HASH VALUES.
                 
                 PROVEN IN PRAXIS.

"""


def shorthash(string):
    hash_sum = sum((257**i)*ord(string[i]) for i in range(len(string)))
    hashvalue = bin(hash_sum % 2**32)[2:]
    return hashvalue.zfill(32)

a = int(shorthash("746ubz4"),2)
b = int(shorthash("746ubz43"),2)
print(a==b)                        
print(a)
print(b)    

print()
hashvalue = shorthash("b43")
print(hashvalue)
print(int(hashvalue,2))








