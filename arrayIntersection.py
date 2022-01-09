def arrayIntersection(array1, array2):
    hashTable = {}
    intersectionArray = []
    if len(array1) >= len(array2):
        largerArray = array1
        smallerArray = array2
    else:
        largerArray = array2
        smallerArray = array1

    for value in largerArray:
        hashTable[value] = True

    for value in smallerArray:
        if hashTable.get(value) is not None:
            intersectionArray.append(value)

    print(intersectionArray)

arrayIntersection( [1,2,3,4,5], [0,2,4,6,8] )
