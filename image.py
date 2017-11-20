class Image:
	#attributes
	#list circleList;

	def __init__(self,circleList):
		self.circleList = circleList;

	def getCircleList(self):
		return self.circleList;


	def addCircle(self,circle):
		self.circleList.append(circle);

	def removeCircle(self,circle):
		self.circleList.remove(circle);

	def nbOfCircles(self):
		return len(self.circleList)


