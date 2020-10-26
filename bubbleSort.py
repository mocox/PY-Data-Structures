## Bubble Sort
## Big O
## Best Average Worst
## O(n) O(n^2)  O(n^2)
## Best case scenario if and only if array mostly sorted
## Worst case because double nested loops


def bubble_sort(arr):
    noSwaps = False
    for i in range(len(arr) - 1, 0, -1):
        noSwaps = True
        for j in range(0, i -1, 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                noSwaps = False
        if noSwaps: 
            break
    
    return arr


arr = bubble_sort([2,5,6,4,1,88,24,99])
print("Sorted array :-> ", arr)