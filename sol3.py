def validMountainArray(arr):
    if len(arr) < 3:
        return False

    i, j = 0, len(arr) - 1

    while i < len(arr) - 1 and arr[i] < arr[i + 1]:
        i += 1

    while j > 0 and arr[j] < arr[j - 1]:
        j -= 1

    return i > 0 and j < len(arr) - 1 and i == j
arr = [2, 1]
print(validMountainArray(arr))
