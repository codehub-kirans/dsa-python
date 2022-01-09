def characterCountInArray(array):
    if len(array) == 1:
        return len(array[0])
    elif len(array) == 0:
        return 0
    else:
        return len(array[0]) + characterCountInArray(array[1:])

#Test
print(characterCountInArray(['ab', 'cd', 'efg', 'hi']))
print(characterCountInArray([]))