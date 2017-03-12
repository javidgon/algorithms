a = [55, 3, 23, 2, 54, 4, 6, 7, 99, 103]

n = len(a)


def quicksort(arr, start, end):
    def _partition(arr, start, end):
        # Our pivot is always the first element in the array
        pivot = arr[start]

        # We define two markers
        left = start + 1
        right = end

        # We do this only until both markers cross
        while not right < left:
            # Place the left marker on the first element that is bigger
            # than the pivot
            while left <= right and arr[left] <= pivot:
                left = left + 1
            # Place the right marker on the first element that is smaller
            # than the pivot
            while right >= left and arr[right] >= pivot:
                right = right - 1

            # Before switching them, we make sure that both markers
            # have not crossed!
            if right >= left:
                # Switch the elements as they were not properly ordered
                arr[left], arr[right] = arr[right], arr[left]

        # Switch the pivot with the middle point represented by "right"
        arr[start], arr[right] = arr[right], arr[start]

        return right

    if start < end:
        # partition the list
        pivot = _partition(arr, start, end)
        # sort both halves
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, end)
    return arr

quicksort(a, 0, n - 1)
print(a)

# Time Complexity: 0(n * log n)
# Auxiliary Space: O(1)