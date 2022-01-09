def firstNonDuplicate(string):
    stringHashTable = {}
    for character in string:
        if stringHashTable.get(character) is None:
            stringHashTable[character] = True
        else:
            stringHashTable[character] = False

    for k,v in stringHashTable.items():
        if v is True:
            print("Non-duplicate: ",k)
            #break

firstNonDuplicate("minimum")
