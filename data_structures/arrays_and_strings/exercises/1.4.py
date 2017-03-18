# Time Complexity: O(n!)
# Auxiliary Space: O(n!)
def is_permutation_of_palindrome(string):
    def _get_all_permutations(string, step=0, permutations=[]):
        if step == len(string)-1:
            return permutations.append(''.join(string))
        
        for i in range(step, len(string)):
            string_copy = [character for character in string]
            string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
            _get_all_permutations(string_copy, step + 1, permutations)
        
    def _is_there_a_palindrome(permutations):
        for permutation in permutations:
            s = permutation
            if s == s[::-1]:
                print('{}, {}'.format(s, s[::-1]))
                return True
        return False
    permutations = []
    _get_all_permutations(string.replace(' ', ''), 0, permutations)
    return _is_there_a_palindrome(permutations)
    
assert is_permutation_of_palindrome('tact coa') == True
assert is_permutation_of_palindrome('rdaar') == True
assert is_permutation_of_palindrome('thema') == False