class SingletonFactory:
	def __init__(self, class_name):
		self.__class = class_name
		self.__instance = None

	def createSingleton(self):
		if self.__instance is None:
			self.__instance = self.__class()
			return self.__instance
		else:
			return self.__instance

class Subject:
	def outputFive(self):
		print('5')

s = Subject()
s2 = Subject()
s.outputFive()
s2.outputFive()
print(s is s2)

sf = SingletonFactory(Subject)
sf1 = sf.createSingleton()
sf2 = sf.createSingleton()
sf1.outputFive()
sf2.outputFive()
print(sf1 is sf2)