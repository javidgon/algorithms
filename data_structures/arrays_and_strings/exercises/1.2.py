# Time Complexity: O(n)
# Auxiliary Space: O(n)
def is_a_permutation(string1, string2):
    def _get_chars(string):
        chars = {}
        for i in string:
            if not chars.get(i):
                chars[i] = 1
            else:
                chars[i] += 1
        return chars
    
    chars1 = _get_chars(string1)
    chars2 = _get_chars(string2)
    return chars1 == chars2

assert is_a_permutation('eci', 'ice') == True
assert is_a_permutation('hello', 'olle') == False
assert is_a_permutation('hello', 'holle') == True
    
    
    