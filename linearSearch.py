## Linearly search for a number in an array
## Best Average Worst Big O
## O(1)  O(n)   O(n)

def linear_search(arr, val):
    for num in arr:
        if num == val:
            return arr.index(num)    
    return -1


index = linear_search([1,2,3,10,53,8,99], 53)
print("index is :-> ", index)