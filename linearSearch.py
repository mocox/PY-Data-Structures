
def search(arr, val):
    for num in arr:
        if num == val:
            return arr.index(num)    
    return -1


index = search([1,2,3,10,53,8,99], 53)
print("index is :-> ", index)