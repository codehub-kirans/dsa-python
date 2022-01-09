#Best case & Average case = O(N log N); Worst case = O(N^2/2)
class QuickSort:
    array = []

    def __init__(self, array) -> None:
        self.array = array
    
    def partition(self, left_index, right_index):
        #Setup
        pivot_index = right_index
        pivot = self.array[pivot_index]
        right_index -=1

        while True:
            while self.array[left_index] < pivot and left_index <= pivot_index:
                left_index +=1
            
            while self.array[right_index] > pivot and right_index >= 0:
                right_index -=1

            #check we've covered compared elements with a pivot in a partition traversal
            if left_index >= right_index:
                break
            else:
                #Swap left & right index values
                self.array[left_index], self.array[right_index] = self.array[right_index], self.array[left_index]
                #increment left_index to resume traversal after swap since we already compared pivoted value in the whule loop before
                left_index +=1
        
        #swap left index value and pivot
        self.array[left_index], self.array[pivot_index] = self.array[pivot_index], self.array[left_index]

        return left_index

    def sort(self, left_index, right_index):
        #base case
        if right_index - left_index <= 0:
            return

        #partition array to get the pivot index
        pivot_index = self.partition(left_index,right_index)

        #First Recursively paritition the left subarray
        self.sort(left_index, pivot_index - 1)
        #Then Recursively partition the right subarray
        self.sort(pivot_index + 1, right_index)

    def quickselect(self, kth_lowest_value, left_index, right_index):
        
        #Debug
        #print("Left Index: ", left_index, "| Right Index: ", right_index)

        #base case where the subarray has only 1 cell
        if right_index - left_index <= 0:
            kth_index_val =  str(kth_lowest_value) + "th lowest value is " + str(self.array[left_index])
            return kth_index_val

        pivot_index = self.partition(left_index, right_index)

        if kth_lowest_value < pivot_index:
            kth_index_val = self.quickselect(kth_lowest_value, left_index, pivot_index - 1)
        elif kth_lowest_value > pivot_index:
            kth_index_val = self.quickselect(kth_lowest_value, pivot_index + 1, right_index)
        else: #kth_lowest_value == pivot_index:
            kth_index_val =  str(kth_lowest_value) + "th lowest value is " + str(self.array[pivot_index])
            return kth_index_val 

        return kth_index_val

array1 = [5,1,3,8,2]
qs = QuickSort(array1)
print("Original Array: ", qs.array)
qs.sort(0, len(array1)-1)
print("Sorted Array: ", qs.array)

array2 = [0, 50, 20, 10, 60, 30, 15, 90, 23]
qs = QuickSort(array2)
print("Original Array: ", qs.array)
qs.sort(0, len(array2)-1)
print("Sorted Array: ", qs.array)

qs2 = QuickSort(array2)
print(qs2.quickselect(2, 0, len(qs2.array) - 1))

