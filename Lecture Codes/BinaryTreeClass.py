#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:54:14 2024

@author: cornelius
"""

"""
                            TO DOS
                
                1. get depth function
                2. get level elements function
                3. display as list of lists 
                4. search
                5. traverse
                6. delete
                    

"""


class Node():
    
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None        # children of the node
        self.right = None
   
    




class BinaryTree():
    
    def __init__(self):
        self.root = None                # set root to None in the beginning
        self.nodes = []
    
    
    def insert(self,key,value):
        
        new_node = Node(key,value)      # create a Node object with key and value
        
        if self.root is None:           # if there is no root node yet set new node as root
            self.root = new_node
            self.nodes.append(self.root)
            return 
        
        current = self.root             # start with root node
        
        while True:                     # while current is not None
        
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    self.nodes.append(new_node)
                    break
                else:
                    current = current.left
                    
            elif key > current.key:
                if current.right is None:
                    current.right = new_node
                    self.nodes.append(new_node)
                    break
                else:
                    current = current.right
    
        
    
    
    
    

    def __str__(self):
        liste = [self.nodes[i].right for i in range(len(self.nodes))]
        return str(liste)





tree = BinaryTree()
tree.insert(2, "hallo")
tree.insert(3,"idiot")
tree.insert(4, "3")
print(tree)

node = tree.nodes[0]
print(node.right.value)



























