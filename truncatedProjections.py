# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 16:17:11 2017

@author: mazouth--laurol
"""

import image 
import framework
from project import *

#initialization of parameters and set the framework=FOV

frame = Framework(0,0,5)
saveImage=0
a = 100 #nb of subdivisions of phi
m = 1000 #nb of subdivisions of s
l = 1000 #nb of subdivisions of segment L
xl = -10; xr = 10; lstep = (xr-xl)/l
y0 = 10
eps = 5

L = np.array([(xl + i*lstep,y0) for i in range(0,l)])

