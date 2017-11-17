# tomographyProject

framework.py contains the framework class
image.py contains the image class
test.py contains the test using these two clases

"framework.py" contains the following functions:

    __init__(self,xmax,ymax,imageList,currentImage):
    set_xmax (self,xmax):
    set_ymax (self,ymax):
	set_imageList(self,imageList):
	set_imageCurrent(self,im):

	#getters
	get_xmax (self):
	get_ymax(self):
	get_ImageList(self):
	get_imageCurrent(selfself,):

	#add image im in the image list 
	add_Image(self,im):

	#remove image im in the image list 
	remove_Image(self,im):

	#to plot the framework
	plot_fram(self):

	#nb of imageList existing
	nb_of_image(self):

"image.py" contains contains the following functions:

    __init__(self,circleList):
	get_circleList(self):
	add_circle(self,circle):
	remove_circle(self,circle):
	nb_of_circle():
