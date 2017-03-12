a = [55, 3, 23, 2, 54, 4, 6, 7, 99, 103]


# We assume that the array is "sorted". Otherwise this won't work.
def binary_search(arr, item):
    first = 0
    last = len(arr) - 1
    found_item_idx = None

    # We check that we both didn't find the item already, and that we
    # didn't run out of items in the array.
    while first <= last and not found_item_idx:
        m = first + last // 2
        if arr[m] == item:
            found_item_idx = m
        else:
            # Here is the "magic". We split the array and
            # "chose" the right part depending on the values.
            if item < arr[m]:
                last = m - 1
            else:
                first = m + 1
    return found_item_idx

print(binary_search(a, 103))

# Time Complexity: 0(log n)
# Auxiliary Space: O(1)