#Best case O(N), average case O(N^2/2). worst case O(N^2)
def insertionSort(list):
    for i in range(1, len(list)):
        tempValue = list[i] #initialize second value of each pass-through
        position = i - 1 #initialize position to left of tempValue

        while position >= 0:
            if list[position] > tempValue:
                list[position + 1] = list[position]
                position -=1
            else:
                break

        list[position + 1] = tempValue #insert tempValue back into correct position
    
    return list

#Test function
print(insertionSort([65,55,45,35,25,15,10]))