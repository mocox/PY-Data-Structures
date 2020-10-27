## Radix Sort
## Big O
## Worst    Average     Best
##
##

import math

def get_digit(num, i):
    # get which position the digit is in 10, 100, 1000 etc
    return math.floor(abs(num) / math.pow(10,i)) % 10

def digit_count(num):
    # get a count of the digits
    if num == 0:
        return 1
    return math.floor(math.log10(abs(num))) + 1

def get_max_digits(nums):
    # get the maximum nuber of digits contained in the array
    maxDigits = 0
    for i in range(0, len(nums) - 1, 1):
        maxDigits = max(maxDigits, digit_count(nums[i]))
    return maxDigits

def build_holders():
    # We create a set of arrays to hold the units, 10, 100, 1000 etc
    arr = []
    for i in range(0,10):
        subArray = []
        arr.append(subArray)
    
    return arr

def spread_holders(arr):
    # like the spread operator in javascript, this concats the multiple arrays into one
    spread = []
    for i in range(0, len(arr), 1):
        spread += arr[i]
    
    return spread


def radix_sort(nums):
    # get maximum digits in list
    maxDigitCount = get_max_digits(nums)
    # loop through needed amount of times
    for k in range(0, maxDigitCount, 1):
        # now we need to build the digit holders so we can spread them later
        digitHolders = build_holders()
        # loop through all the numbers in the list
        for l in range(0, len(nums), 1):
            # get which holder the number will belong to
            digit = get_digit(nums[l], k)
            # add the item to the relevant holder
            digitHolders[digit].append(nums[l])
        # now we have done that iteration we can spread the values back into
        # nums so we can do another iteration if needed
        nums = spread_holders(digitHolders)
    
    return nums


arr = radix_sort([22,56,1,3,14,1003,99,67])
print('Sorted-> ', arr)