# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:39:39 2017

@author: mazouthm
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from framework import *
from image import *

class Circle:
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
        #2 cases : the line intersects
        #                 it doesn't
        first = 0; last = 0;
        if len(line) == 1:
            return 0 
        
        while ((self.isInCircle(line[first]) == False) & (first < len(line)-1)):
                first = first + 1
            
        last = first
        while ((last < len(line)-1) & self.isInCircle(line[last]) ): #if the last element of the line is in the circle, it is not taken into account
            last = last + 1
        
        if last != first:
            if (last == (len(line)-1)): #special if to take into account the last element if necessary
                if self.isInCircle(line[last]):
                    return np.linalg.norm(line[last] - line[first])
                else:
                    return np.linalg.norm(line[last-1] - line[first])
            else:
                    return np.linalg.norm(line[last-1] - line[first])
        return 0
        


def line(framework, phi,s,dl): #returns a np.array of points corresponding to the projection line at angle phi and length s, given a dl step in the sigmaPhi direction
                 #TODO : finding the first and last point belonging to the framework
        thetaPhi = np.array([np.cos(phi),np.sin(phi)])
        sigmaPhi = np.array([-np.sin(phi),np.cos(phi)])
        lstart = 0; lend = 0;
        while (abs(s*thetaPhi[0] + lstart*dl*sigmaPhi[0]) <= framework.xmax) &  (abs(s*thetaPhi[1] + lstart*dl*sigmaPhi[1]) <= framework.ymax): #finding one extermity
            lstart = lstart-1
        while (abs(s*thetaPhi[0] + lend*dl*sigmaPhi[0]) <= framework.xmax) &  (abs(s*thetaPhi[1] + lend*dl*sigmaPhi[1]) <= framework.ymax): #finding one extermity
            lend = lend+1
            
        return np.array([(s*thetaPhi + i*dl*sigmaPhi) for i in range (lstart+1,lend)]) 
        
def buildSinogram(framework,a,m,dl): # (a,m) = (nb of subdivisions of phi, nb of subdivisions of s)
    radonTransform = np.zeros((a,m))
    #deriving the range of values of phi and s
    dphi = np.pi/a        
    #the length abs(sMax) s.t the line remains in the framework depends on phi
    for k in range(0,a): #stops to a-1 : no projection for angle pi
        phi = k*dphi
        if (0.0 <= phi <= np.arctan(framework.ymax/framework.xmax)):
            sMax = framework.xmax/np.cos(phi)
        elif (np.pi-np.arctan(framework.ymax/framework.xmax) <= phi <= np.pi):
            sMax = abs(framework.xmax/np.cos(phi))
        else:
            sMax = abs(framework.ymax/np.sin(phi))
        ds = 2*sMax/m
        
        for j in range(1,m): 
            #for a given angle k*phi, a given length j*ds : compute the radon transform
            for circle in framework.getCurrentImage().getListOfCircles():
                line1 = line(framework,k*dphi,-sMax + j*ds,dl)
                radonTransform[k,j] = radonTransform[k,j] + circle.lengthLineIntersection(line1)*circle.intensity
        
    #display the sinogram
    plt.imshow(radonTransform, interpolation='bilinear', 
              cmap=cm.gist_gray, 
              origin='lower', 
              extent=[-framework.xmax,framework.xmax,0,180],aspect='auto')

    plt.xticks(size = 8)
    plt.yticks(size = 8)
    
    plt.xlabel('s',fontsize=10)
    plt.ylabel('\phi',fontsize=10)
    plt.title('Sinogram',fontsize=12, color='r')
    #return the sinogram ?
    return radonTransform
    
            