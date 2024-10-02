#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:06:27 2024

@author: cornelius
"""

import numpy as np

class Circle():
    
    def __init__(self,radius=1):
        
        self.radius = radius
        
    
    def area(self):
        
        return round(np.pi * self.radius**2,2)
    


class NewCirc(Circle):
    
    def __init__(self,radius):
        
        super().__init__(radius)
        
    
    def circumference(self):
        return self.radius * 2 * np.pi



circle = NewCirc(1)
area = circle.area()
print(area)
print(circle.circumference())
