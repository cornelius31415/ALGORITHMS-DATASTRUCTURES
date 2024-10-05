#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:42:01 2024

@author: cornelius
"""
import numpy as np
import matplotlib.pyplot as plt
import math

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
                
     
    
    def add_edge(self,vertex1, vertex2, weight = 1):
        
        self.adjacency_matrix[vertex1,vertex2] = weight
        self.adjacency_matrix[vertex2,vertex1] = weight

    # -----------------------------------------------------------------------------
    #                               ANALYZING A GRAPH
    # -----------------------------------------------------------------------------   

    def neighbors(self,vertex):
        neighbors = []
        for node in self.nodes:
            if node != vertex and self.adjacency_matrix[node,vertex] != 0:
                neighbors.append(node)
        
        return neighbors
    


    
    
    def dijkstra(self,start,end):
        
        """
                                        1.
        - Create a dictionary for the cost to get to each node from the start
        - Set cost to reach start to 0
        - Set cost to reach every other node to infinity
        
                                        2.
        - Create a list for each node visited
        - A node will be added after it has been chosen as the one neighbor
          whose overall cost is minimal
        
                                        3.
        - Set current node to start 
        - Get neighbors of this current node
        
                                        4.
        - Calculate the cost of getting to each neighbor node by getting
          the cost to get to the current node from the costs-dictionary
          and add it to the weight of the edge 
          
                                        5.
        - If the calculated cost is smaller than the one written in 
          the costs-dictionary, then update the cost
          
                                        6.
        - Append the current node to the list of visited nodes
        
                                        7.
        - Get all the neighbors of the current node that have not yet 
          been added to the visited list
        - Go through the neighbors, check if they are in the visited list
          and add the unvisited neighbor as a key to a dictionary whose values
          will be the cost to reach that neighbor
          
                                        8.
        - Choose the neighbor with the smallest cost
        - Append end node to the visited list
        -> Now the visited list is the shortest path
        
        
        """
        costs = {start: 0}
        for node in self.nodes:
            if node != start:
                costs[node] = np.inf
    
        visited = []
        current_node = start
        
        while current_node != end:
            
            neighbors = self.neighbors(current_node)
            
            for neighbor in neighbors:
                
                cost = costs[current_node] + self.adjacency_matrix[neighbor,current_node]
                if cost < costs[neighbor]:
                    costs[neighbor] = cost
            visited.append(current_node)
            
            # now i need neighbors who have not been visited before and choose the one with
            # the shortest overall path
            unvisited_neighbors = {}
            for neighbor in neighbors:
                if neighbor not in visited:
                    unvisited_neighbors[neighbor] = costs[neighbor]
                
            current_node = min(unvisited_neighbors,key=unvisited_neighbors.get)
                            
        visited.append(end)
        return visited
        
    
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
                if self.adjacency_matrix[vertex1,vertex2] != 0:
                    weight = self.adjacency_matrix[vertex1, vertex2]
                    x1,y1 = node_positions[vertex1]
                    x2,y2 = node_positions[vertex2]
                    ax.plot([x1,x2],[y1,y2],zorder=1,color='orange')
         
                    mid_x, mid_y = (x1+x2)/2, (y1+y2)/2
                    ax.text(mid_x,mid_y,str(weight),ha='center',va='center',zorder=3,
                            bbox=dict(facecolor='mintcream', edgecolor='black', 
                                      boxstyle='round,pad=0.5'))    
                    
                    
                    
    def draw_shortest_path(self,start,end):
        
        fig, ax = plt.subplots()
        ax.axis('off')
        ax.set_xlim(-1.5,1.5)
        ax.set_ylim(-1.5,1.5)
        
        node_positions = {}                     # coordinates for each node
        angle_step = 2*np.pi/len(self.nodes)
        radius = 1
        
        path = self.dijkstra(start, end)
        
        for idx, node in enumerate(self.nodes):
            angle = idx * angle_step
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            node_positions[node] = (x,y)        # coordinate for each node
            if node == start or node == end:
                ax.scatter(x,y,s=500,color='green',zorder=2)
                ax.text(x,y,node,ha='center',va='center',zorder=3)
            else:
                ax.scatter(x,y,s=500,color='lightblue',zorder=2)
                ax.text(x,y,node,ha='center',va='center',zorder=3)
        
        for vertex1 in self.nodes:
            for vertex2 in self.nodes:
                if self.adjacency_matrix[vertex1,vertex2] != 0:
                    weight = self.adjacency_matrix[vertex1, vertex2]
                    x1,y1 = node_positions[vertex1]
                    x2,y2 = node_positions[vertex2]
                    ax.plot([x1,x2],[y1,y2],zorder=1,color='orange')
                    
                    for i in range(len(path)-1):
                        X1,Y1 = node_positions[path[i]]
                        X2,Y2 = node_positions[path[i+1]]
                        ax.plot([X1,X2],[Y1,Y2],zorder=1,color='green')
                        
                    
                    mid_x, mid_y = (x1+x2)/2, (y1+y2)/2
                    ax.text(mid_x,mid_y,str(weight),ha='center',va='center',zorder=3,
                            bbox=dict(facecolor='mintcream', edgecolor='black', 
                                      boxstyle='round,pad=0.5'))    
                    
                    
                    

