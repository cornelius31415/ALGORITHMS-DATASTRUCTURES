#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:15:04 2024

@author: cornelius
"""

"""

                Create a Binary Tree only based on primitive datatypes
                and the Array Class defined in another file.

"""

from Array import Array 


class Node():
    
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        
        
    
    



class BinaryTree():
    
    def __init__(self,number_of_nodes=10):
        self.root = None
        self.size = number_of_nodes
        self.nodes = Array(self.size)
        
    def insert(self,key,value):
        
        new_node = Node(key,value)
        current = self.root
        
        if self.root == None:
            self.root = new_node
            self.nodes.insert(self.root)
            return                          # function has to end here
            
        while True:
            if key < current.key:
                if current.left == None:
                    current.left = new_node
                    self.nodes.insert(current.left)
                    break
                else:
                    current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = new_node
                    self.nodes.insert(current.right)
                    break
                else:
                    current = current.right
            
            
            
    def __str__(self):
        
        return self.nodes
        
        pass
            
            
            
            
tree = BinaryTree()
tree.insert(10, "d")
tree.insert(2, "sdf")
tree.insert(12, 23)
print([tree.nodes.get(i).right for i in range(len(tree.nodes))])

print(tree.nodes.get(0).left.value)
            
    
    