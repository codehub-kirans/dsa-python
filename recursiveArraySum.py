def recursiveArraySum(array):
    if len(array) == 0:
        return 0
    return array[0] + recursiveArraySum(array[1:])

#Test Sum
print(recursiveArraySum([1,2,3,4,5]))
print(recursiveArraySum([]))