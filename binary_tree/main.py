from collections import deque

class Tree:
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None

	def value(self):
		return value

	def insert(self, value):
		if self.value is None or self.value == value:
			self.value = value
		elif value > self.value:
			if self.right is None:
				self.right = Tree(value=value)
			else:
				self.right.insert(value=value)
		elif value < self.value:
			if self.left is None:
				self.left = Tree(value=value)
			else:
				self.left.insert(value=value)

	def find(self, value):
		if self.value == value:
			return value
		elif value < self.value:
			if self.left is None:
				return None
			else:
				return self.left.find(value)
		elif value > self.value:
			if self.right is None:
				return None
			else:
				return self.right.find(value)

	def is_tree_lesser(self, tree, value):
		if tree is None:
			return True
		return tree.value <= value and \
			self.is_tree_lesser(tree.left, value) and \
			self.is_tree_lesser(tree.right, value)

	def is_tree_greater(self, tree, value):
		if tree is None:
			return True
		return tree.value > value and \
			self.is_tree_greater(tree.left, value) and \
			self.is_tree_greater(tree.right, value)

	def breath_first_walk(self):
		visit_queue = deque([self]) if self.value is not None else []
		tree_nodes = []

		while len(visit_queue) > 0:
			this_node = visit_queue.popleft()

			tree_nodes.append(this_node.value)

			if this_node.left is not None:
				visit_queue.append(this_node.left)

			if this_node.right is not None:
				visit_queue.append(this_node.right)

		return tree_nodes

	def depth_first_walk(self):
		left_tree = self.left.depth_first_walk() if self.left is not None else []
		right_tree = self.right.depth_first_walk() if self.right is not None else []
		tree = [self.value] if self.value is not None else []

		return left_tree + tree + right_tree

t = Tree()
t.insert(12)
t.insert(9)
t.insert(14)
t.insert(13)
t.insert(15)
t.insert(10)
t.insert(7)
print(t.depth_first_walk())
print(t.breath_first_walk())
print(t.is_tree_lesser(t.left, t.value))
print(t.is_tree_greater(t.left, t.value))