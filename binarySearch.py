## Binary Searching, only works on sorted array
## Big O
## Best     Average     Worst
## O(1)     (Log n)     (log n)
## O(log n) almost equals O(1)

import math

def binary_search(arr, which):
    start = 0
    end = len(arr) - 1
    middle = math.floor((start + end) / 2)
    ## loop through array
    while arr[middle] != which and start <= end:
        ## print the varaiables
        print(start, middle, end)
        ## check the logic and change start and end as appropriate
        if which < arr[middle]: 
            end = middle - 1
        else:
            start = middle + 1
        ## get a new middle
        middle = math.floor((start + end) / 2)
    
    return middle if arr[middle] == which else -1


index = binary_search([2,3,5,6,9,13,15,28,30], 13)
print("index is :-> ", index)