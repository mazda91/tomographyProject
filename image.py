class Image:
	#attributes
	#list diskList;

	def __init__(self,listOfDisks = []):
		self.listOfDisks = listOfDisks;

	def getListOfDisks(self):
		return self.listOfDisks;


	def addDisk(self,disk):
		self.listOfDisks.append(disk);

	def removeDisk(self,disk):
		self.listOfDisks.remove(disk);

	def nbOfDisks(self):
		return len(self.listOfDisks)


