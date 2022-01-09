def evenCountInArray(array):
    if len(array) == 0:
        return [] #Return Empty Array
    if array[0] % 2 == 0:
        return [array[0]] + evenCountInArray(array[1:])
    else:
        return evenCountInArray(array[1:])

#Test
print(evenCountInArray([1,2,3,4,5]))