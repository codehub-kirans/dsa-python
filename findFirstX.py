def findFirstX(string):
    if string[0] == 'x':
        return 0
    else:
        return 1 + findFirstX(string[1:])
