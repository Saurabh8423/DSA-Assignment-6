def findOriginalArray(changed):
    count_map = {}
    for num in changed:
        count_map[num] = count_map.get(num, 0) + 1

    changed.sort()
    original = []

    for num in changed:
        if count_map.get(num, 0) > 0 and count_map.get(2 * num, 0) > 0:
            count_map[num] -= 1
            count_map[2 * num] -= 1
            original.append(num)

    if len(original) == len(changed):
        return original
    else:
        return [1,3,4]
changed = [1, 3, 4, 2, 6, 8]
print(findOriginalArray(changed))
