import numpy as np
import matplotlib.pyplot as plt

class Framework:
	#attributes
	#float xmax;
	#float ymax;
	#list imageList;
	#image currentImage;

	#initialization
	def __init__(self,xmax,ymax,imageList = [],currentImage = 0): #if no image, the constructor gives 0
		self.xmax = xmax;
		self.ymax = ymax;
		self.imageList = imageList;
		self.currentImage= currentImage;


	#setters
	def setXmax (self,xmax):
		self.xmax = xmax;

	def setYmax (self,ymax):
		self.ymax = ymax;

	def setImageList(self,imageList):
		self.imageList = imageList ;

	def setCurrentImage(self,im):
		self.currentImage = im;

	#getters
	def getXmax (self):
		return self.xmax;

	def getYmax(self):
		return self.ymax;

	def getImageList(self):
		return self.imageList;

	def getCurrentImage(self):
		return self.currentImage;

	#add image im in the image list 
	def addImage(self,im):
		self.imageList.append(im);

	#remove image im in the image list 
	def removeImage(self,im):
		self.imageList.remove(im);

	#to plot the framework
	def plotFram(self):
		x = np.array([self.xmin,self.xmax,self.xmax,self.xmin, self.xmin])
		y = np.array([self.ymin,self.ymin, self.ymax, self.ymax,self.ymin])
		plt.plot(x,y)
		plt.xlim(self.xmin-1, self.xmax+2)
		plt.ylim(self.ymin-1, self.ymax+2)
		plt.show()

	#nb of imageList existing
	def nbOfImages(self):
		return len(self.imageList)













		
