# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:39:39 2017

@author: mazouthm
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class circle:
    "class"
    def __init__(self,center = 0, radius = 0, intensity = 0):
        self.center = center
        self.radius = radius
        self.intensity = intensity
        
    def getCenter(self):
        return self.center
        
    def getRadius(self):
        return self.radius
        
    def getIntensity(self):
        return self.intensity
        
    def setCenter(self, center):
        self.center = center
        
    def setRadius(self, radius):
        self.radius = radius
        
    def setIntensity(self,intensity):
        self.intensity = intensity
        
    def isInCircle(self,point):
        return (np.linalg.norm(point - self.center) <= self.radius)
        
    def lengthLineIntersection(self,line):
        first = 0; last = 0;
        while (self.isInCircle(line[first] == False)):
            first = first + 1
            
        last = first
        while (self.isInCircle(line[last])):
            last = last + 1
        
        return np.linalg.norm(line[last] - line[first])
    

def test():
    #test isInCircle
    #expected result : True, False, False, False, False
    center1 = np.array([2,2]); radius1 = 2; intensity1 = 0;
    C1 = circle(center1, radius1, intensity1)
    point1 = np.array([2,4]); point2 = np.array([2,4.1]); point3 = np.array([2,-0.1]); point4 = np.array([-0.1,2]); point5 = np.array([4,1.5])
    list_points = [point1,point2,point3,point4,point5]
    for point in list_points:
        print(C1.isInCircle(point))
    
    #test lengthLineIntersection
    line = np.array[2,np.arange(0,5)])
    print(C1.lengthLineIntersection(line))
            