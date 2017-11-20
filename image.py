class Image:
	#attributes
	#list circleList;

	def __init__(self,listOfCircles = []):
		self.listOfCircles = listOfCircles;

	def getListOfCircles(self):
		return self.listOfCircles;


	def addCircle(self,circle):
		self.listOfCircles.append(circle);

	def removeCircle(self,circle):
		self.listOfCircles.remove(circle);

	def nbOfCircles(self):
		return len(self.listOfCircles)


