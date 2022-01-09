def arrayDuplicates(stringArray):
    stringHashTable = {}
    for value in stringArray:
        if stringHashTable.get(value) is None:
            stringHashTable[value] = True
        else:
            print("Found Duplicate: ", value)
            return
    
    print("No Duplicates Found")

arrayDuplicates(["a", "b", "c", "d", "c", "e", "f"])