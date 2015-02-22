# A heap is defined by the parent being higher than the two children

import math

class Heap:
	def __init__(self):
		self.__heap = []

	def insert(self, value):
		self.__heap.append(value)
		self.__siftUp(len(self.__heap) - 1)

	def delete(self, index):
		self.__heap[index], self.__heap[-1] = self.__heap[-1], self.__heap[index]
		del(self.__heap[-1])
		self.__siftDown(index)

	def getMax(self):
		if len(self.__heap) == 0:
			return None
		else:
			return self.__heap[0]

	def getMin(self):
		if len(self.__heap) == 0:
			return None
		else:
			return self.getMinFromNode(0)

	def getMinFromNode(self, node):
		if len(self.__heap) == 0:
			return None
		else:
			#from pdb import set_trace; set_trace()
			l = node * 2 + 1
			r = node * 2 + 1
			if not self.hasChildren(node):
				return self.__heap[node]

			if self.hasLeftChild and not self.hasRightChild:
				return self.getMinFromNode(l)

			if self.hasRightChild and not self.hasLeftChild:
				return self.getMinFromNode(r)

			if self.__heap[l] < self.__heap[r]:
				return self.getMinFromNode(l)
			else:
				return self.getMinFromNode(r)

	def hasLeftChild(self, node):
		l = node * 2 + 1
		if l < len(self.__heap):
			return True
		else:
			return False

	def hasRightChild(self, node):
		r = node * 2 + 1
		if r < len(self.__heap):
			return True
		else:
			return False

	def hasChildren(self, node):
		return self.hasLeftChild(node) or self.hasRightChild(node) 

	def __siftDown(self, node):
		l = node * 2 + 1
		r = node * 2 + 1
		heap_size = len(self.__heap)

		# Get the children values
		l_val = self.__heap[l] if l < heap_size else None
		r_val = self.__heap[r] if r < heap_size else None

		# Check if we have any children
		if l_val is None and r_val is None:
			return

		# If we only have a left child
		if r_val is None and l_val is not None:
			if l_val > self.__heap[node]:
				self.__heap[node], self.__heap[l] = self.__heap[l], self.__heap[node]
				return

		# If we only have a right child
		if l_val is None and r_val is not None:
			if r_val > self.__heap[node]:
				self.__heap[node], self.__heap[r] = self.__heap[r], self.__heap[node]
				return

		biggest = l if l_val > r_val else r

		# Check if the biggest child is greater that us
		if self.__heap[biggest] > sel.__heap[node]:
			self.__heap[node], self.__heap[biggest] = self.__heap[biggest], self.__heap[node]
			self.__siftDown(biggest)

	def __siftUp(self, node):
		parent = int(math.floor((node - 1) / 2))

		if parent >= 0 and self.__heap[node] > self.__heap[parent]:
			self.__heap[node], self.__heap[parent] = self.__heap[parent], self.__heap[node]
			self.__siftUp(parent)

	def display(self):
		print(self.__heap)


h = Heap()

print(h.getMin())
print(h.getMax())

h.insert(1)
h.insert(6)
h.insert(5)
h.insert(2)
h.insert(3)
h.insert(4)
h.insert(2)

h.display()

print(h.getMin())

h.delete(3)

h.display()

print(h.getMin())
print(h.getMax())