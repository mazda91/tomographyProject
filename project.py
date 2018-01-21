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
        
        
#    def lengthLineIntersection(self,s,phi):
#        thetaPhi = np.array([np.cos(phi),np.sin(phi)])
#        if abs(s-np.dot(self.center,thetaPhi)) > self.radius:
#            return 0
#        else:
#            return 2*np.sqrt(self.radius**2 - (s-np.dot(self.center,thetaPhi))**2)
        
    def lengthLineIntersection(self,s,phi):
        if abs(s) > self.radius:
            return 0
        else:
            return 2*np.sqrt(self.radius**2 - s**2)
        
def sinogram(globalFmw,FOV,a,m,eps,move,translation,nbMotions):
    sinoFOV = np.zeros((a,m)) 
    listOfDisks = FOV.getCurrentImage().getListOfDisks()
    highestIntensity = np.array([listOfDisks[i].getIntensity() for i in range(0,len(listOfDisks))]).argmax()
    for index_disk in range(0,len(listOfDisks)):
        if index_disk != highestIntensity:
            sinoFOV = sinoFOV + radonTransform(globalFmw,FOV,a,m,listOfDisks[index_disk],eps,0,translation,nbMotions)
        else:
            sinoFOV = sinoFOV + radonTransform(globalFmw,FOV,a,m,listOfDisks[index_disk],eps,move,translation,nbMotions)
        
    return sinoFOV
    
def radonTransform(globalFmw,FOV,a,m,disk,eps,move,translation,nbMotions): # (a,m) = (nb of subdivisions of phi, nb of subdivisions of s)
    radonMatrix = np.zeros((a,m))
    scale = disk.radius
    disk.setRadius(1) #using formulae linking radon transform of a scaled disk with the rT on unit disk
    #deriving the range of values of phi and s
    ds = 2*FOV.radius/m
    randMotions = np.random.random_integers(0,a,nbMotions)
    for k in range(0,a): #stops to a-1 : no projection for angle pi
        if move == 1:
            if np.any(randMotions == k):
                disk.setCenter(disk.getCenter() + translation)
        phi = -np.pi/2 + eps + k*(np.pi-2*eps)/a
        thetaPhi = np.array([np.cos(phi),np.sin(phi)])
        for j in range(0,m): 
            #for a given angle phi, a given length j*ds : compute the radon transform
            #formula for s to be in the FOV
            sMinFOV = np.dot(np.array([FOV.xcenter,FOV.ycenter]),thetaPhi) - FOV.radius
            s = sMinFOV + j*ds
            changeVariable = (s -np.dot(thetaPhi,disk.center))/scale
            radonMatrix[k,j] = radonMatrix[k,j] + scale*projLine(changeVariable,phi,disk)  
    disk.setRadius(scale)
    return radonMatrix

def projLine(s,phi,disk):
    return disk.lengthLineIntersection(s,phi)*disk.intensity
    
def plotSinogram(globalFmw,FOV,sinogram,plotTitle,imageInfo,save):
    #display the sinogram
    plt.imshow(sinogram, interpolation='bilinear', 
              cmap=cm.gist_yarg, 
              origin='lower', 
              extent=[-FOV.radius,FOV.radius,-90,90],aspect='auto')

    plt.xticks(size = 8)
    plt.yticks(size = 8)
    
    plt.xlabel('s',fontsize=10)
    plt.ylabel('phi',fontsize=10)
    plt.title(imageInfo,fontsize=12, color='r')
    if save == 1:
        plt.savefig(plotTitle + ".png")

def linearInterpolation(x,vecX):
    idx = np.abs(vecX - x).argmin()
    id_middle = int(idx/2)
    if (x-vecX[idx])<0:
        idx -=1
    coeff = 1. - abs(x-vecX[idx])/(vecX[id_middle+1]-vecX[id_middle])
    return idx,coeff
    
def B(framework,sinoGrid,n,x,vecPhi):
    a = sinoGrid.shape[0]
    m = sinoGrid.shape[1]
    ds = 2*framework.radius/m
    weight = np.tan(vecPhi)**n / np.cos(vecPhi)
    vecProj = np.zeros(vecPhi.shape[0])
    thetaPhi = np.array([np.cos(vecPhi),np.sin(vecPhi)])
    thetaPhi = thetaPhi.T
    
    for k in range(0,a):
        s = np.dot(x,thetaPhi[k])
        sMin = np.dot(np.array([framework.xcenter,framework.ycenter]),thetaPhi[k]) - framework.radius
        sMax = sMin + 2*framework.radius
        vecS = np.arange(sMin,sMax,ds)
        (index_closest,linear_coeff) = linearInterpolation(s,vecS)
        vecProj[k] = linear_coeff*sinoGrid[k,index_closest] + (1-linear_coeff)*sinoGrid[k,index_closest+1]
    return integrale(vecPhi,vecProj*weight)
    
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
    

    