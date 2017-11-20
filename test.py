import image 
import framework
from project import *

##here circleList contains 4 circles 
#circleList1 = [1,2,3,4];
#circleList2 = [5,6,7,8];
#circleList3 = [9,10,11,12];
#
#
#im1 = image.imageClass(circleList1);
#im2 = image.imageClass(circleList2);
#im3 = image.imageClass(circleList3);
#
#attr1 = im1.get_circleList();
#im1.add_circle(10);
#im1.remove_circle(2);
#
#print(attr1);
#print('\n');
#
#xmin = 0
#ymin = 0 
#xmax = 10
#ymax = 10
#imageList = [im1, im2]
#currentImage = im1 
#fram1 =  framework.frameworkClass(xmin , ymin, xmax,ymax,imageList,currentImage)
##print(fram1.get_ymax())
#fram1.plot_fram()
#
#fram1.add_Image(im3)
#print("the number of image in this fram is " , fram1.nb_of_image() ) 
#
#
#fram1.remove_Image(im3)
#print("the number of image in this fram is " , fram1.nb_of_image()) 
#
#
# #test isInCircle
##expected result : True, False, False, False, False
center1 = np.array([2,2]); radius1 = 2; intensity1 = 0;
C1 = Circle(center1, radius1, intensity1)
point1 = np.array([2,4]); point2 = np.array([2,4.1]); point3 = np.array([2,-0.1]); point4 = np.array([-0.1,2]); point5 = np.array([4,1.5])
list_points = [point1,point2,point3,point4,point5]
for point in list_points:
    print(C1.isInCircle(point))

#test lengthLineIntersection
#expected result : 4.0
line2 = np.array([(2,0.25*i) for i in range (0,10)])
print(C1.lengthLineIntersection(line2))

frame = Framework(10,10)
line1 = line(frame, np.pi/2 , 3 ,0.01)
print(C1.lengthLineIntersection(line1))

#test Sinogram
center2 = np.array([0,0]); radius2 = 1; intensity2 = 2;
C2 = Circle(center2, radius2, intensity2)
line2 = line(frame,0,-10,0.1)
line3 = np.array([(-10,0.1*i) for i in range(-101,101)])
print(C2.lengthLineIntersection(line3))
img1 = Image()
img1.addCircle(C2)     

frame.addImage(img1)
frame.setCurrentImage(img1)

buildSinogram(frame,10,10,0.1)





