## Selection Sorting
## Big O
## Best     Average     Worst
## O(n^2)   O(n^2)      O(n^2)
## Since we are lopping within a loop, it is n^2

from helpers import swap_items

swap = lambda arr, index1, index2: swap_items(arr, index1, index2)
    
def selection_sort(arr):
    ## outer loop
    for i in range(0, len(arr) - 1, 1):
        lowest = i
        ## inner loop
        for j in range(i + 1, len(arr), 1):
            if arr[lowest] > arr[j]:
                lowest = j
        ## check if we need to swap
        if i != lowest: 
            swap(arr, i, lowest)
    
    return arr

arr = selection_sort([0,2,34,22,10,18,13, 1])
print("Sorted: -> ", arr)

