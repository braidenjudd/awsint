numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 5

def pairs(nums, target_sum):
    pairs = []

    for i, num in enumerate(nums):
        for n in nums[i:]:
            if (n + num) == target_sum:
                pairs.append((num, n))

    return pairs

for pair in pairs(numbers, target_sum):
    print(pair)

