def string_rotation(string1, string2):
    def _is_substring(string1, string2):
        """
        Check if `string2` is a substring of `string1`
        """
        substring = ''
        i = 0
        j = 0

        while (i < len(string1) and j < len(string2)):
            if string1[i] == string2[j]:
                substring += string2[j]
                j += 1
            else:
                j = 0
                substring = ''
            i += 1

        return string2 == substring

    if len(string1) != len(string2):
        return False
    else:
        return _is_substring(string1+string1, string2)

assert string_rotation('hello', 'ohell') == True
assert string_rotation('waterbottle', 'erbottlewat') == True
assert string_rotation('waterbottle', 'amparo') == False
