class Subject:
	def __init__(self):
		self.observers = []
		self.value = ''

	def set(self, value):
		self.value = value
		for observer in self.observers:
			observer(value)

	def get(self):
		return self.value

	def register_observer(self, observer):
		self.observers.append(observer)

def observer1(value):
	print(value)

def observer2(value):
	print(value + 1)

def observer3(value):
	print(value + 2)



s = Subject()
s.set(0)
s.register_observer(observer1)
s.register_observer(observer2)
s.register_observer(observer3)
s.set(5)