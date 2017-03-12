# This is an example of the "Selection Sort" Algorithm.

# This is the easiest sorting algorithm, but also one of the most inefficient
# ones O(n**2). It basically replaces the current element for the minimum
# element from the rest of the array. The same for each iteration.

a = [55, 3, 23, 2, 54, 4, 6, 7, 99, 103]


def selection_sort(arr):
    n = len(a)
    for i in range(n):
        min_idx = i
        
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

selection_sort(a)
print(a)

# Time Complexity: 0(n**2)
# Auxiliary Space: O(1)