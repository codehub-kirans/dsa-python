def recursiveCountX(string):
    if len(string) == 0:
        return 0

    if string[0] == 'X':
        return 1 + recursiveCountX(string[1:])
    else:
        return 0 + recursiveCountX(string[1:])

#test countX
print(recursiveCountX('XaXbXc'))
print(recursiveCountX(''))