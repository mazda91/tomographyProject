import numpy as np
import matplotlib.pyplot as plt

class frameworkClass:
	#attributes
	#float xmax;
	#float ymax;
	#list imageList;
	#image currentImage;

	#initialization
	def __init__(self,xmin, ymin, xmax,ymax,imageList,currentImage):
		self.xmin = xmin;
		self.ymin = ymin;
		self.xmax = xmax;
		self.ymax = ymax;
		self.imageList = imageList;
		self.currentImage= currentImage;


	#setters
	def set_xmax (self,xmax):
		self.xmax = xmax;

	def set_ymax (self,ymax):
		self.ymax = ymax;

	def set_imageList(self,imageList):
		self.imageList = ImageList ;

	def set_imageCurrent(self,im):
		self.currentImage = im;

	#getters
	def get_xmax (self):
		return self.xmax;

	def get_ymax(self):
		return self.ymax;

	def get_ImageList(self):
		return self.imageList;

	def get_imageCurrent(selfself,):
		return self.currentImage;

	#add image im in the image list 
	def add_Image(self,im):
		self.imageList.append(im);

	#remove image im in the image list 
	def remove_Image(self,im):
		self.imageList.remove(im);

	#to plot the framework
	def plot_fram(self):
		x = np.array([self.xmin,self.xmax,self.xmax,self.xmin, self.xmin])
		y = np.array([self.ymin,self.ymin, self.ymax, self.ymax,self.ymin])
		plt.plot(x,y)
		plt.xlim(self.xmin-1, self.xmax+2)
		plt.ylim(self.ymin-1, self.ymax+2)
		plt.show()

	#nb of imageList existing
	def nb_of_image(self):
		return len(self.imageList)













		
