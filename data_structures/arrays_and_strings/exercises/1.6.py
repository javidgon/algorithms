# Time Complexity: O(n)
# Auxiliary Space: O(n)

def compress_string(string):
    previous_char = None
    size = 0
    chars = []

    def _append(previous_char, size):
        if size > 1:
            chars.append('{}{}'.format(previous_char, size))
        else:
            chars.append(previous_char)

    for idx, char in enumerate(string):
        if previous_char == char or not previous_char:
            size += 1
        else:
            _append(previous_char, size)
            size = 1

        previous_char = char
        if idx == len(string) - 1:
            _append(previous_char, size)

    compressed_string = ''.join(chars)
    return compressed_string if len(compressed_string) < len(string) else string
    
assert compress_string('aabcccd') == 'a2bc3d'
assert compress_string('aaaaabbbbbcccd') == 'a5b5c3d'
assert compress_string('aabc') == 'aabc'            