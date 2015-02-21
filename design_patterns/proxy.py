from timeit import Timer

class Proxy:
	def __init__(self):
		self.s = Subject()
		self.__getCount = 0
		self.cacheValue = None
		self.cache = True

	def get2ToPowerOf(self):
		self.__getCount += 1

		if not self.cache:
			return self.s.get2ToPowerOf()
		
		if self.cacheValue is None:
			self.cacheValue = self.s.get2ToPowerOf()
			return self.cacheValue
		else:
			return self.cacheValue

	def setExp(self, value):
		self.cacheValue = None
		self.s.setExp(value)

	def getGetCount(self):
		return self.__getCount

	def toggleCache(self):
		self.cache = not self.cache

class Subject:
	def __init__(self):
		value = ''

	def get2ToPowerOf(self):
		return 2**self.value

	def setExp(self, value):
		self.value = value

p = Proxy()
p.setExp(12738)

t = Timer(lambda: p.get2ToPowerOf())
print(t.timeit(number=5000))
p.toggleCache()
print(t.timeit(number=5000))