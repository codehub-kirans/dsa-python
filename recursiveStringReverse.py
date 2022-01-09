def recursiveStringReverse(string):
    if len(string) == 0:
        return ''
    return recursiveStringReverse(string[1:]) + string[0] 

#test reverse
print(recursiveStringReverse("abcde"))