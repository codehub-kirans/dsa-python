#O(N^2/2)
def selectionSort(list):
    for i in range(0, len(list) - 1):
        lowestNumberIndex = i # Initialize lowest number index in each pass through
        for j in range(i + 1, len(list)):
            if list[j] < list[lowestNumberIndex]:
                lowestNumberIndex = j

        if i != lowestNumberIndex: #swap if the lowest value is not in its correct place
            temp = list[i]
            list[i] = list[lowestNumberIndex]
            list[lowestNumberIndex] = temp

    return list

#Test function
print(selectionSort([65,55,45,35,25,15,10]))