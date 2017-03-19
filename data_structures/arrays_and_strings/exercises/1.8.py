# Time Complexity: O(n**2)
# Auxiliary Space: O(n)

def zero_matrix(A):
    zero_rows = set()
    zero_columns = set()
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i in zero_rows or j in zero_columns:
                A[i][j] = 0
    return A
A = [[1, 2, 0], [2, 3, 4], [3, 4, 2]]

assert zero_matrix(A) == [[0, 0, 0], [2, 3, 0], [3, 4, 0]]
