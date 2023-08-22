def number_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the remaining unsorted part of the array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the first element in the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


numbers = [21, 400, 8, -3, 77, 99, -16, 55, 111, -36, 28]
number_sort(numbers)
print(numbers)
