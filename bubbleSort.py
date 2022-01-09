#O(N^2)
def bubbleSort(list):
    unsortedIndexSoFar = len(list) - 1
    isSorted = False #Prelimnarilty establish list is unsorted

    while not isSorted:
        isSorted = True
        for i in range(unsortedIndexSoFar):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i] #bubble up the larger value to the right
                isSorted = False
        unsortedIndexSoFar -= 1 # on each pass-through, the largest value has been bubbled up to the right in the correct position

    return list        

#Test function
print(bubbleSort([65,55,45,35,25,15,10]))