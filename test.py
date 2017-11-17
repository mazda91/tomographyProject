import image 
import framework

#here circleList contains 4 circles 
circleList1 = [1,2,3,4];
circleList2 = [5,6,7,8];
circleList3 = [9,10,11,12];


im1 = image.imageClass(circleList1);
im2 = image.imageClass(circleList2);
im3 = image.imageClass(circleList3);

attr1 = im1.get_circleList();
im1.add_circle(10);
im1.remove_circle(2);

print(attr1);
print('\n');

xmin = 0
ymin = 0 
xmax = 10
ymax = 10
imageList = [im1, im2]
currentImage = im1 
fram1 =  framework.frameworkClass(xmin , ymin, xmax,ymax,imageList,currentImage)
#print(fram1.get_ymax())
fram1.plot_fram()

fram1.add_Image(im3)
print("the number of image in this fram is " , fram1.nb_of_image() ) 


fram1.remove_Image(im3)
print("the number of image in this fram is " , fram1.nb_of_image()) 








