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

class Disk:
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
        
        
    def lengthLineIntersection(self,s):
        if abs(s) > self.radius:
            return 0
        else:
            return 2*np.sqrt(self.radius**2 - s**2)
        
def sinogram(globalFmw,truncFmw,a,m,L):
    sinoMatrix = np.zeros((a,m)) 
    dccMatrix = np.zeros((a,m))
    for disk in truncFmw.getCurrentImage().getListOfDisks():
        sinoMatrix = sinoMatrix + radonTransform(globalFmw,truncFmw,a,m,L,disk)[0]
        dccMatrix = dccMatrix + radonTransform(globalFmw,truncFmw,a,m,L,disk)[1]
    return sinoMatrix,dccMatrix
    
def radonTransform(globalFmw,truncFmw,a,m,L,disk): # (a,m) = (nb of subdivisions of phi, nb of subdivisions of s)    
    Lstart = L[0]; Lend= L[len(L)-1]; y0 = L[0,1]
    dccMatrix = np.zeros((a,m))
    radonMatrix = np.zeros((a,m))
    scale = disk.radius
    disk.setRadius(1) #using formulae linking radon transform of a scaled disk with the rT on unit disk
    #deriving the range of values of phi and s
    ds = 2*globalFmw.radius/m
    for k in range(0,a): #stops to a-1 : no projection for angle pi
        phi = -np.pi/2 + k*np.pi/a
        thetaPhi = np.array([np.cos(phi),np.sin(phi)])
        for j in range(0,m): 
            #for a given angle phi, a given length j*ds : compute the radon transform
            #formula for s to be in the FOV
            sMinFOV = np.dot(np.array([truncFmw.xcenter,truncFmw.ycenter]),thetaPhi) - truncFmw.radius
            sMaxFOV = sMinFOV + 2*truncFmw.radius
            s = -globalFmw.radius + j*ds
            if sMinFOV <= s <= sMaxFOV:#line at s intersects FOV ?
                smax = np.dot(disk.getCenter(),thetaPhi) + scale
                smin = np.dot(disk.getCenter(),thetaPhi) - scale
                if (min(smin,smax) <= s <= max(smin,smax)): #line intersect the disk ?
                    changeVariable = (s -np.dot(thetaPhi,disk.center))/scale
                    radonMatrix[k,j] = radonMatrix[k,j] + scale*projLine(changeVariable,phi,disk)  
                if(np.dot(Lstart,thetaPhi) <= s <= np.dot(Lend,thetaPhi)): #line intersect segment L ?
                    dccMatrix[k,j] = radonMatrix[k,j]
    disk.setRadius(scale)
    return radonMatrix, dccMatrix

def projLine(s,phi,disk):
    return disk.lengthLineIntersection(s)*disk.intensity
    
def plotSinogram(globalFmw,truncFmw,sinogram,plotTitle,imageInfo,save):
    #display the sinogram
    plt.imshow(sinogram, interpolation='bilinear', 
              cmap=cm.gist_yarg, 
              origin='lower', 
              extent=[-globalFmw.radius,globalFmw.radius,-90,90],aspect='auto')

    plt.xticks(size = 8)
    plt.yticks(size = 8)
    
    plt.xlabel('s',fontsize=10)
    plt.ylabel('phi',fontsize=10)
    plt.title(imageInfo,fontsize=12, color='r')
    if save == 1:
        plt.savefig(plotTitle + ".png")
        
def B(framework,n,L,a,eps):
    l = L.shape[0]
    phi = np.arange((-np.pi/2)+eps,(np.pi/2)-eps,(np.pi-2*eps)/a)
    weight = np.tan(phi)**n / np.cos(phi)
    vecProj = np.zeros(a)
    res = np.zeros(l)
    thetaPhi = np.array([np.cos(phi),np.sin(phi)])
    thetaPhi = thetaPhi.T
    
    for i in range(0,l):
        vecProj = np.zeros(a)
        for k in range(0,a):
            for disk in framework.getCurrentImage().getListOfDisks():
                vecProj[k] += projLine(np.dot(L[i],thetaPhi[k]),phi[k],disk)    
         
        res[i] = integrale(phi,vecProj*weight)
    return res
    
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
    

    