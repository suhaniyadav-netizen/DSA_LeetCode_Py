#BUBBLE SORT 
# Sorting algorithm that repeatedly steps through the list, compares adjacent elements and 
# swaps them if they are in the wrong order. The pass through the list is repeated until the 
# list is sorted. The algorithm gets its name from the way smaller elements "bubble" to the 
# top of the list.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)   
print("Sorted array is:", sorted_arr)



# Optimized Bubble Sort : Saves Time by stopping if the array is already sorted. 
# If no swapping occurs in a pass, the array is considered sorted and the algorithm can stop early.

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums