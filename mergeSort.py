## Merge Sort 
## Big O
##   Worst       Average          Best
## O(n log n)   O(n log n)      O(n log n)
##

import math

def merge(arr1, arr2):
    arrMerged = []
    i = j = 0
    # loop through and append ass necessary
    while (i < len(arr1) and j < len(arr2)):
        if arr2[j] > arr1[i]:
            arrMerged.append(arr1[i])
            i+=1
        else:
            arrMerged.append(arr2[j])
            j+=1
    # get the rest of arr1
    while (i < len(arr1)):
        arrMerged.append(arr1[i])
        i+=1

    # get the rest of arr 2
    while (j < len(arr2)):
        arrMerged.append(arr2[j])
        j+=1
    print('arrays -> ', arrMerged)
    return arrMerged

def merge_sort(arr):
    # gate keeper for recursion
    if len(arr) <= 1:
         return arr
    # get the mid point of the array
    mid = math.floor(len(arr) / 2)
    # get the left and right sides of the array and keep recusing
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # call the merge with the left and right arrays, eventually this will be the whole array sorted
    return merge(left, right)


arr = merge_sort([10, 33, 101, 5, 1])
print('Sorted array -> ', arr)

    
