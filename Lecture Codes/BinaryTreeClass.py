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
                8. Printing tree with arrays
                    

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
    
        
    # -----------------------------------------------------------------------------
    #                               BASIC OPERATIONS
    # -----------------------------------------------------------------------------


    def insert(self,key,value):
        
        new_node = Node(key,value)      # create a Node object with key and value
        
        if self.root is None:           # if there is no root node yet set new node as root
            self.root = new_node
            self.nodes.append(self.root)
            return 
        
        current = self.root             # start with root node
        
        while current is not None:                     # while current is not None
        
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
                    
                    
    
    def search(self,key):                       # search for an element in a binary tree
                                                # best case O(logn) and worst case O(n)
        
        current = self.root                     # set current node to root
        
     
        while current is not None:              # as long as the current node is not None
            if key == current.key:              # check if key is aligning with key of current node
                return current.value            # if not then reset the current node to either
            elif key < current.key:             # the left or the right child
                current = current.left
            else:
                current = current.right
                


      
        
    
    
    def delete(self,key):
        
        
        pass
    
    
    def traverse(self):
        
        
        pass
    
        
            
    # -----------------------------------------------------------------------------
    #                               SIDE OPERATIONS
    # -----------------------------------------------------------------------------
    
    
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
            
            tree = []
            for element in current_level_nodes:
                tree.append(element.value)
                
                
        return tree
    
    
    # -----------------------------------------------------------------------------
    #                            MAGIC CLASS FUNCTIONS
    # -----------------------------------------------------------------------------  

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
tree.insert(1, "3")
print(tree)
print(tree.search(3))
node = tree.nodes[0]
print(tree.get_depth())



























