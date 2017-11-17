class imageClass:
	#attributes
	#list circleList;

	def __init__(self,circleList):
		self.circleList = circleList;

	def get_circleList(self):
		return self.circleList;


	def add_circle(self,circle):
		self.circleList.append(circle);

	def remove_circle(self,circle):
		self.circleList.remove(circle);

	def nb_of_circle():
		return len(self.circleList)


