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

def quick_sort(unsorted):








	def parition(unsorted, start, end):
		pivot = unsorted[end]
		pi = start

		for i,  in range(0, end):
			if unsorted[i] <= pivot:
				unsorted[i], unsorted[pi] = unsorted[pi], unsorted[i]
				pi += 1

		unsorted[end], unsorted[pi] = unsorted[pi], unsorted[end]
		return pi

	if (start < end):
		pi = parition(unsorted, start, end)
		print(pi)
		quick_sort(unsorted, start, pi-1)
		quick_sort(unsorted, pi+1, end)

def heap_sort(unsorted_list):
	sorted_list = unsorted_list
	return sorted_list

small_test_data = rand_list(10, 0, 20)
small_test_data2 = rand_list(10, 0, 20)
# print(small_test_data)
# print(quick_sort(small_test_data, 0, 9))
# print(small_test_data)

print(quicksort(small_test_data2))


# t_insertion = Timer(lambda: insertion_sort(test_data_insertion))
# print(t_insertion.timeit(number=5000))

# t_selection = Timer(lambda: selection_sort(test_data_selection))
# print(t_selection.timeit(number=5000))

# t_bubble = Timer(lambda: bubble_sort(test_data_bubble))
# print(t_bubble.timeit(number=5000))

# t_merge = Timer(lambda: merge_sort(test_data_merge))
# print(t_merge.timeit(number=5000))