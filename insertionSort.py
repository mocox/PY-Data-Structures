## Insertion Sort
## Big O
## Worst   Average     Best
## O(n^2)   O(n^2)    O(n^2)
## If array is almost sorted then best case is slightly better


def insertion_sort(arr):
    # outer loop
    for i in range(1, len(arr), 1):
        current = arr[i]
        j = i - 1
        # inner loop
        while(j >= 0 and arr[j] > current):
            arr[j+1] = arr[j]
            j = j - 1
        # insert at correct position, j will be the last index found    
        arr[j+1] = current
    
    return arr


arr = insertion_sort([3,101,5,4,88,77,44,12])
print("Sorted array -> ", arr)
