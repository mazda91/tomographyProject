import image 
import framework
from project import *



globalFrame = Framework(0,0,150)
truncatedFrame = Framework(0,130,50)
saveImage=0
a = 100 #nb of subdivisions of phi
m = 1000 #nb of subdivisions of s

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
truncatedFrame.addImage(img1)
globalFrame.setCurrentImage(0)
truncatedFrame.setCurrentImage(0)

sinoMatrix = sinogram(globalFrame,globalFrame,a,m)
truncsino = sinogram(globalFrame,truncatedFrame,a,m)


imageInfo = ""
for disk in globalFrame.getCurrentImage().getListOfDisks():
    imageInfo = imageInfo + ","+ str(disk.center)

plt.figure()
plotSinogram(globalFrame,truncatedFrame,truncsino,"images/sinograms/2SymmetricDisks4",imageInfo,saveImage)
#plotSinogram(globalFrame,globalFrame,sinoMatrix,"images/sinograms/2SymmetricDisks4",imageInfo,saveImage)
#test constantness of radonTransform for a disk
test = np.copy(sinoMatrix)
for k in range(1,np.shape(test)[0]):
    test[k] = test[k] - test[0]
test[0] = np.zeros(np.shape(test[0]))





