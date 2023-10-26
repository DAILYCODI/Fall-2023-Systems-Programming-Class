#!/usr/bin/env python3
# A search algorithm that finds the position of a target value within a sorted array
def binary_search(array, val):
    
    left = 0
    right = len(array) - 1
    middle = left + (right - left) // 2
    #print(f"the middle point before while loop", middle)
    while left <= right:  
        #print(left)
        #print(right)
        middle = left + (right - left) // 2 # (left + right) // 2
        #print(f"middle val in while loop: ",middle)
        if array[middle] == val: 
             return middle
        elif left >= right:
            return left
        elif array[middle] < val:
            left = middle + 1
            #print(f"left val in loop: ", left)
        elif array[middle] > val:
            right = middle - 1
            #print(f"right val in loop: ", right)
    return left

array = [n for n in range(10)]
print(f"1. ", binary_search(array, 3))
print(f"2. ", binary_search(array, 7))
print(f"3. ", binary_search(array, 11))
print(f"4. ", binary_search(array, 20))