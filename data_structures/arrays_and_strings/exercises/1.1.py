# Time Complexity: 0(n**2)
# Auxiliary Space: 0(1)
def has_unique_characters(string):
    for idx_i, i in enumerate(string):
        for idx_j, j in enumerate(string):
            if i == j and idx_i != idx_j:
                return False
    return True


assert has_unique_characters('ice') == True
assert has_unique_characters('iceberg') == False
assert has_unique_characters('icebergg') == False
assert has_unique_characters('ioce') == True