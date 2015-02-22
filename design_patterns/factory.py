class SubjectFactory:
	def __init__(self, class_name):
		self.__class = class_name

	def createSubject(self):
		return self.__class()

class Subject:
	def outputFive(self):
		print('5')

sf = SubjectFactory(Subject)
s1 = sf.createSubject()
s2 = sf.createSubject()
s1.outputFive()
s2.outputFive()
print(s1 is s2)