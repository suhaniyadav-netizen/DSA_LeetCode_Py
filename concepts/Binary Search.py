# FINDING MIDDLE ELEMENT 
#Binary search is an efficient algorithm for finding a specific value within a sorted list or array.
#It works on the principle of "divide and conquer" by repeatedly dividing the search space in half
#at each step, significantly reducing the number of comparisons needed. 
#Time Complexity: It has a time complexity of O(log n), 
#meaning the time it takes to search grows logarithmically as the size of the data (n) increases.

def binary(arr, key):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1
             