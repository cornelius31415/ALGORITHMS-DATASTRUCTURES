#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:42:01 2024

@author: cornelius
"""
import numpy as np
import matplotlib.pyplot as plt

class Graph():
    
    def __init__(self):
        
        self.nodes = []
        self.adjacency_matrix = {}
        
    # -----------------------------------------------------------------------------
    #                               CREATING A GRAPH
    # -----------------------------------------------------------------------------    
    
    def add_vertex(self,vertex):
        
        if vertex not in self.nodes:
            self.nodes.append(vertex)
            for node in self.nodes:
                self.adjacency_matrix[node,vertex]=0
                self.adjacency_matrix[vertex,node]=0
                
     
    
    def add_edge(self,vertex1, vertex2):
        
        self.adjacency_matrix[vertex1,vertex2] = 1
        self.adjacency_matrix[vertex2,vertex1] = 1

    # -----------------------------------------------------------------------------
    #                               ANALYZING A GRAPH
    # -----------------------------------------------------------------------------   

    def neighbors(self,vertex):
        neighbors = []
        for node in self.nodes:
            if node != vertex and self.adjacency_matrix[node,vertex]==1:
                neighbors.append(node)
        
        return neighbors
    
    # -----------------------------------------------------------------------------
    #                               PLOTTING A GRAPH
    # -----------------------------------------------------------------------------    
    
    def draw_graph(self):
        
        fig, ax = plt.subplots()
        ax.axis('off')
        ax.set_xlim(-1.5,1.5)
        ax.set_ylim(-1.5,1.5)
        
        node_positions = {}                     # coordinates for each node
        angle_step = 2*np.pi/len(self.nodes)
        radius = 1
        
        for idx, node in enumerate(self.nodes):
            angle = idx * angle_step
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            node_positions[node] = (x,y)        # coordinate for each node
            ax.scatter(x,y,s=500,color='lightblue',zorder=2)
            ax.text(x,y,node,ha='center',va='center',zorder=3)
            
        
        for vertex1 in self.nodes:
            for vertex2 in self.nodes:
                if self.adjacency_matrix[vertex1,vertex2] == 1:
                    x1,y1 = node_positions[vertex1]
                    x2,y2 = node_positions[vertex2]
                    ax.plot([x1,x2],[y1,y2],zorder=1)
         
                

        
        
# -----------------------------------------------------------------------------
#                               TRYING IT OUT
# -----------------------------------------------------------------------------
    

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A", "B")
g.add_edge("B", "D")
g.add_edge("A", "C")
g.add_edge("B", "C")
print(g.neighbors("D"))
g.draw_graph()


