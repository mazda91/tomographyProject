# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:39:39 2017

@author: mazouthm
"""

import numpy as np
import math
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
        return (np.linalg.norm(point - self.center) <= self.radius + 10**(-10))
        
    def lengthLineIntersection(self,line):
        #2 cases : the line intersects
        #                 it doesn't
        first = 0; last = 0;
        if (len(line) == 1) | (len(line) == 0):
            return 0 
        
        while ((self.isInCircle(line[first]) == False) & (first < len(line)-1)):
                first = first + 1
            
        last = first
        for i in range(first,len(line)):
            if self.isInCircle(line[i]) == True:
                last = i
        return np.linalg.norm(line[last] - line[first])
        
        
        


def line(fmw, phi,s,dl): #returns a np.array of points corresponding to the projection line at angle phi and length s, given a dl step in the sigmaPhi direction
                 #TODO : finding the first and last point belonging to the framework fmw
        thetaPhi = np.array([np.cos(phi),np.sin(phi)])
        sigmaPhi = np.array([-np.sin(phi),np.cos(phi)])
        lstart = 0; lend = 0;
        while (np.linalg.norm(s*thetaPhi + lstart*dl*sigmaPhi - np.array([fmw.xcenter,fmw.ycenter]))<= fmw.radius): #finding one extermity
            lstart = lstart-1
        while (np.linalg.norm(s*thetaPhi + lend*dl*sigmaPhi - np.array([fmw.xcenter,fmw.ycenter])) <= fmw.radius): #finding one extermity
            lend = lend+1
            
        return np.array([(s*thetaPhi + i*dl*sigmaPhi) for i in range (lstart+1,lend)]) 
        
def buildSinogram(framework,a,m,dl): # (a,m) = (nb of subdivisions of phi, nb of subdivisions of s)
    radonTransform = np.zeros((a,m)) 
    #deriving the range of values of phi and s
    dphi = 2*np.pi/a        
    for k in range(0,a): #stops to a-1 : no projection for angle pi
#        import pdb; pdb.set_trace()
        phi = k*dphi
        ds = 2*framework.radius/m
        
        for j in range(1,m): 
            #for a given angle k*phi, a given length j*ds : compute the radon transform
            for circle in framework.getCurrentImage().getListOfCircles():
                line1 = line(framework, phi,-framework.radius + j*ds,dl)
                radonTransform[k,j] = radonTransform[k,j] + circle.lengthLineIntersection(line1)*circle.intensity
        
    #display the sinogram
    plt.imshow(radonTransform, interpolation='bilinear', 
              cmap=cm.gist_gray, 
              origin='lower', 
              extent=[-framework.radius,framework.radius,0,360],aspect='auto')

    plt.xticks(size = 8)
    plt.yticks(size = 8)
    
    plt.xlabel('s',fontsize=10)
    plt.ylabel('\phi',fontsize=10)
    plt.title('Sinogram',fontsize=12, color='r')
    #return the sinogram ?
    return radonTransform

def integrale(vecX,vecY): #returns the integrale(trapeze formula) of vecY function on vecX interval
        integral = 0
        for i in range(0,len(vecX)-1):
            integral = integral + (vecX[i+1]-vecX[i])*(vecY[i+1]+vecY[i])/2
        return integral
        
        
def moment(framework,radonTransform,n): #moment of order n
    dimRadon = np.shape(radonTransform)
    a = dimRadon[0] #nb of subdivisions of phi interval : [0,pi]
    vecMoment = np.zeros(a)
    m = dimRadon[1] #nb of subdivisions of interval s
    ds = 2*framework.radius/m
    s = np.array([(-framework.radius + i*ds) for i in range(0,m)])
    
    for k in range(0,a):
        vecMoment[k] = integrale(s,radonTransform[k,:]*(s**n))
    return vecMoment
        
def trigoDotProduct(phi,vecP,vecQ):
    return integrale(phi,vecP*vecQ)
                
def projOnBasis(phi,vecMoment,vecBasis): #projection of the moment on a vector basis of trigonometric polynomials
    if trigoDotProduct(phi,vecBasis,vecBasis) != 0:
        return vecBasis*trigoDotProduct(phi,vecBasis,vecMoment)/trigoDotProduct(phi,vecBasis,vecBasis)    
    else :
        return 0
    
def projectionMoment(phi,n,vecMoment): #n : order of the moment to be projected
    dim = len(vecMoment)
    projRes = np.zeros(dim)
    degrees = np.array([n-2*i for i in range(0,math.floor(n/2)+1)])
    for i in degrees:
        vecCos = np.cos(i*phi)
        vecSin = np.sin(i*phi)
        proj1 = projOnBasis(phi,vecMoment,vecCos)
        proj2 = projOnBasis(phi,vecMoment,vecSin)
        projRes = projRes + proj1 + proj2
    return projRes
            