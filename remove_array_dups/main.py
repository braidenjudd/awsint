arr = [4, 32, 43, 43, 23, 0 , 1, 2, 44, 32]

deduped_arr = []

for number in arr:
	if number not in deduped_arr:
		deduped_arr.append(number)

print(arr)
print(deduped_arr)