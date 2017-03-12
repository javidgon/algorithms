a = [55, 3, 23, 2, 54, 4, 6, 7, 99, 103]

n = len(a)


def merge_sort(arr, start, end):
    def _merge(arr, m):
        i = 0
        j = 0
        k = 0
        
        left_arr = arr[:m]
        right_arr = arr[m:]

        # Start comparing elements from the left and right side. We chose the
        # one which is smaller.
        while(i < len(left_arr) and j < len(right_arr)):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # This two while loops are necessary in case there're still elements
        # that have not been fully merged (either from the left or right side).
        while(i < len(left_arr)):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while(j < len(right_arr)):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    if start < end:
        # We figure out the middle idx
        m = (start + end)//2

        # Left Array: [l,m]
        merge_sort(arr, start, m)
        # Right Array: [m+1,r]
        merge_sort(arr, m+1, end)
        # Finally, we merge the arrays.
        _merge(arr, m)

merge_sort(a, 0, n-1)
print(a)

# Time Complexity: 0(n * log n)
# Auxiliary Space: O(n)