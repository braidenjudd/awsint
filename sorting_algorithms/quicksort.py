import random
from timeit import Timer
import math

def rand_list(number_values, max_value, min_value):
	def rand_list_item(number_values, max_value, min_value):
		for i in range(0, number_values):
			yield random.randint(max_value, min_value)

	rand_list = []
	for value in rand_list_item(number_values, max_value, min_value):
		rand_list.append(value)

	return rand_list



small_test_data = rand_list(10, 0, 20)
print(small_test_data)
quicksort(small_test_data)
print(small_test_data)

# t_insertion = Timer(lambda: insertion_sort(test_data_insertion))
# print(t_insertion.timeit(number=5000))