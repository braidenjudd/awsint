class Subject:
	def __init__(self, value):
		self.__value = value

	def getCostPrice(self):
		return self.__value * 1.0

	def getSalePrice(self):
		return self.__value * 1.3

class GSTTaxedSubject:
	def __init__(self, subject):
		self.__subject = subject

	def getCostPrice(self):
		return self.__subject.getCostPrice() * 1.0

	def getSalePrice(self):
		return self.__subject.getSalePrice() * 1.1

s = Subject(10)
print(s.getCostPrice())
print(s.getSalePrice())

gst_s = GSTTaxedSubject(s)
print(gst_s.getCostPrice())
print(gst_s.getSalePrice())