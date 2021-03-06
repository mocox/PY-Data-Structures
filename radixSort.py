## Radix Sort
## Big O
## Worst      Average         Best
## O(n^2)    O(n log n)     O(n log n)
## Only sorts positive integers

import math
from helpers import spread_array_of_arrays, create_double_array

spread = lambda arr: spread_array_of_arrays(arr)
build_holders = lambda count: create_double_array(count)    

def get_digit(num, i):
    # get which position the digit is in units, 10, 100, 1000 etc
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

def radix_sort(nums):
    # get maximum digits in list
    maxDigitCount = get_max_digits(nums)
    # loop through needed amount of times
    for k in range(0, maxDigitCount, 1):
        # now we need to build the digit holders so we can spread them later
        digitHolders = build_holders(10)
        # loop through all the numbers in the list
        for l in range(0, len(nums), 1):
            # get which holder the number will belong to
            digit = get_digit(nums[l], k)
            # add the item to the relevant holder
            digitHolders[digit].append(nums[l])
        # now we have done that iteration we can spread the values back into
        # nums so we can do another iteration if needed
        nums = spread(digitHolders)
    
    return nums


arr = radix_sort([22,56,1,3,14,1003,99,67])
print('Sorted-> ', arr)