# Time Complexity: O(n)
# Auxiliary Space: O(1)

def are_they_zero_or_one_edits_away(string1, string2):
    def _check_insert_or_delete(string1, string2):
        index1 = 0
        index2 = 0
        found = True

        while (index1 < len(string1) and index2 < len(string2)):
            if string1[index1] != string2[index2]:
                if found == False:
                    return False

                if len(string1) < len(string2):
                    index2 += 1
                else:
                    index1 += 1
                found = False
            else:
                index1 += 1
                index2 += 1

        if not found and (index1 != len(string1) or index2 != len(string2)):
            return False

        return True
    
    def _check_replace(string1, string2):
        found = True
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                if found == False:
                    return False
                
                found = False
        return True

    if len(string1) == len(string2):
        return _check_replace(string1, string2)
    elif abs(len(string1) - len(string2)) == 1:
        return _check_insert_or_delete(string1, string2)
    else:
        return False
        
assert are_they_zero_or_one_edits_away('hello', 'hllo') == True
assert are_they_zero_or_one_edits_away('hello', 'hll') == False
assert are_they_zero_or_one_edits_away('hello', 'helo') == True
assert are_they_zero_or_one_edits_away('hello', 'hillo') == True
assert are_they_zero_or_one_edits_away('hello', 'hileo') == False
assert are_they_zero_or_one_edits_away('h', 'hello') == False
assert are_they_zero_or_one_edits_away('', 'h') == True
assert are_they_zero_or_one_edits_away('', 'he') == False
assert are_they_zero_or_one_edits_away('hell', 'hello') == True