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

frame = Framework(0,0,5)
line1 = line(frame, np.pi/2 , 2 ,0.1)
print(C1.lengthLineIntersection(line1))

#test Sinogram
center2 = np.array([0,0]); radius2 = 4; intensity2 = 4;
C2 = Circle(center2, radius2, intensity2)
line2 = line(frame,0,-10,0.1)
print(C2.lengthLineIntersection(line2))
img1 = Image()
img1.addCircle(C2)     
#center2 = np.array([1,1]); radius2 = 1; intensity2 = 4;
#C2 = Circle(center2, radius2, intensity2)
#img1.addCircle(C2)
frame.addImage(img1)
frame.setCurrentImage(0)

radonTransform = np.zeros((100,100))
radonTransform = buildSinogram(frame,100,100,0.1)
#test constantness of radonTransform for a circle
test = np.copy(radonTransform)
for k in range(1,np.shape(test)[0]):
    test[k] = test[k] - test[0]
test[0] = np.zeros(np.shape(test[0]))

#test integrale function
x = np.linspace(0,np.pi,1000)
y = np.sin(x)

res = integrale(x,y)
print(res)

#test moment function
order = 0
plt.figure()
vecMoment = moment(frame,radonTransform,order)
absPhi = np.linspace(0,np.pi,len(vecMoment))
plt.plot(absPhi,vecMoment)

#testDotProduct
phi = np.linspace(0,2*np.pi,100)
vecP = np.sin(5*phi)
vecQ = np.sin(5*phi)
res = trigoDotProduct(phi,np.ones(100),np.ones(100))
print(res)
#we derive consistent and precise values for norms of basis trigonometric 
#polynomial functions

#test projectionMoment
vecProj = projectionMoment(phi,order,vecMoment)
print(np.linalg.norm(vecMoment-vecProj))

ds = 2*frame.radius/100
line1 = line(frame,1*(2*np.pi/100),-frame.radius + 62*ds,0.1)
line2 = line(frame,2*(2*np.pi/100),-frame.radius + 62*ds,0.1)

x = C2.lengthLineIntersection(line1)
y = C2.lengthLineIntersection(line2)

