import image 
import framework
from project import *

##here diskList contains 4 disks 
#diskList1 = [1,2,3,4];
#diskList2 = [5,6,7,8];
#diskList3 = [9,10,11,12];
#
#
#im1 = image.imageClass(diskList1);
#im2 = image.imageClass(diskList2);
#im3 = image.imageClass(diskList3);
#
#attr1 = im1.get_diskList();
#im1.add_disk(10);
#im1.remove_disk(2);
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
saveImage=0
a = 100 #nb of subdivisions of phi
m = 1000 #nb of subdivisions of s

#test Sinogram
center2 = np.array([0,0]); radius2 = 2; intensity2 = 2;
C2 = Disk(center2, radius2, intensity2)

img1 = Image()
#img1.addDisk(C2)     
center2 = np.array([1,3]); radius2 = 1; intensity2 = 2;
C2 = Disk(center2, radius2, intensity2)
img1.addDisk(C2)
center2 = np.array([-1,-3]); radius2 = 1; intensity2 = 2;
C2 = Disk(center2, radius2, intensity2)
img1.addDisk(C2)
frame.addImage(img1)
frame.setCurrentImage(0)

sinoMatrix= np.zeros((a,m))
sinoMatrix = sinogram(frame,a,m)
imageInfo = ""
for disk in frame.getCurrentImage().getListOfDisks():
    imageInfo = imageInfo + ","+ str(disk.center)


plotSinogram(frame,sinoMatrix,"images/sinograms/2SymmetricDisks4",imageInfo,saveImage)
#test constantness of radonTransform for a disk
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
order = 0
plt.figure()
vecMoment = moment(frame,sinoMatrix,order)
absPhi = np.linspace(0,2*np.pi,len(vecMoment))
plt.plot(absPhi,vecMoment)
#plt.savefig("images/moments/unitDiskMoment0.png")


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
#plt.savefig("images/moments/unitDiskProjMoment0.png")
print(np.linalg.norm(vecMoment-vecProj))


