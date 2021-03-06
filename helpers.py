
def swap_items(arr, index1, index2):
    # just swap the values at the given indexes
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def create_double_array(count):
    # We create a set of arrays to hold the units, 10, 100, 1000 etc
    arr = []
    for i in range(0,count):
        subArray = []
        arr.append(subArray)
    
    return arr

def spread_array_of_arrays(arr):
    # like the spread operator in javascript, this concats the multiple arrays into one
    spread = []
    for i in range(0, len(arr), 1):
        spread += arr[i]
    
    return spread