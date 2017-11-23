import numpy as np
import matplotlib.pyplot as plt

class Framework:
	#attributes
	#float xmax;
	#float ymax;
	#list imageList;
	#image currentImage;

	#initialization
	def __init__(self,xcenter,ycenter ,radius, imageList = [],currentImage = 0): #if no image, the constructor gives 0
		self.xcenter = xcenter;
		self.ycenter = ycenter;
		self.imageList = imageList;
		self.currentImage= currentImage;
		self.radius = radius;

	#setters
	def setXcenter (self,xcenter):
		self.xcenter = xcenter;

	def setYcenter (self,ymax):
		self.ycenter = ycenter;

	def setRadius(self, radius):
		self.radius = radius;

	def setImageList(self,imageList):
		self.imageList = imageList ;

	def setCurrentImage(self,order):
		self.currentImage = self.imageList(order);

	#getters
	def getXcenter (self):
		return self.xcenter;

	def getYcenter(self):
		return self.ycenter;

	def getRadius(self):
		return self.radius;

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













		
