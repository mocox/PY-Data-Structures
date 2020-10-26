## Linearly search for a number in an array
## Big O
## Best Average Worst 
## O(1)  O(n)   O(n)

def linear_search(arr, val):
    for num in arr:
        if num == val:
            return arr.index(num)    
    return -1


index = linear_search([1,2,3,10,104,8,99, 16, 44], 16)
print("index is :-> ", index)