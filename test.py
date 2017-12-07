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



frame = Framework(0,0,5)
a = 100 #nb of subdivisions of phi
m = 1000 #nb of subdivisions of s

#test Sinogram
center2 = np.array([0,0]); radius2 = 1; intensity2 = 2;
C2 = Circle(center2, radius2, intensity2)

img1 = Image()
img1.addCircle(C2)     
center2 = np.array([1,1]); radius2 = 2; intensity2 = 4;
C2 = Circle(center2, radius2, intensity2)
#img1.addCircle(C2)
frame.addImage(img1)
frame.setCurrentImage(0)

sinoMatrix= np.zeros((a,m))
sinoMatrix = sinogram(frame,a,m)
plotSinogram(frame,sinoMatrix)
#test constantness of radonTransform for a circle
test = np.copy(sinoMatrix)
for k in range(1,np.shape(test)[0]):
    test[k] = test[k] - test[0]
test[0] = np.zeros(np.shape(test[0]))

#test integrale function
x = np.linspace(0,np.pi,1000)
y = np.sin(x)

res = integrale(x,y)
print(res)

#test moment function
order = 5
plt.figure()
vecMoment = moment(frame,sinoMatrix,order)
absPhi = np.linspace(0,2*np.pi,len(vecMoment))
plt.plot(absPhi,vecMoment)

#testDotProduct
phi = np.linspace(0,2*np.pi,a)
vecP = np.sin(5*phi)
vecQ = np.sin(5*phi)
res = trigoDotProduct(phi,np.ones(a),np.ones(a))
print(res)
#we derive consistent and precise values for norms of basis trigonometric 
#polynomial functions

#test projectionMoment
vecProj = projectionMoment(phi,order,vecMoment)
plt.figure()
plt.plot(phi,vecProj)
print(np.linalg.norm(vecMoment-vecProj))


