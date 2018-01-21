# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 01:29:06 2017

@author: mazouth--laurol
"""
import image 
import framework
from project import *
import unittest

class SinoGramTest(unittest.TestCase):
    """test case utilisé pour les fonctions utiles au calcul du sinograme"""
    
    def setUp(self):
        """Initialisation des tests"""
        self.frame = Framework(0,0,5)
        self.a = 100 #nb of subdivisions of phi
        self.m = 1000 #nb of subdivisions of s
        self.vecX = np.arange(0,1,0.1)
        #define an image in the framework
        img1 = Image()
        center1 = np.array([0,0]); radius1 = 2; intensity1 = 2;
        self.disk = Disk(center1, radius1, intensity1)
        img1.addDisk(self.disk)
        self.frame.addImage(img1)
    def test_lengthLineIntersection(self):
        """teste le fonctionnement de lengthLineIntersection"""
        res = self.disk.lengthLineIntersection(0,0)
        self.assertEqual(res, 4)
        
    def test_integrale(self):
        """Test de la fonction integrale"""
        x = np.linspace(0,np.pi,1000)
        y = -np.sin(x)
        
        res = integrale(x,y)
        self.assertTrue(abs(-2-res) <= 10**-5)
    
    def test_dotProduct(self):
        """test la fonction DotProduct"""
        phi = np.linspace(0,2*np.pi,self.a)
        vecP = np.sin(5*phi)
        vecQ = np.sin(6*phi)
        res = trigoDotProduct(phi,vecP,vecQ)
        self.assertTrue(abs(res) <= 10**-10)
        
    def test_linearInterpolation(self):
        self.assertEqual((6,0.5),linearInterpolation(0.65,self.vecX))
    
 
        
        