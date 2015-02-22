import random
from timeit import Timer
import math

def rand_list(number_values, max_value, min_value):
	rand_list = []
	for value in rand_list_item(number_values, max_value, min_value):
		rand_list.append(value)

	return rand_list

def rand_list_item(number_values, max_value, min_value):
	for i in range(0, number_values):
		yield random.randint(max_value, min_value)

test_data_selection = rand_list(100, 0, 100)
test_data_bubble = test_data_selection[:]
test_data_merge = test_data_selection[:]
test_data_insertion = test_data_selection[:]
test_data_quicksort = test_data_selection[:]

def selection_sort(unsorted_list):
	sorted_list = []
	while len(unsorted_list) > 0:	
		min_value = min(unsorted_list)
		min_index = unsorted_list.index(min_value)
		sorted_list.append(min_value)
		del(unsorted_list[min_index])

	return sorted_list


[1, 4, 6, 2, 5, 2, 20]
def insertion_sort(unsorted_list):
	for i in range(0, len(unsorted_list)):
		value = unsorted_list[i]
		hole = i
		while hole > 0 and unsorted_list[hole - 1] > value:
			unsorted_list[hole], unsorted_list[hole - 1] = unsorted_list[hole - 1], unsorted_list[hole]
			hole = hole - 1

	return unsorted_list

def bubble_sort(unsorted_list):
	num_sorted = len(unsorted_list) - 1

	while num_sorted > 0:
		swapped = False
		for i in range(0, num_sorted):
			if unsorted_list[i] > unsorted_list[i+1]:
				unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
				swapped = True
		num_sorted -= 1
		if swapped is False:
			break

	return unsorted_list

def merge_sort(unsorted_list):
	def merge(l_list, r_list):
		ri = 0
		li = 0
		
		sorted_list = []

		while li < len(l_list) and ri < len(r_list):
			if (l_list[li] < r_list[ri]):
				sorted_list.append(l_list[li])
				li += 1
			else:
				sorted_list.append(r_list[ri])
				ri += 1

		if li < len(l_list):
			sorted_list += (l_list[li:])

		if ri < len(r_list):
			sorted_list += (r_list[ri:])

		return sorted_list

	if len(unsorted_list) < 2:
		return unsorted_list

	mid = math.floor(len(unsorted_list) / 2)
	l_list = merge_sort(unsorted_list[:mid])
	r_list = merge_sort(unsorted_list[mid:])

	return merge(l_list, r_list)

def quick_sort(unsorted, start, end):
	def parition(data, start, end):
		pivot = data[end]
		pi = start

		for i in range(start, end):
			if data[i] <= pivot:
				data[i], data[pi] = data[pi], data[i]
				pi += 1

		data[end], data[pi] = data[pi], data[end]
		return pi
	
	if start < end:
		pivot = parition(unsorted, start, end)
		quick_sort(unsorted, start, pivot - 1)
		quick_sort(unsorted, pivot + 1, end)

def quicksort(unsorted):
	quick_sort(unsorted, 0, len(unsorted) - 1)
	return unsorted

def heap_sort(unsorted_list):
	def siftDown(a, start, end):
		root = start

		while root * 2 + 1 <= end:
			l = root * 2 + 1
			r = root * 2 + 2
			swap = root

			if a[root] < a[l]:
				swap = l
			if r <= end and a[root] < a[r]:
				swap = r
			if swap == root:
				return
			else:
				a[root], a[swap] = a[swap], a[root] 
				swap = root

	def heapify(a, count):
		start = int(math.floor((count - 2) / 2))
		while start >= 0:
			siftDown(a, start, count - 1)
			start -= 1

		return a

	sorted_list = heapify(unsorted_list, len(unsorted_list))
	end = len(unsorted_list) - 1
	while end > 0:
		print(unsorted_list)
		unsorted_list[0], unsorted_list[end] = unsorted_list[end], unsorted_list[0]
		end -= 1
		siftDown(unsorted_list, 0, end)

	return sorted_list

small_test_data = rand_list(10, 0, 20)
print(small_test_data)
print(heap_sort(small_test_data))

# small_test_data2 = rand_list(10, 0, 20)
# # print(small_test_data)
# # 
# # print(small_test_data)

# t_quicksort = Timer(lambda: quicksort(test_data_quicksort[:]))
# print(t_quicksort.timeit(number=5000))

# t_selection = Timer(lambda: selection_sort(test_data_selection))
# print(t_selection.timeit(number=5000))

# t_bubble = Timer(lambda: bubble_sort(test_data_bubble))
# print(t_bubble.timeit(number=5000))

# t_merge = Timer(lambda: merge_sort(test_data_merge))
# print(t_merge.timeit(number=5000))