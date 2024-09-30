#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:54:14 2024

@author: cornelius
"""

"""
                            TO DOS
                

                4. search
                5. traverse
                6. delete
                7. Comment everything!!!
                    

"""


# -------------------------------------------------------------------------------------------------------

#                                            NODE CLASS

# -------------------------------------------------------------------------------------------------------

class Node():
    
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None        # children of the node
        self.right = None
   
    



# -------------------------------------------------------------------------------------------------------

#                                            TREE CLASS

# -------------------------------------------------------------------------------------------------------


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
    
        
    
    
    
    def get_depth(self):
        
        if self.root == None:               # if there is no root there is no depth
            return 0
        
        # tree only with a root is defined as depth 0
        level = [self.root]
        depth = 0
        
        while level:                        # as long as level list is not empty
            
            depth += 1                      # increase the depth by 1
            level_size = len(level)         # the size of the level of a tree is the amount of nodes
            
            for i in range(level_size):     # go through all nodes in level
                current_node = level.pop(0)     # start with first node in level list, get it and delete it
                if current_node.left:       # if left child of current node is not None
                    level.append(current_node.left)
                if current_node.right:
                    level.append(current_node.right)
        return depth
    
    
    def get_nodes_at_level(self,level):
        
        if self.root == None:
            return []
        
        current_level_nodes = []
        level_nodes = [self.root]
        current_level = 1
        
        while level_nodes and current_level <= level:
            
            level_size = len(level_nodes)
            
            if current_level == level:
                for i in range(level_size):
                    current_node = level_nodes.pop(0)
                    current_level_nodes.append(current_node)
            else:
                for i in range(level_size):
                    current_node = level_nodes.pop(0)
                    if current_node.left:
                        level_nodes.append(current_node.left)
                    if current_node.right:
                        level_nodes.append(current_node.right)
                        
                        
            current_level += 1

    
        return current_level_nodes
    
    
    

    def __str__(self):
        
        result = []
        depth = self.get_depth()
        
        for level in range(1,depth+1):
            result.append(self.get_nodes_at_level(level))
            
        return str(result)






# -------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------

tree = BinaryTree()
tree.insert(2, "hallo")
tree.insert(3,"idiot")
tree.insert(4, "3")
print(tree)

node = tree.nodes[0]
print(tree.get_depth())



























