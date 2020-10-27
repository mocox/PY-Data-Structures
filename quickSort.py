## Quick Sort
## Big O
##  Worst    Average           Best
## O(n^2)   O(n log n)      O(n log n)
##

from helpers import swap_items

swap = lambda arr, index1, index2: swap_items(arr, index1, index2)

def pivot(arr, start, end): 
    # get the start pivot value   
    pivot = arr[start]
    # get the initila swapIndex
    swapIndex = start
    # loop the array from start to end indexes
    for i in range(start, end, 1):
        # if the pivot value is less than the value at the array index
        # then swap the values
        if pivot > arr[i]:
            swapIndex+=1
            swap(arr, swapIndex, i)
    # swap the pivot value
    swap(arr, start, swapIndex)
    return swapIndex
    
def quick_sort(arr, left = 0, right = 0):
    # set right as value of array length
    if right == 0:
        right = len(arr) - 1
    # the left index is less than the right index, i.e start is less than the end
    if (left < right):
        # get the pivot index from the array
        pIndex = pivot(arr, left, right)
        # perform recursion on both left and right sides
        quick_sort(arr, left, pIndex - 1)
        quick_sort(arr, pIndex + 1, right)

    return arr

arr = quick_sort([23,4,123,101, 6, 18, 1002])
print("Sorted array -> ", arr)

