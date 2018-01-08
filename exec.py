import image 
import framework
from project import *



globalFrame = Framework(0,0,150) #here to help emphasize the difference between the complete sinogram and 
#the truncated one : the sinogram is computed only for the considered part, but displayed w.r.t the whole framework 
#dimensions
FOV = Framework(0,90,50)
saveImage=0
a = 100 #nb of subdivisions of phi
m = 100 #nb of subdivisions of s
l = 1000 #nb of subdivisions of segment L
xl = -40; xr = 40; lstep = (xr-xl)/l
y0 = 100
eps = 10*np.pi/180

L = np.array([(xl + i*lstep,y0) for i in range(0,l)])

#build image
img1 = Image()

#set of disks
center2 = np.array([0,0]); radius2 = 80; intensity2 = 1;
C2 = Disk(center2, radius2, intensity2)
img1.addDisk(C2)     
center2 = np.array([10,30]); radius2 = 50; intensity2 = 2;
C2 = Disk(center2, radius2, intensity2)
    #img1.addDisk(C2)
center2 = np.array([-1,-3]); radius2 = 1; intensity2 = 2;
C2 = Disk(center2, radius2, intensity2)
    #img1.addDisk(C2)
globalFrame.addImage(img1)
FOV.addImage(img1)
globalFrame.setCurrentImage(0)
FOV.setCurrentImage(0)

sinoMatrix = sinogram(globalFrame,globalFrame,a,m,L)
sinoFOV = sinogram(globalFrame,FOV,a,m,L)


imageInfo = ""
for disk in globalFrame.getCurrentImage().getListOfDisks():
    imageInfo = imageInfo + ","+ str(disk.center)

plt.figure()
plotSinogram(globalFrame,globalFrame,sinoMatrix,"images/sinograms/2SymmetricDisks4",imageInfo,saveImage)
plt.figure()
plotSinogram(globalFrame,FOV,sinoFOV,"images/sinograms/2SymmetricDisks4",imageInfo,saveImage)

#test constantness of radonTransform for a disk
test = np.copy(sinoMatrix)
for k in range(1,np.shape(test)[0]):
    test[k] = test[k] - test[0]
test[0] = np.zeros(np.shape(test[0]))

order = 3
Bn = B(globalFrame,order,L,a,eps)
plt.figure()
plt.plot(L,Bn,"b.")



