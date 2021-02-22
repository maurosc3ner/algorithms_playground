# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
import numpy as np
import sys

import time
sys.setrecursionlimit(5000)
class qsGeeks:
    def partition(self,arr, low, high):
        i = (low-1)		 # index of smaller element
        pivot = arr[high]	 # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:

                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    # The main function that implements QuickSort
    # arr[] --> Array to be sorted,
    # low --> Starting index,
    # high --> Ending index

    # Function to do Quick sort


    def quickSort(self,arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:

            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)


# Driver code to test above
n=10000000
prg=qsGeeks()
input=np.random.randint(0,1000,n)
# print(len(input))
print(input)
input=list(input.flatten())
start_time=time.time()
prg.quickSort(input, 0, n-1)
print("quickSort geeks --- %s seconds ---" % (time.time() - start_time))
print("Sorted array is:")
print(np.array(input))

# This code is contributed by Mohit Kumra
#This code in improved by https://github.com/anushkrishnav
