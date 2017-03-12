# This is an example of the "Bubble Sort" Algorithm.

# This is also quite inefficient O(n**2).
# It works on "pairs", so on each iteration it compares the current element
# with the one on its right side, and if it has a lower value, it switches them.

a = [55, 3, 23, 2, 54, 4, 6, 7, 99, 103]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort(a)
print(a)

# Time Complexity: 0(n**2)
# Auxiliary Space: O(1)