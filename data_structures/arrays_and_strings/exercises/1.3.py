# Time Complexity: O(n)
# Auxiliary Space: O(n)

def urlify(string, string_length):
    def _replace_space(char):
        if char == ' ':
            return '%20'
        else:
            return char
    return ''.join([_replace_space(char) for char in string])
    
string = 'hello my friend'
assert urlify(string, len(string)) == 'hello%20my%20friend'