def findMaxLength(nums):
    max_length = 0
    count = 0
    count_map = {0: -1}

    for i in range(len(nums)):
        count += 1 if nums[i] == 1 else -1

        if count == 0:
            max_length = max(max_length, i + 1)
        elif count in count_map:
            max_length = max(max_length, i - count_map[count])
        else:
            count_map[count] = i

    return max_length
nums = [0, 1]
print(findMaxLength(nums))
